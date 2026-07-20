# Política de enarmonia, armadura e oitavas

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Produzir uma escrita musical legível e coerente, sem confundir equivalência sonora com equivalência notacional.

## Regra principal de grafia

A nova letra da nota é determinada pelo componente `diatonic_steps`. O acidente necessário é calculado para alcançar o deslocamento `chromatic_semitones`.

Exemplo de segunda maior acima:

```text
C -> D
E -> F#
Bb -> C
```

Um algoritmo que soma apenas dois semitons pode gerar grafias erradas, como `E -> Gb`.

## Política de armadura

1. Transpor a tonalidade declarada pelo intervalo simples.
2. Preservar o modo.
3. Preferir armaduras convencionais entre sete bemóis e sete sustenidos.
4. Quando duas grafias forem sonoramente equivalentes, escolher a de menor complexidade, salvo exigência teórica explícita suportada.
5. Registrar `ENHARMONIC_SIMPLIFICATION` quando a grafia for simplificada.
6. Não inferir tonalidade quando o documento não a declara.

## Acidentes locais

- Recalcular a necessidade visual do acidente no contexto da armadura resultante.
- Preservar a altura efetiva da nota.
- Não copiar cegamente o símbolo de acidente da origem.
- Manter acidentes de cortesia apenas quando a biblioteca e o perfil suportarem; caso contrário, registrar perda visual não semântica.

## Cifras

Para `<harmony>` suportado:

- transpor `root-step/root-alter`;
- transpor `bass-step/bass-alter`;
- preservar qualidade, extensões e alterações relativas;
- rejeitar ou avisar quando a construção não puder ser round-tripped com segurança.

## Oitavas

A parcela `octave_change` preserva a oitava sonora de instrumentos como violão, sax tenor e sax barítono.

- `octave_change` do instrumento não é a mesma coisa que marcação gráfica `8va/8vb`;
- marcas de oitava na música devem ser preservadas como notação e não absorvidas no preset do instrumento;
- a clave pode possuir `clef-octave-change`, que também não deve ser duplicado na transposição instrumental.

## Clave

No MVP Core a clave da origem é preservada. O sistema pode avisar `TARGET_CLEF_REVIEW_RECOMMENDED` quando a clave padrão do destino for diferente. Redesenho automático de clave é uma capacidade futura.

## Tessitura

A transposição correta pode produzir notas fora da tessitura prática do destino. O Core não altera oitavas para “caber” automaticamente. Quando ranges confiáveis estiverem cadastrados, pode emitir `OUT_OF_RECOMMENDED_RANGE` sem mudar as notas.

## Casos obrigatórios

- C maior -> D maior;
- F maior -> G maior;
- Eb maior -> F maior;
- tonalidade menor;
- mudança de tonalidade no meio da parte;
- acidentes cromáticos;
- dupla alteração quando inevitável;
- simplificação enarmônica;
- instrumento com transposição de oitava;
- armadura ausente/atonal.
