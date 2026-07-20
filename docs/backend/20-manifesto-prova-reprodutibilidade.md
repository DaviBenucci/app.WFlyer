# Manifesto de prova, auditoria e reprodutibilidade

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Permitir demonstrar como um resultado foi produzido sem expor dados internos sensíveis nem depender de confiança cega na interface.

## `processing_manifest`

Manifesto interno completo:

```json
{
  "schema_version": "1.0",
  "job_id": "uuid",
  "operation": "TRANSPOSE",
  "input_sha256": "...",
  "normalized_sha256": "...",
  "output_sha256": "...",
  "source_instrument_snapshot": {},
  "target_instrument_snapshot": {},
  "operation_parameters": {},
  "engine_versions": {},
  "policy_versions": {},
  "random_seed": null,
  "invariants": [],
  "event_mapping_summary": {},
  "warnings": [],
  "watermark_token_hash": null,
  "created_at": "2026-07-20T12:00:00Z"
}
```

## `assurance_report`

Relatório público allowlisted:

```json
{
  "assurance_level": "TRANSFORMATION_VERIFIED",
  "operation": "TRANSPOSE",
  "source_confirmed": true,
  "checks": [
    "concert_pitch_preserved",
    "rhythm_preserved",
    "measure_structure_preserved",
    "target_range_checked"
  ],
  "warnings": [],
  "verification_token": "WF-7K3D-9Q2M"
}
```

Não incluir score bruto de modelo, paths, stacktrace, nomes de containers ou segredos.

## Mapeamento de eventos

Para transposição e redução, o backend mantém tabela/artefato de mapeamento:

```text
source_event_id
output_event_id
operation
pitch_before
pitch_after
onset_before/after
duration_before/after
reason_code
```

Harmonização inclui `generated_event_id`, acorde/função, voz, regra/modelo e eventos melódicos condicionantes.

## Assinatura e verificação

O hash do manifesto e dos artefatos públicos pode ser assinado com chave de serviço em KMS/HSM. A verificação deve confirmar:

- assinatura válida;
- hash do arquivo baixado;
- job e versão do manifesto;
- status de revogação/expiração quando aplicável.

A chave privada nunca entra no worker genérico nem em imagem de frontend.

## Endpoint futuro

```text
GET /api/v1/verifications/{verification_token}
```

Retorna somente informações não sensíveis: produto, hash do artefato apresentado, data, tipo de operação, nível de garantia e validade da assinatura. Token não concede download nem acesso ao job.

## Retenção

O usuário pode apagar os bytes da partitura. Após purge, o sistema pode manter somente o mínimo necessário para prova antifraude, conforme política de privacidade: hashes, token pseudônimo, versão, data e status. Não manter título, nome do arquivo ou conteúdo musical sem base aprovada.

## Alterações de engine

Mudança de parser, catálogo, política de enarmonia, modelo de melodia, harmonizador ou renderer cria nova versão. Reprocessar um arquivo com versão nova gera outro manifesto; nunca substituir a prova anterior.

## Dependências adicionais do manifesto

Para operações avançadas, registrar também:

```text
canonical_score_graph_hash
parent_revision_hash
instrument_profile_version
analysis_policy_version
melody_model_or_solver_version
harmony_policy_version
adaptation_budget_version
playability_rule_set_version
playback_manifest_version
engraving_profile_version
watermark_policy_version
feature_flag_snapshot
applicable_pm_ids
mdr_ids
human_review_decision_ids
```

Uma variante não determinística é reproduzível apenas no sentido de artefato preservado: mesmos bytes, inputs, parâmetros e manifest. Não se deve prometer regeneração idêntica se o provedor não a garante.
