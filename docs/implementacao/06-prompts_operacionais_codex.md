# Prompts operacionais para IA/Codex

## Executar uma fase

```text
Leia docs/README.md, a hierarquia documental, o escopo, a matriz de suporte,
o DGATE-*, as decisões DEC-*, as evidências EVID-* e a Fase <N> do guia canônico.
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

## Prompt bloqueante para inteligência musical

Antes de implementar extração, harmonização ou watermark, a IA deve responder:

1. qual `operation` está sendo implementada;
2. quais eventos podem ser removidos ou criados;
3. como cada evento de saída recebe provenance;
4. quais hard constraints bloqueiam publicação;
5. onde ocorre review humana;
6. como o resultado é reproduzido e verificado;
7. quais fixtures e métricas provarão o gate.

Se alguma resposta não estiver na documentação, parar, registrar DEC-* e as evidências necessárias. Não preencher lacunas com “melhores práticas” genéricas.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Prompt de pre-mortem antes da implementação

```text
Leia a documentação canônica, a matriz de riscos e qa/19-matriz-falhas-pre-mortem.md.
Para a capacidade solicitada, produza:
1. requisitos e contratos;
2. modos de falha conhecidos e novos;
3. sinais de detecção;
4. comportamento fail-closed;
5. estados de interface;
6. testes, fixtures e observabilidade;
7. decisões DEC-*, evidências EVID-* e gate DGATE-* aplicáveis.
Não escreva código até resolver contradições documentais.
```

## Prompt de fidelidade visual

```text
Use o reference_id indicado em design-reference/reference-manifest.yaml.
Abra especificação, protótipo, story e baseline disponíveis.
Implemente must_have, must_not_have e todos os estados aplicáveis.
Não copie referências externas, não invente seções e não atualize golden sem revisão.
Entregue screenshots e relatório de divergências.
```

## Prompt de revisão musical independente

```text
Não reutilize a função transformadora como oráculo.
Reparse origem e saída, compare invariantes, event mapping e cobertura.
Classifique comissão, omissão, atribuição e apresentação.
Quando não puder provar uma decisão material, retorne revisão/rejeição, não sucesso.
```
