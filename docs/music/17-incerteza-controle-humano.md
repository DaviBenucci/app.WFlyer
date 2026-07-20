# Incerteza musical por evento e região

> Status: canônico. Revisão: 2026-07-20.

## Princípio

Um único número de confiança para a obra inteira pode esconder um compasso crítico. O W_Flyer representa incerteza na menor região útil.

## Modelo

```ts
type MusicalUncertainty = {
  uncertainty_id: string
  operation: string
  region: MusicalRange
  affected_event_ids: string[]
  category: string
  alternatives: AlternativeHypothesis[]
  evidence_codes: string[]
  decision: 'auto_safe' | 'review' | 'reject'
  policy_version: string
}
```

Scores internos podem existir para calibração, mas a API pública prioriza categoria, motivo e ação.

## Fontes

- OMR;
- estrutura/voz/pauta;
- instrumento de origem;
- extração de melodia;
- centro tonal/modal;
- análise de acordes;
- adaptação/tocabilidade;
- geometria/renderização;
- score following.

## Agregação

O nível do job é o pior estado material não resolvido, não a média. Uma única nota ambígua que altera melodia pode bloquear publicação mesmo com 99% do documento estável.

## Revisão

A review deve mostrar região, alternativas e impacto. Confirmar uma hipótese cria snapshot; mudanças na fonte invalidam a confirmação.

## Calibração

- conjunto de calibração separado do teste de release;
- reliability diagrams/curvas por categoria quando houver score;
- limiares definidos antes do benchmark;
- monitoramento de drift por versão;
- nenhuma baixa confiança é convertida em warning não bloqueante por pressão de cobertura.
