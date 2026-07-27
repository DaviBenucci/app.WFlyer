# Filas, backpressure e workers

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Filas separadas

```text
core-musicxml
omr
render
audio
billing
fiscal
maintenance
```

Um OMR pesado não bloqueia transposição simples.

## Job

- idempotency key;
- lease;
- heartbeat;
- attempt count;
- timeout;
- cancellation flag;
- stage;
- error class;
- artifact publication state.

## Retry

Apenas falha transitória:

- timeout de rede;
- serviço temporariamente indisponível;
- throttling;
- perda de worker.

Não repetir indefinidamente:

- MusicXML inválido;
- regra musical não suportada;
- certificado expirado;
- dado fiscal inválido;
- autorização negada.

## Backpressure

- limite global;
- limite por usuário/organização;
- tamanho máximo de backlog;
- autoscaling por idade da mensagem e CPU;
- circuit breaker em dependência;
- DLQ;
- modo degradado.

## Publicação

Artefato temporário → verificação → hash → promoção atômica → banco `available`.
