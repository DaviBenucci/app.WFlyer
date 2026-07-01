# Seleção de instrumento de origem

## Objetivo

Confirmar manualmente para qual instrumento a partitura original foi escrita.

## Fluxo

```text
Carregar instrumentos
Usuário escolhe instrumento de origem
Wizard grava source_instrument_id
```

## Detecção automática

Detecção automática perfeita não faz parte do MVP. Se existir sugestão simples no futuro, ela nunca deve substituir a confirmação manual.

## UI

- Busca por nome.
- Filtro por família quando útil.
- Cards com instrumento, família e afinação.
- Explicação simples de transposição.

## Regras

- Origem é obrigatória.
- Instrumento deve estar ativo no catálogo.
- Confidence score não aparece na UI pública.

## Testes

- Busca encontra instrumento.
- Seleção habilita próxima etapa.
- Instrumento inativo não pode ser selecionado.
