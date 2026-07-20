# Consistência entre áudio e partitura

> Status: canônico para trilhas D e Q. Revisão: 2026-07-20.

## Testes

- event_id -> occurrence -> timestamp;
- pitch soante;
- duração/onset;
- repeats/endings/jumps;
- tempo changes;
- A/B alignment;
- solo/mute por parte;
- cursor em compasso correto;
- seek e loop;
- sample fallback;
- pausa/retomada/background.

## Corpus mínimo

- repeat simples;
- primeira/segunda casa;
- D.C. al Fine;
- D.S. al Coda;
- pickup;
- fermata;
- mudança de compasso/tempo;
- instrumento transpositor;
- multiparte.

## Gate

Divergência de pitch ou ordem de eventos bloqueia score following. Erro de timbre/realismo pode ser warning se identificado.
