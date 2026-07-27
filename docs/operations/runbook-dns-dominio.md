# Runbook — DNS ou domínio

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. verificar expiração do domínio e status no registrador;
2. verificar nameservers e DNSSEC;
3. consultar registros em múltiplos resolvedores;
4. verificar certificado;
5. comparar zona com versão documentada;
6. remover registro órfão somente após confirmar dependência;
7. usar rollback de zona;
8. considerar propagação/TTL;
9. manter status page em domínio/provedor independente;
10. registrar alteração e responsável.
