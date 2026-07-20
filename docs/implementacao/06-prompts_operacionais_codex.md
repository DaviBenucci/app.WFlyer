# Prompts operacionais para IA/Codex

## Executar uma fase

```text
Leia docs/README.md, a hierarquia documental, o escopo, a matriz de suporte,
as decisões pendentes e a Fase <N> do guia canônico.
Inspecione o código e descreva o comportamento atual, os arquivos afetados,
os riscos e os testes antes de alterar.
Execute somente a Fase <N>. Não habilite capability futura.
Ao final, apresente comandos/resultados, contratos/migrations alterados,
pendências e evidência de cada item do gate. Marque BLOQUEADA se faltar evidência.
```

## Revisar o motor musical

```text
Audite a mudança contra docs/music/01-modelo-transposicao.md,
03-politica-enarmonia-oitavas.md e 05-invariantes-validacao.md.
Verifique componentes diatônico/cromático/oitava, pitch de concerto,
armadura, harmony, ritmo, <transpose> e round trip A->B->A.
Não aprove por comparação textual de XML.
```

## Revisar segurança de arquivo

```text
Audite sessão/CSRF/IDOR, streaming/quarentena, parser XML seguro,
limites estruturais, fila idempotente, sandbox, download e retenção.
Execute o corpus de docs/qa/08-testes-seguranca-arquivos.md.
Não trate MIME/extensão/UUID como controle suficiente isoladamente.
```

## Revisar contrato

```text
Compare OpenAPI, DTOs backend, cliente gerado, frontend e documentação.
Liste breaking changes, enums/erros divergentes e campos internos expostos.
Não edite o cliente gerado manualmente.
```
