# Visão técnica completa do W_Flyer

> Status: referência. Revisão: 2026-07-27.  
> Público: arquitetos de software, desenvolvedores experientes, engenheiros de plataforma, QA, segurança e profissionais responsáveis pelos motores musicais.  
> Regra: este documento centraliza a visão do sistema, mas não substitui contratos especializados. Em caso de conflito, prevalece a hierarquia definida em `08-hierarquia-documental.md`.

## 1. Objetivo do sistema

O W_Flyer é uma aplicação web de preparação musical verificável. Seu núcleo deve transformar uma representação musical estruturada, preservar invariantes formais, registrar proveniência e expor ao usuário apenas o nível de garantia efetivamente demonstrado pelo backend.

O primeiro produto executável é o **MVP Core MusicXML**:

```text
MusicXML não comprimido
→ ingestão segura
→ normalização para modelo musical canônico
→ transposição instrumental determinística
→ verificação independente
→ serialização MusicXML
→ artefato privado para download
```

O projeto não trata como sinônimos:

- transposição;
- reconhecimento óptico musical;
- extração de melodia;
- redução monofônica;
- harmonização;
- adaptação idiomática;
- arranjo/orquestração;
- engraving;
- reprodução de áudio.

Cada operação possui contrato, riscos, níveis de garantia e gates próprios.

## 2. Estado atual do repositório

Na revisão de 2026-07-27:

- Fase 0 concluída, sincronizada e arquivada no OpenSpec;
- documentação de produto, arquitetura, segurança, QA e domínio musical consolidada;
- Graphify, OpenSpec, Serena e Context7 preparados para o fluxo dos agentes;
- arquitetura física planejada;
- código funcional ainda não iniciado;
- Fase 1 `establish-executable-foundation` ainda não aberta.

Ainda não existem:

- `apps/web`;
- `apps/api`;
- `apps/worker`;
- banco, migrations e storage operacional;
- pacotes Python musicais;
- suíte de testes de produto;
- pipeline CI da aplicação.

## 3. Princípios arquiteturais

### 3.1 Fail-closed

Diante de ambiguidade material, violação de invariante ou impossibilidade de comprovação, o sistema não publica o artefato como confiável.

Estados aceitáveis incluem:

- rejeição explícita;
- `awaiting_user_input`;
- falha determinística não retentável;
- conclusão com warning não material;
- conclusão verificada.

É proibido escolher silenciosamente uma interpretação musical apenas para concluir o job.

### 3.2 PostgreSQL como fonte de verdade

Fila, cache e workers não são a autoridade sobre o estado do job. O PostgreSQL mantém:

- estado;
- estágio;
- tentativas;
- idempotência;
- eventos;
- proveniência;
- artefatos;
- retenção;
- manifesto de versões.

### 3.3 Transformador e verificador separados

O componente que produz a transformação não valida sozinho a própria saída.

```text
Transformation Engine
→ output candidate
→ independent reparse
→ Music Verifier
→ publish/reject
```

O verificador deve operar sobre a representação semântica, não apenas comparar XML textual.

### 3.4 Imutabilidade e versionamento

Uploads, tentativas e artefatos são identificados por IDs e hashes. Uma nova execução não sobrescreve silenciosamente a evidência anterior.

### 3.5 Domínio musical no backend

Regras canônicas não são implementadas em componentes React nem duplicadas em TypeScript. O frontend recebe contratos de apresentação e resultados calculados pelo backend.

### 3.6 Capabilities desabilitadas por padrão

Uma funcionalidade documentada não está automaticamente disponível. Ativação exige:

- decisão/ADR;
- contrato;
- fixtures;
- testes;
- observabilidade;
- feature flag;
- gate de release;
- rollback.

### 3.7 Controle humano em operações inferenciais e criativas

Extração de melodia, harmonização e arranjo não recebem o mesmo nível de garantia de uma transformação determinística. Ambiguidade ou criação musical relevante exige revisão ou aceite do usuário.

## 4. Escopo do MVP Core

### 4.1 Entradas

Suportadas:

- `.musicxml`;
- `.xml` somente quando a inspeção confirmar MusicXML.

Desabilitadas:

- `.mxl`;
- `.pdf`;
- `.png`, `.jpg`, `.jpeg`;
- entrada manuscrita.

### 4.2 Perfil musical

Suportado:

