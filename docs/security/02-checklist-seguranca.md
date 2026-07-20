# Checklist de segurança do Core

## Sessão e autorização

- [ ] Token opaco com entropia adequada; apenas hash persistido.
- [ ] Cookie `HttpOnly`, `Secure`, `SameSite=Lax`, path restrito.
- [ ] CSRF obrigatório em toda mutação.
- [ ] Toda consulta de objeto inclui `session_id`.
- [ ] Objeto de outra sessão retorna `404`.
- [ ] Cookie/CSRF não aparecem em URL, JS storage, log ou analytics.
- [ ] CORS allowlist quando origens forem separadas.

## Upload

- [ ] Formato vem de capability ativa.
- [ ] Limite aplicado durante streaming.
- [ ] Arquivo vazio e excesso rejeitados cedo.
- [ ] Extensão, MIME reportado, MIME detectado e assinatura comparados.
- [ ] Nome interno independente do filename.
- [ ] Quarentena antes de parsing/aprovação.
- [ ] SHA-256/tamanho registrados e conferidos.
- [ ] Arquivo rejeitado não cria job.

Core permitido:

```text
application/vnd.recordare.musicxml+xml
application/xml ou text/xml somente após validar que é MusicXML
```

PDF e MXL ficam desabilitados até os gates específicos.

## XML/MusicXML

- [ ] Entidades externas, DTD externo, XInclude e rede desabilitados.
- [ ] Sem modo de recuperação silenciosa.
- [ ] Limites de bytes, profundidade, nós, texto, medidas, vozes e eventos.
- [ ] Raiz/namespace/versão/perfil validados.
- [ ] Schema/catálogo local; sem fetch remoto.
- [ ] Saída transposta é parseada/validada novamente.

## Fila/worker/sandbox

- [ ] Payload contém apenas IDs/correlation ID.
- [ ] Tarefa idempotente e reentrega testada.
- [ ] Timeouts, memória, CPU, PIDs e disco limitados.
- [ ] Subprocesso sem `shell=True` e sem argumento não validado.
- [ ] Usuário não root, sem rede, root fs read-only.
- [ ] Diretório temporário exclusivo e limpeza.
- [ ] Versões/digests de engines registrados.
- [ ] Cancelamento não publica artefato parcial.

## API e saída

- [ ] Erro usa envelope e taxonomia.
- [ ] Sem stacktrace/path/`storage_key`/task id/stderr.
- [ ] Rate limit/quota por operação.
- [ ] Idempotency-Key em criação de job.
- [ ] Downloads autorizados e `no-store`/`nosniff`/attachment.
- [ ] Filename de resposta sem CR/LF/path traversal.
- [ ] Artefato expirado/purged bloqueado.
- [ ] URL assinada, se existir, é curta e não logada.

## Storage e retenção

- [ ] Buckets/prefixos privados.
- [ ] Credencial mínima por serviço.
- [ ] Expiração bloqueia antes do purge físico.
- [ ] Purge idempotente e reconciliado.
- [ ] Objetos órfãos detectados.
- [ ] Limpar histórico local não é confundido com deleção do servidor.

## Supply chain e operação

- [ ] Dependências travadas e verificadas.
- [ ] Scanner/SBOM no CI.
- [ ] Segredos fora do repositório e imagem.
- [ ] Logs com redaction e acesso restrito.
- [ ] Alertas para fila, worker, purge e falhas semânticas.
- [ ] Backup/restore e migrações testados antes de produção.

## Evidência obrigatória

Cada item marcado deve apontar para teste, configuração ou revisão. “Documentado” sem implementação/teste não satisfaz o gate de produção.
