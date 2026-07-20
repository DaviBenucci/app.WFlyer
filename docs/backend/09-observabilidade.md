# Observabilidade e auditoria operacional

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Diagnosticar disponibilidade, fila, integridade musical e abuso sem coletar o conteúdo das partituras nem expor segredos.

## Logs estruturados

Campos allowlisted:

```json
{
  "timestamp": "2026-07-20T12:00:00Z",
  "level": "info",
  "service": "wflyer-worker",
  "environment": "production",
  "correlation_id": "req_01J...",
  "job_id": "uuid",
  "attempt_number": 1,
  "event": "stage_completed",
  "stage": "validating",
  "duration_ms": 418
}
```

Não registrar cookie, CSRF, URL assinada, `storage_key`, conteúdo XML/PDF, stderr completo, nome original desnecessário ou payload integral.

## Correlação

- API gera/valida `X-Correlation-ID`;
- ID é propagado para outbox, broker, worker e eventos;
- erros públicos devolvem o mesmo ID;
- IDs fornecidos pelo cliente não são confiados sem validação de formato/tamanho.

## Métricas

### Serviço

```text
request rate/latency/error por rota
sessions criadas/rejeitadas
bytes de upload e rejeições
fila: profundidade, idade do item mais antigo, tempo de espera
jobs por status/stage e duração
retries, timeouts, cancelamentos e jobs presos
storage: erro, bytes, objetos órfãos, atraso de purge
```

### Qualidade musical

```text
falhas por invariante
warnings por categoria
formatos e versões de entrada
engine manifest por job
sucesso por fixture/corpus em CI
OMR: métricas agregadas somente quando a feature existir
```

Não usar dados agregados para afirmar precisão sem corpus/versionamento.

## Tracing

Spans recomendados:

```text
session.create
upload.stream
upload.validate
transposition.create
outbox.publish
job.claim
stage.normalize
stage.transpose
stage.validate
stage.render
artifact.publish
artifact.download
purge.execute
```

Amostragem nunca inclui o corpo do documento.

## Alertas mínimos

- readiness falhando;
- fila/idade acima do limite operacional;
- taxa de falha ou timeout anormal;
- worker sem heartbeat;
- storage/banco/Redis indisponível;
- purge atrasado ou objetos órfãos;
- aumento de `SEMANTIC_VALIDATION_FAILED` após release;
- aumento de `UNSAFE_DOCUMENT`/rate limit.

Limiares e SLOs exatos são decisão operacional pendente e devem ser definidos antes de produção.

## Auditoria

Eventos de segurança e ciclo de vida devem permitir responder:

- qual sessão criou/excluiu um recurso;
- quando ocorreu upload, job, download, expiração e purge;
- qual versão de engine produziu o artefato;
- qual erro/warning categórico ocorreu.

Auditoria não é um espelho de logs brutos e respeita retenção/minimização.

## Métricas musicais avançadas

Internas e sem labels de alta cardinalidade:

```text
wflyer_assurance_failure_total{check,operation}
wflyer_review_required_total{kind}
wflyer_review_resolution_seconds{kind}
wflyer_melody_ambiguity_total{band}
wflyer_harmony_variant_rejected_total{constraint}
wflyer_target_capability_violation_total{type}
wflyer_watermark_failure_total{stage}
wflyer_signature_failure_total{key_id}
```

Não colocar título, nome do arquivo, pitch sequence, token completo ou hash inteiro em labels. Dashboards separam falha operacional de falha musical determinística.

## Métricas da visão crítica

### Integridade e revisão

```text
verified_false_positive_rate{capability,instrument,texture}
review_required_rate{reason}
rejection_rate{failure_mode_id}
unknown_failure_rate{stage}
provenance_coverage_ratio
musical_diff_unmapped_event_count
stale_revision_conflict_rate
```

### Musicalidade aplicada

```text
melody_event_precision/recall/f1{texture}
melody_boundary_f1
playability_false_negative_rate{instrument}
harmonization_hard_constraint_rejection_rate
variant_semantic_distance
score_part_inconsistency_count
playback_mapping_error_rate
```

### Operação

```text
outbox_oldest_pending_seconds
job_lease_recovery_count
artifact_checksum_failure_count
cancel_publish_race_count
dlq_depth
worker_version_mismatch_count
capability_rollback_count
```

Métricas agregadas sempre devem ser quebradas por formato, instrumento, textura, complexidade, versão de engine e capability. Uma média boa não autoriza rollout de um estrato reprovado.

## Alertas críticos

Alertar imediatamente quando houver:

- resultado revogado após publicação;
- checksum/provenance inconsistente;
- IDOR/autorização;
- `verified_false_positive` confirmado;
- score/parte divergente;
- unknown failure em estágio de publicação;
- conteúdo musical/PII detectado em log;
- capability ligada sem gate aprovado.
