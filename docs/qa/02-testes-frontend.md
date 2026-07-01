# Testes de frontend

## Fluxo mínimo

- Enviar arquivo.
- Selecionar instrumento de origem.
- Selecionar instrumento de destino.
- Confirmar transposição.
- Ver status.
- Ver resultado.
- Baixar artefato.
- Transpor outra partitura.

## Componentes mínimos

- `UploadDropzone`.
- `InstrumentSelector`.
- `TransposeSummary`.
- `ProcessingStatus`.
- `ResultDownloadCard`.
- `ErrorState`.
- `EmptyState`.
- `LocalHistory`.

## Estados mínimos

```text
idle
uploading
uploaded
configuring
queued
processing
completed
failed
expired
```

## Acessibilidade

- Fluxo funciona com teclado.
- Campos possuem labels.
- Status de processamento usa `aria-live`.
- Erros são textuais.
- Botões têm área de toque adequada.
- `prefers-reduced-motion` é respeitado.

## Critérios de aceite

- Usuário completa fluxo feliz.
- Usuário entende erro de arquivo inválido.
- Usuário entende falha de processamento.
- Mobile não quebra layout.
- Teclado alcança todos os controles.
