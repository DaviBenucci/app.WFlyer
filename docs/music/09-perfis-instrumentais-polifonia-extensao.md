# Perfis instrumentais, polifonia e extensão

> Status: canônico para expansão do catálogo. Revisão: 2026-07-20.

## Objetivo

Modelar o que um instrumento pode executar, além da sua afinação. A família do instrumento não é suficiente para decidir transposição, redução, harmonização ou arranjo.

## Modelo

```ts
type InstrumentCapabilities = {
  polyphony_class: 'monophonic' | 'limited_polyphonic' | 'polyphonic'
  max_simultaneous_notes?: number
  written_range: { min: string; max: string }
  comfortable_range?: { min: string; max: string }
  preferred_clefs: string[]
  sounding_octave_behavior: number
  sustain_model: 'breath' | 'bow' | 'pluck' | 'keyboard' | 'other'
  max_span_semitones?: number
  supports_double_stops?: boolean
  supports_chord_symbols?: boolean
  supports_multiple_staves?: boolean
  capability_version: string
}
```

Valores de extensão e técnica exigem revisão por instrumentista e podem variar por nível. O catálogo deve distinguir limite absoluto de faixa confortável.

## Classes

### Monofônico

Uma nota principal por instante, desconsiderando técnicas estendidas. Exemplos usuais incluem muitos sopros e voz solo.

### Polifonia limitada

Permite duplas, acordes ou múltiplas cordas com restrições físicas. O motor precisa de regras específicas de instrumento; `max_simultaneous_notes` isolado não basta.

### Polifônico

Permite múltiplas vozes com maior liberdade, ainda sujeito a extensão, span, mãos, pedais e técnica.

## Regras de operação

- `TRANSPOSE` preserva todas as notas somente quando o destino suporta a textura.
- Origem polifônica para destino monofônico exige `EXTRACT_MELODY` ou seleção de voz.
- Origem monofônica para destino polifônico permanece monofônica até o usuário solicitar `HARMONIZE`.
- Revoicing, drop de notas, mudança de oitava e divisão entre mãos pertencem a `ARRANGE_FOR_INSTRUMENT`.
- A API deve retornar capacidades e motivos de incompatibilidade antes de criar o job.

## Teclado

Uma pauta em clave de Sol pode conter acordes, vozes independentes, contracantos e notas de acompanhamento. A aplicação não deve presumir que a voz superior seja sempre a melodia nem que toda nota na pauta de Sol pertença à mesma função.

Para teclado em duas pautas, o gate futuro deve analisar ambas as pautas, cruzamento de mãos/vozes e contexto harmônico. O MVP Core continua rejeitando multipauta até esse gate.

## Validação de tocabilidade

O validador separa:

- `absolute_range_violation`: impossível/fora do cadastro;
- `comfortable_range_warning`: possível, mas fora da faixa recomendada;
- `polyphony_violation`: simultaneidade incompatível;
- `span_violation`: abertura ou combinação impraticável;
- `technique_review_required`: regra não modelada com segurança.

Uma violação rígida bloqueia publicação. Warnings de conforto exigem confirmação ou alternativa de oitava/revoicing.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Perfil de capacidade completo

```ts
type InstrumentCapabilityProfile = {
  profileVersion: string
  writtenRange: PitchRange
  soundingRange: PitchRange
  comfortableRanges: RegisterProfile[]
  nominalPolyphony: number
  practicalPolyphony: number
  maximumChordSpan?: Interval
  supportsSustain: boolean
  breathDependent: boolean
  supportsDoubleStops: boolean
  supportsMultiphonics: 'NO' | 'SPECIAL_TECHNIQUE' | 'YES'
  preferredClefs: Clef[]
  difficultyRules: RuleReference[]
  idiomaticPatterns: RuleReference[]
  discouragedPatterns: RuleReference[]
  reviewerApproval: ApprovalReference
}
```

## Regras de prudência

- técnica especial nunca é presumida;
- extensão publicada por fabricante não equivale a faixa confortável;
- acordes possíveis dependem de disposição, duração e contexto, não só de número de notas;
- dificuldade depende de andamento e vizinhança;
- perfil pedagógico não redefine impossibilidade física;
- ausência de regra retorna `UNKNOWN`.
