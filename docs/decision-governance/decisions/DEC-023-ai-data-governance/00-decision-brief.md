# DEC-023 — Governança de dados para motores de IA

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-023`. Implementação autorizada: **não**.

## Pergunta de decisão

Quais provedores, regiões, retenção, treino e consentimentos são permitidos para conteúdo musical?

## Por que esta decisão existe

Partituras podem conter dados, autoria e material protegido; metadata não confiável também pode conter prompt injection.

## Prazo e gate

- trilha: `GOV`;
- fase: `AI-PROVIDER`;
- gate: `entry`;
- owner: `privacy_reviewer`.

## Bloqueios atuais

- `BLOCKED_BY_PRIVACY_REVIEW`
- `BLOCKED_BY_LEGAL_REVIEW`
- `BLOCKED_BY_SECURITY_REVIEW`

## Opções conhecidas

- execução local
- provedor com retenção zero aprovada
- nenhum uso de modelo externo

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-024`](../../evidence-register.yaml) — Revisão de fornecedores e dados para IA (`PLANNED`); devido antes de `AI-PROVIDER`.

## Critérios de aprovação pré-definidos

- [ ] inventário de fornecedores
- [ ] DPA/termos avaliados
- [ ] uso para treino desabilitado por padrão
- [ ] redaction e minimização
- [ ] consentimento separado quando aplicável
- [ ] kill switch por fornecedor

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `security_lead`
- `legal_reviewer`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Não enviar arquivos a provedor externo sem aprovação.

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
