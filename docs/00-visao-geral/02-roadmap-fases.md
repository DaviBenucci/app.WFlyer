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
