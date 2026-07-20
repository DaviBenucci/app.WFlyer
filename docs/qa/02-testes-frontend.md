# Testes de frontend

> Revisão: 2026-07-20.

## Unitários/componentes

- `CapabilityGate` mostra apenas formatos ativos;
- `UploadDropzone` anuncia erro e oferece alternativa ao drag;
- `InstrumentPicker` usa catálogo da API e navegação de combobox;
- `TranspositionRoute` representa diatônica/cromática/oitava e possui texto equivalente;
- `ProcessingTimeline` mapeia status/stage sem inventar progresso;
- `WarningPanel` mantém warnings materiais;
- `ArtifactRow` bloqueia download por retenção;
- ações local/servidor são distintas;
- shells e navigation não encobrem foco/conteúdo;
- componentes respondem ao container compacto e amplo;
- Motion respeita estado, presença e reduced motion;
- cena GSAP cria uma timeline, possui cleanup e fallback estático.

## Storybook

- stories para estados definidos em `../frontend/13-storybook-governanca-ui.md`;
- testes de interação com teclado;
- addon de acessibilidade no CI;
- visual regression em viewports definidos;
- conteúdo longo, muitos warnings e erro multilinha;
- reduced motion e tema suportado;
- animações desabilitadas/estabilizadas para snapshots determinísticos;
- intro normal, já vista, interrompida e com falha de chunk.

## Integração com API mockada por contrato

Cobrir:

```text
bootstrap de sessão e CSRF
upload validated
format not enabled
source mismatch
job queued -> running -> completed
completed_with_warnings
failed/cancelled
polling 429/Retry-After
erro de rede temporário
401/404 por perda/troca de sessão
410 por expiração
```

Mocks são gerados/validados contra OpenAPI.

## Acessibilidade

- fluxo completo por teclado;
- foco retorna ao título/erro após mudança relevante;
- dropzone com Enter/Espaço;
- combobox conforme ARIA;
- `aria-live` não anuncia cada polling;
- foco não é encoberto;
- zoom 200%, mobile, forced colors e reduced motion;
- preview possui alternativa textual;
- auditoria automática + revisão manual.

## Qualidade visual

- nenhum componente mantém tema padrão de biblioteca sem adaptação;
- home não usa hero/card layout genérico;
- Transpor usa StudioShell;
- listas não viram card soup;
- ausência de overflow em nomes longos;
- diff visual de token é revisado, não atualizado automaticamente.

## Segurança

- cookie não é acessível no JS;
- CSRF não é persistido/logado;
- mensagens/filename como texto;
- respostas `no-store` não são cacheadas;
- download não aceita URL arbitrária.

## Performance

- rota pública não carrega renderer/preview pesado;
- lazy-loading é verificável;
- nenhuma animação mantém CPU ativa em background;
- GSAP ausente das rotas sem cena;
- Anime.js e React Spring ausentes do Core;
- timelines/listeners não vazam após navegação repetida;
- métricas/bundle comparados ao baseline.

Detalhamento obrigatório: `09-testes-motion-performance.md`.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Cobertura por `reference_id`

CI deve gerar matriz:

```text
reference_id x state x viewport x input_mode x motion_preference
```

Não é necessário testar produto cartesiano completo, mas cada combinação excluída precisa de justificativa de risco.

## Casos críticos adicionais

- warning bloqueante persiste após refresh;
- diff parcial não aparece como completo;
- `UNKNOWN` não usa aparência de sucesso;
- navegação por teclado entre origem/resultado e change list;
- foco permanece visível com sticky bars;
- audio transport não inicia sozinho;
- cursor de playback não captura leitor de tela a cada frame;
- conflito de revisão preserva edição local sem sobrescrever servidor;
- baseline não pode ser atualizado por bot sem aprovação.
