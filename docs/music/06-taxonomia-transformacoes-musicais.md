# Taxonomia de transformações musicais

> Status: canônico. Revisão: 2026-07-20.

## Princípio

O W_Flyer deve separar operações determinísticas, inferenciais e criativas. Usar o verbo “transpor” para todas elas cria contratos falsos, métricas inválidas e resultados difíceis de auditar.

## Operações canônicas

| Operação | Objetivo | Preserva todas as notas? | Natureza | Publicação automática |
|---|---|---:|---|---|
| `TRANSPOSE` | Reescrever a mesma música para outra afinação instrumental. | Sim, dentro do perfil. | Determinística. | Sim, somente após invariantes. |
| `EXTRACT_MELODY` | Identificar uma linha melódica principal em material polifônico. | Não; seleciona eventos de origem. | Inferencial. | Apenas sem ambiguidade material ou após confirmação. |
| `REDUCE_TO_MONOPHONIC` | Adaptar uma linha confirmada para um instrumento monofônico. | Preserva a linha escolhida; descarta vozes não selecionadas de forma explícita. | Determinística após a seleção. | Sim, após validação. |
| `HARMONIZE` | Acrescentar acordes ou vozes a uma melodia confirmada. | A melodia fica bloqueada; novas notas são derivadas. | Criativa e condicionada. | Não sem escolha/aceite do usuário. |
| `ARRANGE_FOR_INSTRUMENT` | Reorquestrar/revoicing para capacidades do instrumento de destino. | Pode alterar distribuição, oitava e textura conforme política. | Mista. | Gate futuro. |

## Regras de linguagem

- **Transposição** não escolhe a melodia e não cria harmonia.
- **Extração de melodia** não é uma transposição; é uma seleção auditável de eventos.
- **Harmonização** não é “correção musical”; é geração de uma proposta estética sujeita a restrições.
- **Arranjo** não pode ser implementado como simples alteração de clave ou oitava.
- O termo **transcrição** deve ser qualificado na UI e na API: `reconhecimento OMR`, `extração de melodia` ou `reescrita para instrumento`.

## Matriz por origem e destino

| Origem | Destino | Operação recomendada |
|---|---|---|
| Monofônica | Monofônico | `TRANSPOSE`; adaptação de oitava/range somente se autorizada. |
| Monofônica | Polifônico | `TRANSPOSE`; `HARMONIZE` opcional para acrescentar textura. |
| Polifônica | Monofônico | `EXTRACT_MELODY` + `REDUCE_TO_MONOPHONIC`; nunca eliminar vozes silenciosamente. |
| Polifônica | Polifônico | `TRANSPOSE` se todas as vozes forem preservadas; `ARRANGE_FOR_INSTRUMENT` se houver revoicing. |

## Contrato de proveniência

Cada evento de saída deve possuir uma origem:

```ts
type EventProvenance = {
  output_event_id: string
  origin: 'source' | 'generated_harmony' | 'generated_arrangement'
  source_event_ids: string[]
  transformation_id: string
  rule_or_model_version: string
}
```

Em `TRANSPOSE`, todo evento afinado deriva de um evento de origem. Em `HARMONIZE`, a melodia deriva da origem e as novas vozes recebem `origin = generated_harmony`.

## Proibição de ambiguidade silenciosa

Quando a operação solicitada exige uma decisão que não pode ser comprovada — por exemplo, escolher entre duas linhas melódicas plausíveis — o job deve entrar em `awaiting_user_input` com motivo específico. Publicar um resultado arbitrário como “correto” é proibido.
