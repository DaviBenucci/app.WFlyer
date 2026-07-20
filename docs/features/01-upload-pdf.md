# Upload de partitura

> O nome histórico do arquivo contém “pdf”, mas o Core aceita MusicXML. PDF permanece sob feature gate.

## Objetivo

Receber uma partitura, validar o formato ativo e criar um upload pertencente à sessão anônima.

## Fonte de formatos

A UI consulta `GET /api/v1/capabilities`. No Core:

```text
.musicxml                       habilitado
.xml que seja MusicXML válido   habilitado
.mxl                            desabilitado
.pdf                            desabilitado até gate OMR
.png/.jpg                       fora do MVP
```

Não hardcodar PDF como permitido. Quando `pdf_omr=false`, a UI não oferece PDF e a API retorna `FORMAT_NOT_ENABLED`.

## Fluxo

```text
criar/renovar sessão anônima
-> consultar capabilities
-> selecionar arquivo
-> validação local apenas para feedback
-> POST /api/v1/uploads com CSRF
-> backend faz streaming para quarentena
-> valida bytes, tipo e estrutura segura
-> retorna upload validated ou erro
```

## UI

- informar formatos e limite retornados/configurados;
- permitir teclado e botão alternativo à dropzone;
- mostrar filename sanitizado e tamanho;
- não prometer que extensão válida implica partitura válida;
- permitir remover upload ainda não associado a job.

Estados locais de UI:

```text
idle | selecting | uploading | validating | ready | error
```

Estados persistidos do upload estão em `../backend/16-maquina-estados.md`.

## Segurança

- `file.type` e extensão são apenas indícios;
- backend limita bytes durante o streaming;
- filename original não vira path;
- XML usa parser seguro;
- arquivo rejeitado nunca entra no pipeline;
- frontend não lê nem armazena o conteúdo permanentemente;
- sessão/CSRF são obrigatórios.

## Critérios de aceite

- formatos exibidos refletem capabilities;
- MusicXML suportado cria upload `validated`;
- XML genérico não MusicXML é rejeitado;
- PDF/MXL desabilitados não são aceitos nem apenas ocultados;
- arquivo vazio, excessivo, malformado ou hostil é rejeitado;
- resposta e log não expõem path/`storage_key`;
- recurso de outra sessão não pode ser consultado ou apagado.
