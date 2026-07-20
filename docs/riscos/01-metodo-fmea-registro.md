# Método FMEA e registro de riscos

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Avaliar como cada capacidade pode falhar, qual efeito terá sobre música, usuário, segurança e operação, e quais controles impedem publicação incorreta.

## Dimensões

```text
severity: low | medium | high | critical
detectability: easy | moderate | hard
likelihood: rare | possible | likely | frequent
handling: reject | review | retry | degrade | incident
retry_class: never | transient | after_user_action | after_configuration_change
```

Impacto musical silencioso, acesso indevido, perda de autoria, corrupção do canônico ou publicação de resultado não verificado são `critical` ou `high`, mesmo quando raros.

## Ciclo de vida

```text
identified
→ control_designed
→ test_planned
→ implemented
→ evidenced
→ residual_risk_accepted
→ monitored
→ retired
```

`residual_risk_accepted` exige owner e justificativa. Não é sinônimo de “sem risco”.

## FMEA por capability

O preflight deve responder:

1. qual é o dano máximo;
2. como a falha pode permanecer silenciosa;
3. qual componente detecta;
4. se o detector é independente do transformador;
5. qual resposta é segura;
6. se retry pode piorar ou duplicar efeito;
7. como reverter/pausar;
8. qual métrica alerta regressão;
9. quais estratos do corpus são afetados;
10. qual risco residual precisa de aprovação.

## Critério de bloqueio

Uma capability não entra em rollout quando houver `PM-*` aplicável sem:

- owner;
- teste ou inspeção manual definida;
- comportamento de falha;
- código/estado observável;
- plano de rollback;
- evidência no gate.
