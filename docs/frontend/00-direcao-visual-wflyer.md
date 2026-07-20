# Direção visual e experiência do W_Flyer

> Status: canônico para identidade visual e UX. Revisão: 2026-07-20.

## Objetivo

O W_Flyer deve parecer uma ferramenta musical criada por pessoas que entendem partitura, não um painel SaaS genérico nem uma coleção de componentes prontos. A experiência deve transmitir:

- precisão musical;
- leveza operacional;
- confiança no processamento;
- personalidade editorial;
- foco na partitura e na decisão do usuário.

## Conceito de produto

A direção visual combina três ideias:

```text
Estúdio de transposição
+ papel de partitura
+ trajetória entre instrumentos
```

A aplicação não imita um editor musical completo. Ela organiza o fluxo como um **workspace de transposição**: o arquivo ocupa a superfície principal e as decisões de origem, destino, formato e revisão ficam em um inspector contextual.

## Assinatura visual

### 1. Papel e tinta

- superfícies principais claras e levemente quentes, próximas de papel editorial;
- texto em tom de tinta escura, não preto puro;
- bordas finas e estruturais, inspiradas em pautas e barras de compasso;
- sombras discretas, usadas somente para elevação funcional.

### 2. Trajetória musical

A relação origem → destino pode ser representada por uma linha de trajetória curta e própria do produto. Ela pode aparecer em:

- hero da página inicial;
- resumo de transposição;
- processamento;
- histórico;
- resultado.

Essa linha não deve virar decoração repetitiva. Ela representa mudança de escrita preservando o som de concerto.

### 3. Ritmo editorial

- composição assimétrica em páginas institucionais;
- densidade média no workspace;
- títulos curtos e específicos;
- blocos separados por alinhamento, espaço e linhas, não por cards em excesso;
- números, intervalos e estados com hierarquia tipográfica própria.

## Princípios de UX

### Tarefa antes de decoração

A ação principal deve ser evidente sem depender de slogan, animação ou tutorial. O usuário precisa entender rapidamente:

1. qual arquivo pode enviar;
2. qual instrumento está na origem;
3. qual instrumento receberá a escrita;
4. qual intervalo será aplicado;
5. quando e por quanto tempo o resultado ficará disponível.

### Domínio musical visível

Usar linguagem e componentes próprios do W_Flyer:

- `InstrumentPicker` por família e afinação;
- `TranspositionRoute` com origem, destino e intervalo;
- `ScoreSurface` para arquivo/preview;
- `ProcessingTimeline` com etapas reais;
- `WarningPanel` com localização musical quando disponível;
- `ArtifactRow` para os arquivos resultantes.

### Sofisticação contida

A interface pode ser moderna sem excesso de brilho. O produto deve preferir:

- tipografia forte;
- grids bem resolvidos;
- transições curtas;
- contraste de superfícies;
- componentes específicos do domínio;
- detalhes consistentes.

Evitar usar efeitos como substituto de clareza.

## Três modos de layout

### PublicShell

Usado em:

```text
/
/como-funciona
/instrumentos
```

Características:

- header compacto;
- conteúdo editorial;
- largura controlada;
- sem sidebar permanente;
- CTA para iniciar transposição.

### StudioShell

Usado em:

```text
/transpor
/resultado/{job_id}
```

Características:

- navegação compacta;
- área principal ampla;
- inspector contextual no desktop;
- action bar fixa quando necessário;
- estado do job sempre visível;
- partitura/arquivo como centro visual.

### UtilityShell

Usado em:

```text
/historico
/configuracoes
```

Características:

- listas e preferências com densidade média;
- sem dashboard de métricas;
- filtros simples;
- prioridade para leitura e ação.

## Elementos que fazem a interface parecer gerada por IA

São proibidos como padrão do produto:

- hero com título em gradiente e três cards genéricos abaixo;
- excesso de roxo/azul luminoso sem função;
- glassmorphism em todas as superfícies;
- cards com raio muito grande para qualquer conteúdo;
- ícone `Sparkles` ou estrelas para representar qualquer recurso;
- textos como “revolucione sua experiência musical”;
- números, depoimentos ou métricas inventadas;
- dashboards vazios para “preencher” a tela;
- animações contínuas de notas flutuantes;
- uso do tema padrão do shadcn/ui sem revisão de tokens e composição;
- repetir o mesmo layout de card em todas as páginas;
- esconder complexidade real atrás de frases vagas sobre IA.

## Regra de autenticidade

Antes de aprovar uma página, responder:

```text
Esta composição poderia pertencer a qualquer app de upload de arquivo?
```

Se a resposta for sim, a página ainda não expressa o domínio do W_Flyer.

## Critérios de aceite

- a página Transpor parece um workspace musical, não um formulário administrativo;
- origem, destino e intervalo possuem representação visual própria;
- a partitura/arquivo ocupa a hierarquia principal;
- nenhum componente existe somente para preencher espaço;
- o sistema visual é consistente sem parecer o tema padrão de uma biblioteca;
- movimento e cor continuam opcionais para compreensão;
- a interface continua clara com conteúdo real, nomes longos e warnings múltiplos.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Referência visual vinculante

A identidade só é considerada especificada quando a página possui `reference_id`, estados e composição em `../design-reference/reference-manifest.yaml`. O pacote atual inclui protótipos originais para home, workspace, revisão de melodia, comparação, harmonização e ensaio.

## Interface de confiança musical

A hierarquia visual deve responder, nesta ordem:

1. qual operação será executada;
2. sobre qual revisão e instrumento;
3. o que o sistema sabe e não sabe;
4. o que mudou ou será criado;
5. qual decisão é necessária do músico;
6. qual nível de garantia pode ser atribuído;
7. quais artefatos podem ser usados.

Decoração nunca pode competir com pauta, warning, decisão ou ação principal.

## Diferenciação funcional

O W_Flyer deve parecer um estúdio de preparação musical por meio de componentes de domínio — partitura, rota instrumental, diff, regiões, variantes, tocabilidade, transporte e revisão — e não por ícones de nota espalhados ou metáforas de “IA mágica”.
