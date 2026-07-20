# Taxonomia de erros públicos

> Status: canônico. Revisão: 2026-07-20.

## Envelope

```json
{
  "error": {
    "code": "UNSUPPORTED_SCORE_STRUCTURE",
    "message": "Esta partitura usa uma estrutura ainda não suportada.",
    "correlation_id": "req_01J...",
    "retryable": false,
    "field_errors": []
  }
}
```

`code` é estável para clientes; `message` é localizada e pode evoluir. Exceção interna nunca vira código público automaticamente.

## Sessão e autorização

| Código | HTTP | Retry | Uso |
|---|---:|---|---|
| `SESSION_REQUIRED` | 401 | não | sessão ausente, inválida ou expirada |
| `CSRF_INVALID` | 403 | não | mutação sem CSRF válido |
| `RESOURCE_NOT_FOUND` | 404 | não | recurso inexistente ou de outra sessão |
| `RATE_LIMITED` | 429 | sim | quota temporária; usar `Retry-After` |

## Upload e formato

| Código | HTTP | Retry | Uso |
|---|---:|---|---|
| `EMPTY_FILE` | 400 | não | zero bytes |
| `FILE_TOO_LARGE` | 413 | não | limite excedido |
| `INVALID_FILE_TYPE` | 415 | não | tipo não permitido |
| `FILE_SIGNATURE_MISMATCH` | 422 | não | extensão/MIME/assinatura incoerentes |
| `FORMAT_NOT_ENABLED` | 422 | não | capability desabilitada |
| `UNSAFE_DOCUMENT` | 422 | não | estrutura hostil ou proibida |
| `UPLOAD_NOT_AVAILABLE` | 409 | não | upload ainda não está validado ou está em estado incompatível |
| `UPLOAD_EXPIRED` | 410 | não | upload expirou ou já foi purgado |
| `UPLOAD_IN_USE` | 409 | não | upload já possui job; excluir pelo recurso do job |
| `FILE_INTEGRITY_FAILED` | 422 | não | hash/tamanho divergente |

## Domínio musical

| Código | HTTP | Retry | Uso |
|---|---:|---|---|
| `MUSICXML_PARSE_FAILED` | 422 | não | XML inválido ou não MusicXML |
| `UNSUPPORTED_SCORE_STRUCTURE` | 422 | não | multiparte, multipauta ou recurso fora do perfil |
| `SOURCE_INSTRUMENT_MISMATCH` | 422 | não | `<transpose>` contradiz origem selecionada |
| `UNSUPPORTED_NOTATION` | 422 | não | microtom/percussão/elemento sem semântica segura |
| `TRANSPOSITION_FAILED` | 500 | não | falha inesperada do motor; requer correção ou nova versão |
| `INVALID_MUSICAL_DOCUMENT` | 422 | não | a entrada é estruturalmente válida, mas musicalmente inconsistente |
| `SEMANTIC_VALIDATION_FAILED` | 500 | não | resultado produzido pelo motor viola invariante e não pode ser publicado |
| `OMR_LOW_RELIABILITY` | 422 | não | PDF não alcança gate de qualidade |

## Operação e artefatos

| Código | HTTP | Retry | Uso |
|---|---:|---|---|
| `IDEMPOTENCY_CONFLICT` | 409 | não | mesma chave, payload diferente |
| `INVALID_JOB_STATE` | 409 | não | operação incompatível com estado |
| `JOB_NOT_COMPLETED` | 409 | sim | resultado ainda não disponível |
| `PROCESSING_LIMIT_EXCEEDED` | 422 | não | documento excede limite determinístico de complexidade/recursos |
| `PROCESSING_TIMEOUT` | 503 | sim | tentativa excedeu prazo por condição operacional transitória |
| `RENDERER_UNAVAILABLE` | 503 | sim | saída opcional indisponível |
| `RENDER_FAILED` | 500 | não | renderer falhou de forma não classificada |
| `ARTIFACT_STORAGE_FAILED` | 503 | sim | falha transitória de storage |
| `ARTIFACT_EXPIRED` | 410 | não | retenção encerrada |
| `STORAGE_UNAVAILABLE` | 503 | sim | não foi possível persistir/ler por indisponibilidade operacional |
| `SERVICE_UNAVAILABLE` | 503 | sim | dependência essencial indisponível |

## Regras

- Cada código possui um status HTTP canônico; causas com semânticas diferentes usam códigos diferentes.
- `retryable=true` só quando repetir a mesma operação é seguro e plausível.
- Erro de job persistido aparece no DTO do próprio job; erro HTTP usa o envelope.
- Campo inválido usa `field_errors` com paths allowlisted.
- Mensagens não citam engine, biblioteca, path, comando, schema interno ou stacktrace.
- Códigos novos exigem atualização deste arquivo, OpenAPI, frontend e testes de contrato.
