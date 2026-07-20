# Corpus e fixtures

## Estrutura

```text
tests/fixtures/
  musicxml/core/valid/
  musicxml/core/rejected/
  musicxml/expected/
  hostile/xml/
  hostile/mxl/
  hostile/pdf/
  omr/inputs/
  omr/expected/
  metadata/manifest.yml
```

## Manifesto obrigatório

Cada fixture registra:

```text
id
path
sha256
formato/versão
origem e licença
características musicais
perfil esperado: accept | reject | warning
instrumento de origem
resultados esperados por destino
data/revisor
```

Não incluir partitura protegida sem autorização/licença adequada.

## Classes Core válidas

- tonalidades maiores/menores;
- sem armadura/atonal simples;
- acidentes;
- mudança de tonalidade/compasso/clave;
- vozes e acordes em uma pauta;
- ties/tuplets/grace notes suportadas;
- harmony;
- instrumentos em C, Bb, Eb, F e transposição de oitava.

## Rejeitadas

- multiparte/multipauta;
- microtom;
- unpitched/percussão;
- tablatura;
- score-timewise/opus;
- XML malformado/hostil;
- metadata de origem contraditória.

## Golden e revisão

- manter original imutável;
- expected semântico em formato legível;
- golden de arquivo só para saída estável relevante;
- mudança de biblioteca não autoriza atualizar tudo automaticamente;
- revisão musical obrigatória para alteração de pitch/armadura/harmony.

## Corpus OMR

Antes de ativar PDF, cobrir digital, scan, ruído, rotação, resoluções, fontes, páginas múltiplas e falhas conhecidas. Separar treino/ajuste do conjunto de avaliação para não inflar métricas.
