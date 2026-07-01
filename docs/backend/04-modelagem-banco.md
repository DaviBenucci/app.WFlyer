# Modelo de dados do MVP

## Tabelas mínimas

```text
instruments
uploads
processing_jobs
generated_artifacts
job_events
```

## instruments

```text
id
name
family
key_name
written_to_concert
is_active
created_at
updated_at
```

Regras:

- `id` deve ser slug estável.
- `written_to_concert` é obrigatório.
- Instrumento inativo não pode ser usado em novo job.

## uploads

```text
id
original_filename
mime_type
size_bytes
storage_key
status
expires_at
created_at
updated_at
```

Regras:

- `storage_key` é interno e nunca aparece em DTO público.
- `original_filename` não pode ser usado como path físico.
- `status` inicial é `uploaded`.

## processing_jobs

```text
id
upload_id
source_instrument_id
target_instrument_id
status
progress
error_code
error_message
correlation_id
started_at
finished_at
created_at
updated_at
```

Regras:

- `progress` deve ficar entre 0 e 100.
- `error_message` deve conter mensagem segura para suporte interno; a API pública deve filtrar o que for técnico.
- `correlation_id` deve conectar API, worker e logs.

## generated_artifacts

```text
id
job_id
artifact_type
filename
mime_type
size_bytes
storage_key
expires_at
created_at
```

Regras:

- `artifact_type` inicial: `final_musicxml`, `final_pdf` quando renderização PDF estiver disponível.
- `storage_key` é interno.
- Artefato expirado não pode ser baixado.

## job_events

```text
id
job_id
event_type
message
metadata_json
created_at
```

Regras:

- Eventos públicos devem conter mensagem segura.
- `metadata_json` não pode guardar stacktrace, segredo ou path físico quando puder aparecer em consulta pública.

## Status possíveis

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

## Índices recomendados

```text
uploads(status)
uploads(expires_at)
processing_jobs(upload_id)
processing_jobs(status)
processing_jobs(created_at)
processing_jobs(correlation_id)
generated_artifacts(job_id)
generated_artifacts(expires_at)
job_events(job_id, created_at)
```

## Fora do modelo mínimo

As tabelas abaixo são futuras e não devem bloquear o MVP:

- `users`;
- `plans`;
- `subscriptions`;
- `cloud_library`;
- `shared_scores`;
- `admin_audit_logs`;
- `push_subscriptions`.
