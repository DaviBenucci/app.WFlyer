# Protocolo de preflight por capacidade

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Impedir que uma capability comece por tela, biblioteca ou algoritmo antes de ter contrato, risco, corpus, comportamento seguro e rollback.

## Documento obrigatório

Cada capacidade deve criar `preflight/<capability>-<version>.md` com:

```text
capability e owner
objetivo e não objetivos
matriz suportada
operações e níveis de garantia
schemas/API/tabelas/artefatos
invariantes e proveniência
PM-* e riscos aplicáveis
falhas desconhecidas e kill switch
corpus, licença e estratos
métricas e thresholds definidos antes do teste
estados de frontend e reference_id
segurança, privacidade, autoria e retenção
observabilidade, custo e quotas
feature flag, rollout e rollback
decisões pendentes
```

## Gate de entrada

Não iniciar código quando houver:

- decisão musical ou legal pendente que altere o contrato;
- corpus sem proveniência/licença;
- ausência de comportamento fail-closed;
- métrica escolhida depois de ver o resultado;
- UI sem estados de erro/revisão;
- modelo/solver sem validador independente;
- capability sem kill switch;
- referência visual externa sem transformação em padrão interno.

## Gate de saída

O preflight recebe `APPROVED_FOR_IMPLEMENTATION` somente com aprovação de produto, engenharia e especialistas aplicáveis. Aprovação do preflight não ativa produção; apenas autoriza iniciar a implementação.

## Mudança de escopo

Alteração de formato, instrumento, operação, engine, modelo, policy ou guarantee reabre o preflight e pode invalidar evidência anterior.
