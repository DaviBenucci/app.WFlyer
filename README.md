# WFlyer — Documentação técnica da aplicação

Este repositório documenta a aplicação `app.WFlyer`: uma ferramenta web para receber uma partitura, escolher instrumento de origem, escolher instrumento de destino, calcular a transposição musical correta, processar o arquivo de forma assíncrona e entregar um resultado baixável.

Esta etapa é somente documental. Não há implementação de código de produção neste pacote.

## Escopo atual

O WFlyer deve começar como um MVP sem login obrigatório, focado na transposição musical:

1. upload de partitura;
2. seleção manual do instrumento de origem;
3. seleção manual do instrumento de destino;
4. criação de job de processamento;
5. acompanhamento de status;
6. motor musical centralizado;
7. resultado final baixável;
8. mensagens claras de erro;
9. validação de arquivo;
10. testes musicais, backend e frontend.

O escopo canônico está em `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`.

## Estratégia de formato

O início do desenvolvimento deve seguir a decisão MusicXML-first:

```text
Fase 1: MusicXML-first para validar o motor musical.
Fase 2: PDF simples com pipeline de leitura controlado.
Fase 3: PDF real com validação, avisos e revisão assistida.
```

PDF é importante para o usuário final, mas não deve ser prometido como leitura perfeita de qualquer partitura. PDFs escaneados, manuscritos, tortos ou com baixa qualidade devem gerar erro amigável quando a aplicação não conseguir ler a partitura com confiança.

## Regra musical central

A regra universal de transposição é:

```text
intervalo_escrito = origem.written_to_concert - destino.written_to_concert
```

Exemplo:

```text
Piano C -> Trompete Bb
origem.written_to_concert = 0
destino.written_to_concert = -2
intervalo = 0 - (-2) = +2 semitons
```

A transposição deve alterar notas, acordes, acidentes, armadura de clave, tonalidade escrita, partes individuais quando houver múltiplos instrumentos e metadados musicais relevantes. Não basta alterar o nome da tonalidade.

Documento detalhado: `W-Flyer_Regra-Transposição.md`.

## Fora do MVP inicial

Não são dependências do MVP:

- login;
- biblioteca em nuvem;
- planos pagos;
- assinatura;
- dashboard administrativo;
- colaboração entre usuários;
- editor visual completo de partitura;
- detecção automática perfeita de instrumento;
- detecção automática perfeita de tonalidade;
- OMR perfeito para qualquer PDF;
- aplicativo mobile nativo;
- integração Spotify;
- site institucional ou landing page.

## Estrutura de código esperada

```text
app-wflyer/
  apps/
    web/
      src/
        app/
        components/
        features/
        services/
        hooks/
        lib/
        styles/
        tests/
    api/
      src/
        modules/
        routes/
        services/
        workers/
        repositories/
        validators/
        middlewares/
        tests/
  packages/
    shared/
      src/
        types/
        constants/
        music/
        validation/
    ui/
      src/
        components/
  docs/
```

Detalhe de responsabilidades: `docs/backend/13-estrutura-pastas.md`.

## Documentos principais

- Escopo e MVP: `docs/00-visao-geral/05-escopo-mvp-app-wflyer.md`
- Decisões arquiteturais: `docs/00-visao-geral/01-decisoes-arquiteturais.md`
- Roadmap técnico: `docs/00-visao-geral/02-roadmap-fases.md`
- Stack recomendada: `docs/00-visao-geral/04-stack-recomendada.md`
- Contratos de API: `docs/backend/03-endpoints-api.md`
- Modelo de dados: `docs/backend/04-modelagem-banco.md`
- Pipeline assíncrono: `docs/backend/05-pipeline-processamento.md`
- Fila e worker: `docs/backend/07-filas-e-workers.md`
- Catálogo de instrumentos: `docs/features/11-catalogo-instrumentos-mvp.md`
- Acessibilidade: `docs/frontend/06-acessibilidade.md`
- Testes: `docs/qa/01-estrategia-testes.md`
- Guia Codex: `docs/100-implementacao/guia-codex-app-wflyer.md`
- Critérios de aceite: `docs/100-implementacao/criterios-aceite-mvp.md`

## Regra rígida para Codex

```text
O Codex só poderá avançar para a próxima fase quando a fase anterior estiver concluída, testada e documentada.
```

Se surgir imprevisto, o Codex deve resolver dentro da fase atual, registrar a decisão e somente depois avançar.

## Escopo proibido nesta documentação

Esta documentação da aplicação não deve conter instruções de publicação online, domínio, DNS, hospedagem, servidor de produção ou integração Spotify. Qualquer material desse tipo deve ficar em documento separado e explicitamente marcado como fora do escopo da aplicação `app.WFlyer`.
