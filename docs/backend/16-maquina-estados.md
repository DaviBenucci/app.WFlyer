# Máquinas de estado

> Status: canônico. Revisão: 2026-07-20.

Estados de upload, processamento e retenção são ortogonais. É proibido usar um único enum para representar os três ciclos.

## UploadStatus

```text
quarantined -> validated
quarantined -> rejected
validated   -> expired
rejected    -> purged
expired     -> purged
validated   -> purged   (deleção antecipada, sem job ativo)
```

| Estado | Significado |
|---|---|
| `quarantined` | bytes recebidos, ainda não aprovados para job |
| `validated` | tipo, integridade e perfil inicial aprovados |
| `rejected` | arquivo recusado; erro público categorizado |
| `expired` | janela encerrada; acesso bloqueado |
| `purged` | bytes removidos; metadados mínimos podem permanecer |

Upload rejeitado nunca cria job.

## JobStatus

```text
queued -> running
queued -> cancel_requested
running -> cancel_requested
running -> completed
running -> completed_with_warnings
running -> failed
cancel_requested -> cancelled
cancel_requested -> failed   (falha ao encerrar/limpar)
```

Estados terminais:

```text
completed
completed_with_warnings
failed
cancelled
```

Não existe `uploaded`, `processing`, `transposing`, `rendering` ou `expired` em `JobStatus`; esses conceitos pertencem a upload, stage ou retenção.

## ProcessingStage

```text
queued
preprocessing
recognizing
normalizing
transposing
validating
rendering
finalizing
```

- `recognizing` só aparece para PDF/OMR habilitado.
- `rendering` só aparece quando saída renderizada foi solicitada e habilitada.
- stage descreve a atividade atual, não o resultado do job.
- ao terminar, o último stage pode permanecer registrado, mas `status` é terminal.

## RetentionStatus

```text
active -> expired -> purging -> purged
active -> purging -> purged     (deleção antecipada)
purging -> expired              (rollback controlado se purge falhar antes de remover bytes)
```

Download só é permitido em `active` e para job com sucesso terminal.

## Progresso

- `0..100`, calculado pelo servidor;
- monotônico em uma tentativa;
- pode ficar estável por longos períodos;
- `100` apenas para sucesso terminal;
- falha/cancelamento conserva o último valor e a UI não interpreta como porcentagem concluída;
- pesos por stage são configuração versionada.

## Concorrência

Toda transição usa compare-and-set/lock e valida estado atual. Transição inválida não é ignorada silenciosamente: gera conflito interno, métrica e reconciliação quando necessário.

## Tabela pública de UI

| Status | Stage | Mensagem sugerida |
|---|---|---|
| `queued` | `queued` | Aguardando processamento. |
| `running` | `normalizing` | Preparando a estrutura musical. |
| `running` | `transposing` | Transpondo a partitura. |
| `running` | `validating` | Conferindo o resultado musical. |
| `running` | `rendering` | Gerando o formato solicitado. |
| `completed` | qualquer | Resultado pronto. |
| `completed_with_warnings` | qualquer | Resultado pronto; revise os avisos. |
| `failed` | qualquer | Não foi possível concluir. |
| `cancel_requested` | qualquer | Cancelamento solicitado. |
| `cancelled` | qualquer | Processamento cancelado. |

## Estado de espera por decisão humana

Capacidades avançadas adicionam um estado não terminal:

```text
running -> awaiting_user_input
awaiting_user_input -> queued           (review submetida)
awaiting_user_input -> cancel_requested
awaiting_user_input -> failed           (review expirada/inválida conforme política)
```

`review_kind` é ortogonal:

```text
source_recognition
melody_selection
harmony_variant
```

O worker encerra a tentativa ao entrar em espera. Uma nova tentativa começa após review, com `review_revision` no fingerprint.

## ProcessingStage avançado

```text
analyzing_structure
extracting_melody
reducing
harmonizing
arranging
assuring
watermarking
signing
```

`reviewing` não é stage de worker; é `status = awaiting_user_input`.

## Tabela pública adicional

| Status | Stage/review | Mensagem sugerida |
|---|---|---|
| `awaiting_user_input` | `source_recognition` | Revise trechos que não puderam ser confirmados. |
| `awaiting_user_input` | `melody_selection` | Confirme qual linha deve ser mantida como melodia. |
| `awaiting_user_input` | `harmony_variant` | Compare e escolha uma proposta de harmonização. |
| `running` | `assuring` | Conferindo a transformação musical. |
| `running` | `watermarking` | Preparando a versão identificada. |

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Estados de revisão e capacidades avançadas

### `ReviewStatus`

```text
NOT_REQUIRED
PENDING
IN_PROGRESS
CONFLICTED
APPROVED
REJECTED
SUPERSEDED
```

### `RevisionStatus`

```text
DRAFT
VALIDATING
VALID
INVALID
APPROVED
PUBLISHED
SUPERSEDED
PURGED
```

### `ArtifactValidationStatus`

```text
PENDING
SEMANTIC_VALID
LAYOUT_VALID
AUDIO_SYNC_VALID
INVALID
```

### Stages adicionais

```text
BUILDING_EVENT_GRAPH
ANALYZING_FORM
ANALYZING_MELODY
AWAITING_MELODY_REVIEW
CHECKING_PLAYABILITY
GENERATING_VARIANTS
AWAITING_VARIANT_APPROVAL
GENERATING_SCORE_PARTS
VALIDATING_SCORE_PARTS
GENERATING_PLAYBACK_MAP
RENDERING_AUDIO
VALIDATING_AUDIO_SYNC
VALIDATING_ENGRAVING
```

`COMPLETED` exige somente os artefatos solicitados e aplicáveis. Um job de harmonização não pode concluir antes da escolha da variante quando o contrato exigir aprovação.

## Estados de revisão, revisão musical e pacote

### ReviewTaskStatus

```text
OPEN
IN_PROGRESS
SUBMITTED
CONFLICTED
APPROVED
REJECTED
SUPERSEDED
CANCELLED
```

Uma decisão `APPROVED` referencia uma revisão exata. Nova revisão torna a aprovação anterior histórica; não a transfere automaticamente.

### RevisionStatus

```text
DRAFT
AWAITING_REVIEW
APPROVED
REJECTED
SUPERSEDED
REVOKED
```

`REVOKED` preserva hashes e cadeia, mas bloqueia novos downloads.

### EnsemblePackageStatus

```text
DRAFT
BUILDING
VERIFYING
AWAITING_REVIEW
COMPLETED
FAILED
CANCELLED
REVOKED
```

Pacote não permite estado “parcialmente completo”. Artefatos opcionais podem falhar isoladamente, mas score/partes obrigatórios constituem transação lógica única.

### PlaybackManifestStatus

```text
BUILDING
VALIDATING
READY
PARTIAL
FAILED
SUPERSEDED
```

`PARTIAL` desabilita score following nas regiões não mapeadas e deve ser explícito na UI.
