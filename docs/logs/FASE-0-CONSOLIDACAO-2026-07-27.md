# Consolidação e fechamento documental da Fase 0

Data: 2026-07-27
Estado: correções preparadas; atualização final do Graphify e checkpoint Git devem ser executados na máquina do projeto.

## Objetivo

Eliminar inconsistências encontradas após a auditoria do repositório, sem iniciar frontend, backend, worker, banco ou motor musical.

## Correções aplicadas

1. `README.md` passou a refletir o estado real: Fase 0 concluída, Fase 1 não iniciada e ausência de código funcional.
2. `TREE.md` passou a representar a árvore atual e a arquitetura física planejada.
3. `MANIFESTO_VALIDACAO.md` passou a registrar escopo, método e resultados reproduzíveis.
4. `AGENTS.md` incorporou OpenSpec, Graphify, Serena, Context7, gates musicais, frontend e economia segura de tokens.
5. `openspec/config.yaml` recebeu contexto e regras do W_Flyer.
6. O hook do Graphify deixou de conter caminho absoluto pessoal.
7. Serena recebeu contexto inicial e exclusões; `languages` permanece vazio até existir código analisável.
8. A mudança `bootstrap-core-foundation` foi sincronizada em `openspec/specs/phase-zero-foundation/` e arquivada.
9. A arquitetura física adotou pacotes Python internos compartilhados por API e worker em `packages/python/`.
10. Referências visuais de capabilities futuras passaram a usar `status: reference`, `capability_status: disabled` e gate explícito.
11. A documentação de bootstrap separou a Fase 0 de agentes da Fase 1 de produto.
12. A validação foi separada em repositório portável e toolchain local do agente.

## Decisão arquitetural fechada

API e worker não manterão cópias próprias do domínio musical. Ambos dependerão dos pacotes internos:

```text
packages/python/music-domain
packages/python/musicxml
packages/python/instrument-catalog
packages/python/transposition-engine
packages/python/music-verifier
```

Isso está registrado no ADR-051 e em `docs/backend/13-estrutura-pastas.md`.

## Referências visuais

A consolidação não aprova pixels ou composição em nome do product owner. Ela apenas impede que referências futuras autorizem implementação prematura.

Continuam aguardando aprovação humana:

- Home e workspace do Core;
- processing e upload error;
- instrument picker e processing timeline;
- demais baselines visuais.

Melodia, harmonização, ensaio, ensemble, tocabilidade, playback, Musical Diff visual e Ink Transfer de produção permanecem referências futuras desabilitadas.

## Graphify

O `graph.json` e o `GRAPH_REPORT.md` presentes no pacote concordam em:

```text
3.076 nós
2.890 relações
292 comunidades
```

Os arquivos `.graphify_health*.json` registram uma fotografia intermediária anterior, com 3.043/2.858. Eles são históricos e não devem ser usados para determinar frescor.

Como esta consolidação altera documentação e configuração, o grafo deve ser atualizado na máquina do projeto antes do checkpoint Git:

```bash
graphify update .
pnpm run verify:repository
```

## Passos finais na máquina do projeto

```bash
graphify update .
pnpm run verify:repository
pnpm run verify:agent-toolchain
git diff --check
git add -A
git commit -m "docs: consolidate and close phase 0"
git tag phase-0-complete
```

Não executar esses comandos se algum gate falhar. Não criar a mudança da Fase 1 antes da aprovação do usuário.

## Pendências preservadas

- versão Python do produto;
- typechecker Python;
- cache remoto Nx;
- aprovação humana dos golden examples;
- todas as decisões `PEND-*` relacionadas a capabilities avançadas;
- atualização efetiva do Graphify e criação do checkpoint Git na máquina do usuário.
