# DEC-022 — Colaboração, identidade e retenção

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-022`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual identidade, convite, revogação, concorrência, moderação e retenção suportam revisão colaborativa?

## Por que esta decisão existe

Comentários e decisões musicais exigem autorização por recurso, versão e trilha auditável.

## Prazo e gate

- trilha: `C`;
- fase: `C0`;
- gate: `exit`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Opções conhecidas

- revisão por convite
- organizações
- colaboração adiada

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-023`](../../evidence-register.yaml) — Threat model e teste de colaboração (`PLANNED`); devido antes de `C0`.

## Critérios de aprovação pré-definidos

- [ ] threat model e IDOR testados
- [ ] ETag/conflitos explícitos
- [ ] revogação imediata
- [ ] retenção e anonimização aprovadas
- [ ] âncoras versionadas

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `security_lead`
- `privacy_reviewer`
- `engineering_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir somente após conta permanente e revisions.

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
