# DEC-030 — Broker e orquestração de produção

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-032`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual mecanismo de fila/orquestração atende durabilidade, retry, DLQ, cancelamento e custo de produção?

## Por que esta decisão existe

A fila não é fonte de verdade, mas falhas de entrega e ACK podem duplicar ou perder processamento se a idempotência falhar.

## Prazo e gate

- trilha: `INF`;
- fase: `INF2`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Opções conhecidas

- Celery + Redis com controles aprovados
- SQS com adapter de worker
- Temporal somente se DEC-035 justificar

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-031`](../../evidence-register.yaml) — Fault injection e custo do broker (`PLANNED`); devido antes de `INF2`.

## Critérios de aprovação pré-definidos

- [ ] fault injection de crash/duplicata/timeout
- [ ] DLQ e reprocessamento controlado
- [ ] backpressure e prioridade
- [ ] compatibilidade Python
- [ ] custo e operação medidos
- [ ] PostgreSQL/outbox preservados

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `security_lead`
- `finance_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Comparar após métricas reais do worker Core.

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
