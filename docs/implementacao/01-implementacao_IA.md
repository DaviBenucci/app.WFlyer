# Implementação IA — instruções operacionais

## Papel do Codex

Transformar a documentação técnica da aplicação `app.WFlyer` em código seguro, testado e incremental quando a fase de implementação começar.

Nesta etapa, a fonte de verdade é:

```text
docs/100-implementacao/guia-codex-app-wflyer.md
```

## Ordem obrigatória

1. Auditoria documental.
2. Estrutura base do projeto.
3. Backend mínimo.
4. Banco de dados.
5. Catálogo de instrumentos.
6. Regra musical e testes unitários.
7. Upload e validação de arquivos.
8. Fila e worker.
9. API de jobs.
10. Frontend funcional mínimo.
11. Tela de processamento e resultado.
12. Download de artefatos.
13. Testes automatizados.
14. Segurança e revisão técnica.
15. Critérios finais do MVP.

## Regra rígida

```text
O Codex só poderá avançar para a próxima fase quando a fase anterior estiver concluída, testada e documentada.
```

## Não inventar sem documentação

- endpoints;
- campos de DTO;
- tabelas;
- status de job;
- regras de transposição;
- rotas frontend;
- estados do wizard;
- mensagens públicas;
- formatos de token;
- funcionalidades futuras.

## Nunca fazer no MVP

- Processar transposição pesada dentro da request HTTP principal.
- Expor stacktrace.
- Expor path físico.
- Expor `storage_key`.
- Salvar segredos no frontend.
- Criar login como dependência inicial.
- Criar pagamento, planos, dashboard administrativo ou biblioteca em nuvem.
- Criar integração Spotify.
- Prometer OMR perfeito para qualquer PDF.

## Registros obrigatórios

Toda fase implementada deve registrar:

- arquivos alterados;
- testes executados;
- resultado;
- falhas e correções;
- pendências;
- decisão técnica nova, se houver.
