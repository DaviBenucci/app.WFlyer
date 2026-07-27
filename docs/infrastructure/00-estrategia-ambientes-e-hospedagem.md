# Estratégia de ambientes e hospedagem

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Princípio

Não usar uma única hospedagem como ponto de falha para site, SaaS, banco e clientes.

## Ambientes

```text
local
preview
staging
production
```

Dados de produção não são copiados para preview sem anonimização e autorização.

## Distribuição recomendada

| Componente | Estratégia |
|---|---|
| Site institucional | hospedagem gerenciada/static ou VPS separado |
| Aplicação | AWS São Paulo como alvo de produção |
| Banco SaaS | RDS PostgreSQL |
| Arquivos | S3 privado |
| Workers | ECS/Fargate ou pool aprovado por benchmark |
| Sites de clientes | contas/projetos isolados, fora do SaaS |
| Status page | provedor/ambiente independente |

## Desenvolvimento inicial

EasyPanel/VPS pode ser utilizado para desenvolvimento e demonstração. Não é considerado arquitetura final da aplicação paga quando hospeda todos os componentes na mesma máquina.

## Produção

A produção deve poder perder uma tarefa de web/API/worker sem perder dados ou interromper toda a plataforma.
