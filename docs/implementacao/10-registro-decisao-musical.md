# Registro de decisão musical

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Registrar decisões humanas e algorítmicas que afetam conteúdo musical sem transformar opinião estética em regra universal.

## Estrutura

```yaml
decision_id: MD-0001
revision_id: uuid
region_id: region-17-20
decision_type: MELODY_SELECTION
options_presented:
  - candidate-a
  - candidate-b
selected_option: candidate-a
decided_by: user|reviewer|policy
reason_code: CONTINUITY_OF_MOTIF
free_text_reason: null
input_version: 3
created_at: 2026-07-20T12:00:00Z
supersedes: null
```

## Decisões que exigem registro

- seleção de melodia ambígua;
- confirmação de instrumento/origem OMR;
- mudança de oitava ou simplificação na adaptação;
- escolha de variante harmônica;
- relaxamento explícito de regra estética;
- aprovação de warning material;
- merge de revisão concorrente;
- alteração de curva de tensão ou perfil expressivo.

## Regras

- decisão referencia exatamente a revisão e região exibidas;
- decisão não é reaplicada a material diferente sem confirmação;
- texto livre não substitui `reason_code`;
- uma decisão pode ser superseded, nunca reescrita;
- o backend inclui a decisão na provenance e no manifesto;
- aprovação estética não valida segurança, direitos ou invariantes determinísticos.
