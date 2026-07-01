# Segurança do backend

## Objetivo

Proteger upload, jobs, artefatos, erros públicos e logs sem adicionar login como dependência do MVP.

## Regras obrigatórias

- Validar MIME real.
- Validar extensão.
- Limitar tamanho.
- Renomear arquivo internamente.
- Não confiar no nome original.
- Não expor arquivo diretamente.
- Não expor stacktrace.
- Não expor logs internos.
- Não salvar segredos no frontend.
- Aplicar rate limit.
- Definir timeout de processamento.
- Sanitizar inputs.
- Validar payload.
- Usar `correlation_id` em logs.
- Retornar mensagens amigáveis.

## Erro público

```json
{
  "error": {
    "code": "INVALID_FILE_TYPE",
    "message": "O arquivo enviado não é uma partitura válida.",
    "correlation_id": "req_123"
  }
}
```

## Proibido no DTO público

```text
stacktrace
storage_key
storage_path
raw_log
worker_exception
secret
token_hash
filesystem_path
```

## Upload

Tipos permitidos no início:

```text
application/pdf
application/vnd.recordare.musicxml+xml
application/xml
text/xml
```

Imagens podem ser avaliadas futuramente, mas não entram no MVP inicial.

## Worker

- Falha do worker não pode derrubar a API.
- Erros internos devem virar `error_code` e mensagem pública segura.
- Retentativas devem ser limitadas.
- Timeout deve marcar job como `failed`.

## Download

- Artefato expirado deve ser bloqueado.
- Download deve validar artefato e job.
- Resposta nunca pode revelar path físico ou chave interna.
