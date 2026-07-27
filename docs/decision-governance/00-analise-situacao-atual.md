# Análise da situação atual do projeto

> Revisão: 2026-07-27. Escopo: documentação e governança; nenhum código funcional foi implementado.

## Estado confirmado

- Fase 0: tecnicamente concluída e arquivada;
- Fase 1: não iniciada;
- frontend, API, worker, banco, migrations e motor musical: inexistentes;
- marca: pendente, com uso temporário apenas de `W_Flyer` em texto;
- empresa: ainda não formalizada;
- billing, fiscal e produção: planejados, não habilitados;
- site institucional e planejamento empresarial privado: fora deste repositório.

## Problema encontrado antes desta atualização

As decisões existiam em texto livre, mas nem todas tinham ID canônico, owner, aprovadores, evidência, prazo de fase ou estado verificável. Isso permitia que um agente confundisse “opção estudada” com “opção aprovada”, instalasse ferramenta opcional cedo demais ou avançasse para uma fase sem prova.

Também era necessário impedir dois falsos positivos:

1. evidência `REJECTED` ou `STALE` não pode satisfazer um gate;
2. decisão `SUPERSEDED` não pode satisfazer um gate ativo apenas por aparecer no fim do lifecycle.

## Resultado desta consolidação

- **47 decisões controladas** em `decision-register.yaml`;
- **48 bundles de evidência** em `evidence-register.yaml`;
- **48 fases/trilhas com gates de entrada e saída** em `phase-decision-gates.yaml`;
- pacote completo para cada `DEC-*`;
- gates opcionais separados do Core, evitando bloquear o MVP por Rive, Pact, Temporal, mutation testing ou cache remoto;
- decisões próprias para backup/DR, observabilidade e contas/organizações;
- rastreabilidade dos IDs legados e reserva de `PEND-026`/`PEND-027`;
- validação automática e consulta de gate.

## O que permanece deliberadamente aberto

Engines, thresholds, custos, preços, provedores, topologia final, política fiscal, identidade e lançamento continuam pendentes até suas evidências e aprovações. Esta documentação define **como decidir**, não finge que a decisão já existe.
