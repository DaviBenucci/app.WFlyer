# Guia de implementação para Codex — app.WFlyer

## Regra rígida

```text
O Codex só poderá avançar para a próxima fase quando a fase anterior estiver concluída, testada e documentada.
```

Se surgir bloqueio ou erro, criar subetapa dentro da fase atual, corrigir, validar e registrar antes de avançar.

## Fase 0 — Auditoria documental

Objetivo: confirmar que o escopo técnico está claro e livre de mistura com site institucional, Spotify ou requisitos futuros obrigatórios.

Arquivos envolvidos:

- `README.md`
- `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`
- `docs/100-implementacao/criterios-aceite-mvp.md`

Criar ou alterar: apenas documentação.

Não alterar: código de produção.

Testes obrigatórios: revisão de links internos e busca por termos fora de escopo.

Critério de conclusão: documentação aprovada para iniciar estrutura base.

Riscos: iniciar código com requisitos contraditórios.

Checklist final:

- [ ] Escopo do MVP está explícito.
- [ ] Fora do MVP está explícito.
- [ ] MusicXML-first está documentado.
- [ ] Não há dependência de Spotify.

## Fase 1 — Estrutura base do projeto

Objetivo: criar a organização inicial de pastas sem implementar fluxo musical completo.

Arquivos envolvidos:

- `apps/web/`
- `apps/api/`
- `packages/shared/`
- `packages/ui/`
- `docs/`

Criar: estrutura base, configs mínimas, scripts de lint/test quando definidos.

Alterar: README técnico se a estrutura final divergir da documentação.

Não alterar: regra musical sem testes.

Testes obrigatórios: validação de estrutura e comandos base existentes.

Critério de conclusão: frontend, backend, shared, UI e docs separados.

Riscos: acoplar regra musical ao frontend ou duplicar tipos.

Checklist final:

- [ ] Frontend em `apps/web`.
- [ ] Backend em `apps/api`.
- [ ] Tipos compartilhados em `packages/shared`.
- [ ] Componentes reutilizáveis em `packages/ui`.

## Fase 2 — Backend mínimo

Objetivo: criar a API base com saúde, erros padronizados e módulos vazios.

Arquivos envolvidos:

- `apps/api/src/routes/`
- `apps/api/src/modules/`
- `apps/api/src/middlewares/`
- `apps/api/src/validators/`

Criar: `GET /health`, tratamento de erro, `correlation_id`, validação de payload.

Alterar: contratos em `docs/backend/03-endpoints-api.md` se houver ajuste necessário.

Não alterar: pipeline musical pesado.

Testes obrigatórios: `/health` responde e erro segue envelope padrão.

Critério de conclusão: API base testada.

Riscos: vazar stacktrace ou criar contratos não documentados.

Checklist final:

- [ ] `GET /health` existe.
- [ ] Erro público usa `{ "error": ... }`.
- [ ] `correlation_id` aparece em erros.

## Fase 3 — Banco de dados

Objetivo: criar modelo mínimo para instrumentos, uploads, jobs, artefatos e eventos.

Arquivos envolvidos:

- `apps/api/src/repositories/`
- `apps/api/src/modules/*`
- migrations quando existirem.

Criar: tabelas `instruments`, `uploads`, `processing_jobs`, `generated_artifacts`, `job_events`.

Alterar: `docs/backend/04-modelagem-banco.md` se o nome de campo mudar.

Não alterar: login, planos ou biblioteca em nuvem.

Testes obrigatórios: migrations aplicam e repositórios básicos funcionam.

Critério de conclusão: modelo mínimo persistente e documentado.

Riscos: armazenar binários no banco ou expor `storage_key`.

Checklist final:

- [ ] Tabelas mínimas criadas.
- [ ] Índices básicos documentados.
- [ ] Status permitidos validados.

## Fase 4 — Catálogo de instrumentos

Objetivo: implementar catálogo mínimo com `written_to_concert`.

Arquivos envolvidos:

- `packages/shared/src/music/`
- `apps/api/src/modules/instruments/`
- `docs/features/11-catalogo-instrumentos-mvp.md`

Criar: seed/catálogo, endpoint `GET /api/instruments`, validação de instrumento ativo.

Alterar: docs de catálogo apenas se houver decisão musical justificada.

Não alterar: cálculo por pares hardcoded.

