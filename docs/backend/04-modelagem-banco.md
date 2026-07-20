# Modelo de dados do MVP

> Status: canônico. Revisão: 2026-07-20.

## Tabelas

```text
anonymous_sessions
instruments
uploads
processing_jobs
processing_attempts
generated_artifacts
job_events
outbox_events
```

## anonymous_sessions

```text
id UUID PK
token_hash BYTEA/STRING UNIQUE NOT NULL
csrf_secret_hash BYTEA/STRING NOT NULL
expires_at TIMESTAMPTZ NOT NULL
last_seen_at TIMESTAMPTZ
revoked_at TIMESTAMPTZ
created_at TIMESTAMPTZ NOT NULL
```

Somente hashes são persistidos. O valor do cookie nunca aparece em log.

## instruments

```text
id SLUG PK
name
family
key_name
written_to_concert_diatonic INT
written_to_concert_chromatic INT
written_to_concert_octave INT
default_clef
aliases_json
is_pitched BOOL
is_active BOOL
catalog_version
created_at
updated_at
```

`total_semitones` é derivado. O job guarda snapshot do preset para reprodutibilidade.

## uploads

```text
id UUID PK
session_id FK
original_filename_sanitized
input_format
reported_mime_type
detected_mime_type
size_bytes
sha256 UNIQUE POR SESSAO OPCIONAL
storage_key
status
validation_error_code
expires_at
validated_at
deleted_at
created_at
updated_at
```

Status conforme `16-maquina-estados.md`.

## processing_jobs

```text
id UUID PK
session_id FK
upload_id FK
idempotency_key_hash
request_fingerprint
source_instrument_id FK
target_instrument_id FK
source_instrument_snapshot_json
target_instrument_snapshot_json
interval_diatonic
interval_chromatic
interval_octave
interval_total_semitones
notation_policy
requested_output_formats_json
status
stage
progress_pct
retention_status
warning_count
public_error_code
public_error_message
correlation_id
engine_manifest_json
cancel_requested_at
started_at
finished_at
expires_at NULL ATE SUCESSO
purged_at
created_at
updated_at
```

Constraint única: `(session_id, idempotency_key_hash)`.

## processing_attempts

```text
id UUID PK
job_id FK
attempt_number INT
queue_task_id INTERNAL
status
worker_version
music_engine_version
omr_engine_version NULL
renderer_version NULL
started_at
finished_at
internal_error_class
internal_error_fingerprint
created_at
```

`queue_task_id` e detalhes internos nunca são públicos.

## generated_artifacts

```text
id UUID PK
job_id FK
attempt_id FK
artifact_type
visibility ENUM(internal, public)
filename_sanitized
mime_type
size_bytes
sha256
storage_key
format_version
expires_at
purged_at
created_at
```

Constraint recomendada: um artefato público ativo por `(job_id, artifact_type)`; retries substituem por transação/reconciliação controlada.

Tipos iniciais:

```text
input_original
raw_musicxml
normalized_musicxml
transposed_musicxml
rendered_pdf
processing_report
```

## job_events

```text
id UUID PK
job_id FK
attempt_id FK NULL
visibility ENUM(internal, public)
event_type
public_message NULL
metadata_json
created_at
```

Eventos públicos usam payload allowlisted. Stacktrace e paths nunca entram em evento público.

## outbox_events

Usada para publicar jobs sem perder consistência entre banco e Redis:

```text
id UUID PK
aggregate_type
aggregate_id
event_type
payload_json
published_at
attempts
created_at
```

## Índices

```text
anonymous_sessions(token_hash)
anonymous_sessions(expires_at)
uploads(session_id, created_at)
uploads(status, expires_at)
processing_jobs(session_id, created_at)
processing_jobs(status, stage)
processing_jobs(retention_status, expires_at)
processing_jobs(correlation_id)
processing_attempts(job_id, attempt_number)
generated_artifacts(job_id, visibility)
generated_artifacts(expires_at, purged_at)
job_events(job_id, created_at)
outbox_events(published_at, created_at)
```

## Integridade

- `progress_pct` entre 0 e 100;
- intervalos e snapshots imutáveis após criação do job;
- sessão do job deve ser a mesma do upload;
- artefato público só para job terminal de sucesso;
- purge não apaga evidência mínima necessária imediatamente, mas remove bytes e dados sensíveis conforme política;
- deleção física e status de retenção são reconciliáveis.
