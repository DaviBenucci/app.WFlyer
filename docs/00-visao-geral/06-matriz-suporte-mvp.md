# Matriz de suporte do MVP

> Status: canônico. Revisão: 2026-07-20.

## Formatos de entrada

| Formato | Core | Condição |
|---|---|---|
| `.musicxml` | Suportado | XML seguro, uma parte e uma pauta. |
| `.xml` | Suportado com inspeção | Aceito apenas se o elemento raiz e a estrutura forem MusicXML. |
| `.mxl` | Desabilitado por padrão | Exige gate de ZIP/MXL e feature flag. |
| `.pdf` | Desabilitado por padrão | Exige gate OMR e feature flag `pdf_omr`. |
| `.png`, `.jpg`, `.jpeg` | Fora do MVP | Não aceitar. |

## Estrutura musical

| Capacidade | Core | Comportamento |
|---|---|---|
| Uma parte e uma pauta | Sim | Perfil principal. |
| Múltiplas vozes na mesma pauta | Sim | Ritmo e voz devem ser preservados. |
| Acordes de notas simultâneas | Sim | Todas as alturas são transpostas. |
| Cifras/harmony simples | Sim, quando parseadas | Transpor raiz e baixo. |
| Mudança de tonalidade | Sim | Transpor cada região. |
| Mudança de clave | Preservar | A clave não é automaticamente redesenhada para o destino no Core. |
| Ties e tuplets | Sim | Estrutura temporal preservada. |
| Letras, dinâmica e articulações | Preservar | Não são transpostas. |
| Duas pautas na mesma parte | Não | Rejeitar com `UNSUPPORTED_SCORE_STRUCTURE`. |
| Múltiplas partes | Não | Rejeitar com `UNSUPPORTED_SCORE_STRUCTURE`. |
| Percussão não afinada | Não | Rejeitar. |
| Tablatura | Não | Rejeitar. |
| Microtons | Não | Rejeitar. |
| Instrument change | Não | Rejeitar. |

## Saída e fidelidade

| Item | Compromisso |
|---|---|
| Altura de concerto | Deve ser invariável após a transposição. |
| Grafia das notas | Deve seguir o intervalo diatônico e a política enarmônica. |
| Ritmo e compassos | Devem ser preservados semanticamente. |
| Layout/paginação | Melhor esforço; não precisa ser idêntico ao original. |
| MusicXML `<transpose>` | Deve representar o instrumento de destino. |
| PDF de saída | Somente com adapter habilitado. |

## Regra de expansão

Qualquer nova capacidade exige:

1. alteração desta matriz;
2. ADR ou decisão registrada;
3. fixtures positivas e negativas;
4. critérios de segurança;
5. atualização de API/UX quando aplicável.

## Matriz de operações

| Operação | MVP Core | Trilha | Condição |
|---|---|---|---|
| Transpor todas as notas | Sim | Core | Uma parte/pauta no perfil. |
| Extrair melodia polifônica | Não | L | Corpus, ambiguidade e revisão aprovados. |
| Reduzir para monofônico | Não | L | Melodia confirmada e perfil do destino. |
| Harmonizar | Não | H | Melodia bloqueada, perfis e gate humano. |
| Arranjar/revoicing | Não | H/M | Regras técnicas por instrumento. |
| Watermark em PDF | Não no Core | W/R | Renderer e assinatura aprovados. |

## Regra de promessa

A palavra “verificado” só pode aparecer para operação e nível de garantia retornados pelo backend. `completed_with_warnings` não autoriza ocultar uma ambiguidade que muda notas.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Capabilities estruturais preparadas, mas não habilitadas

| Capability | Core | Preparação permitida | Publicação |
|---|---|---|---|
| `event_provenance` | básica | IDs e manifesto | interna/relatório básico |
| `musical_diff_ui` | não obrigatória | contrato e fixtures | somente após D |
| `melody_extraction` | não | schemas, flags e corpus | somente após L |
| `playability_analysis` | não | perfil versionado | somente após I |
| `harmonization` | não | operação/versões | somente após H |
| `audio_ab` | não | playback map schema | somente após A |
| `rehearsal_mode` | não | UX reference | somente após A/Q |
| `ensemble_package` | não | source graph schema | somente após E |
| `collaborative_review` | não | revisão/ETag | somente após C |

## Dimensões adicionais da matriz avançada

Toda expansão deve declarar, no mínimo:

```text
formatos e versão
estrutura musical aceita
operações permitidas
instrumentos/perfis
notação especial
grau de automação
nível de garantia
revisão humana obrigatória
artefatos gerados
limites operacionais
política de erro
```

Não existe `supported=true` sem essas dimensões.

## Capacidades documentadas, porém desabilitadas

| Capacidade | Core | Documentada | Condição de ativação |
|---|---:|---:|---|
| Musical Diff determinístico | não obrigatório | sim | proveniência completa e gate D |
| audição A/B | não | sim | playback manifest e gate de sincronização |
| extração de melodia polifônica | não | sim | corpus, revisão e gate L |
| análise de forma/harmonia | não | sim | avaliação por região e gate H0 |
| harmonização | não | sim | variantes, constraints e avaliação cega |
| tocabilidade/adaptação | não | sim | perfis por instrumento e gate A |
| score/partes/ensemble | não | sim | grafo multiparte e gate E |
| modo de ensaio | não | sim | áudio, mapa e assets validados |
| colaboração | não | sim | identidade/autorização e controle de revisão |

`documentada = sim` nunca deve ser interpretado como `capability.enabled = true`.
