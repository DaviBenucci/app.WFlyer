# Segurança do backend

> Status: canônico. Revisão: 2026-07-20.

## Fronteiras de confiança

```text
navegador não confiável
-> API autenticada por sessão anônima
-> banco/storage/broker privados
-> worker
-> sandbox de parser/OMR/renderizador
```

Todo ID, header, filename, MIME, XML e artefato de ferramenta externa é não confiável até validação.

## Sessão, autorização e CSRF

- cookie opaco, `HttpOnly`, `Secure`, `SameSite=Lax` e rotação/expiração;
- somente hash do token no banco;
- toda consulta por upload/job/artefato inclui `session_id`;
- UUID não substitui autorização;
- recurso inexistente ou de outra sessão retorna `404`;
- métodos mutáveis exigem `X-CSRF-Token` vinculado à sessão;
- CORS usa allowlist explícita quando houver origens separadas;
- tokens, cookies e CSRF nunca aparecem em URL, log ou analytics.

## Upload e parser

- allowlist por capability ativa;
- limite de bytes antes e durante streaming;
- extensão, MIME reportado, MIME detectado e assinatura devem ser coerentes;
- nome interno independente do original;
- arquivo começa em quarentena;
- MusicXML usa parser seguro, sem entidades externas, XInclude, rede ou recuperação silenciosa;
- limites de profundidade, nós, medidas, eventos e texto;
- MXL permanece desabilitado até controles de ZIP slip/bomb e `container.xml`;
- PDF permanece desabilitado até sandbox e gate OMR.

Nenhum detector isolado prova que um arquivo é seguro; as validações são combinadas com parsing restritivo e isolamento.

## Subprocessos e supply chain

- nunca usar `shell=True` com dados do usuário;
- argumentos em lista e paths internos;
- binários e imagens de container fixados por versão/digest;
- usuário sem privilégios, root filesystem read-only e sem rede;
- limites de recursos e timeout;
- diretório temporário exclusivo e limpeza;
- SBOM/scanner de dependências no CI;
- atualizações de parser, rasterizador, OMR e renderer exigem regressão hostil.

## Abuso e disponibilidade

Aplicar quotas/rate limits separados para:

```text
criação de sessão
upload por sessão/IP
bytes enviados por janela
jobs ativos por sessão
jobs por período
polling
downloads
```

Limites exatos são configuração obtida por benchmark. A API deve rejeitar cedo e retornar `429`/`413`, sem enfileirar trabalho impossível.

## Saída e download

- validar MusicXML/PDF produzido como dado não confiável;
- permitir apenas tipos de artefato allowlisted;
- autorizar antes de obter stream ou URL assinada;
- `Content-Disposition: attachment`;
- `X-Content-Type-Options: nosniff`;
- `Cache-Control: private, no-store`;
- nomes sanitizados e sem CR/LF;
- nunca servir arquivo de quarentena.

## Erros e logs

Resposta pública contém código estável, mensagem segura e `correlation_id`. É proibido retornar:

```text
stacktrace
exception class
storage_key ou path
task id interno
comando executado
engine stderr bruto
token/cookie/CSRF
conteúdo do documento
```

Logs usam allowlist de campos, redaction e controle de acesso. Nome original deve ser omitido ou minimizado quando não necessário.

## Segredos

- somente secret manager/variáveis protegidas;
- nenhuma credencial em repositório, frontend ou imagem;
- rotação e escopo mínimo;
- ambientes isolados;
- URLs de conexão mascaradas em erros e telemetria.

## Gate

Nenhum formato ou processador novo é habilitado apenas porque “funcionou em um arquivo”. Deve passar pela matriz de segurança, autorização, limites e observabilidade descrita em `../qa/08-testes-seguranca-arquivos.md`.
