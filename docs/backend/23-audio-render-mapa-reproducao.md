# Backend de áudio e mapa de reprodução

> Status: canônico para trilhas D e Q. Revisão: 2026-07-20.

## Serviços

```text
PlaybackGraphBuilder
PlaybackMapValidator
AudioRendererAdapter
LoudnessNormalizer
AudioArtifactPublisher
```

## Contrato

Áudio é gerado a partir da versão canônica e do `performed_time`. O renderer recebe eventos soantes, não pitches escritos sem conversão.

## Artefatos

```text
playback_graph_json
audio_preview_ogg|mp3|wav conforme decisão
playback_map_json
audio_render_report
```

Formatos e codecs exigem decisão de licença e compatibilidade.

## Validações

- número de occurrences;
- monotonicidade temporal;
- ausência de overlap impossível do renderer;
- pitch soante;
- duração total;
- repeats/jumps;
- loudness e clipping;
- hash/version do sample set.

## Segurança

- sem URL arbitrária de soundfont;
- assets allowlisted e licenciados;
- renderer em sandbox quando externo;
- limites de duração/canais/tamanho;
- artefatos privados e expirados.
