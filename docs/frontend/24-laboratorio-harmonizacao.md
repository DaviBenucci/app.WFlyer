# Laboratório de harmonização

> Status: canônico para trilha H. Revisão: 2026-07-20.

## Objetivo

Permitir configurar, comparar e aprovar propostas harmônicas sem esconder que conteúdo novo foi criado.

## Composição

```text
HarmonyLabHeader
├── fonte e melodia bloqueada
├── perfil de fidelidade
└── garantia/versão

ScoreWorkspace
├── MelodyLayer
├── HarmonyVariantLayer
└── TensionCurveOverlay opcional

HarmonyInspector
├── linguagem/modo
├── densidade
├── ritmo harmônico
├── tensão
├── voicing/dificuldade
└── restrições

VariantRail
└── 2–4 variantes comparáveis
```

## Princípios

- não existe botão “melhorar magicamente”;
- a melodia bloqueada permanece visível;
- parâmetros usam linguagem musical, com ajuda contextual;
- modos gregos não são apresentados como filtros emocionais;
- andamento e modo informam sugestões, não determinam intenção;
- cada variante apresenta diferenças, violações evitadas e limitações.

## Fluxo

1. confirmar melodia e regiões;
2. escolher perfil de fidelidade;
3. confirmar centros tonais/modais sugeridos;
4. definir densidade, ritmo harmônico e dificuldade;
5. gerar variantes;
6. ouvir e comparar por frase;
7. inspecionar `Musical Diff`;
8. escolher ou ajustar;
9. aprovar variante e criar nova versão.

## Variant card

Cada variante mostra:

```text
nome neutro
resumo de linguagem
cadências preservadas
quantidade de acordes criados/substituídos
faixa de tensão
nível de tocabilidade
warnings
seed/engine ocultos no detalhe técnico, não na tela principal
```

Não usar estrelas ou porcentagem genérica de “qualidade”.

## Tensão

A curva pode ser editada por âncoras como repouso, crescimento, clímax e resolução. Ela não deve inferir rótulos emocionais absolutos.

## Falhas

- nenhuma variante válida: mostrar restrições incompatíveis;
- melodia alterada: rejeitar variante;
- centro tonal ambíguo: solicitar confirmação por região;
- instrumento monofônico: gerar cifras/parte separada, não acordes impossíveis;
- versão da fonte mudou: invalidar comparação e solicitar rebase.

## Critérios de aceite

- variantes são semanticamente diferentes e reproduzíveis;
- notas criadas são identificáveis;
- usuário pode retornar à melodia sem perda;
- nenhum parâmetro é fabricado pelo frontend;
- aprovação cria versão imutável.
