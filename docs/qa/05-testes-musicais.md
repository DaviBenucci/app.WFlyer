# Testes musicais

> Status: canônico. Revisão: 2026-07-20.

## Oráculo

Comparar semântica, não XML textual. Extrair eventos por parte/pauta/medida/voz/onset com pitch escrito, pitch de concerto, duração, ties/tuplets, tonalidade, compasso, clave, harmony e `<transpose>`.

## Unit/property tests do catálogo

Para todo instrumento A e B:

```text
interval(A->B) = A.to_concert - B.to_concert
concert(source) = concert(transposed)
interval(A->B) = -interval(B->A)
A -> B -> A é semanticamente equivalente
```

Cobrir total e componente diatônico/oitava, não apenas pitch class.

## Pares obrigatórios

| Origem | Destino | Intervalo escrito esperado |
|---|---|---|
| Piano | Trompete Bb | M2 acima: `(1,2,0)` |
| Trompete Bb | Piano | M2 abaixo: `(-1,-2,0)` |
| Piano | Sax alto Eb | M6 acima: `(5,9,0)` |
| Piano | Sax tenor Bb | M9 acima: `(1,2,1)` |
| Piano | Sax barítono Eb | M13 acima: `(5,9,1)` |
| Violão | Piano | P8 abaixo: `(0,0,-1)` |
| Trompa F | Piano | P5 abaixo: `(-4,-7,0)` |
| Clarinete Bb | Sax alto Eb | P5 acima: `(4,7,0)` |
| mesmo instrumento | mesmo | uníssono `(0,0,0)` |

## Fixtures Core

- escala maior/menor em diferentes armaduras;
- acidentes locais e de cortesia;
- mudanças de tonalidade;
- múltiplas vozes na mesma pauta;
- acordes simultâneos;
- ties e tuplets;
- grace notes suportadas;
- cifras com raiz e baixo;
- mudança de clave/compasso;
- instrumento de origem com/sem `<transpose>`;
- layout/metadados que podem mudar sem alterar semântica.

## Rejeição

- mais de uma parte;
- mais de uma pauta;
- `score-timewise`/opus;
- percussão não afinada;
- microtons;
- tablatura;
- recurso cuja semântica não possa ser preservada;
- `<transpose>` contraditório.

## Invariantes

- número/ordem de medidas e vozes;
- onset/duração/ritmo;
- pitch de concerto por nota;
- tonalidades/armaduras transpostas;
- harmony transposta;
- `<transpose>` do destino;
- nenhuma dupla transposição;
- output parseável e dentro do perfil.

## Golden files

Golden XML é revisado por músico/engenheiro, versionado com origem/licença e acompanhado de representação semântica esperada. Atualizar golden exige explicar a mudança; nunca aceitar snapshot massivamente só para “fazer passar”.
