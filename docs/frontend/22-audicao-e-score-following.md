# Audição comparativa e score following

> Status: canônico para trilha futura de áudio. Revisão: 2026-07-20.

## Objetivo

Permitir ouvir origem e resultado no mesmo ponto musical, sem usar o áudio como substituto da validação semântica.

## Modos

```text
ORIGINAL
RESULT
A_B_TOGGLE
SPLIT_MELODY_HARMONY
SOLO_PART
ENSEMBLE
```

## Controles mínimos

- play/pause;
- posição por compasso/tempo;
- loop por seleção;
- velocidade sem alterar pitch, dentro de limites aprovados;
- metrônomo;
- contagem de entrada;
- volume por camada/parte;
- troca A/B preservando posição;
- retorno ao início da frase.

## Semântica

A reprodução usa pitch de concerto. A partitura pode mostrar pitch escrito. A UI deve identificar ambos quando a diferença for relevante.

O cursor visual usa `PlaybackMapDTO`, não estimativa baseada apenas na duração total do áudio.

## Repetições e saltos

Antes de habilitar score following, o backend resolve:

- repeats;
- first/second endings;
- D.C., D.S., segno, coda e fine;
- pickups;
- fermatas e cadenzas conforme política;
- mudanças de andamento e compasso;
- swing/humanização apenas como camada de performance.

## Falhas e fallback

- se o mapa for parcial, desabilitar cursor nas regiões afetadas;
- se amostra instrumental falhar, usar fallback identificado, não fingir timbre real;
- se `AudioContext` exigir gesto, mostrar ação explícita;
- se áudio e partitura divergirem, interromper A/B e registrar erro;
- não baixar samples de terceiros sem licença e política de cache.

## Acessibilidade

- todos os controles possuem nome e atalho documentado;
- foco não é movido a cada nota;
- cursor visual tem equivalente textual opcional;
- metrônomo visual respeita reduced motion;
- volume inicial e picos passam por normalização segura;
- não reproduzir automaticamente ao abrir página.

## Critérios de aceite

- alternância A/B mantém posição dentro da tolerância aprovada;
- pitch soante coincide com o grafo canônico;
- repeats e endings passam no corpus de reprodução;
- áudio não altera o nível de garantia do MusicXML;
- autoplay não é requisito de fluxo.
