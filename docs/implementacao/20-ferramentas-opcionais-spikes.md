# Ferramentas opcionais e protocolo de spike

> Status: não instalar antes de ADR, hipótese mensurável e aprovação.

## Regra comum

Cada spike precisa conter:

- problema atual mensurado;
- hipótese;
- alternativa sem a ferramenta;
- protótipo descartável;
- custo de bundle/infra/licença/manutenção;
- risco de segurança e dados;
- teste de remoção;
- decisão `adotar`, `adiar` ou `rejeitar`.

## Temporal

### Problema que pode resolver

Orquestração durável de pipelines longos com retries, timers, sinais, espera por revisão e retomada após falha.

### Instalação do spike Python

```bash
uv add temporalio
```

Também é necessário Temporal Service/CLI local conforme documentação oficial.

### Gate

Comparar:

```text
Celery + Redis + outbox + leases + reconciliação
versus
Temporal workflows + activities + workers
```

Métricas:

- recuperação de crash;
- idempotência;
- espera por revisão humana;
- observabilidade;
- complexidade operacional;
- custo;
- capacidade de versionar workflows.

### Proibição

Não operar Celery e Temporal como orquestradores concorrentes do mesmo pipeline. Se Temporal for adotado, documentar migração e ownership.

## Rive

### Uso permitido

- microilustrações independentes;
- estado vazio;
- feedback de seleção;
- elemento de marca reativo.

### Uso proibido

- partitura real;
- renderização de MusicXML;
- `Ink Transfer` principal;
- lógica de estado do produto;
- conteúdo essencial sem fallback.

### Instalação do spike

Escolher renderer após medir suporte e bundle. A documentação oficial apresenta pacotes React como `@rive-app/react-canvas` e opções WebGL/Canvas.

```bash
pnpm add @rive-app/react-canvas
```

Verificar versão correlata do runtime e WASM. Lazy-load obrigatório, reduced motion e fallback estático.

## Pact

### Quando adotar

Somente quando consumidor e provedor evoluírem/deployarem de forma suficientemente independente para OpenAPI + integração não cobrirem o risco.

### Instalação

```bash
pnpm add -D @pact-foundation/pact
```

### Uso

- consumidor declara interações realmente usadas;
- provider verifica contratos;
- Pact não substitui OpenAPI, autenticação, schema nem E2E;
- dados sensíveis não entram nos pacts.

## StrykerJS

### Objetivo

Verificar se testes TypeScript detectam mutações relevantes.

### Inicialização

```bash
npx stryker init
npx stryker run
```

Revisar `stryker.config.mjs`. Executar sobre packages críticos/afetados, preferencialmente noturno ou semanal. Não exigir score global alto sem excluir código gerado e mutações equivalentes justificadas.

## mutmut

### Objetivo

Mutation testing dos motores Python.

### Instalação

```bash
uv add --dev mutmut
uv run mutmut run
uv run mutmut browse
```

Requer suporte a `fork`; no Windows, usar WSL. Rodar somente com árvore Git limpa/commitada e configuração de paths. Priorizar transposição, invariantes e autorização.

## Critério de aprovação

| Ferramenta | Aprovar quando | Rejeitar/adiar quando |
|---|---|---|
| Temporal | simplificar recuperação e revisão humana de forma mensurável | infraestrutura supera benefício do MVP |
| Rive | interação única com bundle aceitável e fallback | apenas “decorar” interface ou duplicar GSAP/Motion |
| Pact | deploys independentes geram regressões de contrato | OpenAPI e integração já cobrem o risco |
| StrykerJS | revelar testes fracos em domínio crítico | custo excessivo sem foco |
| mutmut | revelar sobreviventes relevantes em motor musical | suíte instável ou plataforma incompatível |

## Fontes oficiais

- Temporal: <https://docs.temporal.io/develop/python>
- Rive React: <https://rive.app/docs/runtimes/react/react>
- Pact JS: <https://docs.pact.io/implementation_guides/javascript/readme>
- StrykerJS: <https://stryker-mutator.io/docs/stryker-js/getting-started/>
- mutmut: <https://mutmut.readthedocs.io/en/latest/index.html>
