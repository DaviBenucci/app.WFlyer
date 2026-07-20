# Seleção do instrumento de origem

## Objetivo

Registrar para qual instrumento a parte de entrada foi escrita. No Core a seleção é manual e obrigatória.

## Fluxo

```text
GET /api/v1/instruments
-> usuário busca/filtra
-> seleciona origem
-> UI mostra afinação escrita/concerto em linguagem simples
-> seleção entra no pedido de transposição
```

## Fonte de verdade

O catálogo vem da API. Não manter uma cópia independente com intervalos no frontend.

## Metadado do arquivo

Durante a normalização, o backend lê `<transpose>` quando presente:

- coincide com o preset selecionado: continuar;
- ausente: usar a declaração manual;
- diverge: falhar com `SOURCE_INSTRUMENT_MISMATCH` e pedir correção.

O sistema não deve “escolher o que parece certo” silenciosamente.

## Detecção automática

Detecção de instrumento por texto/OMR não faz parte do Core. Uma sugestão futura deve indicar que é sugestão, registrar fonte/confiança internamente e exigir confirmação.

## Regras de UI

- origem obrigatória;
- apenas instrumento ativo e afinado suportado;
- busca por nome/alias;
- explicar instrumentos que soam em oitava;
- não exibir score numérico de confiança;
- preservar seleção apenas como preferência local, nunca como prova do arquivo.

## Testes

- catálogo e aliases funcionam;
- instrumento inativo não é selecionável;
- metadata coincidente passa;
- metadata divergente bloqueia;
- metadata ausente usa seleção manual;
- violão e sax tenor exibem indicação de oitava.
