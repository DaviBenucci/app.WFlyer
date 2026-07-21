# Toolchain do backend e motores musicais

> Status: canônico para API, workers e packages Python.

## pytest

### Instalação

```bash
uv add --dev pytest
```

### Organização

```text
tests/
├── unit/
├── property/
├── integration/
├── contract/
├── security/
├── golden/
└── regression/
```

Convenções:

- arquivos `test_*.py`;
- fixtures pequenas e explícitas;
- markers registrados;
- relógio, random seed e ambiente controláveis;
- nenhum teste depende de ordem de execução;
- erro esperado precisa validar tipo/código, não apenas mensagem ampla.

## Hypothesis

### Instalação

```bash
uv add --dev hypothesis
```

### Propriedades obrigatórias do Core

- A→B→A recupera semântica suportada;
- altura de concerto é preservada;
- duração total não muda na transposição exata;
- nenhum evento desaparece sem provenance;
- transposição composta equivale ao intervalo composto quando política é igual;
- serialização/reparse preserva o grafo canônico;
- entradas hostis respeitam limites.

Estratégias customizadas devem gerar partituras válidas e inválidas de forma separada. Não usar geração aleatória sem invariantes musicais.

Falha minimizada pelo Hypothesis vira fixture de regressão quando representar bug relevante.

## Testcontainers

### Pré-requisito

Runtime compatível com Docker API funcional.

### Instalação inicial

```bash
uv add --dev "testcontainers[postgres]"
```

Adicionar módulos conforme arquitetura real, não preventivamente.

### Uso

- PostgreSQL real para migrations, constraints e concorrência;
- Redis real para fila/cache quando aplicável;
- storage S3 compatível/MinIO ou LocalStack em gate próprio;
- Toxiproxy/fault injection quando necessário;
- lifecycle por fixture para evitar vazamento.

Testcontainers não substitui E2E nem ambiente de homologação. Imagens devem ser pinadas por tag/digest aprovado.

## Ruff

### Instalação

```bash
uv add --dev ruff
```

Comandos:

```bash
uv run ruff check .
uv run ruff check --fix .
uv run ruff format .
uv run ruff format --check .
```

Configuração fica em `pyproject.toml` ou `ruff.toml`. Ruff não substitui typechecker; mypy ou pyright permanece decisão da stack.

## Camadas de teste

### Unitário

- intervalos;
- pitch/enarmonia;
- catálogo instrumental;
- invariantes;
- estados de job;
- autorização pura.

### Property/metamórfico

- equivalências musicais;
- round trips;
- preservação estrutural;
- limites e parsers.

### Integração

- API + PostgreSQL;
- migration upgrade/downgrade quando suportado;
- outbox + worker;
- retry/idempotência;
- retenção/purge;
- storage e manifesto.

### Golden/semântico

- MusicXML de entrada;
- grafo esperado;
- MusicXML de saída;
- diff semântico;
- erro esperado para documento fora do suporte.

### Segurança

- XXE/XInclude;
- zip bomb/MXL quando habilitado;
- path traversal;
- IDOR;
- CSRF;
- limites de CPU/memória/tempo;
- sanitização de logs.

## Gate local rápido

```bash
uv run ruff check .
uv run ruff format --check .
uv run pytest tests/unit tests/property -q
```

## Gate de PR

```bash
uv run pytest tests/unit tests/property tests/contract -q
uv run pytest tests/integration -q
uv run pytest tests/security -q
```

A seleção final é orquestrada pelo Nx conforme projetos afetados.

## Fontes oficiais

- pytest: <https://docs.pytest.org/en/stable/getting-started.html>
- Hypothesis: <https://hypothesis.readthedocs.io/en/latest/quickstart.html>
- Testcontainers: <https://testcontainers.com/guides/getting-started-with-testcontainers-for-python/>
- Ruff: <https://docs.astral.sh/ruff/installation/>
