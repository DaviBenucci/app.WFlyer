# Página Instrumentos suportados

> Revisão: 2026-07-20.

## Rota

```text
/instrumentos
```

## Objetivo

Apresentar o catálogo como biblioteca musical pesquisável, não como grid de cards repetidos.

## Shell

`PublicShell` ou `UtilityShell`, conforme navegação final.

## Desktop

```text
Header da página
Busca + filtros por família
InstrumentLibrary
  lista/tabela estruturada
InstrumentDetailPanel
```

A lista permite comparar nome, afinação, família, clave e comportamento de C escrito. O painel detalha o item selecionado.

## Mobile

- busca no topo;
- chips de família em scroll acessível;
- linhas compactas;
- detalhe em sheet;
- CTA para usar como origem/destino.

## Dados

Vêm da API/cliente gerado. Não hardcodar intervalos.

## Apresentação

Para cada instrumento:

- nome e aliases;
- família;
- afinação;
- “quando lê C, soa ...” com oitava;
- intervalo escrito → concerto;
- clave padrão como referência;
- badge de transposição de oitava quando aplicável.

## Visual de família

Famílias podem ter ícone/acentuação secundária, mas a cor não muda regras de status nem prejudica contraste.

## Ações

```text
Usar como origem
Usar como destino
Iniciar transposição
```

A seleção prévia deve ser confirmada na tela Transpor.

## Estados

```text
loading
loaded
empty_search
api_error
offline_sem_cache_privado
```

## Critérios de aceite

- comparação é mais fácil que em um grid de cards;
- instrumentos de oitava aparecem corretamente;
- busca por alias funciona;
- teclado e mobile são suportados;
- nenhum instrumento inativo é oferecido.
