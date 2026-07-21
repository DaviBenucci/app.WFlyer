# Relatório final — bootstrap e Fase 0

> Data: 2026-07-21. Escopo: exclusivamente bootstrap, governança da IA e fundação da Fase 0. Branch: `main`. HEAD observado: `c99beed`.

## Resultado executivo

| Item | Resultado |
|---|---|
| Status da fase | `CONCLUIDA` com ressalvas documentadas |
| Estado do gate | aprovado para encerrar a Fase 0; não libera a Fase 1 |
| OpenSpec | 1.6.0; mudança `bootstrap-core-foundation`; 4/4 artefatos válidos |
| Graphify | 0.9.23; 3.043 nós, 2.858 arestas, 292 comunidades; integridade aprovada |
| Serena | 1.6.1; projeto ativado; MCP habilitado; sem arquivos analisáveis ainda |
| Context7 | setup CLI 0.5.5; MCP OAuth habilitado e consulta funcional aprovada |
| Workspace | privado, sem dependências; Node 24.18.0 e pnpm 11.15.1 fixados |
| Testes de produto | zero coletores configurados; baseline zero registrado sem simulação |
| Ferramentas proibidas | nenhuma instalada |
| Funcionalidades de produto | nenhuma implementada |
| `sudo`/pacotes do sistema | não utilizados |
| Próxima fase desbloqueada | **não** |

## Ordem executada

1. Ambiente, Git, sistema e ferramentas-base foram inventariados.
2. A leitura inicial foi limitada aos documentos de entrada autorizados.
3. O relatório de pré-instalação foi gravado antes das instalações.
4. OpenSpec, Graphify, Serena e Context7 foram instalados/configurados nessa ordem.
5. OpenSpec foi inicializado e a mudança `bootstrap-core-foundation` foi criada.
6. O primeiro grafo consistente foi recuperado após o reboot, consultado e validado.
7. Serena foi ativada e os dois MCPs foram verificados no Codex.
8. Proposta, design, especificação e plano detalhado da Fase 0 foram criados antes do workspace.
9. O workspace mínimo, sem frameworks, foi criado e verificado.
10. O Graphify foi atualizado novamente, incluindo a cobertura residual de YAML, HTML e imagens.
11. Logs, rollback e gate foram consolidados; nenhuma tarefa da Fase 1 foi iniciada.

## Ambiente final

| Item | Versão/estado |
|---|---|
| Diretório e raiz Git | `/home/davi-benucci/Área de trabalho/app.WFlyer` |
| Branch | `main`, acompanhando `origin/main` |
| Sistema | Ubuntu 26.04 LTS, kernel 7.0.0-28, x86_64 |
| Git | 2.53.0 |
| Node.js | 24.18.0 |
| npm | 11.16.0 |
| Corepack | 0.35.0 |
| pnpm | 11.15.1 |
| Python | `python` ausente; `python3` 3.14.4 |
| uv | 0.11.29 |
| Docker | cliente 29.6.2; servidor 29.6.1; daemon acessível após reativação do serviço de usuário |
| Codex CLI | 0.145.0-alpha.18 |

O baseline anterior à instalação permanece em `FASE-0-PRE-INSTALACAO-2026-07-21.md`.

## Ferramentas instaladas e escopos

| Ferramenta | Versão | Instalação | Integração/projeto |
|---|---:|---|---|
| pnpm | 11.15.1 | shim Corepack em `~/.local/bin` | fixado em `packageManager` |
| OpenSpec | 1.6.0 | pacote global pnpm do usuário | `openspec/` e seis skills Codex no projeto |
| Graphify | 0.9.23 | `uv tool`, requisito exato `graphifyy==0.9.23` | skill Codex global e do projeto em 0.9.23; saídas locais em `graphify-out/` |
| Serena | 1.6.1 | `uv tool`, requisito exato `serena-agent==1.6.1`, Python gerenciado 3.13.14 | MCP global do Codex, registro global Serena e `.serena/project.yml` |
| Context7 | 0.5.5 | setup executado por `npx` fixado; não há pacote CLI global permanente | MCP OAuth, regra global Codex e skill universal do usuário |

### Alterações globais do usuário

- `~/.local/bin/` e o armazenamento global do pnpm para pnpm/OpenSpec;
- `~/.local/share/uv/tools/graphifyy/` e `~/.local/share/uv/tools/serena-agent/`;
- `~/.codex/config.toml` para os MCPs Serena e Context7;
- `~/.codex/skills/graphify/` para a skill global alinhada;
- `~/.codex/AGENTS.md` e `~/.agents/skills/context7-mcp/` para Context7;
- `~/.serena/serena_config.yml` para o registro do projeto;
- cache do npm utilizado pelo setup `ctx7@0.5.5` e credencial OAuth mantida pelo Codex.

