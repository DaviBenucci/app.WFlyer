# Tela Configurações locais

> Revisão: 2026-07-20.

## Rota

```text
/configuracoes
```

## Shell

`UtilityShell`.

## Objetivo

Reunir preferências locais sem parecer painel de conta ou plano.

## Estrutura

```text
Preferências de transposição
  origem padrão
  destino padrão
  formato de saída ativo

Experiência
  redução de movimento
  tema, somente se suportado integralmente

Dados deste navegador
  limpar histórico/preferências
  explicação sobre sessão e servidor
```

Usar seções com dividers. Não envolver cada configuração em card individual.

## Regras

- preferências são conveniência e sempre confirmadas;
- output desabilitado não permanece selecionado;
- não guardar cookie, CSRF, arquivo, URL ou segredo;
- limpar dados locais não apaga servidor;
- tema escuro só aparece se todos os estados estiverem validados;
- respeitar preferência do sistema antes de override local.

## Ações destrutivas

A área de dados possui explicação direta, confirmação e distinção entre:

```text
Limpar referências deste navegador
Apagar arquivos conhecidos no servidor
```

## Fora do Core

Push, conta, plano, sincronização, analytics opt-in, sons e nuvem.

## Critérios de aceite

- interface compacta e legível;
- app funciona sem storage;
- alteração não muda job já criado;
- limpeza descreve efeito real;
- página não sugere que existe conta autenticada.
