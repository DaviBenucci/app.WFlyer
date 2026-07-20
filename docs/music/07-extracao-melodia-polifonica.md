# Extração de melodia em material polifônico

> Status: canônico para a trilha de inteligência musical. Capacidade desabilitada no MVP Core.

## Objetivo

Selecionar uma linha melódica coerente a partir de uma parte ou score com várias notas simultâneas, vozes ou pautas, preservando a relação entre cada nota escolhida e o evento original.

## Correção conceitual

A nota mais aguda em cada instante não é necessariamente a melodia. A extração deve considerar continuidade, voz notada, frase, métrica, duração, registro, repetição, acentuação e padrões de acompanhamento. Um algoritmo de “pegar a nota de cima” pode falhar em cruzamento de vozes, contracantos, arpejos e texturas de teclado.

## Pré-condições

1. O documento simbólico foi normalizado.
2. Para entrada OMR, toda ambiguidade estrutural relevante foi corrigida ou confirmada.
3. Eventos possuem IDs estáveis por parte, pauta, medida, voz e onset.
4. Repetições, ties, grace notes e anacruse foram normalizados sem perder proveniência.

## Pipeline

```text
MusicXML normalizado
-> segmentação por frases/regiões
-> detecção de vozes e candidatos
-> extração de atributos por evento
-> grafo temporal de candidatos
-> otimização de caminho melódico
-> detecção de ambiguidade
-> confirmação quando necessária
-> redução monofônica
-> validação e manifesto
```

## Evidências por evento

O motor pode utilizar, de forma versionada:

- voz MusicXML declarada;
- parte/pauta e direção de hastes quando confiáveis;
- presença de letra, slur, articulação e dinâmica;
- posição métrica e duração;
- continuidade de altura e direção do contorno;
- registro relativo e estabilidade da linha;
- repetição temática e padrões sequenciais;
- separação em relação a padrões de acompanhamento;
- densidade e papel harmônico local;
- seleção explícita do usuário.

Nenhuma evidência isolada é verdade universal. Pesos e regras devem ser versionados em `melody_extractor_manifest`.

## Seleção por segmentos

A melodia pode mudar de voz ao longo da música. A unidade de decisão não deve ser obrigatoriamente “uma voz para a peça inteira”. O resultado registra segmentos:

```ts
type MelodySegmentSelection = {
  segment_id: string
  start_measure: number
  end_measure: number
  selected_source_event_ids: string[]
  alternative_paths: Array<{ source_event_ids: string[]; score_band: string }>
  evidence_codes: string[]
  ambiguity: 'none' | 'material' | 'blocking'
  confirmed_by_user: boolean
}
```

## Gate de ambiguidade

- `none`: um caminho é claramente dominante e não viola regras; pode prosseguir.
- `material`: duas ou mais alternativas são plausíveis; mostrar revisão antes da publicação.
- `blocking`: a estrutura ou o reconhecimento não permite inferência segura; exigir correção ou rejeitar.

Scores numéricos brutos podem existir internamente, mas a decisão pública deve ser explicável por região e ação necessária.

## Revisão assistida

A UI deve permitir:

- ouvir/visualizar apenas a linha selecionada;
- alternar entre candidatos por frase;
- clicar em notas de origem para incluir ou excluir;
- bloquear uma voz ou pauta em uma região;
- desfazer e restaurar a sugestão automática;
- confirmar explicitamente a seleção final.

## Invariantes da redução

- cada nota de saída referencia pelo menos um evento de origem;
- nenhuma nota nova é criada em `EXTRACT_MELODY`;
- onset e duração são preservados, salvo política explícita de legato/sustentação;
- ties e anacruse continuam semanticamente válidos;
- notas simultâneas na linha selecionada exigem escolha explícita ou política documentada;
- eventos descartados constam no relatório, não desaparecem sem rastro;
- a transposição, quando solicitada, ocorre depois da seleção da melodia.

## Adaptação ao destino

Depois da extração, `REDUCE_TO_MONOPHONIC` verifica extensão escrita e de concerto, clave e notas impraticáveis. Mudança de oitava só pode ocorrer quando a política `allow_octave_adaptation` estiver ativa e deve ser registrada por frase/evento.

## Gate de ativação

A capability `melody_extraction` só pode ser ativada quando:

1. corpus rotulado por músicos estiver versionado;
2. métricas por nota e por segmento estiverem definidas antes do benchmark;
3. calibração de ambiguidade for avaliada;
4. revisão assistida estiver operacional;
5. nenhuma baixa confiança gerar publicação automática;
6. resultados forem reproduzíveis por versão e seed quando aplicável.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Casos adversariais obrigatórios

O extrator deve ser testado contra:

- melodia em voz interna;
- cruzamento entre pautas;
- troca de voz no meio da frase;
- dobramento em oitava/uníssono;
- arpejo superior de acompanhamento;
- contracanto mais agudo que o tema;
- cue/ossia;
- letras associadas a uma voz;
- anacruse, grace notes e ties;
- duas melodias igualmente plausíveis.

## Solução arquitetural

1. construir candidatos por voz/pauta e caminhos que podem migrar entre elas;
2. segmentar por frase, não por nota isolada;
3. extrair features musicais e evidências codificadas;
4. rankear candidatos sem apagar alternativas;
5. calibrar ambiguidade por região;
6. solicitar decisão humana quando o custo de erro for material;
7. preservar todos os eventos não selecionados no diff.

`highest_pitch` pode ser uma feature, nunca regra final.

## Métricas

Além de precisão por nota, medir fronteira de frase, troca de voz, eventos de acompanhamento incluídos, eventos melódicos omitidos, cobertura automática e falsos positivos publicados como verificados.
