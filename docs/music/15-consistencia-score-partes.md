# Consistência entre score e partes

> Status: canônico para trilha E. Revisão: 2026-07-20.

## Princípio

Score do maestro e partes individuais são projeções do mesmo grafo musical canônico. Não devem ser gerados por pipelines independentes que possam divergir.

## Identidade estável

```text
work_id
score_version_id
part_id
staff_id
voice_id
event_id
measure_id
rehearsal_mark_id
```

Uma parte derivada preserva os IDs dos eventos semânticos e pode adicionar IDs editoriais próprios.

## Invariantes

- pitch de concerto de cada evento coincide entre score e parte;
- pitch escrito respeita instrumento e modo concert/written;
- onset, duração, ties, tuplets e repeats coincidem;
- dinâmica, articulação, letra e marca de ensaio aplicáveis são preservadas;
- cortes, tacets e cues são explícitos;
- numeração de compassos e rehearsal marks coincidem;
- transposição não é aplicada duas vezes;
- mudança no score invalida/regenera partes derivadas.

## Layout separado

Quebra de sistema/página, tamanho de pauta, cues e page turns pertencem à projeção editorial da parte. Podem diferir do score sem alterar semântica.

## Condensing e divisi

Condensing automático, divisi/unison e cues são trilhas próprias. Não entram como simples merge de vozes. Exigem identidade de músicos/players, regras de entrada/saída e revisão.

## Manifesto

Cada pacote registra:

```text
canonical_score_hash
score_artifact_hash
part_artifact_hashes
instrument_profile_versions
renderer_version
layout_policy_version
consistency_check_results
```

## Gate

- corpus de score/partes;
- properties de consistência;
- alterações incrementais;
- teste de transposição por instrumento;
- revisão de page turns;
- nenhum artefato público se uma parte divergir.
