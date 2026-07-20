# Arquitetura de componentes frontend

> Revisão: 2026-07-20.

## Objetivo

Evitar componentes gigantes, duplicação de telas e acoplamento entre UI e contratos de transporte.

## Estrutura orientativa

```text
src/
  app/
    (public)/
    (studio)/
    (utility)/
  features/
    session/
    capabilities/
    upload/
    instruments/
    transposition/
    jobs/
    artifacts/
    history/
    settings/
    motion/
  components/
    primitives/
    product/
    layouts/
  lib/
    api/
    formatting/
    accessibility/
    storage/
    motion/
  styles/
    tokens.css
    globals.css
```

## Regras de fronteira

- `app/` compõe rotas e layouts;
- `features/` contém estado, adapters, hooks e componentes ligados ao caso de uso;
- `components/primitives/` contém controles sem regra de domínio;
- `components/product/` contém linguagem visual do W_Flyer;
- DTO gerado não é passado por toda a árvore sem adapter de view quando a apresentação exige derivação;
- transformação musical não ocorre no adapter de view.

## Server e Client Components

### Server por padrão

Usar Server Components para:

- páginas públicas;
- conteúdo estático/editorial;
- layout e metadata;
- composição que não exige browser API.

### Client somente quando necessário

- dropzone;
- combobox;
- polling;
- localStorage seguro;
- sheets/dialogs interativos;
- controle de preview;
- View Transition iniciada por interação;
- componentes Motion;
- cenas GSAP lazy-loaded.

Adicionar `'use client'` no menor limite possível.

## API de componentes

Preferir props semânticas:

```ts
<TranspositionRoute
  source={sourceView}
  target={targetView}
  interval={intervalView}
  status="confirmed"
/>
```

Evitar prop soup:

```ts
<Component
  purple
  large
  rounded
  showArrow
  isMusic
  useGradient
  compactOnMobile
/>
```

Variações devem representar intenção, não classes CSS acidentais.

## Composition

Usar composição para componentes complexos somente quando a estrutura for estável e documentada. Não criar API compound apenas por moda.

Exemplo:

```tsx
<WarningPanel severity="warning">
  <WarningPanel.Title>Revise o compasso 18</WarningPanel.Title>
  <WarningPanel.Description>...</WarningPanel.Description>
  <WarningPanel.Action>Ver detalhes</WarningPanel.Action>
</WarningPanel>
```

## Estado e side effects

- query cache não é store global genérica;
- polling fica no feature `jobs`;
- toast não controla estado de domínio;
- URL contém `job_id` quando a rota precisa ser recuperável;
- preferences locais são versionadas;
- efeitos possuem cleanup e não continuam após estado terminal;
- cada nó possui uma única engine proprietária;
- GSAP usa `useGSAP`, refs/escopo local e não seleciona DOM global;
- scene components não implementam regra musical nem dependem da estrutura interna do renderer.

## Erros

- error boundaries por shell/feature;
- erro de rota, rede e domínio possuem componentes distintos;
- `correlation_id` é exibido apenas quando útil ao suporte;
- mensagem externa nunca é HTML.

## Critérios

- nenhum componente de página ultrapassa responsabilidade clara;
- componentes de produto podem ser demonstrados isoladamente;
- não há regra musical em hooks de UI;
- não há duplicação de layouts desktop/mobile quando CSS/composição resolve;
- dependência de browser fica confinada a Client Components;
- `SignatureTranspositionScene` possui fallback estático e boundary próprio;
- a rota não importa GSAP diretamente; importa o componente de cena de forma dinâmica.
