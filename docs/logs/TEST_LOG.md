# Test Log

Este arquivo registra comandos e resultados efetivamente executados.

## Template

```text
## YYYY-MM-DD — Escopo
Comandos executados:
Ambiente/versões:
Fixtures:
Resultado:
Falhas encontradas:
Correções aplicadas:
Testes não executados e motivo:
```

## 2026-07-21 — Verificação do bootstrap e da Fase 0

Comandos executados:

- `openspec status --change bootstrap-core-foundation`;
- `openspec validate bootstrap-core-foundation --strict`;
- `pnpm run verify:toolchain`;
- `serena project health-check .`;
- `codex mcp list`, `codex mcp get serena` e `codex mcp get context7`;
- sessão efêmera e somente leitura do Codex com chamadas Context7 `resolve-library-id` e `query-docs`;
- descoberta por `rg` de scripts, configurações e arquivos de teste;
- `pnpm install --lockfile-only --frozen-lockfile --offline --ignore-scripts`;
- `docker context ls`, `systemctl --user status docker-desktop.service` e `systemctl --user start docker-desktop.service`;
- validação sintática do shell com `bash -n` e validação estrutural de JSON com Node.js.

Ambiente/versões:
Ubuntu 26.04 LTS; Git 2.53.0; Node.js 24.18.0; npm 11.16.0; Corepack 0.35.0; pnpm 11.15.1; Python `python` ausente; Python 3.14.4 em `python3`; uv 0.11.29; Docker client 29.6.2 e server 29.6.1; OpenSpec 1.6.0; Graphify 0.9.23; Serena 1.6.1 em Python 3.13.14; Context7 CLI 0.5.5.

Fixtures:
Não aplicável; nenhuma funcionalidade de produto foi criada.

Resultado:

- OpenSpec: 4/4 artefatos completos; validação estrita com código de saída 0.
- Verificador da Fase 0: aprovado com código de saída 0; versões e artefatos obrigatórios presentes; Serena e Context7 habilitados.
- Context7: MCP funcional; `/graphify-labs/graphify` resolvido e documentação retornada por `query-docs`.
- Graphify inicial: 2.933 nós, 2.744 arestas e zero endpoints inválidos no verificador corrigido.
- Lockfile: instalação offline/congelada aprovada; SHA-256 permaneceu `17c814b167307942d3609c7b9d916ceddb85839573ab39baa114e30edb132a1a`.
- Coletores: zero scripts de teste, zero configurações e zero arquivos-fonte de teste executáveis.
- Docker: após o reboot, o serviço de usuário foi reativado sem `sudo`; cliente 29.6.2 e servidor 29.6.1 responderam ao teste final.

Falhas encontradas:

- A primeira versão do verificador procurava `edges`, mas o JSON do Graphify usa `links`; o resultado inicial de zero arestas era incorreto.
- O health-check da Serena registra `No analyzable files found` depois de ativar corretamente o projeto e expor 29 ferramentas.
- Uma tentativa inicial de inventário de coletores encerrou cedo devido a `pipefail` quando `rg` não encontrou resultados.
- O daemon Docker Desktop estava inativo após o reboot, embora o cliente e o contexto continuassem instalados.

Correções aplicadas:

- O verificador passou a validar `links`, exige pelo menos uma aresta e comprovou 2.744 relações válidas.
- O inventário passou a tratar resultado vazio como baseline zero esperado e foi repetido com sucesso.
- A skill global do Graphify foi atualizada de 0.9.17 para 0.9.23 para coincidir com a CLI e a integração do projeto.
- O serviço `docker-desktop.service` foi iniciado no escopo do usuário e o daemon voltou a responder, sem alteração de pacote do sistema.

Testes não executados e motivo:
Nx, lint, typecheck, Vitest, Playwright, pytest e demais coletores de produto não foram executados porque não estão configurados e pertencem a fases posteriores. Nenhuma suite simulada foi criada para mascarar esse baseline.

## 2026-07-20 — Validação documental da revisão técnica

Comandos executados:

- inventário de todos os arquivos Markdown;
- validador de arquivos não vazios e newline final;
- verificação de referências internas entre documentos Markdown;
- buscas por API sem `/api/v1`, DTO escalar antigo, fonte histórica obrigatória e nomes de estado conflitantes;
- `diff -ruN` entre documentação original e revisada;
- empacotamento ZIP e verificação do arquivo.

Ambiente/versões:
Validação local por scripts Python e ferramentas POSIX do ambiente de revisão.

Fixtures:
Não aplicável; esta etapa altera somente documentação.

Resultado:
91 arquivos Markdown validados; 183 referências internas conferidas; 15 blocos JSON parseados; nenhum arquivo não Markdown inesperado; zero inconsistências no validador final. O ZIP foi testado após o empacotamento.

Falhas encontradas:
Durante a revisão foram encontrados links conceituais ambíguos, fórmula escalar antiga, rotas sem versão e referências históricas; foram corrigidos antes do pacote final.

Correções aplicadas:
Documentos canônicos e referências sincronizados.

Testes não executados e motivo:
Não foram executados testes de frontend, backend, MusicXML, segurança runtime ou OMR porque nenhum código de aplicação foi fornecido ou alterado nesta tarefa.

## 2026-06-19 — Validação documental do guia

Resultado:
Arquivos Markdown principais existiam e não estavam vazios. Nenhum teste de aplicação foi executado.

## 2026-05-14 — Validação documental inicial

Resultado:
Estrutura documental gerada. Nenhum teste de aplicação foi executado.

## 2026-07-27 — Validação da consolidação da Fase 0

Comandos executados:

- `python3 scripts/validate-repository.py`;
- parsing de JSON e YAML;
- verificação de links Markdown relativos;
- validação de paths do manifesto visual;
- validação estrutural de `graphify-out/graph.json`;
- comparação de contagens com `GRAPH_REPORT.md`;
- inspeção do estado OpenSpec arquivado;
- `bash -n` nos scripts versionados;
- `git diff --check`.

Ambiente/versões:
Ambiente isolado de revisão; não possui OpenSpec, Graphify, Serena ou Context7 instalados.

Fixtures:
Não aplicável; nenhum código de produto foi criado.

Resultado:
Validação documental e estrutural aprovada no pacote corrigido. O grafo existente contém 3.076 nós e 2.890 relações válidas e concorda com o relatório.

Falhas encontradas:
Arquivos raiz obsoletos, contexto OpenSpec vazio, hook absoluto, arquitetura Python ambígua, visual futuro tratado como vinculante e verificador local dependente da máquina.

Correções aplicadas:
As correções constam em `FASE-0-CONSOLIDACAO-2026-07-27.md`.

Testes não executados e motivo:
A atualização do Graphify e a verificação dos MCPs não foram executadas porque essas CLIs não existem no ambiente de revisão. Devem ser executadas na máquina do projeto antes do checkpoint Git.
