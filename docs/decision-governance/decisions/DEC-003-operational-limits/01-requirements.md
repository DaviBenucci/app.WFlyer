# Requisitos — DEC-003

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Limites operacionais por formato e operação**;
- fase limite: `CORE-4:exit`;
- owner: `platform_lead`;
- evidências: `EVID-004`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] benchmark com cenários inicial, provável e pico
- [ ] limites definidos antes de produção
- [ ] rejeição segura e mensagem pública específica
- [ ] timeouts e quotas testados
- [ ] custo p95 conhecido para operações comerciais

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
