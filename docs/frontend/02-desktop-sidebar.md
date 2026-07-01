# Navegação desktop

## Objetivo

Definir navegação simples para o MVP, focada na ferramenta de transposição.

## Itens permitidos no MVP

```text
Início -> /
Transpor -> /transpor
Resultado -> /resultado/{job_id}
Instrumentos -> /instrumentos
Histórico local -> /historico
Configurações locais -> /configuracoes
```

## Fora do MVP

Não exibir links para compartilhamento, dashboard autenticado ou painel administrativo.

## Acessibilidade

- Item ativo com `aria-current="page"`.
- Foco visível.
- Navegação por teclado.
- Labels textuais ou `aria-label` em ícones.
