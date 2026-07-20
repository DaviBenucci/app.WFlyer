# Arquitetura de motion e escolha de bibliotecas

> Status: canônico para animações do frontend. Revisão: 2026-07-20.

## Objetivo

Definir quais tecnologias controlam movimento no W_Flyer, em quais limites elas podem ser usadas e como evitar animações genéricas, concorrentes, excessivas ou difíceis de manter.

Motion não é uma camada decorativa separada. Ele comunica:

- entrada e saída de elementos;
- continuidade entre origem e destino;
- alteração de estado;
- progresso real do processamento;
- hierarquia e foco;
- identidade musical do produto.

## Decisão resumida

O W_Flyer adota uma arquitetura em três níveis:

```text
CSS nativo
  microestados simples e baratos

Motion for React
  animações declarativas da interface React

GSAP
  animação-assinatura SVG e sequências cinematográficas isoladas
```

Não usar Anime.js ou React Spring no MVP Core. A inclusão futura de uma quarta engine exige ADR e remoção de sobreposição funcional.

## Matriz comparativa

| Critério | Motion for React | GSAP | Anime.js | React Spring |
|---|---|---|---|---|
| Integração declarativa com estado React | Excelente | Boa com `@gsap/react`, porém imperativa | Possível, mas menos natural | Excelente |
| Entrada, saída e presença | Excelente | Possível com timeline/manual | Boa | Boa |
| Layout e shared element | Excelente | Exige estratégia adicional | Não é foco principal | Possível, menos direto |
| Timeline complexa e coreografia | Boa | Excelente | Muito boa | Limitada para cenas longas |
| SVG, paths e desenho de linhas | Muito boa | Excelente | Muito boa | Boa |
| Física de mola | Nativa | Disponível por easings/plugins | Disponível por easings | Principal especialidade |
| Gestos React/touch | Excelente | Boa com plugins/handlers | Exige mais composição | Boa |
| Curva de manutenção no Next.js | Baixa | Média | Média | Média |
| Adequação ao W_Flyer | UI cotidiana | Cena de transposição | Redundante com GSAP | Redundante com Motion |

## Escolha principal: Motion for React

Motion é a engine padrão dos componentes React porque fornece uma API declarativa ligada a props e estado, além de entrada, saída, layout, SVG, gestos e `useReducedMotion`.

Usos aprovados:

- `AnimatePresence` para erros, warnings, sheets e troca de estados;
- `layout` e `layoutId` para continuidade entre componentes;
- microinterações de botões, linhas, seletores e itens;
- expansão/reordenação de listas;
- transições do `TranspositionRoute`;
- entrada discreta de shells e regiões;
- SVG simples, como desenho de uma rota ou barra de compasso;
- gestos aprovados com alternativa por teclado.

Motion não deve ser usado para reproduzir uma timeline cinematográfica com dezenas de passos imperativos apenas porque já está instalado.

## Escolha especializada: GSAP

GSAP é aprovado somente para cenas com coreografia temporal avançada, especialmente a animação-assinatura da tinta musical. A integração React ocorre com `@gsap/react` e `useGSAP`, sempre em Client Component e com cleanup automático.

Usos aprovados:

- `SignatureTranspositionScene`;
- sequência SVG de tinta, notas e pauta;
- motion path da origem para o destino;
- desenho coordenado de linhas;
- timeline de revelação do resultado;
- demonstração editorial controlada na Home.

Usos proibidos:

- hover comum de botão;
- abertura de todo dialog/sheet;
- animações de formulário;
- substituir transições CSS simples;
- selecionar elementos globalmente fora do escopo do componente;
- manter timelines globais entre rotas;
- animar o mesmo elemento que Motion controla.

## Por que Anime.js não é a escolha do Core

Anime.js possui timeline, módulos granulares e utilitários SVG para morphing, line drawing e motion paths. Tecnicamente conseguiria implementar a cena da tinta. Entretanto, no W_Flyer ele ocuparia o mesmo espaço de GSAP sem oferecer vantagem suficiente para justificar duas engines imperativas.

Anime.js permanece uma alternativa de substituição, não dependência simultânea. Uma troca futura deve preservar a API interna da cena e os testes.

