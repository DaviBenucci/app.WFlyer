#!/usr/bin/env python3
"""Gera visões humanas derivadas dos registros canônicos de decisão."""
from __future__ import annotations
from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
DG = ROOT / "docs/decision-governance"
reg = yaml.safe_load((DG / "decision-register.yaml").read_text(encoding="utf-8"))
ev = yaml.safe_load((DG / "evidence-register.yaml").read_text(encoding="utf-8"))
gates = yaml.safe_load((DG / "phase-decision-gates.yaml").read_text(encoding="utf-8"))

def rel_brief(d, prefix=""):
    return prefix + d["brief"].replace("docs/decision-governance/", "")

by_cat = defaultdict(list)
for d in reg["decisions"]:
    by_cat[d["category"]].append(d)

lines = ["# Registro humano de decisões", "", "> GERADO. Fonte: `decision-register.yaml`. Não editar manualmente.", "", f"Total: **{len(reg['decisions'])}**.", ""]
for cat in sorted(by_cat):
    lines += [f"## {cat}", "", "| ID | Legado | Decisão | Status | Fase/gate | Evidências |", "|---|---|---|---|---|---|"]
    for d in by_cat[cat]:
        legacy = ", ".join(d["legacy_ids"]) or "—"
        lines.append(f"| [{d['id']}]({rel_brief(d)}) | {legacy} | {d['title']} | `{d['status']}` | `{d['required_by']['phase']}:{d['required_by']['gate']}` | {', '.join(d['required_evidence_ids'])} |")
    lines.append("")
(DG / "05-registro-humano-decisoes.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")

emap = {e["id"]: e for e in ev["evidence"]}
lines = ["# Matriz de decisões e evidências", "", "> GERADO. Não editar manualmente.", "", "| Evidência | Estado | Decisões | Tipo | Devida antes de |", "|---|---|---|---|---|"]
for e in ev["evidence"]:
    lines.append(f"| `{e['id']}` | `{e['status']}` | {', '.join(e['decision_ids'])} | `{e['type']}` | `{e['due_before']}` |")
(DG / "06-matriz-decisoes-evidencias.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")

lines = ["# Matriz humana de gates por fase", "", "> GERADO. Não editar manualmente.", ""]
for p in gates["phases"]:
    lines += [f"## {p['phase_id']} — {p['title']}", ""]
    for side in ("entry", "exit"):
        g = p[side]
        lines += [f"### {side}", "", "**Decisões:**"]
        lines += [f"- `{x['decision_id']}` ≥ `{x['minimum_status']}`" for x in g["decision_requirements"]] or ["- nenhuma adicional"]
        lines += ["", "**Evidências:**"]
        lines += [f"- `{x['evidence_id']}` ≥ `{x['minimum_status']}`" for x in g["evidence_requirements"]] or ["- nenhuma adicional"]
        lines += ["", g["rule"], ""]
(DG / "07-matriz-gates-fases.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")

lines = [
    "# Decisões pendentes e governança de evidências", "",
    "> Índice humano GERADO. Fontes canônicas: `../decision-governance/*.yaml`.", "",
    "A IA não pode transformar opção em decisão sem evidência e aprovação. Fase 0 está arquivada; Fase 1 ainda não começou.", "",
    "## Registro", "", "| ID | Legado | Decisão | Estado | Fase/gate |", "|---|---|---|---|---|"
]
for d in reg["decisions"]:
    legacy = ", ".join(d["legacy_ids"]) or "—"
    brief = "../decision-governance/" + d["brief"].replace("docs/decision-governance/", "")
    lines.append(f"| [{d['id']}]({brief}) | {legacy} | {d['title']} | `{d['status']}` | `{d['required_by']['phase']}:{d['required_by']['gate']}` |")
lines += ["", "## IDs legados reservados", "", "- `PEND-026`: site institucional fora deste repositório;", "- `PEND-027`: hospedagem de clientes no planejamento empresarial privado.", "", "## Atualização", "", "```bash", "pnpm run generate:decision-docs", "pnpm run verify:repository", "```", ""]
(ROOT / "docs/00-visao-geral/09-decisoes-pendentes.md").write_text("\n".join(lines).rstrip()+"\n", encoding="utf-8")
