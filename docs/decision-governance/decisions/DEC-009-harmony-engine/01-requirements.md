# Requisitos — DEC-009

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Engine ou solver de harmonização**;
- fase limite: `H1:exit`;
- owner: `music_engineering_lead`;
- evidências: `EVID-010`, `EVID-009`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] melodia preservada por invariante
- [ ] planos reproduzíveis e provenance completa
- [ ] restrições rígidas independentes do gerador
- [ ] avaliação cega por músicos
- [ ] licença/dados/custo aprovados
- [ ] variante só publicada após escolha do usuário

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_LICENSE_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
