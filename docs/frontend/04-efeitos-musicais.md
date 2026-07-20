# Movimento e identidade musical

> Status: canônico para motion. Revisão: 2026-07-20.

## Princípio

Movimento deve explicar continuidade, mudança de estado ou trajetória musical. Decoração sem significado é removida.

A arquitetura aprovada está detalhada em:

- `15-arquitetura-motion-e-bibliotecas.md`;
- `16-animacao-assinatura-tinta-transposicao.md`;
- `17-catalogo-animacoes-interface.md`;
- `../qa/09-testes-motion-performance.md`.

## Stack aprovada

```text
CSS nativo
  hover, focus, cor e microestados simples

Motion for React
  presença, layout, gestos, listas e transições React

GSAP
  cena SVG de tinta/transposição e timelines isoladas
```

Anime.js e React Spring não fazem parte do MVP Core. Não instalar múltiplas engines para resolver o mesmo tipo de efeito.

## Tokens de movimento

```text
motion-instant: 80ms
motion-fast: 140ms
motion-standard: 220ms
motion-slow: 320ms
motion-scene: 1200–1800ms
```

Easing orientativo:

```text
entrada: cubic-bezier(0.16, 1, 0.3, 1)
saída: cubic-bezier(0.7, 0, 0.84, 0)
movimento: cubic-bezier(0.22, 1, 0.36, 1)
ênfase: spring somente em interação direta e controlada
```

## Animação-assinatura

A entrada pública pode usar a cena `Ink Transfer`:

```text
pauta de origem
-> tinta se desprende de 4–6 notas
-> trajetória curva representa o intervalo
-> tinta se recompõe na pauta de destino
```

Regras:

- integrada ao hero, nunca splash bloqueante;
- duração inferior a dois segundos;
- exemplo musical fixo e validado;
- autoplay somente uma vez por sessão;
- CTA e conteúdo disponíveis desde o primeiro frame;
- SVG estático como fallback;
- GSAP carregado sob demanda;
- reduced motion usa composição estática/crossfade.

## Usos aprovados

- transição entre estados do workspace;
- expansão do inspector;
- confirmação breve de upload;
- trajetória origem → destino no resumo;
- mudança real de etapa do processamento;
- reordenação/filtragem de listas;
- abertura de sheet/dialog;
- continuidade de rota com progressive enhancement;
- revelação curta do resultado concluído.

## View Transition API

Pode ser usada quando suportada para:

- continuidade do arquivo entre Transpor e Resultado;
- continuidade do `TranspositionRoute`;
- transições de página pública.

Regras:

- fallback sem animação é obrigatório;
- não bloquear navegação aguardando efeito;
- não usar em toda pequena atualização de estado;
- não disputar o mesmo elemento com `layoutId` sem teste;
- respeitar `prefers-reduced-motion`.

## Processamento

A tela de processamento pode usar uma animação curta e repetida de trajetória sobre linhas de pauta estilizadas, desde que:

- exista texto de etapa e progresso real;
- o loop seja discreto;
- não imite porcentagem que o backend não informou;
- pause em aba oculta;
- finalize em estado terminal;
- simplifique em reduced motion;
- não use Canvas/WebGL apenas para decoração.

## Regra de propriedade

Cada nó animado pertence a uma única camada:

```text
CSS | Motion | GSAP
```

Motion não controla propriedades internas da cena GSAP. CSS transition não disputa `transform`/`opacity` com uma engine JavaScript.

## Proibido

- partículas ou notas flutuando pela aplicação;
- parallax em conteúdo funcional;
- cursor personalizado;
- sons automáticos;
- confete em conclusão;
- animações de entrada em todos os elementos;
- loading infinito que não apresenta estado real;
- morphing que dificulta leitura ou foco;
- GSAP para todo hover e dialog;
- Motion e GSAP sobre a mesma propriedade;
- Anime.js/React Spring adicionados “para testar” em produção.

## Reduced motion

Quando ativo:

- durações decorativas passam a zero ou quase zero;
- trajetória vira composição estática;
- deslocamento longo é substituído por crossfade;
- scroll automático é evitado;
- loading mantém texto e indicador simples;
- foco não depende de transição animada.

## Testes

- animação não bloqueia clique, teclado ou leitor de tela;
- foco permanece previsível durante View Transition;
- CTA funciona durante a intro;
- nenhum som ocorre sem consentimento explícito;
- bundle e Core Web Vitals não regridem sem justificativa;
- GSAP não carrega em rotas sem cena;
- Strict Mode não duplica timeline;
- status permanece compreensível sem CSS/animação.
