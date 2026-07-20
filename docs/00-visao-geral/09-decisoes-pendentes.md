# Decisões pendentes

> Status: canônico. Revisão: 2026-07-20.

A IA não pode decidir os itens abaixo sem aprovação explícita.

## PEND-001 — Engine OMR de produção

Avaliar pelo menos:

- qualidade no corpus do W_Flyer;
- execução automatizável;
- isolamento;
- manutenção;
- licença e obrigações de distribuição;
- custo operacional;
- formato e qualidade do MusicXML exportado.

Candidato de spike: Audiveris. Não é decisão de produção.

## PEND-002 — Engine de renderização

Avaliar CLI/API, determinismo, fontes, licença, consumo de recursos e fidelidade. MuseScore Studio pode ser usado no spike, mas não deve ser acoplado diretamente ao domínio.

## PEND-003 — Limites operacionais

Definir após benchmark:

- tamanho máximo por formato;
- páginas por PDF;
- medidas/notas por MusicXML;
- profundidade/nós XML;
- tempo por etapa;
- memória e CPU por worker;
- jobs simultâneos por sessão/IP.

Antes da decisão, usar limites conservadores em configuração e manter PDF desabilitado.

## PEND-004 — Gate quantitativo de PDF

Definir métricas e limiares mínimos do corpus antes de ativar `pdf_omr`. O gate deve medir estrutura, alturas, ritmos, armaduras, estabilidade e taxa de revisão necessária.

## PEND-005 — Suporte a `.mxl`

Só habilitar após validação de container, prevenção de zip slip/zip bomb, limite de entries, tamanho descompactado e recursos referenciados.

## PEND-006 — Expansão para multiparte/multipauta

Exige UX de seleção de parte, instrumentos por parte, política de pauta/clave e novos testes. Não deve ser implementada como “loop sobre parts”.

## PEND-007 — Baseline de extração de melodia

Comparar regras simbólicas, otimização por caminho e modelos treinados no corpus do W_Flyer. Definir métricas, limiar de ambiguidade e política de confirmação antes de escolher implementação.

## PEND-008 — Perfis harmônicos do primeiro release

Aprovar estilos, modos, cromatismo, condução de vozes, densidade e instrumentos inicialmente suportados. Não habilitar todos os modos apenas porque a escala pode ser enumerada.

## PEND-009 — Engine/solver de harmonização

Decidir entre regras + busca, constraint solver e modelo gerador de candidatos. Avaliar explicabilidade, licença, reprodutibilidade, custo, dados de treino e capacidade de executar localmente.

## PEND-010 — Corpus musical e conselho revisor

Definir músicos responsáveis, protocolo de rotulagem, licenças, independência do conjunto de release e critério de desempate.

## PEND-011 — Infraestrutura de assinatura

Selecionar KMS/HSM, algoritmo, rotação, cadeia de confiança, endpoint de verificação e política após purge.

## PEND-012 — Intensidade e desenho do watermark

Validar por impressão e ensaio: posições, opacidade, repetição, token, perfis preview/final e compatibilidade com acessibilidade.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## PEND-013 — Schema final do grafo semântico

Definir IDs, round trip, relações, eventos de direção, cross-staff, grace/cue/ossia, extensões e política de estabilidade entre revisões.

## PEND-014 — Baseline e aprovação dos golden examples

Aprovar composição, tokens, viewports, estados e screenshots em `../design-reference/`. Protótipos atuais são baseline documental original, não aceite visual de produção.

## PEND-015 — Perfis instrumentais iniciais

Selecionar instrumentos, revisores, ranges absoluto/confortável, polifonia, técnicas, dificuldade por andamento e política de versões.

## PEND-016 — Engine e licenças de áudio

Escolher síntese/samples, licenças de distribuição, normalização de loudness, render offline, latência e suporte mobile.

## PEND-017 — Política de score following

Definir escopo inicial: apenas playback gerado ou também acompanhamento de performance ao vivo. A segunda opção exige pesquisa, microfone, privacidade e benchmark próprios.

## PEND-018 — Métricas de Musical Diff

Definir cobertura mínima de eventos por operação, tolerâncias, categorias de mudança e quais gaps impedem garantia.

## PEND-019 — Gate de tocabilidade e dificuldade

Definir separação entre impossibilidade física, dificuldade, preferência idiomática e nível pedagógico; aprovar por instrumento.

## PEND-020 — Gate de engraving

Definir renderer, fonte, detector de colisões, thresholds de virada, revisão de impressão e matriz de dispositivos.

## PEND-021 — Pacote ensemble inicial

Definir formações, papéis, política de divisi/doubling, score em concerto/escrito, transposição, partes e artefatos.

## PEND-022 — Colaboração e retenção

Definir identidade, convite, revogação, comentários, ETag, auditoria, anonimização, retenção e moderação.

## PEND-023 — Governança de dados para IA

Definir provedores permitidos, localização, retenção zero, uso para treino, consentimento, redaction e avaliação de fornecedores.

## PEND-024 — Protocolo do conselho musical

Definir composição, conflito de interesse, número de revisores, instrumento/estilo, desempate, registro de parecer e validade da aprovação.

## Pendências da visão crítica

As decisões abaixo permanecem abertas e bloqueiam ativação das respectivas capabilities:

- instrumentos e níveis de intérprete do primeiro gate de tocabilidade;
- política por instrumento para oitava, respiração, double stops, span e técnicas especiais;
- taxonomia formal/modal e vocabulário de cadências suportado no primeiro analisador;
- como tratar repertório atonal, politonal, microtonal ou com notação contemporânea;
- pesos e métricas do benchmark de melodia por família de textura;
- linguagens harmônicas do primeiro rollout e regras que são hard constraints versus preferências;
- engine e licença de síntese/sons, além do pacote de samples permitido;
- estratégia de score following quando há repeats ambíguos ou improvisação;
- formação inicial do pacote ensemble;
- modelo de identidade necessário para colaboração e aprovação;
- composição visual final dos baselines internos após revisão humana;
- níveis de severidade que podem degradar para warning sem bloquear publicação;
- owners e datas de revisão de cada risco crítico.

A IA deve registrar essas lacunas em preflight e manter a feature flag desligada.
