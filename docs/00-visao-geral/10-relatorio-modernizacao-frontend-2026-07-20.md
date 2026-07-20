# Relatório de modernização do frontend — W_Flyer

> Data: 2026-07-20.

## Diagnóstico

A documentação anterior estava funcionalmente correta, porém visualmente subespecificada. Ela definia sidebar, bottom navigation, tokens básicos e componentes genéricos, mas não fornecia direção suficiente para impedir que uma IA produzisse:

- dashboard SaaS genérico;
- tema padrão do shadcn/ui;
- hero roxo/azul com cards repetidos;
- wizard de upload convencional;
- excesso de cards, radius e efeitos;
- microcopy vaga sobre IA.

## Direção adotada

```text
Estúdio de transposição
+ papel de partitura
+ trajetória entre instrumentos
```

O fluxo principal foi organizado como workspace musical com superfície para arquivo/partitura e inspector contextual. Páginas públicas usam composição editorial, enquanto histórico/configurações mantêm densidade de ferramenta.

## Arquivos adicionados

- `../frontend/00-direcao-visual-wflyer.md`
- `../frontend/10-arquitetura-componentes.md`
- `../frontend/11-conteudo-microcopy.md`
- `../frontend/12-performance-qualidade-visual.md`
- `../frontend/13-storybook-governanca-ui.md`
- `../frontend/14-antipadroes-interface-ia.md`

## Arquivos significativamente revisados

- todos os documentos de `../frontend/01` a `../frontend/06` e `../frontend/09`;
- páginas 01, 02, 03, 04, 05, 06 e 08;
- stack recomendada;
- testes frontend;
- critérios de aceite;
- guia Codex;
- índice, README, referências, decisões e changelog.

## Decisões principais

1. Não usar sidebar larga de dashboard em páginas públicas.
2. Tela Transpor é workspace, não wizard genérico.
3. Design system próprio sobre primitives headless.
4. Paleta baseada em papel/tinta, violeta/cobalto com uso controlado.
5. Tokens semânticos em CSS variables/OKLCH.
6. Server Components por padrão e ilhas Client pequenas.
7. Container queries em componentes reutilizados.
8. View Transition API somente como melhoria progressiva.
9. Storybook, acessibilidade e visual regression como gates.
10. Antipadrões de interface gerada por IA documentados e bloqueantes.

## Limites

A documentação define direção e critérios, mas não substitui:

- wireframes em alta fidelidade;
- protótipo navegável;
- teste com músicos;
- auditoria visual no código implementado;
- benchmark real de bundle e Core Web Vitals.
