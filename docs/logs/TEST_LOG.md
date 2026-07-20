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
