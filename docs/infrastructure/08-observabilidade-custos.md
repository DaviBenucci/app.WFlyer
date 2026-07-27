# Observabilidade e controle de custos

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Sinais

### Aplicação

- latência e erro HTTP;
- jobs por estado;
- idade da fila;
- duração por etapa;
- retries/DLQ;
- falhas musicais;
- downloads;
- sessões.

### Dados

- conexões, CPU, storage e IOPS do banco;
- cache hit;
- crescimento de tabelas;
- S3 por classe;
- backup e restore.

### Comercial futuro

- webhook atrasado;
- divergência de assinatura;
- crédito reservado há muito tempo;
- pagamento sem obrigação fiscal;
- NFS-e pendente/rejeitada.

## Logs

- estruturados;
- correlation ID;
- sem partitura, token, cartão ou certificado;
- retenção definida;
- acesso auditado.

## Custos

Tags mínimas:

```text
product
service
environment
owner
client
cost-center
```

Budgets e alarmes antes da produção. Medir custo por:

- página OMR;
- job MusicXML;
- render;
- GB armazenado;
- download;
- organização;
- cliente hospedado.

## Kill switches

- pausar OMR;
- pausar novos jobs;
- limitar variante de harmonização;
- suspender preview pesado;
- desabilitar feature com custo anormal.
