# Política de upload e storage

## Nome e metadata

- filename original é dado não confiável;
- exibir somente versão sanitizada/truncada;
- remover separadores, controles, CR/LF e nomes reservados;
- path/chave usa IDs internos;
- não inferir tipo apenas pela extensão.

## Streaming e quarentena

- rejeitar `Content-Length` excessivo quando presente, mas também contar bytes reais;
- não carregar arquivo inteiro em memória;
- gravar inicialmente em quarentena privada;
- parsing/aprovação promove por cópia/movimento atômico;
- falha remove/quarentena conforme política sem liberar download.

## MusicXML

- aceitar XML não comprimido no Core;
- validar raiz/perfil com parser seguro;
- bloquear recursos externos;
- impor limites estruturais além de bytes;
- preservar original e gerar artefatos derivados separados.

## MXL e PDF

- MXL é container ZIP e segue política própria antes de ativação;
- PDF usa sandbox/OMR antes de entrar no pipeline canônico;
- mudar MIME allowlist exige capability, threat model, corpus e testes.

## Storage

```text
quarantine/{session}/{upload}/{object}
internal/jobs/{job}/{attempt}/{artifact}
public/jobs/{job}/{artifact}
```

Chaves nunca são públicas. A API controla acesso ou emite URL curta após autorização.

## Retenção

Seguir `../backend/06-storage-e-retencao.md`; o servidor retorna `expires_at` real. Lifecycle do provedor é defesa adicional e deve ser reconciliado com o banco.
