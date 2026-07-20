# Contratos API ↔ frontend

> Status: canônico por referência ao OpenAPI e a `../backend/03-endpoints-api.md`.

## Convenções

```ts
type UUID = string
type ISODateTime = string
```

- base `/api/v1`;
- `credentials: 'include'`;
- mutações enviam `X-CSRF-Token`;
- criação de job envia `Idempotency-Key`;
- datas UTC ISO 8601;
- cliente TypeScript é gerado do OpenAPI;
- schemas de runtime validam fronteiras críticas;
- nunca usar `any` para DTO público.

## Sessão

```ts
type AnonymousSessionResponse = {
  session: { expires_at: ISODateTime }
  csrf_token: string
}
```

O cookie não aparece no DTO nem no código de estado do app.

## Capabilities

```ts
type CapabilitiesDTO = {
  input_formats: {
    musicxml: boolean
    generic_xml_musicxml: boolean
    mxl: boolean
    pdf_omr: boolean
  }
  output_formats: { musicxml: boolean; pdf: boolean }
  profile: {
    max_parts: number
    max_staves_per_part: number
    microtones: boolean
    unpitched_percussion: boolean
  }
  limits: {
    max_upload_bytes: number
    max_musicxml_measures: number
    max_musicxml_events: number
  }
}
```

## Instrumento e intervalo

```ts
type IntervalDTO = {
  diatonic_steps: number
  chromatic_semitones: number
  octave_change: number
  total_semitones: number
  name?: string
}

type InstrumentDTO = {
  id: string
  name: string
  family: string
  key_name: string
  written_to_concert: IntervalDTO
  default_clef: string
  aliases: string[]
  is_active: true
}
```

## Upload

```ts
type UploadStatus = 'quarantined' | 'validated' | 'rejected' | 'expired' | 'purged'

type UploadDTO = {
  upload_id: UUID
  original_filename: string
  input_format: 'musicxml' | 'mxl' | 'pdf'
  mime_type: string
  size_bytes: number
  sha256?: string
  status: UploadStatus
  expires_at: ISODateTime
  warnings: WarningDTO[]
}
```

O Core espera resposta de sucesso `validated`; quarentena/rejeição pode ser observável apenas conforme implementação do upload assíncrono.

## Job

```ts
type JobStatus =
  | 'queued'
  | 'running'
  | 'cancel_requested'
  | 'completed'
  | 'completed_with_warnings'
  | 'failed'
  | 'cancelled'

type ProcessingStage =
  | 'queued'
  | 'preprocessing'
  | 'recognizing'
  | 'normalizing'
  | 'transposing'
  | 'validating'
  | 'rendering'
  | 'finalizing'

type RetentionStatus = 'active' | 'expired' | 'purging' | 'purged'

type WarningDTO = {
  code: string
  message: string
  action?: string
  location?: { page?: number; measure?: string }
}

type PublicErrorSummaryDTO = {
  code: string
  message: string
  retryable: boolean
  correlation_id: string
}

type PublicJobDTO = {
  job_id: UUID
  status: JobStatus
  stage: ProcessingStage
  progress_pct: number
  retention_status: RetentionStatus
  source_instrument_id: string
  target_instrument_id: string
  output_interval: IntervalDTO & { name: string }
  warnings: WarningDTO[]
  error: PublicErrorSummaryDTO | null
  created_at: ISODateTime
  updated_at: ISODateTime
  finished_at: ISODateTime | null
  expires_at: ISODateTime | null
}

type JobStatusDTO = {
  job_id: UUID
  status: JobStatus
  stage: ProcessingStage
  progress_pct: number
  retention_status: RetentionStatus
  message: string
  warnings: WarningDTO[]
  error: PublicErrorSummaryDTO | null
  finished_at: ISODateTime | null
  expires_at: ISODateTime | null
  updated_at: ISODateTime
}
```

## Criar transposição

```ts
type CreateTranspositionRequest = {
  upload_id: UUID
  source_instrument_id: string
  target_instrument_id: string
  output_formats: Array<'musicxml' | 'pdf'>
  notation_policy: 'preserve_source_clef'
}

type CreateTranspositionResponse = {
  job_id: UUID
  status: 'queued'
  stage: 'queued'
  progress_pct: 0
  retention_status: 'active'
  source_instrument_id: string
  target_instrument_id: string
  output_interval: IntervalDTO & { name: string }
  expires_at: null
}
```

O request não contém intervalo. A resposta `202` é um resumo; o DTO completo é obtido em `GET /jobs/{job_id}`.

## Artefato

```ts
type ArtifactDTO = {
  artifact_id: UUID
  artifact_type: 'transposed_musicxml' | 'rendered_pdf'
  filename: string
  mime_type: string
  size_bytes: number
  sha256?: string
  expires_at: ISODateTime
}
```

## Erro HTTP

```ts
type ErrorDTO = {
  error: {
    code: string
    message: string
    correlation_id: string
    retryable: boolean
    field_errors: Array<{ field: string; code: string; message: string }>
  }
}
```

## Polling

- iniciar conforme `Retry-After`;
- backoff com jitter até máximo configurado;
- reduzir em background;
- parar em status terminal;
- `retention_status=expired|purging|purged` desabilita download;
- 401 tenta um único rebootstrap de sessão, sem assumir propriedade recuperável;
- 404 mostra item indisponível/sessão diferente;
- 429 respeita `Retry-After`.

## Testes de contrato

- gerar cliente no CI e falhar por diff não commitado;
- validar fixtures de todos os enums;
- rejeitar campo ausente/tipo inesperado em fronteira crítica;
- garantir ausência de `storage_key`, path, task id, stacktrace e confidence bruto;
- confirmar que UI usa capabilities para formatos e outputs.
