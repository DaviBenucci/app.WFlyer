# Glossário do W_Flyer

> Status: canônico. Revisão: 2026-07-20.

## Altura escrita

Altura notada para o instrumentista.

## Altura de concerto

Altura sonora real usada para comparar instrumentos.

## Intervalo `written_to_concert`

Transformação que deve ser adicionada à altura escrita para obter a altura de concerto. No W_Flyer ela é composta por:

- `diatonic_steps`: passos de letra musical, sem contar a parcela de oitava;
- `chromatic_semitones`: semitons, sem contar a parcela de oitava;
- `octave_change`: oitavas completas.

Exemplo para trompete em Bb:

```json
{
  "diatonic_steps": -1,
  "chromatic_semitones": -2,
  "octave_change": 0
}
```

## Intervalo escrito de saída

Diferença entre a transformação da origem e a transformação do destino:

```text
output_interval = source.written_to_concert - target.written_to_concert
```

A subtração é feita em cada componente.

## MusicXML bruto

MusicXML recebido do usuário ou produzido pelo OMR, antes da normalização do W_Flyer.

## MusicXML normalizado

Representação canônica validada, com estrutura e metadados coerentes para o motor musical.

## OMR

Optical Music Recognition. Conversão de uma imagem de partitura para representação simbólica. Não é OCR textual e não é determinístico em todos os documentos.

## Parte e pauta

Uma parte representa um instrumento/voz no score. Uma pauta é a estrutura de cinco linhas na qual a parte é notada. O MVP Core aceita uma parte e uma pauta por job.

## Grafia enarmônica

Escolha entre notas de mesma altura sonora, como F# e Gb. A grafia depende do intervalo diatônico e da tonalidade, não apenas do número de semitons.

## Job

Solicitação assíncrona de processamento. `status`, `stage` e `retention_status` são conceitos distintos.

## Sessão anônima

Identidade temporária, sem conta, usada para autorizar o acesso aos objetos criados pelo navegador.

## Artefato

Arquivo versionado do pipeline, interno ou público. Exemplos: original, MusicXML normalizado, MusicXML transposto e PDF renderizado.

## Aviso público

Código categórico e mensagem segura que comunica incerteza ou limitação sem revelar métricas internas.

## Gate

Conjunto objetivo de critérios que bloqueia a progressão ou a ativação de uma capacidade.

## Operação musical

Tipo explícito de transformação: `TRANSPOSE`, `EXTRACT_MELODY`, `REDUCE_TO_MONOPHONIC`, `HARMONIZE` ou `ARRANGE_FOR_INSTRUMENT`.

## Extração de melodia

Seleção inferencial e auditável de uma linha principal em material polifônico. Não cria notas.

## Redução monofônica

Conversão de uma linha confirmada para uma única voz executável, com política explícita para oitava e range.

## Harmonização

Criação de notas, acordes ou vozes de acompanhamento condicionadas a uma melodia e perfil. É uma proposta criativa, não uma verdade única.

## Polifonia instrumental

Capacidade e restrições do instrumento para executar notas simultâneas. Pode ser monofônica, limitada ou polifônica.

## Proveniência de evento

Relação entre cada evento de saída, seus eventos de origem e a regra/modelo que o produziu.

## Nível de garantia

Classificação pública baseada em validação estrutural, confirmação da fonte, prova da transformação e aceite de conteúdo criativo.

## Marca d'água forense

Identificação pseudônima distribuída na saída renderizada e vinculada a hash/manifesto. Serve para rastreabilidade; não é impossível de remover.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Grafo semântico musical

Representação interna versionada de partes, pautas, vozes, medidas, eventos, relações e ocorrências. É derivada do MusicXML normalizado e precisa suportar round trip dentro da matriz habilitada.

## Evento musical e ocorrência

Evento é a entidade semântica — por exemplo, uma nota ou marca de ensaio. Ocorrência é uma execução desse evento após expandir repetições, voltas ou saltos no mapa de playback.

## Musical Diff

Comparação semântica entre revisões que classifica preservação, transformação, seleção, remoção e criação de eventos, separando mudança musical de mudança apenas gráfica.

## Adaptação idiomática

Transformação explícita que procura tornar a escrita executável e natural para um instrumento sem confundi-la com transposição. Pode alterar registro, distribuição, respiração, voicing ou articulação dentro de um orçamento aprovado.

## Tocabilidade

Avaliação contextual de possibilidade física, dificuldade e idiomatismo, considerando instrumento, andamento, duração, registro, técnica e nível do intérprete.

## Região analítica

Intervalo temporal do documento no qual uma decisão de forma, frase, tonalidade, modo, cadência, melodia ou harmonia é válida.

## Curva de tensão

Representação controlada de repouso, crescimento, clímax, suspensão e resolução por região. Não é inferência automática de emoção do autor.

## Score following

Sincronização entre tempo de reprodução e elementos da partitura por meio do mapa de ocorrências. Não significa reconhecimento de performance ao vivo, salvo capability específica.

## Engraving

Preparação visual da notação: espaçamento, colisões, quebras, viradas, tamanhos, glifos, hierarquia e legibilidade.

## Golden reference

Exemplo interno versionado composto por especificação, protótipo/story, estados e baseline visual. Orienta a IA sem autorizar cópia de produto externo.

## Pre-mortem

Análise antes da implementação que presume a falha do sistema e enumera causas, sinais, controles, testes e comportamento seguro.

## Falha desconhecida

Defeito não registrado anteriormente. Ao ser descoberto, recebe ID, fixture, causa raiz, controle, teste e avaliação de abrangência.

## Conselho musical

Grupo de revisores qualificados por instrumento/área que aprova perfis, corpus, critérios subjetivos e gates de release avançado.

## Termos adicionados na expansão crítica

- **Musical Diff:** representação semântica das relações e mudanças entre duas revisões, por evento.
- **Event provenance:** origem de um evento preservado, alterado, removido ou criado.
- **Adaptation budget:** conjunto explícito de alterações permitidas em uma adaptação instrumental.
- **Playability finding:** diagnóstico versionado de impossibilidade, dificuldade, desconforto ou não idiomatismo.
- **Instrument capability profile:** modelo de alcance, tessitura, polifonia, sustain, respiração, técnicas e limites práticos.
- **Analysis region:** trecho musical com hipótese tonal, modal, formal ou melódica e sua incerteza.
- **Tension curve:** descrição relativa e editável de repouso, movimento, crescimento, clímax e resolução; não é detector de emoção.
- **Playback graph:** ordem executada de eventos depois de repetições, voltas, saltos e coda.
- **Playback Manifest:** mapa versionado de evento, ocorrência, tempo e localização visual usado por reprodução e score following.
- **Canonical score graph:** grafo semântico comum do qual score e partes são projetados.
- **Musical Decision Record (MDR):** registro da decisão musical, alternativas, evidência, limite e aprovadores.
- **Pre-mortem:** análise antecipada de como uma capacidade pode falhar antes de implementá-la.
- **Fail-closed:** diante de ambiguidade ou falha material, não publicar resultado como seguro.
- **Residual risk:** risco que permanece depois dos controles e precisa de aceite explícito.
- **Golden reference:** referência interna aprovada para composição, estado ou comportamento visual.
