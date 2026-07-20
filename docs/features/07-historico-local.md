# Histórico local

## Objetivo

Facilitar o retorno a jobs recentes no mesmo navegador sem transformar armazenamento local em autenticação ou biblioteca em nuvem.

## Dados permitidos

```text
job_id
filename sanitizado
source_instrument_id
target_instrument_id
output_interval resumido
status observado
retention_status observado
warnings categóricos
created_at
expires_at
artifact_types
```

Não guardar arquivo, XML, PDF, cookie, CSRF, token de sessão, URL assinada, `storage_key` ou erro interno.

## Propriedade

O acesso real depende do cookie `HttpOnly` da sessão. Um `job_id` no IndexedDB/localStorage não concede acesso. Após limpar cookies, o item pode permanecer localmente, mas deve ser marcado como sessão anterior/inacessível ao receber `401`/`404`.

## Sincronização

- histórico é deste navegador/dispositivo;
- a UI atualiza status consultando a API enquanto autorizado;
- `expires_at` local é indicativo; o servidor decide;
- dados locais podem ser limpos sem apagar servidor;
- purge no servidor deve atualizar/remover disponibilidade local.

## Armazenamento

Preferir IndexedDB para coleção estruturada. Falha, bloqueio ou modo privado não pode impedir o fluxo principal.

## Testes

- adicionar ao criar/concluir job;
- recuperar após refresh com mesma sessão;
- não acessar após troca de sessão;
- limpar local não chama purge automaticamente;
- apagar no servidor invalida downloads;
- aplicação funciona com storage local indisponível.
