# DEC-047 — Modelo de conta, autenticação e organizações

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Como sessões anônimas, contas permanentes, organizações, convites, recuperação e ownership de recursos funcionarão antes da monetização?

## Por que esta decisão existe

Pagamento, histórico em nuvem e colaboração não podem depender apenas de um cookie anônimo nem permitir migração ambígua de partituras e créditos.

## Prazo e gate

- trilha: `B`;
- fase: `B0`;
- gate: `entry`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_PRODUCT_SCOPE`
- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- Core anônimo + conversão posterior para conta
- magic link e/ou senha após revisão de segurança
- organizações e SSO em rollout posterior

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-048`](../../evidence-register.yaml) — Threat model e teste do modelo de conta e organizações (`PLANNED`); devido antes de `B0`.

## Critérios de aprovação pré-definidos

- [ ] migração explícita e idempotente de sessão anônima para conta
- [ ] verificação e recuperação de e-mail seguras
- [ ] ownership, revogação, RBAC e organizações documentados
- [ ] rate limiting, auditoria e threat model aprovados
- [ ] retenção, exclusão e minimização de dados definidas
- [ ] billing nunca vinculado somente a sessão anônima

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `security_lead`
- `privacy_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Manter o Core anônimo; criar spike e OpenSpec de contas apenas antes da trilha comercial B0.

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
