# Roadmap técnico do W_Flyer

> Status: canônico. Revisão: 2026-07-27.

## Regra de progressão

Uma fase só termina com código, testes, evidência e documentação coerentes. Bloqueios permanecem visíveis; não se avança criando stubs que fingem atender o gate.


## Gate transversal de decisões

Além do gate técnico de cada fase, o início e a saída são controlados por `../decision-governance/phase-decision-gates.yaml`. Uma decisão necessária abaixo do estado mínimo ou uma evidência obrigatória ausente bloqueia a fase. A IA não pode conceder waiver nem promover decisão para `DECIDED`.

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

## Dependência externa — empresa e site institucional

A abertura da empresa e o site `wflyer.com.br` possuem diretórios/repositórios próprios. Este roadmap não governa a implementação desses projetos. A aplicação apenas registra dependências de lançamento, como dados legais reais, políticas, billing e fiscal. Os IDs legados `PEND-026` e `PEND-027` permanecem reservados para registrar que site institucional e hospedagem de clientes foram movidos para contextos externos. As decisões canônicas `DEC-026` e `DEC-027` tratam, respectivamente, de provedor de pagamento e modelo de preços/créditos.

## Trilha B — billing

| Fase | Nome | Gate |
|---:|---|---|
| B0 | Domínio de planos/créditos | ledger, reservas e entitlements testados sem gateway |
| B1 | Spike Stripe/Mercado Pago | cenários equivalentes comprovados em sandbox |
| B2 | Provedor escolhido | ADR aceita, conta aprovada e custos revisados |
| B3 | Assinaturas | checkout, webhook, portal e renovação testados |
| B4 | Reembolso/reconciliação | eventos duplicados, disputas e divergências cobertos |

## Trilha F — fiscal

| Fase | Nome | Gate |
|---:|---|---|
| F0 | Definição contábil | empresa, município, regime, serviço e emissor confirmados |
| F1 | Homologação NFS-e | autenticação, emissão, consulta, cancelamento e XML aprovados |
| F2 | Integração assíncrona | fila, retries, contingência e reconciliação testados |
| F3 | Produção | contador aprova e emissão real é monitorada |

## Trilha INF — infraestrutura comercial

| Fase | Nome | Gate |
|---:|---|---|
| INF0 | Domínio e ambientes | DNS, HTTPS, contas e separação definidas |
| INF1 | Staging | deploy reproduzível, observabilidade e backup |
| INF2 | Produção AWS | HA, filas, RDS, S3 e segurança aprovados |
| INF3 | Disaster recovery | restore e runbooks exercitados |

Billing e fiscal não bloqueiam a construção técnica do Core, mas bloqueiam o lançamento pago.

## Fora do roadmap inicial

- multiparte e multipauta;
- manuscritos, tablatura, percussão não afinada e microtons;
- editor visual completo;
- login/biblioteca/pagamento/compartilhamento/push;
- reprodução/MIDI e integração Spotify;
- identidade tipográfica/layout idênticos ao original.

## Trilha FE — referências visuais e frontend

| Fase | Nome | Gate |
|---:|---|---|
| FE0 | Aprovação das referências | golden examples do Core, mobile, acessibilidade e identidade provisória aprovados |

## Trilha D — Musical Diff

| Fase | Nome | Gate |
|---:|---|---|
| D0 | Diff verificável | IDs, proveniência, cobertura e gaps materiais aprovados |

## Trilha A — Áudio e modo de ensaio

| Fase | Nome | Gate |
|---:|---|---|
| A0 | Engines e mapa de playback | licenças, privacidade e score following avaliados |

## Trilha T — Tocabilidade e adaptação idiomática

| Fase | Nome | Gate |
|---:|---|---|
| T0 | Gate instrumental | perfis, corpus e revisão por instrumentistas aprovados |

## Trilha E — Ensemble

| Fase | Nome | Gate |
|---:|---|---|
| E0 | Score e partes | consistência, transposição e tocabilidade validadas |

## Trilha C — Colaboração

| Fase | Nome | Gate |
|---:|---|---|
| C0 | Revisão colaborativa | identidade, autorização, concorrência e retenção aprovadas |

## Trilha Q — qualidade musical e conselho

| Fase | Nome | Gate |
|---:|---|---|
| Q0 | Conselho e corpus | papéis, licenças, protocolo e auditoria aprovados |

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
| FE | referências internas, stories e estados | Fase 0 do Core | manifesto validado e aprovação de composição |
| D | IDs, proveniência e Musical Diff | Core 2–5 | grafo semântico e mapeamento estável |
| A | áudio A/B e modo de ensaio | D + renderer/playback | licenças de samples e mapa de ocorrência |
| T | tocabilidade e adaptação idiomática | M + perfis | conselho instrumental e corpus |
| E | score, partes e pacote ensemble | M + T + R | fonte única e verificador score/partes |
| C | revisão colaborativa | D + revisões | autorização, ETag e política de retenção |
| Q | pre-mortem, conselho musical e rollout | todas | métricas e riscos pré-registrados |

### Sequência recomendada

```text
Core 0 -> FE0
Core 2/3 -> D0
M -> L -> T
L + T + análise formal -> H
M + T + H + R -> E
D + mapa de playback -> A
D + revisões + segurança -> C
Q acompanha cada gate
```

### Regra de não antecipação

- Uma tela avançada não autoriza endpoint fictício.
- Um modelo de IA disponível não autoriza capability.
- Um resultado “bonito” não substitui corpus, invariantes e revisão musical.
- Infraestrutura para IDs, versões e proveniência pode ser criada cedo; comportamento avançado permanece desligado.

## Mapa de decisões por trilha

A relação executável não é mantida manualmente nesta página. Consulte `../decision-governance/phase-decision-gates.yaml`, que liga `DGATE-*`, `DEC-*` e `EVID-*` a cada fase.

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
| FE | pacote de referências visuais executáveis | tokens, specs, protótipos e aprovação de baseline |
| D | Musical Diff e audição A/B | IDs/proveniência estáveis e playback manifest |
| M/L | modelo polifônico e extração de melodia | grafo multipauta, corpus anotado e revisão humana |
| T | tocabilidade e adaptação idiomática | perfis revisados por instrumentistas |
| H | análise/harmonização | melodia confirmada, análise por região e avaliação cega |
| E | ensemble, score e partes | grafo multiparte e verificador de consistência |
| Q | ensaio e colaboração | reprodução estável, âncoras versionadas e segurança |

A ordem não implica que todas as trilhas entrarão no primeiro produto comercial. Cada uma permanece `off` até seus gates.

<!-- DECISION-GATES:START -->
## Gate adicional de decisões e evidências

Cada fase conserva seus critérios técnicos originais e também consulta `../decision-governance/phase-decision-gates.yaml`.

```text
gate de entrada → trabalho autorizado → gate de saída → conclusão da fase
```

Um gate vazio significa apenas que não há decisão adicional naquele momento; testes, segurança, documentação e aceite continuam obrigatórios. Ferramentas opcionais foram movidas para fases `FUTURE-*` para não bloquear o Core.
<!-- DECISION-GATES:END -->
