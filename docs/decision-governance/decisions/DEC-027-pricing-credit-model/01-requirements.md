# Requisitos — DEC-027

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Modelo de planos, preços e créditos**;
- fase limite: `B0:exit`;
- owner: `product_owner`;
- evidências: `EVID-028`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] custo mínimo/médio/p95 por operação
- [ ] taxa de falha/reprocessamento
- [ ] gateway/tributos/suporte
- [ ] simulações de perfis leves e intensivos
- [ ] margem e reserva de risco aprovadas
- [ ] campos PENDENTE preenchidos somente após evidência

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
