# Evidências — DEC-004

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-005` — Relatório quantitativo de habilitação PDF: thresholds pré-registrados; métricas estratificadas; false verified rate e review rate
- `EVID-001` — Corpus e benchmark OMR: corpus licenciado e estratificado; anotação de notas, durações, acidentes, armaduras, vozes e estrutura; relatório reproduzível por engine/versão

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
