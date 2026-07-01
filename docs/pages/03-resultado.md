# Tela Resultado

## Rota

```text
/resultado/{job_id}
```

## Objetivo

Exibir o resultado de um job, listar artefatos disponíveis e permitir download controlado.

## Componentes

- `ResultDownloadCard`.
- `ResultSummary`.
- `ArtifactList`.
- `ProcessingStatus`.
- `ErrorState`.

## Dados necessários

```text
job_id
status
source_instrument_id
target_instrument_id
transpose_interval
artifacts
expires_at
public_error_message
```

## Artefatos esperados

```text
final_musicxml
final_pdf quando renderização PDF estiver disponível
```

## Estados

```text
loading
processing
completed
failed
expired
not_found
artifact_unavailable
```

## Regras

- Só permitir download de artefato válido e não expirado.
- Se o job ainda processa, mostrar status.
- Se expirado, orientar nova transposição.
- Não mostrar métricas internas.
- Não expor path físico ou `storage_key`.

## Mensagem de expiração

```text
Este resultado expirou. Gere uma nova transposição para baixar novamente.
```

## Acessibilidade

- Botões de download indicam formato.
- Avisos são textuais.
- Estados de erro são anunciados.

## Critérios de aceite

- Resultado concluído mostra origem, destino e intervalo.
- Artefatos aparecem apenas quando disponíveis.
- Download de expirado é bloqueado.
- Erros não expõem detalhes internos.
