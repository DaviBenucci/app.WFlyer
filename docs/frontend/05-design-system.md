# Design system W_Flyer

> Status: canônico para tokens e componentes. Revisão: 2026-07-20.

## Arquitetura

```text
tokens
-> primitives
-> components
-> patterns
-> page compositions
```

O projeto pode usar componentes headless por meio de shadcn/ui, Base UI ou adapter equivalente. A biblioteca fornece comportamento; **a identidade visual pertence ao W_Flyer**. Não copiar tema, radius e composição padrão sem revisão.

## Relação com a marca

Este documento define o sistema visual provisório da aplicação. Ele não aprova logo, wordmark, tipografia institucional ou paleta corporativa. Antes de usar qualquer ativo de marca, consultar `../../brand/brand-manifest.yaml`.

## Tokens semânticos

Usar CSS variables e, no Tailwind CSS atual, mapear tokens apropriados em `@theme`. Valores abaixo são baseline para protótipo e devem passar por contraste e revisão visual.

```css
:root {
  --wf-background: oklch(0.982 0.008 86);
  --wf-foreground: oklch(0.19 0.025 278);
  --wf-surface: oklch(0.995 0.004 88);
  --wf-surface-muted: oklch(0.955 0.012 88);
  --wf-surface-strong: oklch(0.925 0.018 280);
  --wf-border: oklch(0.875 0.018 278);
  --wf-border-strong: oklch(0.73 0.035 278);

  --wf-primary: oklch(0.55 0.22 291);
  --wf-primary-hover: oklch(0.49 0.23 291);
  --wf-primary-foreground: oklch(0.985 0.004 88);
  --wf-secondary: oklch(0.58 0.17 250);
  --wf-accent: oklch(0.70 0.13 196);

  --wf-success: oklch(0.56 0.15 154);
  --wf-warning: oklch(0.70 0.16 76);
  --wf-danger: oklch(0.57 0.21 27);
  --wf-info: oklch(0.59 0.16 247);

  --wf-focus: oklch(0.66 0.20 291);
  --wf-overlay: oklch(0.12 0.02 278 / 0.58);
}
```

## Tema escuro

A arquitetura de tokens deve permitir tema escuro, mas o Core só anuncia esse tema quando todas as páginas, previews, overlays, estados e contrastes estiverem validados. Não entregar dark mode parcial.

## Paleta e uso

- violeta: ação principal e trajetória de transposição;
- azul/cobalto: informação e origem;
- ciano controlado: destino ou destaque técnico;
- superfícies quentes: papel/partitura;
- cores de status são semânticas e não substituem texto/ícone.

Evitar gradientes em texto. Gradiente pode existir somente em áreas amplas e discretas da marca, nunca em controles ou mensagens de estado.

## Tipografia

### Interface

Usar uma sans variável de alta legibilidade, com fallback de sistema. Candidatos aprováveis após licença e benchmark:

```text
Geist Sans
Manrope
Inter Variable
```

### Editorial

Uma serif discreta pode aparecer em hero, citações técnicas e títulos editoriais. Não usar em formulários ou tabelas. Candidatos:

```text
Source Serif 4
Newsreader
```

### Regras

- carregar com `next/font` ou arquivos aprovados no repositório;
- evitar requisição externa em runtime;
- máximo de duas famílias;
- usar números tabulares em progresso, semitons, datas e medidas;
- line-height mais compacto em títulos e confortável em textos;
- escala fluida com `clamp()` onde fizer sentido.

Escala orientativa:

```text
caption: 12/16
body-sm: 14/20
body: 16/24
body-lg: 18/28
title-sm: 24/30
title: 32/38
display: clamp(40px, 6vw, 72px)
```

## Espaçamento e ritmo

Base de 4px, com decisões principais em múltiplos de 8px.

```text
4, 8, 12, 16, 24, 32, 48, 64, 96
```

Evitar que todo bloco tenha `padding: 24px`. Densidade varia por contexto:

- controles: compactos;
- workspace: médio;
- páginas editoriais: espaçamento amplo;
- tabelas/listas: densidade alta o suficiente para comparação.

## Radius

```text
xs: 4px
sm: 8px
md: 12px
lg: 18px
pill: 999px somente para chips/badges
```

Não aplicar `rounded-2xl` ou maior indiscriminadamente. Superfícies de partitura podem ter radius menor para lembrar papel e precisão.

## Elevação

