# Fontes oficiais — empresa, billing, fiscal e infraestrutura

> Status: referência. Revisão: 2026-07-27.

Este arquivo registra fontes oficiais utilizadas na arquitetura proposta. As páginas podem mudar; a implementação deve consultar a versão vigente no momento da decisão.

## Abertura e regularização

- Redesim: https://www.gov.br/empresas-e-negocios/pt-br/redesim
- Registrar empresa: https://www.gov.br/empresas-e-negocios/pt-br/drei/orientacoes-de-abertura/quero-registrar-minha-empresa
- Abrir CNPJ: https://www.gov.br/empresas-e-negocios/pt-br/redesim/abrir-cnpj

## Proteção de dados e comércio eletrônico

- LGPD compilada: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Decreto nº 7.962/2013: https://www.planalto.gov.br/ccivil_03/_ato2011-2014/2013/decreto/d7962.htm
- Guia da ANPD: https://www.gov.br/anpd/pt-br/centrais-de-conteudo/materiais-educativos-e-publicacoes/guia_lgpd_final.pdf

## NFS-e

- Documentação atual de produção: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual
- Serviço de emissão: https://www.gov.br/pt-br/servicos/emitir-nota-fiscal-de-servico-eletronica

## Stripe

- Subscriptions: https://docs.stripe.com/subscriptions
- Billing: https://docs.stripe.com/billing
- Pix recorrente: https://docs.stripe.com/billing/subscriptions/pix
- Customer Portal: https://docs.stripe.com/customer-management
- Webhooks: https://docs.stripe.com/billing/subscriptions/webhooks

## Mercado Pago

- Assinaturas: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/overview
- Gerenciamento: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/subscription-management
- Webhooks: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/additional-content/your-integrations/notifications/webhooks

## Domínio e AWS

- Registro.br: https://registro.br/
- Route 53 para CloudFront: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/routing-to-cloudfront-distribution.html
- Subdomínio no Route 53: https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/CreatingNewSubdomain.html
- Estratégia multi-account: https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html
- AWS Organizations: https://docs.aws.amazon.com/organizations/latest/userguide/orgs_best-practices.html
- RDS Multi-AZ: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.MultiAZ.html
- AWS Backup cross-region: https://docs.aws.amazon.com/aws-backup/latest/devguide/cross-region-backup.html
- RDS cross-region backup: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReplicateBackups.html
- SQS: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
- S3 Lifecycle: https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lifecycle-mgmt.html
