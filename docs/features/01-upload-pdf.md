# Upload de partitura

## Objetivo

Receber arquivo de partitura com validação em frontend e backend, tratando todo upload como potencialmente perigoso.

## Tipos permitidos inicialmente

```text
application/pdf
application/vnd.recordare.musicxml+xml
application/xml
text/xml
```

## Fluxo

```text
Usuário seleciona arquivo
Frontend valida tipo/tamanho para UX
Frontend mostra resumo
API valida MIME real, extensão e tamanho
API sanitiza nome
API gera nome interno
API salva referência controlada
API cria registro em uploads
```

## Validação frontend

- Campo obrigatório.
- Extensão apenas como indício visual.
- `file.type` não é confiável como única validação.
- Mostrar nome seguro/truncado.
- Exibir erro claro.

## Validação backend obrigatória

- MIME real.
- Extensão.
- Tamanho máximo.
- Arquivo vazio.
- Estrutura mínima quando aplicável.
- Nome original não usado como path.
- Renomeação interna.

## Segurança

- Não salvar em pasta pública.
- Não expor path físico.
- Não retornar `storage_key`.
- Subprocessos, quando existirem, devem ter timeout e não usar `shell=True`.

## Estados públicos

```text
idle
uploading
uploaded
failed
expired
```

## Critérios de aceite

- Arquivo inválido não avança.
- Nome interno não depende do nome original.
- Backend rejeita MIME inválido.
- Erro público é claro e sem detalhes internos.
