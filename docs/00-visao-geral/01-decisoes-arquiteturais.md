# Decisões arquiteturais principais

> Status: canônico. Revisão: 2026-07-20.

## ADR-001 — Projeto orientado por documentação canônica

A implementação deve seguir a hierarquia definida em `08-hierarquia-documental.md`. Código antigo e protótipos são referências, não fontes normativas.

## ADR-002 — MVP sem conta, mas com sessão anônima autorizada

O usuário não precisa criar login. Isso não torna jobs e arquivos públicos. A API deve criar uma sessão anônima opaca, persistida em cookie `HttpOnly`, e validar a propriedade de uploads, jobs e artefatos em todas as operações.

Consequência: UUID é identificador, não autorização. O modelo completo está em `../backend/17-sessao-anonima-autorizacao.md`.

## ADR-003 — Núcleo MusicXML antes de PDF

O primeiro marco executável aceita MusicXML não comprimido, normaliza a entrada, transpõe e devolve MusicXML. PDF de entrada só pode ser habilitado após o adaptador OMR cumprir o gate de qualidade e segurança.

```text
MVP Core: MusicXML -> normalização -> transposição -> validação -> MusicXML
Extensão PDF: PDF -> rasterização -> OMR -> MusicXML bruto -> normalização -> fluxo do Core
```

Consequência: a API não deve aceitar PDF em um ambiente no qual a capacidade `pdf_omr` esteja desabilitada.

## ADR-004 — MusicXML normalizado como representação canônica

O original é imutável. O sistema mantém artefatos distintos para entrada, MusicXML bruto, MusicXML normalizado, MusicXML transposto e renderizações.

## ADR-005 — Modelo de transposição intervalar completo

A transposição não pode ser representada apenas por um inteiro de semitons. Cada instrumento deve declarar:

```text
written_to_concert_diatonic
written_to_concert_chromatic
written_to_concert_octave
```

O intervalo de saída é a diferença vetorial entre origem e destino. Isso preserva grafia diatônica, enarmonia e instrumentos que transpõem oitava.

## ADR-006 — Uma parte e uma pauta por job no MVP Core

O MVP Core processa uma única parte instrumental e uma única pauta por job. Scores multiparte, piano de duas pautas, tablatura, percussão não afinada e mudanças de instrumento dentro da parte ficam fora do gate inicial.

Consequência: arquivos fora desse perfil devem ser rejeitados com erro específico, não processados parcialmente em silêncio.

## ADR-007 — Processamento assíncrono e banco como fonte de verdade

A API apenas recebe, valida, persiste e agenda. Workers executam parsing, OMR, transposição, validação e renderização. O PostgreSQL é a fonte de verdade para estado; o backend de resultados da fila não substitui o banco.

## ADR-008 — Celery e Redis como fila inicial

A fila inicial usa Celery com Redis, versões fixadas em lockfile. O payload contém somente `job_id` e `correlation_id`; o worker cria a tentativa após adquirir o job. Tarefas devem ser idempotentes e serializadas em JSON.

## ADR-009 — Backend Python é a fonte da regra musical

A regra musical canônica reside no backend Python. O frontend recebe o intervalo calculado pela API apenas para exibição. Não existe compartilhamento de código executável de música entre TypeScript e Python.

Consequência: tipos frontend devem ser gerados ou validados a partir do OpenAPI; `packages/shared` não contém o motor musical.

## ADR-010 — Storage privado e retenção separada do estado de processamento

Arquivos ficam em storage privado. O estado de processamento e o estado de retenção são campos diferentes. Um job pode estar `completed` e ter retenção `expired` ou `purged`.

## ADR-011 — Confiança interna, aviso público categórico

Scores numéricos de OMR permanecem internos. O usuário deve receber avisos categóricos acionáveis, como `OMR_REVIEW_RECOMMENDED`, `ENHARMONIC_SIMPLIFICATION` ou `TARGET_CLEF_REVIEW_RECOMMENDED`. Ocultar toda incerteza é proibido.

