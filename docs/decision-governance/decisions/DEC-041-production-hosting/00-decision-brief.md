# DEC-041 — Arquitetura final de hospedagem e ambientes

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual topologia de produção sustenta web, API, workers, banco, storage, filas e recuperação com custo aceitável?

## Por que esta decisão existe

Um único VPS concentra falhas; arquitetura excessiva antes de carga real pode inviabilizar o produto.

## Prazo e gate

- trilha: `INF`;
- fase: `INF0`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_SECURITY_REVIEW`

## Opções conhecidas

- AWS São Paulo como alvo planejado
- alternativa gerenciada somente se comparada
- VPS apenas dev/demo

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-042`](../../evidence-register.yaml) — Modelo de capacidade, custo e arquitetura de hosting (`PLANNED`); devido antes de `INF0/INF2`.

## Critérios de aprovação pré-definidos

- [ ] cenários inicial/provável/pico
- [ ] estimativa mensal e gatilhos de escala
- [ ] isolamento de ambientes/contas
- [ ] backup/restore/observabilidade
- [ ] infraestrutura reproduzível
- [ ] dados no Brasil avaliados

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `security_lead`
- `finance_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Usar AWS como arquitetura-alvo, mas decidir dimensionamento após benchmarks.

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
