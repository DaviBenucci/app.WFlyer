# Roadmap técnico do W_Flyer

> Status: canônico. Revisão: 2026-07-20.

## Regra de progressão

Uma fase só termina com código, testes, evidência e documentação coerentes. Bloqueios permanecem visíveis; não se avança criando stubs que fingem atender o gate.

## MVP Core — MusicXML

| Fase | Nome | Gate de saída |
|---:|---|---|
| 0 | Governança documental | Escopo, matriz, ADRs e pendências aprovados. |
| 1 | Fundação e contratos | Monorepo, CI, API base, OpenAPI, banco, migrations e sessão anônima testados. |
| 2 | Catálogo e modelo musical | Presets vetoriais, snapshots e properties de todos os pares aprovados. |
| 3 | Motor MusicXML | Parsing seguro, normalização, transposição e invariantes passam no corpus Core. |
| 4 | Upload, storage e fila | Quarentena, hashes, outbox, worker idempotente e estados testados. |
| 5 | Corte vertical funcional | MusicXML entra, job assíncrono conclui e MusicXML transposto baixa pela mesma sessão. |
| 6 | Segurança e retenção | CSRF/IDOR, corpus hostil, quotas, expiração, purge e reconciliação aprovados. |
| 7 | UX, acessibilidade e histórico | Fluxo responsivo, teclado, warnings, cancelamento e histórico local completos. |
| 8 | Qualidade e operação | Contratos, E2E, carga Core, observabilidade, migrations e recuperação aprovados. |
| 9 | Aceite do Core | Todos os critérios de aceite atendidos; nenhuma pendência crítica. |

## Trilha R — PDF de saída opcional

Não bloqueia o Core:

| Fase | Nome | Gate |
|---:|---|---|
| R0 | Spike do renderer | CLI/API, licença, determinismo e recursos avaliados. |
| R1 | Adapter e sandbox | Renderização isolada, output validado e falhas categorizadas. |
| R2 | Habilitação | `output_formats.pdf=true` somente no ambiente aprovado. |

## Trilha P — PDF de entrada/OMR

Não bloqueia o Core e não pode ser ativada por conveniência:

| Fase | Nome | Gate |
|---:|---|---|
| P0 | Spike de OMR | Engine, licença, automação, custo e corpus avaliados. |
| P1 | Rasterização/adapter/sandbox | Pipeline isolado sem rede, com limites e manifest. |
| P2 | Corpus e métricas | Métricas definidas previamente e limiares atingidos. |
| P3 | UX de incerteza | Warnings/falha segura/revisão externa validados. |
| P4 | Habilitação controlada | `pdf_omr=true` apenas no ambiente aprovado. |

## Fora do roadmap inicial

- multiparte e multipauta;
- manuscritos, tablatura, percussão não afinada e microtons;
- editor visual completo;
- login/biblioteca/pagamento/compartilhamento/push;
- reprodução/MIDI e integração Spotify;
- identidade tipográfica/layout idênticos ao original.

## Trilha M — Multipauta, multiparte e modelo polifônico

| Fase | Nome | Gate |
|---:|---|---|
| M0 | Modelo canônico avançado | Partes, pautas, vozes, cross-staff e eventos estáveis aprovados. |
| M1 | Parser/normalizador | Corpus multipauta/multiparte preservado semanticamente. |
| M2 | Perfil instrumental | Polifonia, extensão e incompatibilidades versionadas. |
| M3 | Habilitação estrutural | Capabilities e UX de seleção de parte/pauta aprovadas. |

## Trilha L — Extração de melodia

| Fase | Nome | Gate |
|---:|---|---|
| L0 | Corpus rotulado | Segmentos e eventos melódicos revisados por músicos. |
| L1 | Baselines | Regras, skyline e modelos comparados sem publicação automática. |
| L2 | Ambiguidade e revisão | Calibração, alternativas e workspace de confirmação aprovados. |
| L3 | Redução monofônica | Range, oitava, ties e provenance passam nos testes. |
| L4 | Habilitação | `melody_extraction=true` somente após gate congelado. |

## Trilha H — Harmonização

