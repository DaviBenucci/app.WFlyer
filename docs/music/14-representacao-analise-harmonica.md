# Representação de análise harmônica

> Status: canônico para trilha H. Revisão: 2026-07-20.

## Objetivo

Separar símbolos impressos, hipótese analítica e plano de harmonização.

## Camadas

```text
source_harmony_symbols
observed_verticalities
analytical_hypotheses
confirmed_harmonic_map
harmony_plan_variants
rendered_harmony_symbols
```

Uma cifra existente na fonte não é automaticamente uma análise funcional completa. Uma simultaneidade de notas não é automaticamente um acorde estrutural.

## Modelo por região

```ts
type HarmonicRegion = {
  region_id: string
  range: MusicalRange
  tonal_center?: PitchClass
  mode?: ModeId
  chord_hypotheses: ChordHypothesis[]
  selected_hypothesis_id?: string
  non_chord_tones: NonChordToneAnalysis[]
  cadence_relation?: string
  source: 'encoded' | 'inferred' | 'user_confirmed'
  ambiguity: 'none' | 'material' | 'blocking'
}
```

## Notas não harmônicas

Classificações possíveis incluem passagem, bordadura, suspensão, antecipação, apogiatura, pedal e escape. A classificação é contextual e pode permanecer `unknown`.

## Modos e cromatismo

- tonalidade e modo são mapeados por região;
- mistura modal, dominantes secundárias e tonicizações são registradas sem forçar modulação global;
- modos gregos preservam graus característicos;
- enarmonia analítica não reescreve a fonte sem operação explícita.

## MusicXML

`<harmony>` pode representar símbolos e análise funcional, mas o W_Flyer mantém o manifesto analítico separado para:

- alternativas;
- confidence e evidências;
- versionamento;
- decisões do usuário;
- dados que não devem ser impressos.

Ao exportar MusicXML, somente a hipótese confirmada e autorizada é serializada.

## Gate

- análise não altera notas;
- hipóteses permanecem alternativas até confirmação/política;
- o harmonizador usa snapshot confirmado;
- mudanças na análise invalidam variantes derivadas;
- corpus inclui tonal, modal, cromático e regiões ambíguas.
