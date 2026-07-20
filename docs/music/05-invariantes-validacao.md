# Invariantes e validação semântica

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Impedir que um arquivo tecnicamente gerado seja tratado como resultado musicalmente correto.

## Invariante de altura de concerto

Para cada nota afinada mapeada:

```text
source_written + source_to_concert
=
target_written + target_to_concert
```

A comparação considera letra, acidente, oitava e microtons; microtons devem causar rejeição no Core.

## Invariantes rítmicos

- duração total por voz e medida preservada;
- fórmula de compasso preservada;
- posições de ataques preservadas;
- pausas preservadas;
- ties e tuplets semanticamente equivalentes;
- nenhuma medida fica subpreenchida ou sobrepreenchida por efeito da transposição.

## Invariantes estruturais

- uma parte e uma pauta no Core;
- número e ordem de medidas preservados;
- número de vozes preservado;
- mudanças de clave, compasso e tonalidade permanecem nas mesmas posições;
- notas não afinadas ou estruturas proibidas provocam rejeição explícita.

## Invariantes de notação

- armaduras transpostas pelo intervalo simples;
- acidentes representam a altura correta na nova armadura;
- cifras suportadas têm raiz e baixo transpostos;
- letras, dinâmica, articulações e texto não são musicalmente alterados;
- `<transpose>` de saída corresponde ao destino;
- não existe dupla transposição na reprodução.

## Invariantes de artefato

- original imutável;
- hash registrado para cada artefato;
- artefato público deriva do job correto;
- gravação atômica;
- tamanho maior que zero;
- MIME e extensão da saída conferem;
- artefato interno nunca aparece em DTO público.

## Comparação de testes

Testes não devem comparar apenas XML textual. O comparador semântico deve extrair uma representação estável contendo:

```text
part/staff/measure/voice
onset
written pitch
concert pitch
 duration
key/time/clef changes
harmony roots/bass
transpose metadata
```

Diferenças de whitespace, IDs gerados e layout não devem mascarar nem fabricar falhas musicais.

## Resultado com warnings

Um warning só permite `completed_with_warnings` quando nenhum invariante obrigatório foi violado. Violação de altura, ritmo, estrutura suportada ou integridade do artefato sempre resulta em `failed`.
