# Arranjo para ensemble e orquestração assistida

> Status: canônico para trilha E. Capacidade criativa e futura.

## Definição

Arranjar para ensemble distribui funções musicais entre instrumentos e pode criar dobramentos, acompanhamentos, voicings e contrapontos. Não é uma transposição em lote.

## Entradas

- score/melodia/harmonia confirmados;
- formação selecionada;
- perfil de cada instrumentista;
- dificuldade alvo;
- linguagem e fidelidade;
- papel desejado por instrumento quando informado;
- limites de densidade e dobramento.

## Papéis

```text
MELODY
COUNTERMELODY
BASS
HARMONIC_SUPPORT
RHYTHMIC_SUPPORT
PEDAL
DOUBLING
CUE
REST/TACET
```

Papéis são atribuídos por região e podem mudar ao longo da obra.

## Restrições

- extensão/tocabilidade por instrumento;
- balanceamento e registro;
- densidade e clareza da melodia;
- transposição escrita;
- respiração/sustain;
- dobramentos permitidos;
- limite de alterações da fonte;
- consistência score/partes.

## Saídas

```text
conductor_score_written_pitch
conductor_score_concert_pitch opcional
individual_parts
rehearsal_audio
transformation_manifest
musical_diff
playability_reports
```

## Regra criativa

O sistema entrega variantes e explicações. Não imita literalmente arranjo de artista específico nem afirma reproduzir intenção autoral. Perfis de estilo são genéricos e licenciados/documentados.

## Gate

- modelo multiparte maduro;
- perfis instrumentais;
- harmonização/forma confirmadas quando usadas;
- score/parts consistency;
- painel de músicos revisores;
- rollback por versão.
