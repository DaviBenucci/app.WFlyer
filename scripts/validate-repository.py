#!/usr/bin/env python3
"""Validação portável dos artefatos versionados do W_Flyer."""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path
from typing import Iterable

try:
    import yaml
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyYAML é necessário para validar os arquivos YAML.") from exc

try:
    from jsonschema import Draft202012Validator
except ImportError as exc:  # pragma: no cover
    raise SystemExit("jsonschema é necessário para validar os contratos estruturados.") from exc

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "node_modules", ".venv", "venv", "__pycache__", "graphify-out"}


def fail(message: str) -> None:
    print(f"[FALHA] {message}", file=sys.stderr)
    FAILURES.append(message)


def ok(message: str) -> None:
    print(f"[OK] {message}")


def tracked_files() -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
        return [ROOT / raw.decode("utf-8") for raw in result.stdout.split(b"\0") if raw]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [
            path
            for path in ROOT.rglob("*")
            if path.is_file() and not any(part in EXCLUDED_PARTS for part in path.parts)
        ]


def relevant(paths: Iterable[Path]) -> list[Path]:
    return [
        path
        for path in paths
        if path.exists()
        and not any(part in EXCLUDED_PARTS for part in path.relative_to(ROOT).parts)
    ]


def validate_required() -> None:
    required = [
        "README.md",
        "TREE.md",
        "MANIFESTO_VALIDACAO.md",
        "AGENTS.md",
        "docs/00-visao-geral/00-indice.md",
        "docs/00-visao-geral/02-roadmap-fases.md",
        "docs/00-visao-geral/08-hierarquia-documental.md",
        "docs/00-visao-geral/09-decisoes-pendentes.md",
        "docs/decision-governance/README.md",
        "docs/decision-governance/00-analise-situacao-atual.md",
        "docs/decision-governance/01-papeis-aprovacoes.md",
        "docs/decision-governance/02-fluxo-decisao.md",
        "docs/decision-governance/03-evidencias-freshness.md",
        "docs/decision-governance/04-gates-fases-e-ia.md",
        "docs/decision-governance/05-registro-humano-decisoes.md",
        "docs/decision-governance/06-matriz-decisoes-evidencias.md",
        "docs/decision-governance/07-matriz-gates-fases.md",
        "docs/decision-governance/08-migracao-ids-legados.md",
        "docs/decision-governance/decision-register.yaml",
        "docs/decision-governance/decision-register.schema.json",
        "docs/decision-governance/evidence-register.yaml",
        "docs/decision-governance/evidence-register.schema.json",
        "docs/decision-governance/phase-decision-gates.yaml",
        "docs/decision-governance/phase-decision-gates.schema.json",
        "docs/decision-governance/decisions/README.md",
        "docs/00-visao-geral/20-explicacao-completa-nao-tecnica.md",
        "docs/00-visao-geral/21-visao-tecnica-completa.md",
        "docs/backend/13-estrutura-pastas.md",
        "brand/README.md",
        "brand/brand-manifest.yaml",
        "brand/brand-manifest.schema.json",
        "brand/guidelines/brand-guidelines.md",
        "docs/brand/README.md",
        "docs/brand/01-briefing-identidade.md",
        "docs/brand/02-governanca-assets.md",
        "docs/brand/03-checklist-aprovacao-logo.md",
        "docs/billing/01-comparativo-stripe-mercado-pago.md",
        "docs/billing/08-parametros-precos-planos.md",
        "docs/billing/09-sistema-creditos-detalhado.md",
        "docs/billing/10-formulario-decisao-precos-creditos.md",
        "docs/billing/pricing-config.template.yaml",
        "docs/billing/pricing-config.schema.json",
        "docs/policies/00-central-de-politicas.md",
        "docs/policies/01-termos-de-uso.md",
        "docs/policies/02-politica-privacidade.md",
        "docs/policies/03-politica-cookies.md",
        "docs/policies/04-politica-pagamentos-creditos-assinaturas.md",
        "docs/policies/05-politica-cancelamento-reembolso.md",
        "docs/policies/06-politica-direitos-autorais-conteudo.md",
        "docs/policies/07-politica-uso-aceitavel.md",
        "docs/policies/08-politica-retencao-exclusao.md",
        "docs/policies/09-politica-suporte-disponibilidade.md",
        "docs/policies/10-politica-seguranca-incidentes.md",
        "docs/policies/policy-manifest.yaml",
        "docs/policies/policy-manifest.schema.json",
        "docs/pages/18-central-politicas.md",
        "docs/fiscal/01-nfse-arquitetura.md",
        "docs/infrastructure/02-arquitetura-aws-producao.md",
        "docs/operations/README.md",
        "docs/design-reference/reference-manifest.yaml",
        "openspec/config.yaml",
        "openspec/specs/phase-zero-foundation/spec.md",
        "openspec/specs/business-launch-readiness/spec.md",
        "openspec/specs/pricing-credits-policies/spec.md",
        "openspec/specs/brand-identity-foundation/spec.md",
        "openspec/specs/decision-governance/spec.md",
        "scripts/generate-decision-docs.py",
        "scripts/check-decision-gate.py",
        "openspec/changes/archive/2026-07-27-bootstrap-core-foundation/tasks.md",
        "openspec/changes/archive/2026-07-27-document-business-launch-readiness/tasks.md",
        "openspec/changes/archive/2026-07-27-document-pricing-credits-policies/tasks.md",
        "openspec/changes/archive/2026-07-27-document-brand-identity-foundation/tasks.md",
        "openspec/changes/archive/2026-07-27-document-decision-governance/tasks.md",
    ]
    missing = [item for item in required if not (ROOT / item).is_file()]
    if missing:
        fail("arquivos obrigatórios ausentes: " + ", ".join(missing))
    else:
        ok(f"{len(required)} arquivos obrigatórios presentes")


