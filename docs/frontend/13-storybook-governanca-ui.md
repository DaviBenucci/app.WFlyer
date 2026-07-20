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
