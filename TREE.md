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
├── brand/                             # identidade pendente e ativos aprovados futuros
│   ├── source/
│   ├── variants/
│   ├── favicons/
│   ├── guidelines/
│   └── brand-manifest.yaml
├── README.md
├── TREE.md
├── MANIFESTO_VALIDACAO.md
├── W-Flyer_Regra-Transposição.md
├── docs/
│   ├── 00-visao-geral/               # escopo, ADRs, roadmap e visões por público
│   │   ├── 20-explicacao-completa-nao-tecnica.md
│   │   └── 21-visao-tecnica-completa.md
│   ├── 100-implementacao/            # guia, aceite e rastreabilidade
│   ├── backend/
│   ├── billing/                       # assinaturas, créditos e provedores
│   ├── brand/                         # briefing e governança da identidade
│   ├── decision-governance/           # decisões, evidências e gates por fase
│   ├── design-reference/              # specs, protótipos e baselines candidatos
│   ├── features/
│   ├── fiscal/                        # NFS-e e prontidão contábil
│   ├── frontend/
│   ├── implementacao/                 # toolchain e fluxo dos agentes
│   ├── infrastructure/                # hosting, AWS, banco e DR
│   ├── logs/
│   ├── music/
│   ├── operations/                    # runbooks
│   ├── policies/                      # políticas públicas versionadas e central /politicas
│   ├── pages/
│   ├── qa/
│   ├── referencias/
│   ├── riscos/
│   └── security/
├── graphify-out/                     # grafo gerado; índice, não fonte normativa
├── openspec/
│   ├── config.yaml
│   ├── specs/
│   │   ├── phase-zero-foundation/spec.md
│   │   ├── business-launch-readiness/spec.md
│   │   ├── pricing-credits-policies/spec.md
│   │   └── brand-identity-foundation/spec.md
│   └── changes/
│       └── archive/
│           ├── 2026-07-27-bootstrap-core-foundation/
│           ├── 2026-07-27-document-business-launch-readiness/
│           ├── 2026-07-27-document-pricing-credits-policies/
│           ├── 2026-07-27-document-brand-identity-foundation/
│           └── 2026-07-27-document-decision-governance/
├── scripts/
│   ├── validate-repository.py
│   ├── verify-repository.sh
│   ├── verify-local-agent-toolchain.sh
│   └── verify-toolchain.sh           # alias compatível
├── package.json
└── pnpm-lock.yaml
```

`node_modules/`, caches, arquivos locais da Serena, segredos, uploads e builds são descartáveis e não pertencem ao pacote versionado.


## Governança de decisões

```text
docs/decision-governance/
├── README.md
├── decision-register.yaml
├── evidence-register.yaml
├── phase-decision-gates.yaml
├── decisions/DEC-XXX-slug/
└── templates/
```

`DEC-*` identifica a pergunta; `EVID-*` identifica a prova; `DGATE-*` liga a decisão à fase. O Graphify indexa esses artefatos, mas o estado canônico permanece nos registros YAML.

<!-- DECISION-GOVERNANCE-TREE:START -->
## Estrutura de governança de decisões

```text
docs/decision-governance/
├── README.md
├── 00-analise-situacao-atual.md
├── 01-papeis-aprovacoes.md
├── 02-fluxo-decisao.md
├── 03-evidencias-freshness.md
├── 04-gates-fases-e-ia.md
├── 05-registro-humano-decisoes.md       # gerado
├── 06-matriz-decisoes-evidencias.md     # gerado
├── 07-matriz-gates-fases.md             # gerado
├── 08-migracao-ids-legados.md
├── decision-register.yaml
├── evidence-register.yaml
├── phase-decision-gates.yaml
├── *.schema.json
├── decisions/
│   └── DEC-XXX-slug/
│       ├── 00-decision-brief.md
│       ├── 01-requirements.md
│       ├── 02-options.md
│       ├── 03-experiment-plan.md
│       ├── 04-evidence/README.md
│       ├── 05-comparison.md
│       ├── 06-risk-analysis.md
│       ├── 07-decision-record.md
│       └── 08-validation.md
└── templates/

scripts/
├── generate-decision-docs.py
└── check-decision-gate.py
```

Os YAMLs são canônicos; os índices humanos são gerados; o pacote registra o processo completo. O Graphify apenas indexa esses artefatos.
<!-- DECISION-GOVERNANCE-TREE:END -->

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
## Presença digital planejada

```text
wflyer.com.br       → repositório e deploy do site institucional
app.wflyer.com.br   → aplicação deste repositório
status.wflyer.com.br→ status independente
clientes            → repositórios e ambientes isolados
```

O site institucional não será adicionado ao monorepo da aplicação. A infraestrutura AWS de produção e o hosting de clientes também permanecem separados.

## Catálogos comerciais e políticas planejadas

```text
docs/billing/
├── 08-parametros-precos-planos.md
├── 09-sistema-creditos-detalhado.md
├── 10-formulario-decisao-precos-creditos.md
├── pricing-config.template.yaml
└── pricing-config.schema.json

docs/policies/
├── 00-central-de-politicas.md
├── 01-termos-de-uso.md
├── 02-politica-privacidade.md
├── 03-politica-cookies.md
├── 04-politica-pagamentos-creditos-assinaturas.md
├── 05-politica-cancelamento-reembolso.md
├── 06-politica-direitos-autorais-conteudo.md
├── 07-politica-uso-aceitavel.md
├── 08-politica-retencao-exclusao.md
├── 09-politica-suporte-disponibilidade.md
├── 10-politica-seguranca-incidentes.md
├── policy-manifest.yaml
└── policy-manifest.schema.json
```

Esses arquivos preparam decisões futuras; não habilitam cobrança nem publicação jurídica.
