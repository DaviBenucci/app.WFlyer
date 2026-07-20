# Pipeline de processamento

> Status: canônico. Revisão: 2026-07-20.

## Princípio

A API recebe, autoriza e agenda. O worker processa. Nenhuma leitura musical, transposição, OMR ou renderização pesada ocorre dentro da requisição HTTP.

## Entrada do pipeline

Um job só pode ser criado quando:

- a sessão é válida e proprietária do upload;
- o upload está `validated`;
- o formato está habilitado em `/api/v1/capabilities`;
- origem e destino existem e estão ativos;
- o arquivo está dentro do perfil de suporte;
- a chave de idempotência é válida.

A criação do job e do evento de outbox ocorre na mesma transação de banco.

## Pipeline Core — MusicXML

```text
queued
-> preprocessing
-> normalizing
-> transposing
-> validating
-> rendering (somente se solicitado e habilitado)
-> finalizing
-> completed | completed_with_warnings
```

| Stage | Entrada | Saída mínima | Falhas típicas |
|---|---|---|---|
| `preprocessing` | upload validado | cópia de trabalho e hash confirmado | `UPLOAD_NOT_AVAILABLE`, `UPLOAD_EXPIRED`, `FILE_INTEGRITY_FAILED` |
| `normalizing` | MusicXML de entrada | `normalized_musicxml` | `MUSICXML_PARSE_FAILED`, `UNSUPPORTED_SCORE_STRUCTURE` |
| `transposing` | MusicXML normalizado e snapshots dos instrumentos | `transposed_musicxml` provisório | `SOURCE_INSTRUMENT_MISMATCH`, `TRANSPOSITION_FAILED` |
| `validating` | resultado provisório | relatório de invariantes | `INVALID_MUSICAL_DOCUMENT` para entrada inconsistente; `SEMANTIC_VALIDATION_FAILED` para saída do motor inválida |
| `rendering` | resultado validado | `rendered_pdf` provisório | `RENDERER_UNAVAILABLE`, `RENDER_FAILED` |
| `finalizing` | artefatos provisórios | artefatos públicos gravados de forma atômica | `ARTIFACT_STORAGE_FAILED` |

`rendering` é pulado quando PDF de saída não está habilitado. MusicXML transposto é o resultado obrigatório do Core.

## Extensão PDF/OMR

Quando `pdf_omr=true`, o pipeline insere etapas antes da normalização:

```text
preprocessing
-> recognizing
-> raw_musicxml
-> normalizing
-> pipeline Core
```

A especificação completa está em `../music/04-pipeline-omr.md`. Não existe caminho alternativo que transpõe pixels ou altera diretamente o PDF.

## Regras de consistência

- O original é imutável.
- Cada tentativa possui diretório temporário exclusivo.
- O job usa snapshots dos presets de instrumento; mudanças posteriores no catálogo não alteram o resultado.
- A entrada é lida novamente do storage e conferida por hash antes do processamento.
- O MusicXML normalizado e o transposto são artefatos distintos.
- Um retry não pode publicar artefatos públicos duplicados.
- Artefatos provisórios só se tornam públicos após validação e commit de metadados.
- Falha ou cancelamento remove arquivos temporários, mas preserva o registro mínimo de diagnóstico conforme retenção.
- `progress_pct` é calculado pelo servidor, é monotônico e nunca substitui `status`/`stage`.

## Warnings e falhas

Warnings categóricos só permitem `completed_with_warnings` quando nenhum invariante obrigatório foi violado. Exemplos:

```text
ENHARMONIC_SIMPLIFICATION
TARGET_CLEF_REVIEW_RECOMMENDED
OUT_OF_RECOMMENDED_RANGE
LAYOUT_MAY_DIFFER
OMR_REVIEW_RECOMMENDED
```

Altura de concerto incorreta, ritmo alterado, estrutura fora do perfil, corrupção de artefato ou origem incompatível resultam em `failed`.

## Cancelamento

- `DELETE /api/v1/jobs/{job_id}` em job ativo define `cancel_requested`.
- O worker verifica cancelamento entre stages e antes de publicar artefatos.
- Processo externo deve receber término gracioso e, após prazo curto, encerramento forçado.
- Cancelamento não pode produzir artefato público parcial.

## Evidências do processamento

Cada tentativa registra:

```text
job_id e attempt_number
engine manifest e versões
hashes de entrada e saída
duração por stage
warnings e erro categorizado
resultado dos invariantes
correlation_id
```

Esses dados são internos, salvo os campos explicitamente allowlisted nos DTOs públicos.

## Orquestração por operação

Após normalização, o pipeline escolhe um ramo tipado:

```text
TRANSPOSE
-> transpose -> independent_validate

EXTRACT_MELODY
-> analyze -> select_candidates
-> [awaiting_user_input quando ambíguo]
-> reduce -> optional_transpose -> independent_validate

HARMONIZE
-> confirm_melody -> analyze_harmony
-> generate_variants -> validate_constraints
-> awaiting_user_input
-> publish_selected_variant
```

Renderização final:

```text
validated MusicXML
-> render
-> plan watermark safe zones
-> apply distributed watermark
-> hash + sign manifest
-> verify rendered artifact
-> publish atomically
```

Nenhum ramo pode marcar `completed` antes do `assurance_report`. A falha de watermark/assinatura impede publicar o PDF, mas pode permitir MusicXML quando esse formato foi solicitado e sua própria validação passou.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## DAG de processamento avançado

A evolução não deve formar uma função monolítica. O orquestrador monta um DAG por operação:

```text
ingest
-> parse seguro
-> normalizar
-> construir grafo semântico
-> analisar estrutura
-> [revisão de origem, se necessária]
-> executar operação
-> verificar invariantes
-> avaliar destino/tocabilidade
-> gerar provenance/diff
-> renderizar/gerar áudio, quando habilitado
-> validar artefatos derivados
-> publicar atomicamente
```

Nós de análise podem produzir `NEEDS_REVIEW`; não devem escolher silenciosamente para manter o pipeline andando.

## Fronteiras de falha

- erro estrutural: não retry;
- ambiguidade musical: revisão, não retry;
- ausência de perfil: capability/erro, não best effort;
- timeout externo transitório: retry limitado;
- output inválido de modelo/solver: descartar candidato e registrar métrica;
- falha de renderer/áudio: não invalida revisão semântica, mas impede artefato correspondente;
- falha de publicação: artefato continua privado até reconciliação.

## Cache e reprodutibilidade

A chave de cache inclui hash da revisão, operação, parâmetros, versões de catálogo/política/engine/modelo/renderer e seed quando aplicável. Não reutilizar resultado entre versões diferentes apenas porque o arquivo de entrada é igual.
