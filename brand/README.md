# Identidade visual do W_Flyer

> Status: estrutura preparada; identidade oficial ainda não aprovada.

Este diretório organiza os arquivos da futura identidade visual usados pela aplicação. A logo antiga foi rejeitada e removida. Nenhum arquivo anterior deve ser recuperado, reutilizado ou tratado como referência oficial.

## Estrutura

```text
brand/
├── README.md
├── brand-manifest.yaml
├── brand-manifest.schema.json
├── source/                 # arquivos-mestre vetoriais aprovados
├── variants/               # versões horizontal, vertical, clara e escura
├── favicons/               # exportações para navegador e instalação
└── guidelines/
    └── brand-guidelines.md # regras de uso da marca
```

As pastas vazias possuem `.gitkeep` apenas para preservar a estrutura. Elas não representam ativos aprovados.

## Regra temporária

Enquanto `brand-manifest.yaml` estiver com `status: pending`:

- usar somente o nome textual `W_Flyer`;
- não inventar símbolo, wordmark, favicon ou assinatura visual;
- não usar a clave, nota musical ou qualquer imagem antiga como logo provisória;
- não considerar a paleta do protótipo como paleta institucional definitiva;
- não distribuir arquivos para `apps/web/public/brand/`;
- não publicar ativos no site institucional.

## Fonte de verdade

O manifesto desta pasta informa o estado da identidade. Depois da aprovação humana, os arquivos vetoriais aprovados entram em `source/`, suas variações em `variants/` e as exportações técnicas em `favicons/`.

A marca será compartilhada futuramente com o repositório do site institucional. Até ser decidido se haverá um repositório de marca separado, esta pasta funciona como área de governança e preparação da aplicação.

## Aprovação

Um ativo só se torna oficial depois de:

1. aprovação explícita do responsável pelo produto;
2. conferência de legibilidade em tamanhos pequenos;
3. teste em fundos claros e escuros;
4. verificação de contraste e acessibilidade;
5. validação de originalidade e licença;
6. atualização do manifesto;
7. registro da decisão e dos arquivos exportados.