| Fase | Nome | Gate |
|---:|---|---|
| H0 | Perfis e teoria | Linguagens, modos, restrições e instrumentos aprovados por músico. |
| H1 | Motor explicável | Regras + busca geram planos reproduzíveis. |
| H2 | Voicing/tocabilidade | Range, polifonia, span e condução de vozes passam. |
| H3 | Variantes e revisão | Comparação, audição e aceite do usuário completos. |
| H4 | Gate humano | Corpus por estilo e avaliação independente aprovados. |
| H5 | Habilitação | `harmonization=true` com rollout controlado. |

## Trilha W — Watermark e proveniência

| Fase | Nome | Gate |
|---:|---|---|
| W0 | Renderer geometry | Bounding boxes e safe zones disponíveis. |
| W1 | Marca distribuída | Tela/impressão/acessibilidade aprovadas. |
| W2 | Manifesto e assinatura | KMS, verificação, rotação e privacidade aprovados. |
| W3 | Habilitação | PDF final inclui token e prova sem interferência musical. |

## Ordem de dependência das trilhas avançadas

```text
M -> L -> H
R -> W
P -> revisão da origem -> L/H quando solicitado
```

A trilha H não pode começar pelo modelo generativo antes de M, L e perfis instrumentais estarem maduros.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Integração das trilhas críticas

As trilhas abaixo não alteram a promessa do MVP Core; elas evitam que a arquitetura inicial inviabilize os diferenciais futuros.

| Trilha | Objetivo | Dependência mínima | Gate de início |
|---|---|---|---|
| F0 | referências internas, stories e estados | Fase 0 do Core | manifesto validado e aprovação de composição |
| D | IDs, proveniência e Musical Diff | Core 2–5 | grafo semântico e mapeamento estável |
| A | áudio A/B e modo de ensaio | D + renderer/playback | licenças de samples e mapa de ocorrência |
| I | tocabilidade e adaptação idiomática | M + perfis | conselho instrumental e corpus |
| E | score, partes e pacote ensemble | M + I + R | fonte única e verificador score/partes |
| C | revisão colaborativa | D + revisões | autorização, ETag e política de retenção |
| Q | pre-mortem, conselho musical e rollout | todas | métricas e riscos pré-registrados |

### Sequência recomendada

```text
Core 0 -> F0
Core 2/3 -> D0
M -> L -> I
L + I + análise formal -> H
M + I + H + R -> E
D + mapa de playback -> A
D + revisões + segurança -> C
Q acompanha cada gate
```

### Regra de não antecipação

- Uma tela avançada não autoriza endpoint fictício.
- Um modelo de IA disponível não autoriza capability.
- Um resultado “bonito” não substitui corpus, invariantes e revisão musical.
- Infraestrutura para IDs, versões e proveniência pode ser criada cedo; comportamento avançado permanece desligado.

## Gate de documentação antes do primeiro commit funcional

- riscos críticos possuem owner e teste planejado;
- decisões pendentes relevantes estão explícitas;
- schemas de referência visual validam;
- contrato de capability e operação está fechado;
- dados não suportados possuem erro e estado de UI definidos;
- nenhum épico avançado aparece como funcional no Core.

## Trilhas críticas adicionadas

O detalhamento está em `../100-implementacao/plano-evolucao-avancada.md`.

| Trilha | Entrega | Pré-requisito bloqueante |
|---|---|---|
| F0 | pacote de referências visuais executáveis | tokens, specs, protótipos e aprovação de baseline |
| D | Musical Diff e audição A/B | IDs/proveniência estáveis e playback manifest |
| M/L | modelo polifônico e extração de melodia | grafo multipauta, corpus anotado e revisão humana |
| A | tocabilidade e adaptação idiomática | perfis revisados por instrumentistas |
| H | análise/harmonização | melodia confirmada, análise por região e avaliação cega |
| E | ensemble, score e partes | grafo multiparte e verificador de consistência |
| Q | ensaio e colaboração | reprodução estável, âncoras versionadas e segurança |

A ordem não implica que todas as trilhas entrarão no primeiro produto comercial. Cada uma permanece `off` até seus gates.
