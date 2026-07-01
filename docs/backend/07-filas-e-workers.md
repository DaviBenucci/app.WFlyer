# Fila e workers

## Objetivo

Processar transposições fora da API, com status, retentativas, falhas seguras, timeout e idempotência básica.

## Fila inicial

```text
transposition_default
```

## Worker inicial

```text
worker-transposition
```

O worker inicial pode executar o pipeline completo do MVP. Separar leitura, transposição e renderização em workers diferentes é evolução futura.

## Payload da fila

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "correlation_id": "req_123"
}
```

Não incluir path físico, segredo, token de download ou conteúdo do arquivo no payload.

## Retentativas

- Não repetir erro determinístico, como MIME inválido ou MusicXML malformado.
- Repetir de forma limitada falha transitória de storage, fila ou renderização.
- Usar backoff.
- Registrar cada tentativa em `job_events`.

## Timeouts

Cada etapa deve ter timeout documentado antes da implementação:

```text
upload_validation
musicxml_parse
pdf_read
transposition
rendering
artifact_storage
```

Ao estourar timeout:

- marcar job como `failed`;
- usar erro público `PROCESSING_TIMEOUT`;
- registrar `correlation_id`.

## Falhas

Falha do worker não pode derrubar a API.

Fluxo de falha:

```text
capturar erro
registrar log interno com correlation_id
registrar job_event seguro
atualizar processing_jobs.status = failed
preencher error_code
preencher mensagem pública segura
```

## Idempotência básica

- Worker deve verificar status atual antes de processar.
- Job `completed`, `failed`, `expired` ou `cancelled` não deve ser processado novamente sem decisão explícita.
- Reentrega da fila não deve gerar artefatos duplicados sem controle.

## Cancelamento futuro

Cancelamento pode existir como status, mas execução cooperativa de cancelamento é evolução futura. O MVP deve ao menos não quebrar ao encontrar job `cancelled`.

## Observabilidade interna

- Logs com `job_id` e `correlation_id`.
- Duração por etapa.
- Erro categorizado por `error_code`.
- Eventos públicos sem detalhes internos.

## Critérios de aceite

- API coloca job na fila.
- Worker consome job.
- Worker altera status.
- Falha vira `failed`.
- Retentativa é limitada.
- Timeout é documentado.
- Payload não contém segredo nem path físico.
