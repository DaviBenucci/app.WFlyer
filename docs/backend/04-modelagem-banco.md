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

## Expansão para operações e garantia

Adicionar a `processing_jobs` quando as trilhas forem habilitadas:

```text
operation ENUM
operation_parameters_json
assurance_level
review_status
review_kind NULL
source_confirmation_revision NULL
melody_extractor_manifest_json NULL
harmony_profile_snapshot_json NULL
random_seed NULL
```

Novas tabelas:

```text
musical_reviews
melody_selections
harmony_variants
event_provenance
assurance_checks
verification_manifests
watermark_tokens
```

### musical_reviews

```text
id UUID PK
job_id FK
review_kind
revision INT
status ENUM(pending, submitted, superseded, cancelled)
payload_json
submitted_at
created_at
UNIQUE(job_id, review_kind, revision)
```

### event_provenance

```text
id UUID PK
job_id FK
artifact_id FK
output_event_id
origin_kind
source_event_ids_json
transformation_id
rule_or_model_version
metadata_json
```

### verification_manifests

```text
id UUID PK
job_id FK
public_token_hash UNIQUE
manifest_sha256
artifact_sha256
signature
key_id
assurance_level
revoked_at
created_at
```

`watermark_tokens` não armazena PII e não concede autorização. Payloads de revisão exigem schema e limite de tamanho; não armazenar SVG/partitura inteira em JSON.

Novos tipos de artefato:

```text
confirmed_source_musicxml
melody_selection
reduced_melody_musicxml
harmony_plan
harmonized_musicxml
arranged_musicxml
assurance_report
signed_manifest
watermarked_pdf
```

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Modelo avançado reservado

As tabelas abaixo entram apenas com suas capabilities, mas seus relacionamentos orientam IDs e manifests desde o Core.

### `musical_revisions`

```text
id uuid pk
project_id/session_owner_id
parent_revision_id nullable
revision_kind ORIGINAL|NORMALIZED|TRANSPOSED|MELODY_REVIEWED|HARMONIZED|ADAPTED|ENSEMBLE_SCORE|PART
artifact_id
semantic_hash
engine_manifest_id
created_by SYSTEM|USER|REVIEWER
created_at
```

### `musical_events`

Armazena ou referencia o índice semântico necessário a provenance/diff. Eventos pesados podem permanecer em artefato estruturado; o banco mantém IDs, revision, kind, location e hashes.

### `event_provenance`

Expandir com:

```text
source_revision_id
source_event_id nullable
result_revision_id
result_event_id
relation PRESERVED|TRANSFORMED|SELECTED|REMOVED|GENERATED|SPLIT|MERGED
reason_code
rule_or_model_version
human_decision_id nullable
```

### `analysis_regions`

Regiões versionadas de frase, tonalidade, modo, cadência, melodia, tensão ou harmonia, com alternativas e status de revisão.

### `playability_findings`

```text
revision_id
instrument_profile_version
region/event ids
rule_id
classification IMPOSSIBLE|DIFFICULT|NON_IDIOMATIC|COMFORTABLE|UNKNOWN
severity
explanation_code
suggested_actions jsonb
```

### `audio_renders` e `playback_map_entries`

Áudio aponta para revisão, engine/samples/licença, hash, loudness e versão do mapa. Ocorrências não substituem eventos semânticos.

### `ensemble_packages` e `ensemble_parts`

O pacote aponta para revisão-base e formação. Cada parte aponta para a mesma versão de score e possui `part_role`, instrumento, transposição, artifact e validation status.

### `review_sessions`, `annotations` e `musical_decisions`

Âncoras usam event/region/revision IDs, possuem `version`, `resolved_at`, autoria e auditoria. Texto é sanitizado e nunca é interpretado como instrução de modelo.

### `capability_rollouts`

Mantém capability, ambiente, cohort, versão do motor, início/fim, kill switch e critérios. O frontend não é fonte de verdade para habilitação.

## Regras de integridade avançadas

- revisão publicada é imutável;
- uma parte não pode apontar para score de versão diferente;
- provenance não pode formar ciclo inválido;
- evento `GENERATED` não possui source_event obrigatório, mas exige razão;
- decisão humana referencia exatamente a revisão analisada;
- `UNKNOWN` não pode ser persistido como `PASS`;
- purge respeita dependências e política de prova mínima.

## Entidades futuras versionadas

As tabelas abaixo são reservadas para capabilities avançadas e não devem ser criadas antecipadamente sem migration aprovada:

```text
MusicalRevision
Operation
OperationDependency
EventIdentity
EventProvenance
MusicalDiff
AnalysisRegion
AnalysisHypothesis
ReviewTask
ReviewDecision
PlayabilityFinding
InstrumentProfileVersion
PlaybackManifest
PlaybackOccurrence
EnsemblePackage
PartProjection
AnnotationThread
AnnotationAnchor
CapabilitySnapshot
FeatureFlagEvaluation
MusicalDecisionRecordRef
```

## Regras de modelagem

- revisões e artefatos são imutáveis;
- edição cria nova revisão com `parent_revision_id`;
- `EventIdentity` permanece estável quando o evento é semanticamente preservado;
- evento criado recebe `created_by_operation_id` e motivo;
- aprovação referencia exatamente revisão, analysis version e policy version;
- score e partes apontam para o mesmo `canonical_score_graph_id`;
- findings não são strings soltas: possuem código, severidade, localização e evidência;
- capability/engine/profile snapshots ficam registrados no job;
- exclusão lógica não reutiliza IDs;
- annotation anchor pode ficar `orphaned`, nunca ser remapeada silenciosamente.
