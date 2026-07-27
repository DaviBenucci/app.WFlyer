# Documentação técnica do W_Flyer

> Status: canônica. Fase 0 consolidada em 2026-07-27; código funcional ainda não iniciado.

Esta pasta é a fonte normativa para a implementação do W_Flyer. O produto deve transformar material musical com rastreabilidade, explicar o que mudou, interromper o fluxo quando não puder provar uma decisão e manter o músico no controle de inferências e criações.


## Escolha a explicação adequada ao público

- `00-visao-geral/20-explicacao-completa-nao-tecnica.md`: visão integral em linguagem acessível para músicos, gestores, parceiros e leitores sem formação em programação;
- `00-visao-geral/21-visao-tecnica-completa.md`: síntese integral para desenvolvedores e arquitetos, com terminologia técnica, limites de módulo e contratos do sistema.

A primeira explica **o produto e sua utilização**. A segunda explica **como o produto será construído e comprovado**.

## Compromisso realista

A documentação antecipa classes conhecidas e plausíveis de falha, mas nenhuma especificação consegue enumerar todo defeito futuro. Por isso, o projeto combina:

```text
pre-mortem conhecido
+ fail-closed
+ invariantes independentes
+ corpus de regressão
+ observabilidade
+ política para falhas desconhecidas
```

Não é permitido converter ausência de erro detectado em certeza musical. A palavra **verificado** depende dos gates e do nível de garantia definidos pelo backend.

## Ordem de leitura obrigatória antes do primeiro código

1. `00-visao-geral/08-hierarquia-documental.md`
2. `00-visao-geral/05-escopo-mvp-app-wflyer.md`
3. `00-visao-geral/06-matriz-suporte-mvp.md`
4. `00-visao-geral/13-visao-critica-musical-produto.md`
5. `00-visao-geral/14-registro-riscos-pre-mortem.md`
6. `00-visao-geral/15-principios-controle-humano.md`
7. `qa/19-matriz-falhas-pre-mortem.md`
8. `100-implementacao/matriz-rastreabilidade-requisitos.md`
9. `100-implementacao/guia-codex-app-wflyer.md`

## Leitura do MVP Core

1. `music/01-modelo-transposicao.md`
2. `music/02-musicxml-canonico.md`
3. `music/05-invariantes-validacao.md`
4. `music/06-taxonomia-transformacoes-musicais.md`
5. `backend/19-confiabilidade-musical-fail-closed.md`
6. `backend/20-manifesto-prova-reprodutibilidade.md`
7. `backend/03-endpoints-api.md`
8. `backend/04-modelagem-banco.md`
9. `backend/16-maquina-estados.md`
10. `security/02-checklist-seguranca.md`
11. `qa/01-estrategia-testes.md`
12. `100-implementacao/criterios-aceite-mvp.md`

## Leitura do frontend

1. `frontend/00-direcao-visual-wflyer.md`
2. `frontend/05-design-system.md`
3. `frontend/18-pacote-referencias-visuais.md`
4. `frontend/19-contrato-fidelidade-visual-ia.md`
5. `frontend/20-matriz-estados-interface.md`
6. `frontend/15-arquitetura-motion-e-bibliotecas.md`
7. `frontend/16-animacao-assinatura-tinta-transposicao.md`
8. `design-reference/README.md`
9. `design-reference/reference-manifest.yaml`

## Trilhas avançadas

Extração de melodia, adaptação idiomática, harmonização, áudio, modo de ensaio, score/partes, ensemble e colaboração são capacidades separadas e desabilitadas até seus gates. A visão e as dependências estão em:

- `100-implementacao/plano-evolucao-avancada.md`;
- `music/07-extracao-melodia-polifonica.md` a `music/19-arranjo-ensemble-orquestracao.md`;
- `backend/21-orquestracao-analise-musical.md` a `backend/27-colaboracao-concorrencia.md`;
- `qa/10-gates-confiabilidade-avancada.md` a `qa/20-gate-conselho-musical-release.md`.

## Precedência

- Regras de domínio, segurança, acessibilidade e contratos vencem qualquer exemplo visual.
- Para composição visual, prevalece a ordem declarada em `design-reference/reference-manifest.yaml`.
- Protótipos em `design-reference/prototypes/` são referências internas originais; não são código de produção.
- Referências externas servem para estudo de padrões, nunca para copiar marca, código, assets ou layout integral.
- Decisão pendente não pode ser resolvida silenciosamente por IA.

## Identidade do projeto

- Produto: **W_Flyer**.
- Slug técnico: `wflyer`.
- Serviços e pacotes: minúsculos, sem caracteres especiais.
- Transposição, OMR, extração, redução, adaptação, harmonização e arranjo não são sinônimos.

## Pacote crítico pré-implementação

Antes de iniciar qualquer capacidade, a equipe e a IA devem ler também:

1. `00-visao-geral/13-visao-critica-musical-produto.md`;
2. `00-visao-geral/14-registro-riscos-pre-mortem.md`;
3. `qa/19-matriz-falhas-pre-mortem.md`;
4. `riscos/failure-mode-catalog.yaml`;
5. `implementacao/09-protocolo-preflight-capacidade.md`;
6. `100-implementacao/matriz-rastreabilidade-requisitos.md`;
7. `design-reference/reference-manifest.yaml` para qualquer alteração de frontend.

A documentação não afirma que uma lista finita consegue antecipar literalmente todo defeito futuro. Ela combina:

```text
catálogo amplo de falhas conhecidas
+ resposta fail-closed para falha desconhecida
+ preflight obrigatório por capacidade
+ rastreabilidade requisito → risco → contrato → teste → evidência
+ incorporação de todo incidente como regressão
```

## Referências visuais executáveis

`design-reference/` contém specifications YAML, protótipos HTML autorais e baselines PNG gerados a partir desses protótipos. Eles definem composição, hierarquia, estados e proibições. Não são código de produção nem autorização para copiar produtos externos.

A precedência visual é:

```text
segurança, domínio e acessibilidade
> exemplo interno executável
> story aprovada
> specification interna
> baseline visual interno
> inspiração externa
```

## Limite entre Core e capacidades avançadas

Musical Diff, análise polifônica, adaptação idiomática, harmonização, áudio sincronizado, modo de ensaio, score/partes e colaboração estão arquitetados, mas permanecem desabilitados até cumprir seus gates. A presença de documentação ou protótipo não autoriza ativação em produção.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Toolchain de agentes e qualidade

Antes de qualquer implementação, ler nesta ordem:

1. `implementacao/11-arquitetura-ferramentas-agentes.md`;
2. `implementacao/12-bootstrap-toolchain.md`;
3. `implementacao/13-openspec-especificacoes.md`;
4. `implementacao/14-graphify-governanca.md`;
5. `implementacao/15-serena-context7-mcp.md`;
6. `implementacao/16-nx-monorepo-cache.md`;
7. `implementacao/21-fluxo-operacional-ia.md`;
8. `implementacao/toolchain-manifest.yaml`.

A ordem operacional é:

```text
OpenSpec → Graphify → Serena → Context7 quando necessário
→ implementação pequena → Nx affected → gates por risco
→ documentação/logs/grafo
```

Ferramentas opcionais estão bloqueadas até o spike de `implementacao/20-ferramentas-opcionais-spikes.md`.