def validate_json_yaml(paths: list[Path]) -> tuple[int, int]:
    json_count = 0
    yaml_count = 0
    for path in paths:
        rel = path.relative_to(ROOT)
        if "graphify-out" in rel.parts:
            continue
        try:
            if path.suffix == ".json":
                json.loads(path.read_text(encoding="utf-8"))
                json_count += 1
            elif path.suffix in {".yaml", ".yml"}:
                yaml.safe_load(path.read_text(encoding="utf-8"))
                yaml_count += 1
        except Exception as exc:  # noqa: BLE001
            fail(f"arquivo estruturado inválido: {rel}: {exc}")
    ok(f"JSON parseados: {json_count}")
    ok(f"YAML parseados: {yaml_count}")
    return json_count, yaml_count


def validate_json_schemas() -> int:
    design = ROOT / "docs/design-reference"
    pairs: list[tuple[Path, Path]] = [
        (design / "reference-manifest.yaml", design / "schemas/reference-manifest.schema.json"),
        (design / "baseline-manifest.json", design / "schemas/baseline-manifest.schema.json"),
        (design / "motion/ink-transfer/specification.yaml", design / "schemas/motion-spec.schema.json"),
        (ROOT / "docs/implementacao/toolchain-manifest.yaml", ROOT / "docs/implementacao/toolchain-manifest.schema.json"),
        (ROOT / "docs/qa/pre-mortem-register.yaml", ROOT / "docs/qa/pre-mortem-register.schema.json"),
        (ROOT / "docs/riscos/failure-mode-catalog.yaml", ROOT / "docs/riscos/failure-mode-catalog.schema.json"),
        (ROOT / "docs/billing/pricing-config.template.yaml", ROOT / "docs/billing/pricing-config.schema.json"),
        (ROOT / "docs/policies/policy-manifest.yaml", ROOT / "docs/policies/policy-manifest.schema.json"),
        (ROOT / "brand/brand-manifest.yaml", ROOT / "brand/brand-manifest.schema.json"),
        (ROOT / "docs/decision-governance/decision-register.yaml", ROOT / "docs/decision-governance/decision-register.schema.json"),
        (ROOT / "docs/decision-governance/evidence-register.yaml", ROOT / "docs/decision-governance/evidence-register.schema.json"),
        (ROOT / "docs/decision-governance/phase-decision-gates.yaml", ROOT / "docs/decision-governance/phase-decision-gates.schema.json"),
    ]
    pairs.extend((path, design / "schemas/component-spec.schema.json") for path in (design / "golden-components").glob("*/specification.yaml"))
    pairs.extend((path, design / "schemas/page-spec.schema.json") for path in (design / "golden-pages").glob("*/specification.yaml"))
    count = 0
    for data_path, schema_path in pairs:
        data = json.loads(data_path.read_text(encoding="utf-8")) if data_path.suffix == ".json" else yaml.safe_load(data_path.read_text(encoding="utf-8"))
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        errors = list(Draft202012Validator(schema).iter_errors(data))
        if errors:
            first = errors[0]
            fail(f"schema inválido: {data_path.relative_to(ROOT)} em {list(first.path)}: {first.message}")
        count += 1
    ok(f"contratos JSON Schema verificados: {count}")
    return count


LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def validate_markdown_links(paths: list[Path]) -> int:
    checked = 0
    for path in paths:
        if path.suffix.lower() != ".md" or "graphify-out" in path.relative_to(ROOT).parts:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for target in LINK_RE.findall(text):
            target = target.strip().split(maxsplit=1)[0].strip("<>")
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            target = target.split("#", 1)[0]
            if not target:
                continue
            checked += 1
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(ROOT.resolve())
            except ValueError:
                fail(f"link sai da raiz do repositório: {path.relative_to(ROOT)} -> {target}")
                continue
            if not resolved.exists():
                fail(f"link relativo quebrado: {path.relative_to(ROOT)} -> {target}")
    ok(f"links Markdown relativos verificados: {checked}")
    return checked


def validate_design_manifest() -> None:
    path = ROOT / "docs/design-reference/reference-manifest.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    refs = data.get("references", {})
    missing: list[str] = []
    for ref_id, ref in refs.items():
        for key in ("specification", "prototype"):
            value = ref.get(key)
            if value and not (path.parent / value).is_file():
                missing.append(f"{ref_id}:{key}:{value}")
        for key in ("screenshots", "baselines"):
            for value in ref.get(key, []) or []:
                if not (path.parent / value).is_file():
                    missing.append(f"{ref_id}:{key}:{value}")
        if ref.get("capability_status") == "disabled" and ref.get("status") != "reference":
            fail(f"referência futura deve usar status=reference: {ref_id}")
    if missing:
        fail("paths ausentes no manifesto visual: " + ", ".join(missing))
    else:
        ok(f"manifesto visual: {len(refs)} referências com paths existentes")


def validate_brand_state() -> None:
    path = ROOT / "brand/brand-manifest.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    status = data.get("status")
    identity = data.get("identity", {})
    temp = data.get("temporary_policy", {})
    if status == "pending":
        if any(value is not None for value in identity.values()):
            fail("brand pendente contém asset aprovado")
        elif temp.get("mode") != "text_only":
            fail("brand pendente deve usar mode=text_only")
        elif temp.get("allow_old_logo") is not False:
            fail("brand pendente deve bloquear logo antiga")
        else:
            ok("identidade visual pendente e limitada a texto")
    legacy = ROOT / "docs/design-reference/Logo"
    if legacy.exists() and any(legacy.rglob("*")):
        fail("diretório legado de logo ainda contém arquivos")
    else:
        ok("nenhum asset legado de logo presente")
    for html in (ROOT / "docs/design-reference/prototypes").glob("*.html"):
        text = html.read_text(encoding="utf-8", errors="replace")
        if "brand-mark" in text:
            fail(f"protótipo ainda usa marca provisória: {html.relative_to(ROOT)}")


