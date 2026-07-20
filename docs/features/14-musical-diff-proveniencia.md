# Musical Diff e proveniência navegável

> Status: canônico para trilhas determinísticas, inferenciais e criativas. Revisão: 2026-07-20.

## Objetivo

Entregar uma prova legível do que ocorreu entre artefatos musicais, ligando cada mudança ao evento de origem, regra, modelo, decisão humana e versão.

## Tipos de diff

```text
SEMANTIC_DIFF
NOTATION_DIFF
CREATIVE_DIFF
EDITORIAL_DIFF
METADATA_DIFF
```

- `SEMANTIC_DIFF`: pitch, onset, duração, voz, evento criado/removido.
- `NOTATION_DIFF`: grafia, clave, armadura, oitava escrita, sem alterar som de concerto.
- `CREATIVE_DIFF`: harmonia, contraponto, voicing ou arranjo criado.
- `EDITORIAL_DIFF`: layout, respiração, page turn, dedilhado sugerido.
- `METADATA_DIFF`: créditos, título, copyright, instrumento e manifest.

## Contrato

```ts
type MusicalDiffDTO = {
  diff_id: string
  source_version_id: string
  target_version_id: string
  completeness: 'complete' | 'partial' | 'unavailable'
  change_counts: Record<string, number>
  changes: MusicalChangeDTO[]
  unmapped_regions: MusicalRangeDTO[]
}
```

## Proveniência

Cada mudança referencia:

```text
source_event_ids
target_event_ids
transformation_id
rule/model version
review revision
reason codes
assurance check IDs
```

Notas criadas usam `origin_kind=generated` e nunca simulam origem inexistente.

## Regras

- diff parcial reduz o nível de garantia aplicável;
- mudança de layout não conta como mudança musical;
- normalização interna pode produzir mudanças técnicas, mas o relatório público agrupa sem ocultar impacto;
- compactação de ties ou equivalências semânticas usa comparador especializado;
- diff não deve vazar conteúdo de outra sessão;
- exportação textual é disponibilizada para acessibilidade/auditoria.

## Aceite

- transposição possui mapeamento completo no perfil Core;
- redução lista eventos preservados e descartados;
- harmonização lista todas as notas criadas;
- adaptação mostra alteração por frase/evento;
- o usuário consegue retornar da mudança ao compasso correspondente.
