# Requisitos — DEC-014

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Baseline e aprovação dos golden examples**;
- fase limite: `FE0:exit;
- owner: `design_owner`;
- evidências: `EVID-015`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] Core e futuro claramente separados
- [ ] desktop/mobile/zoom/reduced motion revisados
- [ ] componentes e estados extremos cobertos
- [ ] brand manifest respeitado
- [ ] aprovação humana registrada por reference_id

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_USER_APPROVAL`
- `BLOCKED_BY_BRAND_DECISION`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
