# Frontend — Guia detalhado do MVP

## Objetivo

Construir uma ferramenta de transposição musical, não uma landing page. A primeira experiência útil deve levar o usuário ao fluxo de upload, seleção de instrumentos, processamento, resultado e download.

## Fluxo principal

```text
1. Tela inicial da aplicação.
2. Upload da partitura.
3. Seleção do instrumento de origem.
4. Seleção do instrumento de destino.
5. Confirmação da transposição.
6. Tela de processamento.
7. Tela de resultado.
8. Download.
9. Transpor outra partitura.
```

## Componentes mínimos

```text
UploadDropzone
InstrumentSelector
TransposeSummary
ProcessingStatus
ResultDownloadCard
ErrorState
EmptyState
LocalHistory
```

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

## Serviços de API

```text
services/
  apiClient
  instrumentsService
  uploadsService
  transpositionsService
  jobsService
  artifactsService
```

O frontend deve consumir os contratos de `docs/backend/03-endpoints-api.md`.

## Regras de UX

- Loading real.
- Feedback de progresso.
- Mensagens de erro claras.
- Interface responsiva.
- Uso adequado em mobile.
- Botões grandes.
- Labels compreensíveis.
- Acessibilidade.
- Não usar animações que prejudiquem a clareza.

## Segurança no frontend

- Não confiar apenas na validação local.
- Não expor stacktrace.
- Não logar tokens ou payloads sensíveis.
- Não construir path de arquivo.
- Não guardar arquivo original no histórico local.
- Validar resposta da API por schema.

## Fora do MVP frontend

- Login.
- Biblioteca em nuvem.
- Planos pagos.
- Assinatura.
- Dashboard administrativo.
- Compartilhamento público.
- Editor visual completo de partitura.
- Aplicativo mobile nativo.
- Integração Spotify.

## Critérios de aceite

- Usuário consegue enviar arquivo.
- Usuário consegue selecionar instrumento de origem.
- Usuário consegue selecionar instrumento de destino.
- Usuário vê status de processamento.
- Usuário vê erro amigável.
- Usuário consegue baixar resultado.
- Fluxo funciona em mobile.
- Fluxo funciona com teclado.
