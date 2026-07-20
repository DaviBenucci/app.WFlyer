# Relatório de maturidade — confiabilidade, melodia, harmonização e watermark

> Data: 2026-07-20. Status: informativo; decisões normativas estão nos documentos canônicos referenciados.

## Correção central

Foram separados quatro problemas que não podem compartilhar a mesma promessa de qualidade:

1. transposição determinística;
2. reconhecimento/OMR;
3. extração da linha melódica;
4. harmonização/arranjo criativo.

A transposição pode ser formalmente verificada no perfil suportado. OMR e extração são inferenciais e exigem bloqueio/revisão quando ambíguos. Harmonização cria material novo e deve entregar variantes sujeitas a restrições e escolha humana.

## Entregas documentais

- taxonomia de operações;
- extração polifônica por segmentos com proveniência;
- motor de harmonização condicionado e validado;
- perfis instrumentais de polifonia/extensão;
- backend fail-closed e verificador independente;
- manifesto assinado e níveis de garantia;
- workspace de revisão;
- marca d'água em camadas e verificação;
- gates separados de QA e segurança.

## Impacto no roadmap

O MVP Core MusicXML permanece menor e verificável. Capacidades avançadas entram por trilhas independentes:

```text
M — multipauta/multiparte
L — extração de melodia
H — harmonização
W — watermark/proveniência
```

Nenhuma trilha pode ser habilitada somente porque a interface está pronta.

## Regras adicionais de fidelidade e autoria

- harmonização possui perfil explícito `strict`, `conservative` ou `expressive`;
- andamento e modo não são convertidos automaticamente em rótulos emocionais;
- toda reharmonização aparece como diff e variante separada;
- watermark identifica a emissão pelo serviço, não titularidade da composição;
- créditos e avisos de copyright da fonte não podem ser removidos ou substituídos.

## Risco principal

Prometer “100% confiável para partituras complexas” antes do corpus e do gate criaria risco técnico e reputacional. A documentação passa a exigir prova dentro da matriz, revisão explícita fora dela e comunicação honesta do nível de garantia.
