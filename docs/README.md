# Documentação técnica do W_Flyer

> Status: canônica após revisão técnica de 2026-07-20.

Esta pasta é a fonte normativa para a implementação do W_Flyer. O produto é uma aplicação web que recebe uma parte musical, converte-a para uma representação MusicXML controlada, transpõe a escrita entre instrumentos e entrega artefatos para revisão e download.

## Ordem de leitura obrigatória

1. `00-visao-geral/08-hierarquia-documental.md`
2. `00-visao-geral/05-escopo-mvp-app-wflyer.md`
3. `00-visao-geral/06-matriz-suporte-mvp.md`
4. `frontend/00-direcao-visual-wflyer.md`
5. `frontend/15-arquitetura-motion-e-bibliotecas.md`
6. `frontend/16-animacao-assinatura-tinta-transposicao.md`
7. `music/01-modelo-transposicao.md`
8. `music/02-musicxml-canonico.md`
9. `backend/03-endpoints-api.md`
10. `backend/04-modelagem-banco.md`
11. `backend/16-maquina-estados.md`
12. `security/02-checklist-seguranca.md`
13. `qa/01-estrategia-testes.md`
14. `100-implementacao/guia-codex-app-wflyer.md`

## Regra de interpretação

- Documentos marcados como **canônicos** definem comportamento obrigatório.
- Documentos de página e feature detalham UX, mas não podem contradizer escopo, modelo musical, API ou segurança.
- Arquivos em `logs/` registram histórico e não são requisitos normativos.
- Uma decisão pendente não pode ser tratada pela IA como decisão aceita.

## Identidade do projeto

- Nome do produto: **W_Flyer**.
- Slug técnico: `wflyer`.
- Nome de serviços e pacotes: minúsculo, sem caracteres especiais.
- Nomes históricos do projeto podem aparecer em logs antigos, mas não devem ser propagados em novos contratos.
