# Evidências — DEC-045

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-046` — Exercícios de backup, restore e disaster recovery: inventário de dados e dependências; restore PostgreSQL/PITR com integridade e tempo; restore S3/objetos/manifests com hashes; simulação regional por IaC; comparação RPO/RTO e plano de correção

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
