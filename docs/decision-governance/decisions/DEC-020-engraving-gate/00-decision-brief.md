# DEC-020 — Gate de engraving e legibilidade

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-020`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais colisões, viradas, tamanhos e dispositivos bloqueiam a publicação do PDF?

## Por que esta decisão existe

Correção semântica não garante leitura segura durante estudo ou performance.

## Prazo e gate

- trilha: `R`;
- fase: `R1`;
- gate: `exit`;
- owner: `qa_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- detector automático + revisão
- revisão obrigatória por perfil complexo
- bloqueio de PDF em casos não suportados

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-021`](../../evidence-register.yaml) — Gate de legibilidade e engraving (`PLANNED`); devido antes de `R1`.
- [`EVID-003`](../../evidence-register.yaml) — Benchmark de renderer e engraving (`PLANNED`); devido antes de `R0/R1`.

## Critérios de aprovação pré-definidos

- [ ] detector de colisões testado
- [ ] matriz tela/impressão
- [ ] thresholds pré-registrados
- [ ] viradas e densidade aprovadas
- [ ] watermark avaliado em conjunto

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `design_owner`
- `accessibility_reviewer`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir depois do renderer DEC-002.

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
