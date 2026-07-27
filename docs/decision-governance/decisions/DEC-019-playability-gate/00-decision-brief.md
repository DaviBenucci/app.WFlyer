# DEC-019 — Gate de tocabilidade e dificuldade

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-019`. Implementação autorizada: **não**.

## Pergunta de decisão

Como separar impossível, tecnicamente possível, difícil, idiomático e confortável por instrumento e nível?

## Por que esta decisão existe

Uma nota dentro da extensão pode ser inviável no andamento, registro, respiração, span ou técnica.

## Prazo e gate

- trilha: `T`;
- fase: `T0`;
- gate: `exit`;
- owner: `music_director`.

## Bloqueios atuais

- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_CORPUS`

## Opções conhecidas

- regras por instrumento/nível
- classificador de severidade
- somente warnings no primeiro rollout aprovado

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-016`](../../evidence-register.yaml) — Fontes e revisão dos perfis instrumentais (`PLANNED`); devido antes de `CORE-2/T0`.
- [`EVID-020`](../../evidence-register.yaml) — Avaliação de tocabilidade por instrumento (`PLANNED`); devido antes de `T0`.

## Critérios de aprovação pré-definidos

- [ ] perfis e nível do intérprete declarados
- [ ] corpus revisado por instrumentistas
- [ ] severidade e mensagem explicáveis
- [ ] não alterar automaticamente sem autorização
- [ ] taxa de discordância registrada

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `instrument_reviewers`
- `qa_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Aguardar DEC-015 e corpus instrumental.

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