## Por que React Spring não é a escolha do Core

React Spring é forte em animações físicas e valores interativos. Contudo, Motion já oferece springs, presença, layout, gestos e integração suficiente para o produto. Adicionar React Spring duplicaria abstrações e aumentaria o custo cognitivo.

React Spring só deve ser reconsiderado se o produto introduzir uma interação física contínua que Motion não atenda de forma adequada, por exemplo uma superfície instrumental altamente manipulável.

## Regra de propriedade

Cada elemento visual possui exatamente um proprietário de animação:

```text
CSS | Motion | GSAP
```

Regras:

1. Motion e GSAP não animam simultaneamente a mesma propriedade do mesmo nó.
2. Um componente GSAP não expõe nós internos para Motion controlar.
3. Transformações compostas devem ter wrapper separado quando duas camadas forem necessárias.
4. `transition`, `animation` CSS e uma engine JS não disputam `transform` ou `opacity`.
5. A engine não altera estado de domínio; ela apenas representa estado já conhecido.

Exemplo de separação:

```tsx
<motion.section layout>
  <SignatureTranspositionScene />
</motion.section>
```

Motion controla o layout do `section`; GSAP controla apenas o SVG interno.

## Limites de Client Components

- Motion pode existir em pequenas ilhas de interação.
- GSAP fica em componentes marcados com `'use client'` e carregados sob demanda.
- Rotas públicas permanecem Server Components sempre que possível.
- A presença de motion não justifica transformar um layout inteiro em Client Component.
- Não importar GSAP em módulo executado no servidor.

## Carregamento

### Motion

Pode ser parte da camada interativa comum. Preferir importações específicas e avaliar `LazyMotion` quando o bundle justificar.

### GSAP

Carregar dinamicamente somente nas rotas/cenas que o utilizam:

```tsx
const SignatureTranspositionScene = dynamic(
  () => import('./signature-transposition-scene'),
  { ssr: false }
)
```

Plugins devem ser registrados no módulo cliente da cena. A animação precisa funcionar sem o bundle GSAP: o fallback é um SVG estático semanticamente completo.

## Configuração global de acessibilidade

A raiz interativa deve respeitar a preferência do usuário:

```tsx
<MotionConfig reducedMotion="user">
  {children}
</MotionConfig>
```

A cena GSAP consulta `prefers-reduced-motion` e seleciona a variante estática/reduzida antes de criar a timeline.

## Tokens de motion

```text
motion.instant    80ms
motion.fast       140ms
motion.standard   220ms
motion.slow       320ms
motion.scene      1200–1800ms
```

Easings:

```text
enter   cubic-bezier(0.16, 1, 0.3, 1)
exit    cubic-bezier(0.7, 0, 0.84, 0)
move    cubic-bezier(0.22, 1, 0.36, 1)
linear  somente para progresso/path quando semanticamente necessário
spring  somente em resposta direta do usuário
```

Valores concretos são exportados por tokens, não repetidos aleatoriamente em componentes.

## Política de dependências e licença

- versão exata fixada em lockfile;
- dependências registradas no inventário de terceiros;
- Motion Core é tratado como dependência open source;
- GSAP é atualmente gratuito sob licença própria e deve ter sua licença registrada no repositório;
- plugins usados devem ser listados explicitamente;
- upgrade de major version exige regressão visual, reduced motion e benchmark da cena;
- nenhum exemplo premium/licenciado é copiado sem direito de uso.

## Critérios de aceite

- Motion é a engine padrão da UI React;
- GSAP aparece apenas em componentes de cena documentados;
- Anime.js e React Spring não estão instalados no Core;
- não existe disputa de propriedades entre engines;
- cada animação possui fallback/reduced motion;
- GSAP não entra no bundle de rota que não usa cena;
- Strict Mode não duplica timeline nem listeners;
- a interface permanece totalmente operável sem animação.

## Referências relacionadas

- `04-efeitos-musicais.md`
- `16-animacao-assinatura-tinta-transposicao.md`
- `17-catalogo-animacoes-interface.md`
- `../qa/09-testes-motion-performance.md`
