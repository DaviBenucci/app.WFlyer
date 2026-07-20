# Página de pacote para ensemble

> Status: canônico para trilha E. Revisão: 2026-07-20.

## Rota

```text
/ensemble/{version_id}
```

## Objetivo

Configurar formação, validar partes e gerar pacote atômico.

## Composição

```text
EnsembleRoster
RoleAssignmentTimeline
ScorePreview
PartValidationMatrix
PackageOutputs
```

## Estados

```text
formation_empty
analyzing
role_review_required
playability_blocked
parts_ready
rendering_package
package_ready
partial_failure
```

`partial_failure` não libera bundle como concluído; mostra parte afetada e opções de correção.
