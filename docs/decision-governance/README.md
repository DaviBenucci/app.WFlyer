# Governança de decisões do W_Flyer

> Status: **canônico e bloqueante**. Revisão: 2026-07-27.

Esta área controla decisões que dependem de benchmark, custo, empresa formalizada, revisão musical, segurança, privacidade, jurídico, contabilidade ou aprovação de produto. Ela não antecipa o resultado; define como obter e aprovar a resposta.

## Estado atual

- 47 decisões `DEC-*`;
- 48 bundles `EVID-*`;
- 48 fases/trilhas com gates de entrada e saída;
- Fase 0 arquivada; Fase 1 não iniciada;
- nenhuma decisão desta área autoriza código por si só.

## Ordem obrigatória

```text
questão → requisitos → plano pré-registrado → evidência → comparação/risco
→ aprovação humana → ADR/MDR/FDR → OpenSpec → implementação → validação
```

## Fontes canônicas

- [`decision-register.yaml`](decision-register.yaml) — estado, owner, aprovadores, opções, blockers e fase;
- [`evidence-register.yaml`](evidence-register.yaml) — artefatos, provenance, review e freshness;
- [`phase-decision-gates.yaml`](phase-decision-gates.yaml) — entrada/saída de cada fase;
- [`05-registro-humano-decisoes.md`](05-registro-humano-decisoes.md) — visão gerada;
- [`06-matriz-decisoes-evidencias.md`](06-matriz-decisoes-evidencias.md) — rastreabilidade gerada;
- [`07-matriz-gates-fases.md`](07-matriz-gates-fases.md) — gates em leitura humana;
- [`decisions/`](decisions/README.md) — pacote completo por decisão;
- [`templates/`](templates/) — modelos obrigatórios.

## Documentos de orientação

- [`00-analise-situacao-atual.md`](00-analise-situacao-atual.md);
- [`01-papeis-aprovacoes.md`](01-papeis-aprovacoes.md);
- [`02-fluxo-decisao.md`](02-fluxo-decisao.md);
- [`03-evidencias-freshness.md`](03-evidencias-freshness.md);
- [`04-gates-fases-e-ia.md`](04-gates-fases-e-ia.md);
- [`08-migracao-ids-legados.md`](08-migracao-ids-legados.md).

## Regras críticas

1. IA não aprova decisão nem evidencia em nome humano;
2. `REJECTED` e `STALE` nunca satisfazem gate `ACCEPTED`;
3. `SUPERSEDED` não satisfaz gate ativo;
4. ferramentas opcionais têm fases `FUTURE-*` e não bloqueiam o Core;
5. valores quantitativos ficam `PENDENTE` até pré-registro e medição;
6. evidência negativa é preservada;
7. decisão `DECIDED` ainda precisa de OpenSpec para virar implementação;
8. `IMPLEMENTED` ainda precisa de validação para produção.

## Comandos

```bash
pnpm run generate:decision-docs
python3 scripts/check-decision-gate.py CORE-1 --gate entry
python3 scripts/check-decision-gate.py CORE-1 --gate exit
pnpm run verify:repository
```
