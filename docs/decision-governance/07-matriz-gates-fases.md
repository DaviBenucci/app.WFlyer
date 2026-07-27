# Matriz humana de gates por fase

> GERADO. Não editar manualmente.

## CORE-1 — Fundação executável

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-039` ≥ `DECIDED`

**Evidências:**
- `EVID-040` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-2 — Catálogo e modelo musical

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-015` ≥ `VALIDATED`

**Evidências:**
- `EVID-016` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-3 — Motor MusicXML

### entry

**Decisões:**
- `DEC-013` ≥ `DECIDED`
- `DEC-015` ≥ `DECIDED`

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-013` ≥ `VALIDATED`

**Evidências:**
- `EVID-014` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-4 — Upload, storage e fila

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-003` ≥ `DECIDED`

**Evidências:**
- `EVID-004` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-5 — Corte vertical funcional

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-6 — Segurança e retenção do Core

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-7 — UX, acessibilidade e histórico

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-014` ≥ `DECIDED`

**Evidências:**
- `EVID-015` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## CORE-8 — Qualidade e operação

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A qualidade do Core é comprovada pelos testes obrigatórios; mutation testing e Pact permanecem decisões opcionais separadas e não bloqueiam o MVP por ausência de adoção.

## CORE-9 — Aceite do Core

### entry

**Decisões:**
- `DEC-003` ≥ `DECIDED`
- `DEC-013` ≥ `VALIDATED`
- `DEC-014` ≥ `DECIDED`
- `DEC-015` ≥ `VALIDATED`

**Evidências:**
- `EVID-004` ≥ `ACCEPTED`
- `EVID-014` ≥ `ACCEPTED`
- `EVID-015` ≥ `ACCEPTED`
- `EVID-016` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## R0 — Spike do renderer

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-002` ≥ `DECIDED`

**Evidências:**
- `EVID-003` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## R1 — Adapter e sandbox do renderer

### entry

**Decisões:**
- `DEC-002` ≥ `DECIDED`

**Evidências:**
- `EVID-003` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-020` ≥ `DECIDED`

**Evidências:**
- `EVID-021` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## R2 — Habilitação PDF de saída

### entry

**Decisões:**
- `DEC-002` ≥ `VALIDATED`
- `DEC-020` ≥ `VALIDATED`

**Evidências:**
- `EVID-003` ≥ `ACCEPTED`
- `EVID-021` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## P0 — Spike de OMR

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-001` ≥ `DECIDED`

**Evidências:**
- `EVID-001` ≥ `ACCEPTED`
- `EVID-002` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## P1 — Rasterização, adapter e sandbox

### entry

**Decisões:**
- `DEC-001` ≥ `DECIDED`

**Evidências:**
- `EVID-002` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## P2 — Corpus e métricas de OMR

### entry

**Decisões:**
- `DEC-001` ≥ `DECIDED`

**Evidências:**
- `EVID-001` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-004` ≥ `DECIDED`

**Evidências:**
- `EVID-005` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## P3 — UX de incerteza OMR

### entry

**Decisões:**
- `DEC-004` ≥ `DECIDED`

**Evidências:**
- `EVID-005` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## P4 — Habilitação controlada OMR

### entry

**Decisões:**
- `DEC-001` ≥ `VALIDATED`
- `DEC-003` ≥ `DECIDED`
- `DEC-004` ≥ `VALIDATED`

**Evidências:**
- `EVID-001` ≥ `ACCEPTED`
- `EVID-002` ≥ `ACCEPTED`
- `EVID-004` ≥ `ACCEPTED`
- `EVID-005` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## M0 — Modelo canônico avançado

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-006` ≥ `DECIDED`
- `DEC-013` ≥ `DECIDED`

**Evidências:**
- `EVID-007` ≥ `ACCEPTED`
- `EVID-014` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## L0 — Corpus rotulado de melodia

### entry

**Decisões:**
- `DEC-010` ≥ `DECIDED`
- `DEC-024` ≥ `DECIDED`

**Evidências:**
- `EVID-011` ≥ `ACCEPTED`
- `EVID-025` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- `EVID-008` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## L1 — Baselines de melodia

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- `EVID-008` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-007` ≥ `DECIDED`

**Evidências:**
- `EVID-008` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## H0 — Perfis e teoria de harmonização

### entry

**Decisões:**
- `DEC-024` ≥ `DECIDED`

**Evidências:**
- `EVID-025` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-008` ≥ `DECIDED`