- uma parte;
- uma pauta;
- instrumento afinado;
- 12-TET;
- múltiplas vozes na mesma pauta;
- acordes notados;
- notas e pausas;
- ties e tuplets;
- mudanças de tonalidade, clave e compasso;
- letras, dinâmica e articulação preservadas quando parseadas;
- símbolos de harmonia simples quando suportados pelo parser.

Rejeitado no Core:

- múltiplas partes;
- mais de uma pauta na parte;
- percussão não afinada;
- tablatura;
- microtons;
- mudança de instrumento dentro da parte;
- estruturas não representáveis pelo modelo aprovado.

### 4.3 Saída

- MusicXML 4.0 não comprimido;
- sem garantia de layout idêntico ao arquivo de origem;
- metadado de transposição coerente com o instrumento de destino;
- artefato privado, versionado e sujeito a retenção.

## 5. Taxonomia de operações

| Operação | Classe | Preservação | Automação |
|---|---|---|---|
| `TRANSPOSE` | Determinística | Preserva todos os eventos suportados | Publicável após invariantes |
| `EXTRACT_MELODY` | Inferencial | Seleciona subconjunto da origem | Revisão se houver ambiguidade |
| `REDUCE_TO_MONOPHONIC` | Determinística após seleção | Preserva a linha confirmada | Gate futuro |
| `HARMONIZE` | Criativa condicionada | Preserva melodia bloqueada e cria eventos | Exige escolha/aceite |
| `ARRANGE_FOR_INSTRUMENT` | Mista | Pode redistribuir textura, registro e vozes | Gate futuro por instrumento |

DTOs, estados e assurance levels devem carregar a operação explicitamente.

## 6. Arquitetura lógica

```text
┌─────────────────────────────────────────────────────────────┐
│ Browser                                                     │
│ Next.js + React + TypeScript                                │
│ session bootstrap, upload, configuration, polling, download │
└──────────────────────────────┬──────────────────────────────┘
                               │ HTTPS / JSON / multipart
┌──────────────────────────────▼──────────────────────────────┐
│ FastAPI                                                     │
│ authz by anonymous session, CSRF, validation, contracts     │
│ job orchestration, DB transactions, outbox, signed access   │
└──────────────┬───────────────────┬───────────────────────────┘
               │                   │
      ┌────────▼────────┐  ┌───────▼──────────┐
      │ PostgreSQL      │  │ Private storage  │
      │ source of truth │  │ quarantine/data  │
      └────────┬────────┘  └───────┬──────────┘
               │ outbox            │ immutable objects
      ┌────────▼────────┐           │
      │ Redis / Celery  │           │
      │ transport       │           │
      └────────┬────────┘           │
               │                    │
┌──────────────▼────────────────────▼──────────────────────────┐
│ Worker                                                      │
│ parse → normalize → transform → verify → serialize → publish│
│ retries, lease/heartbeat, reconciliation, cleanup            │
└─────────────────────────────────────────────────────────────┘
```

## 7. Arquitetura física planejada

```text
app.WFlyer/
├── apps/
│   ├── web/
│   ├── api/
│   └── worker/
├── packages/
│   ├── api-client/
│   ├── ui/
│   ├── config/
│   └── python/
│       ├── music-domain/
│       ├── musicxml/
│       ├── instrument-catalog/
│       ├── transposition-engine/
│       └── music-verifier/
├── tests/
│   ├── fixtures/
│   └── e2e/
├── docs/
├── openspec/
├── scripts/
├── nx.json
├── pnpm-workspace.yaml
├── pyproject.toml
├── pnpm-lock.yaml
└── uv.lock
```

### 7.1 Fronteiras

`apps/web`:

- composição visual;
- navegação;
- estado de interface;
- upload;
- polling;
- download;
- acessibilidade;
- motion;
- nenhuma regra musical canônica.

`apps/api`:

- HTTP;
- sessão anônima;
- CSRF;
- autorização por recurso;
- persistência;
- idempotência;
- criação de jobs;
- consulta de estado;
- exposição de artefatos;
- publicação de outbox.

`apps/worker`:

- consumo assíncrono;
- execução dos pacotes musicais;
- heartbeat;
- retry;
- reconciliação;
- cleanup;
- publicação atômica.

`packages/python/*`:

- implementação única compartilhada por API e worker;
- sem dependência da aplicação HTTP;
- testável isoladamente;
- versionamento de domínio e engine.

`packages/api-client`:

- gerado a partir do OpenAPI;
- não editado manualmente.

## 8. Stack planejada

### 8.1 Frontend

