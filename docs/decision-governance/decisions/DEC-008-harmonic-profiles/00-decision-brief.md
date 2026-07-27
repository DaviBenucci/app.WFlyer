# DEC-008 — Perfis harmônicos do primeiro release

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-008`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais linguagens, modos, cromatismo, densidades e instrumentos entram no primeiro rollout de harmonização?

## Por que esta decisão existe

Enumerar escalas não define fraseado, cadências, tensão, condução de vozes nem adequação estilística.

## Prazo e gate

- trilha: `H`;
- fase: `H0`;
- gate: `exit`;
- owner: `music_director`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Opções conhecidas

- tonal clássico restrito
- popular funcional
- modal selecionado
- adiar linguagem não validada

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-009`](../../evidence-register.yaml) — Perfis harmônicos e revisão musical (`PLANNED`); devido antes de `H0`.

## Critérios de aprovação pré-definidos

- [ ] vocabulário e hard constraints documentados
- [ ] repertório de referência licenciado
- [ ] músicos revisores por linguagem
- [ ] limites de alteração e fidelidade definidos
- [ ] capabilities não aprovadas permanecem off

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `music_engineering_lead`
- `instrument_reviewers`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Criar perfis H0 antes de selecionar o solver.

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
