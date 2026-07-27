# Requisitos — DEC-026

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Provedor de pagamento**;
- fase limite: `B2:exit`;
- owner: `billing_lead`;
- evidências: `EVID-027`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] mesmos cenários executados em sandbox
- [ ] webhooks assinados e idempotentes
- [ ] upgrade/downgrade/cancelamento/reembolso testados
- [ ] taxas e conta empresarial reais
- [ ] conciliação e portal avaliados
- [ ] adapter interno preservado

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_SANDBOX`
- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_LEGAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
