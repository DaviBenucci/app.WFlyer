# Stack recomendada

## Princípio

A stack deve servir ao MVP técnico: backend assíncrono, frontend de ferramenta, banco relacional, fila de jobs, validação forte de payloads e motor musical testável.

Esta documentação não escolhe fornecedor de publicação online nem trata de domínio, DNS ou servidor de produção.

## Frontend

```text
Next.js
React
TypeScript
Tailwind CSS
shadcn/ui ou componentes próprios equivalentes
Lucide React
React Hook Form
Zod
TanStack Query
Testing Library
Playwright
```

Justificativa:

- TypeScript reduz divergência entre componentes e API.
- Zod valida contratos recebidos.
- TanStack Query organiza upload, criação de job, polling e artefatos.
- Playwright cobre fluxo do usuário e uso mobile/teclado.

## Backend

```text
FastAPI
Python 3.12+
Pydantic v2
SQLAlchemy 2.0
Alembic
PostgreSQL
Redis ou broker equivalente para fila
Celery, RQ ou Dramatiq
pytest
ruff
mypy
```

Recomendação inicial: Celery com Redis ou RQ com Redis. A escolha final deve ser registrada antes da fase de fila/worker.

## Processamento musical

```text
MusicXML como formato prioritário da Fase 1
music21 ou biblioteca equivalente para manipulação musical
MuseScore CLI ou alternativa documentada para renderização futura
OMR somente após validação do motor MusicXML-first
```

## Storage controlado pela aplicação

O MVP deve abstrair armazenamento por interface interna. A implementação inicial pode usar storage local controlado ou adaptador equivalente, desde que:

- não use filename original como path;
- não exponha caminho físico ao frontend;
- permita expiração;
- permita testes de download e bloqueio de artefato expirado.

## Segurança

```text
Rate limit
Validação real de MIME
Validação de extensão
Limite de tamanho
Renomeação interna
Erros sem stacktrace
Logs com correlation_id
Timeout por etapa
Subprocess sem shell=True
DTO público sem storage_key
```
