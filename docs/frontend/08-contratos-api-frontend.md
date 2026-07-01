# Contratos API <-> Frontend

## Objetivo

Evitar divergência entre frontend e backend por meio de DTOs claros, validados e seguros.

Contrato detalhado dos endpoints: `docs/backend/03-endpoints-api.md`.

## Convenções

- Datas em ISO 8601 UTC.
- IDs em UUID, exceto `InstrumentDTO.id`, que usa slug estável.
- Erros públicos usam envelope `{ "error": ... }`.
- Nunca expor path físico.
- Nunca expor `storage_key`.
- Nunca expor stacktrace.
- Nunca expor métricas internas ao usuário.
- O frontend deve validar DTOs com Zod ou estratégia equivalente.

## ErrorDTO

```ts
type ErrorDTO = {
  error: {
    code: string
    message: string
    correlation_id: string
  }
}
```

## InstrumentDTO

```ts
type InstrumentDTO = {
  id: string
  name: string
  family: string
  key_name: string
  written_to_concert: number
  transposes_octave: boolean
  is_active: boolean
  notes?: string
}
```

## UploadDTO

```ts
type UploadDTO = {
  upload_id: string
  original_filename: string
  mime_type:
    | 'application/pdf'
    | 'application/vnd.recordare.musicxml+xml'
    | 'application/xml'
    | 'text/xml'
  size_bytes: number
  status: 'uploaded'
  expires_at: string
}
```

## CreateTranspositionRequest

```ts
type CreateTranspositionRequest = {
  upload_id: string
  source_instrument_id: string
  target_instrument_id: string
}
```

## CreateTranspositionResponse

```ts
type CreateTranspositionResponse = {
  job_id: string
  status: 'queued'
  progress: number
  source_instrument_id: string
  target_instrument_id: string
  transpose_interval: number
  expires_at: string
}
```

## JobStatus

```ts
type JobStatus =
  | 'uploaded'
  | 'queued'
  | 'processing'
  | 'transposing'
  | 'rendering'
  | 'completed'
  | 'failed'
  | 'expired'
  | 'cancelled'
```

## PublicJobDTO

```ts
type PublicJobDTO = {
  job_id: string
  upload_id: string
  status: JobStatus
  progress: number
  source_instrument_id: string
  target_instrument_id: string
  transpose_interval: number
  public_error_message: string | null
  created_at: string
  updated_at: string
  finished_at: string | null
}
```

## JobStatusDTO

```ts
type JobStatusDTO = {
  job_id: string
  status: JobStatus
  progress: number
  message: string
  updated_at: string
}
```

## ArtifactDTO

```ts
type ArtifactDTO = {
  artifact_id: string
  job_id: string
  artifact_type: 'final_musicxml' | 'final_pdf'
  filename: string
  mime_type: string
  size_bytes: number
  expires_at: string
}
```

## Polling

Recomendação inicial:

```text
1s durante os primeiros 10s
2s até 60s
5s após 60s
parar em completed, failed, cancelled ou expired
```

## Estados de UI por status

```text
uploaded     -> arquivo recebido
queued       -> aguardando processamento
processing   -> preparando leitura
transposing  -> transpondo partitura
rendering    -> gerando artefato final
completed    -> pronto para download
failed       -> falha com mensagem pública
expired      -> resultado expirado
cancelled    -> processamento cancelado
```

## Testes de contrato

- Frontend valida DTOs.
- Erro público nunca contém stacktrace.
- Resposta pública nunca contém `storage_key`.
- Resposta pública nunca contém path físico.
- UploadDTO aceita PDF e MusicXML.
- ArtifactDTO não contém path interno.
