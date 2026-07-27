# Alta disponibilidade e falhas

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## API/web

- no mínimo duas tarefas em produção comercial;
- health/readiness;
- load balancer remove instância doente;
- sessão não depende de memória local;
- deploy rolling/blue-green conforme risco.

## Worker

- mensagem volta à fila após visibilidade/lease;
- idempotência impede duplicação;
- reconciler detecta jobs órfãos;
- checkpoint somente quando seguro.

## Banco

- Multi-AZ;
- endpoint gerenciado;
- retry curto com jitter;
- não ocultar transação incerta;
- reconciliação após failover.

## Storage

- upload multipart quando necessário;
- hash;
- confirmação antes de criar job;
- lifecycle;
- versionamento onde fizer sentido;
- acesso privado.

## Modos degradados

- site institucional continua mesmo se app cair;
- status page independente;
- permitir consulta/download quando novos jobs estão pausados;
- fila fiscal pode atrasar sem desativar assinatura paga;
- pagamento confirmado pode aguardar reconciliação fiscal.

## Proibição

Nenhum componente único — VPS, Redis, worker, task ou instância API — pode ser a única cópia do estado autoritativo em produção.