Nenhum arquivo global contendo segredo foi copiado para o repositório.

## Versões e lockfiles

- `.node-version` fixa Node.js 24.18.0.
- `package.json` fixa `pnpm@11.15.1` e não declara dependências.
- `pnpm-lock.yaml` usa lockfile v9 e possui importador raiz vazio; SHA-256 verificado: `17c814b167307942d3609c7b9d916ceddb85839573ab39baa114e30edb132a1a`.
- O lock global do pnpm registra `@fission-ai/openspec@1.6.0`.
- Os receipts do `uv tool` registram `graphifyy==0.9.23` e `serena-agent==1.6.1`.
- Context7 foi sempre invocado como `ctx7@0.5.5`; a integração é persistente, mas o pacote permanece apenas no cache do `npx`.
- Não foi criado `uv.lock`: ainda não existe projeto Python nem versão de backend aprovada. Criá-lo vazio produziria um ecossistema fictício.
- Não foi criado `nx.json`: o manifesto vinculante classifica Nx como Fase 1.

## Arquivos criados e modificados

### Modificados e versionáveis

- `AGENTS.md`;
- `.codex/skills/graphify/.graphify_version`;
- `.codex/skills/graphify/SKILL.md`;
- `.codex/skills/graphify/references/update.md`;
- `docs/logs/CHANGELOG.md`;
- `docs/logs/IMPLEMENTATION_LOG.md`;
- `docs/logs/TEST_LOG.md`.

### Criados e versionáveis

- `.node-version`;
- `package.json`;
- `pnpm-lock.yaml`;
- `scripts/verify-toolchain.sh`;
- `.serena/.gitignore` e `.serena/project.yml`;
- `docs/logs/FASE-0-PRE-INSTALACAO-2026-07-21.md`;
- `docs/logs/FASE-0-RELATORIO-2026-07-21.md`;
- `.codex/skills/openspec-apply-change/SKILL.md`;
- `.codex/skills/openspec-archive-change/SKILL.md`;
- `.codex/skills/openspec-explore/SKILL.md`;
- `.codex/skills/openspec-propose/SKILL.md`;
- `.codex/skills/openspec-sync-specs/SKILL.md`;
- `.codex/skills/openspec-update-change/SKILL.md`;
- `openspec/config.yaml`;
- `openspec/changes/bootstrap-core-foundation/.openspec.yaml`;
- `openspec/changes/bootstrap-core-foundation/README.md`;
- `openspec/changes/bootstrap-core-foundation/proposal.md`;
- `openspec/changes/bootstrap-core-foundation/design.md`;
- `openspec/changes/bootstrap-core-foundation/specs/phase-zero-foundation/spec.md`;
- `openspec/changes/bootstrap-core-foundation/tasks.md`.

### Artefatos locais ignorados pelo Git

- `graphify-out/graph.json`, `GRAPH_REPORT.md`, `graph.html`, `manifest.json`, `cost.json`, memória/reflexões e diagnósticos;
- backups recuperáveis em `graphify-out/pre-fase0-bootstrap-20260721T1600/` e no diretório de backups do Graphify;
- logs de health-check da Serena em `.serena/logs/`, agora ignorados para não versionar caminhos locais.

### Alteração preexistente fora do escopo

`finanças.md` já estava removido no working tree antes do bootstrap. A exclusão pertence ao usuário e não foi restaurada, sobrescrita nem contabilizada como entrega da Fase 0.

## OpenSpec

- Repositório inicializado com perfil `core` e integração Codex.
- Mudança: `bootstrap-core-foundation`.
- Capacidade nova: `phase-zero-foundation`.
- Artefatos: `proposal`, `design`, `specs` e `tasks`, todos completos.
- Execução: 35/35 tarefas marcadas como concluídas; estado OpenSpec `all_done`.
- `openspec validate bootstrap-core-foundation --strict`: aprovado.
- A mudança permanece ativa e não arquivada; arquivamento não foi solicitado e não deve iniciar outra fase.

## Graphify

### Construção e recuperação

O rebuild integral iniciado antes do reboot foi interrompido depois da extração AST. O chunk parcial e os artefatos anteriores foram movidos para backup recuperável. Como a atualização 0.9.17 → 0.9.23 tornou o cache incompatível, o grafo foi reconstruído de forma incremental e auditável a partir do grafo preservado, dos deltas Git e, ao final, de toda a cobertura residual detectada.

