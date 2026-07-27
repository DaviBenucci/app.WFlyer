# DEC-013 — Schema final do grafo semântico musical

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-013`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual schema interno representa partes, pautas, vozes, medidas, eventos, relações e ocorrências de playback com IDs estáveis?

## Por que esta decisão existe

IDs e relações instáveis inviabilizam diff, revisão, áudio, colaboração, score/partes e reprodutibilidade.

## Prazo e gate

- trilha: `M`;
- fase: `M0`;
- gate: `exit`;
- owner: `music_engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- event graph tipado interno
- modelo hierárquico com relações explícitas
- extensões versionadas

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-014`](../../evidence-register.yaml) — Round trip e estabilidade do grafo semântico (`PLANNED`); devido antes de `M0/CORE-3`.

## Critérios de aprovação pré-definidos

- [ ] round trip do perfil suportado
- [ ] IDs estáveis entre serializações equivalentes
- [ ] cross-staff/grace/cue/ossia com política explícita
- [ ] versionamento e migração do schema
- [ ] nenhum dado canônico perdido

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `music_director`
- `qa_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Fechar antes do motor Core e da trilha M.

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