- Next.js App Router;
- React;
- TypeScript strict;
- React Server Components por padrão;
- Tailwind CSS com tokens semânticos;
- shadcn/ui/Radix adaptados, sem tema padrão;
- TanStack Query;
- React Hook Form;
- Zod;
- XState somente para fluxos complexos;
- Motion for React para presença, layout e microinterações;
- GSAP + `@gsap/react` para timelines/SVG aprovados;
- Storybook;
- Vitest/Testing Library;
- MSW;
- Playwright;
- Biome;
- Style Dictionary.

### 8.2 Backend e domínio musical

- Python;
- FastAPI;
- Pydantic;
- SQLAlchemy;
- Alembic;
- PostgreSQL;
- Celery;
- Redis;
- `music21` como candidato inicial atrás de adapter;
- pytest;
- Hypothesis;
- Testcontainers;
- Ruff;
- mypy ou pyright.

### 8.3 Infraestrutura

- storage privado em filesystem no desenvolvimento local;
- storage compatível com S3 em ambientes compartilhados;
- containers para dependências locais;
- execução isolada para processadores externos;
- Nx como orquestrador de targets e affected graph;
- pnpm para JavaScript/TypeScript;
- uv workspace para Python.

Temporal, Rive, Pact, StrykerJS e mutmut permanecem condicionados a spike e ADR.

## 9. Modelo musical canônico

O MusicXML é o formato público de interoperabilidade, mas não deve ser o modelo de trabalho direto de todos os motores.

O parser converte o documento em um grafo/event model tipado, com IDs estáveis independentes de posição no XML.

Representação conceitual:

```python
@dataclass(frozen=True)
class Pitch:
    step: Literal["C", "D", "E", "F", "G", "A", "B"]
    alter: Fraction
    octave: int

@dataclass(frozen=True)
class NoteEvent:
    id: UUID
    measure_id: UUID
    onset: Fraction
    duration: Fraction
    voice: str
    staff: int
    pitch: Pitch | None
    chord_group_id: UUID | None
    tie_start: bool
    tie_stop: bool
    tuplet: TupletRef | None
    provenance: EventProvenance

@dataclass(frozen=True)
class TranspositionVector:
    diatonic_steps: int
    chromatic_semitones: int
    octave_change: int
```

O modelo também deve representar:

- parts/staves dentro do perfil habilitado;
- measures;
- time signatures;
- key signatures;
- clefs;
- voices;
- rests;
- chords;
- directions;
- lyrics;
- dynamics;
- articulations;
- harmony symbols quando suportados;
- source spans para diagnóstico;
- provenance.

## 10. Catálogo instrumental

Cada instrumento suportado possui preset versionado:

```text
id
name
family
key_name
written_to_concert_diatonic
written_to_concert_chromatic
written_to_concert_octave
default_clef
aliases
is_pitched
is_active
catalog_version
```

O job persiste snapshot dos presets de origem e destino para garantir reprodutibilidade mesmo após atualização do catálogo.

`total_semitones` é derivado; ele não substitui o componente diatônico.

## 11. Regra de transposição

A transformação entre instrumentos é calculada por vetor:

```text
output_written_interval = source_written_to_concert
                        - target_written_to_concert
```

Exemplo conceitual:

```text
Origem: instrumento em C
Destino: trompete em Bb
Resultado escrito: +1 passo diatônico, +2 semitons, 0 oitavas
```

A engine deve atualizar coerentemente:

- pitch step;
- alter;
- octave;
- key signature;
- harmony root/bass quando suportados;
- MusicXML `<transpose>`;
- metadados de instrumento.

A grafia não pode ser resolvida apenas por classe cromática. A política enarmônica deve considerar:

- intervalo diatônico;
- tonalidade da região;
- direção e política de notação;
- limites de acidentes aprovados;
- preservação semântica.

## 12. Invariantes do Core

Para `TRANSPOSE`, o verificador deve demonstrar, no perfil suportado:

1. mesma quantidade semântica de eventos preserváveis;
2. mesma estrutura temporal;
3. mesmo número e ordem de compassos;
4. mesmas durações agregadas por voz/compasso;
5. mesma altura de concerto por evento;
6. relações de chord, tie e tuplet preservadas;
7. key signatures transformadas conforme a política;
8. ausência de evento sem proveniência;
9. output reparseável;
10. target instrument metadata coerente;
11. ausência de dupla transposição;
12. hash e manifesto de engine registrados.

A comparação é semântica. Ordenação de atributos, whitespace ou IDs internos do XML não determinam equivalência musical.

## 13. Pipeline de ingestão MusicXML

