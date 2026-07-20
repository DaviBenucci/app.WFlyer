# Página de revisão colaborativa

> Status: canônico para colaboração futura. Revisão: 2026-07-20.

## Rota

```text
/revisoes/{review_session_id}
```

## Objetivo

Centralizar comentários, decisões, mudanças solicitadas e aprovação vinculada a uma versão.

## Composição

```text
ReviewHeader
ScoreWithAnnotations
ThreadPanel
ChangeRequests
ApprovalStatus
```

## Regras

- acesso por convite escopado;
- comentário ancorado semanticamente;
- edição musical cria change request tipado;
- aprovação mostra hash/version;
- nova versão exige rebase/reaprovação;
- presença em tempo real é opcional e não bloqueia fluxo.
