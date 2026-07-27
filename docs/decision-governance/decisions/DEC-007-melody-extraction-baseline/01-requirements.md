# Requisitos — DEC-007

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Baseline de extração de melodia**;
- fase limite: `L1:exit`;
- owner: `music_engineering_lead`;
- evidências: `EVID-008`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] corpus anotado por frase e por mais de um músico
- [ ] métricas de precisão/recall por evento e frase
- [ ] estratos cross-staff, voz interna e dobramento
- [ ] limiar de ambiguidade e alternativas visíveis
- [ ] zero selo verificado quando houver divergência material

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