```text
upload stream
→ limite de bytes
→ filename sanitization
→ content sniffing
→ quarantine object
→ parser XML hardened
→ limites estruturais
→ profile validation
→ canonical normalization
→ source artifact hash
→ job creation
```

Controles do parser:

- DTD e entidades externas desabilitados;
- sem XInclude;
- sem network access;
- limites de profundidade, nós, medidas e eventos;
- timeout e memória limitados;
- rejeição de estruturas não suportadas;
- mensagens públicas sem stacktrace.

`.mxl` continua desabilitado até existir política de container ZIP contra zip slip, expansão excessiva e entradas malformadas.

## 14. Pipeline assíncrono

```text
API transaction
├── create processing_job
├── persist request snapshot
└── insert outbox_event

outbox publisher
→ Celery message
→ worker claims attempt
→ heartbeat/lease
→ read immutable input
→ parse and normalize
→ transform
→ independent verify
→ serialize candidate
→ atomic publish artifacts
→ complete job
```

### 14.1 Reentrega e idempotência

A tarefa deve ser idempotente. Reentrega não pode criar dois resultados públicos equivalentes nem corromper estado.

Controles:

- `Idempotency-Key` por sessão para criação de job;
- `request_fingerprint` para detectar conflito;
- `processing_attempts` para cada execução;
- constraint para artefato público ativo por tipo/job;
- compare-and-set/status transition;
- reconciliation de tentativas órfãs;
- retries somente para erros transitórios.

### 14.2 Retry

Retentável:

- indisponibilidade transitória de storage;
- conexão temporária com banco/Redis;
- worker interrompido antes de commit terminal;
- timeout externo classificado como transitório.

Não retentável automaticamente:

- MusicXML inválido;
- estrutura não suportada;
- violação de invariante;
- ambiguidade musical;
- arquivo hostil;
- configuração de instrumento inválida.

## 15. Máquinas de estado

Estados devem ser separados, não condensados em um único campo.

### 15.1 UploadStatus

Exemplo:

```text
receiving
→ quarantined
→ validating
→ validated
→ rejected
→ deleted
```

### 15.2 JobStatus

```text
queued
→ running
→ awaiting_user_input
→ completed
→ completed_with_warnings
→ failed
→ cancelled
```

### 15.3 ProcessingStage

```text
queued
validating_source
normalizing
transposing
verifying
serializing
publishing
```

### 15.4 RetentionStatus

```text
active
expiring
expired
purged
```

O frontend não infere estado terminal por porcentagem de progresso.

## 16. Níveis de garantia

Níveis previstos:

```text
UNVERIFIED_SOURCE
STRUCTURALLY_VALID
SOURCE_USER_CONFIRMED
TRANSFORMATION_VERIFIED
CREATIVE_VARIANT_VALIDATED
CREATIVE_VARIANT_USER_APPROVED
```

No Core, `TRANSFORMATION_VERIFIED` é o nível relevante para transposição determinística aprovada por todos os gates.

Uma harmonização futura nunca deve receber esse mesmo rótulo apenas porque o XML é válido.

## 17. Contratos HTTP principais

Base: `/api/v1`.

### Infra e sessão

```text
GET  /health
GET  /health/ready
POST /api/v1/sessions/anonymous
GET  /api/v1/capabilities
GET  /api/v1/instruments
```

### Upload e job

```text
POST   /api/v1/uploads
DELETE /api/v1/uploads/{upload_id}
POST   /api/v1/transpositions
GET    /api/v1/jobs/{job_id}
GET    /api/v1/jobs/{job_id}/status
GET    /api/v1/jobs/{job_id}/artifacts
GET    /api/v1/artifacts/{artifact_id}/download
```

Convenções:

- UUID para recursos;
- slug para instrumento;
- datas UTC ISO 8601;
- `Cache-Control: no-store` para respostas sensíveis;
- `X-Correlation-ID` em todas as respostas;
- cookie de sessão `HttpOnly`, `Secure`, `SameSite=Lax`;
- `X-CSRF-Token` em mutações;
- recurso inexistente ou de outra sessão retorna `404`;
- DTO público não expõe `storage_key`, task ID, path, stacktrace ou token hash;
- polling respeita `Retry-After`;
- `expires_at = null` até sucesso terminal.

Erro público:

```json
{
  "error": {
    "code": "UNSUPPORTED_SCORE_STRUCTURE",
    "message": "Esta partitura ainda não é suportada.",
    "correlation_id": "req_...",
    "retryable": false,
    "field_errors": []
  }
}
```

