# Tela Transpor

> Revisão: 2026-07-20.

## Rota

```text
/transpor
```

## Objetivo

Conduzir o usuário em um workspace único, recuperável e validado. Evitar um wizard genérico com várias páginas e cards repetidos.

## Shell

`StudioShell`.

## Composição desktop

```text
StudioHeader
WorkspaceCanvas
  ScoreSurface
  FileSummary ou estado de upload
  ProcessingTimeline quando job existir
ContextInspector
  Instrumento de origem
  Instrumento de destino
  Formato de saída
  TranspositionRoute
StickyActionBar
```

## Composição mobile

```text
Header compacto
Upload/arquivo
Origem
Destino
Resumo da transposição
Formato
Ação fixa
Processamento/resultado contextual
```

O seletor de instrumento abre em sheet pesquisável, agrupado por família.

## Entrada e motion do Studio

- o shell não reinicia uma cena cinematográfica a cada navegação;
- ScoreSurface entra por opacity e deslocamento máximo de 8–12 px;
- inspector acompanha com atraso curto, sem slide lateral longo;
- `TranspositionRoute` desenha quando origem/destino se tornam válidos;
- Motion controla presença/layout; GSAP fica restrito ao `ProcessingInkLoop`;
- reduced motion usa troca imediata/crossfade;
- nenhuma ação espera o fim da animação.

## Estados do workspace

```text
initializing
empty
file_selected
uploading
validated
configuration_incomplete
ready_to_submit
creating_job
processing
completed
failed
cancelled
session_lost
```

Esses estados são de view/composição e não substituem enums do backend.

## Upload

- ScoreSurface lembra uma folha/área de partitura, sem textura pesada;
- drag-and-drop + botão;
- formatos e perfil suportado aparecem antes do envio;
- após validação, mostrar nome, tamanho, formato e resumo estrutural disponível;
- voltar/alterar instrumento não repete upload;
- arquivo hostil/fora do perfil gera ação específica.

## Instrumentos

### Origem

Label:

```text
Instrumento da partitura original
```

### Destino

Label:

```text
Instrumento que receberá a nova escrita
```

O picker mostra:

- nome;
- afinação;
- família;
- “C escrito soa ...”;
- aliases;
- indicação de oitava.

## Resumo

`TranspositionRoute` permanece visível depois que origem/destino forem escolhidos:

```text
Piano em C -> Trompete em Bb
Segunda maior acima (+2 semitons)
```

O valor autoritativo após criação vem do backend.

## Processamento

Substituir spinner isolado por `ProcessingTimeline`:

```text
Preparando
Transpondo
Validando
Finalizando
```

Etapas aparecem conforme `stage` real. Mostrar progresso sem inventar avanço. Permitir cancelar quando aplicável.

Uma versão abstrata da tinta pode percorrer a rota enquanto o job está ativo. Ela não representa porcentagem, reinicia apenas quando o stage muda de forma aprovada, pausa em aba oculta e termina imediatamente em estado terminal.

## Recuperação

Após refresh, usar rota/estado e sessão existente. Sem sessão original, mostrar recurso indisponível; não pedir token local.

## Erros

- formato desabilitado;
- arquivo inválido/hostil;
- estrutura fora do perfil;
- origem incompatível;
- rate limit;
- falha/timeout;
- perda de sessão;
- serviço indisponível.

`correlation_id` aparece como referência secundária.

## Critérios de aceite

- não cria job sem upload validado, origem e destino;
- double click não duplica job;
- a tela parece workspace musical, não formulário administrativo;
- origem, destino e intervalo permanecem claros durante o fluxo;
- polling não confunde rede com falha;
- fluxo funciona por teclado, mobile e zoom;
- capabilities governam formatos/outputs;
- loop de processamento não continua após conclusão/erro/cancelamento;
- navegação e refresh não acumulam timelines.

## Escolha do modo musical

Quando capabilities avançadas estiverem ativas, o inspector inclui `OperationModePicker` depois da análise do arquivo:

```text
Transpor todas as notas
Extrair a melodia principal
Harmonizar a melodia
```

Opções incompatíveis permanecem visíveis com motivo. Para origem polifônica e destino monofônico, “Transpor todas” fica bloqueado e a UI recomenda extração; nunca descarta acordes por conveniência.

Harmonização abre parâmetros essenciais e informa que novas notas serão criadas. A criação do job usa o resumo da operação, não apenas origem/destino.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Preflight musical antes do submit

A tela deve mostrar:

- operação exata;
- estrutura detectada e suportada;
- instrumento/revisão de origem;
- instrumento/perfil de destino;
- intervalo ou natureza criativa da operação;
- incompatibilidades e necessidade de revisão;
- outputs solicitados;
- nível de garantia potencial, sem prometer resultado final.

Para textura polifônica e destino monofônico, a UI não pode remover notas silenciosamente. Deve bloquear “transpor todas” e oferecer extração/redução apenas quando a capability estiver habilitada.

## Referência

`reference_id: WF-TRANSPOSE-001`. Divergência de composição precisa ser registrada no PR.
