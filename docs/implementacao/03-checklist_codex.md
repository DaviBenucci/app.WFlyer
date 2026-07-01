# Checklist Codex

Antes de implementar qualquer fase:

- [ ] Li `README.md`.
- [ ] Li `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`.
- [ ] Li `W-Flyer_Regra-Transposição.md`.
- [ ] Li `docs/features/11-catalogo-instrumentos-mvp.md`.
- [ ] Li `docs/100-implementacao/guia-codex-app-wflyer.md`.
- [ ] Confirmei a fase atual.
- [ ] Confirmei que a fase anterior está concluída, testada e documentada.

Durante a implementação:

- [ ] Não implementei código fora da fase atual.
- [ ] Não criei contrato sem documentar.
- [ ] Não dupliquei regra musical.
- [ ] Não expus stacktrace.
- [ ] Não expus path físico.
- [ ] Não expus `storage_key`.
- [ ] Não coloquei processamento pesado dentro da request HTTP principal.

Antes de finalizar a fase:

- [ ] Executei testes aplicáveis.
- [ ] Registrei testes não executados e motivo.
- [ ] Atualizei documentação afetada.
- [ ] Registrei decisões novas.
- [ ] Listei pendências.
- [ ] Só marquei conclusão com evidência.
