# Parâmetros de preços e planos

> Status: modelo para preenchimento futuro. Nenhum preço comercial foi aprovado. Revisão: 2026-07-27.

## 1. Objetivo

Este documento define **quais campos deverão ser preenchidos** quando o W_Flyer já tiver benchmarks reais de custo, taxa de falha, demanda e suporte.

A ausência de valores é intencional. A IA não pode inventar preços, quotas ou descontos para completar telas, testes ou seed de produção.

O arquivo machine-readable relacionado é:

```text
docs/billing/pricing-config.template.yaml
```

Ele deve permanecer com `status: pending_measurement` enquanto houver valores obrigatórios sem decisão.

## 2. Regras de preenchimento

- moeda comercial inicial: `BRL`;
- dinheiro é armazenado em centavos inteiros;
- percentuais são armazenados em basis points;
- preço exibido no frontend vem do catálogo interno autorizado pela API;
- o frontend nunca envia um valor monetário livre para criar checkout;
- o provedor de pagamento não é a fonte normativa dos planos;
- toda alteração gera nova versão do catálogo;
- planos já contratados mantêm o histórico de preço aplicável;
- valores só podem ser marcados como aprovados após benchmark, revisão contábil, revisão jurídica e spike do provedor.

Exemplos técnicos:

```text
R$ 29,90     → 2990 em amount_minor
2,50%        → 250 em basis points
12,00%       → 1200 em basis points
```

## 3. Premissas financeiras a preencher

| Campo | Valor | Fonte da decisão | Data | Responsável |
|---|---:|---|---|---|
| Taxa percentual do gateway | `PENDENTE` | contrato/proposta do provedor | `PENDENTE` | `PENDENTE` |
| Tarifa fixa por transação | `PENDENTE` | contrato/proposta do provedor | `PENDENTE` | `PENDENTE` |
| Taxa efetiva de tributos | `PENDENTE` | contador e regime tributário | `PENDENTE` | `PENDENTE` |
| Reserva para chargebacks | `PENDENTE` | histórico/risco | `PENDENTE` | `PENDENTE` |
| Reserva para reembolsos | `PENDENTE` | política aprovada | `PENDENTE` | `PENDENTE` |
| Custo médio de suporte por operação | `PENDENTE` | medição operacional | `PENDENTE` | `PENDENTE` |
| Margem de infraestrutura | `PENDENTE` | decisão financeira | `PENDENTE` | `PENDENTE` |
| Margem bruta alvo | `PENDENTE` | decisão financeira | `PENDENTE` | `PENDENTE` |
| Desconto do plano anual | `PENDENTE` | decisão comercial | `PENDENTE` | `PENDENTE` |

## 4. Custos internos a medir

Cada capability terá custo medido separadamente.

