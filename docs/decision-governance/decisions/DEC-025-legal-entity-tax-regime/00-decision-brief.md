# DEC-025 — Natureza jurídica, CNAEs e regime tributário

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-025`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual enquadramento jurídico e tributário corresponde aos serviços e ao SaaS reais?

## Por que esta decisão existe

A IA não pode inferir CNAE, regime, código de serviço ou tributação a partir da ideia do produto.

## Prazo e gate

- trilha: `F`;
- fase: `F0`;
- gate: `exit`;
- owner: `business_owner`.

## Bloqueios atuais

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`

## Opções conhecidas

- definidas somente com contador após abertura

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-026`](../../evidence-register.yaml) — Memorando contábil e jurídico da empresa (`PLANNED`); devido antes de `F0`.

## Critérios de aprovação pré-definidos

- [ ] CNPJ e município confirmados
- [ ] memorando contábil registrado
- [ ] matriz de serviços
- [ ] regime e inscrições aprovados
- [ ] impacto em preço/fiscal documentado

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `accountant`
- `legal_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Aguardar abertura planejada e consulta contábil.

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
