# OpenSpec — governança de especificações e mudanças

> Status: obrigatório para toda mudança material.

## Responsabilidade

OpenSpec mantém o acordo entre produto, documentação, código e agente. Ele evita que o histórico do chat seja a única fonte da intenção.

## Instalação

```bash
pnpm add -g @fission-ai/openspec@latest
openspec --version
openspec init
```

O OpenSpec exige Node.js 20.19 ou superior. A pasta `openspec/` deve ser versionada como código.

## Estrutura esperada

```text
openspec/
├── specs/                 # comportamento vigente
├── changes/               # mudanças ativas
│   └── add-musical-diff/
│       ├── proposal.md
│       ├── design.md
│       ├── tasks.md
│       └── specs/
└── archive/               # mudanças concluídas conforme workflow adotado
```

A estrutura exata gerada pelo CLI prevalece sobre este desenho ilustrativo.

## Quando é obrigatório

Criar mudança OpenSpec para:

- funcionalidade nova;
- alteração de contrato público;
- migration;
- mudança de regra musical;
- mudança de estado XState;
- dependência nova;
- alteração de segurança/autorização;
- alteração do pipeline assíncrono;
- modificação visual estrutural;
- correção de incidente que altera regra ou gate.

Pode ser dispensado apenas para correção mecânica sem mudança comportamental, como typo ou formatação, desde que o diff prove isso.

## Conteúdo mínimo

### `proposal.md`

- problema;
- objetivo e não objetivos;
- usuário/capability afetada;
- risco de não fazer;
- escopo explícito.

### `design.md`

- arquitetura atual;
- opções consideradas;
- decisão e justificativa;
- módulos/símbolos impactados;
- contratos, dados e migrations;
- falhas e rollback;
- telemetria;
- compatibilidade.

### `tasks.md`

Cada item deve ser verificável e pequeno:

```text
- [ ] adicionar contrato e teste que falha
- [ ] implementar domínio
- [ ] implementar adapter
- [ ] integrar frontend
- [ ] executar gates afetados
- [ ] atualizar documentação e Graphify
- [ ] registrar evidências
```

## Fluxo obrigatório da IA

```text
1. selecionar a mudança ativa;
2. ler proposal/design/tasks e specs relacionadas;
3. validar conflito com docs canônicas;
4. consultar Graphify;
5. localizar símbolos com Serena;
6. implementar a próxima tarefa incompleta;
7. executar testes afetados;
8. atualizar tasks.md com evidência real;
9. arquivar somente após Definition of Done.
```

## Regras

- a IA não marca tarefa como concluída antes de executar a evidência;
- mudança não pode conter requisitos contraditórios sem decisão humana;
- specs novas não podem reduzir gate musical ou segurança silenciosamente;
- uma mudança ativa deve ser nomeada de forma estável no prompt;
- alterações paralelas com sobreposição exigem resolução explícita;
- OpenSpec não faz commit, branch, push ou merge; isso permanece responsabilidade do fluxo Git.

## Atualização

```bash
pnpm update -g @fission-ai/openspec
openspec update
```

Revisar todos os arquivos gerados antes de commit. Major upgrade exige ADR e regressão do fluxo de agente.

## Verificação

- comando do agente/OpenSpec aparece no cliente escolhido;
- existe uma mudança de teste criada e lida pelo agente;
- `tasks.md` permite retomar exatamente do ponto anterior;
- os arquivos estão no Git;
- nenhum segredo está em `openspec/`.

## Fonte oficial

- <https://openspec.dev/docs/overview>
- <https://openspec.dev/docs/installation>
- <https://openspec.dev/docs/the-workflow>
- <https://openspec.dev/docs/team-workflow>