## ADR-012 — Ferramentas externas atrás de adapters e sandbox

OMR e renderização são adapters substituíveis. Cada subprocesso roda sem shell, sem rede, com usuário não privilegiado, limites de CPU/memória/tempo e diretório temporário isolado.

## ADR-013 — Fidelidade semântica antes de fidelidade visual

O MVP garante correção de alturas, ritmos, armaduras, vozes e metadados de transposição dentro da matriz suportada. Preservar exatamente a paginação e o layout original é melhor esforço, não critério do Core.

## ADR-014 — Escopo futuro não bloqueia o Core

Login, cobrança, biblioteca em nuvem, compartilhamento público, editor visual completo, aplicativo nativo, push e Spotify permanecem fora do MVP Core.


## ADR-015 — Frontend como workspace musical, não dashboard

Páginas públicas usam header editorial; Transpor e Resultado usam StudioShell com canvas e inspector; Histórico e Configurações usam UtilityShell. Sidebar larga, cards de métricas e dashboard genérico não são padrão do Core.

## ADR-016 — Design system próprio sobre primitives headless

Bibliotecas como shadcn/ui e Base UI podem fornecer comportamento acessível, mas tokens, composição, componentes de produto e microcopy são próprios do W_Flyer. O tema padrão de uma biblioteca não é entrega final.

## ADR-017 — Identidade por domínio, não por efeitos

A assinatura visual combina papel/tinta, trajetória de transposição e ritmo editorial. Motion é progressivo e funcional; partículas, glow excessivo, glassmorphism indiscriminado e card soup são antipadrões.

## ADR-018 — Storybook e regressão visual como gates

Componentes do produto precisam de stories, testes de interação, acessibilidade automatizada e regressão visual revisada antes do aceite do frontend.

## ADR-019 — Motion declarativo e cena GSAP isolada

CSS nativo resolve microestados simples. Motion for React é a engine padrão para presença, layout, gestos e transições ligadas ao estado React. GSAP com `@gsap/react` é carregado sob demanda e restrito à animação-assinatura SVG e timelines explicitamente aprovadas.

Anime.js e React Spring não entram no MVP Core. Cada nó visual possui uma única engine proprietária.

## ADR-020 — A animação de tinta não é o motor musical

A cena `Ink Transfer` usa SVG determinístico e exemplo musical validado para explicar transposição. Durante jobs, o movimento é apenas metáfora acompanhada do estágio real. Notas do arquivo do usuário só poderão ser animadas quando o renderer fornecer mapeamento estável entre eventos musicais e geometria.

## ADR-021 — Operações musicais não são sinônimas

`TRANSPOSE`, `EXTRACT_MELODY`, `REDUCE_TO_MONOPHONIC`, `HARMONIZE` e `ARRANGE_FOR_INSTRUMENT` possuem contratos, artefatos, métricas e gates diferentes. É proibido implementar extração ou harmonização dentro do endpoint de transposição sem operação explícita.

## ADR-022 — Confiabilidade musical é fail-closed

O backend não publica artefato quando um invariante rígido, uma ambiguidade material ou a compatibilidade do destino não estiver resolvida. Disponibilidade e “melhor esforço” não autorizam resultado musical enganoso.

## ADR-023 — Transformador e verificador são independentes

A transformação produz o artefato; outro módulo reparsa origem e saída e valida invariantes sem reutilizar a função transformadora. O resultado recebe nível de garantia e manifesto versionado.

## ADR-024 — Extração de melodia é inferencial e revisável

A linha mais aguda não é regra universal. A seleção pode mudar por segmento, conserva proveniência e entra em `awaiting_user_input` quando houver alternativas plausíveis.

## ADR-025 — Harmonização preserva melodia e entrega variantes

