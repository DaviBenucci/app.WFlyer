# DEC-040 — Cache remoto Nx e política de segurança

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

O projeto precisa de cache remoto e quais artefatos podem sair do ambiente?

## Por que esta decisão existe

Cache remoto economiza CI, mas pode expor outputs, logs ou dados sensíveis.

## Prazo e gate

- trilha: `TOOL`;
- fase: `FUTURE-NX-CACHE`;
- gate: `entry`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_COST_DATA`
- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- cache local somente
- Nx Cloud
- backend remoto aprovado

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-041`](../../evidence-register.yaml) — Análise de cache remoto Nx (`PLANNED`); devido antes de `CORE-8`.

## Critérios de aprovação pré-definidos

- [ ] classificação de outputs
- [ ] segredos excluídos
- [ ] custos/ganho medidos
- [ ] controle de acesso e retenção
- [ ] fallback local

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `security_lead`
- `finance_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Não habilitar antes de CI real.

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
