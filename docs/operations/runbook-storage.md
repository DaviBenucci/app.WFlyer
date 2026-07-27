# Runbook — storage indisponível ou inconsistente

> Status: runbook de referência; deve ser validado por exercício antes do lançamento. Revisão: 2026-07-27.

1. verificar acesso, policy, KMS e região;
2. distinguir falha de upload, leitura e publicação;
3. pausar novos jobs se source não estiver confirmado;
4. não marcar artefato como disponível sem objeto/hash;
5. renovar URLs temporárias, não tornar bucket público;
6. reconciliar banco x objetos;
7. restaurar/corrigir cópia conforme runbook;
8. registrar objetos órfãos e ausentes;
9. validar lifecycle;
10. comunicar impacto de downloads.
