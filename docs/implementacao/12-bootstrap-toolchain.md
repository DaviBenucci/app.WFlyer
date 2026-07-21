# Bootstrap da toolchain do W_Flyer

> Status: canônico. Execute somente na Fase 0, em ambiente limpo, registrando versões e saídas.

## Pré-requisitos

- Git;
- Node.js **20.19 ou superior**, fixado no repositório;
- Corepack e pnpm;
- `uv` para Python;
- runtime compatível com Docker API para Testcontainers;
- navegador e dependências do Playwright;
- Linux/Ubuntu como ambiente de referência para desenvolvimento e CI.

## Princípios

- não executar comandos de instalação às cegas;
- confirmar o diretório raiz antes de cada comando;
- não instalar ferramentas opcionais;
- não incluir CLI de desenvolvimento na imagem de produção;
- não armazenar API keys em arquivos versionados;
- registrar versões em `docs/logs/IMPLEMENTATION_LOG.md`.

## 1. Preparar Node e pnpm

```bash
node --version
corepack enable
corepack prepare pnpm@latest --activate
pnpm --version
```

Depois do bootstrap, substituir `latest` pela versão aprovada e piná-la em `packageManager` no `package.json`.

## 2. Preparar Python e uv

```bash
uv --version
python3 --version
```

A versão Python do backend é decidida na Fase 0 conforme compatibilidade das bibliotecas musicais. Serena usa ambiente próprio com Python 3.13 e não determina a versão do backend.

## 3. Instalar e inicializar OpenSpec

```bash
pnpm add -g @fission-ai/openspec@latest
openspec --version
openspec init
```

- selecionar Codex e os demais agentes realmente usados;
- versionar a pasta `openspec/`;
- após atualização do CLI, executar `openspec update` e revisar o diff;
- nunca apagar histórico de mudanças para “limpar” contexto.

## 4. Instalar Graphify

```bash
uv tool install graphifyy
graphify --version
graphify install --platform codex
```

No agente, construir o grafo inicial:

```text
/graphify .
```

Depois:

```bash
graphify hook install
```

O hook é opcional se o CI ou a rotina local já executar atualização explícita. A saída `graphify-out/` é artefato local/CI e não é fonte canônica.

## 5. Instalar Serena e conectar ao Codex

```bash
uv tool install -p 3.13 serena-agent
serena --version
serena init
serena setup codex
```

Verificação:

```text
1. iniciar Codex na raiz;
2. executar /mcp;
3. confirmar Serena conectada;
4. pedir “ative o diretório atual como projeto usando Serena”;
5. executar um health-check/index do projeto.
```

A configuração manual equivalente usa:

```toml
[mcp_servers.serena]
startup_timeout_sec = 15
command = "serena"
args = ["start-mcp-server", "--project-from-cwd", "--context=codex"]
```

A configuração global fica fora do repositório. Não versionar arquivos contendo caminhos privados ou segredos.

## 6. Configurar Context7 para Codex

```bash
npx ctx7 setup --codex
```

Verificação:

- confirmar o MCP no Codex;
- consultar a documentação de uma dependência instalada e conferir a versão;
- não inserir `CONTEXT7_API_KEY` no Git;
- remover a configuração com `npx ctx7 remove` quando necessário.

## 7. Inicializar Nx em repositório existente

Executar somente depois que o workspace JavaScript existir:

```bash
npx nx@latest init
pnpm nx --version
pnpm nx graph
```

Depois do bootstrap, fixar a versão no lockfile. O global do Nx é opcional; comandos de CI usam o binário local.

## 8. Instalar qualidade e testes do frontend

Na raiz do workspace:

```bash
pnpm add -D -w --save-exact @biomejs/biome
pnpm exec biome init
pnpm add -D -w vitest @vitest/browser
pnpm add -D -w msw
pnpm create playwright
pnpm create storybook@latest
pnpm add -D -w style-dictionary
```

No app web:

```bash
pnpm add xstate @xstate/react
pnpm exec msw init apps/web/public --save
```

Durante a instalação do Storybook, escolher `@storybook/nextjs-vite` salvo incompatibilidade documentada. Não manter stories de exemplo gerados que não representam o produto.

## 9. Instalar qualidade e testes do backend

Dentro do projeto Python:

```bash
uv add --dev pytest hypothesis ruff
uv add --dev "testcontainers[postgres]"
uv run ruff check .
uv run ruff format --check .
uv run pytest --collect-only
```

Adicionar módulos de Testcontainers somente quando a dependência real for usada, por exemplo Redis ou MinIO/LocalStack. Docker deve estar funcional antes dos testes de integração.

## 10. Instalar navegadores do Playwright

```bash
pnpm exec playwright install --with-deps
pnpm exec playwright test --list
```

No CI, utilizar imagem/ambiente compatível e não baixar navegadores de forma não determinística em cada job sem cache ou pinning.

## 11. Verificação consolidada

```bash
bash docs/implementacao/templates/verify-toolchain.sh.example
```

O script é referência e deve ser copiado/adaptado para `scripts/verify-toolchain.sh` quando o monorepo existir.

## Saída obrigatória da Fase 0

- versões registradas;
- `package.json`, `pnpm-lock.yaml`, `uv.lock` e `nx.json` versionados;
- `openspec/` inicializado;
- Graphify e Serena conectados;
- Context7 verificado;
- lint, typecheck e coletores de testes funcionando;
- nenhum framework opcional instalado;
- relatório de falhas ou incompatibilidades.

## Fontes oficiais

- OpenSpec: <https://openspec.dev/docs/installation>
- Graphify: <https://graphify.com/docs/install>
- Serena: <https://oraios.github.io/serena/02-usage/010_installation.html>
- Context7: <https://context7.com/docs/clients/codex>
- Nx: <https://nx.dev/docs/getting-started/installation>
