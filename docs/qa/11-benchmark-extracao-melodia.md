# Benchmark de extração de melodia

> Status: canônico para trilha L. Revisão: 2026-07-20.

## Corpus

Deve conter:

- voz superior simples;
- melodia em voz interna;
- cruzamento de vozes;
- melodia migrando entre pautas;
- octave doubling;
- arpejos/acompanhamento Alberti;
- contracanto;
- letras;
- grace notes/ornamentos;
- polifonia densa;
- trechos sem melodia única consensual.

Cada segmento é anotado por pelo menos dois músicos e adjudicado.

## Splits

```text
train/development, quando houver modelo
calibration
frozen_release_test
adversarial_regression
```

O conjunto frozen não é usado para ajustar limiar após avaliação.

## Métricas

- event precision/recall/F1;
- onset/duration weighted F1;
- phrase boundary accuracy;
- voice-switch accuracy;
- accompaniment false inclusion rate;
- melody omission rate;
- ambiguity calibration;
- review burden por minuto/compasso;
- `verified_false_positive_rate`.

## Regras de gate

- limiares definidos antes da rodada;
- regiões ambíguas podem ser corretamente enviadas a review;
- cobertura automática não compensa falso positivo verificado;
- relatório por textura, não apenas média global;
- regressão em qualquer categoria crítica bloqueia release.
