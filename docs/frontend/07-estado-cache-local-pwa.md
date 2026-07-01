# Estado local e histórico seguro

## Objetivo

Documentar o histórico local mínimo do MVP sem transformar PWA/offline em requisito inicial.

## MVP

O frontend pode manter histórico local com metadados seguros:

```text
job_id
original_filename seguro
source_instrument_id
target_instrument_id
status
created_at
expires_at
completed_at
artifact_types
```

## Não guardar localmente

- Arquivo original.
- MusicXML completo.
- PDF final.
- `storage_key`.
- Stacktrace.
- Logs internos.
- Segredos.

## Fora do MVP

PWA/offline completo fica para fase futura e não deve bloquear a implementação inicial.
