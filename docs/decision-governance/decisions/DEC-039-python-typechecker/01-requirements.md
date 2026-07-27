# Requisitos — DEC-039

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Typechecker Python definitivo**;
- fase limite: `CORE-1:exit`;
- owner: `backend_lead`;
- evidências: `EVID-040`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] spike no scaffold real
- [ ] compatibilidade FastAPI/SQLAlchemy/pacotes internos
- [ ] tempo de execução
- [ ] baseline sem suppressions genéricas
- [ ] versão fixada

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
