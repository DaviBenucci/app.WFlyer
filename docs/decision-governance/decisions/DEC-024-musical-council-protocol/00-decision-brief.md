# DEC-024 — Protocolo do conselho musical

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-024`. Implementação autorizada: **não**.

## Pergunta de decisão

Como compor, convocar, registrar e renovar aprovações do conselho musical?

## Por que esta decisão existe

Aprovação vaga por “um músico” não garante competência, independência ou reprodutibilidade.

## Prazo e gate

- trilha: `Q`;
- fase: `Q0`;
- gate: `exit`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_USER_APPROVAL`

## Opções conhecidas

- painel por família instrumental
- revisores por estilo
- revisão externa sob demanda

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-025`](../../evidence-register.yaml) — Charter e registros do conselho musical (`PLANNED`); devido antes de `Q0`.

## Critérios de aprovação pré-definidos

- [ ] número mínimo de revisores
- [ ] instrumento/estilo compatíveis
- [ ] conflito de interesse
- [ ] desempate
- [ ] parecer versionado
- [ ] prazo de validade

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `qa_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Criar charter antes de benchmarks avançados.

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
