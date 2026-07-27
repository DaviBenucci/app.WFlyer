# Requisitos — DEC-031

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Metas comerciais de SLO, RPO e RTO**;
- fase limite: `INF3:exit;
- owner: `product_owner`;
- evidências: `EVID-032`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] RPO/RTO testados em restore
- [ ] SLO calculado por user journey
- [ ] orçamento e redundância alinhados
- [ ] exclusões e manutenção definidas
- [ ] não publicar SLA antes de validação

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
