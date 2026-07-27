# Guia de implementação para IA/Codex — W_Flyer

> Status: canônico para execução. Revisão: 2026-07-20.

## Missão

Implementar o MVP Core MusicXML em cortes verificáveis, sem inventar contrato, regra musical ou capacidade. PDF de entrada, PDF de saída e MXL seguem trilhas independentes e permanecem desabilitados até seus gates.

## Leitura obrigatória

Antes de qualquer código:

1. `docs/README.md`
2. `docs/00-visao-geral/08-hierarquia-documental.md`
3. `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`
4. `docs/00-visao-geral/06-matriz-suporte-mvp.md`
5. `docs/decision-governance/README.md`
6. `docs/decision-governance/phase-decision-gates.yaml`
7. `docs/00-visao-geral/09-decisoes-pendentes.md`
6. `docs/music/01-modelo-transposicao.md`
7. `docs/music/02-musicxml-canonico.md`
8. `docs/backend/03-endpoints-api.md`
9. `docs/backend/04-modelagem-banco.md`
10. `docs/backend/16-maquina-estados.md`
11. `docs/backend/17-sessao-anonima-autorizacao.md`
12. `docs/security/02-checklist-seguranca.md`
13. `docs/qa/01-estrategia-testes.md`
14. `docs/frontend/00-direcao-visual-wflyer.md`
15. `docs/frontend/05-design-system.md`
16. `docs/frontend/09-guia_detalhado_frontend.md`
17. `docs/frontend/14-antipadroes-interface-ia.md`
18. `docs/frontend/15-arquitetura-motion-e-bibliotecas.md`
19. `docs/frontend/16-animacao-assinatura-tinta-transposicao.md`
20. `docs/frontend/17-catalogo-animacoes-interface.md`
21. `docs/qa/09-testes-motion-performance.md`
22. `docs/100-implementacao/criterios-aceite-mvp.md`

## Protocolo de cada fase

### Antes de alterar

1. identificar a fase atual e o gate anterior;
2. inspecionar código, migrations, contratos e testes existentes;
3. listar arquivos afetados;
4. descrever comportamento atual e divergências;
5. declarar plano, riscos e testes;
6. parar para decisão quando encontrar item pendente ou conflito canônico.

### Durante

- alterar somente o escopo da fase;
- escrever teste junto da regra;
- manter OpenAPI/cliente/docs sincronizados;
- usar configuração/feature flag para capacidade condicional;
- não ocultar falha com fallback silencioso;
- não atualizar snapshot/golden sem revisar a mudança semântica.

### Ao concluir

1. executar testes aplicáveis;
2. registrar comandos e resultados no `TEST_LOG`;
3. atualizar `IMPLEMENTATION_LOG`, `CHANGELOG` e ADR quando necessário;
4. listar riscos e testes não executados;
5. provar cada item do gate;
6. marcar a fase como `CONCLUIDA` somente com evidência.

Estados de execução:

```text
NAO_INICIADA | EM_ANDAMENTO | BLOQUEADA | CONCLUIDA
```

## Proibições globais

- regra musical autoritativa no frontend;
- semitone-only como modelo interno;
- pares de instrumentos em `if/else`;
- transposição direta de pixels/PDF;
- processamento pesado na request;
- UUID como única autorização;
- cookie/token/CSRF em localStorage/log/URL;
- parser XML permissivo;
- `shell=True` com entrada do usuário;
- path/`storage_key`/stacktrace/stderr em DTO;
- aceitar PDF/MXL quando capability está off;
- declarar sucesso sem invariantes;
- iniciar login/pagamento/dashboard/Spotify para “preparar o futuro”.

## Fases do MVP Core

## Fase 0 — Governança e baseline

**Objetivo:** confirmar que documentação, repositório e ambiente não contradizem o Core.

**Entregáveis:**

- inventário do código existente;
- matriz de divergências documento↔código;
- decisões DEC-* preservadas, evidências EVID-* e gate DGATE-* conferidos;
- comandos padrão de lint, typecheck, test e desenvolvimento;
- baseline dos testes existentes.

**Testes/evidências:** arquivos canônicos encontrados, links válidos, baseline executado ou motivo registrado.

