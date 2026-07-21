# Graphify — navegação macro, impacto e economia de contexto

> Status: obrigatório para mudanças transversais. O grafo é índice, não fonte de verdade.

## Instalação

O pacote oficial no PyPI é `graphifyy`, com dois “y”; o binário é `graphify`.

```bash
uv tool install graphifyy
graphify --version
graphify install --platform codex
```

Construir o grafo a partir do agente:

```text
/graphify .
```

Saída esperada:

```text
graphify-out/
├── graph.json
├── GRAPH_REPORT.md
└── graph.html
```

## O que entra no grafo

- código-fonte;
- documentação Markdown;
- OpenAPI, JSON Schema e YAML de contratos;
- migrations;
- testes e fixtures textuais;
- ADRs e OpenSpec;
- tokens e especificações visuais.

## O que deve ser ignorado

- dependências;
- builds e caches;
- storage/upload/quarentena;
- arquivos de usuário;
- binários e vídeos;
- baselines redundantes;
- resultados do próprio Graphify;
- segredos;
- exports gerados.

Usar `templates/.graphifyignore.example` como base.

## Rotina da IA

Antes de alterar mais de um módulo:

1. conferir idade/commit do grafo;
2. ler `GRAPH_REPORT.md`;
3. consultar conceito, caminho ou impacto;
4. registrar nós e relações relevantes no plano;
5. confirmar relações críticas no código com Serena;
6. não tratar relação `INFERRED` ou `AMBIGUOUS` como fato;
7. atualizar o grafo após mudança estrutural.

## Consultas-padrão

```bash
graphify query "quais módulos implementam e verificam transposição?" --budget 1200
graphify query "como upload chega à publicação do artefato?" --dfs --budget 1600
graphify explain "CanonicalMusicGraph"
graphify path "MusicXmlNormalizer" "MusicalDiffVerifier"
```

Os nomes reais de nós devem ser descobertos; não inventar nomes apenas para executar o comando.

## Atualização

```text
/graphify . --update
```

Alternativas locais:

```bash
graphify watch .
graphify hook install
```

No CI, o grafo pode ser reconstruído e comparado para detectar staleness, mas não deve bloquear por diferenças cosméticas sem regra definida.

## Política de tokens

- começar com orçamento entre 800 e 1600 tokens por consulta;
- aumentar somente quando o subgrafo estiver incompleto;
- preferir `path` para uma cadeia conhecida;
- preferir `explain` para um conceito;
- não anexar `graph.json` inteiro ao prompt;
- não usar o grafo para reproduzir conteúdo integral de arquivos.

## Limitações e segurança

- grafo desatualizado pode induzir erro;
- relações semânticas podem ser inferidas incorretamente;
- arquivos ignorados podem esconder dependência importante;
- análise de documentos pode consumir modelo externo conforme configuração;
- revisar política de dados antes de habilitar qualquer processamento remoto.

## Desinstalação

```bash
graphify uninstall --purge
uv tool uninstall graphifyy
```

Não apagar o grafo durante investigação de incidente antes de capturar evidências.

## Fontes oficiais

- <https://graphify.com/docs/install>
- <https://graphify.com/docs/tutorial>
- <https://graphify.com/docs/cli>
- <https://graphify.com/docs/mcp-tools>
