# Runbook — banco degradado ou indisponível

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. verificar evento RDS/failover;
2. medir conexões, locks, CPU, IOPS e storage;
3. identificar query/deploy causador;
4. bloquear operações não essenciais;
5. preservar criação de efeitos financeiros incertos;
6. aguardar/promover failover gerenciado;
7. validar migrations e pool após retorno;
8. reconciliar outbox, jobs, webhooks e reservas;
9. testar leitura/escrita controlada;
10. executar restore somente por decisão formal.