| Operação | Unidade | CPU | Memória | Storage | Tráfego | Terceiros | Falha/reprocesso | Custo total estimado |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| Transposição MusicXML | job | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| OMR de PDF | página | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| Extração de melodia | job | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| Variante de harmonização | variante | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| Adaptação idiomática | parte | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| Renderização de áudio | minuto iniciado | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |
| Pacote para ensemble | parte gerada | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` | `PENDENTE` |

A fórmula de análise deverá considerar, no mínimo:

```text
custo interno por unidade
= compute
+ storage
+ tráfego
+ serviços de terceiros
+ suporte alocado
+ reserva de falha/reprocessamento
+ custos financeiros
+ tributos aplicáveis
```

## 5. Planos a preencher

Os nomes abaixo são nomes de trabalho. Podem mudar antes do lançamento.

### 5.1 Gratuito

| Campo | Valor |
|---|---|
| Preço mensal | `R$ 0,00` |
| Créditos mensais | `PENDENTE` |
| Validade dos créditos | `PENDENTE` |
| Projetos ativos | `PENDENTE` |
| Storage incluído | `PENDENTE` |
| Retenção | `PENDENTE` |
| Capabilities | `PENDENTE` |
| Limites antiabuso | `PENDENTE` |

### 5.2 Músico

| Campo | Valor |
|---|---|
| Preço mensal | `R$ PENDENTE` |
| Preço anual | `R$ PENDENTE` |
| Créditos mensais | `PENDENTE` |
| Créditos acumulam? | `PENDENTE` |
| Projetos ativos | `PENDENTE` |
| Storage incluído | `PENDENTE` |
| Retenção | `PENDENTE` |
| Capabilities | `PENDENTE` |

### 5.3 Profissional

| Campo | Valor |
|---|---|
| Preço mensal | `R$ PENDENTE` |
| Preço anual | `R$ PENDENTE` |
| Créditos mensais | `PENDENTE` |
| Créditos acumulam? | `PENDENTE` |
| Projetos ativos | `PENDENTE` |
| Storage incluído | `PENDENTE` |
| Retenção | `PENDENTE` |
| Capabilities | `PENDENTE` |

### 5.4 Institucional

| Campo | Valor |
|---|---|
| Preço mensal | `R$ PENDENTE` |
| Preço anual | `R$ PENDENTE` |
| Créditos mensais compartilhados | `PENDENTE` |
| Usuários incluídos | `PENDENTE` |
| Usuário adicional | `R$ PENDENTE` |
| Projetos ativos | `PENDENTE` |
| Storage incluído | `PENDENTE` |
| Retenção | `PENDENTE` |
| Capabilities | `PENDENTE` |
| SLA contratual | `PENDENTE` |

## 6. Pacotes avulsos

| Pacote | Créditos | Preço | Validade | Disponível para |
|---|---:|---:|---|---|
| Pequeno | `PENDENTE` | `R$ PENDENTE` | `PENDENTE` | `PENDENTE` |
| Médio | `PENDENTE` | `R$ PENDENTE` | `PENDENTE` | `PENDENTE` |
| Grande | `PENDENTE` | `R$ PENDENTE` | `PENDENTE` | `PENDENTE` |

## 7. Custo em créditos por operação

| Operação | Unidade cobrada | Créditos | Limite por solicitação | Regra para nova tentativa |
|---|---|---:|---:|---|
| Transposição MusicXML | job | `PENDENTE` | `PENDENTE` | falha interna não cobra |
| OMR de PDF | página aceita | `PENDENTE` | `PENDENTE` | reprocesso técnico não cobra novamente |
| Extração de melodia | job | `PENDENTE` | `PENDENTE` | revisão humana não gera cobrança oculta |
| Harmonização | variante solicitada | `PENDENTE` | `PENDENTE` | regeneração informa custo antes |
| Adaptação idiomática | parte | `PENDENTE` | `PENDENTE` | alteração de parâmetros gera nova cotação |
| Renderização de áudio | minuto iniciado | `PENDENTE` | `PENDENTE` | falha de renderer libera reserva |
| Pacote ensemble | parte gerada | `PENDENTE` | `PENDENTE` | pacote parcial não é cobrado como completo |

## 8. Critérios para aprovar um preço

Um valor só pode migrar de `PENDENTE` para aprovado quando houver:

1. amostra suficiente de jobs reais ou benchmark representativo;
2. percentis de custo, não apenas média;
3. taxa de falha e reprocessamento;
4. custo do gateway confirmado;
5. cenário tributário validado pelo contador;
6. reserva para suporte, reembolso e chargeback;
7. margem aprovada;
8. teste de sensibilidade para picos de custo;
9. comparação com alternativas de mercado;
10. registro de decisão com data e responsável.

## 9. Bloqueios obrigatórios

A aplicação não pode entrar em cobrança de produção quando:

- houver `null` ou `PENDENTE` em campo comercial obrigatório;
- o catálogo estiver sem versão aprovada;
- o preço interno divergir do preço configurado no gateway;
- a política de créditos não estiver aprovada;
- os termos de pagamento e reembolso não tiverem revisão jurídica;
- o regime tributário e a emissão fiscal não estiverem confirmados;
- o spike do provedor não tiver concluído cenários de falha.

## 10. Histórico

Toda versão aprovada deve registrar:

```text
catalog_version
valid_from
valid_until
approved_by
benchmark_reference
accounting_review_reference
legal_review_reference
provider_price_ids
change_reason
```

Nunca sobrescrever o histórico comercial de uma assinatura existente.
