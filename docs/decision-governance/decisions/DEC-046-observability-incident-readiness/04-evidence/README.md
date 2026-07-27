# Evidências — DEC-046

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-047` — Teste de observabilidade, alertas e resposta a incidentes: catálogo de SLIs/logs/traces; matriz alerta-owner-runbook; fault injection de API/worker/fila/banco/storage; tabletop de incidente; overhead, cardinalidade, retenção e custo

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
