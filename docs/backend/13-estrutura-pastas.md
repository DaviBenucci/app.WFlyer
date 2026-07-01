# Estrutura de código esperada

## Estrutura base

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

## Responsabilidades

### `apps/web`

Frontend da aplicação:

- telas;
- componentes;
- hooks;
- serviços de API;
- estados de UI;
- testes frontend.

### `apps/api`

Backend da aplicação:

- rotas HTTP;
- módulos de domínio;
- validações;
- serviços;
- workers;
- repositórios;
- middlewares;
- testes backend.

### `packages/shared`

Código compartilhado:

- tipos públicos;
- constantes;
- regra musical central;
- schemas de validação reutilizáveis;
- catálogo base quando fizer sentido.

### `packages/ui`

Componentes visuais reutilizáveis sem regra de negócio sensível.

### `docs`

Documentação técnica, contratos, decisões, critérios de aceite e guia Codex.

## Onde ficam itens críticos

| Item | Local esperado |
|---|---|
| Frontend | `apps/web/src/` |
| Backend | `apps/api/src/` |
| Tipos compartilhados | `packages/shared/src/types/` |
| Regras musicais | `packages/shared/src/music/` ou `apps/api/src/modules/music-engine/` |
| Testes frontend | `apps/web/src/tests/` |
| Testes backend | `apps/api/src/tests/` |
| Testes musicais | `packages/shared/src/music/**/tests/` ou `apps/api/src/modules/music-engine/tests/` |
| Componentes visuais | `apps/web/src/components/` e `packages/ui/src/components/` |
| Serviços de API frontend | `apps/web/src/services/` |
| Workers | `apps/api/src/workers/` |
| Validações | `apps/api/src/validators/` e `packages/shared/src/validation/` |
| Contratos e schemas | `packages/shared/src/validation/`, `apps/api/src/routes/` e docs de API |

## Anti-padrões

- Regra musical dentro de componente React.
- Regra musical duplicada no frontend e backend.
- Route HTTP acessando banco sem service/repository quando a lógica crescer.
- Worker recebendo path físico no payload.
- DTO público retornando `storage_key`.
- Testes musicais sem fixtures controladas.
