# Testes de motion, acessibilidade e performance

> Status: canônico para validação das animações. Revisão: 2026-07-20.

## Objetivo

Garantir que Motion, GSAP, CSS e View Transitions não introduzam regressão funcional, de acessibilidade, memória, bundle ou estabilidade visual.

## Testes unitários e de componente

### Motion for React

- entrada/saída corresponde ao estado React;
- `AnimatePresence` não remove conteúdo antes da ação necessária;
- `layoutId` não gera IDs duplicados;
- reduced motion substitui deslocamento por crossfade/troca imediata;
- callbacks não alteram estado após unmount;
- gestos possuem alternativa por teclado.

### GSAP

- timeline é criada uma vez em Strict Mode;
- `useGSAP` reverte estilos/listeners ao desmontar;
- mudança de dependência não acumula timelines;
- navegação antes do fim encerra a cena;
- `document.hidden` pausa loop;
- estado terminal mata a timeline de processamento;
- fallback estático aparece quando o chunk falha;
- nenhuma seleção escapa do root da cena.

## Testes de acessibilidade

Executar variantes:

```text
prefers-reduced-motion: reduce
forced-colors: active
zoom 200%
teclado
leitor de tela
mobile/touch
```

Verificar:

- conteúdo não fica invisível aguardando animação;
- foco não é movido por transform;
- região removida devolve foco corretamente;
- status possui texto/aria-live independente do efeito;
- animação de tinta tem descrição textual equivalente;
- pausa/replay, quando existir, é acessível;
- nenhum som automático.

## E2E

Cenários mínimos:

1. primeira entrada reproduz intro uma vez;
2. retorno à Home na mesma sessão não repete;
3. reduced motion mostra composição estática;
4. CTA funciona durante a intro;
5. navegação interrompe a cena sem erro de console;
6. job ativo inicia loop discreto;
7. `completed` encerra loop e revela resultado;
8. `failed` encerra loop e mostra erro;
9. aba oculta pausa atividade;
10. refresh recupera estado sem reproduzir cena indevida.

## Visual regression

Para snapshots determinísticos:

- aplicar configuração global de reduced motion ou desabilitar animações;
- aguardar fontes e layout estável;
- congelar dados e timestamps;
- capturar estados inicial, intermediário aprovado e final somente quando necessário;
- não depender de partículas aleatórias;
- usar seed fixo em qualquer variação visual.

Snapshots não substituem revisão em movimento.

## Performance

### Bundle

Medir por rota:

- Home com cena;
- Home após remover/desabilitar cena;
- Transpor sem preview;
- Resultado;
- Histórico.

Gates:

- GSAP não aparece em rota sem cena;
- Anime.js e React Spring não aparecem no lockfile/bundle do Core;
- Motion não puxa feature premium/não usada;
- aumento de bundle é registrado e justificado.

### Runtime

Durante a cena:

- observar long tasks;
- verificar FPS/frame time em dispositivo intermediário;
- procurar layout/recalculate style excessivo;
- medir CPU após timeline encerrar;
- confirmar ausência de timers/RAF ativos após unmount;
- verificar memória após repetir navegação várias vezes.

### Rede e carregamento

- chunk da cena não bloqueia LCP textual/CTA;
- fallback não causa CLS;
- import dinâmico não produz flash vazio;
- assets SVG/fontes possuem cache e dimensões previsíveis.

## Teste de degradação

Simular:

- JavaScript desabilitado na Home pública;
- falha do chunk GSAP;
- browser sem View Transition API;
- baixa potência/reduced motion;
- resize/orientação durante cena;
- conexão lenta.

O produto deve permanecer compreensível e operável.

## Observabilidade

Registrar somente eventos técnicos agregáveis:

```text
motion_intro_started
motion_intro_completed
motion_intro_skipped_reduced
motion_scene_load_failed
```

Não incluir nome de arquivo, MusicXML, instrumento selecionado ou identificador sensível sem finalidade e aprovação de analytics.

## Gate

Uma animação só é aprovada quando:

- testes funcionais e reduced motion passam;
- não há listener/timeline vazando;
- não bloqueia interação;
- bundle por rota está dentro do baseline aprovado;
- fallback estático foi testado;
- revisão humana confirma que o movimento esclarece o domínio.