## 18. Persistência

Tabelas iniciais:

```text
anonymous_sessions
instruments
uploads
processing_jobs
processing_attempts
generated_artifacts
job_events
outbox_events
```

### 18.1 Sessão anônima

Persistir somente hashes do token e do segredo CSRF. Suportar expiração, revogação e `last_seen_at`.

### 18.2 Upload

Persistir:

- nome sanitizado;
- MIME declarado e detectado;
- tamanho;
- SHA-256;
- chave privada de storage;
- status de validação;
- expiração;
- exclusão lógica/purge.

### 18.3 Job

Persistir:

- sessão e upload;
- idempotency hash e request fingerprint;
- source/target IDs e snapshots;
- vetor de transposição;
- política de notação;
- formatos solicitados;
- status, stage e progress;
- assurance level;
- erro público;
- correlation ID;
- engine manifest;
- timestamps e retenção.

### 18.4 Attempt

Cada tentativa registra worker/engine versions, status, timestamps e fingerprint interno do erro.

### 18.5 Artifact

Cada artefato registra tipo, visibilidade, MIME, hash, chave de storage, versão e expiração.

## 19. Sessão, autorização e CSRF

O MVP usa sessão anônima privada.

Fluxo:

```text
POST /sessions/anonymous
→ opaque cookie HttpOnly
→ csrf token returned in body
→ browser sends cookie automatically
→ mutating requests add X-CSRF-Token
```

Autorização é por `session_id` e recurso. Ocultar botão no frontend não é controle de acesso.

Regras:

- query sempre escopada pela sessão;
- `404` para recurso alheio;
- download revalida sessão, ownership, estado e retenção;
- token nunca é logado;
- rate limiting por IP/session conforme endpoint;
- session renewal não estende artefatos já expirados sem política explícita.

## 20. Storage e retenção

Buckets/áreas lógicas:

```text
quarantine/
source/
intermediate/
artifacts/
```

Regras:

- nenhum objeto é público;
- nomes de arquivo não compõem paths confiáveis;
- chaves são geradas pelo servidor;
- publicação é atômica;
- artefato parcial permanece interno;
- download é mediado pela API ou URL temporária autorizada;
- purge é idempotente;
- banco e storage são reconciliados;
- hash de conteúdo é registrado.

Retenção deve ser configurável. A expiração é calculada a partir de `finished_at` para artefatos concluídos.

## 21. Segurança

### 21.1 Upload

- streaming;
- limite de tamanho antes de buffering integral;
- MIME/signature validation;
- quarantine;
- filenames sanitizados;
- negação de formatos não habilitados;
- proteção contra polyglot e XML hostil.

### 21.2 Processadores

OMR, rasterização, renderer e ferramentas externas futuras executam:

- sem root;
- sem rede;
- filesystem mínimo;
- CPU/memória/tempo/process limits;
- sem `shell=True`;
- argumentos estruturados;
- imagem/versionamento fixado;
- cleanup após término.

### 21.3 Aplicação

- headers de segurança;
- CSRF;
- validação de input/output;
- queries parametrizadas via ORM;
- segredo fora do repositório;
- logs sanitizados;
- dependências com lockfile;
- análise de supply chain;
- tratamento de prompt injection em metadados não confiáveis para capacidades com IA.

### 21.4 Privacidade e direitos

- arquivos não são usados para treinamento sem opt-in explícito;
- políticas de retenção e exclusão;
- nenhum dado pessoal na watermark por padrão;
- créditos e copyright do material original não são removidos;
- W_Flyer não reivindica titularidade da obra.

## 22. Frontend

### 22.1 Shells

`PublicShell`:

- home;
- como funciona;
- instrumentos.

`StudioShell`:

- upload/configuração;
- processamento;
- resultado;
- comparação/revisão futura.

`UtilityShell`:

- histórico;
- configurações.

### 22.2 Componentes de domínio

```text
FileDropzone
FileSummary
InstrumentPicker
InstrumentFamilyFilter
TranspositionRoute
IntervalBadge
ScoreSurface
ProcessingTimeline
JobStatusHeader
WarningPanel
ArtifactRow
ExpirationNotice
MusicalDiff
StickyActionBar
```

A UI não deve ser composta majoritariamente por cards genéricos.

### 22.3 Estado complexo

XState pode modelar fluxos como:

```text
idle
→ validatingFile
→ configured
→ submitting
→ processing
→ awaitingReview
→ completed
→ failed
→ expired
```

