# Árvore atual e arquitetura física planejada

> Status: canônico para navegação estrutural. Revisão: 2026-07-27.

## Estrutura atual do repositório

O repositório ainda está na transição entre governança e implementação. A árvore abaixo mostra os artefatos relevantes, sem expandir arquivos gerados ou históricos individuais.

```text
app.WFlyer/
├── .codex/
│   ├── hooks.json
│   └── skills/                       # skills instaladas para Graphify/OpenSpec
├── .serena/
│   └── project.yml                   # configuração versionada do projeto
├── AGENTS.md                         # contrato operacional dos agentes
├── README.md
├── TREE.md
├── MANIFESTO_VALIDACAO.md
├── W-Flyer_Regra-Transposição.md
├── docs/
│   ├── 00-visao-geral/               # escopo, ADRs, roadmap e pendências
│   ├── 100-implementacao/            # guia, aceite e rastreabilidade
│   ├── backend/
│   ├── design-reference/             # specs, protótipos e baselines candidatos
│   ├── features/
│   ├── frontend/
│   ├── implementacao/                # toolchain e fluxo dos agentes
│   ├── logs/
│   ├── music/
│   ├── pages/
│   ├── qa/
│   ├── referencias/
│   ├── riscos/
│   └── security/
├── graphify-out/                     # grafo gerado; índice, não fonte normativa
├── openspec/
│   ├── config.yaml
│   ├── specs/
│   │   └── phase-zero-foundation/spec.md
│   └── changes/
│       └── archive/
│           └── 2026-07-27-bootstrap-core-foundation/
├── scripts/
│   ├── validate-repository.py
│   ├── verify-repository.sh
│   ├── verify-local-agent-toolchain.sh
│   └── verify-toolchain.sh           # alias compatível
├── package.json
└── pnpm-lock.yaml
```

`node_modules/`, caches, arquivos locais da Serena, segredos, uploads e builds são descartáveis e não pertencem ao pacote versionado.

## Arquitetura física planejada para a Fase 1

A Fase 1 deverá criar a fundação abaixo. O scaffold só pode ocorrer dentro da mudança OpenSpec `establish-executable-foundation`.

```text
app.WFlyer/
├── apps/
│   ├── web/                          # Next.js, UX e consumo da API
│   ├── api/                          # FastAPI, HTTP, sessão, autorização e persistência
│   └── worker/                       # execução assíncrona e manutenção
├── packages/
│   ├── api-client/                   # TypeScript gerado a partir do OpenAPI
│   ├── ui/                           # componentes sem regra musical
│   ├── config/                       # configurações compartilháveis
│   └── python/
│       ├── music-domain/             # tipos e invariantes musicais canônicos
│       ├── musicxml/                 # parser, normalização e serialização
│       ├── instrument-catalog/       # perfis versionados de instrumento
│       ├── transposition-engine/     # transformação determinística
│       └── music-verifier/           # verificação independente
├── tests/
│   ├── fixtures/
│   │   ├── musicxml/
│   │   ├── hostile-files/
│   │   └── expected/
│   └── e2e/
├── docs/
├── openspec/
├── scripts/
├── nx.json
├── pnpm-workspace.yaml
├── pyproject.toml
├── pnpm-lock.yaml
└── uv.lock
```

## Decisão de compartilhamento Python

API e worker utilizarão os mesmos pacotes Python internos em `packages/python/`. O domínio musical não ficará dentro da API e não será duplicado em TypeScript.

```text
apps/api      ─┐
               ├─> packages/python/*
apps/worker   ─┘
```

Consequências:

- API e worker continuam implantáveis separadamente;
- parser, catálogo, transformador e verificador possuem uma única implementação;
- dependências são fixadas no workspace `uv`;
- Nx pode orquestrar targets Python chamando `uv run`;
- o frontend recebe somente contratos OpenAPI e dados de apresentação.

A decisão completa está em `docs/00-visao-geral/01-decisoes-arquiteturais.md` e `docs/backend/13-estrutura-pastas.md`.

## Regras estruturais

- não criar `packages/shared/music` em TypeScript;
- não colocar regra musical em componentes React;
- não fazer o worker importar internamente a aplicação HTTP;
- não editar manualmente `packages/api-client`;
- não transformar `graphify-out/` em fonte normativa;
- não adicionar capability avançada ao menu como disponível antes do respectivo gate.
