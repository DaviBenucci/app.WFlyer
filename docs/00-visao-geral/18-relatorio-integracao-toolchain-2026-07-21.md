# Relatório de integração da toolchain de IA e qualidade

> Data: 2026-07-21. Escopo: documentação; nenhuma dependência foi instalada ou executada no código do produto.

## Objetivo

Documentar como agentes devem instalar, combinar e utilizar ferramentas de especificação, navegação, redução de contexto, monorepo, interface reativa e testes em camadas.

## Decisão central

```text
OpenSpec → intenção e critérios
Graphify → impacto macro
Serena → símbolos e referências
Context7 → documentação externa versionada
Nx → tarefas afetadas e cache
XState → fluxos complexos da UI
Storybook/testes → evidência executável
```

## Conteúdo incorporado

- bootstrap ordenado e verificável;
- matriz de 21 ferramentas;
- separação entre ferramentas globais, dependências JS e dependências Python;
- instalação, verificação, uso, atualização e retirada;
- regras de economia de tokens sem perda de invariantes;
- governança de OpenSpec, Graphify, Serena e Context7;
- monorepo e cache com Nx;
- XState para fluxos complexos;
- Storybook, Vitest, MSW, Playwright, Biome e Style Dictionary;
- pytest, Hypothesis, Testcontainers e Ruff;
- spikes para Temporal, Rive, Pact, StrykerJS e mutmut;
- templates de `AGENTS.md`, `.graphifyignore`, bootstrap, verificação e targets Nx;
- integração com Definition of Done, estratégia de testes e guia do Codex.

## Regras críticas

- Graphify é índice, não fonte de verdade.
- Serena atua depois da análise de impacto.
- Context7 não consulta requisitos internos.
- `latest` é permitido somente no bootstrap controlado; lockfiles passam a ser obrigatórios.
- ferramenta opcional não é instalada antes de spike/ADR.
- Temporal não pode disputar o mesmo pipeline com Celery.
- Rive não manipula partitura real nem substitui GSAP/Motion.
- mutation testing é agendado e focado em código crítico.
- nenhuma economia de tokens pode omitir regra musical, segurança ou teste impactado.

## Limites

A documentação contém comandos-base coerentes com as fontes oficiais consultadas na data da revisão. A implementação deverá confirmar compatibilidade entre versões reais, sistema operacional, lockfiles e código criado na Fase 0.
