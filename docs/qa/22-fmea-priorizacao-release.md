# FMEA e priorização de falhas para release

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Priorizar prevenção sem reduzir riscos críticos a uma média enganosa.

## Dimensões

```text
S — severidade: 1 a 5
O — ocorrência estimada: 1 a 5
D — dificuldade de detecção antes do usuário: 1 a 5
RPN informativo = S x O x D
```

## Regras

- `S=5` em música silenciosamente incorreta, acesso indevido, perda de autoria ou execução perigosa nunca é aceito apenas por RPN baixo;
- risco sem dados usa estimativa conservadora;
- “não ocorreu” não equivale a ocorrência zero;
- controles preventivos e detectivos são registrados separadamente;
- risco residual exige owner e data de revisão.

## Registro mínimo

| Campo | Obrigatório |
|---|---|
| ID e capability | sim |
| cenário/efeito/causa | sim |
| S/O/D e justificativa | sim |
| controles atuais | sim |
| teste e observabilidade | sim |
| owner/status | sim |
| residual e decisão | sim |

## Gate

Antes de cada release, revisar riscos novos, mudanças de S/O/D, incidents e cobertura dos `PM-*`. A aprovação do conselho musical não substitui segurança/engenharia; e o inverso também não.
