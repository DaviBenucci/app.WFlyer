# Modo de ensaio

> Status: canônico para trilha futura. Revisão: 2026-07-20.

## Objetivo

Transformar um resultado aprovado em ferramenta de prática e performance, sem sobrecarregar o fluxo de transposição.

## Rota prevista

```text
/ensaio/{version_id}
```

## Composição

```text
RehearsalTopBar
ScoreViewport
PlaybackCursor
AnnotationLayer
RehearsalTransport
OptionalPartMixer
```

## Capacidades

- tela sem distrações;
- zoom e reflow dentro do que o renderer suportar;
- loop por compasso/frase;
- contagem de entrada;
- andamento variável;
- metrônomo;
- solo/mute por parte;
- marcações pessoais em camada separada;
- navegação por pedal/teclado;
- passagem automática opcional;
- modo paisagem/tablet;
- setlist futuro.

## Virada de página

A aplicação pode sugerir pontos de virada com base em pausas e densidade, mas não deve alterar a partitura automaticamente sem preview. Para performance, uma virada ruim é falha de usabilidade material.

## Offline

Offline só é habilitado quando:

- o usuário pediu armazenamento local;
- licença dos assets permite;
- artefatos estão criptografados/isolados conforme plataforma;
- expiração e revogação possuem comportamento documentado;
- o produto deixa claro o que continuará disponível.

## Anotações

Anotações não modificam o MusicXML canônico. Cada marcação usa coordenada semântica quando possível:

```text
part_id + measure_id + event_id + anchor_type
```

Coordenada puramente visual exige estratégia de remapeamento após reflow/renderização.

## Performance

- pré-carregar somente páginas/regiões próximas;
- manter áudio fora do ciclo de render React crítico;
- pausar animações decorativas;
- não re-renderizar toda partitura a cada tick;
- usar cursor em camada separada;
- testar tablets e orientação.

## Critérios de aceite

- controles essenciais funcionam por teclado e toque;
- score following pode ser desligado;
- nenhuma animação decorativa compete com leitura;
- uma falha de áudio não remove acesso à partitura;
- anotações sobrevivem a refresh e estão vinculadas à versão correta.
