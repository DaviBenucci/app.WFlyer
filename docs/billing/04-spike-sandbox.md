# Spike sandbox: Stripe versus Mercado Pago

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## Objetivo

Comparar os dois provedores com os mesmos cenários, evidências e critérios. Não selecionar por preferência subjetiva ou apenas por taxa anunciada.

## Cenários obrigatórios

1. criar cliente;
2. checkout mensal;
3. cartão aprovado;
4. cartão recusado;
5. recorrência Pix disponível;
6. renovação;
7. retry;
8. upgrade imediato;
9. downgrade no ciclo seguinte;
10. cancelamento ao final;
11. reembolso integral e parcial;
12. webhook duplicado;
13. evento fora de ordem;
14. assinatura inválida;
15. indisponibilidade temporária;
16. portal/autosserviço;
17. reconciliação por API;
18. exportação para contabilidade.

## Métricas

- complexidade de implementação;
- cobertura de estados;
- qualidade de sandbox;
- clareza da documentação;
- suporte;
- tempo de integração;
- custos totais;
- conversão prevista;
- recursos brasileiros;
- portabilidade;
- observabilidade.

## Evidência

Cada cenário deve conter:

```text
request/ação
→ evento recebido
→ estado interno esperado
→ efeito no entitlement/ledger
→ compensação em falha
→ teste automatizado
```

## Gate

Nenhum provedor é aprovado sem webhooks idempotentes, reconciliação e cancelamento/reembolso funcionais.
