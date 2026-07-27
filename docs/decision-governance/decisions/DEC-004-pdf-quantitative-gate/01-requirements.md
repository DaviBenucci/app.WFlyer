# Requisitos — DEC-004

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Gate quantitativo para PDF/OMR**;
- fase limite: `P2:exit`;
- owner: `qa_lead`;
- evidências: `EVID-005`, `EVID-001`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] thresholds registrados antes de observar o benchmark final
- [ ] resultados estratificados por formato e complexidade
- [ ] verified_false_positive_rate alvo preenchido e aprovado
- [ ] taxa de revisão e rejeição explicitamente aceita
- [ ] rollout e kill switch definidos

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
