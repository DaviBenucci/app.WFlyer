# Testes musicais

## Objetivo

Garantir que a transposição esteja musicalmente correta, não apenas visualmente funcional.

## Fórmula sob teste

```text
intervalo_escrito = origem.written_to_concert - destino.written_to_concert
```

## Casos mínimos

| Origem | Destino | Intervalo esperado | Exemplo de tonalidade |
|---|---|---:|---|
| Piano C | Trompete Bb | +2 | C -> D |
| Trompete Bb | Piano C | -2 | C -> Bb |
| Piano C | Sax Alto Eb | +9 | C -> A |
| Sax Alto Eb | Piano C | -9 | C -> Eb |
| Clarinete Bb | Sax Alto Eb | +7 | C -> G |
| Trompa F | Piano C | -7 | C -> F |
| Piano C | Piano C | 0 | C -> C |

## Casos estruturais

- Transposição com acidentes locais.
- Transposição com acordes.
- Transposição com armadura de clave.
- Transposição com múltiplas partes quando houver fixture.
- Enarmonia legível quando houver equivalentes.

## Fixtures iniciais

```text
escala de C maior
melodia com F# e Bb
cifras/acordes C, F, G7, Am
trecho com armadura de D maior
partitura com duas partes simples
```

## Regras de falha

O teste deve falhar se:

- apenas o nome da tonalidade for alterado;
- notas permanecerem iguais quando intervalo não for zero;
- armadura não for recalculada;
- acidentes locais forem descartados sem regra;
- transposição inversa não voltar ao resultado esperado.
