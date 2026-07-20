# Página Laboratório de Harmonização

> Status: canônico para trilha H. Revisão: 2026-07-20.

## Rota

```text
/harmonizar/{version_id}
```

## Pré-condições

- capability habilitada;
- melodia confirmada;
- fonte não expirada;
- perfil mínimo disponível.

## Etapas no mesmo workspace

```text
confirmar análise
configurar perfil
gerar variantes
comparar
aprovar
```

Não usar wizard modal que esconda a partitura.

## Estados

```text
analysis_required
profile_incomplete
generating
variants_ready
no_valid_variant
reviewing
approval_pending
approved
source_changed
```

## Saída

Aprovação cria nova versão e redireciona para Resultado/Comparação. Nenhuma variante é chamada de “correta”.
