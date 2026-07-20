# Changelog

## 2026-07-20 — Arquitetura de motion e animação-assinatura

### Decidido

- Motion for React é a engine padrão das animações declarativas da UI.
- GSAP com `@gsap/react` é restrito a cenas SVG/timelines isoladas e lazy-loaded.
- Anime.js e React Spring não integram o MVP Core para evitar sobreposição.
- Cada nó visual possui uma única engine proprietária.

### Adicionado

- comparação técnica entre Motion, GSAP, Anime.js e React Spring;
- especificação `Ink Transfer` para entrada, processamento e resultado;
- catálogo de microinterações por componente;
- estratégia de reduced motion, fallback estático e interrupção;
- testes de Strict Mode, cleanup, background, bundle e performance;
- ADRs 019 e 020.

### Alterado

- Home passou a prever entrada musical integrada ao hero, sem splash;
- Studio e Resultado receberam regras de motion orientadas a estado;
- stack, critérios de aceite, guia Codex, acessibilidade e performance foram atualizados.

### Observação

Esta alteração documenta motion. Não implementa as bibliotecas ou a cena no código.

## 2026-07-20 — Modernização e identidade do frontend

### Alterado

- Frontend deixou de ser especificado como dashboard/sidebar genérico e passou a usar PublicShell, StudioShell e UtilityShell.
- Tela Transpor foi redesenhada documentalmente como workspace com ScoreSurface, ContextInspector e StickyActionBar.
- Navegação desktop usa header público e navigation rail compacta; mobile usa bottom nav com Transpor central.
- Design system ganhou tokens OKLCH, tipografia, espaçamento, radius, elevação, iconografia e regras de composição.
- Páginas Home, Transpor, Resultado, Como funciona, Instrumentos, Histórico e Configurações receberam especificações visuais detalhadas.
- Acessibilidade foi alinhada à meta WCAG 2.2 AA.
- Critérios de aceite e guia Codex passaram a exigir identidade própria, Storybook, visual regression e revisão de antipadrões.

### Adicionado

- direção visual do W_Flyer;
- arquitetura de componentes e limites Server/Client;
- guia de microcopy;
- performance e qualidade visual;
- governança de Storybook;
- antipadrões de interface gerada por IA.

### Observação

Esta alteração amadurece a documentação do frontend. Não implementa componentes ou páginas no código.

## 2026-07-20 — Revisão técnica de maturidade documental

### Corrigido

- Modelo de transposição deixou de ser um escalar de semitons e passou a usar componentes diatônico, cromático e de oitava.
- Catálogo corrigido para violão, sax tenor e sax barítono, com total derivado e snapshots versionados.
- PDF deixou de ser simultaneamente requisito e “futuro”: o Core é MusicXML e PDF/OMR tem trilha com feature gate.
- Perfil Core definido como uma parte e uma pauta por job.
- Sessão anônima, CSRF e autorização por objeto formalizados; UUID não é autorização.
- Upload, job, stage e retenção receberam máquinas de estado separadas.
- API versionada em `/api/v1`, com capabilities, idempotência, deleção e taxonomia de erros.
- Expiração de job definida somente após sucesso; sessão e cookie renovados de forma coerente com a janela real dos artefatos.
- Taxonomia pública estabilizada em um código por status HTTP, com retry explícito.
- Arquitetura corrigida para manter o motor canônico em Python e gerar contratos TypeScript via OpenAPI.
- Pipeline MusicXML formalizado em original, raw, normalized, transposed e artefatos opcionais.
- Segurança ampliada para XML hostil, MXL/ZIP, sandbox, quotas, downloads e supply chain.
- Testes ampliados para properties, invariantes, corpus/golden, IDOR/CSRF, reentrega e arquivos hostis.
- Critérios de aceite passaram a validar produto executável, não apenas documentação.

### Adicionado

- `docs/music/` com modelo, MusicXML canônico, enarmonia, OMR e invariantes.
- máquina de estados, sessão/autorização e taxonomia de erros no backend.
- matriz de suporte, hierarquia documental e decisões pendentes.
- corpus/fixtures, testes hostis e política de sandbox.
- fontes técnicas primárias.
- trilhas separadas para PDF de saída, PDF/OMR e MXL.

### Observação

Esta alteração revisa documentação. Nenhum código de aplicação foi implementado ou validado como parte dela.

## 2026-06-19 — Guia Codex detalhado e backend-first

### Alterado

- Guia de implementação expandido em fases e gates.
- Banco/backend priorizados antes do acabamento visual.
- Contratos, logs e Definition of Done reforçados.
- Guias detalhados de backend e frontend adicionados.

### Observação

Nenhum código de aplicação foi implementado nesta alteração.

## 2026-05-14 — Documentação modular inicial

### Adicionado

- Estrutura modular em Markdown.
- Documentação de páginas, frontend, backend, segurança e QA.
- Logs de implementação, testes e decisões.

### Observação

Nenhum código final de aplicação foi criado nesta etapa.

## 2026-07-20 — confiabilidade musical avançada

- separadas transposição, extração, redução, harmonização e arranjo;
- adicionada política fail-closed e verificador independente;
- criado modelo de provenance, manifesto e níveis de garantia;
- documentados perfis instrumentais, workspace de revisão e harmonização modal/tonal;
- criada estratégia de watermark distribuído e assinatura;
- adicionadas trilhas M/L/H/W e gates de QA/segurança.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## 2026-07-20 — Integração da visão crítica e pre-mortem

### Adicionado

- visão de produto como preparação musical verificável;
- pacote interno de referências visuais e protótipos;
- Musical Diff, tocabilidade, áudio/ensaio, score/partes, ensemble e colaboração como trilhas separadas;
- registro de riscos, matriz de 104 falhas conhecidas e política para falhas desconhecidas;
- ADRs de grafo semântico, IA como propositora, revisão imutável, direitos e rollout;
- benchmarks e gates por capacidade;
- contratos avançados, modelos de dados e estados reservados.

### Alterado

- leitura obrigatória e hierarquia;
- roadmap e decisões pendentes;
- critérios de aceite e guia Codex;
- frontend, backend, música, QA e segurança para refletir falhas e controles.

### Limite

A entrega é documental e inclui protótipos estáticos. Não comprova motores musicais, áudio, renderer ou aplicação funcionando.

## 2026-07-20 — visão crítica, referências executáveis e pre-mortem

### Adicionado

- tese profissional do produto e princípios de controle humano;
- referências visuais internas com YAML, protótipos HTML e baselines PNG;
- Musical Diff, audição A/B, modo de ensaio, tocabilidade, adaptação, ensemble e revisão;
- análise de forma, cadência, tensão e representação harmônica;
- backend de revisões, playback manifest, score/partes, feature flags e governança de modelos;
- 155 modos de falha em matriz e catálogo legível por máquina;
- política fail-closed para falhas desconhecidas e incidentes;
- preflight por capability, MDR e matriz de rastreabilidade;
- benchmarks musicais, fault injection, regressão visual e gate de conselho musical.

### Alterado

- índices, ADRs, escopo, roadmap, API, modelo, estados, erros, observabilidade, frontend, QA, DoD e guia Codex foram integrados à visão crítica.

### Observação

A entrega é documental. Protótipos e baselines não são código de produção; capabilities avançadas permanecem desabilitadas até seus gates.
