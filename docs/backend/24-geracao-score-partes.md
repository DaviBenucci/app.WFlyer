# Geração de score, partes e pacote

> Status: canônico para trilha E. Revisão: 2026-07-20.

## Arquitetura

```text
CanonicalScoreGraph
-> PartProjectionBuilder
-> WrittenPitchTransformer
-> PartLayoutPlanner
-> RendererAdapter
-> ScorePartConsistencyValidator
-> PackageBuilder
```

## Regra

Partes são projeções determinísticas após o arranjo confirmado. O renderer não decide conteúdo musical.

## Package transaction

1. criar package version;
2. gerar todas as projeções;
3. validar consistência;
4. renderizar;
5. validar PDFs;
6. aplicar watermark quando habilitado;
7. assinar manifest;
8. publicar todos os artefatos atomically.

Se uma parte falhar, o package permanece interno/failed.

## ZIP

Bundle comprimido só é habilitado com proteção contra path traversal, limites, nomes sanitizados e manifest externo/interno consistente.

## Regeração

Mudança de layout pode regenerar somente artefatos editoriais. Mudança de evento/instrumento invalida projeção semântica e downstream.
