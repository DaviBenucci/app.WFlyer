# Estrutura de código esperada

> Status: canônico para o início do projeto. Revisão: 2026-07-20.

## Monorepo sugerido

```text
wflyer/
  apps/
    web/
      src/
        app/
        components/
        features/
        services/
        hooks/
        lib/
        tests/

    api/
      src/wflyer/
        api/
        auth/
        capabilities/
        instruments/
        uploads/
        jobs/
        artifacts/
        music/
          model/
          musicxml/
          transpose/
          validate/
        processing/
        storage/
        queue/
        observability/
        security/
        db/
      tests/

    worker/
      src/wflyer_worker/
        tasks/
        processors/
        sandbox/
        maintenance/
      tests/

  packages/
    api-client/        cliente TypeScript gerado a partir do OpenAPI
    ui/                componentes visuais sem regra de domínio
    config/            lint/typecheck/tsconfig compartilháveis

  tests/
    fixtures/
      musicxml/
      hostile-files/
      expected/
    e2e/

  docs/
```

API e worker podem compartilhar o mesmo pacote Python de domínio/infraestrutura por instalação interna, mas devem ser processos implantáveis separadamente.

## Regra musical

A implementação canônica fica em Python no backend:

```text
apps/api/src/wflyer/music/
```

ou em um pacote Python interno extraído quando necessário. Não colocar a regra canônica em `packages/shared/src/music`, pois esse diretório seria TypeScript e criaria duas implementações.

O frontend recebe:

- DTOs OpenAPI gerados;
- intervalo calculado pelo backend;
- labels e exemplos de apresentação.

Ele pode calcular uma prévia puramente visual, mas nunca decide o intervalo enviado ao job nem valida o resultado musical.

## Contratos

- OpenAPI da API é a fonte de tipos de rede.
- `packages/api-client` é gerado e não editado manualmente.
- schemas internos Python não são copiados à mão para TypeScript.
- mudanças incompatíveis exigem versão/ADR e testes de contrato.

## Separação de responsabilidades

| Local | Responsabilidade |
|---|---|
| `apps/web` | UX, estado de tela, polling, acessibilidade e download. |
| `apps/api` | HTTP, sessão, autorização, domínio, persistência e contratos. |
| `apps/worker` | execução assíncrona, sandbox, engines e manutenção. |
| `packages/api-client` | tipos/cliente gerados. |
| `packages/ui` | componentes sem regra musical ou segurança. |
| `tests/fixtures` | corpus versionado e resultados esperados. |

## Anti-padrões

- regra musical em componente React;
- catálogo duplicado/hardcoded no frontend;
- endpoint executando OMR/renderização;
- worker recebendo path ou segredo na mensagem;
- acesso a recurso apenas por UUID, sem `session_id`;
- parser XML permissivo;
- DTO retornando `storage_key` ou engine stderr;
- fixture binária sem licença/origem registradas;
- duas implementações “equivalentes” da transposição em linguagens diferentes.
