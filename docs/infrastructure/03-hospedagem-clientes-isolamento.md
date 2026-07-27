# Isolamento de hospedagem de clientes

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Regra

A conta de produção do W_Flyer não hospeda sites de clientes.

## Opções

- provedor contratado pelo cliente;
- conta/projeto separado gerenciado;
- hospedagem compartilhada com contas isoladas para baixo risco;
- AWS do cliente ou conta separada quando necessário.

## Proibições

- banco compartilhado entre clientes sem arquitetura multi-tenant aprovada;
- credencial administrativa única;
- backup somente no mesmo servidor;
- cliente com acesso à infraestrutura do SaaS;
- reutilizar secrets;
- misturar custos sem tags/registro;
- expor preview publicamente sem necessidade.

## Incidente

Um incidente de cliente deve ter blast radius limitado à unidade daquele cliente. Logs, backup e restauração também devem ser isolados.
