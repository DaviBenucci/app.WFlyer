# Requisitos — DEC-006

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Expansão para multiparte e multipauta**;
- fase limite: `M0:exit`;
- owner: `music_engineering_lead`;
- evidências: `EVID-007`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] round trip semântico do corpus multiparte
- [ ] IDs estáveis e política de cross-staff
- [ ] UX de seleção e erros definida
- [ ] instrumentos por parte validados
- [ ] consistência score/partes testada

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
