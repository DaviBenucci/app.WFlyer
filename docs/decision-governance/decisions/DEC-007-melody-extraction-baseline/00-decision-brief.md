# DEC-007 — Baseline de extração de melodia

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-007`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual baseline identifica a linha melódica por região sem confundir acompanhamento, contracanto ou voz interna?

## Por que esta decisão existe

A linha mais aguda não é regra universal e erros silenciosos mudam o conteúdo musical.

## Prazo e gate

- trilha: `L`;
- fase: `L1`;
- gate: `exit`;
- owner: `music_engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- regras simbólicas
- otimização por caminho/frase
- modelo treinado apenas com governança aprovada
- combinação com revisão humana

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-008`](../../evidence-register.yaml) — Corpus anotado e benchmark de melodia (`PLANNED`); devido antes de `L0/L1`.

## Critérios de aprovação pré-definidos

- [ ] corpus anotado por frase e por mais de um músico
- [ ] métricas de precisão/recall por evento e frase
- [ ] estratos cross-staff, voz interna e dobramento
- [ ] limiar de ambiguidade e alternativas visíveis
- [ ] zero selo verificado quando houver divergência material

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `qa_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Rotular corpus L0 antes de comparar algoritmos.

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
