# Matriz detalhada de falhas — pre-mortem

> Status: canônico e vivo. Revisão: 2026-07-20.

## Como usar

Cada cenário recebe teste, observabilidade e comportamento fail-closed. A lista não promete cobrir o universo de falhas; qualquer falha nova deve virar linha e fixture.

## Aquisição e parsing

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-001 | arquivo vazio/truncado | bytes/hash/parser | rejeitar |
| PM-002 | extensão correta, conteúdo incorreto | assinatura/raiz | rejeitar |
| PM-003 | XXE/XInclude/URL externa | parser seguro | rejeitar/log seguro |
| PM-004 | XML profundo/excessivo | limites | rejeitar |
| PM-005 | MXL zip bomb/path traversal | container gate | rejeitar |
| PM-006 | PDF com conteúdo ativo/malformado | sandbox/validator | rejeitar |
| PM-007 | arquivo muda entre upload/processamento | hash | falhar integridade |
| PM-008 | charset/texto inválido | decoder/schema | erro específico |

## Estrutura musical

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-009 | measures com duração inconsistente | normalizador | review/rejeitar |
| PM-010 | voices sem backup/forward coerente | timeline validator | rejeitar |
| PM-011 | ties órfãos | tie graph | rejeitar/warning conforme impacto |
| PM-012 | tuplets inconsistentes | duration invariant | rejeitar |
| PM-013 | grace notes sem política | profile detector | desabilitar operação |
| PM-014 | cross-staff perdido | event graph | review/block |
| PM-015 | instrument change ignorado | detector | rejeitar perfil |
| PM-016 | unpitched tratado como pitch | notation detector | rejeitar |
| PM-017 | microtom arredondado para semitom | pitch validator | rejeitar |
| PM-018 | cue notes confundidas com material principal | cue metadata | review |
| PM-019 | ossia/alternative staff processada como simultânea | structure detector | review/rejeitar |
| PM-020 | repeats expandidos duas vezes | playback/semantic graph | bloquear |

## Transposição

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-021 | semitone-only gera grafia errada | diatonic invariant | bloquear |
| PM-022 | oitava de instrumento ignorada | interval vector | bloquear |
| PM-023 | `<transpose>` de origem aplicado duas vezes | source normalization | bloquear |
| PM-024 | key signature não acompanha região | key map diff | bloquear |
| PM-025 | harmony root/bass não transpostos | harmony diff | bloquear |
| PM-026 | pitch de concerto muda | independent checker | bloquear |
| PM-027 | nota fora do range após escrita | playability preflight | warning/block conforme operação |
| PM-028 | enarmonia ilegível | policy checker | warning/review |

## OMR

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-029 | clave reconhecida errada | structural comparison/review | origem não verificada |
| PM-030 | armadura omitida | key consistency | review |
| PM-031 | acidente perdido | event confidence | review/block |
| PM-032 | duração/beam incorreto | measure invariant | review/block |
| PM-033 | voz fundida/dividida | voice analysis | review |
| PM-034 | página fora de ordem/ausente | page manifest | review |
| PM-035 | texto/instrumento detectado errado | user confirmation | não assumir |
| PM-036 | OMR exporta MusicXML incompleto | schema + semantic gates | não publicar verificado |

## Extração de melodia

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-037 | nota mais aguda escolhida como regra | benchmark adversarial | modelo proibido |
| PM-038 | acompanhamento arpejado entra na melodia | candidate evidence | review |
| PM-039 | melodia em voz interna omitida | labels/corpus | review/block |
| PM-040 | troca de voz no meio da frase | phrase continuity | review |
| PM-041 | octave doubling vira acorde | doubling policy | escolher política |
| PM-042 | ornamentação descartada | ornament mode | diff/review |
| PM-043 | anacruse perdida | timeline invariant | bloquear |
| PM-044 | notas simultâneas sem decisão | monophony validator | review |
| PM-045 | evento criado na extração | provenance invariant | bloquear |

