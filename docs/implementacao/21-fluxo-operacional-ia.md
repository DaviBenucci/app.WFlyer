# Fluxo operacional obrigatório da IA

> Status: canônico. Aplicável a Codex e qualquer outro agente com acesso ao projeto.

## Fluxo principal

```text
1. identificar a mudança OpenSpec
2. ler requisitos, riscos, ADRs e gates
3. verificar Graphify atualizado
4. consultar impacto macro
5. ativar Serena e localizar símbolos
6. consultar Context7 apenas para dependências externas
7. escrever plano pequeno e verificável
8. criar/ajustar teste que demonstra o requisito
9. implementar o menor corte completo
10. executar Nx affected
11. ampliar testes conforme risco
12. atualizar docs, OpenSpec, logs e grafo
13. revisar diff e rollback
14. só então declarar conclusão
```

## Prompt-base para a IA

```text
Trabalhe exclusivamente na mudança OpenSpec <ID>.

Antes de editar:
1. leia proposal.md, design.md, tasks.md e specs afetadas;
2. consulte Graphify com orçamento inicial de 1200 tokens;
3. confirme as relações críticas com Serena no nível de símbolos;
4. consulte Context7 apenas para APIs externas cuja versão esteja no lockfile;
5. liste invariantes, riscos, contratos e testes afetados;
6. proponha o menor corte vertical.

Durante a implementação:
- não invente requisito, endpoint, migration ou estado;
- não degrade gate musical, segurança ou acessibilidade;
- crie teste que falhe pelo motivo esperado antes da correção;
- use Nx affected para o ciclo rápido;
- pare em decisão pendente.

Ao finalizar:
- execute os gates aplicáveis;
- registre comandos e resultados;
- atualize tasks.md, documentação e Graphify;
- informe testes não executados e riscos residuais;
- não use “concluído” sem evidência.
```

## Classificação da mudança

A IA deve classificar:

- local: um package, sem contrato público;
- transversal: múltiplos packages/apps;
- persistência: schema/migration;
- musical determinística;
- musical inferencial/criativa;
- segurança/autorização;
- visual/interação;
- infraestrutura/workflow.

A classificação determina leitura e gates.

## Ciclo de contexto econômico

### Primeira passada

- OpenSpec ativo;
- índice do Graphify;
- 3 a 8 símbolos Serena;
- contratos/testes diretamente ligados.

### Expansão permitida

Abrir mais contexto somente quando:

- existe consumidor não mapeado;
- tipo público muda;
- teste revela efeito colateral;
- Graphify marca relação ambígua;
- Serena encontra herança/referência adicional;
- Context7 aponta breaking change.

### Expansão proibida

- ler todo o monorepo “para garantir”;
- anexar relatórios completos sem relação;
- consultar Context7 para conceitos internos;
- repetir arquivos já resumidos sem mudança;
- carregar baselines binários sem necessidade visual.

## Antes de editar

Checklist:

- [ ] diretório e branch corretos;
- [ ] working tree compreendida;
- [ ] mudança OpenSpec selecionada;
- [ ] grafo atualizado;
- [ ] projeto Serena ativo;
- [ ] versões de dependências confirmadas;
- [ ] teste de regressão definido;
- [ ] rollback identificado.

## Durante a edição

- alterar um conceito por vez;
- manter contratos e implementações sincronizados;
- não editar outputs gerados;
- executar geradores oficiais;
- evitar refatoração não relacionada;
- não “corrigir” golden files sem provar que a nova saída é correta;
- não silenciar lint/teste para obter verde.

## Após a edição

```bash
pnpm nx affected -t lint typecheck test
```

E, conforme risco:

```text
component/browser
integration/Testcontainers
contract
property/metamorphic
golden/semantic
security
Playwright/visual/accessibility
mutation
corpus completo
```

## Relatório final obrigatório

- mudança executada;
- arquivos e símbolos alterados;
- decisão técnica;
- testes/comandos e resultado;
- cache hits relevantes;
- migrations/contratos;
- screenshots/evidências;
- Graphify atualizado ou motivo;
- riscos residuais;
- próximos itens de `tasks.md`.
