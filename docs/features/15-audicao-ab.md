# Audição A/B sincronizada

> Status: canônico para trilha D. Capacidade futura.

## Objetivo

Comparar fonte e resultado no mesmo ponto musical, com pitch soante e mapa de reprodução confiável.

## Fluxo

```text
versão de origem + versão de resultado
-> gerar/validar playback maps
-> renderizar áudio compatível
-> normalizar loudness
-> alinhar occurrences
-> disponibilizar A/B
```

## Regras

- troca A/B preserva compasso, beat e occurrence;
- origem e resultado são nomeados de forma inequívoca;
- diferenças de timbre não são apresentadas como diferenças de nota;
- loudness é normalizado para evitar preferência enganosa;
- tempo de reprodução pode ser alterado sem modificar o artefato musical;
- nenhuma reprodução automática ao abrir;
- áudio expira conforme artefato e licença.

## Artefatos

```text
source_preview_audio
target_preview_audio
playback_map
waveform_summary opcional
audio_render_manifest
```

## Gate

- consistência pitch/evento;
- repeats/jumps testados;
- alinhamento dentro da tolerância;
- fallback de sample identificado;
- acessibilidade e política de autoplay;
- custos e licenças aprovados.
