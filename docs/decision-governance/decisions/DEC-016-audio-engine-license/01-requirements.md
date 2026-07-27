# Requisitos — DEC-016

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Engine, samples e licenças de áudio**;
- fase limite: `A0:exit`;
- owner: `audio_lead`;
- evidências: `EVID-017`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] licença de distribuição aprovada
- [ ] normalização de loudness
- [ ] latência e render offline medidos
- [ ] fallback definido
- [ ] sem dependência de rede nos testes

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_LICENSE_REVIEW`
- `BLOCKED_BY_BENCHMARK`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
