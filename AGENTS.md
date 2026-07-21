## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

When the user types `/graphify`, use the installed graphify skill or instructions before doing anything else.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- Dirty graphify-out/ files are expected after hooks or incremental updates; dirty graph files are not a reason to skip graphify. Only skip graphify if the task is about stale or incorrect graph output, or the user explicitly says not to use it.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## Navegação obrigatória pelo Graphify

Antes de realizar mudanças que atravessem mais de um módulo:

1. Verifique se `graphify-out/graph.json` está atualizado.
2. Leia `graphify-out/GRAPH_REPORT.md`.
3. Consulte o grafo para identificar:
   - módulos envolvidos;
   - dependências;
   - consumidores;
   - contratos;
   - testes relacionados;
   - possíveis efeitos colaterais.
4. Abra e leia os arquivos-fonte identificados antes de alterá-los.
5. Não trate relações `INFERRED` ou `AMBIGUOUS` como fatos.
6. Confirme relações críticas diretamente no código e na documentação oficial.
7. Não utilize o grafo como substituto para testes, análise de tipos ou validação musical.
8. Após mudanças estruturais, atualize o grafo.
9. Registre divergências entre grafo, código e documentação.
10. Em caso de conflito, prevalecem:
    - contratos de domínio e segurança;
    - ADRs aprovadas;
    - código e testes atuais;
    - grafo atualizado;
    - inferências da IA.
