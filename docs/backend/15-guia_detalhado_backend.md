# Backend — Guia detalhado canônico

Este documento foi reduzido para evitar instruções duplicadas e conflitantes. A implementação do backend deve seguir os documentos canônicos abaixo:

- Visão geral: `docs/backend/01-visao-geral.md`
- Arquitetura API + worker: `docs/backend/02-arquitetura-api-worker.md`
- Contratos de API: `docs/backend/03-endpoints-api.md`
- Modelo de dados: `docs/backend/04-modelagem-banco.md`
- Pipeline assíncrono: `docs/backend/05-pipeline-processamento.md`
- Storage e retenção: `docs/backend/06-storage-e-retencao.md`
- Fila e workers: `docs/backend/07-filas-e-workers.md`
- Segurança backend: `docs/backend/08-seguranca-backend.md`
- Estrutura de pastas: `docs/backend/13-estrutura-pastas.md`
- Testes backend: `docs/backend/14-testes-backend.md`
- Guia Codex: `docs/100-implementacao/guia-codex-app-wflyer.md`

## Regra de uso

Se houver divergência entre este arquivo e os documentos listados acima, prevalecem os documentos canônicos específicos.

## Escopo backend do MVP

- Instrumentos.
- Uploads.
- Transpositions.
- Jobs.
- Artifacts.
- Music engine.
- Security.

## Fora do backend MVP

- Login obrigatório.
- Biblioteca em nuvem.
- Planos pagos.
- Assinatura.
- Dashboard administrativo.
- Compartilhamento público.
- Push notifications.
- Integração Spotify.