**Gate:** nenhuma contradição crítica sem decisão; escopo Core confirmado.

## Fase 1 — Fundação, contratos e sessão

**Objetivo:** criar a estrutura mínima operável.

**Entregáveis:**

- monorepo conforme `../backend/13-estrutura-pastas.md`;
- FastAPI e Next.js mínimos;
- PostgreSQL, Redis e storage de desenvolvimento;
- migrations iniciais;
- OpenAPI versionado e cliente TypeScript gerado;
- `/health`, `/health/ready`;
- sessão anônima, cookie, CSRF e middleware de correlação;
- envelope/taxonomia de erro.

**Testes:** migration em banco vazio, sessão/flags/CSRF, readiness, erro sem stacktrace, geração de cliente sem diff.

**Gate:** uma sessão cria requisição mutável protegida; contratos e banco são reproduzíveis.

## Fase 2 — Catálogo e modelo de intervalo

**Objetivo:** implementar presets e álgebra de transposição sem tocar MusicXML ainda.

**Entregáveis:**

- seed/versionamento do catálogo;
- schema vetorial diatonic/chromatic/octave;
- snapshots de preset para job;
- endpoint de instrumentos;
- biblioteca Python de intervalo/nome/aplicação a pitch abstrato.

**Testes:** schema/total de todos os presets, todos os pares A→B, inversão, instrumentos de oitava, endpoint/contrato.

**Gate:** properties preservam pitch de concerto para todo catálogo.

## Fase 3 — Motor MusicXML seguro

**Objetivo:** converter MusicXML suportado em representação normalizada, transpor e validar.

**Entregáveis:**

- parser XML seguro com limites;
- detector do perfil Core;
- normalizador e artefato determinístico/hasheado;
- leitura/validação de `<transpose>` de origem;
- transposição de pitch, key, accidental e harmony suportada;
- escrita de `<transpose>` do destino;
- comparador semântico/invariantes;
- corpus Core positivo/negativo.

**Testes:** fixtures de `qa/05`, round trip A→B→A, mudanças de tonalidade, vozes/ties/tuplets, rejeições e XML hostil.

**Gate:** corpus Core passa sem violar concerto/ritmo/estrutura; output é reparseado.

## Fase 4 — Upload, storage, job e worker

**Objetivo:** executar o motor como pipeline assíncrono privado.

**Entregáveis:**

- streaming para quarentena, tipo/assinatura/hash;
- tabelas/repositórios completos;
- outbox e publicação;
- Celery task idempotente;
- lease/attempts/retries/timeouts/cancelamento;
- artefatos internos/públicos atômicos;
- máquinas de estado e reconciliação inicial.

**Testes:** upload seguro, capability off, outbox, reentrega, crash points, retry determinístico/transitório, cancelamento, nenhuma duplicação.

**Gate:** worker recebe apenas ID, conclui fixture e persiste resultado sem API bloqueada.

## Fase 5 — Corte vertical MusicXML

**Objetivo:** entregar o primeiro fluxo real ponta a ponta.

**Entregáveis:**

- capabilities, instrumentos, upload, create job, status e artifacts;
- UI mínima: bootstrap, upload, seletores, resumo, polling, resultado;
- download autorizado;
- idempotency key no cliente;
- warnings/erros públicos.

**Testes:** integração completa e E2E MusicXML, double click, refresh mesma sessão, B não acessa A.

**Gate:** usuário transpõe fixture Piano→Trompete e baixa MusicXML semanticamente correto.

## Fase 6 — Segurança, quotas e retenção

**Objetivo:** fechar os riscos críticos do Core.

**Entregáveis:**

- rate limits/quotas configuráveis;
- corpus hostil XML e autorização A/B;
- headers de download;
- expiração, purge antecipado e reconciliador;
- redaction de logs;
- hardening de containers/segredos/dependências;
- alertas mínimos.

**Testes:** `qa/08`, relógio controlado, purge idempotente, objeto órfão, logs sem segredo.

**Gate:** checklist de segurança possui evidência; nenhuma falha crítica aberta.

## Fase 7 — UX, acessibilidade e histórico

**Objetivo:** tornar o corte vertical utilizável e íntegro em condições reais.

