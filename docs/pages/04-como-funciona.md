# Tela Como funciona

## Rota

```text
/como-funciona
```

## Objetivo

Explicar o fluxo técnico e musical da ferramenta sem virar material institucional.

## Conteúdo do MVP

1. O que a aplicação faz.
2. Upload de partitura.
3. Escolha manual de instrumento de origem.
4. Escolha manual de instrumento de destino.
5. Cálculo do intervalo.
6. Processamento assíncrono.
7. Resultado baixável.
8. Limitações de PDF e OMR.

## Exemplo obrigatório

```text
Piano C -> Trompete Bb
0 - (-2) = +2 semitons
C maior -> D maior
```

## Regras

- Não prometer OMR perfeito.
- Explicar que MusicXML é priorizado no início do desenvolvimento.
- Explicar que PDFs ruins podem gerar erro amigável.
- Orientar revisão musical do resultado.

## Critérios de aceite

- Usuário entende o fluxo em até 1 minuto.
- Página explica o risco técnico de PDF.
- Página direciona para `/transpor`.
