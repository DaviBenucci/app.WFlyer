# Processamento de job

## Objetivo

Gerenciar transposição como job assíncrono, evitando processamento pesado na requisição HTTP principal.

## Fluxo

```text
POST /api/transpositions
API cria processing_jobs
API publica tarefa na fila
Worker executa pipeline
Worker registra job_events
Worker atualiza progress/status
Frontend acompanha status
```

## Status oficiais

```text
uploaded
queued
processing
transposing
rendering
completed
failed
expired
cancelled
```

## Progresso sugerido

```text
queued: 0
processing: 20
transposing: 60
rendering: 85
completed: 100
failed: valor atual
expired: valor atual
cancelled: valor atual
```

## Erros

Cada erro deve ter:

```text
error_code
public_error_message
correlation_id
job_event
```

O público nunca recebe stacktrace, path físico ou log bruto.

## Critérios de aceite

- API responde rápido com `job_id`.
- Worker processa fora da API.
- Status atualiza por etapa.
- Falha registra evento e mensagem pública segura.
- Job finaliza em estado terminal.
