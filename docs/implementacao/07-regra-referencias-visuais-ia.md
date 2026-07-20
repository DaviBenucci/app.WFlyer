# Regra operacional de referências visuais para IA

> Status: bloqueante. Revisão: 2026-07-20.

## Prompt obrigatório

```text
Antes de escrever frontend:
1. leia docs/design-reference/reference-manifest.yaml;
2. identifique reference_id e specification;
3. abra o protótipo interno e story, se existirem;
4. liste estados e proibições;
5. implemente com tokens oficiais;
6. gere screenshots nos viewports definidos;
7. execute interação, acessibilidade e visual diff;
8. registre divergências; não atualize baseline sem aprovação.
```

## Saída esperada da IA

- referência usada;
- arquivos alterados;
- states cobertos;
- screenshots;
- testes;
- divergências;
- lacunas.

## Falha

Sem referência aplicável, criar issue/proposta `draft`; não inventar composição como final.
