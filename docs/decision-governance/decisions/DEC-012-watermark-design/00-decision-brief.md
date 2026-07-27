# DEC-012 — Intensidade e desenho do watermark

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-012`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual marca visível oferece rastreabilidade sem prejudicar leitura, impressão ou acessibilidade?

## Por que esta decisão existe

Marcas agressivas atrapalham execução; marcas simples são fáceis de remover. Nenhuma é infalível.

## Prazo e gate

- trilha: `W`;
- fase: `W1`;
- gate: `exit`;
- owner: `design_owner`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_USER_APPROVAL`
- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- marca distribuída discreta
- token em áreas seguras
- sem marca visual em perfis específicos após decisão

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-013`](../../evidence-register.yaml) — Teste visual, impressão e acessibilidade do watermark (`PLANNED`); devido antes de `W1`.

## Critérios de aprovação pré-definidos

- [ ] testes em tela e impressão
- [ ] safe zones derivadas do renderer
- [ ] opacidade e repetição aprovadas
- [ ] sem PII visível
- [ ] marca não cobre notação ou créditos

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `accessibility_reviewer`
- `legal_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Aguardar geometry map do renderer.

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
