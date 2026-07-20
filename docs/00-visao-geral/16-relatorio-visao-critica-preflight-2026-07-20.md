# Relatório de expansão crítica e preflight — 2026-07-20

> Status: relatório documental. Não é evidência de software implementado.

## Objetivo

Incorporar à documentação a visão de maestro, arranjador, instrumentista, designer de produto, backend, segurança e QA antes do início do código. A revisão procura impedir que decisões difíceis sejam descobertas somente durante a implementação.

## O que foi acrescentado

### Produto e música

- tese do produto centrada em transformar, explicar, verificar, adaptar e devolver controle ao músico;
- separação entre transposição, extração, redução, adaptação, harmonização e arranjo;
- Musical Diff e proveniência por evento;
- análise de forma, frase, cadência e tensão relativa;
- perfis instrumentais práticos, tocabilidade e adaptação idiomática;
- score/partes a partir de grafo único;
- áudio A/B, mapa de reprodução e modo de ensaio;
- ensemble, colaboração, revisões e autoridade humana.

### Frontend

- manifesto de referências visuais;
- specifications YAML, protótipos HTML e baselines PNG próprios;
- exemplos de happy path, ambiguidade, incompatibilidade e falha transitória;
- regra para impedir composição genérica ou cópia de produto externo;
- estados negativos, recuperação, mobile, zoom e reduced motion.

### Backend e confiabilidade

- DAG de operações e revisões imutáveis;
- playback manifest;
- publicação atômica de score/partes;
- feature flags e rollout estratificado;
- governança de modelos/solvers e conteúdo não confiável;
- classificador de falhas, retry e incidentes.

### Riscos e QA

- 155 modos de falha conhecidos com detecção e resposta segura;
- catálogo YAML validável;
- política fail-closed para falhas desconhecidas;
- preflight obrigatório;
- Musical Decision Record;
- fault injection, benchmarks estratificados, teste cego e conselho musical.

## Limite honesto

Nenhuma documentação consegue antecipar literalmente todo bug, repertório, notação ou comportamento de terceiros. O pacote reduz esse risco por quatro mecanismos:

1. catálogo amplo e vivo;
2. invariantes e verificadores independentes;
3. falha desconhecida sem publicação silenciosa;
4. todo incidente vira risco, fixture e teste.

Também não existe prova de que OMR, extração, harmonização, adaptação ou engraving funcionem em produção. Esses módulos continuam desabilitados até implementação e gates.

## Estado das referências visuais

Os protótipos e PNGs definem uma direção interna original e estados importantes. A composição está documentada; o pixel baseline ainda exige revisão humana do produto e depois deve ser substituído/confirmado pelo Storybook da implementação real.

## Próximo gate antes de código

- nomear owners dos riscos críticos;
- aprovar o preflight do Core;
- transformar `TBD-PM-*` aplicáveis em IDs reais de teste;
- aprovar os baselines visuais do Core;
- congelar corpus/licença do Core;
- resolver decisões pendentes que bloqueiam migrations e contratos;
- manter todas as capabilities avançadas `off`.
