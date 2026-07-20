# Processamento de job

## Objetivo

Expor um processamento assíncrono previsível, cancelável e observável sem confundir estado, etapa e retenção.

## Criação

```text
POST /api/v1/transpositions
Idempotency-Key + sessão + CSRF
-> 202 + Location + job_id
```

A API não aguarda transposição.

## Campos públicos

```text
status
stage
progress_pct
retention_status
warnings
error
updated_at
expires_at
```

Enums canônicos: `../backend/16-maquina-estados.md`.

## Polling

- respeitar `Retry-After`;
- usar backoff com jitter;
- pausar/reduzir em aba oculta;
- parar em `completed`, `completed_with_warnings`, `failed` ou `cancelled`;
- `expired` pertence à retenção e pode ocorrer depois da conclusão;
- erros de rede transitórios não mudam o job local para `failed`.

## Cancelamento

A UI pode oferecer cancelar enquanto `queued`, `running` ou `cancel_requested`. A ação chama `DELETE /api/v1/jobs/{job_id}` com CSRF. O estado final pode demorar; não fingir cancelamento instantâneo.

## Mensagens

Mensagens vêm de mapeamento estável de stage/erro. Não mostrar stacktrace, engine, porcentagem de confiança ou log bruto. Warnings categóricos são exibidos com ação clara.

## Critérios de aceite

- criação idempotente não duplica job;
- polling não continua após estado terminal;
- progresso não retrocede;
- cancelamento não disponibiliza artefato parcial;
- refresh da página recupera o job enquanto a mesma sessão existir;
- recurso de outra sessão retorna estado de não encontrado.
