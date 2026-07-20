# Mapa de reprodução e semântica de áudio

> Status: canônico para trilhas D e Q. Revisão: 2026-07-20.

## Objetivo

Derivar uma linha do tempo executável a partir do grafo musical, preservando a relação entre evento, compasso e áudio.

## Duas linhas do tempo

```text
notated_time: posição escrita no score
performed_time: sequência efetivamente reproduzida após repeats/jumps/tempo
```

Um evento pode aparecer mais de uma vez em `performed_time` por causa de repetição.

## Playback map

```ts
type PlaybackOccurrence = {
  occurrence_id: string
  event_id: string
  pass_index: number
  start_seconds: number
  end_seconds: number
  measure_id: string
  beat_position: string
  sounding_pitch?: string
}
```

## Elementos obrigatórios

- tempo inicial e mudanças;
- compasso e anacruse;
- repeats e endings;
- D.C./D.S./coda/fine;
- fermatas e pausas;
- grace notes e ornaments conforme policy;
- swing/humanização separados da grade semântica;
- articulação e dinâmica dentro do perfil de síntese.

## Pitch

Áudio usa pitch soante. Instrumentos transpositores não devem soar no pitch escrito por engano. `A/B` compara versões no mesmo referencial sonoro.

## Síntese

O timbre é auxiliar. Sample/soundfont, licença, versão, latência e fallback entram no manifest. A ausência de timbre realista não altera a validade da notação.

## Score following

O cursor usa occurrences. Em regiões ambíguas ou sem mapeamento, a UI interrompe o follow e mantém playback, ou bloqueia o recurso conforme política.

## Gate

- corpus com repeats/jumps;
- tolerância de sincronização definida;
- event-to-audio mapping testado;
- pitch soante comparado ao grafo;
- sem clipping e com normalização;
- licença dos assets registrada.
