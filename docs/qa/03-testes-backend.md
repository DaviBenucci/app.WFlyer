# Testes de backend

## Endpoints

- `GET /health` responde.
- `GET /api/instruments` lista catálogo ativo.
- `POST /api/uploads` aceita arquivo válido.
- `POST /api/uploads` rejeita MIME inválido.
- `POST /api/uploads` rejeita arquivo grande.
- `POST /api/transpositions` cria job.
- `GET /api/jobs/{job_id}` retorna job público.
- `GET /api/jobs/{job_id}/status` retorna status leve.
- `GET /api/jobs/{job_id}/artifacts` lista artefatos do job.
- `GET /api/artifacts/{artifact_id}/download` baixa artefato válido.

## Jobs e worker

- Job começa em `queued`.
- Worker muda status para `processing`.
- Worker muda status para `transposing`.
- Worker conclui como `completed`.
- Erro do worker vira `failed`.
- Erro do worker não derruba API.
- Retentativa é limitada.
- Timeout vira erro público seguro.

## Segurança

- DTO público não retorna `storage_key`.
- DTO público não retorna path físico.
- Erro público não contém stacktrace.
- Payload malformado é rejeitado.
- Instrumento inexistente é rejeitado.
- Upload expirado não cria job.

## Artefatos

- Artefato válido baixa.
- Artefato inexistente retorna erro seguro.
- Artefato expirado é bloqueado.
- Job não concluído não lista resultado final como disponível.
