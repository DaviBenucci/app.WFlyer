# Decisões pendentes

> Status: canônico. Revisão: 2026-07-20.

A IA não pode decidir os itens abaixo sem aprovação explícita.

## PEND-001 — Engine OMR de produção

Avaliar pelo menos:

- qualidade no corpus do W_Flyer;
- execução automatizável;
- isolamento;
- manutenção;
- licença e obrigações de distribuição;
- custo operacional;
- formato e qualidade do MusicXML exportado.

Candidato de spike: Audiveris. Não é decisão de produção.

## PEND-002 — Engine de renderização

Avaliar CLI/API, determinismo, fontes, licença, consumo de recursos e fidelidade. MuseScore Studio pode ser usado no spike, mas não deve ser acoplado diretamente ao domínio.

## PEND-003 — Limites operacionais

Definir após benchmark:

- tamanho máximo por formato;
- páginas por PDF;
- medidas/notas por MusicXML;
- profundidade/nós XML;
- tempo por etapa;
- memória e CPU por worker;
- jobs simultâneos por sessão/IP.

Antes da decisão, usar limites conservadores em configuração e manter PDF desabilitado.

## PEND-004 — Gate quantitativo de PDF

Definir métricas e limiares mínimos do corpus antes de ativar `pdf_omr`. O gate deve medir estrutura, alturas, ritmos, armaduras, estabilidade e taxa de revisão necessária.

## PEND-005 — Suporte a `.mxl`

Só habilitar após validação de container, prevenção de zip slip/zip bomb, limite de entries, tamanho descompactado e recursos referenciados.

## PEND-006 — Expansão para multiparte/multipauta

Exige UX de seleção de parte, instrumentos por parte, política de pauta/clave e novos testes. Não deve ser implementada como “loop sobre parts”.
