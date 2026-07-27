# DEC-044 — Decisão final de lançamento comercial

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

O W_Flyer possui produto, operação, empresa, políticas, segurança, custos e suporte suficientes para ir ao ar?

## Por que esta decisão existe

Passar testes isolados não prova prontidão comercial integral.

## Prazo e gate

- trilha: `LAUNCH`;
- fase: `LAUNCH`;
- gate: `exit`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_SECURITY_REVIEW`

## Opções conhecidas

- GO
- NO-GO
- GO com escopo/segmento reduzido

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-045`](../../evidence-register.yaml) — Release Readiness Package (`PLANNED`); devido antes de `LAUNCH`.

## Critérios de aprovação pré-definidos

- [ ] Release Readiness Package completo
- [ ] zero risco crítico sem aceite formal
- [ ] rollback e suporte
- [ ] billing/fiscal apenas se lançamento pago
- [ ] métricas/custos aprovados
- [ ] aprovação multidisciplinar registrada

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `music_director`
- `security_lead`
- `accountant`
- `legal_reviewer`
- `support_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Só pode ser avaliada ao final; nunca por inferência da IA.

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