Motion/GSAP executam apresentação. Eles não definem regras de negócio.

### 22.4 Motion

- CSS para microtransições simples;
- Motion for React para presença, layout e gestures;
- GSAP apenas em timelines/SVG isolados;
- nenhuma propriedade controlada por engines concorrentes;
- lazy loading;
- cleanup obrigatório;
- `prefers-reduced-motion`;
- Ink Transfer usa SVG próprio no MVP visual, não geometria da partitura real.

### 22.5 Fidelidade visual

Precedência:

```text
domain/security/accessibility contracts
> internal executable example
> approved Storybook story
> machine-readable specification
> internal screenshot
> external inspiration
```

Golden references não autorizam capabilities desabilitadas.

## 23. Testes

### 23.1 Pirâmide

Frontend:

- Vitest para unitários;
- Testing Library/Browser Mode para componentes;
- Storybook para estados;
- MSW para rede;
- Playwright para E2E, visual e acessibilidade.

Backend/domínio:

- pytest;
- Hypothesis para propriedades;
- Testcontainers para PostgreSQL, Redis e storage;
- contratos OpenAPI;
- corpus MusicXML;
- golden files semânticos.

### 23.2 Propriedades musicais

Exemplos obrigatórios:

```text
transpose(A, B) then transpose(B, A) ≡ original
concert_pitch(output_event) == concert_pitch(source_event)
duration graph remains equivalent
measure sequence remains equivalent
all output events have provenance
serialization then parse preserves canonical semantics
```

A equivalência deve considerar o subconjunto suportado e normalizações aprovadas.

### 23.3 Integração

Testar com serviços reais isolados:

- API + PostgreSQL;
- outbox + dispatcher;
- worker + Redis;
- worker + storage;
- retry/reelivery;
- crash/reconciliation;
- purge;
- ownership/IDOR;
- CSRF;
- migration em banco vazio e upgrade.

### 23.4 E2E

```text
create session
→ upload MusicXML
→ select instruments
→ submit idempotent request
→ poll respecting Retry-After
→ terminal verified result
→ list artifacts
→ authorized download
→ expiration behavior
```

### 23.5 Regression policy

Todo incidente relevante deve gerar:

- risk/failure ID;
- fixture mínima;
- teste de regressão;
- análise de abrangência;
- atualização de documentação/gate;
- rollout controlado.

## 24. Observabilidade

### 24.1 Logs

Logs estruturados com:

- timestamp;
- service;
- environment;
- correlation ID;
- job ID;
- attempt ID;
- stage;
- public/internal error class separadas;
- engine versions;
- duração.

Não logar:

- conteúdo musical integral;
- cookie/token;
- segredo CSRF;
- storage key em mensagens públicas;
- stacktrace para cliente;
- dados pessoais desnecessários.

### 24.2 Métricas

Core:

- upload acceptance/rejection;
- job duration por stage;
- queue latency;
- retry rate;
- failure code rate;
- verifier rejection rate;
- artifact publish failures;
- purge lag;
- storage reconciliation mismatch;
- false verified result rate no corpus congelado.

Capacidades futuras:

- review-required rate;
- automatic coverage;
- melody ambiguity rate;
- musician approval rate;
- playability warning precision;
- harmony blind-review scores.

### 24.3 Tracing

Correlation ID deve atravessar browser, API, outbox, worker e storage operations. OpenTelemetry pode ser adotado na Fase de observabilidade mediante ADR/configuração.

## 25. Entrega e execução

### 25.1 Ambientes

- local;
- CI/test;
- staging;
- produção.

Configuração externa, validada e sem defaults inseguros.

### 25.2 Migrations

- Alembic obrigatório;
- migration aplicada em banco vazio no CI;
- upgrade path testado;
- rollback ou forward-fix documentado;
- aplicação não inicializa em schema incompatível.

### 25.3 Feature flags

Capabilities avançadas iniciam `false`.

Flag não substitui autorização nem validação. O backend continua rejeitando operação não aprovada mesmo que o frontend exponha incorretamente uma ação.

### 25.4 Rollout

- internal;
- corpus/staging;
- usuários selecionados;
- percentual controlado;
- general availability.

Cada capability possui kill switch e critérios de regressão.

## 26. Toolchain de IA e desenvolvimento

Fluxo obrigatório:

```text
OpenSpec change
→ Graphify impact query
→ Serena symbol navigation
→ Context7 only for external APIs
→ implementation slice
→ Nx affected targets
→ tests/gates
→ docs/OpenSpec/Graphify update
```

