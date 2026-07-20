# Catálogo de instrumentos do MVP

> Status: canônico. Revisão: 2026-07-20.

## Modelo

O intervalo declara o que deve ser adicionado à nota escrita para obter a nota de concerto:

```text
written_to_concert_diatonic
written_to_concert_chromatic
written_to_concert_octave
```

Derivado:

```text
total_semitones = chromatic + 12 * octave
```

Campos:

```text
id
name
family
key_name
written_to_concert_diatonic
written_to_concert_chromatic
written_to_concert_octave
default_clef
aliases
is_pitched
is_active
catalog_version
```

## Presets iniciais

| id | instrumento | família | key | diatonic | chromatic | octave | total | clave padrão |
|---|---|---|---|---:|---:|---:|---:|---|
| `piano` | Piano | teclas | C | 0 | 0 | 0 | 0 | treble |
| `voice` | Voz | voz | C | 0 | 0 | 0 | 0 | treble |
| `flute` | Flauta | madeiras | C | 0 | 0 | 0 | 0 | treble |
| `violin` | Violino | cordas | C | 0 | 0 | 0 | 0 | treble |
| `guitar` | Violão | cordas | C | 0 | 0 | -1 | -12 | treble-8 |
| `trumpet-bb` | Trompete Bb | metais | Bb | -1 | -2 | 0 | -2 | treble |
| `clarinet-bb` | Clarinete Bb | madeiras | Bb | -1 | -2 | 0 | -2 | treble |
| `tenor-sax-bb` | Sax tenor Bb | madeiras | Bb | -1 | -2 | -1 | -14 | treble |
| `alto-sax-eb` | Sax alto Eb | madeiras | Eb | -5 | -9 | 0 | -9 | treble |
| `baritone-sax-eb` | Sax barítono Eb | madeiras | Eb | -5 | -9 | -1 | -21 | treble |
| `horn-f` | Trompa F | metais | F | -4 | -7 | 0 | -7 | treble |

`treble-8` é label de apresentação; a representação MusicXML de clave e a transposição instrumental não podem duplicar a oitava.

O preset `piano` representa uma linha/parte melódica em C. Uma partitura típica de piano em grande pauta possui duas pautas e permanece fora do perfil Core.

## Regras

- total é calculado, não editado independentemente;
- API retorna apenas ativos;
- job salva snapshot completo do preset e versão;
- frontend não mantém intervalos autoritativos;
- presets não afinados/percussão ficam fora do Core;
- ranges práticos são futuros e não alteram automaticamente oitavas;
- qualquer correção exige ADR, atualização do corpus e migração/versionamento.

## Testes obrigatórios

- validar schema e total de cada preset;
- todos os pares origem/destino preservam altura de concerto em property test;
- A -> B e B -> A retornam semanticamente à origem;
- cobrir instrumentos com oitava: violão, tenor e barítono;
- conferir `<transpose>` emitido para cada destino;
- detectar catálogo divergente entre banco e fixture versionada.

## Expansão de capacidades instrumentais

O catálogo futuro adiciona `capabilities_snapshot` conforme `../music/09-perfis-instrumentais-polifonia-extensao.md`. Afinação e família continuam insuficientes para decidir harmonização, redução ou tocabilidade. Alterações de faixa/polifonia exigem nova `capability_version` e reexecução do corpus.
