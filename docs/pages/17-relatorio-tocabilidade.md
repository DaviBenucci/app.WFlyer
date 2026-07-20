# Página de relatório de tocabilidade

> Status: canônico para trilha A. Revisão: 2026-07-20.

## Rota

```text
/tocabilidade/{version_id}/{instrument_profile_id}
```

## Objetivo

Apresentar findings por severidade, registro e frase, com alternativas de adaptação.

## Composição

```text
PlayabilityHeader
RegisterOverview
FindingNavigation
ScoreHighlight
OptionInspector
```

## Estados

```text
analyzing
playable
warnings
adaptation_required
unmodeled_technique
profile_changed
```

## Regra

A página não transforma automaticamente ao abrir. Aplicar opções cria novo job/version.
