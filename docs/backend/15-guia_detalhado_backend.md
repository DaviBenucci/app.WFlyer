# Backend — guia de navegação canônico

> Revisão: 2026-07-20.

Este arquivo evita duplicar requisitos. A implementação deve consultar, nesta ordem:

1. `01-visao-geral.md`
2. `02-arquitetura-api-worker.md`
3. `03-endpoints-api.md`
4. `04-modelagem-banco.md`
5. `16-maquina-estados.md`
6. `17-sessao-anonima-autorizacao.md`
7. `05-pipeline-processamento.md`
8. `06-storage-e-retencao.md`
9. `07-filas-e-workers.md`
10. `08-seguranca-backend.md`
11. `18-taxonomia-erros.md`
12. `09-observabilidade.md`
13. `13-estrutura-pastas.md`
14. `../music/01-modelo-transposicao.md`
15. `../music/02-musicxml-canonico.md`
16. `../qa/01-estrategia-testes.md`

## Regra de prevalência

Em divergência, valem a hierarquia de `../00-visao-geral/08-hierarquia-documental.md` e o documento mais específico/canônico. Não resolver conflito inventando um terceiro comportamento.

## Fora do Core

Admin, push e compartilhamento permanecem fora do MVP. Seus documentos não autorizam criar rotas, tabelas ou navegação nesta fase.

## Regra adicional para capacidades musicais avançadas

Antes de codificar OMR complexo, extração, harmonização, arranjo ou watermark, ler:

- `../music/06-taxonomia-transformacoes-musicais.md`;
- `../music/07-extracao-melodia-polifonica.md`;
- `../music/08-motor-harmonizacao-arranjo.md`;
- `19-confiabilidade-musical-fail-closed.md`;
- `20-manifesto-prova-reprodutibilidade.md`;
- `../qa/10-gates-confiabilidade-avancada.md`.

É proibido criar um “algoritmo inteligente” diretamente no controller ou em uma task Celery sem domínio, manifest, invariantes e corpus.
