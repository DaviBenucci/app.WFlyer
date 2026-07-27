# DEC-027 — Modelo de planos, preços e créditos

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-029`. Implementação autorizada: **não**.

## Pergunta de decisão

Como converter custo e valor de uso em planos, quotas e créditos sem gerar prejuízo ou surpresa ao usuário?

## Por que esta decisão existe

Operações MusicXML, OMR, harmonia e ensemble têm custos muito diferentes.

## Prazo e gate

- trilha: `B`;
- fase: `B0`;
- gate: `exit`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`

## Opções conhecidas

- assinatura com créditos
- créditos avulsos
- combinação aprovada após simulações

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-028`](../../evidence-register.yaml) — Modelo de custo e simulação de preços (`PLANNED`); devido antes de `B0`.

## Critérios de aprovação pré-definidos

- [ ] custo mínimo/médio/p95 por operação
- [ ] taxa de falha/reprocessamento
- [ ] gateway/tributos/suporte
- [ ] simulações de perfis leves e intensivos
- [ ] margem e reserva de risco aprovadas
- [ ] campos PENDENTE preenchidos somente após evidência

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `finance_owner`
- `accountant`
- `billing_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Coletar custos reais antes de preencher pricing-config.

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
