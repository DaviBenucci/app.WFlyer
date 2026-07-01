# Storage e retenção

## Objetivo

Guardar arquivos fora do banco, com isolamento, nomes internos seguros e expiração controlada.

## Regras

- O banco guarda metadados.
- Arquivos ficam em storage controlado pela aplicação.
- `storage_key` é interno.
- Filename original nunca define path.
- Download público não expõe path físico.
- Artefatos expirados não podem ser baixados.

## Organização interna sugerida

```text
uploads/{upload_id}/{uuid}.musicxml
uploads/{upload_id}/{uuid}.pdf
jobs/{job_id}/intermediate/{uuid}.musicxml
jobs/{job_id}/artifacts/{artifact_id}.musicxml
jobs/{job_id}/artifacts/{artifact_id}.pdf
```

## Retenção

Regra inicial:

```text
Arquivos originais e artefatos finais expiram após 15 dias.
```

Ao expirar:

- marcar `uploads.status` ou `processing_jobs.status` como `expired` quando aplicável;
- bloquear download;
- registrar evento em `job_events`;
- remover referência física quando o mecanismo de limpeza existir.

## Segurança

- Não salvar arquivo em pasta pública.
- Não usar nome original como path.
- Não retornar `storage_key`.
- Não retornar path local.
- Não logar conteúdo do arquivo.
- Sanitizar metadados visíveis ao usuário.

## Testes

- Artefato válido pode ser baixado.
- Artefato expirado é bloqueado.
- `storage_key` não aparece em resposta pública.
- Nome original malicioso não altera path interno.
