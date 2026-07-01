# Privacidade e retenção

## Regra de retenção

Arquivos originais e artefatos finais ficam no armazenamento controlado pela aplicação por até 15 dias.

## Histórico local

O navegador pode manter metadados locais. O usuário deve poder limpar esses dados.

## Dados mínimos

No MVP, armazenar apenas o necessário:

```text
job_id
filename sanitizado
instrumentos
status
artefatos
expiração
```

## Após expiração

- Bloquear download.
- Marcar job como `expired` quando aplicável.
- Remover ou anonimizar metadados sensíveis quando aplicável.
- Registrar evento de expiração.

## Mensagem ao usuário

```text
Arquivos expiram após 15 dias. Baixe o resultado se quiser manter uma cópia.
```
