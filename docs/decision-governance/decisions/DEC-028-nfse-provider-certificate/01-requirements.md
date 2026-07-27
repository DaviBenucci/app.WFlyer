# Requisitos — DEC-028

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Emissor de NFS-e, autenticação e certificado**;
- fase limite: `F1:exit`;
- owner: `fiscal_lead`;
- evidências: `EVID-029`, `EVID-026`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] município/regime/código de serviço confirmados
- [ ] homologação de emissão/consulta/cancelamento
- [ ] certificado e segredo protegidos
- [ ] contingência e reconciliação
- [ ] aprovação formal do contador

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_SANDBOX`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
