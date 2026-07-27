# DEC-045 — Backup, restore e recuperação de desastre

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual estratégia de backup, restauração e recuperação regional consegue atender aos RPO/RTO aprovados sem criar falsa sensação de segurança?

## Por que esta decisão existe

Backup sem restauração exercitada não comprova recuperabilidade; banco, objetos, manifests, secrets e infraestrutura possuem ordens de recuperação diferentes.

## Prazo e gate

- trilha: `INF`;
- fase: `INF3`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_COST_DATA`

## Opções conhecidas

- PITR + backups versionados + cópia cross-region + IaC e runbooks
- estratégia alternativa somente após teste comparável

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-046`](../../evidence-register.yaml) — Exercícios de backup, restore e disaster recovery (`PLANNED`); devido antes de `INF3`.

## Critérios de aprovação pré-definidos

- [ ] inventário de dados e dependências aprovado
- [ ] restore real de PostgreSQL executado e cronometrado
- [ ] restore de objetos, hashes e manifests executado e validado
- [ ] procedimento regional reproduzível por IaC e runbook
- [ ] RPO/RTO observados comparados às metas DEC-031
- [ ] custos, retenção, criptografia e owner aprovados

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar somente após staging e topologia de produção estarem disponíveis; até lá, manter plano e runbook como requisitos.

## Sequência obrigatória

```text
requisitos congelados
→ plano de experimento
→ evidência bruta
→ comparação
→ risco/rollback
→ aprovação humana
→ ADR/MDR/FDR
→ OpenSpec de implementação
→ implementação
→ validação pós-implementação
```
