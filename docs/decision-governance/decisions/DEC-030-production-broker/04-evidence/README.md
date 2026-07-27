# Evidências — DEC-030

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-031` — Fault injection e custo do broker: duplicata/crash/ACK/timeout; DLQ/backpressure/prioridade; durabilidade/custo/operação

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
