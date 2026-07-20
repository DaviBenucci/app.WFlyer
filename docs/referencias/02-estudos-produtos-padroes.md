# Estudos de produtos e padrões de interface

> Status: referência não normativa. Revisão: 2026-07-20.

## Regra

Produtos externos são estudados por padrão de interação, não copiados. Qualquer conclusão útil deve virar specification, protótipo ou story própria do W_Flyer antes da implementação.

## Dimensões de estudo

| Categoria | Pergunta | Aplicação possível |
|---|---|---|
| ferramentas de alta densidade | como manter hierarquia e velocidade sem card soup? | StudioShell e navegação por teclado |
| design systems | como tokens, foco e contraste são governados? | foundations e primitives |
| editores de notação | como selecionar evento, navegar por compasso e revisar mudanças? | ScoreSurface e Musical Diff |
| prática/ensino | como partitura, áudio, loop e andamento permanecem sincronizados? | modo de ensaio |
| performance | como reduzir distração, virar página e anotar? | RehearsalShell |
| colaboração | como comentário, versão e conflito aparecem? | revisão colaborativa |
| engraving profissional | como score, partes, page turns e legibilidade são avaliados? | gate de renderização |

## Ficha obrigatória

Cada estudo em `../design-reference/external-studies/` deve registrar:

```text
produto e data observada
problema estudado
padrão observado
por que é relevante
riscos de cópia/inadequação
adaptação original proposta
reference_id interno resultante
```

## Proibições

- armazenar screenshot/asset sem direito;
- reproduzir logo, paleta ou composição integral;
- copiar código inspecionado;
- citar produto externo como requisito de implementação;
- misturar padrões incompatíveis sem uma decisão interna.
