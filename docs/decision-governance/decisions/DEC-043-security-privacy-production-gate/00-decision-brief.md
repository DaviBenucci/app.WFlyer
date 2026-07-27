# DEC-043 — Gate de segurança e privacidade para produção

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `nenhum`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais evidências mínimas de segurança, privacidade, restore e resposta a incidentes são exigidas antes de produção?

## Por que esta decisão existe

Documentação sem controles implementados não protege arquivos, contas, pagamentos ou autoria.

## Prazo e gate

- trilha: `LAUNCH`;
- fase: `LAUNCH`;
- gate: `entry`;
- owner: `security_lead`.

## Bloqueios atuais

- `BLOCKED_BY_IMPLEMENTATION`
- `BLOCKED_BY_SECURITY_REVIEW`
- `BLOCKED_BY_PRIVACY_REVIEW`

## Opções conhecidas

- produção bloqueada até pacote aceito

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-044`](../../evidence-register.yaml) — Pacote de segurança e privacidade de produção (`PLANNED`); devido antes de `LAUNCH`.

## Critérios de aprovação pré-definidos

- [ ] inventário/fluxo de dados
- [ ] threat model atualizado
- [ ] IDOR/CSRF/upload hostil/dependências
- [ ] pentest ou revisão independente aplicável
- [ ] restore e incident runbooks exercitados
- [ ] riscos críticos com owner/evidência

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `privacy_reviewer`
- `product_owner`
- `engineering_lead`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Montar pacote durante hardening; aprovar antes do go-live.

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
