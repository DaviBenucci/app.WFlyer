# Tela Transpor

## Rota

```text
/transpor
```

## Objetivo

Guiar o usuário pelo fluxo de upload, seleção manual de instrumentos, confirmação, criação de job e processamento.

## Etapas do MVP

```text
1. Upload da partitura.
2. Seleção do instrumento de origem.
3. Seleção do instrumento de destino.
4. Confirmação da transposição.
5. Processamento.
6. Resultado.
```

## Componentes

- `TranspositionWizard`.
- `UploadDropzone`.
- `InstrumentSelector`.
- `TransposeSummary`.
- `ProcessingStatus`.
- `ErrorState`.
- `WizardNavigationActions`.

## Dados externos

```text
GET /api/instruments
POST /api/uploads
POST /api/transpositions
GET /api/jobs/{job_id}/status
GET /api/jobs/{job_id}/artifacts
```

## Validações

- Arquivo obrigatório.
- Tipos permitidos conforme checklist de segurança.
- Origem obrigatória.
- Destino obrigatório.
- Origem e destino podem ser iguais; nesse caso o intervalo esperado é 0.
- Upload com falha não pode criar job.

## Estados

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

## Erros públicos

- Arquivo inválido.
- Arquivo grande demais.
- Instrumento não selecionado.
- Falha ao criar job.
- Tempo de processamento excedido.
- Erro de leitura musical.

## Segurança

- Frontend valida para UX, backend valida de verdade.
- Não expor path local do arquivo.
- Não logar payload sensível.
- Não exibir métricas internas.

## Acessibilidade

- Dropzone acessível por teclado.
- Stepper com etapa atual em texto.
- Erros em região `aria-live`.
- Botões com área de toque adequada.

## Critérios de aceite

- Usuário não processa sem arquivo válido.
- Usuário não processa sem origem e destino.
- Feedback de intervalo aparece antes de confirmar.
- Ao criar job, a UI muda para processamento.
- Polling encerra em `completed`, `failed`, `cancelled` ou `expired`.
