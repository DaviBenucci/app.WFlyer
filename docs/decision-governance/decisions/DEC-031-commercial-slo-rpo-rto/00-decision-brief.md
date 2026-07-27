# DEC-031 — Metas comerciais de SLO, RPO e RTO

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-033`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais metas de disponibilidade, perda máxima e recuperação são sustentáveis pelo orçamento?

## Por que esta decisão existe

Prometer SLA sem arquitetura e exercícios comprovados cria risco contratual e operacional.

## Prazo e gate

- trilha: `INF`;
- fase: `INF3`;
- gate: `exit`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Opções conhecidas

- metas internas sem SLA
- SLA comercial somente após histórico
- tiers institucionais futuros

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-032`](../../evidence-register.yaml) — Exercício de backup, restore e DR (`PLANNED`); devido antes de `INF3`.

## Critérios de aprovação pré-definidos

- [ ] RPO/RTO testados em restore
- [ ] SLO calculado por user journey
- [ ] orçamento e redundância alinhados
- [ ] exclusões e manutenção definidas
- [ ] não publicar SLA antes de validação

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `platform_lead`
- `finance_owner`
- `support_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar DR em staging antes de aprovar.

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
