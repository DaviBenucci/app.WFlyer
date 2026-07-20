# Princípios de controle humano e autoridade musical

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Definir onde a aplicação pode agir automaticamente, onde deve pedir confirmação e como registrar decisões do músico.

## Classes de decisão

| Classe | Exemplo | Automação permitida | Publicação |
|---|---|---|---|
| Determinística | transpor pitch escrito preservando concerto | automática após invariantes | `TRANSFORMATION_VERIFIED` |
| Inferencial | escolher melodia principal | automática apenas sem ambiguidade material | exige review quando necessário |
| Criativa | criar harmonia, voicing ou arranjo | gerar alternativas | usuário escolhe/aprova |
| Editorial | quebra de sistema, página, respiração sugerida | sugestão e preview | aceite conforme impacto |
| Autoral | alterar melodia, frase, forma ou letra | nunca silenciosamente | consentimento explícito e nova versão |

## Autoridades

```text
backend determinístico -> fatos de transformação
analisadores -> evidências e candidatos
validadores -> bloqueios e warnings
usuário músico -> decisões inferenciais e criativas
revisor especialista -> gate de corpus/release
frontend -> apresentação; nunca autoridade musical
```

## Regras

1. Toda decisão humana cria revisão imutável com autor, timestamp e base revision.
2. A UI mostra o que foi sugerido, o que foi confirmado e o que foi criado.
3. Um override humano não apaga o warning original; registra justificativa.
4. Um override não pode violar integridade estrutural, segurança ou impossibilidade física rígida sem mudar o perfil/capability.
5. A mesma região pode ter estados diferentes; não reduzir incerteza a um único score global.
6. A aplicação nunca usa silêncio do usuário como aprovação.
7. Regenerar uma variante não sobrescreve a anterior.
8. Ações destrutivas ou autorais exigem preview do diff.

## Níveis de intervenção

```text
AUTO_SAFE
AUTO_WITH_NOTICE
REVIEW_REQUIRED
USER_CHOICE_REQUIRED
EXPERT_REVIEW_REQUIRED
REJECTED
```

O nível é derivado por política versionada e pode variar por região. `AUTO_SAFE` só é permitido dentro do perfil testado.

## Explicação mínima

Uma sugestão deve responder, em linguagem adequada ao músico:

- qual região foi analisada;
- qual hipótese foi adotada;
- quais evidências pesaram;
- quais alternativas existiam;
- qual impacto a escolha produz;
- como ouvir ou visualizar a diferença;
- como desfazer.

## Conflitos

Se duas revisões partirem da mesma base, a segunda não sobrescreve a primeira. O backend retorna conflito de revisão e oferece comparação/merge apenas quando os tipos de alteração forem compatíveis.

## Critérios de aceite

- não existe publicação por timeout de review;
- decisões estão vinculadas ao hash da fonte e à revisão base;
- a UI diferencia “sugestão”, “confirmação” e “resultado verificado”;
- o histórico permite retornar a uma versão anterior;
- conteúdo criativo nunca recebe selo de transformação determinística.
