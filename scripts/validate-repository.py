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
        "docs/00-visao-geral/20-explicacao-completa-nao-tecnica.md",
        "docs/00-visao-geral/21-visao-tecnica-completa.md",
        "docs/backend/13-estrutura-pastas.md",
        "docs/design-reference/reference-manifest.yaml",
        "openspec/config.yaml",
        "openspec/specs/phase-zero-foundation/spec.md",
        "openspec/changes/archive/2026-07-27-bootstrap-core-foundation/tasks.md",
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
    active = ROOT / "openspec/changes/bootstrap-core-foundation"
    archived = ROOT / "openspec/changes/archive/2026-07-27-bootstrap-core-foundation"
    main_spec = ROOT / "openspec/specs/phase-zero-foundation/spec.md"
    if active.exists():
        fail("mudança bootstrap-core-foundation ainda está ativa")
    elif not archived.is_dir() or not main_spec.is_file():
        fail("Fase 0 não está sincronizada e arquivada corretamente")
    else:
        tasks = (archived / "tasks.md").read_text(encoding="utf-8")
        if "- [ ]" in tasks:
            fail("arquivo arquivado contém tarefas incompletas")
        else:
            ok("OpenSpec da Fase 0 sincronizado e arquivado")


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
    validate_hooks()
    validate_openspec_state()
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
