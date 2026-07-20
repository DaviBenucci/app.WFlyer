# Sandbox de processadores de documentos

> Status: canônico para qualquer parser externo, rasterizador, OMR ou renderer.

## Objetivo

Conter falhas e exploração de ferramentas que processam dados controlados pelo usuário.

## Perfil mínimo

```text
usuário não root
sem capabilities do Linux
no-new-privileges
filesystem raiz read-only
/tmp/work exclusivo e com quota
sem rede de entrada/saída
limite de CPU e wall clock
limite de memória/swap
limite de PIDs/threads
limite de arquivos, file size e open descriptors
seccomp/AppArmor/SELinux quando disponível
imagem fixada por digest
```

O processo recebe somente arquivos internos por bind/mount controlado. Nunca recebe path, flag ou comando diretamente do cliente.

## Execução

- argumentos em lista; `shell=False`;
- ambiente mínimo, locale/timezone definidos;
- stdout/stderr limitados e sanitizados;
- output somente em diretório allowlisted;
- proibir symlinks/hardlinks e paths que escapem;
- validar tipo, quantidade, tamanho e estrutura de cada saída;
- matar árvore inteira ao timeout/cancelamento;
- apagar workdir mesmo após crash.

## Perfis por engine

Cada adapter declara:

```text
engine_name/version/digest
input allowlist
output allowlist
limits padrão
exit codes conhecidos
retry policy
license/provenance
health check
```

Upgrade de engine cria novo manifest e executa corpus funcional + hostil antes de rollout.

## MXL/ZIP

Quando habilitado:

- inspecionar entries sem extrair arbitrariamente;
- rejeitar paths absolutos, `..`, drive letters, symlink e special files;
- limitar número de entries, tamanho individual/total e compression ratio;
- rejeitar arquivos aninhados fora da allowlist;
- ler `META-INF/container.xml` com parser XML seguro;
- copiar somente rootfile aprovado para workdir.

## PDF/OMR

- limitar páginas, dimensões, DPI e pixels totais;
- rasterizar no sandbox;
- rejeitar senha/criptografia/recursos não suportados;
- não executar JavaScript, anexos, URLs ou conteúdo multimídia;
- OMR lê somente raster/arquivo intermediário permitido;
- validar MusicXML de saída como entrada hostil nova.

## Testes

- timeout e kill da árvore;
- tentativa de rede falha;
- tentativa de escrita fora do workdir falha;
- fork bomb/PID limit;
- consumo de memória/disco limitado;
- symlink/path escape bloqueado;
- saída inesperada rejeitada;
- stderr enorme truncado;
- arquivo hostil não afeta outro job;
- workdir é removido.
