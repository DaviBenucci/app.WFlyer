# Contrato de fidelidade visual para IA/Codex

> Status: canônico e bloqueante. Revisão: 2026-07-20.

## Regra principal

Antes de implementar ou modificar uma página, a IA deve ler `../design-reference/reference-manifest.yaml`, localizar a referência aplicável e declarar o que será preservado.

## Protocolo obrigatório

### Antes do código

1. identificar `reference_id`;
2. listar arquivos executáveis, specifications, stories e fixtures aplicáveis;
3. registrar elementos obrigatórios e proibidos;
4. listar estados de erro, loading, review, offline e conteúdo extremo;
5. confirmar tokens, breakpoints, acessibilidade e reduced motion;
6. apontar lacunas ou conflitos antes de inventar solução.

### Durante

- usar tokens oficiais;
- preservar hierarquia e foco da tarefa;
- não substituir composição por grade de cards;
- não adicionar hero, glow, gradiente, métricas, depoimentos ou seções sem referência;
- não esconder erro em toast quando a especificação exige estado persistente;
- não converter tudo em Client Component por causa de animação;
- não copiar código, branding, texto ou ilustração de produto externo;
- manter fixtures e stories sincronizadas.

### Depois

1. gerar screenshots nos viewports especificados;
2. executar interação, acessibilidade e visual regression;
3. comparar com o baseline;
4. anexar diff e justificativa de divergências;
5. testar nomes longos, warnings múltiplos, zoom, teclado e reduced motion;
6. atualizar referência somente após aprovação humana.

## Formato do relatório

```text
Reference ID:
Página/componente:
Estado implementado:
Elementos vinculantes preservados:
Divergências intencionais:
Motivo:
Screenshots gerados:
Testes de interação:
Acessibilidade:
Reduced motion:
Riscos visuais restantes:
Aprovação do diff: pendente|aprovada|rejeitada
```

## Precedência

```text
regra musical, API, segurança e acessibilidade
> exemplo executável interno aprovado
> story aprovada
> specification machine-readable
> golden screenshot
> texto de inspiração
```

Um screenshot nunca autoriza texto ilegível, foco ausente ou interação inacessível.

## Lacuna de referência

A ausência de referência não autoriza invenção silenciosa. A IA deve:

1. registrar `DESIGN_REFERENCE_MISSING`;
2. propor até três composições próprias do W_Flyer;
3. explicar trade-offs;
4. aguardar decisão ou criar um protótipo marcado como `draft`;
5. não promover draft a binding sem aprovação.

## Proibições

- atualizar screenshot esperado sem revisar o diff;
- usar lorem ipsum ou dados falsos em golden final;
- copiar exatamente layout ou paleta de marca externa;
- construir apenas o happy path;
- ignorar fixtures de sessão expirada, baixa confiança ou erro musical;
- utilizar score de diferença de pixels como aprovação automática;
- atribuir autoria musical à aplicação por microcopy decorativa.

## Gate

A tarefa de frontend não está concluída sem `reference_id`, story, estados aplicáveis, evidência visual e revisão de acessibilidade.
