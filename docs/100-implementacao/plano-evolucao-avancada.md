# Plano de evolução avançada após o MVP Core

> Status: canônico. Revisão: 2026-07-20.

## Regra

Nenhuma trilha avançada começa por interface ou marketing. Primeiro são aprovados modelo, corpus, riscos, contratos e gate.

## F0 — Referências visuais internas

- validar `design-reference`;
- transformar protótipos em stories;
- produzir baselines internos;
- cobrir estados extremos;
- gate de fidelidade visual.

## D — Musical Diff e áudio comparativo

```text
D0 IDs/proveniência completa
D1 diff semântico
D2 UI de comparação
D3 playback graph/map
D4 áudio A/B
D5 gate de sincronização
```

## M/L — Modelo polifônico e melodia

```text
M0 event graph multiparte/pauta
M1 normalização avançada
L0 corpus anotado
L1 candidatos
L2 review
L3 redução/adaptação básica
L4 rollout limitado
```

## A — Tocabilidade e adaptação

```text
A0 perfis instrumentais revisados
A1 checker hard constraints
A2 difficulty/idiomatic warnings
A3 opções de adaptação
A4 UI/diff
A5 gate por instrumento
```

## H — Harmonia

```text
H0 análise tonal/modal/forma
H1 motor de regras/solver
H2 voicing/tocabilidade
H3 variantes e laboratório
H4 avaliação cega
H5 rollout por perfil
```

## E — Ensemble, score e partes

```text
E0 canonical score graph
E1 part projections
E2 arrangement roles
E3 consistency validator
E4 engraving/package
E5 gate de conjunto
```

## Q — Ensaio e colaboração

```text
Q0 playback estável
Q1 rehearsal mode
Q2 annotations
Q3 review sessions
Q4 offline/setlists
Q5 rollout
```

## Dependências

```text
Core -> F0
Core -> D0
M -> L
L + A -> H
M + A + H -> E
D + R -> Q
E + D -> rehearsal ensemble
```

## Critério de entrada em fase

- decisão pendente resolvida;
- owner;
- risco/pre-mortem;
- corpus e licença;
- schema/API draft;
- feature flag off;
- métricas pré-definidas.

## Critério de saída

- código e testes;
- evidência do corpus;
- revisão musical;
- segurança/privacidade;
- UI states;
- observabilidade;
- rollback;
- documentação atualizada.