Resultados:

- grafo consistente inicial: 2.933 nós e 2.744 arestas;
- grafo final: 3.043 nós, 2.858 arestas, 6 hiperarestas e 292 comunidades;
- diagnóstico final: zero endpoints ausentes ou pendentes, zero self-loops, zero arestas duplicadas e zero colapsos;
- manifesto: 309/309 arquivos do corpus estampados, zero novos/alterados e zero removidos após o update;
- um arquivo sensível (`tokens.example.json`) foi deliberadamente ignorado pelo detector;
- HTML, relatório, JSON e backups foram regenerados;
- os nomes das comunidades novas foram derivados dos hubs pelo `cluster-only`; um refinamento editorial com `graphify label` é opcional, não um requisito do gate.

A extração semântica por subagentes não expôs telemetria de tokens ao orquestrador. Por isso `cost.json` e o report registram `0/0` com nota explícita: valor **não medido**, não consumo real zero.

### Documentos vinculantes localizados pelo grafo

- `AGENTS.md` e `README.md`;
- `docs/00-visao-geral/00-indice.md`;
- `docs/00-visao-geral/02-roadmap-fases.md`;
- `docs/00-visao-geral/08-hierarquia-documental.md`;
- `docs/00-visao-geral/09-decisoes-pendentes.md`;
- `docs/100-implementacao/guia-codex-app-wflyer.md`;
- `docs/implementacao/11-arquitetura-ferramentas-agentes.md`;
- `docs/implementacao/12-bootstrap-toolchain.md`;
- `docs/implementacao/13-openspec-especificacoes.md`;
- `docs/implementacao/14-graphify-governanca.md`;
- `docs/implementacao/15-serena-context7-mcp.md`;
- `docs/implementacao/20-ferramentas-opcionais-spikes.md`;
- `docs/implementacao/21-fluxo-operacional-ia.md`;
- `docs/implementacao/22-manutencao-atualizacao-toolchain.md`;
- `docs/implementacao/toolchain-manifest.yaml` e seu schema;
- artefatos ativos de `openspec/changes/bootstrap-core-foundation/`.

A consulta foi preservada em `graphify-out/memory/query_20260721_193830_quais_são_todos_os_documentos_vinculantes_à_fase_0.md`. Relações críticas foram confirmadas nas fontes; relações `INFERRED` não foram usadas como requisito.

### Destaques do report

God nodes: `Decisões arquiteturais principais` (51 arestas), `Glossário do W_Flyer` (37), `Guia de implementação para IA/Codex` (29) e `Decisões pendentes` (27).

Conexões relevantes: a memória da consulta da Fase 0 referencia explicitamente o manifesto da toolchain; o relatório de pré-instalação referencia a mudança `bootstrap-core-foundation`. Entre as perguntas sugeridas, o grafo destaca hubs genéricos de schemas e comunidades fracamente conectadas, pontos de melhoria futuros do modelo, não bloqueios desta fase.

## Serena e Context7 no Codex

`codex mcp list` e `codex mcp get` mostram:

- Serena: habilitada, transporte stdio, comando `serena start-mcp-server --context=codex --project-from-cwd`;
- Context7: habilitado, transporte HTTP, OAuth, URL `https://mcp.context7.com/mcp/oauth`.

Serena ativou `app.WFlyer`, carregou o backend LSP e expôs 29 ferramentas. O health-check termina com `No analyzable files found`, pois `languages: []` e nenhum código de aplicação existe; não foi configurada uma linguagem falsa para mascarar o estado.

Uma nova sessão efêmera e somente leitura do Codex chamou Context7 de ponta a ponta:

1. `resolve-library-id` resolveu `/graphify-labs/graphify`;
2. `query-docs` retornou a documentação atual;
3. foram confirmados `uv tool install graphifyy` e `graphify install --project --platform codex`.

## Inventário documento ↔ código

| Área | Estado na Fase 0 | Evidência |
|---|---|---|
| Documentação | 231 arquivos Markdown presentes | inventário local e grafo |
| Código de aplicação | 0 arquivos | busca por extensões de fonte, excluindo o verificador |
| Testes de produto | 0 arquivos e 0 configs | descoberta por `rg` |
| Toolchain | implementada somente na raiz | `package.json`, lockfile, script, OpenSpec, Graphify e Serena |
| Contratos/migrations | nenhum criado | fora do escopo da Fase 0 |
| Documentos de produto | sem implementação correspondente | esperado: as fases funcionais ainda não começaram |

Comandos padronizados nesta fase:

