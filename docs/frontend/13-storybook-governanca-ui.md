# Storybook e governança da UI

> Revisão: 2026-07-20.

## Objetivo

Usar Storybook como catálogo executável dos componentes e estados, não como vitrine opcional.

## Escopo mínimo

Todo componente em `components/product/` deve possuir stories aplicáveis para:

```text
default
hover/focus quando relevante
disabled
loading
empty
error
conteúdo longo
mobile/container compacto
reduced motion
high contrast quando possível
```

## Stories obrigatórias

```text
FileDropzone
InstrumentPicker
TranspositionRoute
ProcessingTimeline
WarningPanel
ArtifactRow
ExpirationNotice
HistoryRow
ScoreSurface
StickyActionBar
```

## Interação

- stories com `play` para teclado e fluxos críticos;
- addon de acessibilidade configurado para falhar CI em violações definidas;
- fixtures validadas contra contratos;
- nenhuma story depende de rede externa;
- estado do backend é representado por fixtures nomeadas, não booleanos vagos.

## Visual regression

- baseline versionado;
- revisão humana obrigatória;
- não aceitar diff global por mudança acidental de token;
- componentes de motion possuem captura em estado estável;
- fontes e timezone fixados no ambiente de teste.

## Documentação

Cada componente do produto deve registrar:

- propósito;
- quando usar;
- quando não usar;
- estrutura/composição;
- estados;
- acessibilidade;
- exemplos de conteúdo real;
- dependências de capability.

## Governança

Alteração em token global exige:

1. diff visual dos componentes afetados;
2. teste de contraste;
3. checagem de páginas principais;
4. registro no changelog quando perceptível;
5. aprovação de design/UX.

## Gate

A Fase 7 não termina sem:

- catálogo dos componentes do produto;
- testes de interação críticos;
- acessibilidade automatizada;
- visual regression revisada;
- estados de erro e conteúdo extremo demonstrados.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Referências e matriz de estados

Cada story crítica deve declarar:

```text
reference_id
capability
fixture_id
state
viewport
expected_warnings
keyboard_path
reduced_motion_behavior
```

Stories obrigatórias adicionais:

- diff completo, parcial e criativo;
- melodia com ambiguidade material/bloqueante;
- tocabilidade `UNKNOWN`, warning e blocking;
- variantes iguais/sem variante válida;
- áudio sem mapa compatível;
- conflito de revisão;
- anotação órfã;
- score/parte divergente.

## Política de baseline

- baseline é gerado em ambiente fixado;
- atualização exige reviewer e motivo;
- mudança de token pode atualizar várias imagens, mas não elimina revisão;
- antialiasing/fonte podem causar ruído; limiar automatizado não decide qualidade;
- screenshot não substitui teste de teclado, foco, leitura de tela e estado.

## Stories mínimas da expansão crítica

- `TransposeWorkspace`: incompatibilidade, review, falha transitória, expiração;
- `MelodyReview`: candidatos, cross-staff, conflito de revisão;
- `MusicalDiff`: determinístico, criativo, parcial, revogado;
- `HarmonyLab`: profile incompleto, variantes, nenhuma válida;
- `PlayabilityReport`: warning, blocking, explicação e alternativa;
- `PlaybackTransport`: ready, mapping partial, audio unavailable, background resume;
- `EnsemblePackage`: building, inconsistency, complete, revoked;
- `PersistentRecoveryPanel`: retry, user action, configuration change, incident;
- todos em mobile, 200% zoom, forced colors e reduced motion.

Stories devem usar fixtures versionadas; não mockar estado “bonito” que a API não consegue produzir.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Integração com a toolchain

- Storybook usa MSW para cenários de rede reutilizáveis;
- stories críticas participam dos testes de interação;
- Vitest Browser é preferido quando APIs reais do navegador forem relevantes;
- Playwright valida páginas e fluxos completos;
- Nx executa apenas stories/testes afetados quando a configuração de inputs estiver correta;
- Style Dictionary gera tokens; stories nunca editam outputs gerados;
- Biome e TypeScript são gates antes do build do Storybook.

Consultar `../implementacao/18-frontend-toolchain-testes.md`.
