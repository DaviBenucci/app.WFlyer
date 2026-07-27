# Runbook — API indisponível

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. confirmar impacto por health check externo;
2. verificar CloudFront/WAF/ALB;
3. verificar tarefas ECS e readiness;
4. correlacionar deploy recente;
5. verificar banco, secrets e dependências;
6. pausar deploy/rollback se necessário;
7. ativar status page;
8. preservar jobs e uploads;
9. validar recuperação com transação de teste;
10. registrar causa, duração e ação preventiva.

Não reiniciar repetidamente sem identificar crash loop ou dependência.
