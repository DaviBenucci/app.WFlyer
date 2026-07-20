# Arquitetura API, fila e workers

> Status: canônico. Revisão: 2026-07-20.

## Topologia lógica

```text
Browser
  -> Web Next.js
  -> API FastAPI
       -> PostgreSQL
       -> Storage privado
       -> Redis broker
  -> Worker Celery
       -> Music engine
       -> OMR sandbox opcional
       -> Renderer sandbox opcional
       -> PostgreSQL / Storage
```

Web e API devem ser publicados sob o mesmo site lógico sempre que possível. Isso simplifica cookies de sessão, CORS e CSRF.

## Criação de sessão

```text
POST /api/v1/sessions/anonymous
-> gerar token aleatório
-> armazenar apenas hash
-> definir cookie HttpOnly/Secure/SameSite
-> retornar CSRF token e expiração
```

## Upload

```text
stream para quarentena
-> aplicar limite enquanto recebe
-> identificar formato por conteúdo + extensão
-> calcular SHA-256
-> validação superficial segura
-> mover atomically para storage privado
-> criar upload(validated)
```

Upload não executa OMR nem transposição.

## Criação do job

```text
POST /api/v1/transpositions
-> validar sessão e CSRF
-> validar Idempotency-Key
-> autorizar upload
-> validar capabilities e instrumentos
-> calcular intervalo completo no backend
-> criar processing_job(queued)
-> criar evento de outbox
-> publicar payload mínimo após commit
-> responder 202 + Location + Retry-After
```

A transação deve evitar job órfão. O padrão recomendado é outbox transacional ou publicação com reconciliação idempotente.

## Execução

```text
adquirir job com lease
-> criar processing_attempt
-> check cancel/retention
-> preprocessing
-> recognizing, apenas PDF
-> normalizing
-> transposing
-> validating
-> rendering, se solicitado e habilitado
-> finalizing
-> completed ou completed_with_warnings
```

## Consistência

- banco é a fonte do status;
- cada attempt possui identidade própria;
- artefatos usam chave determinística/única por job, tipo e versão;
- reentrega não duplica resultado;
- gravação de arquivo antecede publicação do artefato no banco;
- falha após gravar deve ser reconciliável.

## Falhas

Erros determinísticos não são repetidos. Erros transitórios usam backoff e limite. Falha de worker nunca derruba a API. O erro público é categorizado; detalhes ficam em log interno.

## Cancelamento e exclusão

`DELETE /api/v1/jobs/{id}` marca `cancel_requested` se o job estiver ativo. Workers verificam o pedido entre etapas. Depois do cancelamento ou para jobs terminais, o cleanup remove artefatos e marca retenção como `purged`.

## Pipeline avançado por operação

```text
API
-> job + operation + snapshots
-> outbox
-> orchestrator worker
-> canonical source
-> operation worker
   -> transpose
   -> melody extraction/reduction
   -> harmony generation
-> independent assurance worker
-> renderer/watermark/signing
-> atomic publication
```

Jobs que precisam de confirmação entram em `awaiting_user_input`; não mantêm subprocesso ou lease ativo. A resposta do usuário cria uma revisão versionada e reenfileira a continuação.

Filas de OMR, harmonização e renderização devem ter quotas/circuit breakers independentes para não bloquear transposição Core.
