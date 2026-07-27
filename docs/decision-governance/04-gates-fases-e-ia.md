# Gates por fase e comportamento da IA

`phase-decision-gates.yaml` não substitui os gates de código, segurança, música e QA; ele adiciona o gate de decisão/evidência.

## Consulta

```bash
python3 scripts/check-decision-gate.py CORE-1 --gate entry
python3 scripts/check-decision-gate.py CORE-1 --gate exit
```

Código de saída `0` libera apenas a camada de decisão. Código diferente de zero exige parada ou trabalho limitado ao experimento explicitamente autorizado.

## Ferramentas opcionais

Temporal, Rive, Pact, mutation testing e cache remoto possuem fases `FUTURE-*`. A ausência deles não bloqueia o MVP. Eles também não podem ser instalados preventivamente.

## Resposta mínima quando bloqueado

```text
Decisão bloqueada: DEC-XXX
Fase/gate: ...
Estado: ...
Evidências faltantes: EVID-...
Trabalho permitido: pesquisa/spike autorizado
Implementação proibida: ...
Aprovação necessária: ...
```
