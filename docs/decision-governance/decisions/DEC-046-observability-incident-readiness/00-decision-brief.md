# DEC-046 — Observabilidade, alertas e prontidão de incidentes

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais logs, métricas, traces, alertas, retenções e runbooks são necessários para detectar e responder às falhas críticas do W_Flyer?

## Por que esta decisão existe

Sem sinais e alertas acionáveis, a redundância técnica não garante detecção, diagnóstico ou recuperação dentro das metas operacionais.

## Prazo e gate

- trilha: `INF`;
- fase: `INF2`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_COST_DATA`

## Opções conhecidas

- stack gerenciada da AWS
- stack alternativa aprovada por custo e operação

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-047`](../../evidence-register.yaml) — Teste de observabilidade, alertas e resposta a incidentes (`PLANNED`); devido antes de `INF2/LAUNCH`.

## Critérios de aprovação pré-definidos

- [ ] SLIs para web, API, jobs, banco, storage, billing e fiscal definidos
- [ ] correlation IDs e tracing nos fluxos críticos
- [ ] nenhum segredo ou conteúdo musical sensível em logs
- [ ] alertas ligados a owner, severidade e runbook
- [ ] tabletop/fault injection comprova detecção e escalonamento
- [ ] overhead, cardinalidade, retenção e custo aprovados

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir catálogo inicial de sinais durante o corte vertical e validar sob carga antes de produção.

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