- verificação: `pnpm run verify:toolchain`;
- lint: não configurado, pertence à Fase 1;
- typecheck: não configurado, pertence à Fase 1;
- testes de produto: nenhum coletor configurado;
- dev/build: não configurados, pois não existe aplicação.

## Comandos executados

### Bootstrap e instalação

```bash
corepack enable --install-directory /home/davi-benucci/.local/bin
corepack prepare pnpm@11.15.1 --activate
pnpm add -g @fission-ai/openspec@1.6.0
uv tool upgrade graphifyy
uv tool install --force 'graphifyy==0.9.23'
graphify install --project --platform codex
graphify install --platform codex
uv tool install -p 3.13 'serena-agent==1.6.1'
serena init -b LSP
serena setup codex
npx -y ctx7@0.5.5 setup --mcp --codex --oauth --yes
codex mcp login context7
```

### OpenSpec e workspace

```bash
openspec init . --tools codex --profile core
openspec new change bootstrap-core-foundation
openspec status --change bootstrap-core-foundation
openspec instructions proposal|design|specs|tasks --change bootstrap-core-foundation --json
openspec validate bootstrap-core-foundation --strict
pnpm install --lockfile-only --ignore-scripts
pnpm install --lockfile-only --frozen-lockfile --offline --ignore-scripts
```

Os quatro comandos `openspec instructions` foram executados individualmente; a barra acima apenas os agrupa no relatório.

### Verificações e grafo

```bash
pnpm run verify:toolchain
serena project index .
serena project health-check .
codex mcp list
codex mcp get serena
codex mcp get context7
graphify reflect --if-stale
graphify query "Quais documentos e artefatos vinculam a Fase 0...?"
graphify explain "phase-zero-foundation"
graphify cluster-only .
bash -n scripts/verify-toolchain.sh
git diff --check
```

A detecção, extração AST/semântica, merge, diagnóstico e gravação do manifesto do Graphify seguiram os scripts Python fornecidos pela própria skill 0.9.23. As consultas de inventário usaram `rg`, Git e leitores locais.

### Recuperação Docker pós-reboot

```bash
docker context ls
systemctl --user status docker-desktop.service --no-pager
systemctl --user start docker-desktop.service
docker version --format 'client={{.Client.Version}} server={{.Server.Version}}'
```

## Verificações e resultados

| Verificação | Resultado |
|---|---|
| `openspec validate ... --strict` | aprovado |
| `pnpm run verify:toolchain` | aprovado após correção do coletor de arestas |
| lockfile offline/congelado | aprovado, hash inalterado |
| Graphify health | aprovado, zero flags estruturais |
| Graphify detector pós-update | 0 novos/alterados; 0 removidos; 1 sensível ignorado |
| Serena ativação | aprovada |
| Serena análise simbólica | indisponível até existir código analisável |
| Serena MCP | habilitada |
| Context7 MCP | habilitado e testado funcionalmente |
| Docker | daemon acessível após iniciar serviço de usuário |
| coletores de teste | nenhum configurado; baseline zero |
| `bash -n` e JSON | aprovados |
| `git diff --check` | aprovado |
| escopo proibido | nenhum pacote, config ou funcionalidade encontrada |

## Falhas encontradas e correções

1. **Reboot durante o Graphify:** o rebuild integral foi interrompido. Artefatos parciais foram preservados e a recuperação usou deltas auditáveis e backups.
2. **Cache Graphify incompatível:** a troca 0.9.17 → 0.9.23 marcava o corpus como alterado. O manifesto foi regenerado após cobrir 309/309 arquivos detectados.
3. **Skill Graphify global antiga:** 0.9.17 divergira da CLI 0.9.23. A skill global e a de projeto foram alinhadas em 0.9.23.
4. **Versão Graphify não fixada no receipt:** o ambiente foi reinstalado com `graphifyy==0.9.23`.
5. **Login Context7 pendente:** o setup iniciou OAuth, e `codex mcp login context7` concluiu a autenticação.
6. **Serena sem fontes:** o projeto ativa, mas o health-check não encontra arquivos analisáveis. O estado real foi mantido.
7. **Validador Graphify incorreto:** a primeira versão procurava `edges`; o JSON usa `links`. O script foi corrigido, passou a exigir arestas e confirmou 2.858 no grafo final.
8. **Inventário vazio com `pipefail`:** a primeira busca encerrou cedo porque `rg` retornou 1 ao não encontrar testes. O caso vazio foi tratado explicitamente e a coleta foi repetida.
9. **Docker inativo após reboot:** o serviço de usuário foi iniciado sem `sudo`; cliente e servidor voltaram a responder.
10. **Telemetria semântica indisponível:** os subagentes não expuseram contadores ao orquestrador; o valor 0 foi marcado como não medido.
11. **Limpeza direta recusada pelo ambiente:** a tentativa não removeu arquivos; os temporários explicitamente listados foram excluídos depois pelo mecanismo seguro de patch, preservando todas as saídas e backups.

