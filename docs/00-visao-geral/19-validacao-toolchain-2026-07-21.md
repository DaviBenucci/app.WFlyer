# Validação documental da toolchain

> Data: 2026-07-21.

## Verificações executadas

- parsing de todos os JSON;
- parsing de todos os YAML;
- validação de `toolchain-manifest.yaml` contra JSON Schema;
- unicidade dos 21 IDs de ferramenta;
- existência dos documentos obrigatórios;
- H1 em todos os Markdown;
- links Markdown internos relativos;
- sintaxe Bash dos templates;
- presença de todos os frameworks no catálogo;
- busca básica por segredos nos novos documentos;
- comparação com a versão anterior para detectar remoções.

## Resultado

```text
272 arquivos após a integração inicial
203 documentos Markdown
12 arquivos JSON
26 arquivos YAML/YML
21 ferramentas no manifesto
0 links internos quebrados
0 JSON/YAML inválidos
0 erros de schema
0 scripts Bash inválidos
0 arquivos anteriores removidos
0 erros
0 warnings
```

Os números finais do pacote podem ser maiores por incluir este relatório, o relatório externo, checksums e artefatos de entrega. A validação final do ZIP deve ser executada após a compactação.

## O que não foi validado

- instalação real de cada pacote;
- compatibilidade entre versões futuras;
- execução de Nx, MCPs ou frameworks;
- código de frontend/backend, ainda inexistente neste pacote;
- segurança de configurações globais do ambiente do usuário.
