# Roadmap técnico do MVP

## Regra de progressão

```text
O Codex só poderá avançar para a próxima fase quando a fase anterior estiver concluída, testada e documentada.
```

O guia operacional detalhado está em `docs/100-implementacao/guia-codex-app-wflyer.md`.

## Fases

| Fase | Nome | Resultado esperado |
|---:|---|---|
| 0 | Auditoria documental | Escopo técnico revisado e sem mistura com requisitos fora do MVP. |
| 1 | Estrutura base do projeto | Separação clara entre frontend, backend, pacotes compartilhados e docs. |
| 2 | Backend mínimo | API base, health, erro padrão e módulos iniciais. |
| 3 | Banco de dados | Tabelas mínimas e status documentados. |
| 4 | Catálogo de instrumentos | Instrumentos mínimos com `written_to_concert`. |
| 5 | Regra musical e testes unitários | Fórmula central e testes MusicXML-first. |
| 6 | Upload e validação de arquivos | Upload seguro com tipos permitidos e limites. |
| 7 | Fila e worker | Job processado fora da requisição HTTP. |
| 8 | API de jobs | Status, progresso, eventos públicos e artefatos. |
| 9 | Frontend funcional mínimo | Usuário cria job pela interface. |
| 10 | Tela de processamento e resultado | Status acessível, erro claro e resultado. |
| 11 | Download de artefatos | Download controlado e bloqueio de expirado. |
| 12 | Testes automatizados | Matriz musical, backend, frontend e segurança. |
| 13 | Segurança e revisão técnica | Upload, erros, logs, rate limit, timeout e tokens revisados. |
| 14 | Critérios finais do MVP | Aceite objetivo registrado. |

## Fases futuras separadas

As frentes abaixo não fazem parte do MVP inicial:

- login;
- histórico em nuvem;
- biblioteca;
- planos pagos;
- assinatura;
- dashboard administrativo;
- colaboração entre usuários;
- editor visual completo;
- detecção automática perfeita de instrumento;
- detecção automática perfeita de tonalidade;
- OMR perfeito para qualquer PDF;
- aplicativo mobile nativo;
- integração Spotify.
