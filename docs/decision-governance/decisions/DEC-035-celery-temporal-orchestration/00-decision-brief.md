# DEC-035 — Celery versus Temporal para workflows longos

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

A complexidade dos workflows justifica substituir a orquestração Celery por Temporal?

## Por que esta decisão existe

Temporal melhora durable execution, mas adiciona infraestrutura e regras operacionais.

## Prazo e gate

- trilha: `TOOL`;
- fase: `FUTURE-TEMPORAL`;
- gate: `entry`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Opções conhecidas

- manter Celery
- adotar Temporal
- não misturar ambos no mesmo pipeline

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-036`](../../evidence-register.yaml) — Spike Celery versus Temporal (`PLANNED`); devido antes de `FUTURE-TEMPORAL`.

## Critérios de aprovação pré-definidos

- [ ] spike com retry/signal/timer/cancelamento
- [ ] custo e operação comparados
- [ ] migração/lock-in avaliados
- [ ] uma única orquestração por pipeline

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `finance_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Opcional; não bloqueia o Core local.

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