def validate_hooks() -> None:
    path = ROOT / ".codex/hooks.json"
    data = json.loads(path.read_text(encoding="utf-8"))
    blob = json.dumps(data)
    if re.search(r'/(home|Users)/[^" ]+', blob):
        fail(".codex/hooks.json contém caminho absoluto pessoal")
    elif "graphify hook-check" not in blob:
        fail("hook portátil do Graphify não encontrado")
    else:
        ok("hook do Graphify é portátil")


def validate_openspec_state() -> None:
    changes = [
        (
            ROOT / "openspec/changes/bootstrap-core-foundation",
            ROOT / "openspec/changes/archive/2026-07-27-bootstrap-core-foundation",
            ROOT / "openspec/specs/phase-zero-foundation/spec.md",
            "bootstrap-core-foundation",
        ),
        (
            ROOT / "openspec/changes/document-business-launch-readiness",
            ROOT / "openspec/changes/archive/2026-07-27-document-business-launch-readiness",
            ROOT / "openspec/specs/business-launch-readiness/spec.md",
            "document-business-launch-readiness",
        ),
        (
            ROOT / "openspec/changes/document-pricing-credits-policies",
            ROOT / "openspec/changes/archive/2026-07-27-document-pricing-credits-policies",
            ROOT / "openspec/specs/pricing-credits-policies/spec.md",
            "document-pricing-credits-policies",
        ),
        (
            ROOT / "openspec/changes/document-brand-identity-foundation",
            ROOT / "openspec/changes/archive/2026-07-27-document-brand-identity-foundation",
            ROOT / "openspec/specs/brand-identity-foundation/spec.md",
            "document-brand-identity-foundation",
        ),
        (
            ROOT / "openspec/changes/document-decision-governance",
            ROOT / "openspec/changes/archive/2026-07-27-document-decision-governance",
            ROOT / "openspec/specs/decision-governance/spec.md",
            "document-decision-governance",
        ),
    ]
    for active, archived, main_spec, name in changes:
        if active.exists():
            fail(f"mudança {name} ainda está ativa")
            continue
        if not archived.is_dir() or not main_spec.is_file():
            fail(f"mudança {name} não está sincronizada e arquivada corretamente")
            continue
        tasks = (archived / "tasks.md").read_text(encoding="utf-8")
        if "- [ ]" in tasks:
            fail(f"mudança arquivada {name} contém tarefas incompletas")
        else:
            ok(f"OpenSpec {name} sincronizado e arquivado")


