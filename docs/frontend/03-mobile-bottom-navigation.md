# Navegação mobile

> Revisão: 2026-07-20.

## Estrutura

Manter cinco destinos estáveis:

```text
Início
Histórico
Transpor
Instrumentos
Ajustes
```

“Transpor” ocupa a posição central e recebe ênfase moderada. Não usar botão flutuante desconectado da barra nem formato exagerado que esconda conteúdo.

## Comportamento

- a barra respeita `env(safe-area-inset-bottom)`;
- conteúdo reserva espaço inferior real;
- label permanece visível;
- estado ativo usa forma, peso e texto, não apenas cor;
- em rotas contextuais de processamento/resultado, “Transpor” continua ativo sem criar uma aba “Resultado”;
- com teclado aberto, a barra pode recolher quando necessário para não competir com campos e sheets;
- dentro de dialog/sheet, o foco permanece no overlay e a bottom nav não recebe interação.

## Sticky action bar

A ação do fluxo fica em barra separada acima da bottom nav:

```text
Voltar | Continuar
Cancelar | Acompanhar processamento
Baixar resultado | Transpor outra
```

Não colocar ações de formulário dentro da navegação global.

## Gestos

- nenhum gesto é obrigatório;
- swipe pode ser melhoria, nunca única forma de navegar;
- drag-and-drop possui seleção de arquivo alternativa;
- zoom/preview possui controles visíveis.

## Critérios

- área de toque mínima de 44 x 44 CSS px;
- labels não truncam silenciosamente em 320px;
- safe area e teclado foram testados;
- bottom nav e action bar não se sobrepõem;
- leitor de tela identifica destino e estado atual;
- recursos futuros não aparecem desabilitados como parte do produto.
