# Estratégia de testes do MVP

## Objetivo

Garantir que a aplicação comece a ser codada com testes para regra musical, backend, frontend e segurança.

## Testes musicais obrigatórios

- Piano C -> Trompete Bb.
- Trompete Bb -> Piano C.
- Piano C -> Sax Alto Eb.
- Sax Alto Eb -> Piano C.
- Clarinete Bb -> Sax Alto Eb.
- Trompa F -> Piano C.
- Mesmo instrumento -> mesmo resultado.
- Transposição com acidentes.
- Transposição com acordes.
- Transposição com armadura de clave.

## Testes de backend obrigatórios

- `/health` responde.
- Upload válido é aceito.
- Upload inválido é rejeitado.
- Arquivo grande é rejeitado.
- Job é criado.
- Job muda de status.
- Worker processa job.
- Erro no worker não quebra API.
- Download só funciona para artefato válido.
- Arquivo expirado não pode ser baixado.

## Testes de frontend obrigatórios

- Usuário consegue enviar arquivo.
- Usuário consegue selecionar instrumento de origem.
- Usuário consegue selecionar instrumento de destino.
- Usuário vê status de processamento.
- Usuário vê erro amigável.
- Usuário consegue baixar resultado.
- Fluxo funciona em mobile.
- Fluxo funciona com teclado.

## Testes de segurança obrigatórios

- Não expor stacktrace.
- Não expor caminho interno do arquivo.
- Não aceitar extensão perigosa.
- Não aceitar MIME inválido.
- Não aceitar payload malformado.
- Rate limit documentado.
- Validações documentadas.

## Evidência

Quando houver código, cada fase deve registrar:

```text
data
fase
arquivos alterados
comandos executados
resultado
falhas
correções
pendências
```

Nenhum teste deve ser declarado como executado sem evidência.
