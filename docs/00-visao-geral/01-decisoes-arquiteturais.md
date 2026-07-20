# Decisões arquiteturais principais

> Status: canônico. Revisão: 2026-07-20.

## ADR-001 — Projeto orientado por documentação canônica

A implementação deve seguir a hierarquia definida em `08-hierarquia-documental.md`. Código antigo e protótipos são referências, não fontes normativas.

## ADR-002 — MVP sem conta, mas com sessão anônima autorizada

O usuário não precisa criar login. Isso não torna jobs e arquivos públicos. A API deve criar uma sessão anônima opaca, persistida em cookie `HttpOnly`, e validar a propriedade de uploads, jobs e artefatos em todas as operações.

Consequência: UUID é identificador, não autorização. O modelo completo está em `../backend/17-sessao-anonima-autorizacao.md`.

## ADR-003 — Núcleo MusicXML antes de PDF

O primeiro marco executável aceita MusicXML não comprimido, normaliza a entrada, transpõe e devolve MusicXML. PDF de entrada só pode ser habilitado após o adaptador OMR cumprir o gate de qualidade e segurança.

```text
MVP Core: MusicXML -> normalização -> transposição -> validação -> MusicXML
Extensão PDF: PDF -> rasterização -> OMR -> MusicXML bruto -> normalização -> fluxo do Core
```

Consequência: a API não deve aceitar PDF em um ambiente no qual a capacidade `pdf_omr` esteja desabilitada.

## ADR-004 — MusicXML normalizado como representação canônica

O original é imutável. O sistema mantém artefatos distintos para entrada, MusicXML bruto, MusicXML normalizado, MusicXML transposto e renderizações.

## ADR-005 — Modelo de transposição intervalar completo

A transposição não pode ser representada apenas por um inteiro de semitons. Cada instrumento deve declarar:

```text
written_to_concert_diatonic
written_to_concert_chromatic
written_to_concert_octave
```

O intervalo de saída é a diferença vetorial entre origem e destino. Isso preserva grafia diatônica, enarmonia e instrumentos que transpõem oitava.

## ADR-006 — Uma parte e uma pauta por job no MVP Core

O MVP Core processa uma única parte instrumental e uma única pauta por job. Scores multiparte, piano de duas pautas, tablatura, percussão não afinada e mudanças de instrumento dentro da parte ficam fora do gate inicial.

Consequência: arquivos fora desse perfil devem ser rejeitados com erro específico, não processados parcialmente em silêncio.

## ADR-007 — Processamento assíncrono e banco como fonte de verdade

A API apenas recebe, valida, persiste e agenda. Workers executam parsing, OMR, transposição, validação e renderização. O PostgreSQL é a fonte de verdade para estado; o backend de resultados da fila não substitui o banco.

## ADR-008 — Celery e Redis como fila inicial

A fila inicial usa Celery com Redis, versões fixadas em lockfile. O payload contém somente `job_id` e `correlation_id`; o worker cria a tentativa após adquirir o job. Tarefas devem ser idempotentes e serializadas em JSON.

## ADR-009 — Backend Python é a fonte da regra musical

A regra musical canônica reside no backend Python. O frontend recebe o intervalo calculado pela API apenas para exibição. Não existe compartilhamento de código executável de música entre TypeScript e Python.

Consequência: tipos frontend devem ser gerados ou validados a partir do OpenAPI; `packages/shared` não contém o motor musical.

## ADR-010 — Storage privado e retenção separada do estado de processamento

Arquivos ficam em storage privado. O estado de processamento e o estado de retenção são campos diferentes. Um job pode estar `completed` e ter retenção `expired` ou `purged`.

## ADR-011 — Confiança interna, aviso público categórico

Scores numéricos de OMR permanecem internos. O usuário deve receber avisos categóricos acionáveis, como `OMR_REVIEW_RECOMMENDED`, `ENHARMONIC_SIMPLIFICATION` ou `TARGET_CLEF_REVIEW_RECOMMENDED`. Ocultar toda incerteza é proibido.

## ADR-012 — Ferramentas externas atrás de adapters e sandbox

OMR e renderização são adapters substituíveis. Cada subprocesso roda sem shell, sem rede, com usuário não privilegiado, limites de CPU/memória/tempo e diretório temporário isolado.

## ADR-013 — Fidelidade semântica antes de fidelidade visual

O MVP garante correção de alturas, ritmos, armaduras, vozes e metadados de transposição dentro da matriz suportada. Preservar exatamente a paginação e o layout original é melhor esforço, não critério do Core.

## ADR-014 — Escopo futuro não bloqueia o Core

Login, cobrança, biblioteca em nuvem, compartilhamento público, editor visual completo, aplicativo nativo, push e Spotify permanecem fora do MVP Core.


## ADR-015 — Frontend como workspace musical, não dashboard

Páginas públicas usam header editorial; Transpor e Resultado usam StudioShell com canvas e inspector; Histórico e Configurações usam UtilityShell. Sidebar larga, cards de métricas e dashboard genérico não são padrão do Core.

## ADR-016 — Design system próprio sobre primitives headless

Bibliotecas como shadcn/ui e Base UI podem fornecer comportamento acessível, mas tokens, composição, componentes de produto e microcopy são próprios do W_Flyer. O tema padrão de uma biblioteca não é entrega final.

## ADR-017 — Identidade por domínio, não por efeitos

A assinatura visual combina papel/tinta, trajetória de transposição e ritmo editorial. Motion é progressivo e funcional; partículas, glow excessivo, glassmorphism indiscriminado e card soup são antipadrões.

## ADR-018 — Storybook e regressão visual como gates

Componentes do produto precisam de stories, testes de interação, acessibilidade automatizada e regressão visual revisada antes do aceite do frontend.

## ADR-019 — Motion declarativo e cena GSAP isolada

CSS nativo resolve microestados simples. Motion for React é a engine padrão para presença, layout, gestos e transições ligadas ao estado React. GSAP com `@gsap/react` é carregado sob demanda e restrito à animação-assinatura SVG e timelines explicitamente aprovadas.

Anime.js e React Spring não entram no MVP Core. Cada nó visual possui uma única engine proprietária.

## ADR-020 — A animação de tinta não é o motor musical

A cena `Ink Transfer` usa SVG determinístico e exemplo musical validado para explicar transposição. Durante jobs, o movimento é apenas metáfora acompanhada do estágio real. Notas do arquivo do usuário só poderão ser animadas quando o renderer fornecer mapeamento estável entre eventos musicais e geometria.
