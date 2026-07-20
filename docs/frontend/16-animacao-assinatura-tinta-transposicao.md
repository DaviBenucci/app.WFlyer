# Animação-assinatura — tinta musical em transposição

> Status: canônico para a cena de identidade do W_Flyer. Revisão: 2026-07-20.

## Nome interno

```text
Ink Transfer / Transferência de Tinta
```

## Objetivo de produto

Representar visualmente o princípio do W_Flyer: a escrita muda de uma partitura para outra, enquanto a intenção musical é preservada.

A cena deve parecer parte do domínio musical, não uma animação abstrata de partículas. Ela usa notas, pauta, tinta e trajetória para explicar origem, intervalo e destino.

## Regra semântica

A animação não é o motor musical e não pode afirmar que uma nota real já foi processada.

- Na Home, usa uma demonstração musical fixa e correta.
- Durante processamento, é uma metáfora de atividade, acompanhada do estágio real em texto.
- No Resultado, só revela o destino depois que o backend retorna estado terminal válido.
- Não converte pixels, não lê MusicXML e não calcula intervalo.

## Contextos aprovados

### 1. Entrada pública

Ao entrar pela primeira vez na sessão:

- a pauta de origem é desenhada discretamente;
- algumas notas aparecem como tinta impressa;
- cópias de tinta se desprendem e percorrem uma curva;
- a pauta de destino é revelada;
- as notas são recompostas na nova altura escrita;
- o `TranspositionRoute` apresenta origem, intervalo e destino.

A cena ocorre integrada ao hero; não é splash screen e não bloqueia CTA, navegação ou leitura.

### 2. Entrada no Studio

Na primeira abertura de `/transpor`:

- `ScoreSurface` entra por opacidade e pequeno deslocamento;
- o inspector acompanha após 60–100 ms;
- a rota de transposição desenha somente quando origem e destino são definidos;
- a cena cinematográfica completa não se repete.

### 3. Processamento

Pode existir uma versão curta e abstrata:

- uma pequena gota/traço cruza a rota;
- a etapa textual muda somente com o `stage` real;
- o loop não simula porcentagem;
- o loop pausa em aba oculta e encerra em estado terminal.

### 4. Revelação do resultado

Quando o resultado válido chega:

- o destino recebe um breve desenho de tinta;
- o `TranspositionRoute` preserva continuidade visual;
- warnings entram antes das ações de download;
- não há confete ou celebração genérica.

## Storyboard da entrada pública

Duração alvo: 1,4 a 1,8 segundo. O conteúdo textual já existe no DOM desde o primeiro frame.

```text
0–180 ms
pauta de origem desenha; labels já estão legíveis

140–380 ms
4–6 glifos musicais surgem com opacidade e pequeno scale

340–780 ms
clones de tinta se desprendem; a origem permanece legível

460–980 ms
clones percorrem curvas Bézier em stagger curto

720–1120 ms
pauta de destino e barra de compasso são desenhadas

900–1380 ms
glifos se recompõem na posição transposta

1200–1600 ms
rota, intervalo e CTA assentam; timeline encerra totalmente
```

Não manter animação contínua após a conclusão.

## Linguagem visual

- tinta principal: token `--ink-primary`;
- tinta em trânsito: token `--ink-motion`, com contraste controlado;
- papel: superfície do design system;
- trajetória: curva fina que lembra fraseado, não neon;
- no máximo 6 glifos em movimento;
- notas usam SVG próprio ou fonte musical licenciada/aprovada;
- nenhuma partícula aleatória fora da trajetória;
- nenhum glow forte, blur amplo ou explosão.

## Arquitetura de componentes

```text
SignatureTranspositionScene
├── SceneA11ySummary
├── SourceStaff
│   └── SourceGlyphs
├── InkTravelLayer
│   ├── MotionPaths
│   └── InkGlyphClones
├── TargetStaff
│   └── TargetGlyphs
└── SceneLabels
    └── TranspositionRoute
```

Props orientativas:

```ts
type SignatureTranspositionSceneProps = {
  sourceInstrument: InstrumentView
  targetInstrument: InstrumentView
  interval: IntervalView
  mode: 'intro' | 'processing' | 'result'
  autoplay?: boolean
  onComplete?: () => void
}
```

A cena recebe dados de apresentação já validados. Não recebe DTO bruto nem implementa regra musical.

## Implementação com GSAP

Plugins aprovados:

```text
@gsap/react
MotionPathPlugin
DrawSVGPlugin, quando o desenho da pauta justificar
```

`MorphSVGPlugin` não é requisito. Para o MVP, mover cópias de glifos e usar máscaras é mais previsível do que morphing entre formas musicais diferentes.

