# Seleção do instrumento de destino

## Objetivo

Escolher para qual instrumento a parte será reescrita e apresentar a transformação calculada pelo backend.

## Fluxo

```text
selecionar destino
-> UI pode mostrar prévia não autoritativa
-> POST /api/v1/transpositions
-> backend calcula output_interval vetorial
-> UI exibe nome, direção e oitava
```

Exemplos:

```text
Piano -> Trompete Bb: segunda maior acima (+2)
Piano -> Sax tenor Bb: nona maior acima (+14)
Violão -> Piano: uma oitava abaixo (-12)
```

## Regras

- destino obrigatório e ativo;
- não aceitar instrumento não afinado no Core;
- origem e destino iguais são permitidos: intervalo zero, normalização/validação ainda ocorrem;
- não reduzir todo intervalo a “N semitons” quando a grafia diatônica ou a oitava importam;
- cliente nunca envia o intervalo como autoridade.

## Feedback

Mostrar:

- origem e destino;
- nome do intervalo;
- direção;
- exemplo de nota/tonalidade somente quando o contexto permite;
- aviso de oitava para instrumentos relevantes;
- aviso de revisão de clave/tessitura quando retornado pelo job.

## Testes

- Piano -> Trompete Bb resulta em `(diatonic=1, chromatic=2, octave=0)`;
- Piano -> Sax tenor Bb resulta em `(1, 2, 1)` e total `+14`;
- Violão -> Piano resulta em `(0, 0, -1)`;
- alteração do destino atualiza resumo;
- resposta do backend prevalece sobre qualquer prévia local.
