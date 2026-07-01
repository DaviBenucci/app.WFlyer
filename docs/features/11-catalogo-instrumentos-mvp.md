# Catálogo inicial de instrumentos do MVP

## Objetivo

Definir o catálogo mínimo que o backend deve servir ao frontend e que o motor musical deve usar para calcular a transposição.

O campo central é `written_to_concert`: quantos semitons a nota real soa em relação à nota escrita.

## Campos obrigatórios

```text
id
name
family
key_name
written_to_concert
transposes_octave
octave_offset
observations
is_active
```

## Instrumentos mínimos

| id | nome | família | afinação | written_to_concert | transpõe oitava | observações | casos de teste mínimos |
|---|---|---|---:|---:|---|---|---|
| `piano` | Piano | teclas | C | 0 | não | Som real. | Piano -> Trompete Bb; mesmo instrumento. |
| `voice` | Voz | voz | C | 0 | não | Som real para canto. | Voz -> Clarinete Bb. |
| `flute` | Flauta | madeiras | C | 0 | não | Som real. | Flauta -> Sax Alto Eb. |
| `violin` | Violino | cordas | C | 0 | não | Som real. | Violino -> Trompa F. |
| `guitar` | Violão | cordas | C | 0 | sim | Notação pode soar uma oitava abaixo; o MVP deve registrar a observação e não ignorar política de oitava. | Violão -> Piano sem mudar classe de altura. |
| `trumpet-bb` | Trompete Bb | metais | Bb | -2 | não | Quando lê C, soa Bb. | Piano -> Trompete Bb; Trompete Bb -> Piano. |
| `clarinet-bb` | Clarinete Bb | madeiras | Bb | -2 | não | Quando lê C, soa Bb. | Clarinete Bb -> Sax Alto Eb. |
| `tenor-sax-bb` | Sax Tenor Bb | madeiras | Bb | -14 | sim | Soa nona maior abaixo do escrito. | Sax Tenor Bb -> Piano; Piano -> Sax Tenor Bb. |
| `alto-sax-eb` | Sax Alto Eb | madeiras | Eb | -9 | não | Quando lê C, soa Eb abaixo. | Piano -> Sax Alto Eb; Sax Alto Eb -> Piano. |
| `baritone-sax-eb` | Sax Barítono Eb | madeiras | Eb | -21 | sim | Soa décima terceira maior abaixo do escrito. | Sax Barítono Eb -> Piano. |
| `horn-f` | Trompa F | metais | F | -7 | não | Quando lê C, soa F. | Trompa F -> Piano; Piano -> Trompa F. |

## Regras

- O catálogo deve ser a fonte de verdade para transposição.
- O frontend não deve manter catálogo paralelo como regra final.
- Instrumentos inativos não podem ser usados para criar job.
- Alias e nomes alternativos podem existir, mas não substituem `id` estável.
- A transposição não deve ser codificada por par de instrumentos.

## Casos de teste obrigatórios

```text
Piano C -> Trompete Bb: +2 semitons
Trompete Bb -> Piano C: -2 semitons
Piano C -> Sax Alto Eb: +9 semitons
Sax Alto Eb -> Piano C: -9 semitons
Clarinete Bb -> Sax Alto Eb: +7 semitons
Trompa F -> Piano C: -7 semitons
Mesmo instrumento -> 0 semitons
```

Também devem existir testes com acidentes, acordes e armadura de clave.
