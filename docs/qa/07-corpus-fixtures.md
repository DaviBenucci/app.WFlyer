# Corpus e fixtures

## Estrutura

```text
tests/fixtures/
  musicxml/core/valid/
  musicxml/core/rejected/
  musicxml/expected/
  hostile/xml/
  hostile/mxl/
  hostile/pdf/
  omr/inputs/
  omr/expected/
  metadata/manifest.yml
```

## Manifesto obrigatório

Cada fixture registra:

```text
id
path
sha256
formato/versão
origem e licença
características musicais
perfil esperado: accept | reject | warning
instrumento de origem
resultados esperados por destino
data/revisor
```

Não incluir partitura protegida sem autorização/licença adequada.

## Classes Core válidas

- tonalidades maiores/menores;
- sem armadura/atonal simples;
- acidentes;
- mudança de tonalidade/compasso/clave;
- vozes e acordes em uma pauta;
- ties/tuplets/grace notes suportadas;
- harmony;
- instrumentos em C, Bb, Eb, F e transposição de oitava.

## Rejeitadas

- multiparte/multipauta;
- microtom;
- unpitched/percussão;
- tablatura;
- score-timewise/opus;
- XML malformado/hostil;
- metadata de origem contraditória.

## Golden e revisão

- manter original imutável;
- expected semântico em formato legível;
- golden de arquivo só para saída estável relevante;
- mudança de biblioteca não autoriza atualizar tudo automaticamente;
- revisão musical obrigatória para alteração de pitch/armadura/harmony.

## Corpus OMR

Antes de ativar PDF, cobrir digital, scan, ruído, rotação, resoluções, fontes, páginas múltiplas e falhas conhecidas. Separar treino/ajuste do conjunto de avaliação para não inflar métricas.

## Expansão do corpus

```text
tests/fixtures/
  polyphony/melody_labeled/
  polyphony/ambiguous/
  harmony/profiles/
  harmony/expected_constraints/
  instruments/playability/
  watermark/rendered/
  provenance/manifests/
```

Fixtures de melodia registram eventos selecionados por segmento e divergência entre revisores. Fixtures de harmonia registram hard constraints e avaliações humanas separadamente; não congelar uma única harmonização como “verdade absoluta”.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Proveniência e licença do corpus

Cada item declara:

```text
source_type
license_or_permission
allowed_purposes
contains_personal_data
may_train_models
may_benchmark
may_publish_excerpt
reviewers
split train|validation|release_hidden
```

`may_benchmark=true` não implica `may_train_models=true`.

## Partições obrigatórias

- unit fixtures sintéticas;
- regression corpus de incidentes;
- adversarial corpus;
- musician-reviewed benchmark;
- release-hidden corpus sem acesso do desenvolvimento/modelo;
- layout/print corpus;
- audio sync corpus.

Variações derivadas do mesmo score não podem vazar entre treino e release-hidden.

## Estratificação crítica do corpus

O corpus deve etiquetar, quando aplicável:

- instrumento/família e afinação;
- written/concert pitch;
- número de partes, pautas e vozes;
- textura: monodia, homofonia, contraponto, melodia acompanhada, arpejo;
- cross-staff, voice crossing, octave doubling e cue/ossia;
- tonalidade, modo, modulação, cromatismo, atonalidade;
- andamento, fórmula de compasso, tuplets e repeats;
- range/tessitura, técnica e dificuldade;
- qualidade de imagem/OMR;
- licença e origem;
- split de treino/calibração/validação/holdout.

O holdout de release não pode ser usado para escolher regra depois que o resultado foi visto. Incidente novo entra em suíte de regressão separada e também inspira caso adversarial não idêntico.
