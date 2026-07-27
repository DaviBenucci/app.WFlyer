# DEC-036 — Adoção de Rive para microilustrações

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Rive agrega interação autoral sem sobrepor Motion/GSAP nem prejudicar desempenho e acessibilidade?

## Por que esta decisão existe

Adicionar uma terceira engine visual pode aumentar bundle, manutenção e inconsistência.

## Prazo e gate

- trilha: `TOOL`;
- fase: `FUTURE-RIVE`;
- gate: `entry`;
- owner: `design_owner`.

## Bloqueios atuais

- `BLOCKED_BY_USER_APPROVAL`
- `BLOCKED_BY_BENCHMARK`

## Opções conhecidas

- não usar Rive
- usar apenas microilustrações aprovadas

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-037`](../../evidence-register.yaml) — Protótipo Rive e orçamento de performance (`PLANNED`); devido antes de `FUTURE-UI`.

## Critérios de aprovação pré-definidos

- [ ] protótipo isolado
- [ ] bundle/performance/reduced motion medidos
- [ ] responsabilidade sem sobreposição
- [ ] asset autoral e acessível

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `frontend_lead`
- `accessibility_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Não instalar preventivamente.

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