- nível 0: sem sombra;
- nível 1: menu, popover e sheet;
- nível 2: dialog;
- usar borda antes de sombra em cards e painéis;
- glass/blur somente em header quando houver razão funcional e contraste comprovado.

## Iconografia

- um único conjunto de ícones lineares para ações comuns;
- ícones próprios para famílias de instrumentos e conceitos musicais quando necessário;
- stroke e tamanho consistentes;
- nenhuma ação importante usa apenas ícone sem nome acessível;
- evitar símbolos “mágicos” para processamento automático.

## Primitives

```text
Button
IconButton
Link
Input
Textarea
Field
Label
Checkbox
Switch
RadioGroup
Select
Combobox
Dialog
Sheet
Popover
Tooltip
Tabs
Separator
ScrollArea
Progress
Toast
```

## Componentes do produto

```text
ScoreSurface
FileDropzone
FileSummary
InstrumentPicker
InstrumentFamilyFilter
TranspositionRoute
IntervalBadge
ProcessingTimeline
JobStatusHeader
WarningPanel
ArtifactRow
ExpirationNotice
HistoryRow
CapabilityNotice
StickyActionBar
EmptyState
ErrorState
```

## Padrões de composição

### Formulários

- labels persistentes;
- ajuda abaixo do campo;
- erro próximo do campo e no resumo quando necessário;
- placeholders não substituem label;
- ação principal não fica distante do contexto;
- combobox de instrumentos agrupa por família e aceita aliases.

### Cards

Card não é container universal. Usar somente quando o conteúdo representa uma unidade independente. Preferir:

- seção com divider;
- lista estruturada;
- surface contínua;
- inspector;
- tabela responsiva.

### Feedback

- toast somente para confirmação transitória;
- erro que exige ação permanece na página;
- warning musical nunca desaparece apenas em toast;
- progresso possui etapa e texto, não apenas porcentagem.

## Microcopy

Usar termos concretos:

```text
“Segunda maior acima (+2 semitons)”
“Resultado pronto com 2 avisos para revisão”
“Este arquivo contém mais de uma pauta e não faz parte do Core atual”
```

Evitar:

```text
“Algo mágico está acontecendo”
“Deixe a IA fazer o trabalho”
“Revolucione sua música”
```

## Gate

Um componente só é “pronto” quando possui:

- API de props restrita e documentada;
- estados reais em Storybook;
- teclado e leitor de tela;
- contraste;
- mobile/container query;
- loading, erro e conteúdo longo;
- teste de interação;
- aprovação visual fora do tema padrão da biblioteca.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Tokens e componentes de análise musical

Adicionar tokens semânticos para:

```text
--diff-preserved
--diff-transformed
--diff-generated
--diff-removed
--review-ambiguous
--review-blocking
--playability-impossible
--playability-difficult
--playability-unknown
--playback-cursor
--locked-melody
```

A cor nunca é o único canal; cada estado inclui label, ícone/forma e texto acessível.

## Componentes críticos

- `MusicalDiffNavigator`;
- `EventChangeInspector`;
- `AssuranceSummary`;
- `MelodyCandidatePanel`;
- `AnalysisRegionRail`;
- `PlayabilityReport`;
- `HarmonyVariantCard`;
- `ScorePartConsistencyNotice`;
- `PlaybackTransport`;
- `RehearsalOverlay`;
- `RevisionTimeline`;
- `AnnotationAnchor`.

Esses componentes não podem ser reduzidos a `Card` genérico sem API de domínio.

## Golden examples

Tokens e componentes devem ser demonstrados com fixtures reais/sintéticas controladas em Storybook. O arquivo `../design-reference/fixtures/ui-states.json` é ponto de partida; produção deverá usar mocks gerados do OpenAPI.

## Componentes profissionais adicionados

```text
MusicalDiffNavigator
EventProvenancePopover
ConfidenceRegionOverlay
MelodyCandidateLane
HarmonyVariantRail
TensionCurveEditor
PlayabilityFindingPanel
PlaybackTransport
ScoreFollowingCursor
RehearsalToolbar
EnsemblePartMatrix
ReviewThread
RevisionBadge
CapabilityGateNotice
PersistentRecoveryPanel
```

Cada componente deve possuir estados no `design-reference`/Storybook. Cores não são o único canal; eventos e findings têm rótulo, ícone/forma e texto.

`ScoreSurface` não pode depender da estrutura DOM privada de um renderer para identidade musical. Event IDs e geometria entram por adapter explícito.
