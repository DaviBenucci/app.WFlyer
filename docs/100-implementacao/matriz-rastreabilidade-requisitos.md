# Matriz de rastreabilidade de requisitos

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Vincular requisito, risco, contrato, teste e evidência. A implementação deve manter uma versão executável desta matriz no repositório.

## Convenção de IDs

```text
REQ-MUS-*  regra musical
REQ-API-*  contrato
REQ-UX-*   interface
REQ-SEC-*  segurança/privacidade
REQ-QA-*   qualidade
REQ-OPS-*  operação
```

## Baseline

| Requisito | Documento | Risco | Teste mínimo | Gate |
|---|---|---|---|---|
| REQ-MUS-001 preservar pitch de concerto | `../music/01-modelo-transposicao.md` | RISK-MUS-001 | property A→B e checker independente | Core |
| REQ-MUS-002 não publicar ambiguidade | `../backend/19-confiabilidade-musical-fail-closed.md` | RISK-BE-004 | review/reject fixtures | Core/L/H |
| REQ-MUS-003 proveniência por evento | `../features/14-musical-diff-proveniencia.md` | RISK-MUS-005 | completeness test | D/H/A |
| REQ-MUS-004 melodia por região | `../music/07-extracao-melodia-polifonica.md` | RISK-MUS-003 | benchmark adversarial | L |
| REQ-MUS-005 tocabilidade por perfil | `../music/13-verificador-tocabilidade.md` | RISK-MUS-006 | instrument fixtures | A |
| REQ-MUS-006 score/partes consistentes | `../music/15-consistencia-score-partes.md` | RISK-MUS-009 | properties | E |
| REQ-UX-001 referência visual interna | `../frontend/18-pacote-referencias-visuais.md` | RISK-UX-004 | visual/state coverage | F0 |
| REQ-UX-002 operações não confundidas | `../features/12-modos-operacao-musical.md` | RISK-UX-001 | E2E/microcopy | todas |
| REQ-SEC-001 metadado não é instrução | `../security/08-metadados-nao-confiaveis-prompt-injection.md` | RISK-SEC-003 | adversarial model fixture | H |
| REQ-SEC-002 preservar créditos | `../security/07-direitos-autorais-atribuicao-licencas.md` | RISK-LGL-001 | metadata diff | todas |
| REQ-QA-001 falha nova gera regressão | `../qa/19-matriz-falhas-pre-mortem.md` | todos | incident fixture | todas |

## Regra de manutenção

PR que altera requisito deve atualizar IDs, testes e evidência. Requisito sem teste deve declarar por que é manual e quem aprova.

## Requisitos avançados adicionados

| Requisito | Documento | Risco principal | Teste/gate |
|---|---|---|---|
| REQ-MUS-007 Musical Diff por evento | `../features/14-musical-diff-proveniencia.md` | RISK-MUS-005 | completeness + semantic diff |
| REQ-MUS-008 análise por região, não hipótese global forçada | `../music/11-analise-forma-fraseado-cadencias.md` | RISK-MUS-007 | corpus com modulação/modal/ambíguo |
| REQ-MUS-009 curva de tensão não é emoção automática | `../music/12-curva-tensao-harmonica.md` | RISK-MUS-008 | UX + review musical |
| REQ-MUS-010 adaptação usa budget explícito | `../music/10-adaptacao-idiomatica-instrumental.md` | RISK-MUS-006 | property/diff + aprovação |
| REQ-MUS-011 tocabilidade depende de tempo/perfil | `../music/13-verificador-tocabilidade.md` | RISK-MUS-006 | instrumentista + fixtures |
| REQ-MUS-012 áudio segue playback graph | `../music/16-mapa-reproducao-audio.md` | RISK-MUS-010 | occurrence/timestamp corpus |
| REQ-MUS-013 score/partes compartilham grafo | `../music/15-consistencia-score-partes.md` | RISK-MUS-009 | consistency properties |
| REQ-UX-003 estados negativos são especificados | `../frontend/20-matriz-estados-interface.md` | RISK-UX-002 | Storybook/E2E/a11y |
| REQ-UX-004 IA segue manifest interno | `../frontend/19-contrato-fidelidade-visual-ia.md` | RISK-UX-004 | visual diff + human review |
| REQ-OPS-001 preflight antecede código | `../implementacao/09-protocolo-preflight-capacidade.md` | todos | review do preflight |
| REQ-OPS-002 feature flag default off | `../backend/25-feature-flags-rollout-musical.md` | RISK-BE-003 | rollout/rollback test |
| REQ-OPS-003 falha desconhecida fecha publicação | `../riscos/02-falhas-desconhecidas-incidentes.md` | todos | fault injection/unknown exception |
| REQ-QA-002 155 PM rastreáveis | `../riscos/failure-mode-catalog.yaml` | todos | schema + IDs + evidence |
| REQ-SEC-003 conteúdo não vira prompt | `../security/08-metadados-nao-confiaveis-prompt-injection.md` | RISK-SEC-003 | adversarial fixtures |
| REQ-LGL-001 créditos e licença preservados | `../security/07-direitos-autorais-atribuicao-licencas.md` | RISK-LGL-001 | metadata/license gate |

## Colunas da versão executável

A matriz no repositório deve possuir, no mínimo:

```text
requirement_id
capability_id
source_documents
mdr_ids
api_schema_refs
migration_refs
backend_modules
frontend_reference_ids
public_error_codes
failure_mode_ids
test_ids
metrics
runbook
feature_flag
evidence_links
owner
status
residual_risk
```

O template está em `traceability.template.yaml`.
