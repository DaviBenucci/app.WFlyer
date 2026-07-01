# Backend — Visão geral

## Objetivo

Definir o backend do MVP `app.WFlyer`: API, banco, módulos de domínio, fila, worker, validações, artefatos e segurança.

O backend é a camada de confiança. Ele valida arquivos, cria uploads e jobs, controla status, executa processamento assíncrono por worker, aplica a regra musical por motor centralizado e entrega artefatos sem expor detalhes internos.

## Módulos esperados

```text
modules/
  instruments/
  uploads/
  transpositions/
  jobs/
  artifacts/
  music-engine/
  security/
```

## Responsabilidades por módulo

### instruments

- Listar instrumentos disponíveis.
- Guardar dados de transposição.
- Validar instrumento ativo.
- Servir catálogo para o frontend.

### uploads

- Receber arquivo.
- Validar tipo.
- Validar tamanho.
- Armazenar referência interna.
- Criar registro de upload.

### transpositions

- Receber origem e destino.
- Criar job de transposição.
- Validar regra musical.
- Iniciar processamento assíncrono.

### jobs

- Controlar status.
- Registrar progresso.
- Registrar falhas.
- Permitir consulta pelo frontend.

### artifacts

- Guardar referência do arquivo gerado.
- Permitir download controlado.
- Bloquear download de artefato expirado ou inválido.

### music-engine

- Aplicar regra musical.
- Manipular MusicXML ou representação musical interna.
- Alterar notas, acordes, acidentes e armadura.
- Validar resultado.

### security

- Padronizar erros públicos.
- Gerar e propagar `correlation_id`.
- Aplicar rate limit.
- Validar payload.
- Evitar vazamento de stacktrace, path físico, segredo ou log bruto.

## Endpoints mínimos do MVP

```text
GET /health
GET /api/instruments
POST /api/uploads
POST /api/transpositions
GET /api/jobs/{job_id}
GET /api/jobs/{job_id}/status
GET /api/jobs/{job_id}/artifacts
GET /api/artifacts/{artifact_id}/download
```

## O que o backend não deve fazer

- Processar transposição pesada dentro da requisição HTTP principal.
- Confiar apenas na validação do frontend.
- Salvar arquivos binários no banco.
- Expor path físico ou `storage_key`.
- Expor stacktrace.
- Expor logs internos.
- Implementar login como dependência do MVP.
- Implementar pagamento, planos, biblioteca em nuvem ou painel administrativo no MVP.
- Integrar Spotify.

## Critérios de aceite

- API base responde.
- Upload válido é aceito.
- Upload inválido é rejeitado.
- Job é criado em estado `queued`.
- Worker altera status.
- Erro no worker não derruba API.
- Artefato válido pode ser baixado.
- Artefato expirado é bloqueado.
- Regra musical vem de módulo centralizado.
- Testes básicos passam.
