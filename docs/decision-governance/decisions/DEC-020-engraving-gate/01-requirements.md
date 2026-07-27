# Requisitos — DEC-020

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Gate de engraving e legibilidade**;
- fase limite: `R1:exit`;
- owner: `qa_lead`;
- evidências: `EVID-021`, `EVID-003`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] detector de colisões testado
- [ ] matriz tela/impressão
- [ ] thresholds pré-registrados
- [ ] viradas e densidade aprovadas
- [ ] watermark avaliado em conjunto

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
