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
