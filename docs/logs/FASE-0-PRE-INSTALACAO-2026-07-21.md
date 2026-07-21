# Relatório de pré-instalação — bootstrap e Fase 0

> Status: evidência operacional. Captura: 2026-07-21T15:57:20-03:00. Escopo: somente bootstrap e Fase 0.

## Ambiente confirmado

| Item | Resultado |
|---|---|
| Diretório atual | `/home/davi-benucci/Área de trabalho/app.WFlyer` |
| Raiz Git | `/home/davi-benucci/Área de trabalho/app.WFlyer` |
| Branch | `main`, acompanhando `origin/main` |
| Working tree inicial | alteração preexistente do usuário: `finanças.md` removido; deve ser preservada |
| Sistema | Ubuntu 26.04 LTS (`resolute`), kernel Linux 7.0.0-28, x86_64 |
| Git | 2.53.0 (`/usr/bin/git`) |
| Node.js | 24.18.0 (`/usr/local/bin/node`); satisfaz `>=20.19` |
| npm | 11.16.0 (`/usr/local/bin/npm`) |
| Python | comando `python` ausente; `python3` 3.14.4 em `/usr/bin/python3` |
| uv | 0.11.29 (`/home/davi-benucci/.local/bin/uv`) |
| Docker | cliente 29.6.2; servidor 29.6.1; daemon acessível |
| Codex CLI | 0.145.0-alpha.18 |

## Ferramentas encontradas

| Ferramenta | Versão/estado | Escopo observado |
|---|---|---|
| Corepack | 0.35.0 | instalação do Node em `/usr/local` |
| Graphify | 0.9.17 | `uv tool`, em `/home/davi-benucci/.local/share/uv/tools` |
| Integração Graphify | 0.9.17 | projeto: `.codex/skills/graphify/` e `.codex/hooks.json` |
| Grafo anterior | presente | `graphify-out/`; será reconstruído como evidência desta execução |

Versões publicadas consultadas antes da instalação: pnpm 11.15.1, OpenSpec 1.6.0, Graphify 0.9.23, Serena 1.6.1, `ctx7` 0.5.5 e `@upstash/context7-mcp` 3.2.4.

## Ferramentas ausentes

- `pnpm`;
- OpenSpec;
- Serena;
- `ctx7`;
- qualquer servidor MCP registrado no Codex;
- fundação local do workspace: `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml`, `pyproject.toml`, `uv.lock` e `nx.json`;
- diretórios `openspec/` e `.serena/`.

## Incompatibilidades e desvios controlados

1. `/usr/local/bin` e `/usr/local/lib/node_modules` pertencem a `root` e não são graváveis pelo usuário. Os comandos globais não usarão esse prefixo e nenhum `sudo` será executado.
2. O shim de `pnpm` não existe. Corepack será habilitado em `/home/davi-benucci/.local/bin` e a versão será fixada em 11.15.1.
3. O Graphify instalado está seis releases de patch atrás da versão publicada consultada (0.9.17 → 0.9.23); a ferramenta e sua integração de projeto serão atualizadas antes do novo grafo.
4. O manifesto solicita Serena sobre Python 3.13, mas apenas Python 3.14.4 está instalado. `uv` provisionará Python 3.13 em ambiente gerenciado do usuário, sem alterar o Python do sistema nem definir a versão do futuro backend.
5. O comando não versionado `python` está ausente. Isso não bloqueia as ferramentas, que usarão interpretadores explícitos gerenciados pelo `uv`.
6. O manifesto classifica Nx como Fase 1, embora o bootstrap documental liste `nx.json` entre as saídas da Fase 0. Pela precedência solicitada nesta execução, Nx não será instalado preventivamente; a divergência será mantida visível no gate.
7. MCPs adicionados à configuração global não são recarregados pela sessão Codex já aberta. A verificação usará o registro do Codex e health-check/handshake; uma nova sessão poderá ser necessária para disponibilizar as ferramentas ao agente atual.

## Comandos propostos

Os comandos abaixo serão executados nessa ordem, após este relatório, com versões resolvidas registradas no relatório final:

```bash
corepack enable --install-directory /home/davi-benucci/.local/bin
corepack prepare pnpm@11.15.1 --activate
pnpm add -g @fission-ai/openspec@1.6.0
openspec --version

uv tool upgrade graphifyy
graphify install --project --platform codex
graphify --version

uv tool install -p 3.13 serena-agent==1.6.1
serena init
# registrar o servidor Serena no Codex conforme a CLI instalada

npx -y ctx7@0.5.5 setup --mcp --codex --yes
# se o setup exigir autenticação interativa, usar a configuração MCP oficial equivalente

openspec init . --tools codex --profile core
openspec new change bootstrap-core-foundation
```

O grafo inicial, a ativação Serena, o plano da Fase 0 e a fundação do workspace serão executados somente depois dessas quatro integrações, conforme a ordem solicitada.

## Alterações globais previstas

- shims e cache do Corepack/pnpm dentro do perfil do usuário;
- pacote global OpenSpec no escopo de usuário do pnpm;
- atualização do ambiente isolado Graphify sob `~/.local/share/uv/tools`;
- ambiente isolado Serena e Python 3.13 gerenciado pelo `uv`;
- configuração MCP do Codex em `~/.codex/config.toml`;
- cache efêmero do `npx` para `ctx7`/Context7 MCP;
- nenhuma alteração em pacote do sistema, `/usr/local` ou configuração com segredo versionado.

## Alterações previstas no projeto

- inicialização de `openspec/` e integração Codex gerada pelo OpenSpec;
- mudança `openspec/changes/bootstrap-core-foundation/`;
- atualização da integração Graphify de projeto e de `graphify-out/`;
- metadados locais da Serena, se a CLI os criar;
- plano e relatórios da Fase 0;
- estrutura mínima e lockfiles somente se confirmados pelo grafo e pelo plano, sem frameworks ou funcionalidade de produto.

## Riscos e controles

- **Working tree não limpo:** não tocar em `finanças.md`; revisar o diff por caminho ao final.
- **Instalação global sem privilégio:** usar exclusivamente diretórios do usuário; interromper antes de qualquer necessidade de `sudo`.
- **Mudança automática de `AGENTS.md`:** revisar e preservar as regras existentes ao instalar OpenSpec/Graphify.
- **Autenticação Context7:** não registrar API key no repositório nem imprimir segredo; reportar bloqueio se o MCP não funcionar sem coordenação externa.
- **Grafo anterior:** não tratá-lo como evidência da execução atual; gerar nova extração e registrar saúde do grafo.
- **Custo de extração semântica:** usar extração local/agent conforme Graphify, sem pedir chave e sem enviar segredos.
- **Escopo:** não instalar Nx, frameworks de frontend/backend, Temporal, Rive, Pact, StrykerJS, mutmut, OMR, renderer musical ou motor de harmonização nesta etapa.
- **Gate honesto:** coletores vazios ou ferramentas registradas sem handshake serão reportados como tal, nunca como implementação funcional.

## Fontes de validação

- OpenSpec: <https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md>
- Graphify: <https://github.com/Graphify-Labs/graphify>
- Serena: <https://github.com/oraios/serena>
- Context7: <https://context7.com/docs/resources/all-clients>
- versões publicadas: registries npm e PyPI consultados em 2026-07-21.
