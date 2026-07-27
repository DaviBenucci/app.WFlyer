#!/usr/bin/env bash
set -uo pipefail

repo_root="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
failure_count=0

pass() {
  printf '[OK] %s\n' "$1"
}

fail() {
  printf '[FALHA] %s\n' "$1" >&2
  failure_count=$((failure_count + 1))
}

note() {
  printf '[INFO] %s\n' "$1"
}

require_command() {
  local command_name="$1"
  if command -v "$command_name" >/dev/null 2>&1; then
    pass "comando disponível: $command_name"
  else
    fail "comando ausente: $command_name"
  fi
}

expect_equal() {
  local label="$1"
  local expected="$2"
  local actual="$3"
  if [[ "$actual" == "$expected" ]]; then
    pass "$label = $actual"
  else
    fail "$label: esperado '$expected', obtido '$actual'"
  fi
}

expect_enabled_mcp() {
  local server_name="$1"
  local output
  if ! output="$(codex mcp get "$server_name" 2>&1)"; then
    fail "MCP $server_name não registrado"
    return
  fi
  if grep -Fq 'enabled: true' <<<"$output"; then
    pass "MCP habilitado: $server_name"
  else
    fail "MCP desabilitado: $server_name"
  fi
}

cd "$repo_root"

for command_name in git node npm corepack pnpm python3 uv docker openspec graphify serena codex npx; do
  require_command "$command_name"
done

if command -v python >/dev/null 2>&1; then
  note "alias python disponível: $(python --version 2>&1)"
else
  note "alias python ausente; python3 é o executável disponível"
fi

note "$(git --version)"
note "$(python3 --version)"
note "$(uv --version)"
if docker_version="$(docker version --format 'client={{.Client.Version}} server={{.Server.Version}}' 2>/dev/null)"; then
  pass "Docker acessível: $docker_version"
else
  fail 'Docker instalado, mas daemon inacessível'
fi

expected_node="$(tr -d '[:space:]' < .node-version)"
expect_equal 'Node.js fixado' "$expected_node" "$(node --version | sed 's/^v//')"
expect_equal 'npm resolvido' '11.16.0' "$(npm --version)"
expect_equal 'Corepack resolvido' '0.35.0' "$(corepack --version)"
expect_equal 'pnpm fixado' '11.15.1' "$(pnpm --version)"
expect_equal 'OpenSpec resolvido' '1.6.0' "$(openspec --version)"
expect_equal 'Graphify resolvido' 'graphify 0.9.23' "$(graphify --version 2>/dev/null | tail -n 1)"
expect_equal 'Serena resolvida' 'Serena 1.6.1' "$(serena --version)"
package_manager="$(node -e "process.stdout.write(require('./package.json').packageManager)")"
expect_equal 'packageManager' 'pnpm@11.15.1' "$package_manager"

for required_file in \
  AGENTS.md \
  docs/logs/FASE-0-PRE-INSTALACAO-2026-07-21.md \
  openspec/changes/archive/2026-07-27-bootstrap-core-foundation/proposal.md \
  openspec/changes/archive/2026-07-27-bootstrap-core-foundation/design.md \
  openspec/specs/phase-zero-foundation/spec.md \
  openspec/changes/archive/2026-07-27-bootstrap-core-foundation/tasks.md \
  .codex/skills/graphify/.graphify_version \
  .serena/project.yml \
  graphify-out/graph.json; do
  if [[ -s "$required_file" ]]; then
    pass "artefato presente: $required_file"
  else
    fail "artefato ausente ou vazio: $required_file"
  fi
done

expect_equal 'skill Graphify do projeto' '0.9.23' "$(tr -d '[:space:]' < .codex/skills/graphify/.graphify_version)"

if [[ -d openspec/changes/archive/2026-07-27-bootstrap-core-foundation && -s openspec/specs/phase-zero-foundation/spec.md ]]; then
  pass 'mudança OpenSpec da Fase 0 sincronizada e arquivada'
else
  fail 'mudança OpenSpec da Fase 0 não está sincronizada/arquivada'
fi

if node - graphify-out/graph.json <<'NODE'
const fs = require('node:fs');
const graph = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
const nodes = Array.isArray(graph.nodes) ? graph.nodes : [];
const edges = Array.isArray(graph.links)
  ? graph.links
  : (Array.isArray(graph.edges) ? graph.edges : []);
const ids = new Set(nodes.map((node) => node.id));
const invalid = edges.filter((edge) => {
  const source = edge.source ?? edge.from;
  const target = edge.target ?? edge.to;
  return !source || !target || source === target || !ids.has(source) || !ids.has(target);
});
if (nodes.length === 0 || edges.length === 0 || invalid.length > 0) process.exit(1);
console.log(`${nodes.length} nós; ${edges.length} arestas; ${invalid.length} arestas inválidas`);
NODE
then
  pass 'grafo estruturalmente íntegro'
else
  fail 'grafo ausente ou estruturalmente inválido'
fi

expect_enabled_mcp serena
expect_enabled_mcp context7

if [[ -e nx.json || -e pyproject.toml || -e uv.lock ]]; then
  fail 'artefato de fase posterior ou ecossistema Python artificial detectado'
else
  pass 'Nx e projeto Python permanecem fora da Fase 0'
fi

if node <<'NODE'
const pkg = require('./package.json');
const dependencyFields = ['dependencies', 'devDependencies', 'optionalDependencies', 'peerDependencies'];
if (dependencyFields.some((field) => pkg[field] && Object.keys(pkg[field]).length > 0)) process.exit(1);
NODE
then
  pass 'package.json sem dependências de produto'
else
  fail 'package.json contém dependências fora do escopo'
fi

if ((failure_count > 0)); then
  printf '[RESULTADO] %d verificação(ões) falharam.\n' "$failure_count" >&2
  exit 1
fi

printf '[RESULTADO] Fundação da Fase 0 verificada com sucesso.\n'
