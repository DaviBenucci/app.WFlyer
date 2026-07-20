# Estratégia de testes

> Status: canônico. Revisão: 2026-07-20.

## Princípio

O W_Flyer precisa provar quatro propriedades independentes:

1. correção musical;
2. segurança/autorização de documentos;
3. confiabilidade assíncrona;
4. usabilidade/acessibilidade do fluxo.

Cobertura de linhas não substitui nenhuma delas.

## Pirâmide

```text
unit/property: intervalos, catálogo, normalização e estados
component/integration: API, banco, storage, fila, frontend
contract: OpenAPI/cliente/DTOs
golden/semantic: MusicXML e resultados esperados
security corpus: XML/MXL/PDF/IDOR/CSRF/DoS
E2E: fluxos reais do usuário
performance/soak: limites antes de produção/PDF
```

## Gates do Core

- todos os presets e pares preservam altura de concerto;
- fixtures Core passam no comparador semântico;
- parser rejeita corpus hostil sem rede/leitura local/exaustão;
- A não acessa recursos de B;
- reentrega/retry não duplica job/artefato;
- downloads e purge respeitam retenção;
- cliente OpenAPI não diverge;
- fluxo E2E MusicXML funciona em desktop/mobile/teclado;
- nenhum warning/erro interno vaza.

## Ambientes

- banco/Redis/storage reais em integração via containers;
- engines externas fixadas por versão;
- relógio controlável para expiração;
- seed/corpus versionado;
- sem depender de rede pública nos testes.

## Evidência

Cada execução registra comando, commit, ambiente, versões, fixtures, resultado e falhas em `../logs/TEST_LOG.md`. Teste não executado deve ter motivo; não pode ser declarado como aprovado.

## PDF/OMR

Possui gate separado com corpus representativo, métricas definidas antes da avaliação, sandbox, performance e revisão de falsos positivos/negativos. Aprovar Core não aprova PDF.
