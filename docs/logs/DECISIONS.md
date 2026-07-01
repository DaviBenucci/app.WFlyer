# Decisions Log

## ADR-001 — Projeto novo orientado por documentação

Status: ACEITA

Decisão: construir a aplicação a partir da documentação técnica atual, sem reaproveitar código antigo como base.

## ADR-002 — MVP sem login obrigatório

Status: ACEITA

Decisão: validar a transposição musical sem exigir autenticação.

## ADR-003 — MusicXML-first

Status: ACEITA

Decisão: iniciar pelo motor musical com MusicXML controlado, depois evoluir para PDF simples e só então PDF real com validação e avisos.

## ADR-004 — Processamento assíncrono

Status: ACEITA

Decisão: API cria job e worker processa fora da requisição HTTP principal.

## ADR-005 — Regra musical centralizada

Status: ACEITA

Decisão: usar a fórmula única `intervalo_escrito = origem.written_to_concert - destino.written_to_concert`.

## ADR-006 — Arquivos fora do banco

Status: ACEITA

Decisão: banco guarda metadados e referências internas; arquivos ficam em armazenamento controlado pela aplicação.

## ADR-007 — Escopo futuro separado

Status: ACEITA

Decisão: login, biblioteca em nuvem, planos, painel administrativo, compartilhamento, push, aplicativo nativo e Spotify ficam fora do MVP inicial.
