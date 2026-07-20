# Stack recomendada

> Status: canônico. Revisão: 2026-07-20.

## Princípio

Versões exatas são fixadas em lockfiles na Fase 1. A documentação define responsabilidades e escolhas arquiteturais, não versões flutuantes.

## Frontend

```text
Next.js App Router + React + TypeScript strict
React Server Components por padrão
Tailwind CSS com CSS variables/theme tokens
shadcn/ui com primitives headless adaptados ao W_Flyer
TanStack Query
React Hook Form
Zod
Storybook
Testing Library
Playwright
Motion for React como engine padrão da UI
GSAP + @gsap/react apenas para cenas SVG/timelines isoladas
```

### Regras

- tipos de API gerados/validados a partir do OpenAPI;
- nenhuma regra musical canônica no frontend;
- não transformar layouts inteiros em Client Components;
- tokens semânticos são fonte visual; classes não substituem design system;
- componentes copiados de registry precisam ser adaptados e documentados;
- polling respeita `Retry-After`, pausa/reduz em aba oculta e encerra em estado terminal;
- cookies de sessão são `HttpOnly`;
- heavy preview/renderer é lazy-loaded;
- fontes são otimizadas e não dependem de rede externa em runtime;
- View Transition API pode ser progressive enhancement, nunca requisito funcional;
- CSS resolve microestados simples; Motion resolve presença/layout/gestos React;
- GSAP é lazy-loaded e restrito à animação-assinatura e cenas aprovadas;
- Anime.js e React Spring não são dependências do MVP Core;
- uma propriedade de um nó não pode ser controlada simultaneamente por CSS, Motion e GSAP.

## Backend

```text
FastAPI
Python
Pydantic
SQLAlchemy
Alembic
PostgreSQL
Celery
Redis
pytest
ruff
mypy ou pyright
```

Regras:

- PostgreSQL é fonte de verdade para jobs;
- Celery transporta trabalho;
- serialização da fila em JSON;
- migrations obrigatórias;
- OpenAPI versionado e testado.

## Processamento musical

```text
MusicXML 4.0 como formato canônico de saída
music21 como candidato inicial do motor
adapter de OMR selecionado após spike
adapter de renderização selecionado após spike
```

Integrações ficam atrás de interfaces, com versão registrada no job.

## Storage

- filesystem privado para desenvolvimento/teste;
- storage compatível com objetos para ambientes compartilhados.

## Execução isolada

OMR, rasterização e renderização ocorrem em processo/container separado, sem rede e com limites de recursos.

## Decisões que continuam bloqueadas

- engine OMR de produção;
- engine de renderização;
- limites exatos de páginas, tamanho e tempo;
- suporte público a `.mxl`.
