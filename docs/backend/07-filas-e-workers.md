# Filas e workers

> Status: canônico. Revisão: 2026-07-20.

## Tecnologia inicial

- Celery para execução de tarefas;
- Redis como broker inicial;
- PostgreSQL como fonte de verdade para estado;
- outbox transacional para publicar jobs sem janela de perda entre banco e broker.

Redis e Celery não são a fonte de verdade do status público.

## Semântica de entrega

A entrega deve ser tratada como **pelo menos uma vez**. Portanto, toda tarefa precisa ser idempotente e tolerar reentrega.

Payload da fila:

```json
{
  "job_id": "4986c7e5-47c6-4a4c-9988-d8b0a558fc72",
  "correlation_id": "req_01J..."
}
```

Não incluir conteúdo, path, `storage_key`, cookie, CSRF, token de download ou dados musicais no payload.

## Aquisição do job

Antes de processar, o worker:

1. lê o job no banco;
2. verifica estado e retenção;
3. tenta adquirir lease/lock transacional;
4. cria `processing_attempts` com número incremental;
5. confirma que nenhum artefato público válido já satisfaz o job;
6. inicia o primeiro stage.

Job terminal não é reprocessado por simples reentrega. Reprocessamento explícito cria novo job ou operação administrativa futura.

## Retentativas

| Classe | Retry | Exemplo |
|---|---|---|
| determinística | não | XML malformado, estrutura não suportada, origem incompatível |
| transitória | limitada, com backoff e jitter | storage temporariamente indisponível, broker instável |
| recurso/timeout | conforme política; normalmente não cega | limite de memória, arquivo excessivo, OMR travado |
| bug desconhecido | no máximo política conservadora | exceção não classificada |

Cada tentativa registra classe, fingerprint e duração. O número máximo e backoff são configuração versionada, não números espalhados no código.

## Limites e isolamento

- time limit global e por stage;
- limite de memória, CPU, PIDs e arquivos para subprocessos;
- diretório temporário por tentativa;
- sem rede para processadores de documento;
- processo não privilegiado;
- limpeza em `finally` e job de recuperação para resíduos.

## Heartbeat e jobs presos

Workers atualizam lease/heartbeat. Um reconciliador identifica:

- `running` sem heartbeat válido;
- tentativa encerrada sem estado terminal;
- outbox não publicada;
- artefato provisório órfão.

A recuperação é idempotente e registra evento. Não assumir que ausência de heartbeat significa automaticamente que é seguro executar duas instâncias em paralelo.

## Cancelamento

- `cancel_requested` é persistido no banco;
- worker verifica o sinal entre stages;
- tarefa em subprocesso recebe término controlado;
- publicação final verifica novamente o cancelamento;
- resultado terminal é `cancelled`, sem artefato público parcial.

## Filas sugeridas

```text
wflyer.core       normalização/transposição/validação
wflyer.render     renderização opcional
wflyer.omr        PDF/OMR, somente quando habilitado
wflyer.maintenance purge, reconciliação e outbox
```

O MVP pode iniciar com menos workers físicos, desde que as rotas lógicas, limites e prioridades estejam preservados.

## Testes obrigatórios

- reentrega do mesmo task não duplica artefato;
- crash depois do storage e antes do commit é reconciliado;
- erro determinístico não entra em loop;
- falha transitória respeita máximo/backoff;
- lease expirado é detectado;
- cancelamento durante stage não publica resultado;
- payload da fila não contém dados sensíveis;
- falha do worker não derruba a API.
