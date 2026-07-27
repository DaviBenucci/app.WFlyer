# Comparativo: Stripe e Mercado Pago

> Status: comparação técnica preliminar em 2026-07-27. Taxas, disponibilidade por conta e exigências comerciais devem ser verificadas novamente no spike.

## Matriz

| Critério | Stripe | Mercado Pago |
|---|---|---|
| Assinaturas | Billing com ciclo completo | API de assinaturas e planos |
| Pix recorrente | Pix Automático documentado | validar fluxo exato disponível para a conta |
| Portal do cliente | hospedado e configurável | gestão pelo ecossistema e/ou telas próprias |
| Cobrança por uso | forte suporte | maior lógica interna provável |
| Upgrade/downgrade | recursos amplos | gerenciamento, pausa, cancelamento e pro rata documentados |
| Internacionalização | alta aderência | foco forte na América Latina |
| Familiaridade no Brasil | média/alta | muito alta |
| Webhooks | eventos amplos | assinatura secreta e eventos |
| Complexidade | maior, com domínio rico | mais direto em casos simples |

## Stripe — vantagens

- assinatura, faturas, trials e portal de autoatendimento;
- Pix Automático para recorrência documentado;
- boa modelagem para SaaS e cobrança por uso;
- expansão internacional;
- checkout hospedado;
- documentação de webhooks e idempotência.

## Stripe — riscos/desvantagens

- maior quantidade de conceitos;
- custos e recursos precisam ser confirmados para a conta brasileira;
- uso incorreto de estados de invoice/subscription pode liberar acesso indevido;
- dependência operacional do Billing se o domínio interno não for bem isolado.

## Mercado Pago — vantagens

- marca conhecida pelo público brasileiro;
- assinaturas automáticas;
- periodicidade configurável;
- novas tentativas em recusas;
- pausa, cancelamento e reativação;
- checkout e links com boa aderência local.

## Mercado Pago — riscos/desvantagens

- cobrança por uso e ledger continuarão sendo responsabilidade do W_Flyer;
- expansão internacional menos uniforme;
- portal e fluxos avançados podem exigir mais telas próprias;
- Pix recorrente e eventos exatos devem ser comprovados na conta/sandbox vigente.

## Conclusão preliminar

```text
Candidato preferencial: Stripe
Alternativa: Mercado Pago
Decisão final: bloqueada até spike sandbox + análise comercial + validação contábil
```

## Fontes oficiais

- Stripe Subscriptions: https://docs.stripe.com/subscriptions
- Stripe Pix recorrente: https://docs.stripe.com/billing/subscriptions/pix
- Stripe Customer Portal: https://docs.stripe.com/customer-management
- Stripe webhooks: https://docs.stripe.com/billing/subscriptions/webhooks
- Mercado Pago Assinaturas: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/overview
- Mercado Pago gerenciamento: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/subscription-management
- Mercado Pago webhooks: https://www.mercadopago.com.br/developers/pt/docs/subscriptions/additional-content/your-integrations/notifications/webhooks
