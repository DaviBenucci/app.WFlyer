# Pacote de referências visuais internas

> Status: canônico para execução do frontend. Revisão: 2026-07-20.

## Objetivo

Reduzir interpretação livre da IA e evitar que o W_Flyer seja implementado como um template SaaS genérico. As referências vinculantes vivem em `../design-reference/` e usam composição própria, sem copiar identidade visual, código ou assets de terceiros.

## Princípio

Produtos externos servem apenas para estudo de padrões específicos. A implementação deve seguir primeiro exemplos internos aprovados.

```text
contrato de domínio/acessibilidade
> exemplo interno executável
> story aprovada
> especificação de página/componente
> screenshot golden produzido internamente
> inspiração externa
```

Em caso de conflito, segurança, acessibilidade, contrato de API e regra musical prevalecem sobre qualquer imagem.

## Conteúdo do pacote

```text
design-reference/
├── reference-manifest.yaml
├── schemas/
├── foundations/
├── golden-pages/
├── golden-components/
├── motion/
├── fixtures/
├── do-dont/
├── external-studies/
├── templates/
└── prototypes/
```

O pacote entregue nesta documentação já contém:

- manifesto com precedência e referências;
- schemas para validação das especificações;
- tokens de exemplo;
- especificações de Home, Transpor, Revisão de Melodia, Resultado/Diff, Laboratório de Harmonização e Modo de Ensaio;
- especificações de componentes de domínio;
- fixtures de estados extremos;
- protótipos HTML/CSS próprios e sem dependências externas.

## Níveis de obrigatoriedade

| Nível | Significado |
|---|---|
| `binding` | estrutura, hierarquia, estados e comportamento são obrigatórios |
| `binding-composition` | composição e relações espaciais são obrigatórias; pixels podem evoluir |
| `reference` | padrão recomendado, sujeito a justificativa |
| `illustrative` | exemplo didático, não normativo |

## Golden pages mínimas

1. Home desktop e mobile;
2. Estúdio vazio;
3. arquivo validado e configuração pronta;
4. falha de upload/estrutura;
5. processamento e cancelamento;
6. revisão de melodia ambígua;
7. comparação original versus resultado;
8. relatório de tocabilidade;
9. laboratório de harmonização;
10. comparação de variantes;
11. modo de ensaio;
12. pacote de score/partes;
13. estado expirado/session lost;
14. reduced motion e forced colors.

## Estudos externos

O diretório `external-studies/` não deve conter cópia indiscriminada de screenshots ou código. Cada estudo registra:

```text
produto e URL de origem
padrão observado
problema que o padrão resolve
adaptação própria para W_Flyer
o que é proibido copiar
licença/proveniência do material armazenado
```

Sem direito de uso, manter apenas análise textual e wireframe próprio.

## Workflow

1. escolher a referência pelo `reference-manifest.yaml`;
2. abrir protótipo e specification correspondente;
3. implementar story com as fixtures oficiais;
4. gerar screenshots em ambiente determinístico;
5. revisar visualmente e por acessibilidade;
6. registrar divergências intencionais;
7. aprovar baseline;
8. somente então usar o screenshot como golden.

## Regra contra pixel worship

Visual diff detecta regressão, mas não decide sozinho qualidade. Antialiasing, fonte, sistema operacional e navegador podem variar. A aprovação considera:

- hierarquia;
- densidade;
- alinhamento;
- conteúdo real;
- estados;
- comportamento responsivo;
- foco e contraste;
- coerência musical.

## Critérios de aceite

- toda página implementada possui referência interna ou decisão registrada;
- não existe componente de produto criado apenas por conveniência da biblioteca;
- os protótipos não são copiados como código de produção sem refatoração e testes;
- nenhuma referência externa prevalece sobre identidade própria;
- baseline visual não é atualizado automaticamente para “fazer CI passar”.