Testes obrigatórios: catálogo retorna todos os instrumentos mínimos e rejeita instrumento inativo.

Critério de conclusão: frontend pode listar origem e destino pela API.

Riscos: duplicar catálogo no frontend.

Checklist final:

- [ ] Instrumentos mínimos existem.
- [ ] `written_to_concert` confere com a documentação.
- [ ] Testes cobrem instrumentos principais.

## Fase 5 — Regra musical e testes unitários

Objetivo: implementar a fórmula central e fixtures MusicXML.

Arquivos envolvidos:

- `packages/shared/src/music/`
- `apps/api/src/modules/music-engine/`
- `W-Flyer_Regra-Transposição.md`
- `docs/qa/05-testes-musicais.md`

Criar: cálculo de intervalo, transposição de notas, acordes, acidentes e armadura sobre representação estruturada.

Alterar: apenas regra musical documentada quando houver correção validada.

Não alterar: PDF real antes de MusicXML estar coberto.

Testes obrigatórios: matriz musical mínima.

Critério de conclusão: MusicXML controlado transpõe corretamente.

Riscos: alterar só tonalidade e esquecer notas/acordes.

Checklist final:

- [ ] Fórmula central testada.
- [ ] Casos inversos testados.
- [ ] Acidentes, acordes e armadura testados.

## Fase 6 — Upload e validação de arquivos

Objetivo: aceitar arquivos permitidos com validação segura.

Arquivos envolvidos:

- `apps/api/src/modules/uploads/`
- `apps/api/src/validators/`
- `docs/security/02-checklist-seguranca.md`

Criar: `POST /api/uploads`, validação de MIME, extensão e tamanho.

Alterar: contratos de upload se necessário.

Não alterar: armazenamento público direto.

Testes obrigatórios: arquivo válido aceito, inválido rejeitado, grande rejeitado.

Critério de conclusão: upload cria registro e não expõe path interno.

Riscos: confiar no nome original ou no header do navegador.

Checklist final:

- [ ] MIME permitido validado.
- [ ] Extensão validada.
- [ ] Nome interno renomeado.

## Fase 7 — Fila e worker

Objetivo: garantir processamento fora da requisição HTTP principal.

Arquivos envolvidos:

- `apps/api/src/modules/jobs/`
- `apps/api/src/workers/`
- `docs/backend/07-filas-e-workers.md`

Criar: publicação de job, worker consumidor, retentativas, timeout e eventos.

Alterar: pipeline assíncrono se houver mudança de status.

Não alterar: processamento síncrono no endpoint.

Testes obrigatórios: job publicado, consumido e atualizado.

Critério de conclusão: worker processa job simulado sem derrubar API.

Riscos: request HTTP ficar presa em processamento pesado.

Checklist final:

- [ ] Job entra em `queued`.
- [ ] Worker muda status.
- [ ] Falha vira `failed` com erro seguro.

## Fase 8 — API de jobs

Objetivo: expor status, progresso, eventos públicos e artefatos do job.

Arquivos envolvidos:

- `apps/api/src/modules/jobs/`
- `apps/api/src/modules/artifacts/`
- `docs/backend/03-endpoints-api.md`

Criar: `GET /api/jobs/{job_id}`, `GET /api/jobs/{job_id}/status`, `GET /api/jobs/{job_id}/artifacts`.

Alterar: DTOs públicos documentados.

Não alterar: campos internos em resposta pública.

Testes obrigatórios: consulta de status, job inexistente, token inválido, job expirado.

Critério de conclusão: frontend consegue acompanhar o processamento.

Riscos: expor logs, stacktrace ou `storage_key`.

Checklist final:

- [ ] Status público funciona.
- [ ] DTO público não vaza dado interno.
- [ ] Eventos públicos são seguros.

## Fase 9 — Frontend funcional mínimo

Objetivo: implementar fluxo visual básico com backend real.

Arquivos envolvidos:

- `apps/web/src/app/`
- `apps/web/src/features/transposition/`
- `apps/web/src/services/`
- `apps/web/src/components/`

Criar: UploadDropzone, InstrumentSelector, TransposeSummary e estados básicos.

Alterar: contratos frontend se backend mudar.

Não alterar: funcionalidades futuras como login, planos ou painel administrativo.

Testes obrigatórios: upload, seleção de origem, seleção de destino e erro amigável.

