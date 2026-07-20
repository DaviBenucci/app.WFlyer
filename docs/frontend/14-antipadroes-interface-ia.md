# Antipadrões de interface gerada por IA

> Revisão: 2026-07-20.

## Objetivo

Impedir que a implementação converta a documentação em um template genérico por conveniência.

## Antipadrões visuais

### Card soup

Sintoma: cada seção vira um card arredondado com ícone e texto.

Correção: usar hierarquia editorial, dividers, listas, inspector e surfaces contínuas.

### Purple SaaS

Sintoma: gradiente violeta/azul, blobs luminosos e glow em todos os botões.

Correção: usar a paleta semântica com superfícies de papel, tinta e cor apenas em trajetória/ação.

### Glass em excesso

Sintoma: blur e transparência em cards, menus e formulários.

Correção: superfícies sólidas; blur somente quando existe sobreposição real e contraste estável.

### Hero genérico

Sintoma:

```text
Título grandioso
Subtítulo vago
Botão roxo
Mockup flutuante
Três benefícios idênticos
```

Correção: demonstrar a relação instrumento original → destino e permitir começar a tarefa.

### Dashboard sem necessidade

Sintoma: métricas de arquivos, gráficos e cards no MVP sem conta.

Correção: histórico e ações recentes em lista. Não inventar analytics.

### Animação como identidade

Sintoma: notas voando, partículas e transições longas.

Correção: identidade por composição, tipografia, linguagem e componentes do domínio.

## Antipadrões de conteúdo

- “com tecnologia de ponta” sem explicar o recurso;
- “potencialize sua criatividade”;
- “processamento inteligente” como única descrição;
- chamar toda validação de IA;
- prometer que o resultado está correto sem warnings/invariantes;
- usar emojis em mensagens de erro ou sucesso crítico.

## Antipadrões de implementação

- instalar biblioteca para um único efeito trivial;
- copiar blocos de registry sem adaptar semântica;
- `use client` no layout inteiro;
- uma store global para todo estado;
- duplicar página mobile e desktop;
- hardcode de instrumentos na UI;
- regra de domínio em componente;
- skeleton sem relação com o conteúdo;
- toast como única mensagem de erro;
- esconder funcionalidades desabilitadas atrás de “em breve” em toda tela.

## Checklist de revisão

- a página possui um objetivo operacional claro?
- o layout é específico do conteúdo?
- há mais cards do que unidades reais de informação?
- cor ou animação está compensando hierarquia ruim?
- os textos mencionam formato, instrumento e ação?
- um usuário entende a limitação sem ler documentação técnica?
- a página continua boa sem gradiente, glow e motion?
- o componente veio de biblioteca sem adaptação visível?

Qualquer resposta problemática bloqueia aprovação visual.
