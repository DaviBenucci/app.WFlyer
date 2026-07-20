# Checklist para IA/Codex

## Antes

- [ ] Li hierarquia, escopo, matriz e decisões pendentes.
- [ ] Li o documento musical/backend/security/QA específico.
- [ ] Em tarefa de frontend, li direção visual, design system, arquitetura e antipadrões.
- [ ] Confirmei fase e evidência do gate anterior.
- [ ] Inspecionei código, migrations, OpenAPI e testes atuais.
- [ ] Listei arquivos, riscos e comandos de validação.
- [ ] Verifiquei que a tarefa não depende de capability desabilitada.

## Durante

- [ ] Não criei contrato/enum/erro sem atualizar a fonte canônica.
- [ ] Não dupliquei regra musical no frontend.
- [ ] Não copiei tema/composição padrão de biblioteca como resultado final.
- [ ] Mantive shells, tokens semânticos e componentes do domínio.
- [ ] Mantive modelo diatônico/cromático/oitava.
- [ ] Mantive sessão/CSRF/autorização por objeto.
- [ ] Mantive processamento pesado no worker.
- [ ] Tratei reentrega/idempotência/estado inválido.
- [ ] Não expus token/path/`storage_key`/stacktrace/stderr.
- [ ] Adicionei teste que falharia antes da correção.

## Antes de concluir

- [ ] Executei testes aplicáveis e registrei comandos.
- [ ] Testei cenário feliz, erro, autorização e regressão musical afetada.
- [ ] OpenAPI/cliente/migrations/docs estão sincronizados.
- [ ] Golden/snapshot alterado foi revisado, não aceito cegamente.
- [ ] Storybook, visual regression, conteúdo extremo e acessibilidade foram executados quando aplicáveis.
- [ ] Registrei testes não executados e risco.
- [ ] Provei o gate; caso contrário, marquei `BLOQUEADA`.
