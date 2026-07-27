# Página — Central de Políticas

> Status: especificação de frontend futuro. Rota proposta: `/politicas`.

## Objetivo

Oferecer um ponto público, legível e pesquisável para todas as políticas do W_Flyer.

## Estrutura

```text
PublicShell
├── título e resumo
├── identificação da empresa
├── grupo Uso da aplicação
├── grupo Dados e segurança
├── grupo Comercial
├── histórico de versões
└── contatos
```

## Rotas relacionadas

```text
/termos
/privacidade
/cookies
/pagamentos-e-creditos
/cancelamento-e-reembolso
/direitos-autorais-e-conteudo
/uso-aceitavel
/retencao-e-exclusao
/suporte-e-disponibilidade
/seguranca
```

## Regras de UX

- disponível sem login;
- footer do site e da aplicação apontam para `/politicas`;
- busca por título e tema;
- versão e vigência visíveis;
- link permanente para cada documento;
- impressão e leitura mobile;
- nenhum modal obrigatório para ler;
- preferência de cookies não bloqueia políticas;
- documentos históricos claramente identificados;
- rascunhos internos nunca aparecem em produção.

## Estados

- política vigente;
- nova versão com vigência futura;
- versão histórica;
- documento temporariamente indisponível;
- empresa não formalizada: rota não publicada externamente.

## Aceite

A página informa quais políticas foram aceitas pela conta, mas o aceite ocorre no contexto correto: cadastro, upload ou checkout.
