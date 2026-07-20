# Testes de consistência de score e partes

> Status: canônico para trilha E. Revisão: 2026-07-20.

## Properties

Para cada evento projetado:

```text
concert_pitch(score) == concert_pitch(part)
onset(score) == onset(part)
duration(score) == duration(part)
measure_id(score) == measure_id(part)
```

Pitch escrito difere conforme instrumento, mas deve recompor o mesmo pitch de concerto.

## Cenários

- instrumentos C/Bb/Eb/F;
- transposição de oitava;
- mudanças de clave/tonalidade;
- repeats;
- tacets/cues;
- instrument doubling futuro;
- written/concert conductor score;
- alteração incremental e regeneração.

## Gate

Uma divergência impede publicação do package inteiro.
