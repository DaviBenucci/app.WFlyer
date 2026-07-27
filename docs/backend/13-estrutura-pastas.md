# Estrutura de código esperada

> Status: canônico para o início do projeto. Revisão: 2026-07-20.

## Monorepo canônico para a Fase 1

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
      src/wflyer_api/
        api/
        auth/
        capabilities/
        instruments/
        uploads/
        jobs/
        artifacts/
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
    api-client/              cliente TypeScript gerado do OpenAPI
    ui/                      componentes visuais sem regra musical
    config/                  lint/typecheck/tsconfig compartilháveis
    python/
      music-domain/          tipos, IDs e invariantes canônicos
      musicxml/              parsing, normalização e serialização
      instrument-catalog/    perfis e transposições versionadas
      transposition-engine/  transformação determinística
      music-verifier/        verificação independente

  tests/
    fixtures/
      musicxml/
      hostile-files/
      expected/
    e2e/

  docs/
```

## Compartilhamento entre API e worker

API e worker instalam os mesmos pacotes internos de `packages/python/` por meio do workspace `uv`, mas permanecem processos e unidades de implantação separados.

```text
apps/api      ─┐
               ├─> packages/python/*
apps/worker   ─┘
```

O worker não importa a aplicação FastAPI. A API não executa jobs musicais pesados dentro da requisição HTTP.

## Regra musical

A implementação canônica fica em Python nos pacotes internos:

```text
packages/python/music-domain/
packages/python/musicxml/
packages/python/instrument-catalog/
packages/python/transposition-engine/
packages/python/music-verifier/
```

Não colocar a regra canônica em `packages/shared/src/music` nem duplicá-la em TypeScript.

O frontend recebe:

- DTOs OpenAPI gerados;
- intervalo calculado pelo backend;
- labels e exemplos de apresentação;
- Musical Diff produzido pelo backend.

Ele pode calcular uma prévia puramente visual, mas nunca decide o intervalo enviado ao job nem valida o resultado musical.

## Contratos

- OpenAPI da API é a fonte de tipos de rede.
- `packages/api-client` é gerado e não editado manualmente.
- schemas internos Python não são copiados à mão para TypeScript.
- mudanças incompatíveis exigem versão/ADR e testes de contrato.
- o workspace `uv` possui um lockfile compartilhado para API, worker e pacotes Python.

## Separação de responsabilidades

| Local | Responsabilidade |
|---|---|
| `apps/web` | UX, estado de tela, polling, acessibilidade e download. |
| `apps/api` | HTTP, sessão, autorização, persistência e contratos. |
| `apps/worker` | execução assíncrona, sandbox, engines e manutenção. |
| `packages/python/music-domain` | modelo semântico, IDs e invariantes. |
| `packages/python/musicxml` | parser, normalização, serialização e round trip suportado. |
| `packages/python/instrument-catalog` | perfis instrumentais versionados. |
| `packages/python/transposition-engine` | transformação determinística. |
| `packages/python/music-verifier` | reparsing, invariantes e garantia independente. |
| `packages/api-client` | tipos/cliente gerados. |
| `packages/ui` | componentes sem regra musical ou segurança. |
| `tests/fixtures` | corpus versionado e resultados esperados. |

## Anti-padrões

- regra musical em componente React;
- catálogo duplicado/hardcoded no frontend;
- motor musical dentro de `apps/api` e outra cópia no worker;
- worker importando a aplicação HTTP;
- endpoint executando OMR/renderização;
- worker recebendo path ou segredo na mensagem;
- acesso a recurso apenas por UUID, sem `session_id`;
- parser XML permissivo;
- DTO retornando `storage_key` ou engine stderr;
- fixture binária sem licença/origem registradas;
- duas implementações “equivalentes” da transposição em linguagens diferentes.
