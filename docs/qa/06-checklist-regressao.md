# Checklist de regressão

Antes de concluir uma tarefa, o Codex deve verificar:

## Produto

- [ ] O comportamento implementado está documentado?
- [ ] A rota está correta?
- [ ] MVP e futuro não foram misturados indevidamente?

## Frontend

- [ ] Estados loading/error/empty existem?
- [ ] Acessibilidade básica foi mantida?
- [ ] Reduced motion respeitado?
- [ ] Mobile não ficou quebrado?

## Backend

- [ ] Endpoint tem validação?
- [ ] Erro público é seguro?
- [ ] Não há processamento pesado na request?
- [ ] Status de job é terminal em falhas?

## Segurança

- [ ] Não há token em log?
- [ ] Não há path interno em resposta pública?
- [ ] Upload é validado no backend?
- [ ] Download valida autorização?

## Testes

- [ ] Unitários rodaram?
- [ ] Typecheck/lint rodaram?
- [ ] E2E afetado rodou?
- [ ] Resultado registrado em `docs/logs/TEST_LOG.md`?

## Documentação

- [ ] `docs/logs/IMPLEMENTATION_LOG.md` atualizado?
- [ ] `docs/logs/CHANGELOG.md` atualizado se comportamento mudou?
- [ ] `docs/logs/DECISIONS.md` atualizado se houve decisão nova?
