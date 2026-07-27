# Roadmap da integração de pagamentos

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## Pré-requisitos

- empresa formalizada;
- Core musical estável;
- custos medidos;
- contas permanentes implementadas;
- modelo de planos aprovado;
- fiscal definido;
- termos e privacidade revisados.

## Fases

### B0 — domínio interno

- plans, prices, entitlements;
- credit wallet e ledger;
- usage reservation;
- estados de subscription/payment/refund;
- testes sem gateway.

### B1 — adapter e sandbox

- Stripe e Mercado Pago em spikes separados;
- checkout hospedado;
- webhook;
- consulta/reconciliação;
- sem produção.

### B2 — provedor escolhido

- ADR aceita;
- SDK fixado;
- secrets manager;
- feature flag;
- ambiente de teste integrado.

### B3 — assinatura e portal

- compra;
- renovação;
- falha de cobrança;
- cancelamento;
- upgrade/downgrade;
- portal do cliente.

### B4 — créditos e jobs

- quote;
- reserva;
- consumo;
- liberação;
- reversão;
- concorrência e idempotência.

### B5 — reembolso, disputa e reconciliação

- full/partial refund;
- chargeback;
- ledger reversal;
- conciliação diária;
- alertas.

### B6 — homologação fiscal e lançamento

- integração NFS-e;
- termos finais;
- teste E2E financeiro/fiscal;
- revisão contábil;
- produção controlada.
