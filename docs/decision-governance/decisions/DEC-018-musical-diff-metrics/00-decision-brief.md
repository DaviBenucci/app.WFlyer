# DEC-018 — Métricas e cobertura do Musical Diff

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-018`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual cobertura de proveniência/diff é necessária para cada tipo de transformação?

## Por que esta decisão existe

Um diff parcial pode ocultar nota criada, removida ou alterada e invalidar o selo de verificação.

## Prazo e gate

- trilha: `D`;
- fase: `D0`;
- gate: `exit`;
- owner: `qa_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- cobertura por evento e relação
- cobertura por operação
- bloqueio por gaps materiais

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-019`](../../evidence-register.yaml) — Cobertura e testes do Musical Diff (`PLANNED`); devido antes de `D0`.

## Critérios de aprovação pré-definidos

- [ ] categorias de mudança canônicas
- [ ] tolerâncias definidas por operação
- [ ] gaps materiais bloqueiam garantia
- [ ] metamorphic tests
- [ ] UI não recalcula correspondências

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_engineering_lead`
- `music_director`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir junto ao schema DEC-013.

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
