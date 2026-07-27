# DEC-038 — Escopo e cadência de mutation testing

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais módulos e frequência justificam StrykerJS/mutmut sem tornar CI inviável?

## Por que esta decisão existe

Cobertura de linhas pode esconder testes fracos, mas mutation testing é caro.

## Prazo e gate

- trilha: `TOOL`;
- fase: `FUTURE-MUTATION`;
- gate: `entry`;
- owner: `qa_lead`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_COST_DATA`

## Opções conhecidas

- somente módulos críticos alterados
- execução noturna/semanal
- adiar até suíte madura

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-039`](../../evidence-register.yaml) — Piloto de mutation testing (`PLANNED`); devido antes de `CORE-8`.

## Critérios de aprovação pré-definidos

- [ ] piloto em motor musical/ledger
- [ ] tempo e sobreviventes medidos
- [ ] threshold e exceções aprovados
- [ ] não bloquear bootstrap prematuramente

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar depois de suíte unit/property estável.

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
