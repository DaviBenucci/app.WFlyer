# Runbook — worker parado ou fila acumulada

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. identificar fila e idade da mensagem;
2. verificar workers, CPU, memória e crash;
3. separar erro transitório de payload determinístico;
4. impedir autoscaling descontrolado contra banco;
5. pausar entrada se backlog exceder limite;
6. escalar fila afetada;
7. mover poison messages para DLQ;
8. reconciliar jobs órfãos;
9. confirmar idempotência antes de replay;
10. registrar fixture do incidente.
