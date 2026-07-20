# Gates de confiabilidade musical avançada

> Status: canônico para OMR, extração de melodia, harmonização e watermark.

## Regra

Cada capacidade possui gate independente. Aprovar transposição não aprova OMR, extração, harmonização ou arranjo.

## Métricas de decisão e cobertura

Toda capability inferencial deve publicar conjuntamente:

```text
verified_false_positive_rate
review_required_rate
rejection_rate
automatic_coverage
```

No corpus congelado de release, `verified_false_positive_rate` tem alvo rígido `0`. Isso não prova correção universal; comprova que, naquele corpus e versão, nenhum caso errado foi promovido indevidamente a “verificado”. Cobertura automática nunca pode ser aumentada relaxando o gate sem nova avaliação e aprovação.

## Transposição determinística

Obrigatório:

- zero violação de altura de concerto;
- zero perda/duplicação de eventos no perfil;
- propriedades A->B->A e A->B->C equivalentes;
- ritmo, vozes, ties, tuplets e mudanças preservados;
- verificador independente aprovado;
- mutação proposital do motor é detectada pela suíte.

## OMR

Medir separadamente:

- notas/pitches;
- onset e duração;
- armaduras, claves e compassos;
- vozes e acordes;
- medidas/pautas/partes;
- taxa de páginas ou regiões que exigem revisão;
- calibração de alertas de baixa confiabilidade.

Um agregado único não pode esconder erro crítico de pitch ou ritmo.

## Extração de melodia

No corpus rotulado:

- precision/recall/F1 de eventos;
- acerto por onset e duração;
- continuidade por segmento/frase;
- taxa de ambiguidade corretamente bloqueada;
- taxa de publicação automática incorreta;
- desempenho por textura: acordes, arpejo, vozes cruzadas, contracanto e teclado.

O gate deve privilegiar baixa taxa de falso “sem ambiguidade”. Quando o modelo não sabe, deve parar.

## Harmonização

Automático:

- melodia bloqueada preservada em 100%;
- 100% das restrições rígidas;
- saída parseável, temporalmente válida e tocável;
- provenance de todas as notas geradas;
- reprodutibilidade por versão/seed;
- diversidade mínima entre variantes sem simples mudança cosmética;
- diff identifica cada acorde/voz acrescentado, removido ou substituído;
- perfil de fidelidade bloqueia alterações que não foram autorizadas.

Humano:

- painel de músicos por estilo;
- critérios separados: coerência, condução de vozes, tocabilidade, respeito ao perfil e utilidade;
- avaliações e divergências registradas;
- nenhum resultado humano isolado substitui restrições automáticas.

## Watermark e proveniência

- marca legível sem interferir na leitura;
- token consistente em todas as páginas;
- tentativa de remover uma instância não elimina todas as camadas no conjunto de testes;
- hash/assinatura detectam modificação;
- crop e reimpressão preservam ao menos identificação prevista no perfil de teste;
- sem alteração de notas/layout semântico;
- sem PII;
- sem remoção de créditos da fonte ou falsa alegação de copyright do W_Flyer.

## Corpus

Separar:

```text
train_or_tuning
validation
frozen_release_test
adversarial
human_review
```

O conjunto de release não pode ser usado para ajustar threshold. Alteração de threshold, engine, catálogo ou política reabre o gate.

## Evidência de aceite

Cada release avançada registra:

- commit e imagens;
- versões e configurações;
- hashes do corpus;
- métricas brutas e por classe;
- falhas conhecidas;
- aprovação técnica e de músico responsável;
- decisão explícita de capability/rollout.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Gates adicionais

### Musical Diff

- cobertura de eventos conforme operação;
- zero relações proibidas;
- classificação musical versus layout validada;
- navegação e explicação revisadas.

### Tocabilidade

- hard constraints sem falso negativo conhecido no corpus release-hidden;
- `UNKNOWN` calibrado e não tratado como sucesso;
- revisão por instrumentista;
- andamento e contexto incluídos.

### Score/partes e engraving

- consistência semântica bidirecional;
- marcas/compassos/transposição consistentes;
- zero colisão bloqueante;
- impressão e page turns revisados.

### Áudio/ensaio

- pitch de concerto correto;
- mapa de repetições/voltas correto;
- tolerância de sincronização definida antes do teste;
- loudness comparável no A/B;
- licenças de samples aprovadas.

### Frontend

- reference manifest/schema válido;
- estados críticos cobertos;
- diff visual revisado por humano;
- WCAG e reduced motion testados;
- nenhum capability fictício.

## Gate transversal de pre-mortem

Para cada capability:

- preflight aprovado;
- todos os `PM-*` aplicáveis mapeados;
- `critical/high` evidenciados ou risco residual aceito;
- unknown failure fail-closed comprovado;
- fault injection em boundaries;
- métricas estratificadas;
- feature flag default off;
- rollback ensaiado;
- MDRs aprovados;
- conselho musical aprova o estrato;
- nenhuma alegação de qualidade excede a evidência.