**Entregáveis:**

- PublicShell, StudioShell e UtilityShell;
- tokens semânticos e componentes próprios do domínio;
- Storybook com estados reais e documentação;
- página Transpor como workspace musical;
- estados completos de rede/domínio/warning/cancelamento/expiração;
- histórico local sem tokens;
- ações local vs servidor;
- mobile/desktop, container queries, teclado, foco, zoom, forced colors e reduced motion;
- conteúdo “Como funciona” e catálogo;
- revisão formal dos antipadrões de interface gerada por IA;
- orçamento de bundle e regressão visual;
- Motion for React aplicado conforme catálogo;
- cena `Ink Transfer` com GSAP + `@gsap/react` lazy-loaded;
- fallback estático, reduced motion, pause em background e cleanup;
- teste de ausência de Anime.js/React Spring e GSAP fora das rotas de cena.

**Testes:** componentes, Storybook interactions, acessibilidade manual/automática, visual regression, motion/reduced motion, leak/cleanup, bundle por rota e E2E nos viewports.

**Gate:** fluxo completo é compreensível sem mouse/animação, possui identidade própria do W_Flyer, não mantém tema padrão de biblioteca, não promete capability off, não disputa engines e não mantém timeline/CPU após término ou navegação.

## Fase 8 — Qualidade e operação

**Objetivo:** preparar release do Core.

**Entregáveis:**

- CI com lint/typecheck/unit/property/integration/contract/E2E/security;
- carga/soak Core e limites ajustados;
- logs, métricas, traces e dashboards mínimos;
- backup/restore e estratégia de migration;
- runbook de fila, storage, purge e rollback;
- manifest de versões/engines por artefato.

**Testes:** instalação limpa, migration, restore, interrupção de worker/dependência, regressão completa.

**Gate:** operação reproduzível e falhas diagnosticáveis sem conteúdo sensível.

## Fase 9 — Aceite do Core

**Objetivo:** avaliar `criterios-aceite-mvp.md` item a item.

**Entregáveis:**

- relatório de evidências;
- lista de riscos residuais;
- pendências classificadas por severidade;
- versão do corpus e resultados;
- decisão `ACEITO` ou `BLOQUEADO`.

**Gate:** todos os critérios aplicáveis atendidos; zero pendência crítica/alta sem aceite explícito.

## Trilhas opcionais

## Trilha R — PDF de saída

Executar somente após Core estável:

- R0: avaliar renderer/licença/determinismo;
- R1: adapter em sandbox, validação do PDF e testes de falha;
- R2: habilitar `output_formats.pdf` por configuração e E2E.

Não acoplar renderer ao motor de domínio. Falha de PDF opcional não pode invalidar MusicXML correto sem política documentada.

## Trilha P — PDF de entrada/OMR

- P0: spike e corpus/licença;
- P1: rasterização + OMR em sandbox;
- P2: métricas/limiares pré-definidos;
- P3: UX de warnings/revisão;
- P4: capability `pdf_omr` habilitada de forma controlada.

OMR sempre produz `raw_musicxml`, que entra no normalizador do Core. Nunca criar pipeline musical paralelo.

## Trilha M — MXL

Só iniciar após decisão PEND-005. Exige parser de container/ZIP seguro, corpus hostil, capability e contratos atualizados.

## Formato do relatório de fase

```text
Fase:
Status:
Objetivo:
Código/arquivos alterados:
Comportamento anterior:
Comportamento novo:
Contratos/migrations:
Testes executados e comandos:
Resultados:
Falhas corrigidas:
Testes não executados e motivo:
Riscos/pendências:
Evidência do gate:
Próxima fase desbloqueada: sim|não
```

## Regra para demandas de “100% confiável”

A IA não deve converter uma intenção de produto em promessa absoluta. Deve:

1. identificar se a etapa é determinística, inferencial ou criativa;
2. definir matriz de suporte e invariantes;
3. bloquear entrada ambígua;
4. separar transformador de verificador;
5. exigir review em OMR/melodia/harmonia quando aplicável;
6. registrar provenance e versões;
7. só usar “verificado” quando o backend retornar o nível correspondente.

