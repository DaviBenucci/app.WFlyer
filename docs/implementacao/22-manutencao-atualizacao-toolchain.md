# Manutenção, atualização e retirada da toolchain

> Status: canônico.

## Inventário

Toda ferramenta deve constar em `toolchain-manifest.yaml` com:

- finalidade;
- escopo;
- adoção;
- comando de instalação;
- verificação;
- owner;
- política de atualização;
- rollback/remoção;
- dados acessados.

## Cadência

- patches de segurança: assim que avaliados;
- minor versions: janela mensal;
- major versions: mudança OpenSpec/ADR separada;
- MCPs/CLIs globais: revisão trimestral ou por incidente;
- imagens de Testcontainers/Playwright: pinning e revisão periódica;
- browsers: atualização coordenada com snapshots.

## Processo de atualização

```text
1. abrir mudança OpenSpec de manutenção
2. ler release notes/migration guide com Context7 e fonte oficial
3. atualizar uma família por vez
4. regenerar lockfile
5. executar lint/typecheck/unit
6. executar integração e E2E afetados
7. atualizar Graphify se estrutura mudou
8. comparar performance/bundle/snapshots
9. registrar rollback
```

## Ferramentas globais

### OpenSpec

```bash
pnpm update -g @fission-ai/openspec
openspec update
```

### Graphify

```bash
uv tool upgrade graphifyy
```

Reconstruir/atualizar grafo e validar relatório.

### Serena

```bash
uv tool upgrade serena-agent
serena project health-check
```

### Context7

Executar novamente o setup se a configuração/client mudar. Nunca sobrescrever configuração sem revisar o diff.

## Dependências do projeto

- usar Nx migrate para Nx;
- usar pnpm/lockfile para JS;
- usar `uv lock`/`uv sync` para Python;
- não atualizar dependência musical e golden files no mesmo commit sem relatório de diferença;
- não atualizar renderer/fontes sem regressão de engraving;
- não atualizar Playwright/Storybook sem validar baselines e interações.

## Supply chain

- dependências somente de registries aprovados;
- nomes de pacote conferidos contra typosquatting;
- scripts de instalação revisados;
- SBOM/licenças conforme política do projeto;
- MCPs avaliados como software com acesso ao projeto;
- tokens mínimos e rotacionáveis;
- nenhuma partitura de usuário enviada para serviço de desenvolvimento sem consentimento/política.

## Retirada

Uma ferramenta deve ser removida quando:

- duplica responsabilidade;
- não produz evidência útil;
- aumenta contexto/tempo de forma desproporcional;
- está abandonada ou vulnerável;
- impede atualização essencial;
- viola política de dados.

A retirada exige:

- remover dependência e config;
- substituir targets/scripts;
- atualizar AGENTS/OpenSpec/docs;
- limpar cache/artefatos;
- comprovar que gates permanecem cobertos.

## Auditoria trimestral

Perguntas:

- a IA realmente usa OpenSpec, Graphify e Serena na ordem definida?
- o Graphify está atualizado?
- Context7 está sendo usado só para dependências externas?
- cache Nx está correto?
- existem testes duplicados ou lacunas?
- ferramentas opcionais viraram dependências sem ADR?
- tokens e tempo diminuíram sem aumento de regressões?
- quais incidentes escaparam dos gates?
