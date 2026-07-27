# DEC-003 — Limites operacionais por formato e operação

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-003`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais limites de tamanho, complexidade, tempo, memória e concorrência serão aceitos por operação?

## Por que esta decisão existe

Limites ausentes permitem exaustão de CPU, memória, banco, fila e storage.

## Prazo e gate

- trilha: `CORE`;
- fase: `CORE-4`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Opções conhecidas

- limites conservadores por configuração
- limites por plano após custos
- limites adaptativos somente após observabilidade

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-004`](../../evidence-register.yaml) — Benchmark de limites e capacidade (`PLANNED`); devido antes de `CORE-4/CORE-8`.

## Critérios de aprovação pré-definidos

- [ ] benchmark com cenários inicial, provável e pico
- [ ] limites definidos antes de produção
- [ ] rejeição segura e mensagem pública específica
- [ ] timeouts e quotas testados
- [ ] custo p95 conhecido para operações comerciais

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`
- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Medir o corte vertical Core antes de preencher limites definitivos.

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
