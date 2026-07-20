# Backend — visão geral

> Status: canônico. Revisão: 2026-07-20.

## Responsabilidade

O backend é a camada de confiança do W_Flyer. Ele autoriza o acesso por sessão anônima, valida arquivos, persiste o estado, agenda jobs, executa o motor musical em workers e entrega artefatos privados.

## Módulos

```text
sessions
capabilities
instruments
uploads
transpositions
jobs
artifacts
music_engine
omr
rendering
storage
security
observability
```

## Limites de responsabilidade

### API

- contratos HTTP e OpenAPI;
- criação/validação de sessão;
- autorização por objeto;
- validação de payload;
- upload em quarentena;
- criação idempotente de job;
- consulta de estado;
- download e exclusão controlados.

### Worker

- parsing e normalização MusicXML;
- rasterização/OMR quando habilitado;
- transposição;
- validação semântica;
- renderização quando habilitada;
- gravação atômica de artefatos;
- atualização de status, stage, attempts e eventos.

### Banco

Fonte de verdade para sessão, propriedade, jobs, estágios, retenção, artefatos, attempts e eventos.

### Storage

Bytes privados e imutáveis. O banco guarda referências e hashes.

## Regra musical

O motor canônico fica em Python, por exemplo:

```text
apps/api/src/wflyer/music/
```

O frontend não executa uma cópia autoritativa do algoritmo.

## Contratos mínimos

- `POST /api/v1/sessions/anonymous`;
- `GET /api/v1/capabilities`;
- `GET /api/v1/instruments`;
- `POST /api/v1/uploads`;
- `POST /api/v1/transpositions`;
- `GET /api/v1/jobs/{job_id}`;
- `GET /api/v1/jobs/{job_id}/status`;
- `GET /api/v1/jobs/{job_id}/artifacts`;
- `GET /api/v1/artifacts/{artifact_id}/download`;
- `DELETE /api/v1/jobs/{job_id}`.

## Proibições

- processamento musical pesado na request;
- autorização baseada apenas em UUID;
- binário no banco;
- path ou `storage_key` em DTO;
- parser XML com rede/entidades externas;
- subprocesso no processo da API;
- regra musical em React/TypeScript;
- aceitar PDF quando `pdf_omr=false`;
- declarar sucesso sem validar invariantes.

## Camada de inteligência musical

Módulos adicionais, ativados por capability:

```text
score_analysis
melody_extraction
monophonic_reduction
harmony_planning
instrument_adaptation
assurance
provenance
watermarking
```

O domínio recebe uma `operation` explícita. `transpositions` não deve se tornar um módulo genérico que descarta ou cria notas sem contrato.

## Regra de confiança

Toda saída passa por `assurance`, que reparsa fonte e resultado, avalia invariantes e produz `assurance_report`. O worker transformador não autoaprova o próprio resultado.
