# Assinaturas, créditos e ledger

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## 1. Entidades

```text
Plan
PlanPrice
Subscription
Entitlement
CreditWallet
CreditLedgerEntry
UsageQuote
UsageReservation
Payment
Refund
```

## 2. Ledger

O saldo não deve ser alterado diretamente. Cada mudança cria uma entrada imutável:

- monthly_grant;
- purchase;
- reservation;
- consumption;
- release;
- refund;
- expiration;
- manual_adjustment.

Uma correção cria entrada compensatória; não apaga o histórico.

## 3. Reserva

```text
quote
→ transação bloqueia saldo
→ reservation criada
→ job criado
→ sucesso: consume
→ falha interna: release
```

A reserva e a criação do job devem participar de uma transação/outbox coerente.

## 4. Valores monetários

```text
amount_minor = 2990
currency = BRL
```

Nunca usar `float` para dinheiro.

## 5. Direitos

O acesso resulta de:

```text
capability técnica
AND entitlement do plano
AND quota/crédito
AND compatibilidade do arquivo
```

O gateway não define sozinho o que a aplicação pode executar.

## 6. Concorrência

- lock/transação no wallet;
- idempotency key por operação;
- unique constraint para efeito externo;
- sem saldo negativo, salvo regra explícita;
- retry seguro;
- teste com jobs simultâneos.

## 7. Especificação detalhada

Este documento apresenta o núcleo. O comportamento completo, incluindo lotes, expiração, cotação, falhas parciais, organizações, API, concorrência e testes, está em `09-sistema-creditos-detalhado.md`.

Preços, quantidades e validade são preenchidos somente em `08-parametros-precos-planos.md`, `10-formulario-decisao-precos-creditos.md` e `pricing-config.template.yaml`.
