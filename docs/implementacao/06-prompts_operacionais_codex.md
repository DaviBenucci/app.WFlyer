# Prompts operacionais para Codex

## Prompt para iniciar uma fase

```text
Leia README.md, docs/00-visao-geral/05-escopo-mvp-app-wflyer.md,
W-Flyer_Regra-Transposição.md e docs/100-implementacao/guia-codex-app-wflyer.md.
Execute somente a fase <N>, sem avançar para a próxima.
Ao final, registre testes, arquivos alterados, pendências e critério de conclusão.
```

## Prompt para revisão de fase

```text
Revise a fase <N> contra o guia Codex e os critérios de aceite do MVP.
Procure vazamento de stacktrace, path físico, storage_key, regra musical duplicada
e requisitos fora do MVP.
```

## Prompt para regra musical

```text
Antes de alterar o motor musical, leia W-Flyer_Regra-Transposição.md e
docs/features/11-catalogo-instrumentos-mvp.md.
Garanta que a fórmula usada seja:
intervalo_escrito = origem.written_to_concert - destino.written_to_concert.
```
