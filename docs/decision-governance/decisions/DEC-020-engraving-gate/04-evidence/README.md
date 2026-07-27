# Evidências — DEC-020

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-021` — Gate de legibilidade e engraving: colisões; viradas/densidade; tela/impressão; watermark
- `EVID-003` — Benchmark de renderer e engraving: golden MusicXML/PDF; detector de colisões; impressão e dispositivos; licença/fontes/performance

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