## Análise/harmonização

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-046 | modo global ignora modulação | tonal region map | review |
| PM-047 | nota de suspensão tratada como chord tone | non-chord analysis | variante penalizada/rejeitada |
| PM-048 | cadência estrutural destruída | cadence invariant | rejeitar no perfil |
| PM-049 | ritmo harmônico excessivo para andamento | density policy | warning/rejeitar |
| PM-050 | melodia alterada | locked melody hash | bloquear |
| PM-051 | vozes paralelas proibidas no perfil clássico | voice-leading rules | rejeitar variante |
| PM-052 | regra clássica aplicada a jazz/modal | profile mismatch | bloquear policy |
| PM-053 | acorde sem pitch de melodia compatível | vertical validator | rejeitar |
| PM-054 | modelo inventa símbolo/nota inválida | schema/constraints | rejeitar |
| PM-055 | todas variantes praticamente iguais | semantic distance | regenerar/avisar |
| PM-056 | “sentimento” inferido como fato | UX/content tests | remover/confirmar usuário |

## Tocabilidade/adaptação

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-057 | range absoluto cadastrado errado | catalog review | flag off/corrigir versão |
| PM-058 | acorde impossível apesar de contagem válida | instrument solver | bloquear |
| PM-059 | frase de sopro sem respiração | tempo/phrase model | finding |
| PM-060 | registro sem projeção | register profile | warning |
| PM-061 | dificuldade ignora andamento | tempo-aware rules | recalcular |
| PM-062 | adaptação remove nota estrutural | fidelity/diff | review/block |
| PM-063 | técnica não modelada tratada como segura | unknown-technique rule | expert review |
| PM-064 | nível iniciante usado como física absoluta | profile separation | corrigir severity |

## Score, partes e engraving

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-065 | parte diverge do score | consistency properties | bloquear pacote |
| PM-066 | score em concert e parte written confundidos | mode manifest | bloquear |
| PM-067 | rehearsal marks divergentes | ID check | bloquear |
| PM-068 | page turn em passagem contínua | layout analysis | warning/block |
| PM-069 | colisão cobre acidente/dinâmica | geometry detector | bloquear PDF |
| PM-070 | fonte musical ausente troca glifo | font manifest | bloquear renderer |
| PM-071 | watermark atravessa nota | safe-zone validator | bloquear PDF |
| PM-072 | layout diff interpretado como musical | diff classifier | separar categorias |

## Áudio/ensaio

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-073 | áudio usa pitch escrito | pitch comparison | bloquear áudio |
| PM-074 | repeat/endings fora de ordem | occurrence corpus | bloquear following |
| PM-075 | A/B desalinhado | timestamp tolerance | desabilitar toggle |
| PM-076 | volume diferente influencia avaliação | loudness normalization | normalizar |
| PM-077 | cursor atualiza DOM inteiro | performance test | refatorar camada |
| PM-078 | autoplay sem consentimento | E2E/a11y | impedir |
| PM-079 | sample sem licença | dependency inventory | não distribuir |
| PM-080 | anotação perde âncora após reflow | remap check | marcar órfã |

## Backend e operação

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-081 | double click cria jobs duplicados | idempotency test | mesmo job |
| PM-082 | worker crash após upload de artefato | atomic publish test | reconciliar/não público |
| PM-083 | retry de erro determinístico | taxonomy test | não retry |
| PM-084 | job preso por lease expirado | reconciler | retomar/falhar seguro |
| PM-085 | cache usa versão antiga de modelo | dependency hash | invalidar |
| PM-086 | flag UI on/backend off | capability contract | UI obedece backend |
| PM-087 | progresso inventado | stage contract | sem percentual falso |
| PM-088 | purge remove manifesto antes da política | retention tests | ordem correta |

