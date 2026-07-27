# Evidências — DEC-023

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-024` — Revisão de fornecedores e dados para IA: DPA/termos/região; retenção/treino; redaction/consentimento; kill switch

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
