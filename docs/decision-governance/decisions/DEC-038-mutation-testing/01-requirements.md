# Requisitos — DEC-038

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Escopo e cadência de mutation testing**;
- fase limite: `FUTURE-MUTATION:entry`;
- owner: `qa_lead`;
- evidências: `EVID-039`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] piloto em motor musical/ledger
- [ ] tempo e sobreviventes medidos
- [ ] threshold e exceções aprovados
- [ ] não bloquear bootstrap prematuramente

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_COST_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