Responsabilidades:

- OpenSpec: intenção, requisitos, design e tasks;
- Graphify: grafo macro de documentos/módulos;
- Serena: símbolos e referências no código;
- Context7: documentação de dependências externas;
- Nx: project graph, affected, cache e execução;
- AGENTS.md: regras obrigatórias do agente.

O grafo não é fonte normativa. Relações inferidas precisam ser confirmadas no código ou contrato.

## 27. Fases de implementação

### Fase 1 — fundação executável

- monorepo pnpm/uv/Nx;
- Next.js base;
- FastAPI base;
- PostgreSQL/Alembic;
- sessão anônima mínima;
- Redis/Celery;
- storage local privado;
- health/readiness/capabilities;
- lint, typecheck, testes e CI.

Sem motor musical.

### Fase 2 — domínio e catálogo

- pitch/interval model;
- transposition vectors;
- instrument presets/versioning;
- invariantes do modelo;
- fixtures básicas.

### Fase 3 — MusicXML e engine

- parser seguro;
- normalizador;
- serializer;
- transposition engine;
- independent verifier;
- property tests;
- golden corpus.

### Fases 4–9 — Core integrado

- upload/job pipeline;
- corte vertical;
- UX final;
- segurança;
- observabilidade;
- retenção;
- aceite.

### Trilhas avançadas

- PDF/OMR;
- Musical Diff e áudio;
- modelo multipauta/multiparte;
- extração de melodia;
- adaptação idiomática;
- harmonização;
- ensemble;
- ensaio e colaboração.

## 28. Arquitetura das capacidades futuras

### 28.1 PDF/OMR

```text
PDF/image
→ sandboxed rasterization
→ OMR adapter
→ raw MusicXML
→ confidence/evidence
→ user confirmation
→ Core pipeline
```

OMR não publica resultado como verificado sem confirmação/gates definidos.

### 28.2 Extração de melodia

Análise sobre event graph com candidatos por frase/região. Evidências podem incluir:

- voice/staff;
- continuidade;
- métrica;
- duração;
- lyrics;
- dinâmica/articulação;
- registro relativo;
- motif recurrence;
- accompaniment pattern separation.

`highest note = melody` é proibido.

### 28.3 Harmonização

```text
confirmed melody
→ phrase/form analysis
→ tonal/modal regions
→ structural/non-chord note classification
→ harmonic rhythm
→ candidate chords/functions
→ voicing/voice leading
→ hard constraint validation
→ ranked variants
→ user selection
```

Modelos/solvers são proposers não confiáveis; validação rígida permanece fora deles.

### 28.4 Adaptação idiomática

Instrument capability profile:

```text
written/sounding/comfortable range
nominal/practical polyphony
chord span
double stops/multiphonics
breath/sustain
register profiles
fingering/difficulty model
idiomatic and discouraged patterns
```

A engine reporta impossível, possível, difícil, idiomático ou confortável e apresenta diff antes de alterar.

### 28.5 Score/parts

Um canonical score graph gera projections de score e partes. Validador bidirecional garante:

- mesma música;
- transposição por instrumento;
- rehearsal marks;
- measure numbering;
- atomic package version.

### 28.6 Audio/rehearsal

Playback map deve expandir repetições, casas, D.C., D.S., coda e mudanças de tempo. A posição visual não pode ser inferida apenas pelo índice linear do XML.

## 29. Arquitetura empresarial, billing, fiscal e hosting

### 29.1 Contexto pré-CNPJ

A pessoa jurídica ainda não existe. Billing e NFS-e permanecem feature flags desabilitadas. Nenhuma regra de CNAE, regime, imposto, certificado ou emissor é canônica até decisão formal registrada.

### 29.2 Separação de produtos

```text
wflyer-site repository
app.WFlyer repository
client repositories/deployments
```

`wflyer.com.br` hospeda o institucional; `app.wflyer.com.br` aponta por DNS para a distribuição da aplicação. Sites de clientes não compartilham a conta de produção do SaaS.

### 29.3 Billing

Domínio interno desacoplado por `BillingProvider`. Candidato preliminar: Stripe; alternativa: Mercado Pago. O modelo previsto usa subscriptions, entitlements, credit ledger e usage reservations. Webhooks assinados, idempotência e reconciliação são obrigatórios.

### 29.4 Fiscal

Pagamento cria obrigação fiscal assíncrona. `FiscalProvider` abstrai emissor nacional, municipal, terceiro ou processo manual. A emissão só é habilitada após município, regime, inscrição, código de serviço, certificado/autenticação e homologação serem definidos.

