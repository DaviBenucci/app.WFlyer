# Adaptação idiomática instrumental

> Status: canônico para trilha A. Capacidade desabilitada no MVP Core.

## Definição

Adaptação idiomática transforma material confirmado para que seja executável e musicalmente natural no instrumento de destino. Ela é distinta de transposição: pode alterar oitava, voicing, articulação, respiração, distribuição entre mãos/cordas ou densidade.

## Operações possíveis

```text
OCTAVE_DISPLACEMENT
VOICE_REASSIGNMENT
CHORD_REVOICING
NOTE_OMISSION_WITH_APPROVAL
PHRASE_BREATHING
ARTICULATION_TRANSLATION
REGISTER_REBALANCE
HAND_OR_STRING_DISTRIBUTION
RHYTHMIC_SIMPLIFICATION_WITH_APPROVAL
CUE_OR_ACCOMPANIMENT_SPLIT
```

Cada operação possui política própria. Alterar pitch class, onset, duração ou forma exige nível de autorização mais alto do que mudar clave ou dedilhado sugerido.

## Pipeline

```text
fonte confirmada
-> perfil do destino e do intérprete
-> análise de textura/andamento/frases
-> detecção de violações rígidas
-> geração de alternativas locais
-> avaliação de tocabilidade
-> ranking semântico/idiomático
-> preview + diff
-> decisão do usuário
-> validação e nova versão
```

## Preservação

O usuário escolhe o orçamento:

```ts
type AdaptationBudget = {
  preserve_pitch_classes: boolean
  preserve_rhythm: boolean
  preserve_phrase_boundaries: boolean
  allow_octave_displacement: boolean
  allow_note_omission: boolean
  allow_revoicing: boolean
  allow_articulation_translation: boolean
  max_difficulty: 'beginner' | 'intermediate' | 'advanced' | 'professional'
}
```

## Casos por família

### Sopros e voz

- respiração e duração de frase;
- resistência e tessitura;
- articulações e ataques;
- projeção por registro;
- saltos e dedilhados difíceis no andamento.

### Cordas friccionadas

- cordas duplas/acordes executáveis;
- posições, cruzamentos e open strings;
- extensão de mão;
- arco, sustain e mudanças rápidas.

### Violão e instrumentos de corda dedilhada

- span entre trastes/cordas;
- voicings fisicamente possíveis;
- sustain e campanella;
- posição/capo/afinação;
- independência de vozes.

### Teclados

- distribuição entre mãos;
- span e densidade;
- cruzamentos;
- pedal e sustain;
- legibilidade em duas pautas.

### Percussão afinada

- número de baquetas;
- layout físico;
- sustain/damp;
- alcance e mudanças de instrumento.

## Regra de autoria

A aplicação não altera melodia, forma ou ritmo material apenas para “facilitar” sem preview e consentimento. Toda adaptação gera nova versão e diff.

## Gate

- perfis revisados por instrumentistas;
- corpus por instrumento e nível;
- hard constraints com zero falso negativo conhecido no corpus de release;
- warnings calibrados;
- avaliações humanas de idiomatismo;
- rollback e comparação disponíveis.
