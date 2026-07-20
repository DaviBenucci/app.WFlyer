# Anotações, revisão e aprovação musical

> Status: canônico para colaboração futura. Revisão: 2026-07-20.

## Objetivo

Permitir comentários e decisões ancorados na música, sem alterar silenciosamente o artefato canônico.

## Tipos

```text
COMMENT
QUESTION
CORRECTION_REQUEST
APPROVAL
REJECTION
PERFORMANCE_MARK
PRIVATE_NOTE
```

## Âncoras

Preferência:

```text
event_id
measure_id + beat
phrase_id
part_id + measure_id
page geometry somente como fallback
```

Uma anotação visual deve tentar remapear após nova renderização; se não houver correspondência segura, fica marcada como órfã e exige revisão.

## Fluxo

- criar comentário em revisão específica;
- responder/resolver;
- converter correção em alteração tipada;
- gerar nova versão;
- preservar discussão anterior;
- registrar aprovação por papel de revisor.

## Regras

- aprovação é vinculada ao hash/version_id;
- nova versão invalida aprovação anterior até revalidação;
- comentário não concede acesso ao artefato além do escopo;
- conteúdo de comentário é dado não confiável;
- excluir comentário segue política de auditoria e privacidade;
- usuários anônimos não recebem colaboração pública no Core.
