# Requisitos — DEC-032

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Lifecycle comercial dos créditos**;
- fase limite: `B0:exit`;
- owner: `billing_lead`;
- evidências: `EVID-033`, `EVID-028`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] ledger imutável e concorrência testada
- [ ] ordem de consumo e validade aprovadas
- [ ] resultado parcial/cancelamento definidos
- [ ] upgrade/downgrade e organização
- [ ] reembolso/chargeback reconciliados
- [ ] política pública coerente

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_ACCOUNTING_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
