# Layout responsivo e estratégia de entrega

> Status: canônico para estrutura de página. Revisão: 2026-07-20.

## Objetivo

Construir uma experiência adaptativa e orientada ao conteúdo. Responsividade no W_Flyer não significa apenas empilhar colunas: cada componente deve mudar sua composição conforme o espaço disponível e o estágio do fluxo.

## Ordem de trabalho

```text
contrato OpenAPI + estado de domínio
-> wireframe de conteúdo real
-> componente/tela mínima integrada
-> estados e acessibilidade
-> refinamento visual
-> regressão visual e desempenho
```

Mocks podem ser usados em Storybook para estados difíceis, mas o fluxo de produto só é concluído quando utiliza API real.

## App shells

```text
RootLayout
  SkipLink
  SessionBootstrap
  GlobalStatus
  PublicShell | StudioShell | UtilityShell
```

### PublicShell

```text
PublicHeader
Main
Footer
```

### StudioShell

```text
StudioHeader
DesktopNavigationRail | MobileBottomNav
MainWorkspace
  WorkspaceCanvas
  ContextInspector
StickyActionBar
```

### UtilityShell

```text
CompactHeader
DesktopNavigationRail | MobileBottomNav
PageContainer
```

## Breakpoints orientativos

```text
compact: < 640px
mobile-wide: 640px a 767px
tablet: 768px a 1023px
desktop: 1024px a 1439px
wide: >= 1440px
```

Breakpoints de viewport são fallback. Componentes reutilizáveis devem preferir **container queries** para responder ao espaço real do pai.

## Larguras e densidade

```text
conteúdo editorial: 720px a 780px
landing/page pública: até 1180px
workspace: largura total, com gutters controlados
inspector desktop: 320px a 400px
navigation rail: 64px a 76px
```

Não aplicar um único `max-width` a todas as páginas. A tela de partitura necessita mais área horizontal que páginas de leitura.

## Desktop

### Public pages

- header horizontal compacto;
- navegação textual curta;
- conteúdo com composição assimétrica;
- CTA sem disputar com a marca;
- sem sidebar permanente.

### Workspace

- rail estreito para destinos estáveis;
- canvas principal para arquivo, resumo e estado;
- inspector à direita para decisões e ações;
- action bar fixa apenas durante etapas que exigem continuidade;
- inspector pode colapsar, mas a ação crítica não depende de hover.

## Tablet

- rail pode virar header compacto;
- inspector passa a drawer ou painel abaixo do canvas;
- comparação lado a lado só existe quando houver largura útil;
- botões não são reduzidos a ícones quando o significado ficar ambíguo.

## Mobile

- fluxo em uma coluna;
- bottom navigation somente em destinos estáveis;
- formulário dividido por seções, não por modais encadeados;
- ação primária em sticky action bar acima da safe area;
- teclado não encobre o campo, a lista ou a ação;
- preview/arquivo mantém proporção e permite zoom sem gesto exclusivo;
- área de toque do produto: mínimo de 44 x 44 CSS px.

## Composição adaptativa de componentes

### InstrumentPicker

```text
>= 720px no container: combobox + resumo lateral
< 720px: campo + sheet de seleção
```

### TranspositionRoute

```text
wide: origem -> trajetória -> destino
compact: origem / intervalo / destino em pilha
```

### ResultWorkspace

```text
wide: preview + inspector de downloads/warnings
compact: resumo -> warnings -> preview -> downloads
```

### HistoryList

```text
wide: tabela/lista estruturada
compact: linhas empilhadas, não cards decorativos independentes
```

## Estados globais

```text
session_bootstrapping
api_unavailable
offline
route_loading
reduced_motion
storage_unavailable
error_boundary
```

Estados de job vêm dos DTOs; não criar enums visuais incompatíveis.

## Loading e estabilidade de layout

- reservar espaço para conteúdo assíncrono conhecido;
- skeleton deve reproduzir a estrutura, não uma coleção genérica de retângulos;
- evitar trocar bruscamente a largura do inspector;
- fontes e imagens devem carregar sem deslocar a página;
- feedback de rede não deve substituir o estado do job.

## Critérios de aceite

- fluxo principal funciona entre 320px e telas ultrawide;
- zoom de 200% não cria sobreposição ou perda de ação;
- cada shell mantém hierarquia própria;
- container queries são usadas nos componentes que aparecem em mais de um contexto;
- bottom nav, rail e action bar não cobrem conteúdo;
- teclado, safe area e orientação horizontal são testados;
- loading, vazio, erro, offline, warning e sucesso possuem layouts estáveis;
- frontend não calcula nem envia intervalo autoritativo.
