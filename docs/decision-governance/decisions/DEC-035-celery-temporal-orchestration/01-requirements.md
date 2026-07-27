# Requisitos — DEC-035

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Celery versus Temporal para workflows longos**;
- fase limite: `FUTURE-TEMPORAL:entry`;
- owner: `platform_lead`;
- evidências: `EVID-036`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] spike com retry/signal/timer/cancelamento
- [ ] custo e operação comparados
- [ ] migração/lock-in avaliados
- [ ] uma única orquestração por pipeline

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
