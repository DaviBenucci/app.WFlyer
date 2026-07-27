# Billing, assinaturas e créditos

> Status: arquitetura planejada; integração de produção bloqueada até a empresa estar formalizada e o produto musical praticamente estabilizado.

O objetivo desta pasta é impedir que pagamentos sejam adicionados de forma improvisada no final do projeto. A documentação prepara domínio, estados, segurança e testes, sem autorizar cobrança antes dos gates empresariais, fiscais e técnicos.

Ordem:

1. `00-visao-geral.md`;
2. `01-comparativo-stripe-mercado-pago.md`;
3. `02-adr-provedor-planejado.md`;
4. `03-roadmap-integracao-pagamentos.md`;
5. `04-spike-sandbox.md`;
6. `05-assinaturas-creditos-ledger.md`;
7. `06-webhooks-idempotencia-reconciliacao.md`;
8. `07-reembolsos-chargebacks.md`;
9. `08-parametros-precos-planos.md`;
10. `09-sistema-creditos-detalhado.md`;
11. `10-formulario-decisao-precos-creditos.md`;
12. `pricing-config.template.yaml`.

## Regra de valores pendentes

Enquanto custos reais não tiverem sido medidos, preços, quotas, validade e custos em créditos devem permanecer como `PENDENTE` ou `null`. A IA não pode completar esses campos para criar exemplos visuais, seeds ou testes de produção.
