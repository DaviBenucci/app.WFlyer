# Requisitos — DEC-030

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Broker e orquestração de produção**;
- fase limite: `INF2:exit;
- owner: `platform_lead`;
- evidências: `EVID-031`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] fault injection de crash/duplicata/timeout
- [ ] DLQ e reprocessamento controlado
- [ ] backpressure e prioridade
- [ ] compatibilidade Python
- [ ] custo e operação medidos
- [ ] PostgreSQL/outbox preservados

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
