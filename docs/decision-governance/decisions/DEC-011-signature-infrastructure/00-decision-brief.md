# DEC-011 — Infraestrutura de assinatura e verificação

> Status: `IDENTIFIED`. ID(s) legado(s): `PEND-011`. Implementação autorizada: **não**.

## Pergunta de decisão

Como assinar manifestos/artefatos, rotacionar chaves e verificar integridade após retenção ou purge?

## Por que esta decisão existe

Assinatura mal projetada cria falsa confiança, indisponibilidade ou exposição de chaves.

## Prazo e gate

- trilha: `W`;
- fase: `W2`;
- gate: `exit`;
- owner: `security_lead`.

## Bloqueios atuais

- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_INFRASTRUCTURE_DATA`

## Opções conhecidas

- KMS gerenciado
- HSM conforme necessidade
- assinatura desabilitada no primeiro release

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-012`](../../evidence-register.yaml) — Spike de assinatura, KMS e verificação (`PLANNED`); devido antes de `W2`.

## Critérios de aprovação pré-definidos

- [ ] algoritmo e cadeia aprovados
- [ ] chaves nunca exportadas para aplicação
- [ ] rotação e revogação testadas
- [ ] endpoint de verificação definido
- [ ] política pós-purge explícita

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `platform_lead`
- `legal_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Executar spike W2 somente quando watermark e manifesto existirem.

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
