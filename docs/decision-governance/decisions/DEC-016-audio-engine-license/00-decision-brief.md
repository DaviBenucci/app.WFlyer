# DEC-016 — Engine, samples e licenças de áudio

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-016`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual engine e conjunto sonoro suportam playback consistente, mobile e distribuição legal?

## Por que esta decisão existe

Samples podem ter licenças incompatíveis e renderização pode elevar custos e latência.

## Prazo e gate

- trilha: `A`;
- fase: `A0`;
- gate: `exit`;
- owner: `audio_lead`.

## Bloqueios atuais

- `BLOCKED_BY_LICENSE_REVIEW`
- `BLOCKED_BY_BENCHMARK`

## Opções conhecidas

- síntese local
- soundfont/sample pack licenciado
- serviço externo somente com privacidade aprovada

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-017`](../../evidence-register.yaml) — Spike de áudio, samples e licenças (`PLANNED`); devido antes de `A0`.

## Critérios de aprovação pré-definidos

- [ ] licença de distribuição aprovada
- [ ] normalização de loudness
- [ ] latência e render offline medidos
- [ ] fallback definido
- [ ] sem dependência de rede nos testes

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `legal_reviewer`
- `music_director`
- `platform_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar spike após PlaybackManifest.

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
