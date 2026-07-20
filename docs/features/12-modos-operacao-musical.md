# Modos de operação musical

> Status: canônico para UX e contratos futuros. Revisão: 2026-07-20.

## Objetivo

Fazer o usuário escolher conscientemente o tipo de transformação, sem misturar transposição, redução e harmonização.

## Opções

### Transpor todas as notas

Mantém vozes, acordes e ritmo. Disponível quando a estrutura de origem e a capacidade do destino são compatíveis.

### Extrair a melodia principal

Indicado para teclado, arranjos e partes polifônicas que serão convertidas para instrumento monofônico. Pode abrir uma etapa de revisão por frases.

### Harmonizar a melodia

Acrescenta uma proposta harmônica. Requer melodia confirmada e perfil de estilo. Para destino monofônico, gera cifras ou parte de acompanhamento separada.

### Adaptar para o instrumento

Futuro: revoicing, oitavas, divisão de mãos/cordas e simplificação técnica. Não deve aparecer antes do gate próprio.

## Regras de disponibilidade

A API retorna:

```ts
type OperationCapability = {
  operation: 'TRANSPOSE' | 'EXTRACT_MELODY' | 'HARMONIZE' | 'ARRANGE_FOR_INSTRUMENT'
  enabled: boolean
  reason_code?: string
  requires_review: boolean
}
```

A UI não infere apenas pelo nome do instrumento. Ela usa análise do upload, capabilities do ambiente e perfil instrumental.

## Fluxos

```text
TRANSPOSE
upload -> origem/destino -> resumo -> job -> resultado verificado

EXTRACT_MELODY
upload -> análise -> candidatos -> confirmação -> destino -> redução/transposição -> resultado

HARMONIZE
upload -> confirmar melodia -> perfil -> gerar variantes -> comparar -> escolher -> exportar
```

## Microcopy obrigatória

- “Transpor” — reescreve a mesma música para outra afinação.
- “Extrair melodia” — seleciona uma linha principal em uma partitura com várias notas.
- “Harmonizar” — cria novas notas de acompanhamento e entrega propostas para sua escolha.

Evitar “A IA corrigirá automaticamente” e “resultado perfeito”.

## Critérios de aceite

- operação fica visível no resumo e no resultado;
- opções incompatíveis explicam o motivo;
- nenhuma voz é descartada sem confirmação;
- harmonização mostra que contém conteúdo novo;
- o usuário consegue retornar à fonte sem perder versões;
- review pendente sobrevive a refresh na mesma sessão.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Decisão guiada por capacidade do material e do destino

A interface pode recomendar uma operação, mas não selecioná-la silenciosamente quando muda o significado musical.

| Origem | Destino | Ação segura |
|---|---|---|
| monofônica | monofônico | transpor; adaptação opcional |
| monofônica | polifônico | transpor; harmonizar é operação separada |
| polifônica | monofônico | extrair/reduzir com revisão |
| polifônica | polifônico | transpor textura; adaptar/arranjar separadamente |
| estrutura desconhecida | qualquer | bloquear e pedir correção/revisão |

## Resumo vinculante

Antes de executar, apresentar uma frase equivalente a:

```text
Preservar todas as notas e reescrever para Trompete em Bb.
```

ou:

```text
Selecionar uma linha melódica da revisão confirmada e adaptar para Flauta.
```

ou:

```text
Criar até três variantes harmônicas sem alterar a melodia bloqueada.
```

O resumo entra nos parâmetros do job e no manifesto.
