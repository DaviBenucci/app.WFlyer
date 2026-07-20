# Pacote para ensemble

> Status: canônico para trilha E. Capacidade futura.

## Objetivo

Gerar um conjunto coerente de score, partes, relatórios e áudio de ensaio para uma formação escolhida.

## Configuração

```ts
type EnsembleRequest = {
  source_version_id: string
  ensemble_template_id?: string
  instruments: EnsembleInstrumentRequest[]
  difficulty_profile: string
  fidelity_profile: string
  conductor_score_pitch: 'written' | 'concert' | 'both'
  outputs: string[]
}
```

## Formação

A interface permite duplicação de instrumentos, músico/part assignment, afinação e nível. “Trompete” sem variante/afinação não é suficiente quando houver ambiguidade.

## Saídas

- score de regência;
- partes individuais;
- mapa de instrumentação;
- relatórios de tocabilidade;
- Musical Diff por parte;
- áudio de referência/partes quando habilitado;
- manifesto e checksums;
- bundle ZIP seguro somente após gate de container.

## Validações

- consistência score/partes;
- transposição escrita por instrumento;
- extensão e polifonia;
- duplicações e papéis;
- measure/rehearsal marks;
- page turns;
- créditos e watermark.

## Gate

Nenhum pacote é publicado quando uma parte falha. O usuário pode excluir/reconfigurar instrumento e gerar nova versão; não recebe bundle parcial sem consentimento explícito e identificação clara.
