# Hierarquia e governança documental

> Status: canônico. Revisão: 2026-07-20.

## Precedência

Em caso de conflito, prevalece a ordem abaixo:

1. escopo e matriz de suporte;
2. ADRs e decisões aceitas;
3. especificações do modelo musical;
4. contratos de API, modelo de dados e máquinas de estado;
5. segurança e privacidade;
6. critérios de aceite e QA;
7. direção visual, design system e acessibilidade do frontend;
8. features e páginas;
9. guias de implementação;
10. exemplos e textos de UX;
11. logs históricos.

## Documentos canônicos

São canônicos:

- `01-decisoes-arquiteturais.md`;
- `05-escopo-mvp-app-wflyer.md`;
- `06-matriz-suporte-mvp.md`;
- todos os arquivos de `music/`;
- `../backend/03-endpoints-api.md`;
- `../backend/04-modelagem-banco.md`;
- `../backend/16-maquina-estados.md`;
- `../backend/17-sessao-anonima-autorizacao.md`;
- `../security/02-checklist-seguranca.md`;
- `../qa/01-estrategia-testes.md`;
- `../frontend/00-direcao-visual-wflyer.md`;
- `../frontend/05-design-system.md`;
- `../frontend/06-acessibilidade.md`;
- `../frontend/09-guia_detalhado_frontend.md`;
- `../100-implementacao/criterios-aceite-mvp.md`.

## Regras para a IA

- Não inferir requisito a partir de log histórico.
- Não escolher item marcado como pendente.
- Não alterar contrato público sem atualizar OpenAPI, frontend, testes e changelog.
- Não implementar capacidade fora da matriz por estar disponível em uma biblioteca.
- Ao encontrar contradição, parar a fase, registrar a divergência e corrigir a documentação canônica antes do código.
- Exemplos não substituem regras gerais.

## Estado dos documentos antigos

Arquivos com título “substituído” permanecem apenas como ponte histórica. Eles não devem ser usados como fonte normativa.
