# Toolchain do frontend — identidade, componentes e testes

> Status: canônico para `apps/web` e `packages/design-system`.

## Storybook

### Instalação

```bash
pnpm create storybook@latest
```

Para Next.js, escolher `@storybook/nextjs-vite` salvo incompatibilidade documentada por spike.

### Uso obrigatório

Cada componente de produto deve possuir stories para:

- padrão;
- loading/progresso;
- vazio;
- erro recuperável;
- erro terminal;
- conteúdo extremo;
- teclado;
- mobile;
- zoom 200%;
- contraste elevado;
- reduced motion;
- estados específicos do domínio.

Story não é mock visual estático: interações essenciais usam `play`/testes conforme API atual.

### Proibições

- deixar stories geradas sem relação com W_Flyer;
- snapshots aprovados automaticamente;
- utilizar Storybook como ambiente diferente da aplicação;
- importar segredo ou chamar produção.

## Vitest

### Instalação

```bash
pnpm add -D -w vitest @vitest/browser
```

Scripts:

```json
{
  "scripts": {
    "test": "vitest",
    "test:run": "vitest run",
    "test:browser": "vitest --project browser"
  }
}
```

### Uso

- funções e hooks;
- reducers/guards/máquinas;
- componentes em ambiente de navegador quando APIs reais forem relevantes;
- contratos de serialização;
- adapters sem E2E completo.

CI usa `vitest run`, não watch mode.

## MSW

### Instalação

```bash
pnpm add -D -w msw
pnpm exec msw init apps/web/public --save
```

### Arquitetura

```text
packages/testing-fixtures/msw/
├── handlers.ts
├── browser.ts
├── server.ts
└── scenarios/
```

Os mesmos handlers devem servir a Storybook, Vitest e desenvolvimento. Configurar erro em request não tratada nos testes, exceto allowlist explícita.

Cenários mínimos:

- upload aceito/rejeitado;
- progresso normal e fora de ordem;
- revisão obrigatória;
- retry transitório;
- sessão expirada;
- IDOR negado;
- resultado expirado;
- backend incompatível;
- offline/reconexão.

## Playwright

### Instalação

```bash
pnpm create playwright
pnpm exec playwright install --with-deps
```

Selecionar TypeScript, pasta `e2e`, navegadores e CI. Não aceitar workflow gerado sem revisão.

### Uso

- fluxos ponta a ponta críticos;
- Chromium, Firefox e WebKit definidos pelo gate;
- screenshots em ambiente fixado;
- teclado e foco;
- reduced motion;
- falhas de rede;
- download autorizado;
- rastreio/trace em falha.

Seletores preferenciais:

```text
role + accessible name
label
texto estável de domínio
data-testid somente quando sem alternativa semântica
```

É proibido selecionar por classe de estilo ou estrutura frágil.

## Biome

### Instalação

```bash
pnpm add -D -w --save-exact @biomejs/biome
pnpm exec biome init
```

Comandos:

```bash
pnpm exec biome check --write .
pnpm exec biome ci .
```

Biome formata, organiza imports e aplica lint conforme configuração. TypeScript continua responsável por typecheck.

## Style Dictionary

### Instalação

```bash
pnpm add -D -w style-dictionary
```

### Uso

```text
design tokens fonte
→ Style Dictionary
→ CSS variables + tipos/artefatos gerados
→ design system
```

Comando típico:

```bash
pnpm exec style-dictionary build
```

Outputs gerados não são editados manualmente. Alteração de token exige stories/regressão visual afetadas.

## XState, Motion e GSAP

- XState: lógica de fluxos complexos;
- Motion: presença, layout, gestos e microinterações React;
- GSAP: `Ink Transfer` e timelines SVG isoladas;
- CSS: hover/focus/transição simples.

Uma propriedade visual não pode ter mais de um owner de animação.

## Gate de PR do frontend

```text
Biome
→ TypeScript strict
→ Vitest unit/browser
→ Storybook build/test
→ MSW scenarios
→ Playwright crítico
→ regressão visual
→ acessibilidade
→ bundle/performance afetados
```

## Fontes oficiais

- Storybook: <https://storybook.js.org/docs/get-started/install>
- Storybook Next.js/Vite: <https://storybook.js.org/docs/get-started/frameworks/nextjs-vite>
- Vitest: <https://vitest.dev/guide/>
- MSW: <https://mswjs.io/docs/>
- Playwright: <https://playwright.dev/docs/intro>
- Biome: <https://biomejs.dev/guides/getting-started/>
- Style Dictionary: <https://styledictionary.com/getting-started/installation/>
