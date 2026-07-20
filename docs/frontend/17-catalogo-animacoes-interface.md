# Catálogo de animações da interface

> Status: canônico para microinterações e transições do frontend. Revisão: 2026-07-20.

## Objetivo

Padronizar quando, por que e como um componente se move. A IA não deve inventar uma animação diferente em cada página.

## Princípios

1. estado antes de espetáculo;
2. continuidade antes de entrada repetitiva;
3. transform/opacity antes de propriedades de layout;
4. duração curta para tarefas frequentes;
5. uma animação não pode atrasar uma ação;
6. todo efeito possui versão sem movimento;
7. nenhuma animação substitui texto, foco ou status real.

## Catálogo

| Componente/contexto | Evento | Comportamento | Engine | Duração |
|---|---|---|---|---|
| PublicHeader | primeira entrada | fade + 6–10 px vertical | Motion | 220 ms |
| Navegação ativa | mudança de rota | underline/shared marker com `layoutId` | Motion | 220 ms |
| CTA | hover/tap | cor/elevação mínima; scale máximo 0,98 no tap | CSS/Motion | 80–140 ms |
| ScoreSurface | arquivo arrastado | realce de borda/fundo, sem pulsação contínua | CSS | 140 ms |
| ScoreSurface | arquivo aceito | confirmação breve por linha/barra | Motion | 220–320 ms |
| FileSummary | substituição | crossfade mantendo altura quando possível | Motion | 180–220 ms |
| InstrumentPicker | abrir/fechar | sheet/dialog padrão com foco correto | Motion/primitiva | 180–260 ms |
| Lista de instrumentos | filtrar | itens entram/saem sem cascata longa | Motion | 140–220 ms |
| TranspositionRoute | origem/destino muda | layout compartilhado + desenho curto da rota | Motion | 220–320 ms |
| ProcessingTimeline | stage muda | marcador e texto fazem transição; sem porcentagem falsa | Motion | 180–240 ms |
| ProcessingInkLoop | job ativo | loop abstrato limitado, pausável | GSAP | 1,8–2,8 s |
| WarningPanel | abrir detalhes | expansão com altura/opacity e foco preservado | Motion | 180–260 ms |
| ArtifactRow | download disponível | ação aparece por opacity, sem bounce | Motion | 180 ms |
| Resultado | completed | revelação da tinta + warnings/ações em sequência curta | GSAP + Motion separados | 700–1100 ms |
| HistoryRow | remover/reordenar | saída e relayout | Motion | 180–260 ms |
| Toast | aparecer/sair | deslocamento pequeno + opacity | Motion/primitiva | 180–220 ms |
| Skeleton | carregamento real | shimmer CSS opcional; desativado em reduced motion | CSS | controlado |

## Entrada das páginas

### Páginas públicas

- animar no máximo hero, demonstração e uma região secundária;
- evitar stagger em todos os textos;
- elementos abaixo da dobra usam `whileInView` apenas quando agrega leitura;
- não reiniciar animação ao voltar pelo histórico do navegador quando isso causar distração.

### Studio

- shell permanece estável entre Transpor e Resultado;
- preferir continuidade de elementos a desmontar/remontar tudo;
- `ScoreSurface` e `TranspositionRoute` podem usar `layoutId` quando a estrutura permitir;
- inspector entra discretamente, sem slide de longa distância;
- foco é movido por lógica de acessibilidade, não pela animação.

### Utility

Histórico e Configurações priorizam rapidez. Não usar cenas cinematográficas.

## Variants orientativas do Motion

```ts
export const enterRegion = {
  hidden: { opacity: 0, y: 8 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { duration: 0.22, ease: [0.16, 1, 0.3, 1] },
  },
}
```

```ts
export const fadeSwap = {
  initial: { opacity: 0 },
  animate: { opacity: 1 },
  exit: { opacity: 0 },
}
```

Valores finais devem consumir tokens compartilhados. Variants não são copiados e alterados localmente sem necessidade.

## Gestos

- hover nunca é único meio de descobrir ação;
- tap não reduz componente abaixo de tamanho legível;
- drag possui botão/alternativa equivalente;
- nenhuma navegação depende de swipe;
- evitar magnetic cursor, tilt 3D e perseguição do ponteiro;
- não animar em resposta a cada pixel do mouse sem função operacional.

## Loading e processamento

### Permitido

- skeleton de estrutura conhecida;
- indicador indeterminado explicitamente rotulado;
- timeline de stages reais;
- animação abstrata curta enquanto um stage está ativo.

### Proibido

- barra falsa que avança até 90%;
- mostrar “Transpondo notas” quando o backend ainda está validando upload;
- reiniciar a animação em cada polling;
- manter loop após `completed`, `failed` ou `cancelled`;
- usar animação como única indicação de atividade.

## Erros e warnings

- erro entra uma vez e recebe foco programático apropriado;
- não balançar formulário repetidamente;
- warning não pulsa indefinidamente;
- mudança de severidade não depende apenas de cor;
- retry inicia apenas após ação explícita ou política documentada.

## Sons

O MVP não possui sons de interface automáticos. Qualquer feedback sonoro futuro exige:

- opt-in;
- volume/configuração;
- alternativa visual;
- respeito a preferências do sistema;
- ADR específico.

## View Transitions

A API nativa pode ser usada como progressive enhancement para continuidade entre rotas. Motion continua responsável por componentes React internos. Não combinar View Transition e `layoutId` sobre o mesmo elemento sem teste e decisão explícita.

## Antipadrões

- todos os elementos entrando com fade-up;
- stagger longo em formulários;
- bounce em ações sérias;
- parallax no workspace;
- cursor personalizado;
- notas flutuando continuamente;
- card que levita em qualquer hover;
- animação que altera layout durante digitação;
- duração superior a 400 ms em ação frequente;
- spring “wobbly” em texto, warnings ou arquivos.

## Critérios de aceite

- cada animação está associada a evento/estado claro;
- efeitos repetitivos usam tokens e variants compartilhados;
- reduced motion foi definido;
- teclado e foco funcionam durante entrada/saída;
- nenhuma ação espera a animação terminar;
- loops param em background/estado terminal;
- visual regression pode desativar motion de forma determinística.
