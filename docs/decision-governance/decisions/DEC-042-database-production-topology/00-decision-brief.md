# DEC-042 — Topologia e dimensionamento do banco de produção

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual configuração, pool, índices, retenção e HA suportam jobs, ledger, auditoria e webhooks?

## Por que esta decisão existe

Sobrecarga, locks ou migrations ruins podem parar processamento e billing.

## Prazo e gate

- trilha: `INF`;
- fase: `INF2`;
- gate: `exit`;
- owner: `database_owner`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_COST_DATA`

## Opções conhecidas

- RDS PostgreSQL Multi-AZ planejado
- instância menor em pré-produção
- read replicas somente por evidência

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-043`](../../evidence-register.yaml) — Benchmark e failover do PostgreSQL (`PLANNED`); devido antes de `INF2`.

## Critérios de aprovação pré-definidos

- [ ] modelo e consultas reais
- [ ] carga concorrente e p95/p99
- [ ] failover/PITR testados
- [ ] pool/timeouts/índices
- [ ] crescimento de auditoria/ledger
- [ ] custo mensal aprovado

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `platform_lead`
- `security_lead`
- `finance_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Decidir após corte vertical e teste de carga.

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
