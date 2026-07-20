# Colaboração, concorrência e conflitos

> Status: canônico para colaboração futura. Revisão: 2026-07-20.

## Modelo

Colaboração usa revisões otimistas e eventos, não edição simultânea irrestrita do mesmo MusicXML bruto.

## Recursos

```text
review_sessions
review_participants
annotations
change_requests
approvals
presence_ephemeral
```

## Conflitos

- comentários independentes podem coexistir;
- duas mudanças no mesmo evento/região exigem conflito;
- mudança de layout e comentário podem ser rebaseados se âncora semântica persistir;
- aprovação é invalidada por qualquer mudança dentro do escopo;
- presença nunca é fonte de verdade.

## Segurança

Convite usa token curto/escopado/revogável; acesso é verificado em cada request. Não expor lista pública de obras ou reviewers.