**Evidências:**
- `EVID-009` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## H1 — Motor explicável de harmonização

### entry

**Decisões:**
- `DEC-008` ≥ `DECIDED`
- `DEC-015` ≥ `VALIDATED`

**Evidências:**
- `EVID-009` ≥ `ACCEPTED`
- `EVID-016` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-009` ≥ `DECIDED`

**Evidências:**
- `EVID-010` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## W1 — Marca distribuída

### entry

**Decisões:**
- `DEC-002` ≥ `DECIDED`

**Evidências:**
- `EVID-003` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-012` ≥ `DECIDED`

**Evidências:**
- `EVID-013` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## W2 — Manifesto e assinatura

### entry

**Decisões:**
- `DEC-012` ≥ `DECIDED`

**Evidências:**
- `EVID-013` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-011` ≥ `DECIDED`

**Evidências:**
- `EVID-012` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## FE0 — Referências visuais e frontend

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-014` ≥ `DECIDED`

**Evidências:**
- `EVID-015` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## D0 — Musical Diff verificável

### entry

**Decisões:**
- `DEC-013` ≥ `DECIDED`

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-018` ≥ `DECIDED`

**Evidências:**
- `EVID-019` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

## A0 — Áudio e score following

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-016` ≥ `DECIDED`
- `DEC-017` ≥ `DECIDED`

**Evidências:**
- `EVID-017` ≥ `ACCEPTED`
- `EVID-018` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

## T0 — Tocabilidade e adaptação idiomática

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-019` ≥ `DECIDED`

**Evidências:**
- `EVID-016` ≥ `ACCEPTED`
- `EVID-020` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## E0 — Pacote ensemble

### entry

**Decisões:**
- `DEC-006` ≥ `VALIDATED`
- `DEC-015` ≥ `VALIDATED`

**Evidências:**
- `EVID-007` ≥ `ACCEPTED`
- `EVID-016` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-021` ≥ `DECIDED`

**Evidências:**
- `EVID-022` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

## C0 — Colaboração

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-022` ≥ `DECIDED`

**Evidências:**
- `EVID-023` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

## Q0 — Conselho musical e governança do corpus

### entry

**Decisões:**
- `DEC-010` ≥ `DECIDED`

**Evidências:**
- `EVID-011` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-024` ≥ `DECIDED`

**Evidências:**
- `EVID-025` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

## B0 — Domínio de planos e créditos

### entry

**Decisões:**
- `DEC-047` ≥ `DECIDED`

**Evidências:**
- `EVID-048` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- `DEC-027` ≥ `DECIDED`
- `DEC-032` ≥ `DECIDED`

**Evidências:**
- `EVID-028` ≥ `ACCEPTED`
- `EVID-033` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## B1 — Spike Stripe/Mercado Pago

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- `EVID-027` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## B2 — Provedor escolhido

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- `EVID-027` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-026` ≥ `DECIDED`

**Evidências:**
- `EVID-027` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## F0 — Definição contábil

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-025` ≥ `DECIDED`

**Evidências:**
- `EVID-026` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## F1 — Homologação NFS-e

### entry

**Decisões:**
- `DEC-025` ≥ `DECIDED`

**Evidências:**
- `EVID-026` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-028` ≥ `DECIDED`

**Evidências:**
- `EVID-029` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## INF0 — Domínio e ambientes

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-029` ≥ `DECIDED`
- `DEC-041` ≥ `DECIDED`

**Evidências:**
- `EVID-030` ≥ `ACCEPTED`
- `EVID-042` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## INF2 — Produção AWS e serviços gerenciados

### entry

**Decisões:**
- `DEC-041` ≥ `DECIDED`

**Evidências:**
- `EVID-042` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-030` ≥ `DECIDED`
- `DEC-042` ≥ `DECIDED`
- `DEC-046` ≥ `DECIDED`

**Evidências:**
- `EVID-031` ≥ `ACCEPTED`
- `EVID-043` ≥ `ACCEPTED`
- `EVID-047` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## INF3 — Disaster recovery

### entry

**Decisões:**
- `DEC-041` ≥ `DECIDED`
- `DEC-042` ≥ `DECIDED`

**Evidências:**
- `EVID-042` ≥ `ACCEPTED`
- `EVID-043` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-031` ≥ `DECIDED`
- `DEC-045` ≥ `DECIDED`

