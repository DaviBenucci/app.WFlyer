# Resultado e download

## Objetivo

Disponibilizar artefatos finais com segurança e expiração controlada.

## Artefatos

```text
final_musicxml
final_pdf quando renderização PDF estiver disponível
```

## Download seguro

- Endpoint valida artefato.
- Endpoint valida status do job.
- Endpoint bloqueia expirado.
- Filename de resposta é sanitizado.
- Path interno não aparece.
- `storage_key` não aparece.

## Estados

```text
completed
artifact_missing
expired
failed
```

## Retenção

Arquivos originais e artefatos finais expiram após 15 dias no armazenamento controlado pela aplicação.

## Critérios de aceite

- Usuário baixa apenas artefatos válidos.
- Artefato expirado é bloqueado.
- Erro de download não expõe path interno.
- Histórico local guarda apenas metadados seguros.
