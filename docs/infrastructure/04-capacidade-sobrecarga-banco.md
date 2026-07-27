# Capacidade e prevenção de sobrecarga do banco

> Status: arquitetura proposta; decisões de produção dependem de ADR, orçamento e benchmark. Revisão: 2026-07-27.

## 1. O que não vai para o PostgreSQL

- PDFs;
- imagens;
- MusicXML grande como blob principal quando puder ficar no storage;
- artefatos renderizados;
- logs brutos ilimitados.

O banco guarda metadados, estado, ownership, hashes e referências.

## 2. Proteções

- connection pool com limites;
- timeout de conexão e statement;
- paginação obrigatória;
- índices baseados em queries reais;
- limites de payload;
- batch controlado;
- cache somente para leitura apropriada;
- filas para trabalho pesado;
- retenção/particionamento de eventos;
- `EXPLAIN` em queries críticas;
- métricas de lock, CPU, IOPS e conexões.

## 3. Backpressure

Quando a capacidade atingir limiar:

- reduzir novos jobs por plano/usuário;
- retornar `429` ou estado de fila com retry-after;
- não continuar abrindo conexões;
- preservar consultas de status/download;
- escalar workers sem escalar banco indiscriminadamente.

## 4. Migrações

- expand/contract;
- sem alteração destrutiva no mesmo deploy;
- índice concorrente quando suportado;
- backup antes de mudança de alto risco;
- rollback testado;
- migrations em staging com volume representativo.

## 5. Testes

- pico de criação de jobs;
- polling excessivo;
- eventos de webhook em massa;
- fila acumulada;
- consulta de histórico profundo;
- purge/retention;
- failover e reconnect.
