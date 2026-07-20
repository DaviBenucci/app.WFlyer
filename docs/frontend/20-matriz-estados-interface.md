# Matriz de estados da interface

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Evitar que páginas sejam desenhadas somente para o caminho feliz. Cada estado possui fonte de verdade, ação possível e fallback proibido.

## Bootstrap e sessão

| Estado | Fonte | UI | Ação | Proibido |
|---|---|---|---|---|
| `bootstrapping` | sessão/capabilities | shell estável e skeleton curto | aguardar | splash bloqueante |
| `capabilities_loaded` | API | formatos/operações reais | continuar | hardcode |
| `session_expired_recoverable` | 401 | aviso e rebootstrap único | renovar | loop infinito |
| `session_lost` | 401/404 | explicar perda de propriedade | novo fluxo | prometer recuperar job sem prova |
| `offline_readonly` | navigator/cache | mostrar dados locais marcados | reconectar | criar job offline |

## Upload

| Estado | UI principal | Ação |
|---|---|---|
| `empty` | dropzone e perfil suportado | escolher arquivo |
| `selected_local` | nome/tamanho, ainda não validado | enviar/remover |
| `uploading` | progresso de bytes real | cancelar |
| `quarantined` | validação em curso | aguardar |
| `validated` | resumo estrutural | configurar operação |
| `invalid_type` | motivo e formatos | substituir |
| `unsafe_document` | erro persistente | substituir |
| `unsupported_structure` | recursos detectados | ver requisitos/exportar novamente |
| `expired` | item indisponível | reenviar |

## Configuração musical

| Estado | Condição | Comportamento |
|---|---|---|
| `operation_unselected` | upload válido | explicar diferenças entre operações |
| `source_required` | instrumento não confirmado | bloquear envio |
| `target_required` | operação exige destino | bloquear envio |
| `incompatible_texture` | destino não suporta textura | sugerir extração/adaptação |
| `review_will_be_required` | análise prevê ambiguidade | informar antes do job |
| `ready` | contrato completo | mostrar resumo e impacto |
| `capability_disabled` | flag off | explicar indisponibilidade, sem CTA falso |

## Job

| Estado | UI | Regra |
|---|---|---|
| `creating` | ação desabilitada e idempotente | não duplicar request |
| `queued` | posição/etapa quando disponível | não inventar percentual |
| `running` | timeline por stage real | polling conforme Retry-After |
| `awaiting_user_input` | review persistente | pausar progresso automático |
| `cancel_requested` | confirmação de solicitação | não dizer cancelado ainda |
| `completed` | resultado e garantia | listar artefatos |
| `completed_with_warnings` | warning antes de download | não esconder em toast |
| `failed_retryable` | causa pública e retry seguro | preservar idempotência |
| `failed_deterministic` | correção necessária | não oferecer retry cego |
| `cancelled` | estado terminal | novo job opcional |
| `expired` | download bloqueado | explicar retenção |

## Revisão musical

| Estado | Exemplo | UI |
|---|---|---|
| `source_recognition` | OMR incerto | original e MusicXML sobrepostos |
| `melody_selection` | dois caminhos plausíveis | candidatos por frase |
| `harmony_variant` | variantes geradas | comparação e audição |
| `playability_choice` | oitava/revoicing alternativos | impacto e preview |
| `revision_conflict` | base obsoleta | comparar/recarregar |
| `review_submitting` | PUT em curso | bloquear duplicação |
| `review_accepted` | nova revisão criada | mostrar versão |

## Musical Diff

| Estado | Comportamento |
|---|---|
| `mapping_complete` | navegação bidirecional por evento |
| `mapping_partial` | destacar regiões sem mapeamento e bloquear selo total |
| `no_semantic_change` | declarar equivalência sem esconder layout distinto |
| `creative_additions` | notas criadas em categoria separada |
| `removed_events` | eventos removidos com motivo |
| `metadata_only` | diferenciar metadado de conteúdo musical |

## Áudio e ensaio

| Estado | Regra |
|---|---|
| `audio_loading` | controles estáveis e canceláveis |
| `audio_ready` | origem/resultado claramente identificados |
| `audio_context_blocked` | solicitar gesto do usuário |
| `playback_mapping_partial` | desabilitar score following em regiões sem mapa |
| `sample_unavailable` | fallback sonoro identificado |
| `tab_hidden` | pausar animação visual; áudio segue política explícita |
| `rehearsal_offline` | somente artefatos previamente armazenados e licenciados |

## Harmonização e adaptação

| Estado | Regra |
|---|---|
| `profile_incomplete` | explicar parâmetros obrigatórios |
| `generating_variants` | não exibir uma variante parcial como final |
| `no_valid_variant` | permitir ajustar restrições |
| `variant_ready` | mostrar diferenças e scorecards explicáveis |
| `melody_lock_violation` | rejeitar variante |
| `hard_playability_violation` | bloquear exportação dessa adaptação |
| `soft_playability_warning` | permitir escolha informada |

## Testes obrigatórios

Cada estado acima deve existir em fixture ou factory. Estados críticos possuem story e E2E. O frontend não pode inferir estado terminal a partir de `progress_pct`.
