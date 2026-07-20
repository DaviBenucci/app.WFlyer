# Análise de forma, fraseado e cadências

> Status: canônico para trilhas L, H, A e E. Capacidade inferencial.

## Objetivo

Produzir um mapa musical por regiões para apoiar extração de melodia, harmonização, respiração, page turns e arranjo.

## Saídas

```ts
type StructuralAnalysis = {
  sections: SectionAnalysis[]
  phrases: PhraseAnalysis[]
  motifs: MotifReference[]
  cadences: CadenceHypothesis[]
  tonal_regions: TonalRegion[]
  harmonic_rhythm_regions: HarmonicRhythmRegion[]
  confidence_regions: ConfidenceRegion[]
}
```

## Evidências

- barras, repetições, endings e marcas de ensaio;
- anacruse e duração de frases;
- slurs, respirações e letras;
- cadências melódicas e harmônicas;
- padrões rítmicos/motívicos;
- notas longas, pausas e fermatas;
- mudanças de tonalidade, modo, textura e dinâmica;
- sequência, repetição e contraste;
- indicação explícita do usuário.

## Cadências

Uma cadência é hipótese contextual, não rótulo derivado por um único acorde. O modelo pode registrar:

```text
authentic
half
plagal
deceptive
modal
phrase_end_without_harmonic_confirmation
unknown
```

A análise registra evidências, alternativas e escopo da região.

## Forma

O sistema pode sugerir seções `A`, `B`, `intro`, `verse`, `chorus`, `bridge` apenas quando houver evidência suficiente ou confirmação do usuário. Rótulos de gênero/forma não devem ser inventados com confiança indevida.

## Uso

- extração: evitar troca errática de voz no meio de uma frase;
- harmonização: posicionar ritmo harmônico e preservar cadências;
- adaptação: sugerir respirações e viradas;
- ensemble: distribuir funções por seção;
- ensaio: criar loops por frase/section.

## Ambiguidade

A análise pode ser parcial. Uma frase pode possuir múltiplos finais plausíveis. O sistema não bloqueia transposição por ausência de forma; bloqueia apenas operações que dependam daquela análise.

## Gate

- corpus anotado por pelo menos dois músicos;
- protocolo de concordância e adjudicação;
- métricas por boundary e por rótulo;
- UI para corrigir boundaries;
- versionamento e proveniência.
