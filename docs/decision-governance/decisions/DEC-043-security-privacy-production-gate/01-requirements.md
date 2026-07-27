# Requisitos — DEC-043

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Gate de segurança e privacidade para produção**;
- fase limite: `LAUNCH:entry`;
- owner: `security_lead`;
- evidências: `EVID-044`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] inventário/fluxo de dados
- [ ] threat model atualizado
- [ ] IDOR/CSRF/upload hostil/dependências
- [ ] pentest ou revisão independente aplicável
- [ ] restore e incident runbooks exercitados
- [ ] riscos críticos com owner/evidência

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
