# Requisitos — DEC-022

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Colaboração, identidade e retenção**;
- fase limite: `C0:exit`;
- owner: `product_owner`;
- evidências: `EVID-023`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] threat model e IDOR testados
- [ ] ETag/conflitos explícitos
- [ ] revogação imediata
- [ ] retenção e anonimização aprovadas
- [ ] âncoras versionadas

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
