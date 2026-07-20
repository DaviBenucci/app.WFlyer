# Interface de Musical Diff

> Status: canônico para comparação e proveniência. Revisão: 2026-07-20.

## Objetivo

Permitir que o músico verifique rapidamente o que foi preservado, alterado, removido ou criado entre a fonte e o resultado.

## Composição

```text
DiffHeader
├── operação, garantia e versão
├── origem -> destino
└── filtros

ScoreComparison
├── SourceScorePane
├── TargetScorePane
└── LinkedCursor

ChangeInspector
├── EventIdentity
├── BeforeAfter
├── ReasonCodes
├── Provenance
└── Actions
```

## Categorias

```text
PITCH_TRANSPOSED
ENHARMONIC_RESPELLING
OCTAVE_ADAPTED
CLEF_CHANGED
KEY_SIGNATURE_CHANGED
VOICE_SELECTED
EVENT_REMOVED_FROM_REDUCTION
NOTE_CREATED_BY_HARMONY
NOTE_CHANGED_BY_ARRANGEMENT
ARTICULATION_SUGGESTED
BREATH_MARK_SUGGESTED
LAYOUT_ONLY
METADATA_CHANGED
```

Categorias devem ser localizadas, mas os códigos permanecem estáveis.

## Interação

- clicar em evento da origem seleciona evento(s) derivados;
- clicar no resultado retorna à origem/proveniência;
- navegar por compasso, frase, mudança e warning;
- filtrar alterações sem esconder contagem total;
- ouvir região A/B quando mapa de reprodução existir;
- aceitar/rejeitar apenas operações revisáveis; transposição verificada não é editada no diff sem criar nova revisão;
- exportar relatório textual acessível.

## Mapeamento

A UI usa IDs estáveis retornados pelo backend. Nunca relaciona notas apenas por posição visual ou índice do DOM.

```ts
type DiffLinkDTO = {
  change_id: string
  source_event_ids: string[]
  target_event_ids: string[]
  category: string
  reason_codes: string[]
  severity: 'info' | 'notice' | 'warning' | 'blocking'
  measure_ref: string
  phrase_id?: string
}
```

## Alterações criativas

Notas criadas por harmonização ou arranjo devem ser visualmente distinguíveis sem poluir a partitura. O modo padrão usa contorno/highlight temporário; a exportação final não imprime cores de revisão salvo pedido explícito.

## Acessibilidade

- cada mudança possui resumo textual;
- o cursor vinculado não depende apenas de cor;
- teclado navega entre mudanças;
- zoom dos panes pode ser sincronizado ou independente;
- leitores de tela recebem compasso, voz, pitch escrito/soante, duração e motivo;
- reduced motion desativa travel animation entre panes.

## Falhas

- mapeamento parcial bloqueia promessa de diff completo;
- evento sem geometria permanece disponível na lista textual;
- pane renderizado não é fonte de verdade;
- diferenças de paginação não são tratadas como mudança musical.

## Critérios de aceite

- toda alteração musical material possui proveniência;
- o usuário consegue verificar uma transposição por compasso sem ler XML;
- notas criadas não parecem pertencer à fonte;
- warning bloqueante fica visível antes do download;
- o diff funciona sem áudio e sem animação.
