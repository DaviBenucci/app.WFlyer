# Fluxo de uma decisão

## Lifecycle

```text
IDENTIFIED
→ REQUIREMENTS_DEFINED
→ RESEARCHING
→ EXPERIMENTING
→ EVIDENCE_READY
→ DECISION_PENDING_APPROVAL
→ DECIDED
→ IMPLEMENTED
→ VALIDATED
```

`SUPERSEDED` preserva histórico, mas nunca atende um gate ativo sem que o gate seja atualizado para a decisão substituta.

## Critérios para mover de estado

| Transição | Condição mínima |
|---|---|
| IDENTIFIED → REQUIREMENTS_DEFINED | pergunta, escopo, owner, opções, evidências e fase definidos |
| → RESEARCHING | requisitos aprovados e fontes/candidatos delimitados |
| → EXPERIMENTING | plano pré-registrado, ambiente/corpus e custo autorizados |
| → EVIDENCE_READY | artefatos completos e reproduzíveis, ainda sem aprovação |
| → DECISION_PENDING_APPROVAL | revisão técnica/musical/legal aplicável concluída |
| → DECIDED | approval record humano + decision record |
| → IMPLEMENTED | OpenSpec e código/testes concluídos |
| → VALIDATED | evidência pós-implementação, regressão, operação e rollback aprovados |

A decisão é reaberta quando evidência expira, a versão muda, há incidente, custo se altera materialmente ou o escopo deixa de ser equivalente.
