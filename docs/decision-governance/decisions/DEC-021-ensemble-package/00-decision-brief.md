# DEC-021 — Pacote ensemble inicial

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-021`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais formações, papéis, divisi/doubling e artefatos entram no primeiro pacote ensemble?

## Por que esta decisão existe

Gerar partes sem política de distribuição e consistência pode criar material incoerente ou inexequível.

## Prazo e gate

- trilha: `E`;
- fase: `E0`;
- gate: `exit`;
- owner: `music_director`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`
- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- formação pequena predefinida
- formações configuráveis depois
- score e partes sem arranjo automático inicialmente

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-022`](../../evidence-register.yaml) — Consistência de score, partes e ensemble (`PLANNED`); devido antes de `E0`.

## Critérios de aprovação pré-definidos

- [ ] formações e papéis definidos
- [ ] score/partes do mesmo grafo
- [ ] marcas/compassos/transposição sincronizados
- [ ] validação instrumental
- [ ] pacote publicado atomicamente

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `instrument_reviewers`
- `music_engineering_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Bloqueado por M, I e renderer.

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
