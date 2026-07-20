# Relatório de revisão técnica — 2026-07-20

## Conclusão executiva

A documentação original possuía uma direção de produto coerente, mas ainda não era suficientemente determinística para uma implementação autônoma por IA. Havia ambiguidades de escopo, um modelo musical incompleto, contratos sem autorização formal e critérios de aceite que poderiam aprovar apenas documentação.

A revisão não reinventa o produto. Ela transforma os pontos imaturos em:

- regras canônicas;
- contratos verificáveis;
- máquinas de estado;
- gates de segurança e qualidade;
- decisões explicitamente pendentes.

O **MVP Core MusicXML** está documentalmente apto a orientar a implementação por fases. PDF/OMR, MXL e renderização PDF continuam condicionados aos gates próprios.

## Inventário da revisão

| Métrica | Resultado |
|---|---:|
| Arquivos na documentação original | 74 |
| Arquivos na documentação revisada | 91 |
| Arquivos alterados | 67 |
| Arquivos adicionados | 17 |
| Arquivos preservados sem alteração | 7 |
| Arquivos removidos | 0 |

## Correções críticas aplicadas

| Área | Problema anterior | Correção aplicada |
|---|---|---|
| Regra musical | Um único inteiro de semitons não preservava grafia nem oitavas. | Intervalo com componentes diatônico, cromático e de oitava; total derivado. |
| Catálogo | Violão estava com deslocamento total incorreto; sax tenor/barítono não separavam a parcela de oitava. | Presets corrigidos, versionados e cobertos por property tests. |
| Invariante | Não havia uma condição matemática obrigatória para validar o resultado. | Altura de concerto deve permanecer invariável para cada evento afinado. |
| MusicXML | Entrada, normalização e resultado eram tratados sem uma cadeia canônica de artefatos. | `input_original` → `raw_musicxml` → `normalized_musicxml` → `transposed_musicxml`. |
| Escopo | PDF aparecia simultaneamente como requisito obrigatório e item futuro. | Core MusicXML; PDF/OMR em trilha independente com capability e gate. |
| Estrutura musical | Multiparte/multipauta eram mencionadas sem fluxo de seleção ou regra de rejeição. | Uma parte e uma pauta por job no Core; demais estruturas falham explicitamente. |
| OMR | Pipeline, qualidade, isolamento e responsabilidade pelo erro não estavam definidos. | Adapter, sandbox, corpus, métricas pré-definidas e gate de ativação. |
| Autorização | UUID era implicitamente tratado como suficiente para acesso. | Sessão anônima, propriedade por `session_id`, CSRF e resposta neutra contra enumeração. |
| Sessão e retenção | A sessão poderia expirar antes dos artefatos anunciados. | Renovação deslizante e coerência entre cookie, sessão e janela real de download. |
| Estados | Upload e job compartilhavam conceitos; expiração se misturava ao processamento. | `UploadStatus`, `JobStatus`, `ProcessingStage` e `RetentionStatus` separados. |
| Jobs | Não havia contrato completo para reentrega, tentativas e publicação consistente. | Outbox, attempts, lease/heartbeat, idempotência, reconciliação e artefatos atômicos. |
| API | Rotas sem versão, resposta de criação ambígua e expiração de job prematura. | `/api/v1`, DTOs separados, `expires_at=null` até sucesso e contratos sincronizados. |
| Erros | Um código podia corresponder a múltiplos HTTP status ou retry incerto. | Taxonomia determinística: um código, um status canônico e política de retry explícita. |
| Arquitetura | Regra Python era colocada em pacote TypeScript compartilhado. | Motor canônico no backend Python; frontend usa OpenAPI gerado. |
| Segurança de arquivo | MIME/extensão eram tratados como validação suficiente. | Quarentena, parsing seguro, limites estruturais, XXE/ZIP/DoS e sandbox de subprocessos. |
| Confiança | Ocultar toda incerteza ou mostrar score bruto eram as únicas opções. | Métricas brutas internas; warnings categóricos e acionáveis na saída pública. |
| Testes | Casos exemplificativos sem oráculo semântico e sem corpus hostil. | Properties, invariantes, goldens, comparador semântico, IDOR/CSRF e arquivos hostis. |
| Aceite | Critérios verificavam documentação, não o produto executável. | Gates funcionais, musicais, de segurança, operação, UX e evidência. |

## Novos documentos canônicos principais

- `06-matriz-suporte-mvp.md`;
- `08-hierarquia-documental.md`;
- `09-decisoes-pendentes.md`;
- `../music/01-modelo-transposicao.md`;
- `../music/02-musicxml-canonico.md`;
- `../music/03-politica-enarmonia-oitavas.md`;
- `../music/04-pipeline-omr.md`;
- `../music/05-invariantes-validacao.md`;
- `../backend/16-maquina-estados.md`;
- `../backend/17-sessao-anonima-autorizacao.md`;
- `../backend/18-taxonomia-erros.md`;
- `../security/05-sandbox-processadores.md`;
- `../qa/07-corpus-fixtures.md`;
- `../qa/08-testes-seguranca-arquivos.md`.

## Validação documental executada

A revisão final verificou:

- 91 arquivos Markdown não vazios, em UTF-8 e com newline final;
- exatamente um título H1 estrutural por documento;
- balanceamento de blocos de código;
- 15 exemplos JSON parseáveis;
- 183 referências internas para arquivos Markdown;
- ausência de rotas públicas antigas sem `/api/v1`;
- ausência do contrato escalar antigo como implementação válida;
- ausência de referências normativas ao nome histórico do projeto;
- presença das regras canônicas de intervalo vetorial, autorização por sessão, estados ortogonais e sandbox;
- taxonomia de erros sem status HTTP ou retry ambíguos.

Resultado: **zero inconsistências detectadas pelo validador documental final**.

## Decisões deliberadamente não inventadas

Continuam pendentes e bloqueiam somente as capacidades relacionadas:

- engine OMR de produção;
- engine de renderização de produção;
- limites exatos obtidos por benchmark;
- limiares quantitativos para ativar PDF;
- suporte público a MXL;
- expansão para multiparte/multipauta.

A lista normativa está em `09-decisoes-pendentes.md`.

## Impacto no plano de implementação

O Core pode ser implementado sem esperar OMR ou renderização. A sequência recomendada é:

```text
governança e baseline
→ sessão/contratos
→ catálogo e álgebra musical
→ motor MusicXML seguro
→ upload/storage/job/worker
→ corte vertical
→ segurança/retenção
→ UX/acessibilidade
→ operação e aceite
```

A trilha PDF deve reutilizar o mesmo pipeline a partir de `raw_musicxml`/`normalized_musicxml`, sem criar um motor musical paralelo.

## Limite desta revisão

Esta entrega valida e corrige **documentação**. Nenhum repositório de frontend, backend, migration, OpenAPI real, MusicXML executável, container, OMR ou renderer foi fornecido ou testado nesta tarefa. Portanto, o produto ainda não está tecnicamente aceito; os critérios em `../100-implementacao/criterios-aceite-mvp.md` precisam ser comprovados durante a implementação.
