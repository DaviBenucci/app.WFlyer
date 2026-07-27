# DEC-034 — Identidade visual oficial

> Status: `RESEARCHING`. ID(s) legado(s): `PEND-036`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual símbolo, wordmark, tipografia, paleta e sistema modular representarão empresa e produto musical?

## Por que esta decisão existe

A marca precisa servir ao site institucional e ao app sem parecer exclusivamente musical ou genérica de IA.

## Prazo e gate

- trilha: `BRAND`;
- fase: `BRAND-0`;
- gate: `exit`;
- owner: `design_owner`.

## Bloqueios atuais

- `BLOCKED_BY_USER_APPROVAL`
- `BLOCKED_BY_BRAND_DECISION`

## Opções conhecidas

- direções conceituais a desenvolver em projeto separado

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-035`](../../evidence-register.yaml) — Pacote de aprovação da identidade visual (`PLANNED`); devido antes de `BRAND-0`.

## Critérios de aprovação pré-definidos

- [ ] briefing e três direções comparadas
- [ ] legibilidade e uso monocromático
- [ ] SVG modular com IDs estáveis
- [ ] favicon e lockups
- [ ] similaridade/disponibilidade verificadas
- [ ] aprovação humana e autoria/licença registradas

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Desenvolver em chat/projeto de identidade e atualizar brand-manifest somente após aprovação.

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
