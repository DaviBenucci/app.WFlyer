# Governança dos ativos de marca

> Status: canônico para armazenamento e aprovação dos ativos; não define a logo.

## Separação de responsabilidades

```text
brand/source
→ arquivos-mestre aprovados e editáveis

brand/variants
→ composições derivadas e monocromáticas

brand/favicons
→ exportações técnicas para navegador e instalação

brand/guidelines
→ regras de uso, tamanho, contraste e proteção
```

## Fluxo

```text
briefing
→ propostas identificadas como rascunho
→ comparação e revisão humana
→ checagem de originalidade/licença
→ aprovação
→ arquivos vetoriais finais
→ atualização do brand-manifest
→ exportações
→ distribuição para site e aplicação
```

## Regras

- arquivos antigos removidos não podem reaparecer;
- uma imagem gerada ou esboço não se torna logo por estar no repositório;
- somente caminhos indicados no manifesto podem ser usados em produção;
- o SVG é a fonte principal; PNG e ICO são exportações;
- fontes precisam de licença registrada;
- alterações posteriores exigem nova versão e decisão;
- segredos, certificados e dados empresariais não pertencem à pasta de marca.

## Distribuição

Depois da aprovação:

```text
brand/variants e brand/favicons
→ apps/web/public/brand/ no aplicativo
→ public/brand/ no repositório do site institucional
```

Os projetos consumidores não devem editar os arquivos distribuídos. Uma mudança começa na fonte de verdade da marca e gera novas exportações.
