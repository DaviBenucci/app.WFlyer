# DEC-028 — Emissor de NFS-e, autenticação e certificado

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-030`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual emissor e autenticação são aplicáveis ao município, regime e serviços da empresa?

## Por que esta decisão existe

NFS-e não deve ser tratada genericamente como NF-e/SEFAZ estadual; regras dependem do contexto real.

## Prazo e gate

- trilha: `F`;
- fase: `F1`;
- gate: `exit`;
- owner: `fiscal_lead`.

## Bloqueios atuais

- `BLOCKED_BY_COMPANY_FORMATION`
- `BLOCKED_BY_ACCOUNTING_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_SANDBOX`

## Opções conhecidas

- NFS-e padrão nacional quando aplicável
- emissor municipal
- provedor fiscal terceiro
- operação manual temporária aprovada

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-029`](../../evidence-register.yaml) — Homologação de NFS-e e contingência (`PLANNED`); devido antes de `F1/F2`.
- [`EVID-026`](../../evidence-register.yaml) — Memorando contábil e jurídico da empresa (`PLANNED`); devido antes de `F0`.

## Critérios de aprovação pré-definidos

- [ ] município/regime/código de serviço confirmados
- [ ] homologação de emissão/consulta/cancelamento
- [ ] certificado e segredo protegidos
- [ ] contingência e reconciliação
- [ ] aprovação formal do contador

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `accountant`
- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Aguardar DEC-025 e ambiente de homologação.

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