## Pendências e divergências

- `docs/implementacao/12-bootstrap-toolchain.md` exige `nx.json`, `uv.lock`, lint, typecheck e coletores como saída da Fase 0; o manifesto vinculante classifica Nx e ferramentas de qualidade na Fase 1. Nesta execução prevaleceram o manifesto e a ordem explícita do usuário.
- A matriz de ferramentas coloca Serena/Context7 em Fase 1 em um ponto, enquanto o manifesto os coloca na Fase 0. O manifesto especializado e o pedido explícito resolveram a execução, mas a documentação deve ser reconciliada.
- A versão e o ambiente Python do backend permanecem pendentes; Python 3.13 da Serena não decide o produto.
- Lint, typecheck e suites não podem funcionar antes de seus projetos/coletores existirem; o gate registra baseline zero em vez de instalar ferramentas da Fase 1.
- O refinamento editorial dos 292 nomes de comunidade com `graphify label` é opcional.
- A mudança OpenSpec não foi arquivada.

## Escopo negativo confirmado

Não foram instalados Temporal, Rive, Pact, StrykerJS, mutmut, OMR, renderer musical, motor de harmonização, Nx, Biome, Ruff, Vitest, MSW, Playwright, Storybook, pytest, Hypothesis ou Testcontainers.

Não foram implementados telas de produção, motor musical, upload, transposição, harmonização, PDF, áudio, autenticação ou funcionalidades simuladas.

## Rollback

Os comandos abaixo são um plano de reversão e **não foram executados**.

### Ferramentas e MCPs

```bash
pnpm remove --global @fission-ai/openspec

codex mcp remove serena
uv tool uninstall serena-agent

codex mcp logout context7
npx -y ctx7@0.5.5 remove --codex --all --yes

# Remoção total do Graphify, somente após preservar graphify-out/:
graphify hook uninstall
graphify uninstall --project --platform codex
uv tool uninstall graphifyy
```

Para apenas voltar o Graphify ao baseline anterior, usar `uv tool install --force 'graphifyy==0.9.17'` e restaurar os arquivos versionados da skill após revisar o diff. Não usar `graphify uninstall --purge` sem copiar os backups.

O shim pnpm pode ser removido com `corepack disable --install-directory /home/davi-benucci/.local/bin` depois que OpenSpec não depender mais dele. O serviço Docker pode voltar ao estado inativo pós-reboot com `systemctl --user stop docker-desktop.service`, se isso for realmente desejado.

### Projeto

1. Preservar ou arquivar `openspec/` antes de qualquer remoção; seu histórico não deve ser apagado por limpeza automática.
2. Revisar individualmente os arquivos listados na seção "Criados e versionáveis" antes de removê-los.
3. Restaurar somente os caminhos versionados alterados por esta fase, nunca usar um restore amplo que alcance `finanças.md`.
4. Para o grafo, copiar de volta `graph.json`, `GRAPH_REPORT.md`, `graph.html`, `manifest.json` e o diagnóstico a partir de `graphify-out/pre-fase0-bootstrap-20260721T1600/before-final-workspace-update/`.
5. Remover manualmente o registro do projeto em `~/.serena/serena_config.yml` somente depois de backup; a CLI instalada não oferece subcomando simples de remoção do projeto.

## Gate da Fase 0

| Critério | Estado |
|---|---|
| baseline e relatório de pré-instalação | aprovado |
| instalação ordenada e sem privilégio | aprovado |
| OpenSpec e plano detalhado | aprovado |
| grafo inicial, consulta e update final | aprovado |
| ativação Serena | aprovado com ressalva: nenhum código analisável |
| Serena e Context7 no Codex | aprovado |
| versões e lockfiles aplicáveis | aprovado com ressalva documental sobre `uv.lock`/Nx |
| verificações e coletores | aprovado como baseline zero, sem suites de produto |
| exclusões obrigatórias | aprovado |
| relatórios, falhas, pendências e rollback | aprovado |

**Decisão:** a Fase 0 solicitada está `CONCLUIDA`. O gate permite encerrar este bootstrap, mas a Fase 1 permanece **NÃO LIBERADA** nesta execução, tanto pelo limite expresso do pedido quanto pelas divergências e decisões pendentes registradas acima.
