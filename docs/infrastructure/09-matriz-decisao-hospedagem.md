# Matriz de decisão de hospedagem

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Decisões separadas

Não escolher um único provedor para tudo apenas por conveniência.

| Workload | Opções | Critério principal |
|---|---|---|
| Site institucional | managed hosting, static platform, VPS | simplicidade, SEO, custo, rollback |
| Clientes simples | hosting gerenciado/contas isoladas | suporte e isolamento |
| SaaS | AWS | resiliência, workers, storage, banco |
| Status | provedor externo | independência |

## Avaliação do site institucional

- suporta Next.js/static;
- domínio customizado;
- HTTPS;
- preview;
- logs;
- formulários/serverless ou API segura;
- backup/exportação;
- preço previsível;
- suporte.

## Avaliação de hospedagem de clientes

- contas separadas;
- backup externo;
- restore;
- limites;
- segurança de WordPress, se aplicável;
- e-mail não acoplado ao servidor web quando possível;
- migração;
- painel e auditoria.

## Avaliação AWS do app

- custo em `sa-east-1`;
- serviços disponíveis;
- Fargate versus EC2;
- RDS Multi-AZ;
- SQS versus Celery/Redis;
- S3 e saída;
- observabilidade;
- suporte operacional.

## Gate de escolha

Criar planilha de custo para três cenários:

1. beta com baixo uso;
2. lançamento comercial;
3. crescimento com OMR.

A decisão deve registrar custo fixo, variável, limites, risco e plano de migração.
