# Notificações push — fora do MVP

Notificações push não fazem parte do MVP inicial.

## Regra

Não implementar endpoints, permissões, subscriptions ou envio de push nesta etapa.

## Motivo

O MVP deve usar polling em `GET /api/jobs/{job_id}/status` para acompanhar processamento. Isso é suficiente para validar o fluxo assíncrono sem adicionar permissões do navegador nem novos riscos.

## Alternativa do MVP

- Polling com intervalo controlado.
- Mensagens textuais de status.
- `aria-live` para acessibilidade.
