# Política de Cancelamento e Reembolso — estrutura do documento

> Status: rascunho. Deve ser validado conforme público, canal de venda e legislação aplicável.

## 1. Cancelamento de assinatura

Definir:

- cancelamento imediato ou ao fim do ciclo;
- data de perda dos benefícios;
- uso de créditos remanescentes;
- acesso a projetos e downloads;
- retenção após cancelamento;
- reativação.

Valores atuais: `PENDENTE`.

## 2. Solicitação de reembolso

A interface deve oferecer canal claro e protocolo. O sistema registra:

```text
request_id
purchase_id
reason_category
requested_at
status
analysis_notes
provider_refund_id
fiscal_follow_up
resolved_at
```

## 3. Critérios

A política final deve separar:

- assinatura ainda não utilizada;
- pacote de créditos intacto;
- créditos parcialmente consumidos;
- serviço digital já entregue;
- falha atribuível ao W_Flyer;
- cobrança duplicada;
- fraude ou chargeback;
- obrigação legal aplicável.

Não automatizar negativa apenas porque um crédito foi reservado.

## 4. Prazo e forma

```text
PRAZO_DE_ANALISE: PENDENTE
PRAZO_DE_ESTORNO: depende do meio e provedor; redação final pendente
FORMA_DE_REEMBOLSO: preferencialmente o meio original, conforme suporte e obrigação aplicável
```

## 5. Créditos

- reembolso confirmado gera reversão no ledger;
- entrada original é preservada;
- crédito já consumido exige regra aprovada;
- crédito compensatório não é automaticamente conversível em dinheiro;
- chargeback pode bloquear novos processamentos durante análise, sem exclusão automática de dados.

## 6. Comunicação

Exibir protocolo, estado, motivo, valor, créditos afetados, efeitos fiscais e canal de contestação.
