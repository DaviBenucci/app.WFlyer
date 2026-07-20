# Página Modo de Ensaio

> Status: canônico para trilha Q. Revisão: 2026-07-20.

## Rota

```text
/ensaio/{version_id}
```

## Layout

Prioriza partitura e transporte; esconde navegação secundária. Inspector abre sob demanda.

## Estados

```text
loading_assets
ready
playing
looping
paused
audio_unavailable
mapping_partial
offline_readonly
version_expired
annotation_conflict
```

## Saída do modo

Ao sair, posição e loop podem ser persistidos localmente sem token. Anotações sincronizadas usam revisão e conflito otimista.
