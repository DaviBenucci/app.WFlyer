# Tela Como funciona

> Revisão: 2026-07-20.

## Rota

```text
/como-funciona
```

## Objetivo

Explicar o fluxo real e as limitações com composição editorial e diagramas próprios, sem marketing vago.

## Shell

`PublicShell`.

## Estrutura

```text
Introdução curta
Diagrama 1: nota escrita e som de concerto
Diagrama 2: origem -> intervalo -> destino
Pipeline real do Core
Exemplo Piano -> Trompete Bb
Exemplo com instrumento de oitava
Limitações e revisão
CTA
```

## Diagramas

Usar SVG simples, acessível e determinístico. Cada diagrama possui legenda textual equivalente. Não usar imagem genérica de partitura como fundo.

## Conteúdo obrigatório

1. MusicXML como estrutura usada pelo Core;
2. confirmação de origem e destino;
3. preservação do som de concerto;
4. transposição de notas, armaduras e cifras suportadas;
5. processamento assíncrono;
6. resultado disponível por janela de retenção;
7. necessidade de revisão humana;
8. PDF/OMR somente quando capability existir.

## Exemplo principal

```text
Piano em C -> Trompete Bb
C4 de concerto é escrito como D4 no trompete Bb.
```

## Estilo

- largura de leitura controlada;
- títulos editoriais;
- diagramas inseridos no fluxo;
- dividers inspirados em barras de compasso;
- CTA final discreto.

## Evitar

- accordion para esconder todo o conteúdo;
- cards iguais para cada etapa;
- afirmação de precisão percentual sem corpus;
- explicar tudo como “IA”;
- prometer layout idêntico ao original.
