# Requisitos — DEC-046

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Observabilidade, alertas e prontidão de incidentes**;
- fase limite: `INF2:exit;
- owner: `platform_lead`;
- evidências: `EVID-047`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] SLIs para web, API, jobs, banco, storage, billing e fiscal definidos
- [ ] correlation IDs e tracing nos fluxos críticos
- [ ] nenhum segredo ou conteúdo musical sensível em logs
- [ ] alertas ligados a owner, severidade e runbook
- [ ] tabletop/fault injection comprova detecção e escalonamento
- [ ] overhead, cardinalidade, retenção e custo aprovados

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_COST_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
