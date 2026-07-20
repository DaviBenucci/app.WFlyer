# Estado local, cache e sessão

## Sessão

- cookie `wf_session` é `HttpOnly` e não é lido pelo JavaScript;
- cliente usa `credentials: include`;
- `csrf_token` retornado pelo bootstrap fica somente em memória;
- após refresh, chamar novamente o endpoint de sessão para obter CSRF válido;
- não colocar token em localStorage, IndexedDB, URL, log ou ferramenta de analytics.

## Preferências visuais

Pode persistir somente valores não sensíveis e versionados:

```text
reduced_motion_override
theme, somente quando o tema estiver integralmente suportado
instrumentos padrão
formato de saída preferido
```

Preferência inválida ou de versão antiga volta ao padrão seguro.

## Estado remoto

Usar cache de requisições para:

```text
capabilities
instrumentos
job/status
artefatos
```

- dados sensíveis não são persistidos por padrão;
- status de job respeita `Retry-After` e estados terminais;
- invalidação ocorre após criar/cancelar/apagar;
- erro de rede não inventa estado do servidor.

## Histórico local

Pode persistir somente metadados descritos em `../features/07-historico-local.md`. O histórico não é autorização.

## Service worker/PWA

PWA/offline completo não faz parte do Core. Se houver service worker técnico:

- nunca cachear respostas de sessão, upload, job privado ou download;
- respeitar `Cache-Control: no-store`;
- não oferecer transposição offline;
- não manter artefatos após purge/expiração.

## Limpeza

A UI oferece:

- limpar preferências/histórico local;
- apagar recurso no servidor via ação separada e CSRF.

Falha do storage local não bloqueia a transposição.
