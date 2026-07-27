# Requisitos — DEC-011

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Infraestrutura de assinatura e verificação**;
- fase limite: `W2:exit`;
- owner: `security_lead`;
- evidências: `EVID-012`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] algoritmo e cadeia aprovados
- [ ] chaves nunca exportadas para aplicação
- [ ] rotação e revogação testadas
- [ ] endpoint de verificação definido
- [ ] política pós-purge explícita

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
