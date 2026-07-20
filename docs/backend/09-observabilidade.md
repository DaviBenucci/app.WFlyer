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
