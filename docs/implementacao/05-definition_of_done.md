# Definition of Done

Uma tarefa/fase só está concluída quando:

- [ ] comportamento atende escopo e matriz;
- [ ] DGATE-* aplicável foi atendido e DEC-*/EVID-* foram atualizados;
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

## Definition of Done — operação musical avançada

- operação explícita e documentada;
- evento de saída com provenance;
- hard constraints automatizadas;
- verificador independente;
- ambiguidade bloqueia ou abre review;
- versões/seed/manifest persistidos;
- corpus congelado e evidência registrada;
- capability desligável e rollback testado;
- músico responsável aprovou o gate aplicável;
- microcopy não promete certeza indevida.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Definition of Done — visão crítica

Uma entrega só está pronta quando:

- requisitos e riscos possuem rastreabilidade;
- happy path e falhas conhecidas aplicáveis foram testados;
- falha desconhecida possui comportamento seguro;
- UI possui todos os estados e golden review;
- transformação possui event mapping/provenance;
- `UNKNOWN` não foi convertido em sucesso;
- engine/model/policy versions estão no manifesto;
- capability flag, rollback e observabilidade foram testados;
- revisão musical/segurança/acessibilidade aplicáveis aprovaram;
- documentação, changelog e matriz pre-mortem foram atualizados.

## DoD de visão crítica e pre-mortem

Uma capability não está concluída enquanto:

- preflight não estiver aprovado;
- todo `PM-*` aplicável não estiver implementado/evidenciado ou explicitamente aceito;
- falhas desconhecidas não falharem fechadas;
- fault injection não cobrir boundaries relevantes;
- Musical Diff/provenance não cobrir alterações aplicáveis;
- referência visual e todos os estados não estiverem implementados;
- baseline não tiver revisão humana;
- métricas não estiverem estratificadas por instrumento/textura/formato;
- feature flag, rollout e rollback não estiverem testados;
- decisões musicais não estiverem em MDR;
- documentação, changelog, OpenAPI e matriz de rastreabilidade não estiverem sincronizados.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Definition of Done da toolchain

Uma mudança material não está concluída sem:

- OpenSpec atualizado e tarefas com evidência;
- decisão aprovada não foi confundida com validação pós-implementação;
- impacto Graphify revisado e grafo atualizado se estrutural;
- símbolos/consumidores conferidos;
- dependências externas usadas conforme versão instalada;
- `Nx affected` verde;
- lint, format e typecheck verdes;
- testes unitários e camadas adicionais aplicáveis;
- Storybook/visual/acessibilidade para UI;
- property/golden/segurança para domínio musical;
- nenhuma ferramenta opcional adicionada sem ADR;
- comandos, ambiente, cache e falhas registrados.
