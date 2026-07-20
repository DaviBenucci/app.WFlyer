# Glossário do W_Flyer

> Status: canônico. Revisão: 2026-07-20.

## Altura escrita

Altura notada para o instrumentista.

## Altura de concerto

Altura sonora real usada para comparar instrumentos.

## Intervalo `written_to_concert`

Transformação que deve ser adicionada à altura escrita para obter a altura de concerto. No W_Flyer ela é composta por:

- `diatonic_steps`: passos de letra musical, sem contar a parcela de oitava;
- `chromatic_semitones`: semitons, sem contar a parcela de oitava;
- `octave_change`: oitavas completas.

Exemplo para trompete em Bb:

```json
{
  "diatonic_steps": -1,
  "chromatic_semitones": -2,
  "octave_change": 0
}
```

## Intervalo escrito de saída

Diferença entre a transformação da origem e a transformação do destino:

```text
output_interval = source.written_to_concert - target.written_to_concert
```

A subtração é feita em cada componente.

## MusicXML bruto

MusicXML recebido do usuário ou produzido pelo OMR, antes da normalização do W_Flyer.

## MusicXML normalizado

Representação canônica validada, com estrutura e metadados coerentes para o motor musical.

## OMR

Optical Music Recognition. Conversão de uma imagem de partitura para representação simbólica. Não é OCR textual e não é determinístico em todos os documentos.

## Parte e pauta

Uma parte representa um instrumento/voz no score. Uma pauta é a estrutura de cinco linhas na qual a parte é notada. O MVP Core aceita uma parte e uma pauta por job.

## Grafia enarmônica

Escolha entre notas de mesma altura sonora, como F# e Gb. A grafia depende do intervalo diatônico e da tonalidade, não apenas do número de semitons.

## Job

Solicitação assíncrona de processamento. `status`, `stage` e `retention_status` são conceitos distintos.

## Sessão anônima

Identidade temporária, sem conta, usada para autorizar o acesso aos objetos criados pelo navegador.

## Artefato

Arquivo versionado do pipeline, interno ou público. Exemplos: original, MusicXML normalizado, MusicXML transposto e PDF renderizado.

## Aviso público

Código categórico e mensagem segura que comunica incerteza ou limitação sem revelar métricas internas.

## Gate

Conjunto objetivo de critérios que bloqueia a progressão ou a ativação de uma capacidade.
