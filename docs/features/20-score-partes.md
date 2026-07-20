# Score e partes derivadas

> Status: canônico para trilha E. Revisão: 2026-07-20.

## Objetivo

Gerar score e partes a partir de uma única versão canônica, com transposição e layout adequados a cada instrumento.

## Modos do score

```text
WRITTEN_PITCH
CONCERT_PITCH
BOTH_AS_SEPARATE_ARTIFACTS
```

Trocar modo de visualização não deve modificar o grafo musical.

## Parte

Cada parte possui:

- instrument snapshot;
- eventos semânticos referenciados;
- layout próprio;
- cues/tacets explícitos quando habilitados;
- relatório de tocabilidade;
- hash e manifesto.

## Atualização

Alteração no score cria nova versão e invalida partes derivadas. Regeneração incremental pode reutilizar artefatos somente quando o hash da dependência não mudou.

## Gate

- consistência de pitch/ritmo;
- rehearsal marks e measure numbers;
- transposição escrita;
- page turns;
- bundle atômico.
