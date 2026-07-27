# DEC-014 — Baseline e aprovação dos golden examples

> Status: `RESEARCHING`. ID(s) legado(s): `PEND-014`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais composições, tokens, estados e viewports serão vinculantes para a implementação do frontend?

## Por que esta decisão existe

Sem aprovação, screenshots candidatos podem induzir a IA a implementar capabilities futuras ou identidade provisória como final.

## Prazo e gate

- trilha: `FE0`;
- fase: `FE0`;
- gate: `exit`;
- owner: `design_owner`.

## Bloqueios atuais

- `BLOCKED_BY_USER_APPROVAL`
- `BLOCKED_BY_BRAND_DECISION`

## Opções conhecidas

- aprovar composição atual com ajustes
- substituir baselines após identidade
- aprovar somente estados do Core

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-015`](../../evidence-register.yaml) — Aprovação humana dos golden examples (`PLANNED`); devido antes de `F0/CORE-7`.

## Critérios de aprovação pré-definidos

- [ ] Core e futuro claramente separados
- [ ] desktop/mobile/zoom/reduced motion revisados
- [ ] componentes e estados extremos cobertos
- [ ] brand manifest respeitado
- [ ] aprovação humana registrada por reference_id

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `frontend_lead`
- `accessibility_reviewer`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Revisar golden examples após o protótipo visual e a identidade.

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
