# DEC-033 — Aprovação das políticas públicas

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-035`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais versões de termos, privacidade, cookies, billing, conteúdo, retenção, suporte e segurança podem ser publicadas?

## Por que esta decisão existe

Textos jurídicos precisam refletir controles reais, dados da empresa e fornecedores efetivamente usados.

## Prazo e gate

- trilha: `LAUNCH`;
- fase: `LAUNCH`;
- gate: `entry`;
- owner: `legal_reviewer`.

## Bloqueios atuais

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- publicar somente documentos aprovados
- manter rascunhos fora da rota

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-034`](../../evidence-register.yaml) — Revisão jurídica e inventário de controles das políticas (`PLANNED`); devido antes de `LAUNCH`.

## Critérios de aprovação pré-definidos

- [ ] dados empresariais confirmados
- [ ] inventário de dados/cookies/fornecedores
- [ ] revisão jurídica registrada
- [ ] versionamento e aceite
- [ ] controles técnicos implementados
- [ ] policy-manifest aprovado

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `privacy_reviewer`
- `security_lead`
- `accountant`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Manter /politicas desabilitada para rascunhos finais.

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
