# DEC-006 — Expansão para multiparte e multipauta

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-006`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual modelo, UX e matriz suportam documentos com várias partes e pautas?

## Por que esta decisão existe

Tratar multiparte como loop simples pode misturar instrumentos, claves, vozes, score e partes.

## Prazo e gate

- trilha: `M`;
- fase: `M0`;
- gate: `exit`;
- owner: `music_engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Opções conhecidas

- seleção explícita de parte/pauta
- processamento de score completo em trilha futura
- manter Core de parte única

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-007`](../../evidence-register.yaml) — Corpus e round trip multiparte/multipauta (`PLANNED`); devido antes de `M0/M1`.

## Critérios de aprovação pré-definidos

- [ ] round trip semântico do corpus multiparte
- [ ] IDs estáveis e política de cross-staff
- [ ] UX de seleção e erros definida
- [ ] instrumentos por parte validados
- [ ] consistência score/partes testada

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `product_owner`
- `frontend_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Não implementar antes do schema semântico DEC-013.

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
