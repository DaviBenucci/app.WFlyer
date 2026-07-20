# Feature flags e rollout de capacidades musicais

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Impedir que código presente seja interpretado como capacidade aprovada.

## Flags

```text
pdf_omr
mxl_input
pdf_output
melody_extraction
harmonic_analysis
harmonization
playability_analysis
instrument_adaptation
musical_diff
comparative_audio
ensemble_packages
rehearsal_mode
collaborative_review
watermark
signed_manifest
```

## Estados

```text
off
internal
shadow
audit_only
limited_beta
on
kill_switch
```

`shadow` executa sem mostrar resultado ao usuário para medir. `audit_only` produz relatório interno. Nenhum deles autoriza promessa pública.

## Capability response

A API retorna flag, perfil, restrições, versão de política e reason_code. O frontend não usa variável de build isolada como fonte de verdade.

## Rollout

- corpus e gates aprovados;
- migration compatível;
- observabilidade;
- quota;
- cohort explícita;
- rollback/kill switch;
- suporte e runbook;
- revisão de microcopy.

## Drift

Mudança de modelo, solver, catálogo ou perfil pode reduzir a flag para `audit_only` até requalificação.
