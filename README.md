# W_Flyer — documentação e fundação do projeto

> Estado do repositório em 2026-07-27: **Fase 0 concluída e arquivada; código funcional do produto ainda não iniciado**.

O W_Flyer será uma aplicação web para transformar material musical estruturado com rastreabilidade, validação independente e controle do músico. O primeiro produto executável será o **MVP Core MusicXML**. PDF/OMR, extração de melodia, adaptação idiomática, harmonização, áudio, ensemble e marca d'água são trilhas posteriores e permanecem desabilitadas até seus gates específicos.


## Duas visões completas da aplicação

Para atender públicos diferentes, a documentação possui duas explicações centrais:

- [Explicação completa para quem não é programador](docs/00-visao-geral/20-explicacao-completa-nao-tecnica.md) — apresenta propósito, funcionamento, limites, experiência e evolução em linguagem acessível;
- [Visão técnica completa](docs/00-visao-geral/21-visao-tecnica-completa.md) — consolida domínio, arquitetura, contratos, processamento, segurança, testes e roadmap para profissionais experientes.

Esses documentos são portas de entrada. As especificações especializadas continuam sendo a fonte normativa em cada área.

## Estado atual

Já existem neste repositório:

- documentação canônica de produto, domínio musical, backend, frontend, segurança e QA;
- catálogo de riscos e política `fail-closed`;
- referências visuais internas ainda sujeitas a aprovação humana;
- OpenSpec, Graphify, Serena e Context7 preparados para orientar agentes;
- evidências da Fase 0 e scripts de validação do repositório e da toolchain local.

Ainda **não** existem:

- frontend Next.js;
- API FastAPI;
- worker e fila;
- banco e migrations;
- motor MusicXML/transposição;
- testes de produto;
- CI funcional da aplicação.

A ausência desses itens é esperada neste ponto. Nenhuma tela, endpoint ou capability avançada deve ser simulada para aparentar progresso.

## MVP Core

O primeiro corte funcional obrigatório é:

```text
MusicXML não comprimido
→ validação e normalização seguras
→ seleção do instrumento de origem
→ seleção do instrumento de destino
→ transposição determinística
→ verificação musical independente
→ MusicXML transposto para download
```

Perfil inicial suportado:

- uma parte;
- uma pauta;
- instrumento afinado;
- sistema de 12 semitons;
- notas, pausas, acordes notados, vozes, ties e tuplets suportados;
- mudanças de clave, compasso e tonalidade dentro da parte;
- sessão anônima com recursos privados.

O escopo normativo está em [`docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`](docs/00-visao-geral/05-escopo-mvp-app-wflyer.md).

## Roadmap canônico

A ordem do Core é:

| Fase | Entrega | Estado |
|---:|---|---|
| 0 | Governança documental e ferramentas de orientação da IA | concluída e arquivada |
| 1 | Fundação executável: monorepo, CI, API base, banco, migrations, sessão, worker e storage | próxima; não iniciada |
| 2 | Catálogo instrumental e modelo musical | bloqueada pela Fase 1 |
| 3 | Parser, normalizador, transposição e verificador MusicXML | bloqueada pela Fase 2 |
| 4–9 | Pipeline, corte vertical, segurança, UX, operação e aceite do Core | futuras |

O roadmap completo, incluindo trilhas avançadas, está em [`docs/00-visao-geral/02-roadmap-fases.md`](docs/00-visao-geral/02-roadmap-fases.md).

## Regra musical central

A transposição entre instrumentos usa um intervalo completo, não apenas um número de semitons:

```text
intervalo_escrito = vetor_origem_written_to_concert
                  - vetor_destino_written_to_concert
```

O vetor contém componente diatônico, cromático e de oitava. A especificação introdutória está em [`W-Flyer_Regra-Transposição.md`](W-Flyer_Regra-Transposição.md); o modelo canônico está em `docs/music/`.

## Organização documental

A precedência normativa está em [`docs/00-visao-geral/08-hierarquia-documental.md`](docs/00-visao-geral/08-hierarquia-documental.md). Em caso de conflito, um agente deve interromper a implementação e corrigir a fonte canônica antes de escrever código.

Documentos de entrada:

- índice geral: [`docs/00-visao-geral/00-indice.md`](docs/00-visao-geral/00-indice.md);
- decisões arquiteturais: [`docs/00-visao-geral/01-decisoes-arquiteturais.md`](docs/00-visao-geral/01-decisoes-arquiteturais.md);
- decisões pendentes: [`docs/00-visao-geral/09-decisoes-pendentes.md`](docs/00-visao-geral/09-decisoes-pendentes.md);
- guia de implementação: [`docs/100-implementacao/guia-codex-app-wflyer.md`](docs/100-implementacao/guia-codex-app-wflyer.md);
- critérios de aceite: [`docs/100-implementacao/criterios-aceite-mvp.md`](docs/100-implementacao/criterios-aceite-mvp.md);
- regras dos agentes: [`AGENTS.md`](AGENTS.md).

## Fluxo obrigatório da IA

```text
OpenSpec da mudança
→ consulta dirigida ao Graphify
→ navegação por símbolos com Serena
→ Context7 somente para dependências externas
→ implementação incremental
→ testes e gates aplicáveis
→ atualização de documentação, OpenSpec e Graphify
```

A IA não deve ler indiscriminadamente todo o repositório, inventar decisões pendentes ou avançar de fase sem evidência do gate anterior.

## Próxima mudança

Após a aprovação desta consolidação, a próxima mudança OpenSpec recomendada é:

```text
establish-executable-foundation
```

Ela deverá conter exclusivamente o planejamento e a execução da Fase 1. Não deve iniciar o motor musical nem as capabilities avançadas.

## Validação local

Validação portável dos arquivos versionados:

```bash
pnpm run verify:repository
```

Validação da toolchain do agente na máquina de desenvolvimento:

```bash
pnpm run verify:agent-toolchain
```

Os dois comandos possuem responsabilidades diferentes. A validação do repositório não depende de MCPs, Docker Desktop ou CLIs globais específicas da máquina.

## Regra de progressão

> Uma fase somente pode ser marcada como concluída quando seus contratos, código, testes, evidências e documentação estiverem coerentes. A próxima fase não começa automaticamente.