## Segurança, privacidade e autoria

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-089 | sessão B acessa artefato A | IDOR test | 404 |
| PM-090 | metadado musical injeta prompt | adversarial fixture | tratar como dado |
| PM-091 | log contém letra/partitura | log scanner | bloquear CI/incidente |
| PM-092 | upload usado para treino sem opt-in | data lineage audit | proibido |
| PM-093 | crédito do autor removido | metadata diff | bloquear exportação |
| PM-094 | watermark contém PII | payload policy | rejeitar token |
| PM-095 | link compartilhado sem revogação | security test | não habilitar |
| PM-096 | comentário com script/URL perigosa | sanitização | neutralizar |

## Frontend e referência visual

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-097 | IA substitui workspace por dashboard | golden review | rejeitar PR |
| PM-098 | only-happy-path | state coverage | bloquear DoD |
| PM-099 | warning em toast desaparece | story/E2E | painel persistente |
| PM-100 | baseline atualizado sem revisão | CI policy | bloquear |
| PM-101 | referência externa copiada | provenance review | remover/refazer |
| PM-102 | animação bloqueia CTA | motion test | fallback/imediato |
| PM-103 | reduced motion apenas acelera | accessibility test | variante reduzida |
| PM-104 | GSAP permanece ativo após navegação | leak test | cleanup |

## Unknown failures

Toda falha nova recebe próximo `PM-*`, fixture, owner, causa raiz, controle e teste de regressão. Erro desconhecido com possível impacto musical deve falhar fechado.

## Sessão, API e contratos

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-105 | sessão expira enquanto job válido ainda executa | integração sessão/job | renovar dentro da política ou orientar recuperação; nunca tornar público |
| PM-106 | token CSRF expirado, ausente ou reutilizado | middleware/nonce | `403`, renovar página/token, nenhuma mutação |
| PM-107 | mesma idempotency key usada com payload diferente | hash de request | `409 IDEMPOTENCY_CONFLICT` |
| PM-108 | rate limit ocorre após bytes já escritos em quarentena | teste upload/cleanup | abortar e remover temporário |
| PM-109 | clock skew altera expiração ou URL assinada | teste com relógio controlado | usar horário do servidor e tolerância documentada |
| PM-110 | nome Unicode/confusável ou path-like chega ao storage | normalização/chave gerada | ignorar path do cliente e preservar display name sanitizado |
| PM-111 | upload multipart/chunk duplicado ou fora de ordem | manifest/hash | abortar ou reconstruir somente pelo protocolo suportado |
| PM-112 | capability muda entre configuração e submit | capability snapshot | rejeitar configuração obsoleta e recarregar opções |
| PM-113 | cookie anônimo é perdido e resultado fica órfão | fluxo de recuperação | não contornar autorização; aplicar mecanismo de recuperação aprovado |
| PM-114 | cliente envia revisão antiga após nova confirmação | `expected_revision_id` | `409 REVISION_CONFLICT`, preservar ambas |

## Infraestrutura, concorrência e publicação

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-115 | banco indisponível antes do commit | fault injection | não responder como aceito |
| PM-116 | commit ocorre, mas outbox demora/falha ao publicar | reconciler/outbox age | manter job persistido e publicar posteriormente |
| PM-117 | Redis/broker indisponível | health/fault injection | manter outbox pendente; não perder job |
| PM-118 | mensagem é entregue mais de uma vez | duplicate delivery test | mesma tentativa lógica/sem artefato duplicado |
| PM-119 | worker cai antes/depois de atualizar stage | kill-point tests | lease/reconcile e estado monotônico |
| PM-120 | upload ao storage termina parcialmente | temp key/checksum | não promover chave final |
| PM-121 | storage fica indisponível depois da transformação | fault injection | retry transitório; resultado não concluído |
| PM-122 | checksum do artefato diverge do manifesto | verificação antes de publish/download | bloquear e abrir incidente |
| PM-123 | cancelamento concorre com publicação | compare-and-set terminal | um único estado terminal; cancelado não publica |
| PM-124 | purge concorre com download | lock/version/retention tests | resposta consistente, sem download parcial |
| PM-125 | purge aponta para artefato de sessão errada | ownership + manifest | bloquear, incidente de segurança |
| PM-126 | mensagem vai para dead-letter sem alerta | DLQ monitor | alertar owner e estado público não fica eternamente processando |
| PM-127 | workers com versões diferentes processam o mesmo job | manifest/version policy | fixar versão por job ou rejeitar worker incompatível |
| PM-128 | app e banco executam schemas incompatíveis durante deploy | migration compatibility test | bloquear deploy/worker; nunca adivinhar coluna |
| PM-129 | jobs caros causam starvation dos simples | métricas de fila/quotas | filas e pesos por complexidade |
| PM-130 | partitura válida provoca explosão combinatória | complexity budget | pausar/rejeitar com limite explicável |

