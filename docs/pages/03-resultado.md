# Tela Resultado

> Revisão: 2026-07-20.

## Rota

```text
/resultado/{job_id}
```

## Objetivo

Apresentar o resultado como conclusão verificável: o que foi transposto, quais avisos existem, quais arquivos podem ser baixados e até quando.

## Shell

`StudioShell`.

## Composição

```text
JobStatusHeader
TranspositionRoute
ResultWorkspace
  Preview/ScoreSurface quando disponível
  ResultInspector
    WarningPanel
    ArtifactList
    ExpirationNotice
    ações
```

Sem preview habilitado, a superfície principal apresenta resumo estrutural e informações do arquivo, sem placeholder que prometa renderização futura.

## Hierarquia

1. estado terminal;
2. origem, destino e intervalo;
3. warnings materiais;
4. arquivo principal;
5. expiração/deleção;
6. ação “Transpor outra”.

## Estados

```text
loading
queued/running/cancel_requested
completed
completed_with_warnings
failed
cancelled
retention_expired_or_purged
not_found_or_other_session
network_unavailable
```

## Warnings

- aparecem antes do download quando materiais;
- podem conter compasso/página quando a API fornecer;
- não usam score bruto de confiança;
- ação recomendada é concreta;
- lista extensa pode ser agrupada, sem esconder severidade.

## Artefatos

`ArtifactRow` contém:

- formato;
- nome;
- tamanho;
- checksum opcional;
- expiração;
- botão de download.

MusicXML transposto é principal. PDF aparece somente quando existente.

## Ações

```text
Baixar MusicXML
Transpor outra partitura
Remover arquivos do servidor
Remover do histórico local
```

As duas últimas ações são distintas e explicadas.

## Movimento

A continuidade do `TranspositionRoute` entre processamento e resultado pode usar Motion `layoutId` ou View Transition progressiva, sem controlar o mesmo elemento por ambas simultaneamente.

Após `completed`/`completed_with_warnings`, uma revelação curta pode recompor tinta na pauta de destino. GSAP controla apenas o SVG da cena; Motion controla warnings e ações. A revelação dura no máximo 700–1100 ms, não atrasa download e não usa confete. Em reduced motion, o resultado aparece por crossfade/troca imediata.

## Critérios de aceite

- refresh recupera com mesma sessão;
- sessão diferente não acessa;
- warning não é tratado como sucesso sem ressalva;
- arquivo expirado não oferece download;
- ação destrutiva exige confirmação;
- resultado mantém identidade do workspace sem virar página de “sucesso” genérica;
- timeline de processamento foi encerrada antes da revelação;
- warnings entram de forma legível e não ficam aguardando animação.
