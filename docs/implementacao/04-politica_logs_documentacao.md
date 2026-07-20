# Política de logs de projeto e documentação

## Arquivos

```text
docs/logs/IMPLEMENTATION_LOG.md
docs/logs/TEST_LOG.md
docs/logs/DECISIONS.md
docs/logs/CHANGELOG.md
```

## IMPLEMENTATION_LOG

Registrar tarefa, fase, objetivo, comportamento anterior/novo, arquivos, contratos/migrations, riscos e pendências. Não copiar chain-of-thought; registrar somente justificativas técnicas verificáveis.

## TEST_LOG

Registrar comando exato, ambiente/versões, fixtures, resultado e falhas. “Testes passaram” sem comando/saída/evidência não é registro suficiente.

## DECISIONS

Formato:

```text
ADR-ID / status
contexto
alternativas consideradas
 decisao
consequencias
migracao/rollback
documentos afetados
```

Status:

```text
ACEITA | PENDENTE | REVOGADA | SUBSTITUIDA
```

## CHANGELOG

Registrar mudança de comportamento/contrato/capability percebida por usuário ou integrador. Alteração interna sem impacto pode permanecer apenas no implementation log.

## Anti-alucinação

Ao faltar decisão:

1. não escolher silenciosamente;
2. registrar pendência e alternativas;
3. bloquear somente a capacidade dependente;
4. continuar partes independentes quando seguro;
5. após aprovação, atualizar primeiro o documento canônico.