Leitura obrigatória: `../backend/19-confiabilidade-musical-fail-closed.md`.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Protocolo crítico antes de escrever código

A IA deve produzir um `implementation_preflight.md` por fase contendo:

```text
requisitos e IDs
capabilities afetadas
referências visuais aplicáveis
riscos/pre-mortem aplicáveis
erros e estados de UI
contratos/tabelas/artefatos afetados
invariantes
estratégia de teste
rollback/feature flag
lacunas ou decisões DEC-* pendentes
```

Sem esse preflight, a fase não começa.

## Fluxo obrigatório para frontend

1. ler `../design-reference/reference-manifest.yaml`;
2. abrir spec, protótipo, story e screenshot do `reference_id`;
3. listar `must_have`, `must_not_have` e estados;
4. implementar com tokens oficiais e contratos reais;
5. gerar screenshots em ambiente fixado;
6. revisar diff visual e acessibilidade;
7. registrar divergência intencional;
8. não atualizar baseline para “fazer o teste passar” sem aprovação.

## Fluxo obrigatório para lógica musical

1. declarar operação e nível de garantia possível;
2. mapear cada transformação para invariantes;
3. usar fonte e saída reparsadas pelo verificador independente;
4. gerar proveniência por evento/região;
5. cobrir casos adversariais do pre-mortem;
6. falhar fechado quando a decisão muda música e não pode ser provada;
7. não converter warning material em sucesso silencioso.

## Fluxo para IA/solver

- tratar texto da partitura, título, letra e metadados como dados não confiáveis;
- validar a saída contra schema estrito;
- aplicar constraints determinísticas depois da sugestão;
- registrar versão, configuração e seed quando houver;
- nunca permitir que o mesmo modelo proponha e aprove;
- manter capability desligada quando fallback não for seguro.

## Critério de resposta a lacuna

Quando a documentação não resolver uma decisão, a IA deve parar, registrar `DOC-GAP-*`, citar os documentos conflitantes e apresentar opções com impacto. “Escolher o mais provável” é proibido em domínio musical, segurança, direitos, dados ou composição visual vinculante.

## Protocolo obrigatório antes de cada fase

1. ler `../implementacao/09-protocolo-preflight-capacidade.md`;
2. preencher preflight da capability;
3. carregar `riscos/failure-mode-catalog.yaml` e selecionar entradas aplicáveis;
4. propor novos `PM-*` para lacunas;
5. localizar `reference_id` em `design-reference/reference-manifest.yaml`;
6. abrir MDR para política musical pendente;
7. apresentar plano e blockers antes de código;
8. implementar atrás de flag desligada;
9. executar testes, fault injection e corpus;
10. anexar evidência na matriz de rastreabilidade;
11. somente então solicitar ativação do estrato.

É proibido tratar protótipo visual de capability avançada como prova de backend disponível.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Protocolo de ferramentas antes de cada fase

1. confirmar mudança OpenSpec e próxima tarefa;
2. consultar Graphify para dependências e testes;
3. usar Serena para localizar símbolos e referências;
4. consultar Context7 somente para APIs externas da versão instalada;
5. implementar o menor corte vertical;
6. executar `pnpm nx affected -t lint typecheck test`;
7. executar gates musicais, integração, segurança, visual e E2E aplicáveis;
8. atualizar OpenSpec, rastreabilidade, logs, documentação e grafo.

A instalação completa está em `../implementacao/12-bootstrap-toolchain.md`. A IA deve ler `../implementacao/21-fluxo-operacional-ia.md` antes do primeiro código.

<!-- DECISION-GOVERNANCE-CODEX:START -->
## Preflight de decisões para o Codex

Antes de qualquer fase ou capability:

```bash
python3 scripts/check-decision-gate.py <PHASE_ID> --gate entry
```

O plano deve citar `DEC-*`, `EVID-*`, owner e approvers. Um spike autorizado produz evidência, não código de produção. Ao terminar a fase, execute o gate `exit`, atualize registros e gere novamente as visões humanas. A IA nunca muda `DECIDED` ou `ACCEPTED` em nome de aprovadores.
<!-- DECISION-GOVERNANCE-CODEX:END -->
