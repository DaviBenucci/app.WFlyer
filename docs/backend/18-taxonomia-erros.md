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

## Operações musicais avançadas

| Código | HTTP | Retry | Uso |
|---|---:|---|---|
| `OPERATION_NOT_ENABLED` | 422 | não | capacidade não habilitada. |
| `TARGET_TEXTURE_UNSUPPORTED` | 422 | não | destino não suporta a polifonia solicitada. |
| `MELODY_EXTRACTION_REQUIRED` | 422 | não | operação exige escolher linha melódica. |
| `MELODY_AMBIGUOUS` | 409 | não | múltiplas linhas plausíveis; review necessária. |
| `MELODY_SELECTION_INVALID` | 422 | não | seleção não referencia eventos válidos/coerentes. |
| `REVIEW_VERSION_CONFLICT` | 409 | não | revisão obsoleta. |
| `HARMONY_PROFILE_REQUIRED` | 422 | não | parâmetros mínimos ausentes. |
| `HARMONY_CONSTRAINT_VIOLATION` | 500 | não | variante não passou restrições rígidas. |
| `NO_VALID_HARMONY_VARIANT` | 422 | não | nenhuma proposta atende o perfil. |
| `TARGET_RANGE_UNSATISFIABLE` | 422 | não | não há adaptação permitida dentro da extensão. |
| `ASSURANCE_VALIDATION_FAILED` | 500 | não | verificador independente bloqueou publicação. |
| `WATERMARK_RENDER_FAILED` | 503 | sim | falha transitória no estágio de watermark. |
| `PROVENANCE_SIGNATURE_FAILED` | 503 | sim | manifesto não pôde ser assinado. |
| `VERIFICATION_TOKEN_INVALID` | 404 | não | resposta pública neutra. |

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Códigos críticos adicionais

### Grafo, revisão e diff

```text
EVENT_GRAPH_UNSUPPORTED
EVENT_ID_MAPPING_INCOMPLETE
MUSICAL_DIFF_INCOMPLETE
REVISION_CONFLICT
REVIEW_REQUIRED
REVIEW_ANCHOR_ORPHANED
```

### Melodia, análise e harmonia

```text
MELODY_AMBIGUITY_BLOCKING
TONAL_REGION_AMBIGUOUS
FORM_ANALYSIS_INCOMPLETE
LOCKED_MELODY_CHANGED
NO_VALID_HARMONY_VARIANT
MODEL_OUTPUT_REJECTED
```

### Instrumento e tocabilidade

```text
INSTRUMENT_PROFILE_NOT_APPROVED
PLAYABILITY_UNKNOWN
TARGET_PHYSICALLY_IMPOSSIBLE
TARGET_POLYPHONY_INCOMPATIBLE
ADAPTATION_REQUIRES_APPROVAL
```

### Score, layout e áudio

```text
SCORE_PART_MISMATCH
ENGRAVING_COLLISION_BLOCKING
MUSIC_FONT_MISMATCH
PLAYBACK_MAP_INVALID
AUDIO_NOTATION_MISMATCH
AUDIO_ASSET_LICENSE_MISSING
```

### Dados, direitos e rollout

```text
METADATA_POLICY_VIOLATION
ATTRIBUTION_LOSS_BLOCKING
CAPABILITY_NOT_APPROVED
ROLLOUT_KILLED
```

Cada código precisa de `user_action`, retryability, HTTP status, log severity, métrica, estado de UI e fixture. Mensagem pública não pode expor score, prompt, path ou stacktrace.

## Novos grupos públicos reservados

Os códigos abaixo são reservados; não devem ser retornados enquanto a capability estiver desabilitada:

```text
CAPABILITY_DISABLED
CAPABILITY_CHANGED
REVISION_CONFLICT
REVIEW_REQUIRED
MELODY_SELECTION_REQUIRED
ANALYSIS_AMBIGUOUS
NO_VALID_HARMONY_VARIANT
PLAYABILITY_BLOCKED
ADAPTATION_BUDGET_EXCEEDED
PLAYBACK_MAPPING_UNAVAILABLE
SCORE_PART_INCONSISTENT
ENSEMBLE_PACKAGE_INCOMPLETE
ARTIFACT_REVOKED
ENGINE_VERSION_INCOMPATIBLE
IDEMPOTENCY_CONFLICT
```

Regras:

- código público descreve ação do usuário, não detalhes internos;
- `PM-*` e stack traces não são expostos;
- ambiguidade é `REVIEW_REQUIRED`, não `PROCESSING_FAILED`;
- indisponibilidade transitória declara `retryable=true` e `retry_after` quando aplicável;
- conflito de revisão nunca sobrescreve decisão do outro revisor;
- `UNKNOWN_INTERNAL_ERROR` sempre permanece não publicável e gera `correlation_id`.
