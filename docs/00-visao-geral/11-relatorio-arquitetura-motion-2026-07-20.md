# Relatório de arquitetura de motion — W_Flyer

> Data: 2026-07-20.

## Objetivo

Amadurecer o uso de animações no frontend, selecionar bibliotecas sem sobreposição e transformar a ideia de tinta musical saindo de uma partitura e formando outra em uma especificação implementável, acessível e testável.

## Decisão

```text
CSS nativo
  microestados simples

Motion for React
  presença, layout, gestos e transições ligadas ao estado React

GSAP + @gsap/react
  cena SVG Ink Transfer e timelines isoladas
```

Anime.js e React Spring foram avaliados, mas não entram no MVP Core. Ambos possuem capacidades válidas; sua inclusão simultânea duplicaria o papel já coberto por Motion e GSAP.

## Cena Ink Transfer

A entrada pública passa a prever uma cena integrada ao hero:

1. a pauta de origem é desenhada;
2. 4–6 glifos musicais aparecem;
3. cópias de tinta percorrem curvas entre origem e destino;
4. a pauta de destino é revelada;
5. os glifos são recompostos em uma transformação musical fixa e validada;
6. a rota textual apresenta instrumento original, intervalo e destino.

A cena não é splash screen, não bloqueia CTA, dura menos de dois segundos, toca no máximo uma vez por sessão e possui fallback estático/reduced motion.

## Limite técnico importante

No MVP, a cena usa SVG autoral e não anima as notas reais do arquivo enviado. A evolução para dados reais depende de IDs musicais estáveis e de um `NoteGeometryMap` emitido pelo adapter de renderização. É proibido inferir semântica pela estrutura visual interna de um renderer de terceiros.

## Documentos adicionados

- `../frontend/15-arquitetura-motion-e-bibliotecas.md`
- `../frontend/16-animacao-assinatura-tinta-transposicao.md`
- `../frontend/17-catalogo-animacoes-interface.md`
- `../qa/09-testes-motion-performance.md`

## Documentos integrados

Foram atualizados índice, stack, decisões arquiteturais, frontend, páginas Home/Transpor/Resultado, acessibilidade, performance, QA, critérios de aceite, Definition of Done, guia Codex, referências, decisões e changelog.

## Gates principais

- uma única engine controla cada propriedade/nó;
- GSAP não aparece em rotas sem cena;
- Anime.js e React Spring não entram no lockfile do Core;
- Strict Mode não duplica timeline;
- intro pode ser interrompida sem erro;
- loop pausa em background e termina com o job;
- reduced motion usa composição própria;
- fallback estático mantém identidade e funcionalidade;
- performance é medida em dispositivo móvel intermediário.

## Resultado

A ideia visual foi transformada em decisão arquitetural, storyboard, componentes, fronteiras de bibliotecas, estratégia de carregamento, acessibilidade, orçamento inicial e plano de testes. A implementação no código continua pendente e deve seguir os gates documentados.
