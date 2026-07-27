# Arquitetura de domínio e entrada de tráfego

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## Site

```text
wflyer.com.br
→ DNS
→ CDN/hosting do site
```

## Aplicação

```text
app.wflyer.com.br
→ DNS Alias/CNAME
→ CloudFront/WAF
→ behaviors
   /            → Next.js
   /api/*       → FastAPI/ALB
   /downloads/* → URLs autorizadas ou endpoint
```

## Benefícios de mesmo host para web/API

- cookies same-site;
- menos CORS;
- CSRF mais simples;
- um certificado público;
- interface estável mesmo com origins internos diferentes.

## Status

`status.wflyer.com.br` deve ser hospedado fora da mesma cadeia principal, para continuar informando incidentes quando a AWS ou o app estiverem indisponíveis.

## Migração

- baixar TTL antes;
- validar certificado;
- usar ambiente de staging;
- health check;
- alterar DNS;
- monitorar;
- manter rollback durante janela definida.
