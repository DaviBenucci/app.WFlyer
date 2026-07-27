# Regra operacional de referências visuais para IA

> Status: bloqueante. Revisão: 2026-07-20.

## Prompt obrigatório

```text
Antes de escrever frontend:
1. leia docs/design-reference/reference-manifest.yaml;
2. identifique reference_id, status, capability_status, gate e specification;
3. se status=reference ou capability_status=disabled, não implemente a referência;
4. abra o protótipo interno e story apenas para referências liberadas;
5. liste estados e proibições;
6. implemente com tokens oficiais;
7. gere screenshots nos viewports definidos;
8. execute interação, acessibilidade e visual diff;
9. registre divergências; não atualize baseline sem aprovação.
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
