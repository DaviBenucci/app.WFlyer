# Engraving, layout e legibilidade

> Status: canônico para trilha R. Revisão: 2026-07-20.

## Princípio

Correção semântica e qualidade editorial são gates distintos. Um MusicXML correto pode gerar PDF ilegível; um PDF bonito pode representar música errada.

## Verificações automáticas

- colisão entre notas, acidentes, claves, cifras, letras e dinâmicas;
- espaçamento insuficiente;
- slurs/ties desconectados;
- beams e tuplets inconsistentes;
- quebra de sistema em local proibido;
- page turn sem pausa suficiente;
- marcas de ensaio ausentes/desalinhadas;
- tamanho de pauta abaixo do perfil;
- watermark em safe zone;
- clipping ou conteúdo fora da página.

## Políticas

```text
score_layout_policy
part_layout_policy
rehearsal_layout_policy
preview_layout_policy
watermark_layout_policy
```

Cada uma é versionada. Layout original é preservado por melhor esforço, não por cópia cega de coordenadas incompatíveis.

## Revisão humana

Detecção geométrica não reconhece toda ambiguidade de leitura. O gate de release inclui amostra impressa/tela e músicos revisores.

## Page turns

A sugestão considera pausas, andamento, densidade e contexto de performance. Uma virada ruim pode ser `warning` ou `blocking` conforme perfil profissional.

## Fontes musicais

Glifos seguem SMuFL quando suportado. Fonte, licença e versão são fixadas; fallback não pode trocar símbolo por caractere incorreto.

## Gate

- render determinístico no ambiente de baseline;
- zero clipping no corpus;
- detector de colisão com fixtures;
- regressão visual;
- revisão de partes e impressão;
- PDF e MusicXML vinculados por hash/manifest.
