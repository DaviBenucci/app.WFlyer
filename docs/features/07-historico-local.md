# Histórico local

## Objetivo

Preservar metadados de transposições no dispositivo sem exigir conta.

## Dados permitidos

```text
job_id
nome sanitizado da partitura
instrumento origem
instrumento destino
intervalo
data
status final
expires_at
estado local
```

## Estados

```text
Disponível
Expirado
Removido localmente
Armazenamento local indisponível
```

## Privacidade

- Usuário pode limpar histórico.
- Não salvar tokens permanentes.
- Não sincronizar sem decisão futura.
- Avisar que histórico é deste dispositivo.

## Testes

- Criar histórico após job concluído.
- Atualizar estado expirado.
- Limpar histórico remove registros.
- Aplicação continua funcionando sem armazenamento local.
