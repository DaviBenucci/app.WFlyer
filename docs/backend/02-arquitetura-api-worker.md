# Arquitetura API + Worker

## Componentes internos

```text
frontend
api
database
storage_controlado
queue
worker
music_engine
```

## Princípio

O processamento musical não deve acontecer dentro da requisição HTTP principal. A API cria e consulta jobs; o worker processa.

## Fluxo de criação de job

```text
POST /api/transpositions
  validar payload
  validar upload existente e não expirado
  validar instrumentos ativos
  calcular intervalo_escrito
  criar processing_jobs(status=queued)
  registrar job_events(event_type=queued)
  publicar job_id na fila
  retornar 202 com job_id e status inicial
```

## Fluxo de worker

```text
process_transposition(job_id)
  carregar job
  marcar processing
  ler arquivo original ou MusicXML controlado
  extrair representação musical
  marcar transposing
  aplicar regra musical central
  validar resultado
  marcar rendering
  gerar artefato final
  registrar generated_artifacts
  marcar completed
```

## Status consultável

O frontend deve consultar:

```text
GET /api/jobs/{job_id}/status
```

O polling para quando o job chegar em:

```text
completed
failed
expired
cancelled
```

## Falhas

- Erro determinístico não deve ser repetido indefinidamente.
- Erro transitório pode ter retentativa limitada.
- Falha permanente deve marcar job como `failed`.
- Mensagem pública deve ser amigável.
- Erro interno fica apenas em log controlado com `correlation_id`.

## Critérios de aceite

- API retorna `202 Accepted` ao criar job.
- Worker consome job sem bloquear API.
- Status muda durante processamento.
- Falha no worker vira status seguro.
- Frontend consegue acompanhar progresso.
