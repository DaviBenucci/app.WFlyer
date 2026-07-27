# DEC-037 — Ativação de testes de contrato com Pact

> Status: `IDENTIFIED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Quando testes consumidor-provedor acrescentam valor além do OpenAPI e integração?

## Por que esta decisão existe

Pact precoce adiciona manutenção sem consumidores independentes; tardio pode permitir divergência.

## Prazo e gate

- trilha: `TOOL`;
- fase: `FUTURE-PACT`;
- gate: `entry`;
- owner: `qa_lead`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`

## Opções conhecidas

- OpenAPI/cliente gerado suficiente
- Pact quando evolução independente justificar

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-038`](../../evidence-register.yaml) — Avaliação de necessidade do Pact (`PLANNED`); devido antes de `CORE-8`.

## Critérios de aprovação pré-definidos

- [ ] consumidores/provedores identificados
- [ ] falhas reais não cobertas pelo OpenAPI
- [ ] broker e ownership definidos
- [ ] piloto com custo aceitável

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `frontend_lead`
- `backend_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Reavaliar quando web/API evoluírem separadamente.

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
