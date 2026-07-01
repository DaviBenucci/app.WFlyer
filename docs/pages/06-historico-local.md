# Tela Histórico local

## Rota

```text
/historico
```

## Objetivo

Mostrar transposições recentes armazenadas no navegador/dispositivo, sem exigir conta.

## Escopo MVP

O histórico guarda apenas metadados seguros:

```text
job_id
original_filename sanitizado
source_instrument_id
target_instrument_id
transpose_interval
status
created_at
expires_at
artifact_types
```

## Componentes

- `LocalHistory`.
- `LocalHistoryItem`.
- `RetentionBadge`.
- `ClearHistoryButton`.
- `EmptyState`.

## Regras

- Não guardar arquivo original automaticamente.
- Não guardar MusicXML completo.
- Não guardar PDF final.
- Não guardar `storage_key`.
- Não guardar stacktrace.
- Usuário pode limpar histórico local.
- Item expirado orienta nova transposição.

## Estados

```text
empty
loaded
search_empty
available
expired
removed_local
storage_unavailable
```

## Critérios de aceite

- Histórico aparece após job concluído.
- Item expirado informa indisponibilidade de download.
- Usuário consegue remover histórico local.
- Falha de armazenamento local não quebra a aplicação.
