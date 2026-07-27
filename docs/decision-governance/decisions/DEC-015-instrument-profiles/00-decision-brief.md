# DEC-015 — Perfis instrumentais iniciais

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-015`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais instrumentos e quais propriedades técnicas entram no catálogo inicial?

## Por que esta decisão existe

Afinação correta não basta; extensão, tessitura, polifonia, respiração e técnicas afetam adaptação e tocabilidade.

## Prazo e gate

- trilha: `CORE`;
- fase: `CORE-2`;
- gate: `exit`;
- owner: `music_director`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_CORPUS`

## Opções conhecidas

- catálogo Core restrito
- expansão por família após gate
- perfis avançados versionados fora do Core

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-016`](../../evidence-register.yaml) — Fontes e revisão dos perfis instrumentais (`PLANNED`); devido antes de `CORE-2/T0`.

## Critérios de aprovação pré-definidos

- [ ] fontes musicais registradas
- [ ] revisão por instrumentista
- [ ] written/sounding range e transposição testados
- [ ] estado DRAFT→PRODUCTION_ENABLED
- [ ] properties para todos os pares Core

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `instrument_reviewers`
- `music_engineering_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Selecionar conjunto mínimo do Core e revisores.

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
