# Requisitos — DEC-005

> Estado: `DRAFT`. Este documento congela o que será avaliado; não registra escolha.

## Resultado esperado

Responder à pergunta de [`00-decision-brief.md`](00-decision-brief.md) com evidência suficiente para uma aprovação humana reproduzível.

## Escopo

- decisão: **Suporte a MusicXML comprimido (.mxl)**;
- fase limite: `FUTURE-MXL:entry`;
- owner: `security_lead`;
- evidências: `EVID-006`.

## Fora do escopo

- implementar a opção vencedora;
- habilitar feature flag;
- preencher preço, threshold, licença ou dado legal sem fonte;
- alterar requisito após observar o benchmark sem registrar nova versão.

## Restrições e critérios

- [ ] corpus hostil aprovado
- [ ] limites de entries e tamanho descompactado definidos
- [ ] paths normalizados sem escape
- [ ] recursos referenciados validados
- [ ] telemetria e erro público definidos

## Bloqueadores que precisam ser resolvidos

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_BENCHMARK`

## Aprovação de requisitos

- [ ] owner confirmou pergunta e escopo;
- [ ] aprovadores confirmaram critérios antes do experimento;
- [ ] corpus/dados/licenças foram aprovados quando aplicável;
- [ ] riscos de segurança, privacidade, música, custo e operação foram incluídos.
