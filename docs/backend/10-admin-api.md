# Backend administrativo — fora do MVP

Este documento preserva a existência de uma ideia futura, mas ela não faz parte do MVP inicial.

## Regra

Não implementar API administrativa até existir decisão explícita posterior.

## Motivo

O MVP deve validar transposição musical, upload, jobs, worker, status e download. Painéis internos aumentam escopo, autenticação, permissões e auditoria antes da validação principal do produto.

## Permitido no MVP

- Registrar `correlation_id`.
- Guardar eventos de job.
- Guardar erro categorizado.
- Manter DTO público sem dados internos.

## Proibido no MVP

- Criar rotas administrativas.
- Criar painel administrativo.
- Expor métricas internas ao usuário comum.
- Criar RBAC.
- Criar moderação.
