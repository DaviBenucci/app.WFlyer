# Acessibilidade

## Objetivo

Garantir que o WFlyer possa ser usado por teclado, leitores de tela, dispositivos móveis e usuários com sensibilidade a movimento.

## Requisitos obrigatórios

- H1 único por página.
- Navegação por teclado.
- Ordem lógica de foco.
- Labels em campos.
- Mensagens de erro textuais.
- Contraste adequado.
- `aria-live` para status de processamento.
- Área mínima de toque em mobile.
- Suporte a `prefers-reduced-motion`.
- Não depender apenas de cor para comunicar status.
- Loading acessível.
- Estados vazios e estados de erro compreensíveis.

## Upload

- Dropzone deve aceitar Enter/Espaço.
- Deve existir botão alternativo para selecionar arquivo.
- Erro de arquivo deve ser anunciado em texto.
- Formato e limite devem estar claros.

## Seleção de instrumentos

- Campo pesquisável deve ter label.
- Opções devem ser navegáveis por teclado.
- Estado selecionado não deve depender só de cor.
- Instrumento inválido deve gerar mensagem textual.

## Processamento

- Status deve usar `aria-live`.
- Progresso deve ter texto além de barra visual.
- Erro do job deve ser anunciado.
- Loading deve ter nome acessível.

## Mobile

- Botões grandes.
- Área de toque mínima de 44x44px.
- Conteúdo não deve ficar oculto por navegação fixa.
- Textos devem caber sem sobreposição.

## Movimento

Quando `prefers-reduced-motion` estiver ativo:

- reduzir animações;
- remover efeitos decorativos;
- manter feedback visual simples;
- nunca esconder o status textual.

## Testes

- Fluxo completo só com teclado.
- Auditoria com ferramenta de acessibilidade quando disponível.
- Simulação de mobile.
- Simulação de `prefers-reduced-motion`.
