# Evidências — DEC-047

> Estado: `EMPTY`. Não apagar resultados negativos, falhas, outliers ou logs necessários à reprodução.

## Artefatos esperados

- `EVID-048` — Threat model e teste do modelo de conta e organizações: fluxos visitante/conta/organização; migração de ownership anônimo; threat model de autenticação e recuperação; teste de convite/revogação/RBAC; avaliação de privacidade e retenção; teste UX e acessibilidade

Cada evidência aceita deve atualizar `evidence-register.yaml` com:

- `artifact_paths`;
- `review_record`;
- `source_commit`;
- `environment`;
- `collected_at` e, quando aplicável, `expires_at`.

Arquivos brutos grandes podem ficar em storage controlado, mas este diretório deve conter manifesto, checksums, comandos e localização verificável.
