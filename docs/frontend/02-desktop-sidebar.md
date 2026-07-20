# Navegação desktop e workspace

> Revisão: 2026-07-20.

## Decisão

O W_Flyer não deve usar uma sidebar larga de dashboard em todas as páginas. A navegação varia conforme o shell:

```text
páginas públicas -> header horizontal
workspace/utilidades -> navigation rail compacta
```

## Destinos estáveis do Core

```text
Início          /
Transpor        /transpor
Histórico       /historico
Instrumentos    /instrumentos
Configurações   /configuracoes
```

“Como funciona” fica no header público, menu secundário, ajuda contextual e rodapé. `/resultado/{job_id}` é rota contextual e não item fixo.

## PublicHeader

- wordmark W_Flyer;
- links essenciais;
- CTA “Transpor”;
- altura compacta;
- fundo sólido ou translúcido somente se o contraste permanecer estável;
- não se transformar em mega menu.

## DesktopNavigationRail

Largura orientativa: 68px.

- marca reduzida no topo;
- ícones consistentes;
- labels via tooltip acessível e estado expandido opcional;
- item ativo com indicador geométrico próprio, texto e `aria-current` quando expandido;
- Configurações e ajuda na área inferior;
- nenhum item crítico depende de hover.

## StudioHeader

Exibe somente contexto útil:

- nome sanitizado do arquivo ou “Nova transposição”;
- estado do job;
- expiração quando aplicável;
- ação de fechar/voltar sem perder contexto inadvertidamente.

Não repetir toda a navegação no topo.

## Command menu

Pode ser adicionado como melhoria não bloqueante:

```text
Ctrl/Cmd + K
```

O menu oferece navegação e ações seguras, mas não substitui os controles visíveis nem executa deleção sem confirmação.

## Fora do Core

Não exibir conta, plano, cobrança, compartilhamento, dashboard, administração ou push.

## Critérios

- header público e rail não competem entre si;
- navegação continua compreensível sem tooltip;
- foco visível não é encoberto pelo header;
- rota de resultado não vira destino global;
- o workspace mantém área horizontal prioritária para o conteúdo musical;
- a navegação não se parece com painel administrativo genérico.
