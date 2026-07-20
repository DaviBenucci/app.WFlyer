# Decisions Log

> O resumo canônico está em `../00-visao-geral/01-decisoes-arquiteturais.md`.

## ADR-001 — Projeto orientado por documentação canônica

Status: ACEITA

Decisão: usar a hierarquia documental para resolver conflitos; logs históricos não são requisitos.

## ADR-002 — MVP sem conta, com sessão anônima autorizada

Status: ACEITA

Decisão: não exigir cadastro, mas proteger uploads/jobs/artefatos por cookie opaco, CSRF e propriedade por sessão.

## ADR-003 — Core MusicXML antes de PDF

Status: ACEITA

Decisão: o Core aceita MusicXML não comprimido. PDF/OMR permanece desabilitado até a trilha P cumprir seus gates.

## ADR-004 — MusicXML normalizado como representação canônica

Status: ACEITA

Decisão: preservar original e separar `raw_musicxml`, `normalized_musicxml`, `transposed_musicxml` e renderizações.

## ADR-005 — Intervalo vetorial de transposição

Status: ACEITA; SUBSTITUI a formulação escalar anterior.

Decisão: representar `written_to_concert` por componentes diatônico, cromático e de oitava. `total_semitones` é derivado.

Consequência: snapshots, DTOs, catálogo e testes não podem usar apenas um inteiro.

## ADR-006 — Uma parte e uma pauta no Core

Status: ACEITA

Decisão: rejeitar explicitamente multiparte/multipauta e outras estruturas fora da matriz; não processar parcialmente.

## ADR-007 — Processamento assíncrono com banco como fonte de verdade

Status: ACEITA

Decisão: API persiste/outbox; Celery/Redis transporta; worker executa; PostgreSQL mantém o estado. Tarefas são idempotentes.

## ADR-008 — Motor musical canônico em Python

Status: ACEITA

Decisão: backend implementa a regra; frontend usa cliente OpenAPI e apenas apresenta o intervalo retornado.

## ADR-009 — Estados separados

Status: ACEITA

Decisão: `UploadStatus`, `JobStatus`, `ProcessingStage` e `RetentionStatus` são enums distintos.

## ADR-010 — Diagnóstico interno e warnings públicos

Status: ACEITA

Decisão: scores brutos permanecem internos; riscos materiais são comunicados por warnings categóricos. Invariante violado bloqueia resultado.

## ADR-011 — Processadores externos em adapters e sandbox

Status: ACEITA

Decisão: rasterizador, OMR e renderer são substituíveis, versionados e executados sem rede/privilégio, com limites.

## ADR-012 — Fidelidade semântica antes da visual

Status: ACEITA

Decisão: o Core garante semântica musical dentro da matriz; paginação/layout idênticos não são garantidos.

## ADR-013 — Funcionalidades futuras separadas

Status: ACEITA

Decisão: conta, cobrança, nuvem, compartilhamento, push, editor, app nativo e Spotify não bloqueiam nem entram no Core.


## ADR-014 — Escopo futuro não bloqueia o Core

Status: ACEITA

Decisão: login, cobrança, nuvem, compartilhamento, push, editor, app nativo e Spotify permanecem fora do MVP Core.


## ADR-015 — Frontend como workspace musical, não dashboard

Status: ACEITA

Decisão: páginas públicas usam header editorial; transposição/resultado usam StudioShell com canvas e inspector; utilidades usam lista estruturada. Sidebar larga e dashboard genérico não são padrão.

## ADR-016 — Design system próprio sobre primitives headless

Status: ACEITA

Decisão: shadcn/ui/Base UI ou equivalente pode fornecer primitives, mas tokens, composição, componentes de produto e microcopy são próprios do W_Flyer. Tema padrão de biblioteca não é entrega final.

## ADR-017 — Identidade por domínio, não por efeitos

Status: ACEITA

Decisão: a assinatura visual usa papel/tinta, trajetória de transposição e ritmo editorial. Motion é progressivo e funcional; partículas, glow excessivo e card soup são antipadrões.

## ADR-018 — Storybook e visual regression como gates

Status: ACEITA

Decisão: componentes do produto precisam de stories, testes de interação, acessibilidade e regressão visual antes do aceite do frontend.

## ADR-019 — Motion for React como engine padrão e GSAP como engine de cena

Status: ACEITA

Decisão: CSS resolve microestados simples; Motion for React controla presença, layout, gestos e transições da UI; GSAP + `@gsap/react` é lazy-loaded e restrito à animação-assinatura SVG e timelines explicitamente aprovadas. Anime.js e React Spring não entram no MVP Core.

Consequência: cada nó possui uma única engine proprietária; GSAP não pode aparecer no bundle de rotas sem cena; qualquer nova engine exige ADR e remoção de sobreposição.

## ADR-020 — Ink Transfer é cena autoral e não visualização do processamento musical

Status: ACEITA

Decisão: a animação de tinta usa SVG determinístico e exemplo musical validado na Home. Durante processamento ela é metáfora acompanhada do `stage` real. Notas reais do usuário só poderão ser animadas futuramente quando existir `NoteGeometryMap` estável emitido pelo renderer.

Consequência: o MVP não infere semântica por classes/posições do SVG de terceiros, não promete progresso e sempre possui fallback estático/reduced motion.