## Revisão, colaboração e versionamento

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-131 | dois revisores alteram a mesma região | optimistic concurrency | conflito explícito e merge humano |
| PM-132 | anotação perde âncora após nova revisão | anchor remap | marcar `orphaned`, não mover silenciosamente |
| PM-133 | aprovação é aplicada sobre parent obsoleto | parent/revision check | rejeitar e solicitar nova revisão |
| PM-134 | link revogado continua válido por cache | auth no fetch/cache policy | negar acesso e invalidar cache |
| PM-135 | comentário/metadado renderiza HTML/script | sanitização/CSP | neutralizar e preservar texto seguro |

## Release, modelos, corpus e supply chain

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-136 | feature flag é ligada antes do gate de corpus | policy-as-code | bloquear rollout |
| PM-137 | rollback não consegue ler artefato de schema novo | backward compatibility fixture | manter reader compatível ou impedir rollback inseguro |
| PM-138 | provedor/modelo fica indisponível | circuit breaker | fallback aprovado ou capability indisponível; sem troca silenciosa |
| PM-139 | mesma variante muda sem novo ID por não determinismo | artifact immutability | preservar output concreto e gerar nova revisão |
| PM-140 | licença/dependência muda e invalida distribuição | SBOM/licence gate | bloquear release e substituir/comprovar direito |
| PM-141 | corpus de release vaza para treino/tuning | data-lineage audit | invalidar benchmark e reconstruir split |
| PM-142 | equipe ajusta algoritmo repetidamente contra test set | governance audit | congelar holdout novo e registrar contaminação |
| PM-143 | métrica agregada mascara falha em instrumento/textura | relatório estratificado | não ativar estrato reprovado |
| PM-144 | logs/telemetria capturam conteúdo musical ou PII | scanner/amostragem | remover, rotacionar e abrir incidente |

## Frontend, offline e acessibilidade complementar

| ID | Falha | Detecção | Comportamento |
|---|---|---|---|
| PM-145 | UI mostra sucesso antes do estado terminal verificado | contract/E2E | exibir aceito/processando, nunca concluído otimista |
| PM-146 | rede cai depois que o backend aceitou o job | E2E offline | recuperar pelo job/session; não criar duplicado |
| PM-147 | ação feita offline parece enviada | PWA/E2E | declarar local/não enviado; não enfileirar mutação sem protocolo |
| PM-148 | viewport/zoom esconde CTA, warning ou inspector | visual/a11y matrix | reflow e ação acessível |
| PM-149 | teclado/leitor de tela não consegue selecionar evento musical | interaction/a11y test | oferecer lista textual e controles equivalentes |
| PM-150 | ruído de antialiasing causa atualização indiscriminada de baseline | deterministic visual env | tolerância controlada e revisão humana |
| PM-151 | nomes de notas/instrumentos mudam significado por locale | locale fixtures | armazenar IDs canônicos e localizar apenas apresentação |
| PM-152 | tempo decimal/locale é interpretado incorretamente | parser/locale tests | schema numérico canônico e validação |
| PM-153 | áudio perde sincronização após background/resume | lifecycle test | recalibrar relógio ou desabilitar following |
| PM-154 | service worker entrega capability/API schema antigo | version handshake | invalidar cache e bloquear submit obsoleto |
| PM-155 | reduced motion é respeitado na UI, mas ignorado em canvas/SVG | a11y motion test | substituir por estado estático |
