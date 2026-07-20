# Versionamento e revisões musicais

> Status: canônico. Revisão: 2026-07-20.

## Entidades

```text
musical_works
musical_versions
version_edges
musical_reviews
review_decisions
annotations
approvals
```

## musical_versions

```text
id UUID PK
work_id FK
parent_version_id FK NULL
source_artifact_id FK
operation
operation_manifest_id FK
semantic_hash
status
created_by_kind
created_at
```

A versão é imutável. Alterações criam novo nó.

## version_edges

Registra relações além do parent simples:

```text
DERIVED_FROM
TRANSPOSED_FROM
MELODY_EXTRACTED_FROM
HARMONIZED_FROM
ADAPTED_FROM
ARRANGED_FROM
MERGED_FROM
```

## Concurrency

Revisões usam `base_version_id`, `revision` e `If-Match`. Um submit sobre base alterada retorna conflito. Merge automático é proibido para eventos musicais sobrepostos sem regra específica.

## Aprovação

Aprovação inclui:

```text
version_id
semantic_hash
reviewer_id_or_pseudonymous_role
scope
approved_at
revoked_at
```

Nova versão não herda aprovação por padrão.

## Purge

A política pode remover bytes e manter hashes/relacionamentos mínimos. Não preservar conteúdo musical integral disfarçado em JSON de review.
