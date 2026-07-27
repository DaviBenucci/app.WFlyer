# Evidências — DEC-001

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-001` — Corpus e benchmark OMR: corpus licenciado e estratificado; anotação de notas, durações, acidentes, armaduras, vozes e estrutura; relatório reproduzível por engine/versão
- `EVID-002` — Revisão de licença, sandbox, segurança e custo OMR: licença e distribuição; container sem rede/privilégios; CPU, memória, tempo e custo por página

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
