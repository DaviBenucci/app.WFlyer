# Webhooks, idempotência e reconciliação

> Status: arquitetura proposta; cobrança de produção permanece desabilitada. Revisão: 2026-07-27.

## 1. Webhook é a confirmação assíncrona

O retorno do navegador não ativa plano. O backend valida o webhook e confirma o estado com o provedor quando necessário.

## 2. Pipeline

```text
receive raw body
→ verify signature
→ persist event id/payload hash
→ acknowledge quickly
→ process asynchronously
→ apply idempotent transition
→ record audit
```

## 3. Duplicatas e ordem

- `external_event_id` único;
- eventos antigos não podem regredir estado mais novo;
- transições inválidas vão para revisão;
- handler pode ser repetido;
- side effects usam chaves idempotentes.

## 4. Reconciliação

Job periódico compara:

- assinaturas internas x externas;
- pagamentos;
- reembolsos;
- disputas;
- faturas pendentes;
- eventos não processados.

Divergências geram alerta e não são corrigidas silenciosamente sem regra.

## 5. Segurança

- segredo por ambiente;
- corpo bruto quando exigido;
- limite de tamanho;
- rate limit;
- log sem dados sensíveis;
- replay protection;
- endpoint não depende de sessão do usuário;
- rotação documentada.
