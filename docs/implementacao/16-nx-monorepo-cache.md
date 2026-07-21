# Nx — monorepo, grafo executável e tarefas afetadas

> Status: obrigatório depois que os workspaces existirem.

## Responsabilidade

Nx organiza projetos, dependências e targets. Seu objetivo no W_Flyer é executar somente o necessário, sem ocultar falhas por cache indevido.

## Estrutura alvo

```text
apps/
├── web
├── api
├── worker
└── storybook
packages/
├── music-domain
├── musicxml
├── transposition-engine
├── melody-extraction
├── harmony-engine
├── instrument-catalog
├── design-system
├── api-contracts
└── testing-fixtures
```

O backend Python pode ser representado por targets Nx que chamam `uv run`, mesmo que o código não seja JavaScript.

## Instalação

Em repositório existente:

```bash
npx nx@latest init
pnpm nx --version
pnpm nx graph
```

Após o bootstrap, usar o Nx local e o lockfile.

## Targets mínimos

```text
lint
typecheck
test
unit
property
integration
contract
build
storybook
visual
e2e
security
mutation
```

Nem todo target existe em todo projeto. A ausência deve ser declarada, não mascarada com comando que sempre retorna sucesso.

## Comandos da IA

```bash
pnpm nx show projects
pnpm nx graph
pnpm nx affected -t lint typecheck test
pnpm nx affected -t build integration e2e --base=origin/main --head=HEAD
pnpm nx run web:storybook
pnpm nx run api:test
```

## Cache

Pode ser cacheado:

- lint;
- typecheck;
- unit tests determinísticos;
- build;
- geração de tokens;
- geração de cliente OpenAPI;
- Storybook estático.

Não cachear sem modelagem correta:

- teste que consulta rede pública;
- teste com relógio real não controlado;
- teste de carga;
- teste com dado externo mutável;
- E2E dependente de ambiente compartilhado;
- benchmark musical sem ambiente/seed incluídos no hash.

## Inputs e outputs

Cada target deve declarar:

- fontes de código;
- configs;
- lockfiles;
- variáveis permitidas;
- fixtures/corpus;
- outputs gerados.

Alterar catálogo de instrumentos deve invalidar testes e builds que dependem dele. Alterar apenas um baseline visual não deve executar OMR.

## Integração Python

Exemplo conceitual de target:

```json
{
  "test": {
    "command": "uv run pytest",
    "cwd": "apps/api",
    "cache": true,
    "inputs": ["default", "^default", "{workspaceRoot}/uv.lock"]
  }
}
```

A configuração real deve seguir a versão instalada do Nx e ser validada antes do commit.

## Atualização

```bash
pnpm nx migrate <versao-alvo>
pnpm install
pnpm nx migrate --run-migrations
```

Atualizar um major por vez. Revisar `migrations.json`, executar todos os gates e remover o arquivo somente conforme orientação oficial.

## Regra para a IA

1. usar `nx affected` como primeira execução após alteração;
2. ampliar para suíte completa quando o risco exigir;
3. nunca interpretar cache hit como evidência de que o teste foi executado no código incorreto;
4. usar `--skip-nx-cache` para investigar suspeita de staleness;
5. registrar comandos e hashes no log de testes;
6. não habilitar cache remoto sem avaliação de segurança e segregação de dados.

## Fontes oficiais

- <https://nx.dev/docs/getting-started/installation>
- <https://nx.dev/docs/guides/adopting-nx/adding-to-existing-project>
- <https://nx.dev/docs/features/run-tasks>
