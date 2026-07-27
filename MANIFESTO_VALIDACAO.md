# Manifesto de validação do repositório

Data da consolidação: 2026-07-27
Escopo: arquivos versionados e novos arquivos não ignorados; exclui `.git/`, `node_modules/`, ambientes virtuais, caches, builds, uploads, segredos e o conteúdo gerado de `graphify-out/` do inventário. O grafo é validado separadamente.

## Estado do projeto

```text
Fase 0: concluída, sincronizada e arquivada no OpenSpec
Fase 1: não iniciada
Código funcional do produto: inexistente
Capabilities avançadas: desabilitadas
```

## Inventário atual

| Métrica | Quantidade |
|---|---:|
| Arquivos relevantes do repositório | 404 |
| Documentos Markdown | 307 |
| Arquivos dentro de `docs/` | 344 |
| JSON parseados fora dos artefatos gerados do Graphify | 16 |
| YAML/YML parseados | 34 |
| Contratos JSON Schema verificados | 23 |
| Referências visuais registradas | 16 |
| Links Markdown relativos verificados | 12 |

Os números são uma fotografia desta consolidação. O script deve ser executado novamente após qualquer alteração.

## Verificações aprovadas

- 44 arquivos obrigatórios presentes, incluindo as visões por público, parâmetros comerciais e políticas públicas;
- JSON e YAML sintaticamente válidos;
- 23 pares de dados/JSON Schema válidos;
- links Markdown relativos existentes;
- paths do manifesto de referências visuais existentes;
- references futuras marcadas como `status: reference` quando a capability está desabilitada;
- hook do Graphify sem caminho absoluto pessoal;
- spec `phase-zero-foundation` sincronizada;
- mudanças `bootstrap-core-foundation`, `document-business-launch-readiness` e `document-pricing-credits-policies` arquivadas e sem tarefas incompletas;
- nenhuma dependência, ambiente virtual ou cache versionado;
- `graph.json` estruturalmente íntegro;
- `GRAPH_REPORT.md` coerente com `graph.json`.

## Pacote empresarial e de lançamento

A consolidação inclui documentação nova para:

- empresa ainda não aberta, com formalização planejada para o final de agosto de 2026;
- site institucional em `wflyer.com.br`;
- aplicação futura em `app.wflyer.com.br`;
- serviços de programação e hospedagem gerenciada;
- isolamento de sites de clientes;
- comparação Stripe/Mercado Pago sem decisão final;
- ledger de créditos, webhooks e reconciliação;
- NFS-e e certificado dependentes de validação contábil/municipal;
- arquitetura AWS, banco, filas, backup, DR e runbooks.

Billing e emissão fiscal permanecem desabilitados até seus gates.

## Preços, créditos e políticas públicas

A consolidação também inclui:

- campos preenchíveis para preços, custos, planos e créditos;
- template YAML com valores monetários ainda `null` e schema de validação;
- lifecycle detalhado de cotação, reserva, consumo, liberação, expiração e estorno;
- formulário para decisão após benchmarks;
- central pública planejada em `/politicas`;
- dez políticas especializadas em estado de rascunho pré-empresa;
- manifesto de políticas com rotas, versões, vigência e gates de revisão;
- bloqueio contra publicação de política final ou catálogo comercial incompleto.

Nenhum preço, quantidade de crédito, prazo comercial, CNPJ ou texto jurídico foi inventado.

## Graphify

A fotografia presente no pacote contém:

```text
3.076 nós
2.890 relações
292 comunidades
```

`graph.json` e `GRAPH_REPORT.md` concordam entre si. Os arquivos `.graphify_health*.json` registram uma etapa intermediária anterior, com 3.043 nós e 2.858 relações; devem ser tratados como diagnóstico histórico.

O grafo foi construído a partir do commit `fdf4c158`. Como esta consolidação altera arquivos depois desse commit, o Graphify deve ser atualizado na máquina do projeto antes do checkpoint final:

```bash
graphify update .
```

## Comandos de validação

Validação portável do repositório:

```bash
pnpm run verify:repository
```

Equivalente direto:

```bash
python3 scripts/validate-repository.py
```

Validação das ferramentas instaladas na máquina do agente:

```bash
pnpm run verify:agent-toolchain
```

Verificações finais adicionais:

```bash
bash -n scripts/verify-repository.sh
bash -n scripts/verify-local-agent-toolchain.sh
bash -n scripts/verify-toolchain.sh
git diff --check
```

## Limites desta validação

Esta validação não comprova:

- frontend, API, worker, banco ou storage;
- parsing ou transposição MusicXML;
- testes unitários, integração ou E2E do produto;
- OMR, harmonização, extração de melodia ou renderização;
- conexão efetiva de Serena e Context7 no computador do usuário;
- frescor do Graphify após as correções deste pacote.

Esses itens não existem ou dependem da máquina do projeto. Não foram simulados.

## Passos antes da Fase 1

1. substituir os arquivos do repositório por esta versão corrigida;
2. executar `graphify update .`;
3. executar as duas validações;
4. revisar o diff;
5. criar o commit de consolidação;
6. criar a tag `phase-0-complete`;
7. somente depois, mediante autorização, criar a mudança OpenSpec `establish-executable-foundation`.

## Resultado

```text
Validação documental/estrutural: APROVADA
Atualização Graphify pós-correção: PENDENTE NA MÁQUINA DO PROJETO
Checkpoint Git/tag: PENDENTE
Fase 1 liberada automaticamente: NÃO
```
