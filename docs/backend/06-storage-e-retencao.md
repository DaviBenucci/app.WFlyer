# Storage, ciclo de vida e retenção

> Status: canônico. Revisão: 2026-07-20.

## Princípio

O banco guarda metadados e o storage guarda bytes. O nome original nunca define chave, path ou autorização.

## Zonas lógicas

```text
quarantine/    uploads ainda não aprovados
internal/      original, raw e normalized MusicXML, relatórios
public/        artefatos autorizáveis para download
workdir/       temporário local por tentativa; nunca é storage persistente
```

Estrutura sugerida:

```text
quarantine/sessions/{session_id}/uploads/{upload_id}/{object_id}
internal/jobs/{job_id}/attempts/{attempt_no}/{artifact_id}
public/jobs/{job_id}/{artifact_id}
```

`storage_key` é aleatória/derivada de IDs internos, permanece privada e não contém filename do usuário.

## Gravação e integridade

- upload é escrito em objeto temporário e finalizado atomicamente;
- tamanho e SHA-256 são registrados após a escrita;
- worker confirma tamanho/hash antes de ler;
- artefato final é gravado primeiro como privado/provisório;
- publicação ocorre apenas após validação e atualização transacional dos metadados;
- leituras usam allowlist de bucket/prefixo e nunca aceitam chave arbitrária do cliente.

## Retenção padrão

- upload original: 15 dias a partir de `validated_at`;
- artefatos do job: 15 dias a partir de `finished_at`;
- sessão anônima deve ser renovada de modo a não encerrar antes da janela anunciada de um job recém-concluído;
- o ambiente pode reduzir limites por exigência legal/operacional, mas deve comunicar o valor retornado em `expires_at`.

Retenção não é status de processamento. Use:

```text
retention_status = active | expired | purging | purged
```

## Expiração e purge

1. Ao alcançar `expires_at`, marcar `expired` e bloquear downloads imediatamente.
2. Enfileirar purge idempotente.
3. Remover bytes das zonas pública, interna e de quarentena.
4. Marcar `purged_at` e `retention_status=purged`.
5. Preservar apenas metadados mínimos não sensíveis pelo período operacional definido.
6. Job e upload de outra sessão nunca podem ser afetados.

`DELETE /api/v1/jobs/{job_id}` antecipa esse fluxo. Limpar o histórico do navegador não apaga o servidor; a UI deve oferecer as duas ações separadamente quando o recurso ainda existir.

## Download

- sempre autorizar sessão e propriedade antes de abrir o objeto;
- bloquear `expired`, `purging` e `purged`;
- usar stream pela API no Core;
- URL assinada curta exige decisão explícita e só pode ser emitida após autorização;
- enviar `Content-Disposition`, `Cache-Control: private, no-store` e `X-Content-Type-Options: nosniff`;
- não reutilizar URLs permanentes.

## Controles operacionais

- criptografia em trânsito e em repouso conforme o provedor;
- credenciais do storage somente no backend/worker;
- permissões mínimas por serviço;
- lifecycle do provedor como segunda barreira, não como única fonte de verdade;
- reconciliação periódica entre banco e objetos;
- alarmes para objetos órfãos, purge atrasado e falha de integridade.

## Testes obrigatórios

- path traversal no filename não altera a chave interna;
- objeto de outra sessão não é lido nem apagado;
- hash divergente bloqueia processamento;
- expiração bloqueia download antes do purge físico;
- purge é idempotente;
- objeto órfão é detectado pela reconciliação;
- DTO e log não expõem `storage_key`, path ou URL assinada completa.
