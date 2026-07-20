# Testes de segurança de arquivos e autorização

## XML/MusicXML hostil

- entidade externa para arquivo local;
- entidade externa HTTP/SSRF;
- entity expansion/billion laughs;
- DTD/XInclude;
- profundidade extrema;
- milhões de nós/notas/medidas;
- texto/atributo excessivo;
- namespace/raiz incorretos;
- XML malformado com recovery tentador;
- links/URLs externos;
- extensão/MIME/assinatura divergentes;
- filename com traversal, controles e CR/LF.

Esperado: rejeição segura, sem rede/leitura local, limite de recursos e sem stacktrace.

## MXL, quando habilitado

- `../` e path absoluto;
- drive letter/UNC;
- symlink/hardlink/special file;
- zip bomb e compression ratio extremo;
- excesso de entries/tamanho descompactado;
- nested archives;
- `container.xml` ausente/múltiplo/XXE;
- rootfile fora do container;
- tipos extras inesperados.

## PDF/OMR, quando habilitado

- excesso de páginas/dimensões/pixels;
- PDF criptografado ou corrompido;
- anexos, JavaScript, links e multimídia;
- parser bombs e timeout;
- output inesperado do engine;
- tentativa de rede/escrita/fork;
- stderr/arquivo temporário excessivos;
- crash não afeta outro job.

## Autorização

- IDOR A/B em upload, job, artifact e delete;
- sem cookie, cookie expirado/revogado;
- CSRF ausente/errado/de outra sessão;
- troca/fixação de sessão;
- ID em URL/histórico sem cookie;
- download direto após expiração/purge;
- URL assinada reutilizada após prazo, se existir.

## Abuso

- uploads concorrentes;
- bytes por janela;
- jobs ativos por sessão;
- double click/idempotency conflict;
- polling agressivo;
- download repetido;
- retry/reentrega do broker;
- arquivo pequeno com estrutura enorme.

## Vazamento

Inspecionar respostas, headers, logs, tracing e eventos para:

```text
cookie/CSRF/token
storage_key/path
stacktrace/exception
comando/stderr
conteúdo XML/PDF
URL assinada
metadata de outra sessão
```

## Gate

A suíte roda no CI para parsers e em ambiente isolado para engines pesadas. Nenhum teste hostil deve depender de internet; usar endpoints/arquivos controlados para provar bloqueio.
