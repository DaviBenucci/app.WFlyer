# ADR proposta — provedor de pagamento

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

- ID: ADR-BILL-001
- Status: **proposta, não aceita**
- Candidato: Stripe
- Alternativa: Mercado Pago
- Data: 2026-07-27

## Contexto

O W_Flyer poderá cobrar assinaturas, créditos adicionais e planos institucionais. O produto começará no Brasil, mas pode expandir. A empresa ainda não está aberta e o produto musical não possui custos medidos.

## Decisão proposta

Planejar a arquitetura para Stripe, sem acoplar o domínio. Não instalar SDK nem criar objetos de produção até o gate comercial.

## Condições de aceitação

- empresa formalizada;
- conta aprovada;
- cenários do spike concluídos;
- taxas simuladas;
- Pix/cartão confirmados;
- webhooks, reembolso e cancelamento testados;
- processo fiscal definido;
- política jurídica/consumerista validada;
- fallback operacional documentado.

## Consequências

- `BillingProvider` interno;
- IDs externos ficam no módulo de billing;
- planos e direitos são internos;
- troca futura exige novo adapter, não alteração do motor musical;
- Stripe continua sem efeito até ADR passar para `accepted`.

## Critério de rejeição

A proposta deve ser reavaliada se Mercado Pago oferecer, no momento do lançamento, melhor disponibilidade brasileira, custos, conversão, suporte ou requisitos de conta para os fluxos comprovados.
