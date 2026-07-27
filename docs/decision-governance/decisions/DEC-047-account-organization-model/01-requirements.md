# Requisitos — DEC-047

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Modelo de conta, autenticação e organizações**;
- fase limite: `B0:entry`;
- owner: `product_owner`;
- evidências: `EVID-048`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] migração explícita e idempotente de sessão anônima para conta
- [ ] verificação e recuperação de e-mail seguras
- [ ] ownership, revogação, RBAC e organizações documentados
- [ ] rate limiting, auditoria e threat model aprovados
- [ ] retenção, exclusão e minimização de dados definidas
- [ ] billing nunca vinculado somente a sessão anônima

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_PRODUCT_SCOPE`
- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_IMPLEMENTATION`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
