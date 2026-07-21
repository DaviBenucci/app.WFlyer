# XState — estados reativos e comportamento previsível

> Status: condicional e obrigatório para fluxos complexos aprovados.

## Responsabilidade

XState formaliza estados, eventos, guards, actors e efeitos de fluxos que possuem concorrência, cancelamento, retry, revisão ou expiração.

Motion e GSAP animam; XState decide quando e por que a transição ocorre.

## Instalação

No app web:

```bash
pnpm add xstate @xstate/react
```

Para testes baseados em caminhos, avaliar o pacote atual `@xstate/graph`; não adotar `@xstate/test` novo, pois as utilidades modernas migraram para `xstate/graph`.

## Quando usar

- upload → validação → configuração → processamento → revisão → resultado;
- polling/SSE com pausa, retry, cancelamento e expiração;
- harmonização com variantes e aprovação;
- modo de ensaio com transporte e estados de áudio;
- editor/revisão colaborativa com conflito.

## Quando não usar

- abrir/fechar tooltip;
- alternar um ícone simples;
- estado de formulário já resolvido por React Hook Form;
- cache remoto já resolvido por TanStack Query;
- valor puramente visual que pertence ao Motion.

## Máquina mínima do estúdio

```text
idle
→ fileSelected
→ validating
→ invalid
→ configuring
→ ready
→ submitting
→ processing
→ requiresReview
→ completed
→ failed
→ expired
→ cancelled
```

Eventos devem ser nomes de domínio:

```text
FILE_SELECTED
SOURCE_VALIDATED
SOURCE_REJECTED
ORIGIN_CONFIRMED
TRANSPOSE_REQUESTED
JOB_PROGRESS_RECEIVED
REVIEW_REQUIRED
REVIEW_APPROVED
RETRY_REQUESTED
CANCEL_REQUESTED
RESULT_EXPIRED
```

## Regras de implementação

- contexto tipado;
- eventos discriminados;
- guards puros;
- efeitos em actors, não em guards;
- cleanup explícito de subscriptions;
- estados terminais definidos;
- retry limitado e classificado;
- cancelamento não é erro genérico;
- a máquina não duplica estado autoritativo do backend;
- URL/estado persistido só contém dados seguros;
- cada estado visível possui story e teste.

## Integração com animações

```text
XState snapshot
→ componente deriva estado visual
→ Motion executa presença/layout
→ GSAP executa timeline isolada
```

Nenhuma timeline pode decidir conclusão de job. A transição para `completed` vem do contrato do backend, não do fim de uma animação.

## Testes

- unitários de transitions/guards;
- caminhos felizes e falhas;
- eventos fora de ordem;
- cancelamento durante processamento;
- reconexão;
- expiração;
- reduced motion sem alterar lógica;
- model-based paths quando o custo for justificável.

## Critério de adoção

Uma máquina só entra quando:

- o OpenSpec lista estados/eventos;
- a matriz de estados da UI foi atualizada;
- existe diagrama ou tabela;
- testes de transição existem;
- o time comprova que ela reduz estados impossíveis.

## Fontes oficiais

- <https://stately.ai/docs/xstate>
- <https://stately.ai/docs/xstate-react>
- <https://stately.ai/docs/xstate-test>
