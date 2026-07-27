# Sistema de créditos — funcionamento detalhado

> Status: arquitetura proposta e parametrizável. Quantidades, validade e valores permanecem pendentes. Revisão: 2026-07-27.

## 1. Por que utilizar créditos

O W_Flyer terá operações com custos muito diferentes. Uma transposição MusicXML simples não possui o mesmo custo de um OMR de muitas páginas, de uma harmonização com várias variantes ou de um pacote para ensemble.

Os créditos permitem que cada plano conceda uma quantidade previsível de uso sem prometer processamento ilimitado antes de conhecer o custo real.

Crédito é uma **unidade interna de uso**. A redação jurídica final deverá confirmar que ele:

- não representa saldo bancário;
- não pode ser sacado;
- não rende juros;
- não pode ser transferido entre contas, salvo política institucional expressa;
- não substitui o registro monetário do pagamento;
- segue regras próprias de validade, reembolso e estorno.

Essas afirmações permanecem como proposta até revisão jurídica.

## 2. Tipos de crédito

| Tipo | Origem | Validade | Reembolso | Observação |
|---|---|---|---|---|
| Mensal | concessão do plano | `PENDENTE` | não convertido automaticamente em dinheiro | pode expirar no ciclo |
| Comprado | pacote avulso | `PENDENTE` | conforme política de compra/reembolso | deve ter lote identificável |
| Promocional | campanha ou convite | `PENDENTE` | normalmente não reembolsável | termos da promoção prevalecem |
| Compensatório | falha ou atendimento | `PENDENTE` | não é pagamento novo | exige motivo e operador |
| Institucional | contrato da organização | `PENDENTE` | conforme contrato | pode ser carteira compartilhada |

## 3. Saldo apresentado ao usuário

O sistema deve distinguir:

```text
saldo concedido
saldo reservado
saldo disponível
saldo consumido
saldo expirado
saldo estornado
```

A relação principal é:

```text
saldo disponível = saldo concedido - saldo reservado - saldo consumido - saldo expirado + estornos aplicáveis
```

O frontend exibe o saldo calculado pelo backend. Ele não recalcula o ledger por conta própria.

## 4. Ledger imutável

O saldo é derivado de entradas imutáveis. Não existe coluna de saldo editada manualmente como única fonte de verdade.

Tipos mínimos:

```text
monthly_grant
purchased_grant
promotional_grant
compensatory_grant
reservation
consumption
release
expiration
refund_reversal
chargeback_reversal
manual_adjustment_credit
manual_adjustment_debit
migration_adjustment
```

Cada entrada contém:

```text
entry_id
wallet_id
entry_type
amount_credits
related_reservation_id
related_job_id
related_payment_id
related_subscription_id
idempotency_key
reason_code
created_at
created_by_type
created_by_id
metadata_minimized
```

Uma correção cria uma entrada compensatória. Nunca se apaga a entrada original.

## 5. Cotação antes do processamento

Antes de iniciar um job, a API gera uma cotação:

```text
operation
billing_unit
estimated_units
credit_cost_per_unit
total_credit_cost
quote_expires_at
pricing_catalog_version
assumptions
```

A interface deve mostrar:

- operação solicitada;
- quantidade cobrada;
- custo total em créditos;
- saldo atual;
- saldo após a operação;
- situações que podem alterar a cotação;
- prazo de validade da cotação.

Nenhum custo adicional pode ser aplicado silenciosamente depois da confirmação.

## 6. Reserva

Fluxo normal:

```text
1. usuário confirma a cotação
2. backend valida conta, entitlement e capability
3. transação bloqueia a carteira
4. reserva é criada
5. créditos deixam de estar disponíveis
6. job e outbox são criados na mesma unidade de consistência
7. worker recebe o job
```

Estados da reserva:

```text
pending
active
consumed
released
expired
reversed
```

Transições permitidas:

```text
pending → active
active → consumed
active → released
active → expired
consumed → reversed
```

Transições fora desse conjunto são rejeitadas.

## 7. Consumo

Créditos são consumidos somente quando o resultado comercialmente cobrável foi produzido.

### Transformação determinística

A reserva é consumida depois que:

- o job conclui;
- o verificador independente aprova;
- o artefato é publicado atomicamente;
- o resultado fica acessível ao usuário.

### Operação criativa

Harmonização e adaptação podem cobrar por variante ou parte. O sistema deve definir no catálogo qual evento liquida a reserva:

```text
variante gerada e validada
parte gerada e validada
pacote completo publicado
```

Resultado parcial não pode ser tratado automaticamente como resultado completo.

## 8. Liberação

A reserva é liberada quando:

- formato é rejeitado antes do processamento cobrável;
- capability está indisponível;
- falha interna impede resultado publicável;
- verificador reprova o resultado;
- worker excede tentativas e vai para DLQ;
- cancelamento ocorre antes do ponto de liquidação;
- prazo da reserva expira sem job válido.

A liberação deve ser idempotente. Repetir o evento não devolve créditos duas vezes.

## 9. Falhas parciais

### OMR de várias páginas

A política deve escolher um dos modelos antes da ativação:

```text
A. cobrar somente se todas as páginas concluírem;
B. cobrar por página concluída e claramente disponibilizada;
C. bloquear resultado parcial e liberar tudo.
```

Decisão: `PENDENTE`.

### Pacote ensemble

A política deve escolher:

```text
A. pacote atômico: tudo ou nada;
B. cobrança por parte publicada;
C. pacote base + partes adicionais.
```

Decisão: `PENDENTE`.

### Harmonização com múltiplas variantes

