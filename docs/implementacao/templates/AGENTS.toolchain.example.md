# AGENTS.md — regras de toolchain do W_Flyer

## Ordem obrigatória

1. Trabalhe em uma mudança OpenSpec identificada.
2. Consulte Graphify antes de mudança transversal.
3. Use Serena para localizar e alterar símbolos.
4. Use Context7 apenas para dependências externas e versão instalada.
5. Execute Nx `affected` no ciclo rápido.
6. Amplie testes conforme risco e documentação canônica.
7. Atualize OpenSpec, documentação, logs e Graphify antes de concluir.

## Proibições

- Não inventar contrato, endpoint, estado, migration ou regra musical.
- Não tratar Graphify como fonte de verdade.
- Não usar Context7 para requisito interno.
- Não ler o monorepo inteiro quando Serena/Graphify bastarem.
- Não editar arquivo gerado; executar o gerador.
- Não instalar ferramenta opcional sem ADR/spike.
- Não silenciar teste, typecheck ou lint.
- Não atualizar golden file sem validação semântica/humana aplicável.
- Não declarar conclusão sem comandos e evidências.

## Gates mínimos

```bash
pnpm nx affected -t lint typecheck test
```

Depois, conforme risco: integração, contrato, property, golden, segurança, E2E, visual, acessibilidade e mutation.
