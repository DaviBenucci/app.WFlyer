# Tela inicial

> Revisão: 2026-07-20.

## Rota

```text
/
```

## Objetivo

Levar o usuário à transposição em uma ação e explicar o produto por meio do domínio musical, sem parecer landing page genérica.

## Shell

`PublicShell`.

## Composição desktop

```text
PublicHeader
Hero assimétrico
  Coluna de mensagem/ação
  Demonstração TranspositionRoute
QuickStart ou CTA
Como funciona em três movimentos
Limitações e formatos ativos
Histórico local resumido, quando existir
Footer
```

## Hero

### Conteúdo

- eyebrow opcional: “Transposição instrumental”;
- H1 direto: “Reescreva a partitura para outro instrumento.”;
- texto: preservar o som de concerto, alterar a escrita e revisar o resultado;
- CTA principal: “Transpor uma partitura”;
- CTA secundário: “Entender a transposição”.

### Demonstração visual

Mostrar um exemplo real:

```text
Piano em C
-> segunda maior acima (+2)
Trompete em Bb
```

Pode incluir a animação-assinatura `Ink Transfer`: uma linha de pauta e 4–6 notas ilustrativas transferem tinta para uma segunda pauta, usando exemplo musical fixo e validado. A cena não pode fingir ser preview de arquivo real.

## Animação de entrada

- integrada ao hero, sem splash screen;
- autoplay apenas na primeira visita da sessão;
- duração alvo de 1,4–1,8 segundo;
- CTA, H1 e navegação operáveis desde o início;
- Motion controla entrada de regiões; GSAP controla apenas o SVG interno;
- fallback estático se o chunk falhar;
- reduced motion apresenta origem, rota e destino sem deslocamento longo;
- não repetir ao retornar à Home na mesma sessão.

Consultar `../frontend/16-animacao-assinatura-tinta-transposicao.md`.

## Quick start

Quando o backend estiver disponível, a home pode oferecer uma dropzone compacta que direciona para `/transpor` mantendo o arquivo selecionado de forma segura. Caso isso complique sessão/recuperação, manter somente CTA.

## Conteúdo funcional

1. formatos ativos obtidos das capabilities;
2. três ações: enviar, escolher instrumentos, revisar/baixar;
3. exemplos musicais corretos;
4. aviso de revisão humana;
5. link para instrumentos suportados.

## Evitar

- três cards de benefícios genéricos;
- depoimentos inventados;
- métricas de usuários/arquivos;
- mockup 3D flutuante;
- gradiente aplicado ao H1;
- notas animadas continuamente;
- anunciar PDF quando desabilitado.

## Mobile

- hero em uma coluna;
- demonstração abaixo do CTA;
- CTA principal visível sem scroll excessivo;
- histórico resumido não domina a página;
- bottom navigation aparece após entrar no shell do app, conforme decisão de implementação.

## Estados

- capabilities carregando;
- API indisponível;
- MusicXML disponível;
- PDF beta habilitado, quando aplicável;
- histórico local vazio/com itens.

## Critérios de aceite

- a home demonstra a relação de transposição, não somente fala sobre ela;
- CTA principal é identificado em poucos segundos;
- textos refletem capabilities;
- exemplos incluem oitava corretamente;
- não há promessa fora da matriz;
- composição não replica template SaaS comum;
- animação não bloqueia LCP textual nem interação;
- cena encerra totalmente e não mantém loop/CPU após a entrada.
