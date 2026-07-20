# Orquestração de análises musicais avançadas

> Status: canônico para trilhas L, H, A, D e E. Revisão: 2026-07-20.

## Princípio

Operações avançadas são DAGs de etapas versionadas, não uma função monolítica. Cada etapa declara entradas, saídas, invariantes, custo, retry e dependências.

## Grafo orientativo

```text
normalize
├── structural_analysis
├── playback_graph
├── instrument_profile_snapshot
└── semantic_event_graph

structural_analysis -> melody_candidates -> melody_review -> confirmed_melody
confirmed_melody + harmonic_analysis -> harmony_variants
confirmed_version + instrument_profile -> playability -> adaptation_options
confirmed_score + ensemble_profile -> arrangement -> parts -> package
semantic_event_graph + target_version -> musical_diff
playback_graph + version -> audio_render -> playback_map
```

## Step contract

```ts
type PipelineStepManifest = {
  step_name: string
  step_version: string
  input_artifact_hashes: string[]
  output_artifact_hashes: string[]
  policy_versions: Record<string, string>
  deterministic: boolean
  random_seed?: string
  started_at: string
  finished_at: string
  check_results: string[]
}
```

## Reuso

Uma etapa pode reutilizar cache somente quando todos os hashes e versões de dependência coincidem. Cache nunca é indexado apenas por filename ou job_id.

## Falhas

- falha determinística: não retry;
- dependência indisponível: retry limitado;
- review required: pausa DAG;
- policy/model changed: invalidar downstream;
- fonte purgada: cancelar e não reconstruir de metadado parcial;
- resultado parcial: artefato interno, nunca público.

## Filas

Separar filas por perfil de recurso:

```text
core_musicxml
omr_cpu
analysis_cpu
solver_cpu
audio_render
score_render
package_io
```

Quotas e circuit breakers impedem que harmonização ou OMR bloqueiem transposição Core.
