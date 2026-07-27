# Visão geral de cobrança

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## Estado

- empresa ainda não aberta;
- nenhum provedor escolhido definitivamente;
- nenhuma conta de produção deve ser criada como se a operação comercial já estivesse ativa;
- pagamento não faz parte do MVP Core;
- arquitetura interna deve ficar pronta para futura monetização.

## Modelo comercial preliminar

```text
demonstração limitada
+ assinatura com créditos mensais
+ compra avulsa de créditos
+ planos individuais/profissionais/institucionais
```

Preços, quotas e consumo só podem ser definidos após benchmarks de CPU, OMR, storage, tráfego, suporte, taxas e tributos.

## Princípios

- gateway não é fonte de verdade do domínio interno;
- frontend nunca concede plano;
- webhook validado confirma eventos assíncronos;
- dinheiro é armazenado em unidade mínima da moeda;
- créditos usam ledger imutável;
- processamento reserva crédito antes de iniciar;
- falha interna libera a reserva;
- efeitos financeiros são idempotentes;
- pagamentos e NFS-e são fluxos separados;
- provedor é acessado por adapter.

## Parâmetros ainda não aprovados

Os documentos abaixo estruturam a futura decisão sem inventar números:

- `08-parametros-precos-planos.md` — campos e critérios de aprovação;
- `09-sistema-creditos-detalhado.md` — lifecycle completo do crédito;
- `10-formulario-decisao-precos-creditos.md` — formulário para preencher após benchmarks;
- `pricing-config.template.yaml` — catálogo machine-readable ainda não aprovado.

Qualquer valor `null` ou `PENDENTE` bloqueia a ativação comercial correspondente.
