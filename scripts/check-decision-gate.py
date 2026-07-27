#!/usr/bin/env python3
"""Consulta se o gate documental de decisão de uma fase está liberado."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "docs/decision-governance"

def load(name):
    return yaml.safe_load((BASE / name).read_text(encoding="utf-8"))

def decision_ok(current, required, rank):
    if current == "SUPERSEDED":
        return required == "SUPERSEDED"
    return rank[current] >= rank[required]

def evidence_ok(current, required, rank):
    if current in {"REJECTED", "STALE"}:
        return False
    return rank[current] >= rank[required]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("phase")
    ap.add_argument("--gate", choices=("entry","exit"), default="entry")
    args = ap.parse_args()
    reg, ev, gates = load("decision-register.yaml"), load("evidence-register.yaml"), load("phase-decision-gates.yaml")
    dmap = {d["id"]: d for d in reg["decisions"]}
    emap = {e["id"]: e for e in ev["evidence"]}
    phase = next((p for p in gates["phases"] if p["phase_id"] == args.phase), None)
    if phase is None:
        print(f"Fase desconhecida: {args.phase}", file=sys.stderr)
        return 2
    blocked = False
    req = phase[args.gate]
    print(f"{phase['phase_id']} — {phase['title']} — {args.gate}")
    for x in req["decision_requirements"]:
        d = dmap[x["decision_id"]]
        good = decision_ok(d["status"], x["minimum_status"], gates["status_rank"])
        blocked |= not good
        print(f"[{'OK' if good else 'BLOQUEADO'}] {d['id']} {d['status']} / requerido {x['minimum_status']} — {d['title']}")
    for x in req["evidence_requirements"]:
        e = emap[x["evidence_id"]]
        good = evidence_ok(e["status"], x["minimum_status"], gates["evidence_status_rank"])
        blocked |= not good
        print(f"[{'OK' if good else 'BLOQUEADO'}] {e['id']} {e['status']} / requerido {x['minimum_status']} — {e['title']}")
    if not req["decision_requirements"] and not req["evidence_requirements"]:
        print("[OK] Sem requisito adicional de decisão; demais gates técnicos continuam obrigatórios.")
    print(req["rule"])
    return 1 if blocked else 0

if __name__ == "__main__":
    raise SystemExit(main())
