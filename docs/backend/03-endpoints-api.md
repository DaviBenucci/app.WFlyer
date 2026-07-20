# Contratos de API

> Status: canônico. Revisão: 2026-07-20.

## Convenções

- Base: `/api/v1`.
- JSON para dados; `multipart/form-data` somente no upload.
- IDs em UUID; instrumentos usam slug.
- Datas ISO 8601 UTC.
- Respostas sensíveis usam `Cache-Control: no-store`.
- Toda resposta inclui `X-Correlation-ID`.
- Métodos mutáveis após a criação da sessão exigem cookie de sessão e `X-CSRF-Token`.
- Rotas protegidas sem sessão válida retornam `401`; objeto inexistente ou de outra sessão retorna `404` para evitar enumeração.
- DTO público nunca contém `storage_key`, path, stacktrace, task id, hash de token ou log bruto.

## Erro padrão

```json
{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "O formato deste arquivo não é aceito.",
    "correlation_id": "req_01J...",
    "retryable": false,
    "field_errors": []
  }
}
```

A taxonomia está em `18-taxonomia-erros.md`.

## GET /health

Liveness simples.

```json
{ "status": "ok", "service": "wflyer-api" }
```

Não expõe dependências.

## GET /health/ready

Readiness para operação interna. Pode verificar banco/Redis/storage, mas a resposta pública não inclui credenciais, hosts ou stacktraces.

## POST /api/v1/sessions/anonymous

Cria ou renova uma sessão vazia.

Resposta `201` para criação ou `200` para renovação, com o mesmo corpo:

```json
{
  "session": {
    "expires_at": "2026-08-04T12:00:00Z"
  },
  "csrf_token": "opaque-csrf-token"
}
```

Headers:

```text
Set-Cookie: wf_session=<opaque>; HttpOnly; Secure; SameSite=Lax; Path=/; Max-Age=...
Cache-Control: no-store
```

O token da sessão não aparece no JSON.

## GET /api/v1/capabilities

Resposta `200`:

```json
{
  "input_formats": {
    "musicxml": true,
    "generic_xml_musicxml": true,
    "mxl": false,
    "pdf_omr": false
  },
  "output_formats": {
    "musicxml": true,
    "pdf": false
  },
  "profile": {
    "max_parts": 1,
    "max_staves_per_part": 1,
    "microtones": false,
    "unpitched_percussion": false
  },
  "limits": {
    "max_upload_bytes": 10000000,
    "max_musicxml_measures": 2000,
    "max_musicxml_events": 100000
  }
}
```

Valores são configuração do ambiente, não hardcode de UI. Os números do exemplo são ilustrativos; os limites aprovados permanecem configuráveis até benchmark.

## GET /api/v1/instruments

Resposta `200`:

```json
{
  "items": [
    {
      "id": "trumpet-bb",
      "name": "Trompete Bb",
      "family": "metais",
      "key_name": "Bb",
      "written_to_concert": {
        "diatonic_steps": -1,
        "chromatic_semitones": -2,
        "octave_change": 0,
        "total_semitones": -2
      },
      "default_clef": "treble",
      "aliases": ["trompete em si bemol"],
      "is_active": true
    }
  ]
}
```

A API retorna apenas instrumentos ativos e afinados suportados.

## POST /api/v1/uploads

Headers:

```text
Content-Type: multipart/form-data
X-CSRF-Token: <token>
```

Body:

```text
file=<arquivo>
```

Resposta `201`:

```json
{
  "upload_id": "7b2c89b2-7a7a-4e3e-a91d-6d0d9893a101",
  "original_filename": "melodia.musicxml",
  "input_format": "musicxml",
  "mime_type": "application/vnd.recordare.musicxml+xml",
  "size_bytes": 123456,
  "sha256": "hex-opcional-na-resposta-conforme-politica",
  "status": "validated",
  "expires_at": "2026-08-04T12:00:00Z",
  "warnings": []
}
```

O hash pode ser omitido do DTO público; se exposto, não substitui autorização.

Erros principais:

- `400 EMPTY_FILE`;
- `413 FILE_TOO_LARGE`;
- `415 INVALID_FILE_TYPE`;
- `422 FORMAT_NOT_ENABLED`;
- `422 FILE_SIGNATURE_MISMATCH`;
- `429 RATE_LIMITED`;
- `503 STORAGE_UNAVAILABLE`.

## DELETE /api/v1/uploads/{upload_id}

