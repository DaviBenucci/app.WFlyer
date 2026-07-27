# Manifesto de validação do repositório

Data da consolidação: 2026-07-27
Escopo: documentação, contratos estruturados, governança da IA e artefatos necessários antes da implementação funcional.

## Estado confirmado do projeto

```text
Fase 0: concluída, sincronizada e arquivada no OpenSpec
Fase 1: não iniciada
Código funcional do produto: inexistente
Frontend/API/worker/banco/motor musical: não implementados
Identidade visual oficial: pendente
Capabilities avançadas: desabilitadas
```

A presente entrega não aprova opções técnicas, musicais, comerciais, fiscais ou jurídicas que ainda dependem de evidência. Ela formaliza como essas decisões deverão ser pesquisadas, comparadas, aprovadas, implementadas e validadas.

## Inventário validado

| Métrica | Quantidade |
|---|---:|
| Arquivos relevantes do repositório | 862 |
| Documentos Markdown | 757 |
| Arquivos dentro de `docs/` | 788 |
| JSON parseados | 20 |
| YAML/YML parseados | 39 |
| Contratos JSON Schema verificados | 27 |
| Links Markdown relativos verificados | 237 |
| Decisões controladas (`DEC-*`) | 47 |
| Bundles de evidência (`EVID-*`) | 48 |
| Registros de fase/trilha | 48 |
| Lados de gate (entrada + saída) | 96 |
| Pacotes completos de decisão | 47 |
| Referências visuais registradas | 16 |
| Políticas públicas especializadas | 10 |

Esses números são uma fotografia desta consolidação e devem ser recalculados por `scripts/validate-repository.py` após qualquer alteração.

## Governança de decisões incorporada

A fonte canônica está em `docs/decision-governance/`:

```text
decision-register.yaml
→ pergunta, estado, blockers, owner, aprovadores, opções e fase limite

evidence-register.yaml
→ artefatos, origem, revisão, commit, ambiente, validade e freshness

phase-decision-gates.yaml
→ decisões e evidências mínimas para entrada e saída de cada fase

decisions/DEC-XXX-*/
→ requisitos, opções, experimento, evidências, comparação, risco,
   registro da decisão e validação pós-implementação
```

Regras verificadas:

- uma IA não pode aprovar decisão ou evidência em nome humano;
- `REJECTED` e `STALE` nunca satisfazem um requisito `ACCEPTED`;
- `SUPERSEDED` nunca satisfaz um gate ativo;
- uma decisão `DECIDED` ainda exige ADR/MDR/FDR e OpenSpec próprio antes de implementação;
- uma decisão `IMPLEMENTED` ainda exige validação para produção;
- resultados negativos, falhas e outliers não podem ser apagados;
- thresholds quantitativos devem ser definidos antes de observar o resultado;
- ferramentas opcionais possuem fases `FUTURE-*` e não bloqueiam o Core;
- `PEND-026` e `PEND-027` permanecem reservados, pois site institucional e hospedagem de clientes estão fora deste repositório.

Foram formalizadas decisões específicas para backup/restauração/DR, observabilidade/resposta a incidentes e modelo de contas/organizações, que antes apareciam apenas de forma distribuída.

## Situação dos gates neste baseline

Exemplos executados:

```text
CORE-1:entry
→ aprovado na camada de decisão

CORE-1:exit
→ bloqueado por DEC-039 e EVID-040

FUTURE-MUTATION:entry
→ bloqueado por DEC-038 e EVID-039
```

Isso é intencional. A fundação pode ser iniciada após o preflight da fase, mas não poderá ser marcada como concluída até que o typechecker Python seja comparado e aprovado. Mutation testing permanece opcional e não interfere no MVP.

## OpenSpec e fontes de orientação

A mudança documental `document-decision-governance` está arquivada e sua especificação vigente está em:

```text
openspec/specs/decision-governance/spec.md
```

Também foram atualizados:

- `AGENTS.md`;
- `README.md`;
- `TREE.md`;
- índice, roadmap e hierarquia documental;
- explicações técnica e não técnica;
- guia do Codex e critérios de aceite;
- `openspec/config.yaml`;
- ADR-053 e logs do projeto.

Nenhuma mudança OpenSpec da Fase 1 foi criada ou iniciada.

## Identidade, billing, fiscal e políticas

Continuam válidas as seguintes restrições:

- identidade oficial pendente; somente `W_Flyer` em texto;
- logo antiga removida e proibida como referência;
- preços, custos, créditos e impostos permanecem sem valores inventados;
- Stripe e Mercado Pago continuam candidatos sujeitos a spike futuro;
- billing e emissão fiscal permanecem desabilitados;
- políticas públicas continuam em rascunho pré-empresa e dependem de revisão adequada;
- site institucional e documentação empresarial privada permanecem fora do aplicativo.

## Graphify

`graphify-out/` é um artefato local regenerável e não é fonte de verdade. O validador, quando a pasta existe, confere somente sua integridade estrutural e a coerência entre `graph.json` e `GRAPH_REPORT.md`; isso não comprova frescor.

O grafo existente no ambiente de revisão ainda representa o commit anterior às alterações finais. Por isso, ele pode ser omitido do pacote distribuído e deve ser recriado no repositório real:

```bash
graphify update .
```

Depois da atualização, confirme o commit de origem e execute novamente a validação.

## Comandos de validação

Gerar novamente as visões humanas derivadas dos YAMLs:

```bash
pnpm run generate:decision-docs
```

Validar o repositório:

```bash
pnpm run verify:repository
```

Consultar gates:

```bash
python3 scripts/check-decision-gate.py CORE-1 --gate entry
python3 scripts/check-decision-gate.py CORE-1 --gate exit
```

Validar a toolchain local do agente:

```bash
pnpm run verify:agent-toolchain
```

Verificações adicionais:

```bash
python3 -m py_compile scripts/*.py
bash -n scripts/*.sh
git diff --check
```

## Limites desta validação

Esta validação não comprova:

- execução de frontend, API, worker, PostgreSQL, fila ou storage;
- parsing, normalização, transposição ou verificação MusicXML;
- OMR, extração de melodia, harmonização, engraving ou áudio;
- segurança de produção, carga, failover, restore ou disaster recovery;
- pagamentos, NFS-e ou políticas juridicamente aprovadas;
- qualidade musical avaliada por corpus e músicos;
- conexão dos MCPs no computador do usuário;
- atualização do Graphify após a aplicação desta entrega.

Essas comprovações pertencem às fases e evidências registradas.

## Passos antes da Fase 1

1. aplicar esta versão no repositório real;
2. executar `graphify update .`;
3. executar `pnpm run generate:decision-docs`;
4. executar `pnpm run verify:repository`;
5. executar `pnpm run verify:agent-toolchain`;
6. revisar `git diff --check` e o working tree;
7. criar o checkpoint/tag da Fase 0, caso ainda não existam;
8. somente mediante autorização, abrir `establish-executable-foundation`;
9. consultar `CORE-1:entry` antes de alterar código;
10. não declarar a fase concluída enquanto `CORE-1:exit` estiver bloqueado.

## Resultado

```text
Validação documental e estrutural: APROVADA
Governança de decisões: DOCUMENTADA E VERIFICADA
Decisões técnicas futuras aprovadas nesta entrega: NENHUMA
Implementação funcional iniciada: NÃO
Graphify pós-alteração: PENDENTE NA MÁQUINA DO PROJETO
Fase 1 liberada automaticamente: NÃO
```
