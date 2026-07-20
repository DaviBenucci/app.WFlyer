# Backlog executável — ponte histórica

O backlog e seus gates estão em:

```text
docs/100-implementacao/guia-codex-app-wflyer.md
```

## Ordem Core

```text
0 Governança
1 Fundação/contratos/sessão
2 Catálogo/modelo musical
3 Motor MusicXML
4 Upload/storage/fila
5 Corte vertical
6 Segurança/retenção
7 UX/acessibilidade/histórico
8 Qualidade/operação
9 Aceite
```

PDF de saída e PDF/OMR são trilhas opcionais; não devem ser inseridos no meio do Core como dependência.

## Épicos avançados bloqueados por gate

```text
EPIC-M: modelo multipauta/multiparte
EPIC-L: extração de melodia e revisão
EPIC-H: harmonização e variantes
EPIC-W: watermark, manifesto e assinatura
```

Não mover para “em implementação” sem ADR, corpus, métricas e capability default-off. O primeiro slice de H não pode chamar API de IA e renderizar acordes antes do motor de restrições.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Fundação crítica antes dos épicos avançados

- F0.1 validar schemas e manifest de referências;
- F0.2 transformar protótipos em stories com fixtures;
- Q0.1 criar registro executável `REQ/RISK/PM/test`;
- D0.1 definir IDs estáveis e event mapping no Core;
- D0.2 gerar manifest/diff machine-readable;
- O0.1 implementar kill switch por capability;
- O0.2 estruturar incident-to-fixture workflow.

## Épicos de diferenciação

- D — Musical Diff e comparação;
- L — extração/revisão de melodia;
- I — tocabilidade e adaptação idiomática;
- H — análise/harmonização;
- A — áudio A/B e ensaio;
- E — score/partes/ensemble;
- C — colaboração e versionamento.

Cada épico começa com decisão, corpus, risco, contrato e flag desligada.
