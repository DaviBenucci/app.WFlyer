# Reembolsos, cancelamentos e chargebacks

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## Cancelamento

Padrão proposto para assinatura:

- cancelamento ao final do período;
- cancelamento imediato apenas quando política permitir;
- acesso existente preservado até `current_period_end` quando pago;
- confirmação clara ao usuário.

## Reembolso

- solicitação registrada;
- elegibilidade calculada por política aprovada;
- chamada ao provedor idempotente;
- estado `pending` até confirmação;
- ledger revertido somente com evento confirmado;
- NFS-e cancelada/substituída conforme orientação fiscal.

## Chargeback

- não apagar histórico;
- bloquear novos processamentos de alto custo quando necessário;
- preservar acesso a dados conforme política e obrigação legal;
- registrar evidências;
- reconciliar ledger e financeiro;
- notificar suporte/risco.

## Direito de arrependimento

O fluxo online deve oferecer mecanismo claro e compatível com a legislação aplicável, com validação jurídica antes do lançamento.

## Testes

- reembolso duplicado;
- partial refund;
- refund após crédito consumido;
- disputa após renovação;
- evento fora de ordem;
- falha fiscal depois do reembolso;
- cancelamento durante grace period.
