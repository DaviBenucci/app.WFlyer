# Definition of Done

Uma tarefa/fase só está concluída quando:

- [ ] comportamento atende escopo e matriz;
- [ ] código de produção, migrations e contratos estão completos;
- [ ] autorização, validação, erro e observabilidade foram tratados;
- [ ] regra musical/invariantes afetados possuem testes;
- [ ] happy path, bordas e falhas relevantes foram executados;
- [ ] lint/typecheck/unit/integration/contract/E2E aplicáveis passam;
- [ ] corpus hostil roda quando parser/arquivo/engine mudou;
- [ ] performance roda quando limite, engine, bundle ou componente pesado mudou;
- [ ] frontend alterado possui stories/estados, acessibilidade e visual regression aplicáveis;
- [ ] motion alterado possui reduced motion, cleanup, interrupção, fallback e medição de bundle/runtime;
- [ ] implementação visual não mantém tema padrão de biblioteca nem antipadrão bloqueante;
- [ ] documentação canônica e logs foram atualizados;
- [ ] nenhuma capability futura foi habilitada implicitamente;
- [ ] testes não executados e riscos estão explícitos;
- [ ] gate da fase possui evidência reproduzível.

Código compilando ou uma demonstração manual não satisfaz o DoD isoladamente.
