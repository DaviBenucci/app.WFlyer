# Falhas desconhecidas e resposta a incidentes

> Status: canônico. Revisão: 2026-07-20.

## Princípio

Exceção desconhecida não é um caso de sucesso. Quando houver possibilidade de alteração musical silenciosa, acesso indevido, corrupção, autoria incorreta ou artefato incompleto, a resposta padrão é fail-closed.

## Fluxo

```text
falha detectada
→ interromper publicação/download quando necessário
→ preservar hashes, manifestos e logs mínimos
→ classificar impacto e alcance
→ desabilitar capability/estrato por flag
→ comunicar sem expor conteúdo
→ criar incident_id e próximo PM-*
→ produzir fixture mínima
→ corrigir causa e detector
→ executar regressão estratificada
→ revisar documentação/gates
→ rollout gradual
```

## Conteúdo preservado

Preferir metadados não sensíveis:

- IDs internos;
- hashes;
- versões de engine/schema;
- estágio;
- classe da exceção;
- contagens estruturais;
- correlation ID.

Não copiar partitura, letra, nome pessoal ou arquivo completo para logs. Quando conteúdo for indispensável à investigação, usar storage de incidente com acesso e retenção específicos.

## Publicação e revogação

Se um resultado possivelmente incorreto já foi publicado:

1. marcar artefato/revisão como `revoked` sem apagar prova;
2. impedir novos downloads;
3. informar usuários afetados quando identificáveis;
4. preservar a cadeia de hashes;
5. gerar nova revisão somente após reprocessamento;
6. não substituir bytes sob o mesmo artifact ID.

## Post-incident obrigatório

- causa raiz técnica e de processo;
- por que controles existentes não detectaram;
- novo `PM-*`;
- fixture e teste;
- métrica/alerta;
- impacto nos estratos;
- decisão de reativação;
- atualização do changelog e do risco residual.
