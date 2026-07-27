## Context

O repositório está em estado predominantemente documental e ainda não possui aplicação, dependências de produto ou coletores de testes. A Fase 0 deve preparar a orientação da IA e a toolchain sem antecipar decisões da Fase 1. O manifesto da toolchain é vinculante para classificação e fase das ferramentas; ADRs aprovadas, contratos de domínio e segurança conservam precedência sobre inferências e sobre o grafo.

A execução deve sobreviver a interrupções, preservar alterações preexistentes do usuário e produzir evidências auditáveis. Nenhuma operação desta mudança exige `sudo` ou alteração de pacotes do sistema.

## Goals / Non-Goals

**Goals:**

- Fixar o baseline do ambiente e os riscos antes das instalações.
- Disponibilizar OpenSpec, Graphify, Serena e Context7 para o Codex, com verificação funcional das integrações.
- Usar o grafo para identificar a documentação vinculante da Fase 0 e mantê-lo coerente com a estrutura criada.
- Criar uma superfície raiz mínima e reproduzível para comandos de verificação, sem dependências de produto.
- Registrar versões, comandos, resultados, falhas, pendências, rollback e decisão do gate.

**Non-Goals:**

- Instalar Nx ou qualquer framework de frontend, backend, persistência, filas ou observabilidade destinado a fases posteriores.
- Instalar Temporal, Rive, Pact, StrykerJS, mutmut, OMR, renderer musical ou motor de harmonização.
- Implementar telas de produção, motor musical, upload, transposição, harmonização, PDF, áudio, autenticação ou funcionalidades simuladas.
- Resolver decisões arquiteturais de produto ainda pendentes ou iniciar tarefas da Fase 1.

## Decisions

### 1. O manifesto governa a fase de instalação

Somente ferramentas marcadas como obrigatórias para a Fase 0 serão instaladas como fundação: OpenSpec, Graphify e Serena. Context7 também será configurado porque é uma exigência explícita desta execução e do fluxo de documentação da IA. Nx permanece na Fase 1 conforme o manifesto, ainda que o documento de bootstrap cite arquivos Nx entre saídas desejadas da Fase 0.

Alternativa rejeitada: instalar antecipadamente todas as ferramentas mencionadas nos documentos. Isso eliminaria a distinção entre obrigatório, sob demanda e fases futuras.

### 2. Instalações ficam isoladas do sistema

CLIs Node são instaladas pelo pnpm em prefixo de usuário; CLIs Python são instaladas pelo `uv tool`; MCPs são registrados na configuração do Codex. Artefatos específicos do projeto ficam no repositório. Não se usa `sudo`, `apt` nem modificação equivalente do sistema.

Alternativa rejeitada: instalações globais do sistema, por ampliarem o impacto e exigirem autoridade ausente.

### 3. A integração deve ser verificada pelo consumidor real

Versão de CLI e presença em `codex mcp list` são evidências necessárias, mas não suficientes. Serena deve ativar o projeto a partir da raiz. Context7 deve responder a uma resolução de biblioteca e a uma consulta documental em uma nova sessão do Codex. Limitações honestas, como ausência de arquivos analisáveis para a Serena, são registradas sem simular saúde.

### 4. O grafo é índice e evidência auxiliar

O primeiro grafo deve cobrir o repositório disponível, permitir consulta dos documentos vinculantes e ser atualizado após mudanças estruturais. Relações críticas encontradas no grafo são confirmadas diretamente nos documentos; relações inferidas ou ambíguas não são tratadas como fatos. Saídas incompletas de uma interrupção são preservadas em backup antes da recuperação.

### 5. O workspace raiz será mínimo e sem ecossistemas fictícios

A raiz terá metadados privados do workspace e comandos de verificação, sem dependências de runtime ou desenvolvimento de produto. Um lockfile nativo será gerado somente para um ecossistema realmente inicializado. Ferramentas em escopo de usuário terão suas versões resolvidas no relatório, não serão duplicadas como dependências locais apenas para aparecerem em lockfiles. Um `uv.lock` não será inventado enquanto não houver projeto Python e versão de Python de produto aprovados.

Alternativa rejeitada: criar configuração Nx ou projeto Python vazio. Isso anteciparia a Fase 1 e daria falsa aparência de decisões concluídas.

### 6. Verificações são orientadas por evidência

Um verificador determinístico conferirá comandos essenciais, versões e arquivos esperados sem fazer instalações. Os coletores existentes serão executados quando houver configuração; a inexistência de suites num repositório documental será reportada como baseline zero, nunca substituída por testes falsos.

### 7. O gate não libera automaticamente a Fase 1

O relatório final classifica cada critério como aprovado, aprovado com ressalva ou bloqueado. Concluir esta mudança apenas encerra a Fase 0 solicitada; qualquer início da Fase 1 requer uma decisão posterior e explícita.

## Risks / Trade-offs

- [Documentos divergem sobre Nx na Fase 0] → Aplicar a fase definida no manifesto, registrar a divergência e manter Nx adiado.
- [Ferramentas em escopo de usuário não ficam presas a um lockfile do projeto] → Registrar versões exatas e comandos de reinstalação/rollback no relatório.
- [Repositório documental limita Serena e coletores] → Registrar a ativação bem-sucedida separadamente da ausência esperada de código analisável e suites.
- [Atualização do Graphify pode invalidar cache anterior] → Preservar backups, validar integridade do grafo e registrar a estratégia de recuperação.
- [Configuração MCP do Codex é global ao usuário] → Enumerar o impacto e fornecer remoção individual por servidor.
- [Working tree já continha alteração do usuário] → Excluir essa alteração do escopo e não restaurá-la nem sobrescrevê-la.

## Migration Plan

1. Capturar baseline e emitir o relatório de pré-instalação.
2. Instalar e verificar as quatro ferramentas na ordem solicitada.
3. Inicializar a mudança OpenSpec e produzir seus artefatos de planejamento.
4. Gerar, consultar e validar o grafo; ativar Serena; verificar MCPs no Codex.
5. Criar a fundação mínima do workspace e seus lockfiles aplicáveis.
6. Executar o verificador e os coletores disponíveis.
7. Atualizar e validar novamente o grafo.
8. Emitir o relatório final e parar no gate da Fase 0.

O rollback remove cada registro MCP e instalação de usuário individualmente e restaura saídas do Graphify a partir do backup preservado. Arquivos do projeto só devem ser removidos após revisão da lista produzida no relatório.

## Open Questions

- A documentação deve ser reconciliada posteriormente para remover a ambiguidade entre Nx na Fase 1 do manifesto e `nx.json` entre as saídas da Fase 0 do bootstrap.
- A versão de Python e o formato do ambiente Python do produto devem permanecer pendentes até a fase que realmente inicializar o backend.