A melodia confirmada é bloqueada. O motor gera propostas condicionadas por perfil, submete-as a restrições rígidas e só publica a variante escolhida pelo usuário. Modelos generativos, se usados, geram candidatos e não substituem validadores.

## ADR-026 — Capacidade instrumental além da afinação

Instrumentos declaram polifonia, extensão, faixa confortável, claves e restrições técnicas versionadas. Converter polifonia para instrumento monofônico exige redução explícita.

## ADR-027 — Watermark é dissuasão, rastreabilidade e integridade

A saída PDF usa marca visível distribuída, token pseudônimo, manifesto/hash e assinatura quando habilitada. Nenhuma marca é declarada impossível de remover; a notação musical jamais é alterada para esconder identificação.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## ADR-028 — MusicXML canônico e grafo semântico interno têm papéis diferentes

O MusicXML normalizado permanece o artefato interoperável canônico. Durante processamento, ele é convertido para um grafo semântico interno com IDs estáveis de parte, pauta, voz, medida, evento e ocorrência de playback. Esse grafo não é exposto como substituto público do MusicXML e não pode perder informação necessária ao round trip suportado.

## ADR-029 — Musical Diff é prova de transformação, não decoração

Toda operação que altera, seleciona, remove ou cria eventos deve produzir mapeamento de proveniência. O Core pode começar com manifesto e diff semântico consumível por máquina; a UI de comparação é uma trilha própria. Um resultado determinístico não recebe `TRANSFORMATION_VERIFIED` sem cobertura de eventos conforme sua operação.

## ADR-030 — Perfis instrumentais são capability profiles versionados

O catálogo não se limita a “melódico/harmônico”. Cada perfil aprovado declara transposição, ranges, polifonia nominal e prática, registro, sustain, respiração, span, técnicas, convenções de escrita e severidade das regras. Inferências não suportadas pelo perfil são `UNKNOWN`, nunca “seguras por padrão”.

## ADR-031 — Inferência é regional, explicável e controlada pelo músico

Melodia, forma, centro tonal/modal, cadência e intenção expressiva podem variar ao longo da obra. O backend registra decisões por região, alternativas e evidências. Ambiguidade material muda o job para revisão; um score global de confiança não substitui decisões locais.

## ADR-032 — Motores de IA e solvers são propositores não confiáveis

Modelos e solvers podem sugerir candidatos. Eles não validam a própria saída, não recebem metadados como instruções, não publicam MusicXML diretamente e não podem ultrapassar restrições determinísticas. Versão, configuração, seed quando aplicável, licença e finalidade de dados entram no manifesto.

## ADR-033 — Áudio é derivado do mesmo grafo de eventos

Playback, comparação A/B e score following usam alturas de concerto e um mapa explícito de ocorrências, repetições, saltos e endings. Áudio não é oráculo da notação e não pode ser usado para esconder divergência semântica.

## ADR-034 — Score e partes são projeções de uma fonte musical única

Pacotes para ensemble são gerados a partir do mesmo grafo versionado. Score e partes não são arquivos editados separadamente. IDs, marcas de ensaio, compassos, transposição, cortes e conteúdo musical passam por verificador de consistência antes da publicação.

## ADR-035 — Engraving e legibilidade têm gate próprio

MusicXML semanticamente correto pode produzir PDF ilegível. Renderer, fontes musicais, colisões, viradas de página, tamanhos, safe zones e watermark pertencem ao gate de engraving. PDF com colisão que altere leitura não é publicado.

## ADR-036 — Revisões musicais são imutáveis e derivadas

Original, normalizado, revisado, transformado, harmonizado e adaptado são revisões distintas. Aprovar uma variante cria nova revisão; não sobrescreve a anterior. Cada revisão aponta para pais, decisões humanas, parâmetros, engines e hashes.

## ADR-037 — Colaboração usa concorrência explícita

