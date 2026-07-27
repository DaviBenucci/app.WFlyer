# Requisitos — DEC-045

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Backup, restore e recuperação de desastre**;
- fase limite: `INF3:exit;
- owner: `platform_lead`;
- evidências: `EVID-046`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] inventário de dados e dependências aprovado
- [ ] restore real de PostgreSQL executado e cronometrado
- [ ] restore de objetos, hashes e manifests executado e validado
- [ ] procedimento regional reproduzível por IaC e runbook
- [ ] RPO/RTO observados comparados às metas DEC-031
- [ ] custos, retenção, criptografia e owner aprovados

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_COST_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