A quantidade de variantes incluída e o custo de regeneração devem aparecer antes da confirmação.

## 10. Ordem de consumo dos lotes

Quando a carteira possui créditos de origens diferentes, a ordem deve ser determinística.

Opções a avaliar:

- primeiro o lote que expira mais cedo;
- primeiro promocionais;
- primeiro concessão mensal;
- primeiro comprados.

Recomendação técnica inicial: **expiração mais próxima primeiro**, respeitando restrições jurídicas e promocionais.

Decisão final: `PENDENTE`.

## 11. Renovação da assinatura

No início de cada ciclo aprovado:

```text
invoice/payment confirmado
→ subscription period atualizado
→ monthly_grant criado uma única vez
→ entitlements atualizados
```

A idempotency key deve impedir concessão duplicada quando o webhook for reenviado.

Questões pendentes:

- créditos mensais acumulam? `PENDENTE`;
- há teto de acúmulo? `PENDENTE`;
- créditos são concedidos em trial? `PENDENTE`;
- ciclo proporcional em upgrade concede diferença? `PENDENTE`;
- downgrade reduz lote futuro ou atual? `PENDENTE`.

## 12. Compra avulsa

Fluxo:

```text
checkout criado
→ pagamento confirmado por webhook
→ purchased_grant criado
→ usuário recebe comprovante e histórico
```

Nunca conceder créditos somente porque o navegador voltou para uma página de sucesso.

## 13. Reembolso e chargeback

### Reembolso

A política deve considerar:

- créditos ainda não consumidos;
- créditos parcialmente consumidos;
- serviço já entregue;
- direito aplicável;
- reembolso parcial;
- cancelamento ou substituição fiscal.

O ledger registra reversão; não apaga a compra.

### Chargeback

Quando confirmado:

- registrar evento financeiro;
- impedir concessão duplicada;
- avaliar reversão de créditos remanescentes;
- preservar evidências;
- não apagar projetos por automação financeira;
- limitar novos jobs de alto custo conforme política de risco;
- encaminhar casos duvidosos para revisão.

## 14. Expiração

A expiração é um job de domínio, não simples exclusão de linha.

```text
lote elegível
→ expiration entry
→ saldo recalculado
→ notificação quando aplicável
→ auditoria
```

O usuário deve conseguir ver:

- quantidade a expirar;
- data de expiração;
- origem do lote;
- política aplicável.

Os prazos permanecem `PENDENTE` até decisão comercial e jurídica.

## 15. Organizações

Uma organização poderá usar:

- carteira compartilhada;
- carteiras por equipe;
- limites por membro;
- aprovação para jobs caros;
- orçamento mensal;
- alertas de consumo;
- centro de custo.

A primeira versão institucional deve escolher somente um modelo para evitar saldos inconsistentes.

## 16. Concorrência e consistência

Invariantes obrigatórias:

```text
saldo disponível nunca fica negativo
uma reserva só liquida uma vez
um job não consome duas vezes
um webhook não concede duas vezes
uma liberação não devolve duas vezes
entrada de ledger não é editada
cada efeito externo possui unique constraint/idempotency key
```

Mecanismos:

- transação no PostgreSQL;
- lock pessimista ou atualização condicional versionada;
- unique constraints;
- outbox transacional;
- consumidor idempotente;
- reconciliação periódica.

## 17. Modelo de dados mínimo

```text
credit_wallets
credit_lots
credit_ledger_entries
usage_quotes
usage_reservations
usage_settlements
pricing_catalogs
pricing_operation_rates
billing_reconciliation_findings
```

O saldo materializado pode existir para performance, mas deve ser reconciliável com o ledger.

## 18. API planejada

```text
GET  /api/v1/billing/credits/balance
GET  /api/v1/billing/credits/ledger
GET  /api/v1/billing/credits/expirations
POST /api/v1/usage/quotes
POST /api/v1/usage/reservations
POST /api/v1/usage/reservations/{id}/cancel
GET  /api/v1/usage/reservations/{id}
```

Endpoints internos de liquidação não ficam expostos ao navegador.

## 19. Estados de interface

A interface deve cobrir:

- saldo suficiente;
- saldo insuficiente;
- cotação expirada;
- preço alterado antes da confirmação;
- reserva em criação;
- reserva ativa;
- job concluído e cobrado;
- job falhou e créditos retornaram;
- créditos próximos da expiração;
- ledger indisponível temporariamente;
- divergência em reconciliação sob análise.

## 20. Testes obrigatórios

### Unitários

- cálculo de saldo;
- ordem de consumo;
- expiração;
- reserva;
- consumo;
- liberação;
- estorno;
- upgrade/downgrade.

### Property-based

- saldo nunca negativo;
- soma do ledger igual ao saldo derivado;
- repetir o mesmo comando não muda o resultado;
- qualquer reserva finalizada termina em um único estado terminal.

### Concorrência

- dois jobs disputando o último crédito;
- webhook duplicado;
- dois workers liquidando a mesma reserva;
- cancelamento simultâneo à conclusão;
- expiração simultânea à reserva.

### Reconciliação

- saldo materializado divergente;
- pagamento sem concessão;
- concessão sem pagamento;
- job concluído sem consumo;
- job falho com reserva ativa.

## 21. Decisões que permanecem abertas

- quantidade de créditos por plano;
- custo de cada operação;
- validade de cada tipo de lote;
- acúmulo mensal;
- ordem de consumo;
- tratamento de resultados parciais;
- regra de trial;
- créditos em upgrade/downgrade;
- política institucional;
- relação entre reembolso e créditos já consumidos.

A IA não pode resolver essas decisões por conveniência de implementação.
