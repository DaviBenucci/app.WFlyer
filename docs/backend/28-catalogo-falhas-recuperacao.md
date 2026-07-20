# Catálogo de falhas e política de recuperação

> Status: canônico. Revisão: 2026-07-20.

## Separação de identificadores

- `PM-*`: modo de falha interno, usado por engenharia e QA;
- `risk_id`: risco agregado do produto;
- `incident_id`: ocorrência real;
- `public_error_code`: mensagem estável e acionável da API;
- `correlation_id`: rastreamento técnico.

Um `PM-*` não deve ser exposto ao usuário como texto de erro. Vários modos internos podem mapear para o mesmo código público seguro.

## Classificador

```ts
interface FailureClassification {
  failureModeId: string
  publicErrorCode: string
  handling: 'reject' | 'review' | 'retry' | 'degrade' | 'incident'
  retryClass: 'never' | 'transient' | 'after_user_action' | 'after_configuration_change'
  musicalIntegrityAtRisk: boolean
  authorizationAtRisk: boolean
  artifactPublishAllowed: boolean
  alertPolicy: string
}
```

## Regras

- erro determinístico de música/parsing não entra em retry automático;
- indisponibilidade transitória pode repetir somente operação idempotente;
- ambiguidade musical gera revisão, não loop;
- erro desconhecido não é convertido em warning genérico;
- nenhum catch amplo pode marcar job como `completed`;
- publicação parcial usa status e artifact type explícitos; nunca simula pacote completo;
- retry conserva a versão de engine/configuração ou cria nova revisão declarada.

## Fonte

O catálogo legível por máquina está em `../riscos/failure-mode-catalog.yaml`; a matriz narrativa está em `../qa/19-matriz-falhas-pre-mortem.md`.
