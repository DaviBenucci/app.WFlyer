# DEC-002 — Engine de renderização e engraving

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-002`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual renderer deve transformar MusicXML aprovado em PDF/SVG legível e determinístico?

## Por que esta decisão existe

Sem gate próprio, um documento semanticamente correto pode gerar impressão ilegível, colisões ou paginação inadequada.

## Prazo e gate

- trilha: `R`;
- fase: `R0`;
- gate: `exit`;
- owner: `engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_LICENSE_REVIEW`
- `BLOCKED_BY_MUSICAL_REVIEW`

## Opções conhecidas

- MuseScore Studio por adapter de spike
- renderer alternativo a avaliar
- serviço próprio somente se evidência justificar

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-003`](../../evidence-register.yaml) — Benchmark de renderer e engraving (`PLANNED`); devido antes de `R0/R1`.

## Critérios de aprovação pré-definidos

- [ ] nenhum evento musical omitido no corpus
- [ ] nenhuma colisão crítica não detectada
- [ ] impressão e dispositivos-alvo avaliados
- [ ] fontes e licença compatíveis
- [ ] execução containerizada e reprodutível
- [ ] tempo e memória dentro de limites PENDENTE

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `music_director`
- `frontend_lead`
- `legal_reviewer`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar R0 com golden files de engraving e revisão musical cega.

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
