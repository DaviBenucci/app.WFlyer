# Workspace de revisão musical

> Status: canônico para capacidades que exigem decisão do usuário. Rota condicionada a feature flags.

## Rota

```text
/revisao/{job_id}
```

## Objetivo

Resolver incertezas de reconhecimento, escolha melódica ou harmonização sem transformar o W_Flyer em um editor de partituras completo no primeiro release.

## Motivos

```text
source_recognition
melody_selection
harmony_variant
```

A UI muda o inspector e as ações, mas preserva o mesmo `ReviewWorkspace`.

## Composição

```text
ReviewHeader
  operação, origem, destino, status de garantia
ScoreComparisonCanvas
  fonte
  overlay de regiões/eventos
  proposta/resultado
ReviewInspector
  motivo e explicação
  alternativas
  parâmetros
  warnings
ReviewActionBar
  salvar rascunho
  confirmar e continuar
  rejeitar/cancelar
```

## Revisão de melodia

- linha sugerida destacada;
- acompanhamento atenuado, não oculto permanentemente;
- alternativas por frase;
- seleção por teclado e clique;
- reprodução opcional somente quando implementada;
- contador de regiões pendentes;
- não permitir confirmar enquanto houver bloqueio estrutural.

## Revisão de harmonização

- melodia original visualmente bloqueada;
- notas geradas diferenciadas sem depender só de cor;
- comparação A/B entre variantes;
- controles de densidade, tensão, ritmo harmônico, modo e dificuldade;
- explicação curta por região, sem antropomorfizar a IA;
- opção “manter apenas a melodia”.

## Persistência

Submissões usam versão otimista e idempotência. Conflito de revisão retorna estado atual; duas abas não sobrescrevem silenciosamente.

## Acessibilidade

- operações de seleção possuem alternativa sem drag;
- foco e anúncio por compasso/região;
- zoom até 400%;
- padrões/labels além de cor;
- atalhos documentados e desligáveis;
- reduced motion sem perda de contexto.

## Critérios de aceite

- refresh recupera revisão da mesma sessão;
- origem permanece imutável;
- confirmação cria nova versão, não edita artefato anterior;
- todas as regiões bloqueantes devem ser resolvidas;
- cancelamento não publica resultado parcial;
- retorno ao job mostra a decisão e o novo nível de garantia.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Unidade de decisão

Revisão ocorre por região/frase/evento, com áudio e contexto anterior/posterior quando disponíveis. Uma ação deve declarar escopo:

```text
esta ocorrência
esta frase
regiões semelhantes propostas
restante da revisão, somente com confirmação adicional
```

## Concorrência e auditoria

A decisão inclui `revision_id`, versão, autor, data, alternativa escolhida e motivo opcional. Se a revisão mudou, a UI apresenta conflito; não reaplica silenciosamente a escolha.

## Referência

`reference_id: WF-MELODY-REVIEW-001` para revisão de melodia.
