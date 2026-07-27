# DEC-010 — Corpus musical e conselho revisor

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-010`. Implementação autorizada: **não**.

## Pergunta de decisão

Quem rotula, revisa e aprova o corpus e com quais regras de independência e licença?

## Por que esta decisão existe

Benchmarks musicais sem corpus governado e avaliadores identificados não sustentam promessa de qualidade.

## Prazo e gate

- trilha: `Q`;
- fase: `Q0`;
- gate: `entry`;
- owner: `product_owner`.

## Bloqueios atuais

- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_LICENSE_REVIEW`

## Opções conhecidas

- conselho interno inicial
- revisores externos contratados
- rede por instrumento/estilo

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-011`](../../evidence-register.yaml) — Governança do corpus e conselho (`PLANNED`); devido antes de `Q0`.

## Critérios de aprovação pré-definidos

- [ ] licença/proveniência por fixture
- [ ] separação treino/validação/release
- [ ] protocolo de desacordo e desempate
- [ ] conflitos de interesse registrados
- [ ] validade temporal das aprovações

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `legal_reviewer`
- `qa_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Definir charter antes das trilhas L/H/I.

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
