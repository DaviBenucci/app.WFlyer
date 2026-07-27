# Evidências — DEC-019

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-016` — Fontes e revisão dos perfis instrumentais: transposição/ranges/tessitura; polifonia/técnicas; revisor por instrumento; fixtures.
- `EVID-020` — Avaliação de tocabilidade por instrumento: níveis e andamento; respiração/span/registros; severidade e discordância.

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