### 29.5 Produção AWS

Arquitetura-alvo:

```text
Route 53 → CloudFront/WAF → ALB → ECS web/api
PostgreSQL RDS Multi-AZ
S3 privado
outbox → SQS/DLQ → worker pools
Redis para cache/coordenação curta
```

AWS Organizations separa development e production. Site institucional e sites de clientes permanecem fora do blast radius do app.

### 29.6 Resiliência

- banco não armazena arquivos binários grandes;
- filas por workload;
- backpressure e quotas;
- publicação atômica;
- PITR e backup cross-region quando aprovado;
- status page independente;
- runbooks exercitados;
- RPO/RTO só viram SLA depois de medidos.

## 30. Riscos arquiteturais principais

1. **Promessa de confiabilidade excessiva** — mitigada por assurance levels e fail-closed.
2. **Modelo interno acoplado ao XML/renderer** — mitigado por IDs estáveis e canonical graph.
3. **Dupla implementação musical** — proibida entre TS e Python.
4. **Fila como fonte de verdade** — proibida; DB mantém estado.
5. **Retry de erro determinístico** — taxonomia separa transient/deterministic.
6. **Publicação parcial** — artefato só fica público após verificação e commit atômico.
7. **IDOR em sessão anônima** — ownership em toda query/download.
8. **Parser XML hostil** — parser hardened e limites.
9. **UI habilitando capability futura** — capabilities endpoint e flags backend.
10. **Visual genérico produzido por IA** — golden references, Storybook e contrato de fidelidade.
11. **Harmonização confundida com correção** — taxonomia e garantia separadas.
12. **Grafo/tooling desatualizado** — atualização obrigatória após mudanças estruturais.

O catálogo ampliado está no registro de pre-mortem e FMEA.

## 31. Definition of Done por capability

Uma capability não está concluída apenas porque o happy path funciona.

Requisitos mínimos:

- OpenSpec aprovado;
- contratos de domínio/API;
- migrations;
- código;
- testes unitários, properties e integração aplicáveis;
- segurança;
- observabilidade;
- UI states;
- acessibilidade;
- documentação;
- feature flag/rollout;
- rollback;
- evidência do corpus;
- Graphify atualizado;
- nenhum gate crítico pendente.

## 32. Resumo técnico

O W_Flyer deve ser implementado como um sistema assíncrono, versionado e fail-closed, no qual:

- MusicXML é o formato público canônico do Core;
- um modelo musical interno tipado sustenta transformações;
- a transposição usa vetor diatônico, cromático e de oitava;
- API e worker compartilham pacotes Python independentes;
- PostgreSQL mantém o estado autoritativo;
- outbox e worker idempotente evitam perda/duplicação;
- transformador e verificador são componentes separados;
- artefatos privados são publicados atomicamente;
- assurance level descreve o que foi efetivamente demonstrado;
- frontend não contém regra musical;
- capacidades inferenciais/criativas exigem controle humano;
- testes musicais e corpus são parte da arquitetura, não uma etapa posterior.

## 33. Leitura técnica complementar

Ordem recomendada após este documento:

1. `08-hierarquia-documental.md`;
2. `05-escopo-mvp-app-wflyer.md`;
3. `06-matriz-suporte-mvp.md`;
4. `../music/01-modelo-transposicao.md`;
5. `../music/02-musicxml-canonico.md`;
6. `../music/05-invariantes-validacao.md`;
7. `../backend/02-arquitetura-api-worker.md`;
8. `../backend/03-endpoints-api.md`;
9. `../backend/04-modelagem-banco.md`;
10. `../backend/16-maquina-estados.md`;
11. `../backend/19-confiabilidade-musical-fail-closed.md`;
12. `../security/01-modelo-ameacas.md`;
13. `../qa/01-estrategia-testes.md`;
14. `../100-implementacao/guia-codex-app-wflyer.md`.

## Catálogo de preços, credit ledger e políticas públicas

O domínio comercial utilizará catálogo versionado, valores monetários em unidades mínimas, percentuais em basis points, `usage_quote`, `usage_reservation` e ledger imutável. `pricing-config.template.yaml` mantém valores não decididos como `null`; produção deve rejeitar catálogo incompleto.

A publicação jurídica será governada por `docs/policies/policy-manifest.yaml`. A rota `/politicas` apenas apresenta versões aprovadas; rascunhos, dados empresariais pendentes e políticas sem vigência não podem ser expostos como finais.
