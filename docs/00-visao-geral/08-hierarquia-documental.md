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

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Precedência específica do frontend

Depois dos contratos de domínio, segurança e acessibilidade, a composição visual segue:

```text
referência executável interna
> story aprovada
> especificação machine-readable
> screenshot golden interno
> descrição textual
> inspiração externa
```

A fonte operacional é `../design-reference/reference-manifest.yaml`. Um screenshot não pode contradizer estado, erro, foco, capacidade ou microcopy canônica.

## Precedência específica de resultados musicais

```text
invariantes determinísticos
> decisão humana explícita
> regras de perfil aprovadas
> ranking/heurística
> sugestão de modelo
```

Um modelo não pode superar uma restrição rígida nem reinterpretar decisão bloqueada do usuário.

## Regra para documentos futuros

Todo novo documento deve declarar:

- status (`canônico`, `proposta`, `histórico` ou `referência`);
- capability/gate ao qual pertence;
- documentos que pode complementar, mas não contradizer;
- decisão pendente quando faltar evidência.

## Contratos especializados adicionados

Para seu domínio específico, os seguintes artefatos são vinculantes:

```text
riscos/failure-mode-catalog.yaml
  → modos de falha, resposta segura e teste planejado

design-reference/reference-manifest.yaml
  → precedência e referências visuais

100-implementacao/matriz-rastreabilidade-requisitos.md
  → requisito, risco, teste e evidência

Musical Decision Record aprovado
  → decisão musical que não pode ser inferida apenas por arquitetura
```

Esses artefatos não podem contrariar segurança, escopo e invariantes canônicos. Quando houver conflito, a implementação deve pausar e abrir decisão; não escolher silenciosamente o documento mais conveniente.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Relação entre documentação canônica e OpenSpec

- documentação canônica descreve o comportamento vigente;
- `openspec/changes/` descreve uma alteração ainda em execução;
- uma mudança aprovada não pode contradizer segurança/domínio sem ADR explícita;
- ao concluir, o comportamento vigente e os documentos canônicos são atualizados;
- Graphify, Serena e Context7 são índices/ferramentas e nunca possuem precedência normativa;
- `implementacao/toolchain-manifest.yaml` governa instalação e uso das ferramentas, sem revogar requisitos do produto.
