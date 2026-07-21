## ADDED Requirements

### Requirement: Baseline de pré-instalação
O bootstrap SHALL registrar diretório atual, raiz Git, branch, estado do working tree, sistema operacional e versões de Git, Node.js, npm, Python, uv e Docker antes de instalar ferramentas. O relatório SHALL separar ferramentas encontradas, ausentes, incompatibilidades, comandos propostos, alterações globais, alterações no projeto e riscos.

#### Scenario: Ambiente capturado antes da instalação
- **WHEN** a execução da Fase 0 é iniciada
- **THEN** o relatório de pré-instalação contém todos os campos obrigatórios e distingue `python` ausente de `python3` disponível

### Requirement: Ordem e escopo da toolchain
O bootstrap SHALL instalar e configurar OpenSpec, Graphify com integração de projeto para Codex, Serena MCP para Codex e Context7 compatível com Codex, nessa ordem. As instalações MUST permanecer em escopo de usuário ou projeto e MUST NOT usar `sudo` nem alterar pacotes do sistema.

#### Scenario: Instalação sem privilégio de sistema
- **WHEN** as ferramentas da Fase 0 são instaladas
- **THEN** cada ferramenta é resolvida na ordem exigida, seu escopo é registrado e nenhum gerenciador de pacotes do sistema é invocado

### Requirement: Planejamento OpenSpec
O bootstrap SHALL inicializar OpenSpec, manter a mudança `bootstrap-core-foundation` e produzir proposta, desenho, especificação e tarefas detalhadas antes de qualquer instalação de framework do produto.

#### Scenario: Mudança pronta antes de frameworks
- **WHEN** o status da mudança é validado
- **THEN** todos os artefatos exigidos para aplicação estão completos e nenhum framework de produto foi instalado

### Requirement: Grafo da Fase 0
O bootstrap SHALL gerar o primeiro grafo do repositório, consultá-lo para localizar os documentos vinculantes da Fase 0, confirmar relações críticas nas fontes e atualizá-lo novamente após mudanças estruturais.

#### Scenario: Consulta vinculante auditável
- **WHEN** o grafo inicial está disponível
- **THEN** uma consulta identifica os documentos que governam a Fase 0 e o resultado é registrado com memória ou evidência equivalente

#### Scenario: Estrutura refletida no grafo final
- **WHEN** os artefatos e a fundação do workspace são criados
- **THEN** o Graphify é atualizado e a integridade do grafo final é verificada

### Requirement: Integrações Codex verificadas
O bootstrap SHALL ativar a raiz atual na Serena e SHALL verificar no Codex que Serena e Context7 estão habilitados. Context7 MUST completar uma chamada de resolução de biblioteca e uma consulta documental; limitações de análise da Serena MUST ser reportadas sem simulação.

#### Scenario: Context7 responde pelo MCP
- **WHEN** uma nova sessão do Codex consulta documentação de uma ferramenta
- **THEN** Context7 resolve a biblioteca e retorna documentação pela chamada `query-docs`

#### Scenario: Projeto documental ativado na Serena
- **WHEN** a Serena inicia a partir da raiz do W_Flyer
- **THEN** o projeto atual é ativado e a ausência de arquivos analisáveis, se ocorrer, é registrada como limitação real

### Requirement: Fundação mínima e versões reproduzíveis
O bootstrap SHALL criar somente metadados e comandos necessários à verificação da Fase 0. Toda dependência de projeto resolvida MUST constar no lockfile nativo aplicável, e todas as versões de ferramentas MUST constar no relatório da fase. O bootstrap MUST NOT criar um ecossistema ou lockfile para o qual não exista projeto real.

#### Scenario: Workspace sem dependências funcionais
- **WHEN** a fundação raiz é instalada
- **THEN** seus metadados não contêm dependências de produto e cada lockfile gerado corresponde a um gerenciador realmente inicializado

### Requirement: Verificações e coletores honestos
O bootstrap SHALL executar verificações de instalação e todos os coletores de testes configurados. Se não houver suites ou coletores, o resultado SHALL ser registrado como baseline zero, sem criar funcionalidades ou testes simulados.

#### Scenario: Repositório ainda sem suites
- **WHEN** a descoberta de coletores não encontra configuração de testes
- **THEN** o relatório registra zero suites executáveis e não apresenta testes artificiais como evidência

### Requirement: Exclusões obrigatórias
O bootstrap MUST NOT instalar Temporal, Rive, Pact, StrykerJS, mutmut, OMR, renderer musical ou motor de harmonização. Ele MUST NOT implementar telas de produção, motor musical, upload, transposição, harmonização, PDF, áudio, autenticação ou funcionalidades simuladas.

#### Scenario: Limite da Fase 0 preservado
- **WHEN** os arquivos e pacotes alterados são auditados ao final
- **THEN** nenhuma ferramenta ou funcionalidade excluída está presente como nova instalação ou implementação

### Requirement: Relatório final e parada no gate
O bootstrap SHALL emitir um relatório final com arquivos criados e modificados, ferramentas e escopos, versões, comandos, resultados, integrações MCP, falhas, pendências, rollback e estado do gate. A execução MUST parar ao concluir a Fase 0 e MUST NOT iniciar automaticamente a Fase 1.

#### Scenario: Encerramento controlado
- **WHEN** todas as verificações autorizadas da Fase 0 terminam
- **THEN** o estado do gate é registrado e nenhuma tarefa da Fase 1 é executada
