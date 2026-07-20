# Performance e qualidade visual

> Revisão: 2026-07-20.

## Objetivo

A aparência moderna não pode ser obtida à custa de JavaScript excessivo, instabilidade visual ou processamento no cliente.

## Estratégia

- React Server Components por padrão;
- Client Components somente para interação;
- lazy loading do preview/renderizador e bibliotecas pesadas;
- CSS nativo antes de dependência de motion;
- Motion for React para UI declarativa; GSAP somente em cenas lazy-loaded;
- Anime.js e React Spring ausentes do bundle do Core;
- icons importados individualmente;
- sem Canvas/WebGL decorativo no Core;
- fontes otimizadas e sem requisição externa em runtime;
- imagens com dimensões reservadas;
- listas extensas virtualizadas somente quando medição justificar.

## Orçamentos iniciais

São metas para baseline, não autorização para ignorar análise de rota:

```text
LCP: <= 2.5s no percentil 75
INP: <= 200ms no percentil 75
CLS: <= 0.1 no percentil 75
```

No laboratório:

- nenhuma regressão relevante de Lighthouse sem justificativa;
- rota pública não carrega preview musical pesado;
- dependência nova acima de 50 kB gzip exige registro de decisão;
- bundle da rota Transpor é medido antes/depois de editor, preview ou motion;
- animações não mantêm CPU ativa em aba oculta;
- máximo inicial de 12 nós SVG animados na cena de tinta;
- somente uma timeline cinematográfica ativa;
- GSAP ausente das rotas sem cena;
- CTA/LCP textual não aguardam o chunk de animação.

## Motion e cenas SVG

- `SignatureTranspositionScene` é carregada dinamicamente;
- fallback SVG estático reserva a mesma área para evitar CLS;
- preferir `transform`, `opacity` e path drawing controlado;
- evitar filtros SVG recalculados por frame;
- pausar loops com `document.visibilityState`;
- destruir timelines/RAF/listeners ao desmontar;
- medir em dispositivo móvel intermediário e navegação repetida;
- o visual final precisa continuar coerente com motion desabilitado.

## Score preview

- carregar sob demanda;
- preferir SVG/HTML acessível quando o renderer oferecer;
- não enviar MusicXML inteiro para analytics/log;
- worker de browser somente se houver tarefa real aprovada;
- preview não é requisito para iniciar o Core quando engine não está habilitada.

## Fontes

- usar `next/font` ou arquivos locais aprovados;
- subset de caracteres quando aplicável;
- `font-display` e métricas de fallback alinhadas;
- no máximo duas famílias;
- evitar múltiplos pesos estáticos quando uma variável resolve.

## Visual regression

Capturar páginas/componentes com conteúdo determinístico:

```text
mobile 320/390
 tablet 768
 desktop 1280
 wide 1600
 zoom/reflow selecionado
 tema suportado
```

Não aprovar mudança somente atualizando snapshots. O diff precisa ser revisado.

## Conteúdo extremo

Testar:

- nome de arquivo longo;
- instrumento com nome longo;
- 0, 1 e muitos warnings;
- erro multilinha;
- histórico vazio e com muitos itens;
- tradução futura com expansão de texto;
- progresso 0 e 100;
- data de expiração extensa.

## Critérios

- rotas públicas não carregam dependências do workspace sem necessidade;
- heavy components são lazy-loaded;
- layout não muda após fonte/preview;
- polling reduz frequência em background;
- a identidade visual permanece sem animações e assets pesados.
