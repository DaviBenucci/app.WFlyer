# Interface de adaptação instrumental e tocabilidade

> Status: canônico para trilha A. Revisão: 2026-07-20.

## Objetivo

Mostrar problemas de execução e permitir escolher adaptações idiomáticas sem alterações silenciosas.

## Componentes

```text
PlayabilitySummary
PlayabilityFindingList
InstrumentRegisterMap
DifficultyProfilePicker
AdaptationOptionCard
BeforeAfterPhrasePreview
BreathAndPageTurnOverlay
```

## Finding

```ts
type PlayabilityFindingView = {
  finding_id: string
  category: string
  severity: 'blocking' | 'warning' | 'suggestion'
  measure_ref: string
  message: string
  evidence: string[]
  options: AdaptationOptionView[]
}
```

## Exemplos

- nota fora da extensão absoluta;
- frase de sopro longa no andamento informado;
- registro possível, mas com projeção fraca;
- acorde impossível pela abertura/posição;
- salto rápido acima do perfil de dificuldade;
- articulação não idiomática;
- virada de página em passagem contínua;
- tessitura excessivamente cansativa.

## Interação

- navegar por finding;
- ouvir/visualizar cada alternativa;
- aplicar por evento, frase ou padrão;
- bloquear regiões que não podem mudar;
- selecionar nível do intérprete;
- desfazer/adotar alternativa;
- comparar impacto no diff e na extensão.

## Linguagem

Evitar “errado” quando algo é apenas difícil ou não idiomático. Usar categorias:

```text
não executável no perfil
executável com risco
difícil para o nível selecionado
pouco idiomático
sugestão editorial
```

## Limites

O sistema não substitui julgamento de instrumentista. Instrumentos, modelos, bocais, afinações, extensões e técnicas variam. O perfil deve declarar versão e público-alvo.

## Gate

Uma adaptação só pode ser exportada quando:

- nenhuma violação rígida permanece;
- cada mudança possui proveniência;
- o usuário aprovou alterações autorais/materialmente audíveis;
- a versão do perfil instrumental foi registrada;
- o resultado passou pelo verificador semântico.
