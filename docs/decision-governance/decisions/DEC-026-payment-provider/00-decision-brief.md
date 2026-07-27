# DEC-026 — Provedor de pagamento

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-028`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual provedor atende assinatura, Pix/cartão, webhooks, reembolso, conciliação e expansão com custo aceitável?

## Por que esta decisão existe

A escolha afeta conversão, operação brasileira, segurança, suporte e acoplamento do billing.

## Prazo e gate

- trilha: `B`;
- fase: `B2`;
- gate: `exit`;
- owner: `billing_lead`.

## Bloqueios atuais

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_SANDBOX`
- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_LEGAL_REVIEW`

## Opções conhecidas

- Stripe
- Mercado Pago

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-027`](../../evidence-register.yaml) — Spike sandbox Stripe versus Mercado Pago (`PLANNED`); devido antes de `B1/B2`.

## Critérios de aprovação pré-definidos

- [ ] mesmos cenários executados em sandbox
- [ ] webhooks assinados e idempotentes
- [ ] upgrade/downgrade/cancelamento/reembolso testados
- [ ] taxas e conta empresarial reais
- [ ] conciliação e portal avaliados
- [ ] adapter interno preservado

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `finance_owner`
- `security_lead`
- `accountant`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar B1 somente após empresa e produto estabilizado.

## Sequência obrigatória

```text
requisitos congelados
→ plano de experimento
→ evidência bruta
→ comparação
→ risco/rollback
→ aprovação humana
→ ADR/MDR/FDR
→ OpenSpec de implementação
→ implementação
→ validação pós-implementação
```
