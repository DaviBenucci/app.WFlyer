# Política de Pagamentos, Créditos e Assinaturas — estrutura do documento

> Status: rascunho. Preços, créditos e provedor permanecem pendentes.

## 1. Informações exibidas antes da compra

- plano ou pacote;
- preço total em BRL;
- periodicidade;
- tributos incluídos quando aplicável;
- créditos concedidos;
- validade dos créditos;
- renovação automática;
- data prevista da próxima cobrança;
- recursos incluídos;
- limites;
- regra de cancelamento;
- canal de suporte.

Todos os valores vêm do catálogo versionado. Campos atuais: `PENDENTE`.

## 2. Créditos

Explicar em linguagem simples:

- o que é um crédito;
- tipos de crédito;
- como consultar saldo;
- quando há reserva;
- quando há consumo;
- quando há devolução;
- validade;
- ordem de consumo;
- impossibilidade de saque ou transferência, se juridicamente aprovada.

## 3. Cotação por operação

Antes de confirmar um processamento cobrável, o usuário verá o custo em créditos. Se a cotação expirar ou o preço mudar, será necessária nova confirmação.

## 4. Assinaturas

Campos pendentes:

| Regra | Valor |
|---|---|
| Ciclo mensal | `PENDENTE` |
| Ciclo anual | `PENDENTE` |
| Renovação automática | `PENDENTE` |
| Trial | `PENDENTE` |
| Grace period | `PENDENTE` |
| Tentativas após falha | `PENDENTE` |
| Upgrade | `PENDENTE` |
| Downgrade | `PENDENTE` |

## 5. Confirmação

O retorno do navegador não confirma pagamento. O acesso é liberado depois da confirmação confiável do provedor e da reconciliação interna.

## 6. Falha do processamento

- falha interna antes de resultado cobrável: reserva liberada;
- resultado reprovado pelo verificador: reserva liberada;
- arquivo incompatível: sem consumo quando detectado antes do trabalho cobrável;
- resultado parcial: segue política específica ainda `PENDENTE`.

## 7. Histórico

O usuário poderá consultar pagamentos, faturas, créditos concedidos, reservas, consumos, expirações, estornos e ajustes relevantes.

## 8. Alteração de preços

- nova versão do catálogo;
- comunicação conforme aplicável;
- data de vigência;
- tratamento de assinaturas existentes;
- nenhuma alteração retroativa de histórico.
