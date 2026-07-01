# Contratos de API

## Convenções

- Respostas JSON para endpoints de dados.
- Upload por `multipart/form-data`.
- Datas em ISO 8601 UTC.
- IDs em UUID, exceto instrumentos, que usam slug estável.
- Erros sempre usam envelope `{ "error": ... }`.
- DTO público nunca retorna `storage_key`, path físico, stacktrace, segredo, log bruto ou detalhe interno do worker.

## Erro padrão

```json
{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "O arquivo enviado não é uma partitura válida.",
    "correlation_id": "req_123"
  }
}
```

## GET /health

Objetivo: confirmar que a API está viva.

Entrada: nenhuma.

Resposta 200:

```json
{
  "status": "ok",
  "service": "wflyer-api"
}
```

Erros possíveis: indisponibilidade geral da API.

Segurança: não retornar dependências internas, segredos ou stacktrace.

## GET /api/instruments

Objetivo: listar instrumentos ativos para origem e destino.

Entrada: nenhuma no MVP.

Resposta 200:

```json
{
  "items": [
    {
      "id": "trumpet-bb",
      "name": "Trompete Bb",
      "family": "metais",
      "key_name": "Bb",
      "written_to_concert": -2,
      "transposes_octave": false,
      "is_active": true,
      "notes": "Quando lê C, soa Bb."
    }
  ]
}
```

Validações:

- retornar apenas instrumentos ativos;
- ordenar por família e nome;
- não depender de catálogo hardcoded no frontend.

Status codes:

- `200 OK`.
- `500 INTERNAL_ERROR` com envelope seguro.

## POST /api/uploads

Objetivo: receber arquivo de partitura e criar registro de upload.

Entrada:

```text
Content-Type: multipart/form-data
file=<arquivo>
```

Tipos inicialmente permitidos:

```text
application/pdf
application/vnd.recordare.musicxml+xml
application/xml
text/xml
```

Resposta 201:

```json
{
  "upload_id": "7b2c89b2-7a7a-4e3e-a91d-6d0d9893a101",
  "original_filename": "partitura.musicxml",
  "mime_type": "application/vnd.recordare.musicxml+xml",
  "size_bytes": 123456,
  "status": "uploaded",
  "expires_at": "2026-07-16T12:00:00Z"
}
```

Status codes:

- `201 CREATED`.
- `400 INVALID_FILE`.
- `413 FILE_TOO_LARGE`.
- `415 INVALID_FILE_TYPE`.
- `429 RATE_LIMITED`.
- `500 UPLOAD_STORAGE_FAILED`.

Validações:

- MIME real;
- extensão;
- tamanho;
- arquivo vazio;
- nome original apenas como metadado;
- renomeação interna obrigatória.

Segurança:

- não retornar path físico;
- não retornar `storage_key`;
- não confiar no `Content-Type` enviado pelo navegador.

## POST /api/transpositions

Objetivo: criar job assíncrono de transposição.

Entrada:

```json
{
  "upload_id": "7b2c89b2-7a7a-4e3e-a91d-6d0d9893a101",
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb"
}
```

Resposta 202:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "status": "queued",
  "progress": 0,
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb",
  "transpose_interval": 2,
  "expires_at": "2026-07-16T12:00:00Z"
}
```

Status codes:

- `202 ACCEPTED`.
- `404 UPLOAD_NOT_FOUND`.
- `410 UPLOAD_EXPIRED`.
- `404 INSTRUMENT_NOT_FOUND`.
- `422 TRANSPOSITION_INVALID`.
- `429 RATE_LIMITED`.
- `503 QUEUE_UNAVAILABLE`.

Validações:

- upload existe;
- upload não expirou;
- instrumentos estão ativos;
- intervalo foi calculado pela fórmula central.

Segurança:

- não iniciar processamento pesado no endpoint;
- não aceitar instrumento fora do catálogo;
- registrar `correlation_id`.

## GET /api/jobs/{job_id}

Objetivo: retornar visão pública do job.

Resposta 200:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "upload_id": "7b2c89b2-7a7a-4e3e-a91d-6d0d9893a101",
  "status": "transposing",
  "progress": 65,
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb",
  "transpose_interval": 2,
  "public_error_message": null,
  "created_at": "2026-07-01T12:00:00Z",
  "updated_at": "2026-07-01T12:01:00Z",
  "finished_at": null
}
```

Status codes:

- `200 OK`.
- `404 JOB_NOT_FOUND`.
- `410 JOB_EXPIRED`.

Segurança: não retornar erro interno, worker id, storage, stacktrace ou logs.

## GET /api/jobs/{job_id}/status

Objetivo: endpoint leve para polling do frontend.

Resposta 200:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "status": "rendering",
  "progress": 82,
  "message": "Gerando arquivo final.",
  "updated_at": "2026-07-01T12:02:00Z"
}
```

Status codes:

- `200 OK`.
- `404 JOB_NOT_FOUND`.
- `410 JOB_EXPIRED`.

Validações:

- `progress` entre 0 e 100;
- status pertence à lista oficial.

## GET /api/jobs/{job_id}/artifacts

Objetivo: listar artefatos gerados por job concluído.

Resposta 200:

```json
{
  "items": [
    {
      "artifact_id": "c9d3b87a-9c10-46ea-9db7-b76d99a4a01e",
      "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
      "artifact_type": "final_musicxml",
      "filename": "partitura-transposta.musicxml",
      "mime_type": "application/vnd.recordare.musicxml+xml",
      "size_bytes": 345678,
      "expires_at": "2026-07-16T12:00:00Z"
    }
  ]
}
```

Status codes:

- `200 OK`.
- `404 JOB_NOT_FOUND`.
- `409 JOB_NOT_COMPLETED`.
- `410 JOB_EXPIRED`.

Segurança: nunca retornar `storage_key`.

## GET /api/artifacts/{artifact_id}/download

Objetivo: permitir download controlado de artefato válido.

Resposta 200:

```text
Arquivo binário em stream controlado pela API
```

Alternativa documentável antes da implementação: resposta JSON com URL temporária controlada.

Status codes:

- `200 OK`.
- `404 ARTIFACT_NOT_FOUND`.
- `410 ARTIFACT_EXPIRED`.
- `403 DOWNLOAD_FORBIDDEN`.
- `500 DOWNLOAD_UNAVAILABLE`.

Validações:

- artefato existe;
- artefato não expirou;
- job associado permite download;
- arquivo físico/referência interna existe.

Segurança:

- bloquear artefato expirado;
- não revelar path físico;
- não revelar chave interna de storage;
- não retornar logs do worker.

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
