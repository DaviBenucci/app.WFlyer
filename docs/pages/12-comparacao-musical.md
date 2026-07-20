# Página de comparação musical

> Status: canônico para Musical Diff. Revisão: 2026-07-20.

## Rota

```text
/comparar/{source_version_id}/{target_version_id}
```

## Objetivo

Comparar origem e resultado com panes vinculados, filtros e inspector de mudança.

## Shell

`StudioShell` em modo de comparação.

## Estados

```text
loading
complete_diff
partial_diff
no_semantic_changes
creative_changes
expired_source
expired_target
unauthorized
render_unavailable
```

## Ações

- navegar por mudança;
- filtrar;
- ouvir A/B quando habilitado;
- abrir revisão relacionada;
- exportar relatório;
- voltar ao resultado.

## Gate

A página não tenta reconstruir diff no navegador. IDs e categorias vêm da API; panes podem falhar independentemente sem perder relatório textual.
