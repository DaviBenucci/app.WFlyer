# DEC-004 — Gate quantitativo para PDF/OMR

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-004`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais métricas e limiares permitem ativar PDF/OMR para cada estrato suportado?

## Por que esta decisão existe

Uma média global pode esconder falhas graves em claves, texturas ou qualidades de imagem específicas.

## Prazo e gate

- trilha: `P`;
- fase: `P2`;
- gate: `exit`;
- owner: `qa_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- gate por estrato de corpus
- habilitação restrita por formato/complexidade
- manter capability desligada

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-005`](../../evidence-register.yaml) — Relatório quantitativo de habilitação PDF (`PLANNED`); devido antes de `P2`.
- [`EVID-001`](../../evidence-register.yaml) — Corpus e benchmark OMR (`PLANNED`); devido antes de `P0/P2`.

## Critérios de aprovação pré-definidos

- [ ] thresholds registrados antes de observar o benchmark final
- [ ] resultados estratificados por formato e complexidade
- [ ] verified_false_positive_rate alvo preenchido e aprovado
- [ ] taxa de revisão e rejeição explicitamente aceita
- [ ] rollout e kill switch definidos

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `engineering_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir protocolo P2 depois da escolha experimental da engine.

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
