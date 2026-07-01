# Árvore documental e estrutura esperada

## Documentação atual

```text
app.Wflyer/
  README.md
  W-Flyer_Regra-Transposição.md
  TREE.md
  MANIFESTO_VALIDACAO.md
  docs/
    00-visao-geral/
      00-indice.md
      01-decisoes-arquiteturais.md
      02-roadmap-fases.md
      03-glossario.md
      04-stack-recomendada.md
      05-escopo-mvp-app-wflyer.md
    100-implementacao/
      guia-codex-app-wflyer.md
      criterios-aceite-mvp.md
    backend/
    features/
    frontend/
    implementacao/
    logs/
    pages/
    qa/
    security/
```

## Estrutura esperada para o código futuro

```text
app-wflyer/
  apps/
    web/
      src/
        app/
        components/
        features/
        services/
        hooks/
        lib/
        styles/
        tests/
    api/
      src/
        modules/
        routes/
        services/
        workers/
        repositories/
        validators/
        middlewares/
        tests/
  packages/
    shared/
      src/
        types/
        constants/
        music/
        validation/
    ui/
      src/
        components/
  docs/
```

Detalhes: `docs/backend/13-estrutura-pastas.md`.
