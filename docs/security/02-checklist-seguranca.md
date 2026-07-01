# Checklist de segurança do MVP

## Upload

- [ ] Validar MIME real.
- [ ] Validar extensão.
- [ ] Validar tamanho máximo.
- [ ] Rejeitar arquivo vazio.
- [ ] Renomear arquivo internamente.
- [ ] Não confiar no nome original.
- [ ] Não usar filename em path interno.
- [ ] Não expor arquivo diretamente.
- [ ] Sanitizar metadados visíveis ao usuário.

Tipos inicialmente permitidos:

```text
application/pdf
application/vnd.recordare.musicxml+xml
application/xml
text/xml
```

Tipos de imagem ficam para fase posterior:

```text
image/png
image/jpeg
```

## API

- [ ] Validar payload.
- [ ] Padronizar erro com `{ "error": ... }`.
- [ ] Não expor stacktrace.
- [ ] Não expor path físico.
- [ ] Não expor logs internos.
- [ ] Não expor segredos.
- [ ] Não retornar `storage_key`.
- [ ] Aplicar rate limit em upload, criação de job e download.
- [ ] Usar `correlation_id` em erros e logs.
- [ ] Definir timeout para processamento.
- [ ] Sanitizar inputs textuais.

## Frontend

- [ ] Não salvar segredos.
- [ ] Não logar payload completo com tokens.
- [ ] Não exibir erro técnico bruto.
- [ ] Não depender apenas da validação local.
- [ ] Não construir URL interna de arquivo.
- [ ] Validar schemas de resposta.

## Worker

- [ ] Processar fora da requisição HTTP.
- [ ] Usar timeout por etapa.
- [ ] Usar diretório temporário isolado quando houver arquivo físico.
- [ ] Evitar subprocess com `shell=True`.
- [ ] Registrar falha com `correlation_id`.
- [ ] Converter erro interno em mensagem pública segura.

## Artefatos

- [ ] Download controlado pela API ou URL temporária documentada.
- [ ] Bloquear artefato expirado.
- [ ] Não expor path físico.
- [ ] Não expor chave interna.
- [ ] Validar associação entre job e artefato.

## CORS futuro

- [ ] Quando houver frontend em origem separada, permitir apenas origens explícitas.
- [ ] Não usar wildcard junto com credenciais.
- [ ] Documentar mudanças de CORS antes de implementar.

## Testes de segurança

- [ ] Não expor stacktrace.
- [ ] Não expor caminho interno do arquivo.
- [ ] Não aceitar extensão perigosa.
- [ ] Não aceitar MIME inválido.
- [ ] Não aceitar payload malformado.
- [ ] Rate limit documentado.
- [ ] Validações documentadas.
