# Checklist de regressão

## Escopo e contrato

- [ ] Mudança está dentro do Core ou sob feature gate?
- [ ] Documento canônico/ADR foi atualizado?
- [ ] OpenAPI e cliente gerado estão sincronizados?
- [ ] Enum/erro/capability não foi inventado localmente?

## Música

- [ ] Invariante de altura de concerto passa?
- [ ] Grafia diatônica e oitava foram testadas?
- [ ] Ritmo/vozes/ties/tuplets permanecem?
- [ ] `<transpose>` não foi aplicado duas vezes?
- [ ] Corpus/golden afetado foi revisado conscientemente?

## Segurança

- [ ] Autorização por sessão em todo objeto?
- [ ] CSRF em mutações?
- [ ] Parser/arquivo permanece restritivo?
- [ ] Sem token/path/storage key/stderr em resposta ou log?
- [ ] Rate/size/resource limits preservados?
- [ ] Saída e download são revalidados?

## Assíncrono/storage

- [ ] Reentrega/retry é idempotente?
- [ ] Estado/stage/retenção não foram misturados?
- [ ] Crash/cancelamento não publica parcial?
- [ ] Expiração/purge/reconciliação continuam corretos?

## Frontend

- [ ] Capabilities governam formatos?
- [ ] Loading/network/domain/warning/terminal tratados?
- [ ] Teclado, mobile, zoom e reduced motion?
- [ ] Histórico local não virou autorização?

## Evidência

- [ ] Unit/property/integration aplicáveis executados?
- [ ] E2E afetado executado?
- [ ] Corpus hostil executado quando parser/engine mudou?
- [ ] Performance executada quando limite/engine mudou?
- [ ] Comandos/resultados registrados no TEST_LOG?
- [ ] Testes não executados têm justificativa e risco?
