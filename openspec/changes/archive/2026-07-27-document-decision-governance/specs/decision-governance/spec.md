# Decision Governance Specification

## Requirement: registro machine-readable

O projeto SHALL manter `decision-register.yaml`, `evidence-register.yaml` e `phase-decision-gates.yaml` válidos, versionados e referencialmente íntegros.

### Scenario: decisão ainda aberta

- **WHEN** uma tarefa depende de decisão abaixo do estado mínimo do gate
- **THEN** o agente bloqueia a implementação e informa decisão, evidência, trabalho permitido e aprovação faltantes.

### Scenario: gate sem requisito adicional

- **WHEN** o registro de uma fase não exige `DEC-*` ou `EVID-*` adicional naquele lado do gate
- **THEN** o agente pode prosseguir apenas quanto à camada de decisão, mantendo obrigatórios os gates técnicos, musicais, de segurança, QA e produto.

## Requirement: evidência reproduzível precede aprovação

Evidência `ACCEPTED` SHALL apontar artefatos, review record, commit, ambiente, data e política de freshness. `REJECTED` ou `STALE` SHALL NOT satisfazer gates.

### Scenario: evidência expirada ou materialmente alterada

- **WHEN** versão, corpus, custo, legislação, arquitetura, fornecedor ou incidente invalida a evidência
- **THEN** a evidência passa a `STALE`, o gate volta a bloquear e a decisão é reaberta quando aplicável.

## Requirement: aprovação humana

A IA SHALL NOT alterar decisão para `DECIDED`, preencher assinatura humana, aceitar evidência em nome dos revisores ou habilitar implementação sem decision record aprovado.

## Requirement: pacotes completos

Cada decisão SHALL possuir brief, requisitos, opções, plano pré-registrado, evidence manifest, comparação, risco, decision record e validação pós-implementação.

## Requirement: separação entre decisão e implementação

Uma decisão `DECIDED` SHALL apontar ADR/MDR/FDR aprovado. A implementação SHALL ocorrer em mudança OpenSpec própria. `IMPLEMENTED` SHALL NOT equivaler a `VALIDATED`.

## Requirement: gates de entrada e saída

Cada registro de fase/trilha SHALL conter gate de entrada e gate de saída. O verificador SHALL falhar fechado para estado insuficiente, ID ausente, evidência rejeitada/stale ou decisão superseded.

## Requirement: ferramentas opcionais não bloqueiam o Core

Temporal, Rive, Pact, mutation testing e cache remoto SHALL usar gates `FUTURE-*` separados e SHALL NOT bloquear o MVP Core enquanto não forem adotados.
