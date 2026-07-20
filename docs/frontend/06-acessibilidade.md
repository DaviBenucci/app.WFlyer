# Acessibilidade

> Meta: WCAG 2.2 nível AA para os fluxos públicos do Core. Revisão: 2026-07-20.

## Princípios

Acessibilidade faz parte do contrato do componente, não é etapa final de polimento.

## Requisitos globais

- landmarks semânticos;
- H1 único por página;
- navegação completa por teclado;
- ordem lógica de foco;
- foco visível com contraste e área suficientes;
- foco não encoberto por header, bottom nav, sheet ou action bar;
- labels persistentes;
- erros textuais e associados aos campos;
- status não depende apenas de cor;
- área de toque do produto: mínimo de 44 x 44 CSS px;
- suporte a zoom 200% e reflow;
- `prefers-reduced-motion`;
- alternativas para drag, swipe e hover;
- idioma da página e mudanças de idioma marcadas quando aplicável.

## Upload

- dropzone opera com Enter/Espaço;
- botão “Selecionar arquivo” sempre disponível;
- formato, limite e perfil suportado aparecem antes da seleção;
- erro é anunciado e mantém ação de correção;
- progresso de upload possui nome acessível.

## Seleção de instrumentos

- usar padrão de combobox válido;
- opções agrupadas por família sem criar navegação impossível;
- aliases são pesquisáveis;
- origem/destino são identificados por label, não apenas posição;
- estado selecionado usa texto, marca e cor;
- sheet mobile devolve foco ao campo ao fechar.

## TranspositionRoute

A representação visual origem → destino deve ter equivalente textual completo:

```text
Piano em C para Trompete em Bb, segunda maior acima, dois semitons.
```

Seta, linha e cor não são a única informação.

## Processamento

- região com `aria-live="polite"` anuncia mudança de etapa, não cada polling;
- progress bar possui valor e descrição;
- cancelamento é confirmável e acessível;
- erro recebe foco no título/resumo, sem mover foco repetidamente;
- perda de rede não anuncia job como falho.

## Preview de partitura

Quando houver preview visual:

- canvas/SVG não pode ser a única descrição do resultado;
- fornecer resumo textual: páginas, instrumento, tonalidade quando disponível e warnings;
- controles de zoom têm nome, estado e alternativa por teclado;
- pan/drag possui botões ou scroll padrão;
- contraste do preview não é alterado por filtros decorativos.

## Mobile

- bottom nav e action bar não encobrem foco;
- orientação horizontal continua funcional;
- teclado virtual não impede concluir o formulário;
- menus não exigem hover;
- textos longos não sobrepõem ícones.

## Movimento

Com `prefers-reduced-motion`:

- remover movimento não essencial;
- evitar scroll suave forçado;
- View Transitions usam fallback imediato;
- Motion usa `MotionConfig reducedMotion="user"` e variantes reduzidas;
- GSAP não cria trajetória longa; a cena `Ink Transfer` vira composição estática/crossfade;
- indicador de processamento mantém texto estático;
- nenhum conteúdo importante aparece somente depois de animação;
- a variante reduzida não é apenas a timeline normal executada mais rápido.

A animação de tinta possui resumo textual equivalente e nunca bloqueia CTA, foco ou navegação. Conteúdo e ações existem no DOM desde o primeiro frame.

## Testes

- fluxo completo só com teclado;
- NVDA ou leitor equivalente em pelo menos um navegador desktop;
- VoiceOver/TalkBack em uma amostra mobile;
- axe em Storybook e E2E;
- zoom 200%, texto ampliado e viewport 320px;
- high contrast/forced colors quando suportado;
- reduced motion;
- revisão manual dos critérios que automação não cobre.
