# Cálculo de transposição

> Status: canônico por referência a `../music/01-modelo-transposicao.md`.

## Objetivo

Preservar a altura de concerto ao reescrever a parte para outro instrumento, mantendo grafia musical e oitava coerentes.

## Modelo

Cada instrumento possui:

```text
written_to_concert = (diatonic_steps, chromatic_semitones, octave_change)
```

O intervalo de saída é:

```text
output_interval = source.written_to_concert - target.written_to_concert
```

A operação é componente a componente; `total_semitones` é apenas derivado.

Invariante:

```text
source_written + source_to_concert
=
target_written + target_to_concert
```

## Transformações obrigatórias

- alturas de todas as notas afinadas;
- notas de acordes simultâneos;
- armaduras e mudanças de tonalidade;
- acidentes no novo contexto;
- raiz/baixo de cifras suportadas;
- metadado `<transpose>` do instrumento de destino.

Ritmo, vozes, ties, tuplets, texto, dinâmica e articulações suportadas devem manter semântica.

## Não fazer

- não alterar pixels/PDF diretamente;
- não usar apenas um inteiro de semitons;
- não escolher enarmonia só pelo sinal;
- não codificar pares de instrumento;
- não alterar apenas a armadura;
- não somar duas vezes o `<transpose>`.

## Resultado

O backend retorna o intervalo calculado e produz MusicXML transposto. A validação obrigatória está em `../music/05-invariantes-validacao.md` e a cobertura em `../qa/05-testes-musicais.md`.
