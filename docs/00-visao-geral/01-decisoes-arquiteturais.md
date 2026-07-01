# Decisões arquiteturais principais

## ADR-001 — Projeto novo, orientado por documentação

A nova aplicação `app.WFlyer` deve ser construída a partir desta documentação técnica. Código antigo, protótipos visuais ou documentos conceituais podem servir como referência de produto, mas não definem arquitetura, contratos ou regra musical.

Consequência: antes de codar, o Codex deve ler `README.md`, `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`, `W-Flyer_Regra-Transposição.md` e `docs/100-implementacao/guia-codex-app-wflyer.md`.

## ADR-002 — MVP sem login obrigatório

O MVP deve validar a transposição musical sem exigir autenticação.

Fluxo:

```text
upload -> instrumento de origem -> instrumento de destino -> job assíncrono -> status -> download
```

Login, biblioteca em nuvem, histórico remoto, planos, assinatura e painel administrativo ficam como evolução futura. Nenhum desses itens pode bloquear o MVP.

## ADR-003 — MusicXML-first

O desenvolvimento inicial deve priorizar MusicXML para validar o motor musical com segurança.

```text
Fase 1: MusicXML-first para validar o motor musical.
Fase 2: PDF simples com pipeline de leitura controlado.
Fase 3: PDF real com validação, avisos e revisão assistida.
```

Motivo: MusicXML é estruturado e permite testar notas, acordes, acidentes, armadura e tonalidade escrita com menos incerteza. PDF continua no escopo do produto, mas tem risco maior de leitura.

Consequência: o MVP não deve prometer OMR perfeito nem leitura perfeita de PDF escaneado, manuscrito, torto ou com baixa qualidade.

## ADR-004 — Processamento sempre assíncrono

A API não deve executar leitura musical pesada, transposição ou renderização dentro da requisição HTTP principal.

Fluxo:

```text
API valida entrada
API cria upload/job
API coloca job na fila
Worker processa
Frontend consulta status
Usuário baixa resultado
```

Consequência: qualquer endpoint que criar job deve responder rapidamente com `202 Accepted` e `job_id`.

## ADR-005 — Regra musical centralizada

A fórmula única é:

```text
intervalo_escrito = origem.written_to_concert - destino.written_to_concert
```

Essa regra deve ficar em módulo compartilhado ou motor musical centralizado, nunca duplicada em componentes visuais ou rotas HTTP.

Consequência: não criar `if/else` por par de instrumentos. O catálogo de instrumentos alimenta a fórmula.

## ADR-006 — Arquivos fora do banco, metadados no banco

O banco deve guardar registros, status, eventos e referências internas. Arquivos originais, MusicXML intermediário e artefatos finais devem ficar em storage privado ou pasta controlada pela aplicação.

Consequência: endpoints públicos não retornam `storage_key`, path físico, logs brutos ou detalhes internos do worker.

## ADR-007 — Upload tratado como superfície de risco

Arquivos enviados devem passar por validação de MIME, extensão, tamanho, nome seguro e renomeação interna.

Tipos inicialmente permitidos:

```text
application/pdf
application/vnd.recordare.musicxml+xml
application/xml
text/xml
```

Imagens ficam para fase posterior e não fazem parte do MVP.

## ADR-008 — Frontend orientado ao fluxo de uso

O frontend deve priorizar a ferramenta, não uma landing page.

Fluxo:

```text
UploadDropzone -> InstrumentSelector origem -> InstrumentSelector destino -> TransposeSummary -> ProcessingStatus -> ResultDownloadCard
```

Consequência: a primeira tela útil deve permitir iniciar uma transposição, com estados de loading, erro, vazio, processamento, sucesso e expiração.

## ADR-009 — Futuro separado do MVP

Funcionalidades futuras podem ser documentadas como evolução, mas não podem aparecer como requisito obrigatório do MVP:

- login;
- biblioteca em nuvem;
- planos;
- pagamento;
- dashboard administrativo;
- colaboração;
- compartilhamento público;
- push notifications;
- aplicativo mobile nativo;
- integração Spotify.
