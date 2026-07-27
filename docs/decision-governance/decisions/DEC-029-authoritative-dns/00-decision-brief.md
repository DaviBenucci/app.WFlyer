# DEC-029 — DNS autoritativo e gestão de domínios

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-031`. Implementação autorizada: **não**.

## Pergunta de decisão

Onde hospedar DNS autoritativo e como operar wflyer.com.br/app/status sem ponto único de erro?

## Por que esta decisão existe

A decisão afeta disponibilidade, automação, WAF/CDN, custo e recuperação de incidente.

## Prazo e gate

- trilha: `INF`;
- fase: `INF0`;
- gate: `exit`;
- owner: `platform_lead`.

## Bloqueios atuais

- `BLOCKED_BY_INFRASTRUCTURE_DATA`
- `BLOCKED_BY_COST_DATA`

## Opções conhecidas

- Registro.br DNS
- Cloudflare DNS
- Route 53

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-030`](../../evidence-register.yaml) — Análise e exercício de DNS (`PLANNED`); devido antes de `INF0`.

## Critérios de aprovação pré-definidos

- [ ] ownership e acesso protegidos
- [ ] DNSSEC e MFA avaliados
- [ ] TTL e rollback testados
- [ ] separação site/app/status
- [ ] runbook de troca/falha

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Decidir em INF0, não durante desenvolvimento local.

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
