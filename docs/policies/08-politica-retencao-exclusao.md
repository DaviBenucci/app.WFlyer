# Política de Retenção e Exclusão — estrutura do documento

> Status: rascunho. Prazos finais dependem do produto, obrigações fiscais e contratos.

## Categorias

| Categoria | Prazo planejado | Estado |
|---|---|---|
| Upload original do MVP | até 15 dias | proposta atual |
| Resultado do MVP | até 15 dias após conclusão | proposta atual |
| Intermediários | mínimo necessário | `PENDENTE` |
| Conta | enquanto ativa + regra de encerramento | `PENDENTE` |
| Ledger de créditos | conforme necessidade financeira/auditoria | `PENDENTE` |
| Pagamentos | conforme obrigação aplicável | `PENDENTE` |
| Documentos fiscais | conforme obrigação aplicável | `PENDENTE` |
| Logs de segurança | `PENDENTE` | `PENDENTE` |
| Backups | `PENDENTE` | `PENDENTE` |
| Tickets de suporte | `PENDENTE` | `PENDENTE` |

## Exclusão pelo usuário

- apagar projeto;
- apagar arquivo antes do prazo;
- solicitar encerramento da conta;
- distinguir exclusão imediata da área ativa e expiração em backups;
- informar exceções obrigatórias;
- fornecer protocolo.

## Processo técnico

```text
pedido autorizado
→ bloqueio de acesso
→ purge idempotente da área ativa
→ remoção de derivados
→ registro mínimo de conclusão
→ expiração em backups conforme ciclo
→ confirmação ao usuário
```

## Proibições

- manter arquivo em log;
- manter cópia oculta para treino;
- declarar exclusão imediata de backup quando isso não for tecnicamente verdadeiro;
- apagar registro financeiro obrigatório junto com o arquivo musical;
- conservar PII por conveniência indefinida.
