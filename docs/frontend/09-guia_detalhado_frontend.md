# Frontend — guia detalhado do Core

> Status: canônico para execução do frontend. Revisão: 2026-07-20.

## Objetivo

Entregar uma ferramenta musical moderna, específica e acessível. O frontend apresenta domínio e estado; regras musicais autoritativas continuam no backend.

## Leitura obrigatória

1. `00-direcao-visual-wflyer.md`
2. `01-layout-responsivo.md`
3. `05-design-system.md`
4. `06-acessibilidade.md`
5. `08-contratos-api-frontend.md`
6. `10-arquitetura-componentes.md`
7. `11-conteudo-microcopy.md`
8. `12-performance-qualidade-visual.md`
9. `13-storybook-governanca-ui.md`
10. `14-antipadroes-interface-ia.md`
11. `15-arquitetura-motion-e-bibliotecas.md`
12. `16-animacao-assinatura-tinta-transposicao.md`
13. `17-catalogo-animacoes-interface.md`
14. `../qa/09-testes-motion-performance.md`

## Stack e estratégia

```text
Next.js App Router
React Server Components por padrão
TypeScript strict
Tailwind CSS com tokens semânticos
shadcn/ui + primitives headless adaptados
TanStack Query para estado remoto necessário
React Hook Form + Zod nas fronteiras de formulário
Storybook
Testing Library
Playwright
Motion for React para animações da UI
GSAP + @gsap/react para a cena de tinta isolada
```

Não transformar toda página em Client Component. Interatividade fica em ilhas pequenas e explícitas.

## Fluxo principal

```text
bootstrap da sessão
-> carregar capabilities e instrumentos
-> upload validado
-> configurar origem e destino
-> revisar intervalo retornado
-> criar job idempotente
-> acompanhar etapas reais
-> revisar warnings
-> baixar artefato
-> manter referência segura no histórico local
```

## Composição da tela Transpor

O fluxo não deve parecer um wizard genérico de seis telas. Preferir um workspace progressivo:

```text
ScoreSurface
  arquivo/estado/preview

ContextInspector
  origem
  destino
  formato
  resumo

StickyActionBar
  ação disponível para o estado atual
```

No mobile, os blocos ficam em sequência e o inspector vira seção/sheet conforme a tarefa.

## Componentes mínimos

```text
SessionBootstrap
CapabilityGate
PublicHeader
DesktopNavigationRail
MobileBottomNav
ScoreSurface
UploadDropzone
FileSummary
InstrumentPicker
TranspositionRoute
ProcessingTimeline
WarningPanel
ArtifactRow
ExpirationNotice
StickyActionBar
SignatureTranspositionScene
ProcessingInkLoop
HistoryRow
SettingsSection
ErrorState
EmptyState
```

## Regras de domínio na UI

- backend calcula intervalo autoritativo;
- mostrar nome diatônico, semitons e oitava quando relevante;
- origem e destino sempre têm labels explícitos;
- warning material aparece antes do download;
- capability desabilitada não aparece como funcional;
- `expired` não é falha de processamento;
- erro de polling não vira `failed`;
- metadata local não concede acesso;
- engine/confidence bruta não aparece para usuário comum.

## Serviços

```text
sessionService
capabilitiesService
instrumentsService
uploadsService
transpositionsService
jobsService
artifactsService
```

Todos usam cliente gerado, `credentials: include`, envelope de erro e `correlation_id`.

## Estado

### Server state

TanStack Query ou adapter equivalente para:

- capabilities;
- instrumentos;
- job/status;
- artefatos.

### UI state

Estado local somente para:

- painel aberto;
- campo de busca;
- preferência visual;
- etapa de composição ainda não enviada;
- seleção temporária.

Não duplicar DTO inteiro em store global.

## Entrega por cortes

### Corte 1 — fundação visual

- tokens;
- shells;
- tipografia;
- navigation;
- Storybook;
- primitives adaptados.

### Corte 2 — seleção e upload

- ScoreSurface;
- UploadDropzone;
- FileSummary;
- InstrumentPicker;
- TranspositionRoute.

### Corte 3 — job

- criação idempotente;
- ProcessingTimeline;
- estados de rede e domínio;
- cancelamento.

### Corte 4 — resultado

- warnings;
- artefatos;
- retenção;
- deleção;
- histórico.

### Corte 5 — páginas públicas

- home;
- como funciona;
- instrumentos;
- conteúdo e metadata.

### Corte 6 — acabamento e motion

- responsividade por container;
- Motion for React nos componentes aprovados;
- animação-assinatura `Ink Transfer` com GSAP lazy-loaded;
- View Transitions progressivas;
- fallback estático e reduced motion;
- visual regression;
- acessibilidade manual;
- performance, cleanup e bundle por rota.

Cada corte inclui estados em Storybook e testes de integração aplicáveis.

## Segurança

- CSRF somente em memória;
- nenhum token/cookie em log ou storage;
- filename renderizado como texto;
- download por endpoint autorizado;
- sem `dangerouslySetInnerHTML` para mensagens externas;
- validar URL/redirecionamento;
- não cachear respostas `no-store`.

## Gate de conclusão

- fluxo real funciona em desktop/mobile;
- página Transpor usa StudioShell e não wizard genérico;
- componentes não mantêm aparência padrão do shadcn/ui;
- estados difíceis estão documentados em Storybook;
- teclado, leitor de tela, zoom, forced colors e reduced motion foram avaliados;
- orçamento de bundle e Core Web Vitals não regrediram;
- nenhuma capability futura aparece como funcional;
- análise visual confirma identidade própria do W_Flyer;
- animação de entrada não bloqueia conteúdo e toca no máximo uma vez por sessão;
- GSAP não está presente em rotas sem cena e nenhuma engine disputa propriedades;
- reduced motion, interrupção de rota e cleanup foram testados.
