# Pacote de referências visuais do W_Flyer

> Status: governança de referências visuais. Revisão: 2026-07-27.

Este diretório contém referências internas próprias. Ele não é um catálogo de screenshots de terceiros.

## Ordem

1. `reference-manifest.yaml`;
2. protótipo interno executável;
3. story aprovada no código quando existir;
4. specification da página/componente;
5. screenshot golden gerado no ambiente controlado.

Segurança, domínio musical e acessibilidade prevalecem sobre qualquer referência visual.

## Protótipos

Abra `prototypes/index.html` em navegador. Os protótipos são referências de composição e hierarquia, não código pronto para produção. Eles não substituem Next.js, componentes acessíveis, API real ou testes.

## Assets de terceiros

Não adicionar screenshots, fontes, logos, ilustrações ou código externo sem licença/proveniência. Estudos externos devem ser textuais ou usar wireframes próprios.

## Alterações

Mudança em item `binding` exige:

- motivo;
- revisão visual;
- atualização do manifest/specification;
- novo baseline;
- changelog/decisão quando alterar identidade.

## Aprovação

`approval-register.yaml` registra a aprovação humana. Os screenshots atuais são candidatos originais do W_Flyer gerados a partir dos protótipos estáticos e estão com `pending_product_owner`; servem para orientar composição e revelar lacunas, mas não significam UI de produção aprovada.

## Cobertura

`state-coverage.yaml` lista estados e pendências de implementação. Uma página não está pronta apenas porque possui screenshot do estado principal.

## Baselines incluídos

Cada página principal possui captura desktop e mobile em `golden-pages/<slug>/`. Baselines futuros devem ser gerados em ambiente fixado e revisados junto com teclado, foco, zoom, contraste e reduced motion.

## Baselines documentais incluídos

O pacote contém nove protótipos de página e dezoito PNGs desktop/mobile gerados localmente a partir deles:

- Home;
- workspace de transposição;
- revisão de melodia;
- comparação/Musical Diff;
- laboratório de harmonização;
- modo de ensaio;
- processamento com falha transitória;
- upload incompatível;
- pacote ensemble.

Os hashes e dimensões estão em `baseline-manifest.json`.

Status atual:

```text
referências do Core: orientação de composição sujeita a aprovação humana
referências com status=reference: futuras; não autorizam implementação
pixel baseline: candidato; requer revisão humana do produto
automação/implementação: inexistente nesta entrega
```

Uma referência com `capability_status: disabled` não pode gerar rota, botão ativo, endpoint, feature flag ligada ou código funcional. Ela existe apenas para evitar que a arquitetura futura seja esquecida.

A primeira implementação em Storybook deve comparar-se a estes baselines, registrar divergências justificadas e produzir o baseline de produção aprovado. Não atualizar PNG apenas para silenciar CI.
