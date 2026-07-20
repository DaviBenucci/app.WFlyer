# Regressão visual e golden examples

> Status: canônico para frontend. Revisão: 2026-07-20.

## Fontes

- `../design-reference/reference-manifest.yaml`;
- stories aprovadas;
- screenshots gerados internamente;
- specifications de página/componente.

## Ambiente

Fixar:

```text
browser/version
OS/container
viewport
DPR
fontes
locale/timezone
data fixtures
reduced motion/color scheme
```

Comparação visual pode variar por ambiente; baselines são gerados e comparados no mesmo ambiente controlado.

## Cobertura

- desktop/mobile/tablet;
- conteúdo extremo;
- warnings e erros;
- loading/review/expired;
- zoom/reduced motion/forced colors quando aplicável;
- componentes de domínio;
- motion em frames-chave, não pixel diff de cada frame.

## Aprovação

CI detecta mudança; humano aprova intenção. Atualizar baseline exige:

- issue/PR explicando diferença;
- screenshot antes/depois;
- confirmação de acessibilidade;
- `reference_id`;
- ausência de regressão de estado.

## Proibições

- threshold amplo para esconder alteração;
- update automático de todos os baselines;
- dados aleatórios/data atual em snapshot;
- depender de asset externo instável.