def validate_decision_governance() -> tuple[int, int, int]:
    base = ROOT / "docs/decision-governance"
    register = yaml.safe_load((base / "decision-register.yaml").read_text(encoding="utf-8"))
    evidence_doc = yaml.safe_load((base / "evidence-register.yaml").read_text(encoding="utf-8"))
    gates = yaml.safe_load((base / "phase-decision-gates.yaml").read_text(encoding="utf-8"))

    decisions = register.get("decisions", [])
    evidence = evidence_doc.get("evidence", [])
    phases = gates.get("phases", [])
    dmap = {item.get("id"): item for item in decisions}
    emap = {item.get("id"): item for item in evidence}
    pmap = {item.get("phase_id"): item for item in phases}

    if len(dmap) != len(decisions):
        fail("decision-register contém IDs DEC duplicados")
    if len(emap) != len(evidence):
        fail("evidence-register contém IDs EVID duplicados")
    if len(pmap) != len(phases):
        fail("phase-decision-gates contém phase_id duplicado")

    legacy_ids: list[str] = []
    expected_packages: set[str] = set()
    package_files = {
        "00-decision-brief.md",
        "01-requirements.md",
        "02-options.md",
        "03-experiment-plan.md",
        "04-evidence/README.md",
        "05-comparison.md",
        "06-risk-analysis.md",
        "07-decision-record.md",
        "08-validation.md",
    }
    lifecycle = register.get("lifecycle_order", [])
    status_rank = gates.get("status_rank", {})
    evidence_rank = gates.get("evidence_status_rank", {})

    if status_rank.get("SUPERSEDED", 0) >= status_rank.get("DECIDED", 0):
        fail("SUPERSEDED não pode satisfazer gate ativo por rank")
    for bad in ("REJECTED", "STALE"):
        if evidence_rank.get(bad, 0) >= evidence_rank.get("ACCEPTED", 0):
            fail(f"{bad} não pode satisfazer gate ACCEPTED por rank")

    for decision in decisions:
        did = decision["id"]
        legacy_ids.extend(decision.get("legacy_ids", []))
        phase_id = decision["required_by"]["phase"]
        if phase_id not in pmap:
            fail(f"{did} referencia fase sem gate: {phase_id}")
        for evid in decision.get("required_evidence_ids", []):
            if evid not in emap:
                fail(f"{did} referencia evidência ausente: {evid}")
            elif did not in emap[evid].get("decision_ids", []):
                fail(f"{did}/{evid} sem referência bidirecional")
        brief = ROOT / decision["brief"]
        if not brief.is_file():
            fail(f"brief ausente para {did}: {decision['brief']}")
            continue
        package = brief.parent
        expected_packages.add(package.name)
        for rel in package_files:
            if not (package / rel).is_file():
                fail(f"pacote incompleto {did}: {rel}")
        if decision["status"] in {"DECIDED", "IMPLEMENTED", "VALIDATED"}:
            record = decision.get("decision_record")
            if not record or not (ROOT / record).is_file():
                fail(f"{did} está {decision['status']} sem decision_record existente")
            if not decision.get("implementation_authorized"):
                fail(f"{did} está {decision['status']} mas implementation_authorized=false")
        if decision["status"] in {"IMPLEMENTED", "VALIDATED"}:
            change = decision.get("openspec_change")
            if not change or not (ROOT / change).exists():
                fail(f"{did} está {decision['status']} sem OpenSpec existente")
        if decision["status"] == "VALIDATED":
            for evid in decision.get("required_evidence_ids", []):
                if emap[evid]["status"] != "ACCEPTED":
                    fail(f"{did} VALIDATED com evidência não aceita: {evid}")
        if decision["status"] not in lifecycle:
            fail(f"status desconhecido em {did}: {decision['status']}")

    if len(set(legacy_ids)) != len(legacy_ids):
        fail("IDs PEND legados foram reutilizados")
    reserved = register.get("legacy_id_policy", {}).get("reserved_legacy_ids", {})
    for legacy in ("PEND-026", "PEND-027"):
        if legacy not in reserved:
            fail(f"ID legado reservado sem justificativa: {legacy}")
        if legacy in legacy_ids:
            fail(f"ID legado reservado foi reutilizado: {legacy}")

    packages_root = base / "decisions"
    actual_packages = {path.name for path in packages_root.glob("DEC-*") if path.is_dir()}
    extras = sorted(actual_packages - expected_packages)
    missing = sorted(expected_packages - actual_packages)
    if extras:
        fail("pacotes DEC sem registro: " + ", ".join(extras))
    if missing:
        fail("registros DEC sem pacote: " + ", ".join(missing))

    for item in evidence:
        eid = item["id"]
        for did in item.get("decision_ids", []):
            if did not in dmap:
                fail(f"{eid} referencia decisão ausente: {did}")
            elif eid not in dmap[did].get("required_evidence_ids", []):
                fail(f"{eid}/{did} sem referência bidirecional")
        if item["status"] == "ACCEPTED":
            required = ("artifact_paths", "review_record", "source_commit", "environment", "collected_at")
            for field in required:
                if not item.get(field):
                    fail(f"{eid} ACCEPTED sem {field}")
            for artifact in item.get("artifact_paths", []):
                if not (ROOT / artifact).exists():
                    fail(f"{eid} aponta artefato inexistente: {artifact}")
            review = item.get("review_record")
            if review and not (ROOT / review).is_file():
                fail(f"{eid} aponta review_record inexistente: {review}")
        if item["status"] == "REJECTED" and not item.get("review_record"):
            fail(f"{eid} REJECTED sem review_record")

    valid_decision_statuses = set(status_rank)
    valid_evidence_statuses = set(evidence_rank)
    for phase in phases:
        for side in ("entry", "exit"):
            gate = phase[side]
            for req in gate.get("decision_requirements", []):
                if req["decision_id"] not in dmap:
                    fail(f"gate {phase['phase_id']}:{side} referencia decisão ausente: {req['decision_id']}")
                if req["minimum_status"] not in valid_decision_statuses:
                    fail(f"gate {phase['phase_id']}:{side} usa status DEC inválido")
            for req in gate.get("evidence_requirements", []):
                if req["evidence_id"] not in emap:
                    fail(f"gate {phase['phase_id']}:{side} referencia evidência ausente: {req['evidence_id']}")
                if req["minimum_status"] not in valid_evidence_statuses:
                    fail(f"gate {phase['phase_id']}:{side} usa status EVID inválido")

    optional = {"DEC-035", "DEC-036", "DEC-037", "DEC-038", "DEC-040"}
    for phase in phases:
        if phase["phase_id"].startswith("CORE-"):
            referenced = {
                req["decision_id"]
                for side in ("entry", "exit")
                for req in phase[side].get("decision_requirements", [])
            }
            bad = referenced & optional
            if bad:
                fail(f"ferramenta opcional bloqueia Core em {phase['phase_id']}: {', '.join(sorted(bad))}")

    generated = [
        base / "05-registro-humano-decisoes.md",
        base / "06-matriz-decisoes-evidencias.md",
        base / "07-matriz-gates-fases.md",
        ROOT / "docs/00-visao-geral/09-decisoes-pendentes.md",
    ]
    for generated_path in generated:
        if not generated_path.is_file():
            fail(f"visão gerada ausente: {generated_path.relative_to(ROOT)}")
            continue
        body = generated_path.read_text(encoding="utf-8", errors="replace")
        if generated_path.name in {"05-registro-humano-decisoes.md", "09-decisoes-pendentes.md"}:
            absent = [did for did in dmap if did not in body]
            if absent:
                fail(f"visão gerada desatualizada {generated_path.relative_to(ROOT)}: {absent[:5]}")

    if not FAILURES:
        ok(f"governança: {len(decisions)} decisões; {len(evidence)} evidências; {len(phases)} registros de fase/trilha; {len(phases) * 2} lados de gate")
    return len(decisions), len(evidence), len(phases)


