# Requisitos — DEC-040

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Cache remoto Nx e política de segurança**;
- fase limite: `FUTURE-NX-CACHE:entry`;
- owner: `platform_lead`;
- evidências: `EVID-041`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] classificação de outputs
- [ ] segredos excluídos
- [ ] custos/ganho medidos
- [ ] controle de acesso e retenção
- [ ] fallback local

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_IMPLEMENTATION`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
