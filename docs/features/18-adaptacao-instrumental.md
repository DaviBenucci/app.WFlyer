# Adaptação instrumental assistida

> Status: canônico para trilha A. Capacidade futura.

## Objetivo

Transformar uma versão confirmada em escrita mais executável para um instrumento e nível, oferecendo alternativas localizadas.

## Modos

```text
CHECK_ONLY
SUGGEST
APPLY_SELECTED
```

`CHECK_ONLY` nunca altera notas. `SUGGEST` cria opções. `APPLY_SELECTED` exige escolhas e gera nova versão.

## Parâmetros

- instrumento/configuração;
- nível;
- andamento alvo;
- orçamento de alteração;
- manter pitch classes/ritmo/frases;
- permitir oitava/revoicing/omissão;
- preferência de clave;
- técnica especial permitida.

## Resultado

```text
playability_report
adaptation_options
selected_adaptations
adapted_musicxml
musical_diff
assurance_report
```

## Regra

A aplicação não decide que uma escrita “precisa” ser simplificada apenas por estatística. Violação rígida bloqueia; warning permite decisão informada; sugestão editorial é opcional.
