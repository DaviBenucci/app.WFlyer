# Modelo canônico de transposição

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Definir uma transformação musical que preserve a altura de concerto ao converter uma parte escrita para um instrumento de origem em uma parte escrita para um instrumento de destino.

## Representação do instrumento

Cada preset de instrumento declara o intervalo que deve ser adicionado à nota escrita para obter a nota de concerto:

```ts
type WrittenToConcert = {
  diatonic_steps: number
  chromatic_semitones: number
  octave_change: number
}
```

Os campos `diatonic_steps` e `chromatic_semitones` não incluem a parcela de oitava. O total cromático é derivado:

```text
total_semitones = chromatic_semitones + 12 * octave_change
```

Exemplos:

| Instrumento | diatonic | chromatic | octave | total |
|---|---:|---:|---:|---:|
| Piano em C | 0 | 0 | 0 | 0 |
| Trompete Bb | -1 | -2 | 0 | -2 |
| Trompa F | -4 | -7 | 0 | -7 |
| Sax alto Eb | -5 | -9 | 0 | -9 |
| Sax tenor Bb | -1 | -2 | -1 | -14 |
| Violão | 0 | 0 | -1 | -12 |

## Fórmula

```text
output_interval.diatonic = source.diatonic - target.diatonic
output_interval.chromatic = source.chromatic - target.chromatic
output_interval.octave = source.octave - target.octave
output_interval.total_semitones =
  output_interval.chromatic + 12 * output_interval.octave
```

Aplicação:

```text
target_written_pitch = source_written_pitch + output_interval
```

Invariante central:

```text
source_written_pitch + source.written_to_concert
=
target_written_pitch + target.written_to_concert
```

A igualdade deve ser verificada para cada evento de altura.

## Exemplos

### Piano em C para trompete Bb

```text
source = (0, 0, 0)
target = (-1, -2, 0)
output = (+1, +2, 0) = segunda maior acima
C4 escrito -> D4 escrito
C4 concerto = D4 escrito no trompete -> C4 concerto
```

### Piano em C para sax tenor Bb

```text
source = (0, 0, 0)
target = (-1, -2, -1)
output = (+1, +2, +1) = nona maior acima
C4 escrito -> D5 escrito
```

### Violão para piano

```text
source = (0, 0, -1)
target = (0, 0, 0)
output = (0, 0, -1)
C4 escrito no violão -> C3 escrito no piano
```

O valor anterior `written_to_concert = 0` para violão era incorreto para preservação de oitava sonora.

## Alturas, acordes e cifras

A transformação deve ser aplicada a:

- cada `<pitch>` afinado;
- todas as notas de acordes simultâneos;
- raiz e baixo de símbolos `<harmony>` suportados;
- regiões após mudanças de tonalidade;
- notas ornamentais e grace notes, quando suportadas pelo parser.

Pausas não possuem altura e não são transpostas.

## Armadura e tonalidade

A armadura é transposta pelo componente simples diatônico/cromático. `octave_change` não altera tonalidade.

- modo maior/menor é preservado;
- ausência de armadura não autoriza inferir tonalidade;
- mudanças de tonalidade são processadas individualmente;
- armaduras fora do perfil convencional seguem a política enarmônica ou são rejeitadas.

## Metadado MusicXML `<transpose>`

O documento final deve declarar o intervalo `written_to_concert` do instrumento de destino. As notas do resultado já são alturas escritas para o destino; o metadado existe para que reprodução e intercâmbio obtenham o som de concerto correto.

É proibido aplicar o intervalo nas notas e depois aplicar novamente o `<transpose>` como se fosse uma segunda transformação.

## Metadado da origem

Quando o MusicXML de entrada contém `<transpose>`:

- o backend compara o valor com o preset de origem selecionado;
- se houver divergência, o job falha com `SOURCE_INSTRUMENT_MISMATCH`;
- o MVP não corrige silenciosamente nem ignora a divergência.

Quando o arquivo não contém o metadado, a seleção manual é a fonte declarada.

## Mesmo instrumento

Origem e destino iguais produzem intervalo zero. O job ainda pode normalizar e validar o MusicXML, portanto o arquivo final não precisa ser byte a byte idêntico.

## Proibições

- Não usar apenas `transpose_interval: number` como modelo interno.
- Não escolher F# ou Gb apenas pelo sinal do semitom.
- Não codificar pares de instrumentos com `if/else`.
- Não alterar somente armadura ou nome da tonalidade.
- Não usar MIDI como fonte canônica de notação.
