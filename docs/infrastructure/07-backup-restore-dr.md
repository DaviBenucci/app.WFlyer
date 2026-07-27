# Backup, restauração e disaster recovery

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Princípio

Backup só é válido depois de restauração testada.

## Banco

- backup automático;
- point-in-time recovery;
- snapshot antes de mudanças críticas;
- cópia cross-region quando o gate comercial exigir;
- retenção por ambiente;
- criptografia;
- teste periódico.

## S3

- lifecycle;
- versionamento para classes selecionadas;
- replicação/cópia para artefatos críticos conforme custo;
- inventário;
- teste de recuperação;
- retenção alinhada à privacidade.

## Configuração

- infraestrutura como código;
- secrets não ficam no backup comum;
- zona DNS exportada/documentada;
- imagens e versões fixadas;
- runbooks versionados.

## Metas preliminares

```text
RPO banco: até 5 minutos, sujeito a custo
RTO banco: até 60 minutos, sujeito a teste
RPO artefatos: conforme confirmação de upload/publicação
RTO completo: definido após exercício de DR
```

Não publicar SLA com esses números antes de medi-los.

## Estratégia regional inicial

- produção em São Paulo;
- backups selecionados em outra região;
- infraestrutura reproduzível;
- sem active-active multi-region no primeiro lançamento.

## Fontes oficiais

- AWS Backup cross-region: https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html
- RDS cross-region backups: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html
- RDS backup/restore: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_CommonTasks.BackupRestore.html
