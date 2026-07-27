# Arquitetura AWS de produção

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Região

Alvo inicial: São Paulo (`sa-east-1`), sujeito a análise de custo e disponibilidade dos serviços escolhidos.

## Topologia

```text
Route 53
→ CloudFront + WAF
→ ALB
→ ECS services
   ├── web
   └── api

Outbox/dispatcher
→ SQS queues + DLQ
→ worker pools
   ├── core MusicXML
   ├── OMR futuro
   ├── render futuro
   ├── audio futuro
   ├── billing futuro
   └── fiscal futuro

Data
├── RDS PostgreSQL Multi-AZ
├── S3 privado
├── Redis/ElastiCache para cache/coordenação curta
└── CloudWatch/log archive
```

## Contas

Produção comercial alvo:

```text
management
├── development
├── production
└── log-archive/security (quando adotado)
```

Não executar workloads no management account.

## Banco

- Multi-AZ;
- backups automáticos;
- PITR;
- criptografia;
- pool de conexões;
- alarms;
- migrations controladas;
- restore testado.

## Fila

ADR deverá comparar Celery/Redis previsto originalmente com SQS/adapters. Em AWS, SQS + DLQ oferece fila gerenciada durável; PostgreSQL continua fonte autoritativa.

## Storage

- quarantine;
- source;
- intermediate;
- artifacts;
- exports;
- fiscal.

Buckets privados, URLs temporárias e lifecycle.

## Fontes oficiais

- RDS Multi-AZ: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
- SQS: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
- S3 Lifecycle: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
- ECS Fargate: https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html
