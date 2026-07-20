# Checklist pre-mortem antes de implementar uma capacidade

> Status: bloqueante. Revisão: 2026-07-20.

- [ ] operação classificada como determinística, inferencial ou criativa;
- [ ] matriz de suporte definida;
- [ ] eventos/artefatos de entrada e saída definidos;
- [ ] invariantes rígidos listados;
- [ ] ambiguidades e review definidos;
- [ ] erros públicos e internos definidos;
- [ ] riscos adicionados ao registro;
- [ ] casos da matriz de falhas aplicáveis selecionados;
- [ ] corpus e licenças definidos;
- [ ] métricas e limiares definidos antes do benchmark;
- [ ] feature flag inicia `off`;
- [ ] rollback/kill switch planejado;
- [ ] API, banco e estados desenhados;
- [ ] UX cobre happy path e falhas;
- [ ] referência visual interna existe;
- [ ] acessibilidade/reduced motion consideradas;
- [ ] provenance/diff definidos;
- [ ] privacidade, copyright e retenção revisados;
- [ ] owner técnico e musical definidos;
- [ ] gate de aceite e evidência definidos.

Sem todos os itens aplicáveis, a fase permanece `BLOQUEADA`.