Exclui upload sem job associado ou marca para cleanup. Exige sessão/CSRF. Retorna `204` quando concluído ou `202` quando assíncrono. Upload associado a job retorna `409 UPLOAD_IN_USE`; o cliente deve apagar o job.

## POST /api/v1/transpositions

Headers:

```text
Idempotency-Key: <uuid-ou-string-aleatoria>
X-CSRF-Token: <token>
```

Body:

```json
{
  "upload_id": "7b2c89b2-7a7a-4e3e-a91d-6d0d9893a101",
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb",
  "output_formats": ["musicxml"],
  "notation_policy": "preserve_source_clef"
}
```

O cliente não envia intervalo calculado.

Resposta `202`:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "status": "queued",
  "stage": "queued",
  "progress_pct": 0,
  "retention_status": "active",
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb",
  "output_interval": {
    "diatonic_steps": 1,
    "chromatic_semitones": 2,
    "octave_change": 0,
    "total_semitones": 2,
    "name": "M2"
  },
  "expires_at": null
}
```

Headers:

```text
Location: /api/v1/jobs/{job_id}
Retry-After: 1
```

A mesma `Idempotency-Key` com o mesmo payload retorna o mesmo job. Mesma chave com payload diferente retorna `409 IDEMPOTENCY_CONFLICT`. `expires_at` permanece `null` até o job concluir; então é definido a partir de `finished_at`.

A resposta de criação é um resumo (`CreateTranspositionResponse`), não o DTO completo de consulta. O cliente deve seguir `Location` ou consultar o status para obter timestamps, warnings e erro público.

## GET /api/v1/jobs/{job_id}

Resposta `200`:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "status": "running",
  "stage": "transposing",
  "progress_pct": 62,
  "retention_status": "active",
  "source_instrument_id": "piano",
  "target_instrument_id": "trumpet-bb",
  "output_interval": {
    "diatonic_steps": 1,
    "chromatic_semitones": 2,
    "octave_change": 0,
    "total_semitones": 2,
    "name": "M2"
  },
  "warnings": [],
  "error": null,
  "created_at": "2026-07-20T12:00:00Z",
  "updated_at": "2026-07-20T12:01:00Z",
  "finished_at": null,
  "expires_at": null
}
```

## GET /api/v1/jobs/{job_id}/status

Endpoint leve para polling:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "status": "running",
  "stage": "validating",
  "progress_pct": 78,
  "retention_status": "active",
  "message": "Validando o resultado musical.",
  "warnings": [],
  "error": null,
  "finished_at": null,
  "expires_at": null,
  "updated_at": "2026-07-20T12:02:00Z"
}
```

Pode retornar `Retry-After`. Em sucesso terminal, `finished_at` e `expires_at` são preenchidos. Polling para em `completed`, `completed_with_warnings`, `failed` ou `cancelled`.

## GET /api/v1/jobs/{job_id}/artifacts

Só lista artefatos públicos e disponíveis:

```json
{
  "items": [
    {
      "artifact_id": "c9d3b87a-9c10-46ea-9db7-b76d99a4a01e",
      "artifact_type": "transposed_musicxml",
      "filename": "melodia-transposta.musicxml",
      "mime_type": "application/vnd.recordare.musicxml+xml",
      "size_bytes": 345678,
      "sha256": "...",
      "expires_at": "2026-08-04T12:00:00Z"
    }
  ]
}
```

Job não concluído retorna `409 JOB_NOT_COMPLETED`. Retenção expirada retorna `410 ARTIFACT_EXPIRED`.

## GET /api/v1/artifacts/{artifact_id}/download

Valida sessão, propriedade, estado do job e retenção. Retorna stream com:

```text
Content-Type: tipo validado
Content-Disposition: attachment; filename="nome-sanitizado.musicxml"
Cache-Control: private, no-store
X-Content-Type-Options: nosniff
```

URLs permanentes públicas são proibidas. URL assinada curta só pode ser usada após autorização e decisão documentada.

## DELETE /api/v1/jobs/{job_id}

- job ativo: retorna `202`, status passa a `cancel_requested`;
- job terminal: retorna `202` ou `204` e inicia/efetiva purge;
- operação idempotente;
- após purge, o objeto deixa de disponibilizar artefatos.

## Códigos de status e autorização

- `401` somente para sessão ausente/inválida quando a rota exige sessão;
- `403` para CSRF inválido ou operação proibida na própria sessão;
- `404` para objeto inexistente ou não pertencente à sessão;
- `409` para conflito de estado/idempotência;
- `410` para conteúdo expirado;
- `422` para regra de domínio/formato;
- `429` para quota/rate limit.