Critério de conclusão: usuário cria job pelo frontend.

Riscos: validação visual divergir da validação real do backend.

Checklist final:

- [ ] Upload funciona.
- [ ] Instrumentos vêm da API.
- [ ] Fluxo funciona com teclado.

## Fase 10 — Tela de processamento e resultado

Objetivo: mostrar progresso, resultado e erro de forma clara e acessível.

Arquivos envolvidos:

- `ProcessingStatus`
- `ResultDownloadCard`
- `ErrorState`
- `LocalHistory`

Criar: polling de status, `aria-live`, tela de sucesso e falha.

Alterar: mensagens públicas se necessário.

Não alterar: animações que prejudiquem clareza.

Testes obrigatórios: completed, failed, expired e uso em mobile.

Critério de conclusão: usuário entende o estado atual e próximos passos.

Riscos: polling infinito ou status sem feedback textual.

Checklist final:

- [ ] Progresso acessível.
- [ ] Erro amigável.
- [ ] Resultado aparece quando job conclui.

## Fase 11 — Download de artefatos

Objetivo: permitir download controlado do resultado.

Arquivos envolvidos:

- `apps/api/src/modules/artifacts/`
- `apps/web/src/services/artifacts`

Criar: `GET /api/artifacts/{artifact_id}/download` e ação visual de download.

Alterar: docs de artefatos se tipo de saída mudar.

Não alterar: exposição direta de arquivo por path interno.

Testes obrigatórios: download válido, artefato expirado, artefato inexistente.

Critério de conclusão: resultado final pode ser baixado com segurança.

Riscos: URL permanente ou acesso sem validação.

Checklist final:

- [ ] Download funciona para artefato válido.
- [ ] Expirado é bloqueado.
- [ ] Path interno não aparece.

## Fase 12 — Testes automatizados

Objetivo: consolidar suíte mínima para MVP.

Arquivos envolvidos:

- `apps/api/src/tests/`
- `apps/web/src/tests/`
- `packages/shared/src/**/tests/`
- `docs/qa/`

Criar: testes musicais, backend, frontend e segurança.

Alterar: matriz de testes quando novos riscos surgirem.

Não alterar: escopo do produto para fazer teste passar.

Testes obrigatórios: todos os casos documentados em `docs/qa/01-estrategia-testes.md`.

Critério de conclusão: suíte mínima passa.

Riscos: falsa segurança sem fixtures musicais reais.

Checklist final:

- [ ] Testes musicais passam.
- [ ] Backend passa.
- [ ] Frontend passa.
- [ ] Segurança básica passa.

## Fase 13 — Segurança e revisão técnica

Objetivo: revisar upload, erros, tokens, logs, CORS futuro, rate limit e timeout.

Arquivos envolvidos:

- `docs/security/`
- `docs/backend/08-seguranca-backend.md`
- módulos de upload, jobs e artifacts.

Criar: checklist final de segurança executado.

Alterar: docs quando uma validação for endurecida.

Não alterar: segredos no frontend ou logs verbosos.

Testes obrigatórios: stacktrace não exposto, MIME inválido rejeitado, payload malformado rejeitado.

Critério de conclusão: riscos críticos do MVP mitigados.

Riscos: vazamento de arquivo ou erro técnico para usuário.

Checklist final:

- [ ] Erros públicos seguros.
- [ ] Rate limit documentado.
- [ ] Timeout documentado.
- [ ] Logs com `correlation_id`.

## Fase 14 — Critérios finais do MVP

Objetivo: validar que a aplicação está pronta para ser considerada MVP técnico.

Arquivos envolvidos:

- `docs/100-implementacao/criterios-aceite-mvp.md`
- `docs/logs/CHANGELOG.md`
- `docs/logs/TEST_LOG.md`

Criar: registro final de aceite.

Alterar: pendências objetivas, sem mascarar risco.

Não alterar: escopo aprovado sem decisão explícita.

Testes obrigatórios: checklist completo do MVP.

Critério de conclusão: todos os critérios objetivos atendidos ou pendência formalmente bloqueante.

Riscos: chamar de pronto sem teste musical ou sem pipeline assíncrono.

Checklist final:

- [ ] Critérios de aceite completos.
- [ ] Documentação atualizada.
- [ ] Testes registrados.
- [ ] Próxima fase só começa após aprovação.
