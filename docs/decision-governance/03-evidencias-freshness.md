# Evidências, reprodução e validade

Uma evidência não é apenas uma conclusão escrita. Para ser `ACCEPTED`, deve indicar:

- artefatos e checksums/localização;
- commit, versão e ambiente;
- corpus/dados e licença;
- comandos, seeds e configuração;
- resultados positivos, negativos e falhas;
- revisão e aprovação aplicável;
- data de coleta e regra de expiração.

## Estados

```text
NOT_STARTED → PLANNED → IN_PROGRESS → READY_FOR_REVIEW → ACCEPTED
```

`REJECTED` e `STALE` são estados terminais para o gate atual e **nunca** satisfazem requisito `ACCEPTED`.

## Proibições

- apagar outlier para melhorar média;
- trocar threshold depois de ver o resultado sem reabrir o plano;
- aceitar screenshot sem dados/ambiente quando benchmark exige reprodução;
- usar corpus de treino como corpus de release;
- reutilizar evidência antiga após mudança material sem revisão de freshness.
