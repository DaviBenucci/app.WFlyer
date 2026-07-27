# Runbook — pagamento ou webhook

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. não liberar plano manualmente sem evidência;
2. verificar status do provedor;
3. validar assinatura e logs do evento;
4. consultar objeto externo;
5. conferir evento duplicado/fora de ordem;
6. reprocessar por ferramenta idempotente;
7. reconciliar subscription/payment/ledger;
8. registrar ajuste manual como ledger entry auditada;
9. verificar impacto fiscal;
10. comunicar cliente quando necessário.