**Evidências:**
- `EVID-032` ≥ `ACCEPTED`
- `EVID-046` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## BRAND-0 — Identidade visual oficial

### entry

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-034` ≥ `DECIDED`

**Evidências:**
- `EVID-035` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.

## AI-PROVIDER — Uso de fornecedor/modelo externo de IA

### entry

**Decisões:**
- `DEC-023` ≥ `DECIDED`

**Evidências:**
- `EVID-024` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Cada fornecedor/capability exige OpenSpec, DPA/termos, controles e kill switch aprovados.

## FUTURE-MXL — Suporte opcional a MXL

### entry

**Decisões:**
- `DEC-005` ≥ `DECIDED`

**Evidências:**
- `EVID-006` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

MXL só pode ser habilitado após implementação segura e regressão do corpus hostil.

## FUTURE-TEMPORAL — Spike opcional de Temporal

### entry

**Decisões:**
- `DEC-035` ≥ `DECIDED`

**Evidências:**
- `EVID-036` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A adoção só termina após OpenSpec, implementação, migração e validação; Celery e Temporal não orquestram o mesmo pipeline simultaneamente.

## FUTURE-RIVE — Adoção opcional de Rive

### entry

**Decisões:**
- `DEC-036` ≥ `DECIDED`

**Evidências:**
- `EVID-037` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Rive permanece limitado às microilustrações aprovadas e não substitui a partitura, Motion ou GSAP.

## FUTURE-PACT — Adoção opcional de Pact

### entry

**Decisões:**
- `DEC-037` ≥ `DECIDED`

**Evidências:**
- `EVID-038` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Pact só entra quando lacuna real de contratos consumidor/provedor for comprovada.

## FUTURE-MUTATION — Adoção opcional de mutation testing

### entry

**Decisões:**
- `DEC-038` ≥ `DECIDED`

**Evidências:**
- `EVID-039` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

A cadência e o escopo aprovados devem evitar custo desproporcional e manter foco em módulos críticos.

## FUTURE-NX-CACHE — Adoção opcional de cache remoto Nx

### entry

**Decisões:**
- `DEC-040` ≥ `DECIDED`

**Evidências:**
- `EVID-041` ≥ `ACCEPTED`

Se qualquer requisito falhar, somente pesquisa ou experimento autorizado pode continuar; implementação da capability permanece bloqueada.

### exit

**Decisões:**
- nenhuma adicional

**Evidências:**
- nenhuma adicional

Outputs sensíveis e segredos nunca podem entrar no cache; fallback local continua disponível.

## LAUNCH — Lançamento comercial

### entry

**Decisões:**
- `DEC-025` ≥ `DECIDED`
- `DEC-026` ≥ `DECIDED`
- `DEC-027` ≥ `DECIDED`
- `DEC-028` ≥ `DECIDED`
- `DEC-031` ≥ `DECIDED`
- `DEC-032` ≥ `DECIDED`
- `DEC-033` ≥ `DECIDED`
- `DEC-043` ≥ `VALIDATED`
- `DEC-045` ≥ `VALIDATED`
- `DEC-046` ≥ `VALIDATED`
- `DEC-047` ≥ `VALIDATED`

**Evidências:**
- `EVID-026` ≥ `ACCEPTED`
- `EVID-027` ≥ `ACCEPTED`
- `EVID-028` ≥ `ACCEPTED`
- `EVID-029` ≥ `ACCEPTED`
- `EVID-032` ≥ `ACCEPTED`
- `EVID-033` ≥ `ACCEPTED`
- `EVID-034` ≥ `ACCEPTED`
- `EVID-044` ≥ `ACCEPTED`
- `EVID-046` ≥ `ACCEPTED`
- `EVID-047` ≥ `ACCEPTED`
- `EVID-048` ≥ `ACCEPTED`

Se qualquer requisito falhar, a fase pode apenas pesquisar/planejar o bloqueio; implementação da capability fica proibida.

### exit

**Decisões:**
- `DEC-044` ≥ `DECIDED`

**Evidências:**
- `EVID-045` ≥ `ACCEPTED`

A fase não recebe CONCLUÍDA sem decisões e evidências no estado mínimo, além dos demais gates técnicos.
