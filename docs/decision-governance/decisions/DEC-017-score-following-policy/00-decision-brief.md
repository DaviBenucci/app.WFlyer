# DEC-017 — Política de score following

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-017`. Implementação autorizada: **não**.

## Pergunta de decisão

O primeiro score following acompanha apenas áudio gerado ou também performance capturada?

## Por que esta decisão existe

Performance ao vivo exige microfone, privacidade, latência e tratamento de improvisação/repeats ambíguos.

## Prazo e gate

- trilha: `A`;
- fase: `A0`;
- gate: `exit`;
- owner: `audio_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_PRODUCT_SCOPE`

## Opções conhecidas

- somente playback gerado
- performance ao vivo em fase posterior
- sem score following inicial

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-018`](../../evidence-register.yaml) — Benchmark e política de score following (`PLANNED`); devido antes de `A0`.

## Critérios de aprovação pré-definidos

- [ ] escopo explícito
- [ ] mapa de ocorrência aprovado
- [ ] privacidade e permissão de microfone
- [ ] benchmark de repeats/saltos
- [ ] fallback manual

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `privacy_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Manter acompanhamento ao vivo fora do escopo até evidência própria.

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
