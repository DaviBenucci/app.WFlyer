# Testes backend do MVP

Este documento resume os testes backend obrigatórios. A matriz completa está em `docs/qa/03-testes-backend.md`.

## Mínimo obrigatório

- `/health` responde.
- Upload válido é aceito.
- Upload inválido é rejeitado.
- Arquivo grande é rejeitado.
- Job é criado.
- Job muda de status.
- Worker processa job.
- Erro no worker não quebra API.
- Download só funciona para artefato válido.
- Arquivo expirado não pode ser baixado.

## Segurança

- Erro não expõe stacktrace.
- Resposta não expõe path físico.
- Resposta não expõe `storage_key`.
- Payload malformado é rejeitado.
- MIME inválido é rejeitado.
