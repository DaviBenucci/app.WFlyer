# Política de falhas desconhecidas

> Status: canônico. Revisão: 2026-07-20.

## Princípio

A matriz de pre-mortem reduz surpresa, mas não prova completude. Quando uma falha não classificada puder afetar música, autorização, autoria, privacidade ou integridade, o sistema deve parar a publicação e preservar evidência mínima segura.

## Resposta operacional

1. acionar kill switch da capability/cohort quando necessário;
2. impedir novos resultados potencialmente afetados;
3. identificar versões, instrumentos, operações e artefatos relacionados;
4. criar `INC-*`, `RISK-*` e `PM-*`;
5. produzir fixture mínima sem incluir conteúdo protegido desnecessário;
6. classificar comissão, omissão, atribuição ou apresentação;
7. corrigir causa e adicionar verificador independente quando possível;
8. executar corpus Core, regressão e release-hidden aplicáveis;
9. revisar necessidade de notificação ao usuário;
10. documentar risco residual e aprovar rollout.

## Regra de comunicação

Não afirmar “caso isolado” sem análise de abrangência. Não apagar evidência para melhorar métricas. Não reprocessar silenciosamente uma obra e substituir a revisão anterior.

## Gate de reabertura

A capability só retorna quando há:

- causa raiz ou contenção comprovada;
- teste que falha antes e passa depois;
- análise de abrangência;
- métrica/alerta para reincidência;
- aprovação técnica e musical conforme impacto;
- plano de rollback.
