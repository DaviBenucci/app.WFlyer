# Confiabilidade musical e política fail-closed

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Fazer com que o backend prefira **não entregar** a entregar uma partitura musicalmente enganosa. Disponibilidade operacional não pode superar integridade musical.

## Escopo honesto da garantia

O W_Flyer pode comprovar uma transposição determinística para entrada simbólica validada dentro da matriz suportada. Não pode prometer leitura perfeita de todo PDF, identificação infalível de melodia em toda textura polifônica ou uma única harmonização “correta”.

A comunicação pública deve usar:

```text
Transformação verificada dentro do perfil suportado.
```

E nunca:

```text
100% correto para qualquer partitura.
```

O objetivo rígido de qualidade é diferente de “resolver tudo automaticamente”: **100% dos resultados rotulados como verificados precisam ter passado por todos os gates aplicáveis**. Uma entrada ambígua deve ser pausada, devolvida para revisão ou rejeitada; jamais promovida para “verificada” apenas para aumentar a taxa de conclusão.

## Classes de processamento

| Classe | Exemplos | Política |
|---|---|---|
| Determinística | normalização controlada, `TRANSPOSE`, validação de range | pode publicar após prova. |
| Inferencial | OMR, tonalidade implícita, `EXTRACT_MELODY` | ambiguidade material pausa o job. |
| Criativa | `HARMONIZE`, `ARRANGE_FOR_INSTRUMENT` | gera variantes; exige escolha/aceite. |

## Gates obrigatórios

```text
G0 integridade dos bytes
G1 parse e limites estruturais
G2 normalização semântica da origem
G3 revisão da origem quando veio de OMR
G4 validação específica da operação
G5 verificação independente do resultado
G6 compatibilidade/tocabilidade do destino
G7 publicação atômica, watermark e manifesto
```

Qualquer gate rígido falho impede artefato público.

## Verificador independente

O transformador e o verificador não devem compartilhar a mesma função que calcula o resultado. O verificador reparsa os artefatos e reconstrói uma representação semântica para conferir:

- mapeamento origem-saída;
- altura escrita e de concerto;
- onset, duração, ties, tuplets e vozes;
- armaduras, claves, compassos e mudanças;
- integridade da melodia bloqueada;
- notas geradas e suas regras;
- extensão e polifonia do destino.

Pode haver uma implementação secundária de referência em testes, mas o gate de produção precisa ser deterministicamente executável e versionado.

## Níveis de garantia

```text
UNVERIFIED_SOURCE
STRUCTURALLY_VALID
SOURCE_USER_CONFIRMED
TRANSFORMATION_VERIFIED
CREATIVE_VARIANT_VALIDATED
CREATIVE_VARIANT_USER_APPROVED
```

- `TRANSFORMATION_VERIFIED` só existe para operação determinística com todos os invariantes aprovados.
- Uma origem OMR não pode ultrapassar `STRUCTURALLY_VALID` sem revisão ou critério quantitativo aprovado.
- Harmonização não recebe `TRANSFORMATION_VERIFIED`; recebe validação de restrições e aceite do usuário.

## Estado de revisão

Quando falta uma decisão humana:

```text
status = awaiting_user_input
review_kind = source_recognition | melody_selection | harmony_variant
```

O worker libera lease e recursos. O job só volta para `queued` após submissão idempotente da revisão.

## Artefatos imutáveis

Cada etapa produz artefato novo e hash próprio. Nunca editar in-place:

```text
input_original
raw_musicxml
normalized_musicxml
confirmed_source_musicxml
melody_selection
reduced_melody_musicxml
harmony_plan
harmonized_musicxml
transposed_musicxml
rendered_pdf
assurance_report
signed_manifest
```

## Reprodutibilidade

- versões fixas de parser, catálogo, motor, renderer e modelo;
- snapshots dos instrumentos e políticas no job;
- seed e parâmetros para qualquer geração estocástica;
- original e normalizado imutáveis;
- resultado reproduzível ou diferença explicitamente explicada após upgrade.

## Falhas e retries

- falha semântica determinística: não retry;
- timeout/storage/fila transitórios: retry limitado e idempotente;
- OMR ou extração ambígua: não retry automático esperando resultado diferente;
- crash após gerar bytes: reconciliar hash/estado antes de repetir;
- assinatura/proveniência falha: não publicar PDF final.

## Operação degradada

Se OMR, harmonização, renderer ou assinatura estiverem indisponíveis, suas capabilities ficam `false`. O Core MusicXML não deve fingir que a capacidade avançada está funcional.

## Critério de release

Nenhuma frase comercial de “confiabilidade total” pode ser publicada sem:

1. matriz de suporte explícita;
2. corpus congelado e independente;
3. resultados reproduzíveis;
4. zero violação de invariantes rígidos;
5. revisão musical documentada;
6. política de bloqueio para entradas fora do perfil.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Gates avançados

```text
G8  cobertura de provenance e Musical Diff
G9  decisão regional de melodia/análise
G10 constraints de harmonização e melodia bloqueada
G11 perfil instrumental e tocabilidade
G12 consistência score/partes e engraving
G13 mapa de playback e sincronização de áudio
G14 aprovação humana quando exigida
```

Apenas os gates aplicáveis à operação são executados, mas nenhum pode ser omitido para elevar a taxa de conclusão.

## Proibição de confiança agregada enganosa

Um número global não pode transformar uma região crítica incerta em resultado verificado. O relatório deve declarar:

```text
cobertura por evento/região
decisões automáticas
decisões humanas
itens desconhecidos
warnings materiais
gates executados e versões
```

## Erros de comissão e omissão

O gate mede:

- **comissão:** evento alterado/criado sem autorização ou regra válida;
- **omissão:** evento que deveria ser transformado não foi mapeado;
- **atribuição:** origem ou autor da decisão está incorreto;
- **apresentação:** notação correta ficou visualmente ambígua/ilegível.

Todas as quatro classes podem impedir publicação.

## Integração com o catálogo de falhas

Cada gate e estágio deve declarar os `PM-*` que detecta. O job manifest registra:

```text
applicable_failure_modes
checks_executed
checks_passed
checks_failed
checks_not_applicable
unknown_exception=false|true
```

`checks_not_applicable` exige motivo. Ausência de um checker esperado bloqueia publicação. A lista canônica está em `../riscos/failure-mode-catalog.yaml`.

Uma falha desconhecida não pode ser convertida em baixa confiança para permitir download. Ela segue `../riscos/02-falhas-desconhecidas-incidentes.md`.
