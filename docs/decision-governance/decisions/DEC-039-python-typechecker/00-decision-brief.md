# DEC-039 — Typechecker Python definitivo

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual typechecker será gate do workspace Python e com qual nível de estrito?

## Por que esta decisão existe

A escolha afeta configuração, stubs, velocidade e qualidade da API/domínio.

## Prazo e gate

- trilha: `CORE`;
- fase: `CORE-1`;
- gate: `exit`;
- owner: `backend_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`

## Opções conhecidas

- mypy
- pyright/basedpyright
- outro somente com justificativa

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-040`](../../evidence-register.yaml) — Comparativo de typecheckers Python (`PLANNED`); devido antes de `CORE-1`.

## Critérios de aprovação pré-definidos

- [ ] spike no scaffold real
- [ ] compatibilidade FastAPI/SQLAlchemy/pacotes internos
- [ ] tempo de execução
- [ ] baseline sem suppressions genéricas
- [ ] versão fixada

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `engineering_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Decidir dentro da Fase 1 antes do gate de saída.

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
