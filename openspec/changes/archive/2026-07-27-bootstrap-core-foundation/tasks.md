## 1. Baseline e leitura controlada

- [x] 1.1 Registrar diretório atual, raiz Git, branch, working tree, sistema operacional e versões das ferramentas-base.
- [x] 1.2 Ler inicialmente somente os documentos de entrada autorizados e evitar varredura documental anterior ao Graphify.
- [x] 1.3 Emitir relatório de pré-instalação com inventário, incompatibilidades, comandos, escopos de alteração e riscos.
- [x] 1.4 Preservar a exclusão preexistente e pertencente ao usuário de `finanças.md` fora do escopo da mudança.

## 2. Toolchain de orientação da IA

- [x] 2.1 Instalar OpenSpec 1.6.0 em escopo de usuário e verificar sua CLI.
- [x] 2.2 Instalar Graphify 0.9.23 via `uv tool` e integrar a skill ao Codex no escopo do projeto.
- [x] 2.3 Instalar Serena 1.6.1 via `uv tool`, registrar seu MCP no Codex e manter a configuração do projeto.
- [x] 2.4 Configurar Context7 0.5.5 para Codex via MCP OAuth, sem privilégios de sistema.
- [x] 2.5 Auditar as versões resolvidas e eliminar ou registrar divergências entre pacote e integração instalada.

## 3. OpenSpec e plano vinculante

- [x] 3.1 Inicializar OpenSpec no repositório e criar a mudança `bootstrap-core-foundation`.
- [x] 3.2 Criar proposta, desenho e especificação normativa limitados à Fase 0.
- [x] 3.3 Criar este plano detalhado antes de qualquer framework de produto.
- [x] 3.4 Validar estritamente a mudança e registrar o resultado.

## 4. Graphify e delimitação documental

- [x] 4.1 Gerar o primeiro grafo, preservando backup recuperável quando a execução interrompida invalidar o cache anterior.
- [x] 4.2 Validar integridade estrutural, comunidades, relatório e visualização do grafo inicial.
- [x] 4.3 Consultar o grafo para localizar todos os documentos vinculantes da Fase 0 e confirmar as relações críticas nas fontes.
- [x] 4.4 Registrar o resultado útil da consulta na memória do Graphify.

## 5. Ativação e verificação MCP

- [x] 5.1 Ativar o projeto atual na Serena e registrar a limitação esperada de um repositório ainda sem arquivos analisáveis.
- [x] 5.2 Confirmar Serena e Context7 como habilitados em `codex mcp list`.
- [x] 5.3 Verificar funcionalmente Context7 em nova sessão do Codex com `resolve-library-id` e `query-docs`.
- [x] 5.4 Repetir e registrar o diagnóstico final da Serena e a listagem final de MCPs.

## 6. Fundação mínima do workspace

- [x] 6.1 Criar metadados privados na raiz, sem dependências de produto e sem Nx, com versão do gerenciador de pacotes fixada.
- [x] 6.2 Gerar somente o lockfile nativo aplicável ao workspace realmente inicializado.
- [x] 6.3 Criar verificador determinístico e não mutante para ferramentas, integrações e artefatos obrigatórios.
- [x] 6.4 Confirmar por inventário que nenhuma ferramenta ou funcionalidade expressamente excluída foi adicionada.

## 7. Verificações e coletores

- [x] 7.1 Executar o verificador de instalação e capturar códigos de saída e versões.
- [x] 7.2 Descobrir e executar todos os coletores de testes configurados; registrar baseline zero se nenhum existir.
- [x] 7.3 Executar validações de lockfile e metadados do workspace sem instalar frameworks.
- [x] 7.4 Registrar resultados no log de testes e detalhes de implementação no log correspondente.

## 8. Atualização final do grafo

- [x] 8.1 Atualizar o Graphify após a criação da estrutura inicial do workspace e dos artefatos OpenSpec.
- [x] 8.2 Revalidar nós, arestas, endpoints, comunidades e consultas essenciais do grafo atualizado.
- [x] 8.3 Registrar qualquer divergência restante entre grafo, código e documentação.

## 9. Relatório e gate

- [x] 9.1 Emitir relatório final com arquivos, instalações, escopos, versões, comandos, resultados, MCPs, falhas, pendências e rollback.
- [x] 9.2 Registrar o estado do gate da Fase 0 com evidências e ressalvas documentais.
- [x] 9.3 Encerrar a execução sem iniciar Nx, frameworks, funcionalidades do produto ou qualquer tarefa da Fase 1.