def validate_policy_manifest() -> None:
    path = ROOT / "docs/policies/policy-manifest.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    policies = data.get("policies", {})
    missing: list[str] = []
    for policy_id, policy in policies.items():
        source = policy.get("source")
        if not source or not (path.parent / source).is_file():
            missing.append(f"{policy_id}:{source}")
        if data.get("status") != "approved" and policy.get("legal_review") == "approved":
            fail(f"política aprovada dentro de manifesto não aprovado: {policy_id}")
    if missing:
        fail("fontes ausentes no manifesto de políticas: " + ", ".join(missing))
    else:
        ok(f"manifesto de políticas: {len(policies)} documentos com fontes existentes")


def validate_pricing_template() -> None:
    path = ROOT / "docs/billing/pricing-config.template.yaml"
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if data.get("status") == "approved":
        unresolved = []
        def walk(value, prefix=""):
            if value is None:
                unresolved.append(prefix)
            elif isinstance(value, dict):
                for key, child in value.items():
                    walk(child, f"{prefix}.{key}" if prefix else key)
            elif isinstance(value, list):
                for index, child in enumerate(value):
                    walk(child, f"{prefix}[{index}]")
        walk(data)
        if unresolved:
            fail("catálogo de preços aprovado contém campos null: " + ", ".join(unresolved[:10]))
        elif not all(data.get("approval_gates", {}).values()):
            fail("catálogo de preços aprovado possui gates falsos")
        else:
            ok("catálogo de preços aprovado sem pendências")
    else:
        ok("catálogo de preços permanece explicitamente pendente")


