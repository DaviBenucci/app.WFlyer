# Arquitetura de ferramentas para agentes de IA

> Status: canônico para a Fase 0 e para toda mudança material. Revisão: 2026-07-21.

## Objetivo

Esta arquitetura reduz contexto desperdiçado sem remover informação crítica. Cada ferramenta possui uma responsabilidade exclusiva:

```text
OpenSpec   → define o que deve ser alterado e como provar a conclusão
Graphify   → identifica relações macro entre módulos, contratos, testes e documentação
Serena     → navega e altera código no nível de símbolos
Context7   → consulta documentação atual e versionada de dependências externas
Nx         → executa apenas tarefas afetadas e reutiliza resultados determinísticos
XState     → formaliza fluxos reativos complexos da interface
Storybook  → torna componentes e estados difíceis executáveis e revisáveis
Testes     → comprovam comportamento; nenhuma ferramenta de contexto substitui testes
```

## Regra de não sobreposição

- OpenSpec não substitui a documentação canônica de domínio; registra a mudança que altera essa documentação.
- Graphify não substitui leitura do código, OpenSpec, ADR, teste ou contrato.
- Serena não decide arquitetura; localiza e modifica símbolos depois do impacto ser entendido.
- Context7 não conhece o domínio do W_Flyer; serve apenas para bibliotecas externas.
- Nx não decide quais testes são suficientes; apenas organiza e executa tarefas.
- XState não deve ser usado para estados locais triviais.
- Storybook não substitui E2E nem validação musical.
- Cobertura de código não significa correção musical.

## Camadas de instalação

### Ferramentas globais do agente

Instaladas fora das dependências de produção:

- OpenSpec;
- Graphify;
- Serena;
- Context7, configurado como MCP/skill.

### Dependências do workspace JavaScript

Instaladas localmente, fixadas no `pnpm-lock.yaml`:

- Nx;
- XState;
- Storybook;
- Vitest;
- MSW;
- Playwright;
- Biome;
- Style Dictionary;
- ferramentas opcionais aprovadas por ADR.

### Dependências do workspace Python

Instaladas localmente e fixadas no `uv.lock`:

- pytest;
- Hypothesis;
- Testcontainers;
- Ruff;
- ferramentas opcionais aprovadas por ADR.

## Política de versões

1. `@latest` só pode ser usado no bootstrap inicial controlado.
2. Após o primeiro bootstrap, versões exatas e lockfiles são obrigatórios.
3. A IA não atualiza major versions no mesmo PR de uma funcionalidade.
4. Atualizações de major version exigem OpenSpec/ADR, changelog, migração e regressão.
5. Ferramenta opcional não entra no repositório antes do spike e do gate descritos em `20-ferramentas-opcionais-spikes.md`.
6. O CI usa as mesmas versões do ambiente local por meio dos lockfiles.

## Ordem de precedência para a IA

```text
contratos de domínio, segurança e acessibilidade
> OpenSpec ativo aprovado
> ADRs e documentação canônica
> código e testes atuais
> exemplo interno executável
> Graphify atualizado
> relações inferidas por ferramenta
> suposição da IA
```

## Orçamento de contexto

A IA deve recuperar contexto em camadas:

1. ler o `proposal.md`, `design.md` e `tasks.md` da mudança;
2. consultar o subgrafo relevante no Graphify;
3. localizar símbolos com Serena;
4. abrir somente contratos, implementações e testes diretamente envolvidos;
5. usar Context7 apenas para APIs externas específicas;
6. ampliar o contexto somente quando uma evidência indicar dependência adicional.

É proibido reduzir tokens omitindo:

- invariantes musicais;
- autorização e isolamento de recursos;
- estados de falha;
- critérios de aceite;
- testes impactados;
- migrations e contratos públicos.

## Matriz de adoção

| Ferramenta | Adoção | Fase | Bloqueia código? | Artefato de prova |
|---|---|---:|---:|---|
| OpenSpec | obrigatória | 0 | sim, para mudança material | mudança em `openspec/` |
| Graphify | obrigatória | 0 | sim, para impacto transversal | grafo atualizado e consulta registrada |
| Serena | instalada na Fase 0; obrigatória para código | 0/1 | sim, quando houver código analisável | MCP ativo e símbolos lidos/alterados |
| Context7 | configurado na Fase 0; usado sob demanda | 0/1 | sim, se API externa não estiver confirmada | MCP ativo e biblioteca/versão consultada |
| Nx | obrigatória no monorepo | 1 | sim | `nx affected`/targets verdes |
| XState | condicional | frontend | para fluxos complexos | máquina, eventos e testes |
| Storybook | obrigatória para UI de produto | frontend | sim | stories e estados aprovados |
| Vitest/MSW/Playwright | obrigatória | frontend | sim | testes verdes |
| pytest/Hypothesis/Testcontainers | obrigatória | backend/música | sim | testes verdes |
| Biome/Ruff | obrigatória | 1 | sim | lint/format verdes |
| Style Dictionary | obrigatória quando tokens entrarem | frontend | sim | outputs gerados e verificados |
| Temporal/Rive/Pact/Stryker/mutmut | opcional | spike | não antes do ADR | relatório de spike |

## Critério de sucesso

A arquitetura está funcionando quando a IA consegue responder, antes de editar:

- qual requisito está sendo implementado;
- quais módulos e símbolos são afetados;
- quais contratos públicos mudam;
- quais riscos e invariantes se aplicam;
- quais testes devem falhar antes e passar depois;
- qual comando executará apenas o impacto necessário;
- como reverter a mudança.
