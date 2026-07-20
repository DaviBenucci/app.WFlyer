# Tela Histórico

> Revisão: 2026-07-20.

## Rota

```text
/historico
```

## Objetivo

Listar referências locais a jobs recentes com clareza operacional. Não criar dashboard de métricas no MVP sem conta.

## Shell

`UtilityShell`.

## Composição

```text
PageHeader
Filtros simples, quando necessários
HistoryList
Retention/SessionNotice
```

## Lista

Desktop: linhas estruturadas com colunas adaptativas.

Mobile: linhas empilhadas dentro de uma superfície contínua. Evitar um card grande por item quando isso prejudicar comparação.

## Item

```text
filename sanitizado
origem -> destino
intervalo
status
warnings
criado em
expira em
artefatos
```

`TranspositionRoute` pode ter variante compacta.

## Ações

- abrir resultado;
- remover do histórico local;
- apagar arquivos do servidor, quando autorizado;
- iniciar nova transposição com mesmas preferências.

Repetir não reutiliza bytes expirados.

## Empty state

Não usar ilustração genérica. Mostrar:

```text
Nenhuma transposição neste navegador.
Ao concluir uma transposição, a referência aparecerá aqui enquanto os dados locais estiverem disponíveis.
```

CTA: “Transpor uma partitura”.

## Critérios de aceite

- histórico não parece dashboard;
- ações local e servidor são distintas;
- itens expirados não oferecem download;
- sessão diferente recebe estado neutro;
- lista funciona com nomes longos, muitos warnings e storage indisponível.
