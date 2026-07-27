# Implementação por IA — instruções operacionais

## Fonte de verdade

A IA deve seguir a hierarquia documental e o guia canônico. Código existente é inspecionado antes de alterar, mas não pode revogar requisito canônico silenciosamente.

## Comportamento obrigatório

- identificar fase/gate;
- ler documentos específicos afetados;
- explicar arquivos e comportamento atual;
- propor plano e testes antes de modificar;
- implementar o menor corte completo;
- atualizar contrato/teste/documentação na mesma mudança;
- registrar evidência e pendências;
- parar em decisão pendente/contradição e informar DEC-*, DGATE-* e EVID-* relacionados.

## Não inventar

```text
endpoints, DTOs, enums ou erros
tabelas/campos/migrations
presets/intervalos musicais
capabilities ou formatos
limites quantitativos finais
engine OMR/renderer
UX que contradiga segurança/escopo
```

## Regras de autenticidade

- componentes respondem a tarefas musicais reais;
- exemplos incluem instrumentos de oitava;
- warnings são acionáveis;
- não preencher tela com dashboard/card sem pergunta operacional;
- linguagem musical correta sem expor diagnóstico interno;
- efeito visual não substitui estado/feedback.

## Registros

Cada tarefa atualiza logs aplicáveis e informa explicitamente testes não executados. Nunca afirmar que código, segurança ou música foram validados apenas por leitura documental.

<!-- TOOLCHAIN-IA-2026-07-21 -->

## Ferramentas obrigatórias do agente

A IA segue `21-fluxo-operacional-ia.md`:

```text
OpenSpec ativo
→ Graphify para impacto
→ Serena para símbolos
→ Context7 somente para dependência externa
→ teste primeiro quando aplicável
→ Nx affected
→ gates ampliados por risco
```

A ausência ou falha de uma ferramenta não autoriza suposição silenciosa. A IA registra a limitação, usa método equivalente auditável e não reduz os gates.
