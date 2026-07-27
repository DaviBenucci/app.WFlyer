# DEC-005 — Suporte a MusicXML comprimido (.mxl)

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-005`. Implementação autorizada: **não**.

## Pergunta de decisão

O produto deve aceitar .mxl e sob quais limites de extração?

## Por que esta decisão existe

MXL é um container ZIP e amplia riscos de zip slip, zip bomb, excesso de entries e recursos externos.

## Prazo e gate

- trilha: `CORE`;
- fase: `FUTURE-MXL`;
- gate: `entry`;
- owner: `security_lead`.

## Bloqueios atuais

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_BENCHMARK`

## Opções conhecidas

- manter somente MusicXML não comprimido
- habilitar MXL com parser de container dedicado

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-006`](../../evidence-register.yaml) — Corpus hostil e parser seguro de MXL (`PLANNED`); devido antes de `FUTURE-MXL`.

## Critérios de aprovação pré-definidos

- [ ] corpus hostil aprovado
- [ ] limites de entries e tamanho descompactado definidos
- [ ] paths normalizados sem escape
- [ ] recursos referenciados validados
- [ ] telemetria e erro público definidos

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `qa_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Manter desabilitado até um spike de container seguro.

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
