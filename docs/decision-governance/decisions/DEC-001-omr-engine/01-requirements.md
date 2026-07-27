# Requisitos — DEC-001

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Engine OMR de produção**;
- fase limite: `P0:exit`;
- owner: `engineering_lead`;
- evidências: `EVID-001`, `EVID-002`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] corpus representativo e licenciado aprovado antes do teste
- [ ] métricas de notas, ritmos, acidentes, armaduras e vozes pré-registradas
- [ ] zero publicação automática de falso resultado verificado no corpus congelado
- [ ] execução automatizável em sandbox sem rede
- [ ] licença e obrigações de distribuição aprovadas
- [ ] custo e latência dentro de campos aprovados, ainda PENDENTE

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_LICENSE_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
