# Requisitos — DEC-025

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Natureza jurídica, CNAEs e regime tributário**;
- fase limite: `F0:exit`;
- owner: `business_owner`;
- evidências: `EVID-026`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] CNPJ e município confirmados
- [ ] memorando contábil registrado
- [ ] matriz de serviços
- [ ] regime e inscrições aprovados
- [ ] impacto em preço/fiscal documentado

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
