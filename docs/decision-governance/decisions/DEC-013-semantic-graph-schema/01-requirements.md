# Requisitos — DEC-013

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Schema final do grafo semântico musical**;
- fase limite: `M0:exit`;
- owner: `music_engineering_lead`;
- evidências: `EVID-014`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] round trip do perfil suportado
- [ ] IDs estáveis entre serializações equivalentes
- [ ] cross-staff/grace/cue/ossia com política explícita
- [ ] versionamento e migração do schema
- [ ] nenhum dado canônico perdido

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
