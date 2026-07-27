# AGENTS.md — contrato operacional do W_Flyer

## Estado atual

- Fase 0: concluída e arquivada.
- Fase 1: não iniciada.
- Código funcional do produto: inexistente.
- Próxima mudança recomendada: `establish-executable-foundation`.

Não avance para uma fase ou capability sem mudança OpenSpec, gate explícito e autorização do usuário.

## Ordem obrigatória de trabalho

1. Identifique ou crie uma mudança OpenSpec.
2. Leia apenas os documentos de bootstrap e os artefatos da mudança.
3. Consulte Graphify antes de mudanças transversais.
4. Use Serena para localizar e editar símbolos quando houver código analisável.
5. Use Context7 apenas para dependências externas e para a versão realmente instalada.
6. Produza plano, riscos, rollback, critérios de aceite e testes antes do código.
7. Implemente o menor corte vertical coerente da fase atual.
8. Execute os gates aplicáveis.
9. Atualize OpenSpec, documentação, logs e Graphify.
10. Pare ao concluir a fase; não avance automaticamente.

## Recuperação de contexto e economia de tokens

Use esta sequência:

```text
proposal/design/tasks da mudança
→ Graphify query/path/explain
→ símbolos Serena
→ contratos e testes diretamente relacionados
→ documentação externa específica via Context7
```

Não leia o repositório inteiro para “garantir contexto”. Amplie a leitura somente quando uma evidência concreta indicar dependência adicional.

A economia de tokens nunca autoriza omitir:

- invariantes musicais;
- autorização e isolamento de recursos;
- estados de falha;
- migrations e contratos públicos;
- rollback;
- critérios de aceite;
- testes impactados;
- proveniência e níveis de garantia.

## Graphify

O grafo fica em `graphify-out/` e é um índice derivado.

- Para perguntas sobre o projeto, prefira `graphify query "<pergunta>"`.
- Use `graphify path "<A>" "<B>"` para relações.
- Use `graphify explain "<conceito>"` para foco local.
- Leia `GRAPH_REPORT.md` somente para revisão ampla.
- Relações `INFERRED` ou `AMBIGUOUS` não são fatos.
- Confirme decisões críticas nos documentos canônicos e no código.
- Após alteração estrutural, execute `graphify update .`.
- Se o commit do grafo divergir do `HEAD`, trate o grafo como desatualizado.

## Serena

- Ative a raiz Git como projeto.
- Quando `apps/web` e o workspace Python forem criados, atualize `.serena/project.yml` para incluir `typescript` e `python`.
- Use buscas por símbolo e referências antes de abrir arquivos extensos.
- Não use Serena para substituir leitura de contrato, teste ou especificação.

## Context7

- Use somente para documentação de bibliotecas externas.
- Informe a biblioteca e a versão instalada.
- Não use Context7 para descobrir requisitos do W_Flyer.
- Confirme decisões críticas em documentação primária da dependência.

## Precedência normativa

Em caso de conflito:

1. escopo e matriz de suporte;
2. ADRs aprovadas;
3. modelo musical e contratos de domínio;
4. API, dados e máquinas de estado;
5. segurança e privacidade;
6. critérios de aceite e QA;
7. design system e acessibilidade;
8. OpenSpec da mudança aprovada;
9. código e testes da fase atual;
10. Graphify e inferências do agente.

Ao encontrar contradição, pare e corrija a fonte canônica antes de implementar.

## Regras musicais rígidas

- O backend Python é a única fonte da regra musical.
- Transposição, extração de melodia, adaptação e harmonização são operações distintas.
- O transformador não valida a própria saída.
- Ambiguidade material falha fechado ou solicita revisão.
- Nenhum evento pode desaparecer, surgir ou mudar sem contrato e proveniência.
- Resultados criativos não recebem o mesmo selo de transformação determinística.
- O frontend não recalcula teoria musical nem infere correspondências por geometria.

## Regras de frontend

- Leia `docs/design-reference/reference-manifest.yaml` antes de implementar uma tela.
- Referências com `status: reference` são futuras e não autorizam implementação.
- Capabilities desabilitadas não aparecem como ações disponíveis.
- Não invente dashboard, cards, glows, métricas, depoimentos ou microcopy.
- Use tokens e componentes de produto; não entregue o tema padrão de uma biblioteca.
- Atualização de golden file exige revisão humana aplicável.

## Proibições

- Não inventar contrato, endpoint, estado, migration ou regra musical.
- Não instalar ferramenta opcional sem spike e ADR.
- Não usar `sudo` ou alterar o sistema sem autorização.
- Não inserir segredos, chaves ou caminhos absolutos pessoais em arquivos versionados.
- Não editar artefato gerado quando houver gerador.
- Não silenciar lint, typecheck ou teste.
- Não criar stub que faça uma fase parecer concluída.
- Não declarar conclusão sem comandos, resultados e evidências.

## Gates mínimos

Na Fase 1, o ciclo rápido deverá convergir para:

```bash
pnpm nx affected -t lint typecheck test
uv run ruff check .
uv run ruff format --check .
uv run pytest
```

Amplie conforme risco: integração real, contratos, property tests, golden files, segurança, E2E, visual, acessibilidade, carga e mutation testing.

## Definition of Done do agente

Uma tarefa só termina quando o relatório registra:

- requisito e mudança OpenSpec;
- arquivos e símbolos afetados;
- decisões tomadas e pendências preservadas;
- comandos executados;
- resultados dos testes;
- riscos residuais;
- rollback;
- documentação e Graphify atualizados;
- confirmação de que a próxima fase não foi iniciada.
