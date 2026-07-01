# Tela inicial da aplicação

## Rota

```text
/
```

## Objetivo

Permitir que o usuário inicie uma transposição rapidamente, sem transformar a aplicação em landing page institucional.

## Escopo MVP

A tela inicial deve priorizar a ferramenta:

1. CTA para iniciar transposição.
2. Resumo curto do fluxo: upload -> origem -> destino -> processamento -> download.
3. Exemplos musicais objetivos.
4. Aviso claro de que a leitura de PDF pode falhar em arquivos ruins.

## Componentes

- `AppShell`.
- `PageContainer`.
- `PrimaryCTAButton`.
- `HowItWorksSteps`.
- `PopularConversionsGrid`.
- `EmptyState` quando necessário.

## Exemplos sugeridos

```text
Piano -> Trompete Bb: +2 semitons
Trompete Bb -> Piano: -2 semitons
Piano -> Sax Alto Eb: +9 semitons
Trompa F -> Piano: -7 semitons
```

## Regras

- Não exigir login.
- Não prometer leitura perfeita de qualquer PDF.
- Não exibir métricas internas.
- Não usar discurso de marketing como substituto da ferramenta.

## Acessibilidade

- H1 único.
- CTA com nome acessível.
- Ordem de foco lógica.
- Animações decorativas devem respeitar `prefers-reduced-motion`.

## Critérios de aceite

- Usuário consegue iniciar transposição em até 1 clique.
- Mobile exibe CTA principal sem confusão.
- A tela comunica limitações sem alarmismo.