Padrão obrigatório:

```tsx
'use client'

const root = useRef<SVGSVGElement>(null)

useGSAP(() => {
  if (shouldReduceMotion) return

  const timeline = gsap.timeline({ paused: !autoplay })
  // passos da cena usando refs/seletores restritos ao root

  return () => timeline.kill()
}, {
  scope: root,
  dependencies: [autoplay, sceneKey],
  revertOnUpdate: true,
})
```

A implementação real deve usar refs ou seletores escopados. O código acima é apenas contrato arquitetural.

## Como criar o efeito de tinta

### Estratégia MVP

1. desenhar duas pautas SVG determinísticas;
2. renderizar os glifos de origem;
3. duplicar 4–6 glifos para a camada de trânsito;
4. aplicar `clipPath`/`mask` simples para parecer que a tinta se desprende;
5. mover clones em paths curvos com `MotionPathPlugin`;
6. reduzir opacidade dos clones perto do destino;
7. revelar os glifos finais com máscara/desenho curto;
8. remover/ocultar clones ao encerrar.

Animar preferencialmente:

```text
transform
opacity
stroke-dashoffset/path drawing controlado
```

Evitar filtros SVG recalculados a cada frame. `feTurbulence` pode existir em imagem estática ou trecho muito curto somente após benchmark, nunca como base do efeito.

## Posição musical demonstrativa

A Home usa exemplo fixo e auditado, como:

```text
Piano em C -> Trompete em Bb
Segunda maior acima (+2 semitons)
```

Os glifos de destino devem representar uma transformação coerente. Não escolher posições apenas por estética.

## Partitura real do usuário

### MVP Core

Não animar diretamente as notas reais do arquivo enviado. O renderer pode gerar SVG sem IDs estáveis, e inferir a semântica pela árvore visual criaria acoplamento frágil.

### Evolução futura

A animação com dados reais só é aprovada quando o pipeline fornecer um `NoteGeometryMap` versionado:

```ts
type NoteGeometryMap = {
  sourceEventId: string
  targetEventId: string
  sourceBox: Rect
  targetBox: Rect
  sourcePitch: string
  targetPitch: string
}[]
```

Requisitos:

- IDs musicais estáveis entre normalizado e transposto;
- geometria emitida por adapter de renderização;
- limite de eventos animados;
- fallback para crossfade;
- nenhum parsing heurístico de classes internas do renderer.

## Reprodução e frequência

- autoplay somente na primeira visita da sessão ou quando explicitamente necessário;
- registrar `wflyer.motion.introSeen` em `sessionStorage`, sem informação pessoal;
- não repetir após voltar à Home na mesma sessão;
- oferecer replay apenas em contexto editorial, não no fluxo operacional;
- nunca iniciar som automaticamente;
- a cena não deve capturar scroll ou impedir interação.

## Reduced motion

Com preferência reduzida:

```text
pauta e notas já aparecem prontas
origem/destino usam crossfade de 80–140 ms ou troca imediata
a trajetória é estática
não há deslocamento longo, partículas ou parallax
o texto completo permanece visível
```

A variante reduzida não é uma timeline acelerada; é uma composição diferente.

## Falha de carregamento

Se GSAP ou o chunk falhar:

- mostrar SVG estático;
- não ocultar CTA;
- não emitir erro de produto ao usuário;
- registrar falha técnica sem dados do arquivo;
- não tentar carregar infinitamente.

## Orçamento de performance

Baseline inicial:

```text
máximo de 12 nós SVG animados simultaneamente
máximo de 1 timeline cinematográfica ativa
nenhum loop na Home após a entrada
chunk GSAP ausente das rotas que não usam cena
sem layout thrashing por leitura/escrita alternada em frame
cena pausada em document.visibilityState !== 'visible'
```

A aprovação depende de medição em dispositivo móvel intermediário, não apenas desktop de desenvolvimento.

## Estados de teste

- autoplay normal;
- intro já vista;
- reduced motion;
- background/foreground;
- navegação antes de concluir;
- Strict Mode;
- resize durante a cena;
- erro de chunk;
- instrumentos/labels longos;
- contraste/forced colors;
- zoom 200%.

## Critérios de aceite

- explica transposição sem prometer processamento real;
- CTA e conteúdo são utilizáveis desde o início;
- dura menos de dois segundos na entrada padrão;
- não se repete continuamente;
- usa SVG determinístico e exemplo musical correto;
- reduz ou remove deslocamento conforme preferência;
- timeline é destruída ao desmontar/navegar;
- não carrega GSAP onde não é necessário;
- mantém identidade mesmo no fallback estático.
