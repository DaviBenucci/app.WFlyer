# DEC-032 — Lifecycle comercial dos créditos

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-034`. Implementação autorizada: **não**.

## Pergunta de decisão

Como créditos são concedidos, reservados, consumidos, liberados, expirados, estornados e reconciliados?

## Por que esta decisão existe

Regras ambíguas geram saldo negativo, cobrança dupla, passivo de créditos e conflitos de reembolso.

## Prazo e gate

- trilha: `B`;
- fase: `B0`;
- gate: `exit`;
- owner: `billing_lead`.

## Bloqueios atuais

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_ACCOUNTING_REVIEW`

## Opções conhecidas

- lotes mensais e avulsos separados
- ordem de consumo definida
- validade/acúmulo PENDENTE

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-033`](../../evidence-register.yaml) — Cenários de lifecycle e ledger de créditos (`PLANNED`); devido antes de `B0/B4`.
- [`EVID-028`](../../evidence-register.yaml) — Modelo de custo e simulação de preços (`PLANNED`); devido antes de `B0`.

## Critérios de aprovação pré-definidos

- [ ] ledger imutável e concorrência testada
- [ ] ordem de consumo e validade aprovadas
- [ ] resultado parcial/cancelamento definidos
- [ ] upgrade/downgrade e organização
- [ ] reembolso/chargeback reconciliados
- [ ] política pública coerente

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `finance_owner`
- `legal_reviewer`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Preencher após DEC-027 e revisão jurídica.

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
