# Direitos autorais, atribuição e licenças musicais

> Status: canônico de produto e segurança. Revisão: 2026-07-20.

## Princípios

- o usuário declara possuir autorização para processar o material;
- o W_Flyer não transfere titularidade da obra;
- créditos e avisos de copyright existentes são preservados salvo correção explícita;
- material enviado não é usado para treino sem consentimento separado, específico e revogável conforme política;
- outputs identificam conteúdo gerado/adaptado sem substituir autoria original;
- watermark não usa `© W_Flyer` sobre obra de terceiro.

## Metadados

O pipeline compara e preserva, quando suportado:

```text
title
composer
lyricist
arranger
rights
publisher
source
encoding history
```

Mudança/removal material entra no `METADATA_DIFF` e pode bloquear exportação.

## Conteúdo gerado

Harmonização/arranjo registra contribuição da ferramenta no manifesto e em metadado técnico, sem atribuir composição inteira ao W_Flyer.

## Datasets e samples

Cada corpus, fonte musical, soundfont/sample e modelo possui inventário de licença, provenance e obrigação de distribuição. Item sem licença clara não entra em build/benchmark público.

## Compartilhamento

O produto não oferece link público ou biblioteca pública sem mecanismo de direitos, takedown, revogação e abuso definido.

## Retenção

Direitos autorais não justificam retenção indefinida. Aplicam-se minimização e purge documentados.
