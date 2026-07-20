# Governança de riscos do W_Flyer

> Status: canônico. Revisão: 2026-07-20.

Este diretório transforma o pre-mortem em artefatos operacionais.

## Arquivos

- `01-metodo-fmea-registro.md`: método de identificação, priorização e aceite;
- `02-falhas-desconhecidas-incidentes.md`: resposta a falhas ainda não catalogadas;
- `failure-mode-catalog.yaml`: catálogo legível por máquina;
- `failure-mode-catalog.schema.json`: schema do catálogo.

A matriz humana detalhada permanece em `../qa/19-matriz-falhas-pre-mortem.md`.

## Regra

Nenhum catálogo finito prova ausência de defeitos. A segurança vem da combinação:

```text
modos conhecidos documentados
+ invariantes
+ fault injection
+ observabilidade
+ fail-closed para desconhecidos
+ regressão obrigatória após incidente
```

Todo `PM-*` deve terminar vinculado a teste e evidência antes de a capability correspondente ser ativada.