def validate_graphify() -> tuple[int, int]:
    graph_path = ROOT / "graphify-out/graph.json"
    report_path = ROOT / "graphify-out/GRAPH_REPORT.md"
    if not graph_path.is_file() or not report_path.is_file():
        print("[AVISO] Graphify não está presente; validação estrutural ignorada")
        return 0, 0
    graph = json.loads(graph_path.read_text(encoding="utf-8"))
    nodes = graph.get("nodes", [])
    edges = graph.get("links", graph.get("edges", []))
    ids = {node.get("id") for node in nodes}
    invalid = []
    for edge in edges:
        source = edge.get("source", edge.get("from"))
        target = edge.get("target", edge.get("to"))
        if not source or not target or source == target or source not in ids or target not in ids:
            invalid.append(edge)
    if not nodes or not edges or invalid:
        fail(f"grafo inválido: nodes={len(nodes)} edges={len(edges)} invalid={len(invalid)}")
    else:
        ok(f"grafo estruturalmente íntegro: {len(nodes)} nós; {len(edges)} relações")
    report = report_path.read_text(encoding="utf-8", errors="replace")
    summary = re.search(r"- (\d+) nodes · (\d+) edges", report)
    if summary and (int(summary.group(1)), int(summary.group(2))) != (len(nodes), len(edges)):
        fail("GRAPH_REPORT.md diverge de graph.json")
    else:
        ok("GRAPH_REPORT.md coerente com graph.json")
    return len(nodes), len(edges)


def validate_no_tracked_generated(paths: list[Path]) -> None:
    bad = [
        str(path.relative_to(ROOT))
        for path in paths
        if any(part in {"node_modules", ".venv", "venv", "__pycache__"} for part in path.relative_to(ROOT).parts)
    ]
    if bad:
        fail("artefatos gerados versionados: " + ", ".join(bad[:10]))
    else:
        ok("nenhuma dependência ou ambiente gerado está versionado")


FAILURES: list[str] = []


def main() -> int:
    paths = relevant(tracked_files())
    validate_required()
    json_count, yaml_count = validate_json_yaml(paths)
    schema_count = validate_json_schemas()
    links = validate_markdown_links(paths)
    validate_design_manifest()
    validate_policy_manifest()
    validate_pricing_template()
    validate_brand_state()
    validate_hooks()
    validate_openspec_state()
    decision_count, evidence_count, phase_gate_count = validate_decision_governance()
    graph_nodes, graph_edges = validate_graphify()
    validate_no_tracked_generated(paths)

    md_count = sum(path.suffix.lower() == ".md" for path in paths)
    docs_files = sum("docs" in path.relative_to(ROOT).parts[:1] for path in paths)
    print("[INFO] " + json.dumps({
        "tracked_files": len(paths),
        "markdown_files": md_count,
        "docs_files": docs_files,
        "json_files_parsed": json_count,
        "yaml_files_parsed": yaml_count,
        "json_schema_contracts": schema_count,
        "markdown_links_checked": links,
        "decision_count": decision_count,
        "evidence_count": evidence_count,
        "phase_gate_count": phase_gate_count,
        "gate_side_count": phase_gate_count * 2,
        "graph_nodes": graph_nodes,
        "graph_edges": graph_edges,
        "failures": len(FAILURES),
    }, ensure_ascii=False))

    if FAILURES:
        print(f"[RESULTADO] {len(FAILURES)} falha(s).", file=sys.stderr)
        return 1
    print("[RESULTADO] Repositório validado com sucesso.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
