# Estratégia de testes

> Status: canônico. Revisão: 2026-07-20.

## Princípio

O W_Flyer precisa provar quatro propriedades independentes:

1. correção musical;
2. segurança/autorização de documentos;
3. confiabilidade assíncrona;
4. usabilidade/acessibilidade do fluxo.

Cobertura de linhas não substitui nenhuma delas.

## Pirâmide

```text
unit/property: intervalos, catálogo, normalização e estados
component/integration: API, banco, storage, fila, frontend
contract: OpenAPI/cliente/DTOs
golden/semantic: MusicXML e resultados esperados
security corpus: XML/MXL/PDF/IDOR/CSRF/DoS
E2E: fluxos reais do usuário
performance/soak: limites antes de produção/PDF
```

## Gates do Core

- todos os presets e pares preservam altura de concerto;
- fixtures Core passam no comparador semântico;
- parser rejeita corpus hostil sem rede/leitura local/exaustão;
- A não acessa recursos de B;
- reentrega/retry não duplica job/artefato;
- downloads e purge respeitam retenção;
- cliente OpenAPI não diverge;
- fluxo E2E MusicXML funciona em desktop/mobile/teclado;
- nenhum warning/erro interno vaza.

## Ambientes

- banco/Redis/storage reais em integração via containers;
- engines externas fixadas por versão;
- relógio controlável para expiração;
- seed/corpus versionado;
- sem depender de rede pública nos testes.

## Evidência

Cada execução registra comando, commit, ambiente, versões, fixtures, resultado e falhas em `../logs/TEST_LOG.md`. Teste não executado deve ter motivo; não pode ser declarado como aprovado.

## PDF/OMR

Possui gate separado com corpus representativo, métricas definidas antes da avaliação, sandbox, performance e revisão de falsos positivos/negativos. Aprovar Core não aprova PDF.

## Quinta propriedade: proveniência e decisão explícita

O W_Flyer também precisa provar:

5. nenhuma nota é descartada ou criada sem operação, proveniência e regra explícitas;
6. conteúdo criativo só é publicado após restrições e escolha do usuário;
7. watermark/prova não alteram a música.

Consultar `10-gates-confiabilidade-avancada.md`.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Dimensões adicionais

A pirâmide deve cobrir quatro produtos diferentes:

```text
semântica musical
artefato visual/áudio
sistema distribuído
experiência e decisão humana
```

Uma suíte verde em apenas uma dimensão não aprova a capability.

## Rastreabilidade

Todo teste crítico referencia ao menos um `REQ-*`, `RISK-*` ou `PM-*`. Todo incidente crítico adiciona fixture e teste de regressão. Métrica sem corpus versionado não vale como gate.

## Testes metamórficos

Exemplos:

- A→B→A preserva semântica suportada;
- transpor em duas etapas equivale ao intervalo composto quando a política é igual;
- mudar apenas layout não altera Musical Diff semântico;
- gerar score e extrair partes mantém os mesmos eventos;
- áudio A/B usa alturas de concerto equivalentes em transposição;
- reordenar metadados XML não muda o resultado.

## Camadas críticas adicionadas

Além dos testes existentes, toda capability avançada exige:

```text
properties/invariantes
+ corpus estratificado
+ metamorphic tests
+ differential checker quando possível
+ fault injection
+ human review cega
+ regressão por incidente
+ rollout shadow/canary
```

Cobertura de linhas não substitui cobertura de modos de falha. A matriz de `PM-*` é uma dimensão obrigatória do relatório de teste.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Frameworks normativos por camada

```text
TypeScript unit/component     → Vitest
Browser component             → Vitest Browser + Storybook
Network scenarios             → MSW
E2E/visual/accessibility      → Playwright
Python unit/integration       → pytest
Property/metamorphic          → Hypothesis
Infra real isolada            → Testcontainers
Mutation TypeScript opcional  → StrykerJS
Mutation Python opcional      → mutmut
Task selection/cache          → Nx
```

Detalhes de instalação, uso e proibições estão em `../implementacao/18-frontend-toolchain-testes.md`, `../implementacao/19-backend-toolchain-testes.md` e `../implementacao/20-ferramentas-opcionais-spikes.md`.
