# Modelo de ameaças

> Status: canônico. Revisão: 2026-07-20.

## Ativos

- arquivos originais e artefatos;
- estrutura musical e metadados;
- sessão anônima/CSRF;
- propriedade de uploads/jobs;
- capacidade de CPU/memória/storage;
- integridade do motor/catálogo;
- logs e diagnósticos internos;
- dependências e imagens de processamento.

## Atores

- usuário legítimo;
- atacante externo sem sessão;
- sessão maliciosa tentando abuso/IDOR;
- arquivo hostil;
- dependência/processador comprometido;
- erro operacional ou bug concorrente.

## Ameaças e controles

### Acesso horizontal/IDOR

Ataque: usar UUID de outra sessão.

Controles: cookie opaco, consulta por `(id, session_id)`, `404` neutro, testes A/B, autorização antes de stream/URL.

### CSRF e roubo de sessão

Ataque: criar/apagar recursos usando cookie da vítima ou expor token.

Controles: SameSite, CSRF por header, HTTPS, HttpOnly, rotação, sem tokens em URL/log/storage, CORS allowlist.

### Arquivo poliglota ou tipo falso

Ataque: extensão/MIME enganoso ou parser diferencial.

Controles: capability/allowlist, streaming limitado, assinatura + parse restritivo, quarentena, rejeição de ambiguidades.

### XML hostil

Ataque: XXE, SSRF, leitura local, expansão de entidades, profundidade/quantidade extrema.

Controles: entidades/XInclude/rede desabilitados, limites de estrutura, schema local, timeout/memória e corpus hostil.

### MXL/ZIP hostil

Ataque: zip slip, zip bomb, paths absolutos, links, entries aninhadas.

Controles: feature off no Core; quando ativa, extração segura sem filesystem arbitrário, limites de entries/tamanho/ratio e validação de container.

### PDF/OMR/renderer hostil

Ataque: explorar rasterizador/OMR/renderer ou consumir recursos.

Controles: feature gate, sandbox sem rede/privilégio, filesystem read-only, quotas, timeout, versão fixada, validação da saída.

### Abuso de recursos

Ataque: muitos uploads/jobs/polling/downloads ou partituras estruturalmente enormes.

Controles: rate limit, quota, limites de bytes/nós/eventos/páginas, fila priorizada, cancelamento, reconciliação e alertas.

### Confusão/double transposition

Ataque/bug: metadata de origem contraditória, intervalo aplicado duas vezes ou artefato errado.

Controles: snapshots, `SOURCE_INSTRUMENT_MISMATCH`, invariantes de concerto, vínculo job→artefato e hashes.

### Vazamento por logs/telemetria

Ataque/erro: conteúdo, token, URL assinada ou path em logs.

Controles: allowlist/redaction, acesso restrito, testes de log, retenção e `correlation_id`.

### Supply chain

Ataque: dependência/imagem maliciosa ou vulnerável.

Controles: lockfiles/digests, scanner/SBOM, origem confiável, privilégio mínimo e regressão antes de upgrade.

## Riscos residuais

- OMR pode interpretar música incorretamente mesmo sem falha de segurança;
- MusicXML pode perder layout no round-trip;
- sessão apagada pelo usuário pode impedir acesso a recurso ainda retido;
- rate limiting por IP pode afetar redes compartilhadas.

Esses riscos devem ser comunicados/medidos, não escondidos por afirmação genérica de segurança.
