# MusicXML canônico

> Status: canônico. Revisão: 2026-07-20.

## Papel no sistema

MusicXML normalizado é a representação canônica entre leitura e transposição. O original nunca é sobrescrito.

```text
original
-> raw_musicxml
-> normalized_musicxml
-> transposed_musicxml
-> rendered_pdf opcional
```

## Perfil de entrada do MVP Core

- MusicXML 3.1 ou 4.0;
- XML não comprimido;
- elemento raiz `score-partwise`;
- uma parte;
- uma pauta;
- notação afinada em 12-TET;
- sem recursos externos necessários para interpretar a música.

`score-timewise`, `opus`, MXL, múltiplas partes e múltiplas pautas ficam fora do Core.

## Parsing seguro

O parser deve:

- desabilitar resolução de entidades externas;
- desabilitar XInclude e acesso de rede;
- usar schemas e catálogos locais quando validar;
- impor limites de bytes, profundidade, nós, medidas, eventos e texto;
- interromper em XML malformado;
- não usar modo de recuperação silenciosa;
- não executar XSLT, scripts ou links externos;
- rejeitar namespaces/raízes não reconhecidos.

Um `DOCTYPE` não pode causar acesso externo. A implementação pode rejeitá-lo ou aceitá-lo com resolução totalmente desabilitada; a escolha deve ser testada e registrada.

## Normalização

O normalizador deve produzir uma saída determinística o suficiente para comparação semântica:

1. identificar versão e raiz;
2. validar o perfil estrutural;
3. canonicalizar IDs internos quando necessário;
4. normalizar duração/divisions sem alterar tempo musical;
5. validar vozes, ties, tuplets e compassos;
6. normalizar instrumento e `<transpose>` da origem;
7. preservar elementos suportados não transformados;
8. registrar elementos descartados ou não suportados;
9. exportar MusicXML 4.0;
10. calcular hash SHA-256 do artefato.

## Artefatos

| Tipo | Visibilidade | Finalidade |
|---|---|---|
| `input_original` | interna | Evidência imutável do upload. |
| `raw_musicxml` | interna | Entrada XML ou saída bruta do OMR. |
| `normalized_musicxml` | interna | Fonte canônica do motor. |
| `transposed_musicxml` | pública | Resultado principal. |
| `rendered_pdf` | pública condicional | Resultado renderizado. |
| `processing_report` | interna | Métricas, versões e avisos técnicos. |

## Preservação e perda aceitável

A prioridade é semântica musical. Layout, paginação, posições absolutas, fontes e metadados proprietários podem mudar durante o round-trip. Toda perda conhecida deve:

- estar fora da matriz de garantia; ou
- gerar aviso; ou
- bloquear o job se afetar significado musical.

## Validação de saída

A saída só pode se tornar pública quando:

- o XML é bem formado;
- passa pelo perfil/schema local definido;
- possui uma parte e uma pauta;
- contém ao menos um evento musical válido;
- cumpre os invariantes de `05-invariantes-validacao.md`;
- o hash e o tamanho foram registrados;
- o artefato foi gravado de modo atômico.

## MXL

MXL é um container ZIP, não apenas outro MIME. Quando habilitado, deve validar `META-INF/container.xml`, rootfile, paths, quantidade de entries, tamanho descompactado, taxa de compressão, arquivos aninhados e referências. A feature permanece desabilitada até o gate específico.