Comentários e decisões usam versão/ETag. Alterações concorrentes não são resolvidas por “last write wins” quando afetam música. Âncoras apontam para IDs semânticos e recebem estado de órfã quando o evento deixa de existir.

## ADR-038 — Referências visuais internas são parte do contrato de frontend

A IA deve ler `../design-reference/reference-manifest.yaml` e seguir a precedência declarada. Protótipo, story, spec e screenshot interno formam o golden example. Diferença visual automatizada detecta regressão, mas aprovação humana continua obrigatória.

## ADR-039 — Direitos, créditos e finalidade de dados são invariantes

Créditos e avisos do documento são preservados conforme política; W_Flyer não reivindica titularidade. Arquivos não são usados para treino, avaliação pública ou compartilhamento sem base e consentimento separados.

## ADR-040 — Pre-mortem e falhas desconhecidas fazem parte do ciclo de release

A matriz `../qa/19-matriz-falhas-pre-mortem.md` é entrada do design e do QA. Incidente novo cria ID, fixture, causa raiz, controle, teste e atualização documental antes do rollout. Falha desconhecida com possível impacto musical, de segurança ou autoria falha fechado.

## ADR-041 — Referências internas precedem inspiração externa

A IA implementa o frontend a partir de `design-reference/reference-manifest.yaml`, specifications, protótipos e stories internas. Produtos externos servem apenas para estudo de padrões. Branding, código, assets e layout integral de terceiros não podem ser copiados.

## ADR-042 — Musical Diff é artefato do backend

O backend produz relações entre eventos, invariantes, mudanças e proveniência. O frontend apresenta e navega o diff; não recalcula teoria musical nem infere correspondências por posição de SVG.

## ADR-043 — Áudio é projeção derivada, não prova de correção

Reprodução e score following usam um `PlaybackManifest` derivado do grafo canônico. MIDI e áudio podem auxiliar revisão, mas não substituem validação semântica de MusicXML.

## ADR-044 — Transposição e adaptação idiomática são operações distintas

`TRANSPOSE` preserva o conteúdo musical dentro do contrato. `ARRANGE_FOR_INSTRUMENT` pode deslocar oitava, simplificar, revoicer ou redistribuir apenas dentro de orçamento explícito, com diff e aprovação.

## ADR-045 — Análise e criatividade preservam autoridade humana

Extração de melodia, forma, cadência, curva de tensão e análise harmônica são resultados versionados e revisáveis. Harmonização e arranjo geram variantes; não recebem o mesmo selo de uma transformação determinística.

## ADR-046 — Score e partes derivam do mesmo grafo semântico

Partes não são extraídas de PDFs. Score e partes são projeções do mesmo documento canônico, compartilham IDs e são publicados como pacote atômico somente após verificação cruzada.

## ADR-047 — Perfil instrumental modela capacidade prática

A classificação melódico/harmônico é insuficiente. Perfis versionados incluem pitch escrito/concerto, extensão, tessitura, registros, polifonia prática, sustain, respiração, span, técnicas e dificuldade dependente de andamento.

## ADR-048 — Catálogo de falhas e política desconhecida são bloqueantes

Falhas conhecidas são mantidas em `riscos/failure-mode-catalog.yaml`. Uma exceção desconhecida com possível impacto musical, de autorização ou integridade falha fechada, gera incidente, novo `PM-*`, fixture e regressão.

## ADR-049 — Preflight obrigatório antes de código

Nenhuma capacidade inicia sem preflight que declare contratos, invariantes, modos de falha, rollback, feature flag, testes, corpus, métricas e riscos residuais. A IA não pode preencher uma decisão musical pendente por conveniência.

## ADR-050 — Capacidades avançadas usam rollout estratificado

Melodia, adaptação, harmonia, ensemble e OMR são ativados por versão de modelo, formato, instrumento, complexidade e perfil. Um resultado agregado não autoriza ativação para grupos com desempenho insuficiente.
