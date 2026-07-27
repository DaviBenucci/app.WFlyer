# Requisitos — DEC-023

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Governança de dados para motores de IA**;
- fase limite: `AI-PROVIDER:entry`;
- owner: `privacy_reviewer`;
- evidências: `EVID-024`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] inventário de fornecedores
- [ ] DPA/termos avaliados
- [ ] uso para treino desabilitado por padrão
- [ ] redaction e minimização
- [ ] consentimento separado quando aplicável
- [ ] kill switch por fornecedor

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_SECURITY_REVIEW`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
