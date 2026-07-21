# Serena e Context7 — código interno e documentação externa

> Status: obrigatório para agentes de código. As duas ferramentas possuem papéis diferentes.

## Serena: navegação e edição por símbolos

### Instalação

```bash
uv tool install -p 3.13 serena-agent
serena --version
serena init
serena setup codex
```

Configuração manual do Codex:

```toml
[mcp_servers.serena]
startup_timeout_sec = 15
command = "serena"
args = ["start-mcp-server", "--project-from-cwd", "--context=codex"]
```

Verificação:

```text
/mcp
→ Serena conectada
→ projeto atual ativado
→ índice saudável
```

Comandos operacionais úteis:

```bash
serena project create --index
serena project index
serena project health-check
serena tools list --all
```

### Quando usar

- localizar classe, função, método ou interface;
- encontrar referências e consumidores;
- ler corpo de símbolo sem carregar arquivo inteiro;
- renomear/refatorar com consciência semântica;
- editar uma unidade bem delimitada.

### Quando não usar isoladamente

- decidir arquitetura;
- inferir regra musical;
- validar segurança;
- provar que todos os consumidores foram atualizados;
- substituir testes ou revisão de diff.

### Regra de economia de contexto

```text
Graphify identifica o módulo
→ Serena identifica os símbolos
→ leitura textual confirma detalhes
→ testes provam comportamento
```

Se a IA fizer repetidos `grep`/leituras integrais sem necessidade, deve retornar ao índice simbólico. Hooks da Serena podem ser habilitados no Codex após avaliação e sem autoaprovar alterações destrutivas indiscriminadamente.

### Atualização e remoção

```bash
uv tool upgrade serena-agent
uv tool uninstall serena-agent
```

## Context7: documentação atual de dependências

### Instalação no Codex

```bash
npx ctx7 setup --codex
```

Esse fluxo autentica e configura o Codex. Chaves e tokens ficam fora do repositório.

Remoção:

```bash
npx ctx7 remove
```

### Quando usar

- API ou comportamento de versão instalada;
- configuração de Next.js, Storybook, Vitest, Motion, GSAP, XState, FastAPI, SQLAlchemy, Celery ou outra dependência;
- migração entre versões;
- confirmação de opção de CLI;
- exemplo mínimo atual.

### Quando não usar

- descobrir requisito do W_Flyer;
- substituir ADR ou OpenSpec;
- pesquisar código interno;
- decidir versão sem olhar lockfile;
- trazer exemplo genérico sem adaptar a segurança e arquitetura do projeto.

### Protocolo de consulta

1. identificar pacote e versão no lockfile;
2. formular pergunta específica;
3. pedir documentação para aquela versão quando disponível;
4. comparar com tipos/código instalado;
5. adaptar ao padrão interno;
6. registrar decisão quando houver impacto arquitetural.

Exemplo de prompt:

```text
Consulte Context7 para XState na versão instalada. Confirme a API atual de actors
invocados e cleanup em React. Não implemente antes de comparar com o lockfile e
com a máquina documentada no OpenSpec ativo.
```

## Segurança MCP

- MCPs são ferramentas com acesso e contexto; instalar somente fontes aprovadas;
- revisar comandos antes de permitir escrita;
- não expor `.env`, chaves, partituras de usuários ou storage privado;
- preferir escopo de projeto quando possível;
- documentar servidor, versão e finalidade;
- remover MCP não utilizado.

## Fontes oficiais

- Serena: <https://oraios.github.io/serena/02-usage/010_installation.html>
- Serena/Codex: <https://oraios.github.io/serena/02-usage/030_clients.html>
- Context7/Codex: <https://context7.com/docs/clients/codex>
- Context7: <https://context7.com/docs/overview>
