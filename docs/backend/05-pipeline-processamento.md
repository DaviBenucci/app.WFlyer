# Pipeline assíncrono de processamento

## Princípio

O processamento musical não deve acontecer dentro da requisição HTTP principal.

## Fluxo esperado

```text
1. Usuário envia arquivo.
2. API valida tipo e tamanho.
3. API salva referência interna do arquivo.
4. API cria registro em uploads.
5. API cria registro em processing_jobs.
6. API coloca job na fila.
7. Worker consome job.
8. Worker extrai representação musical.
9. Worker aplica transposição.
10. Worker renderiza o arquivo final quando aplicável.
11. Worker registra artefato gerado.
12. Worker atualiza status do job.
13. Frontend consulta status.
14. Usuário baixa o resultado.
```

## Estratégia MusicXML/PDF

```text
Fase 1: MusicXML-first para validar o motor musical.
Fase 2: PDF simples com pipeline de leitura controlado.
Fase 3: PDF real com validação, avisos e revisão assistida.
```

Regras:

- MusicXML é a prioridade inicial para testar regra musical.
- PDF é formato desejado para usuário final, mas possui risco técnico maior.
- PDFs escaneados, manuscritos, tortos ou de baixa qualidade devem gerar erro amigável.
- A aplicação deve informar quando não conseguir ler a partitura com confiança.

## Etapas internas do worker

```text
queued
processing
transposing
rendering
completed
```

Em falha:

```text
failed
```

Em expiração/cancelamento:

```text
expired
cancelled
```

## Regra musical

```text
intervalo_escrito = origem.written_to_concert - destino.written_to_concert
```

A transposição deve alterar:

- notas;
- acordes;
- acidentes;
- armadura de clave;
- tonalidade escrita;
- partes individuais quando houver múltiplos instrumentos;
- metadados musicais relevantes.

## Validação pós-processamento

- Representação musical final existe.
- Arquivo final tem tamanho maior que zero.
- Intervalo aplicado foi registrado.
- Armadura final corresponde à tonalidade transposta.
- Notas e acordes foram alterados quando esperado.
- Artefato foi registrado em `generated_artifacts`.
- Job terminal foi atualizado.

## Erros públicos possíveis

```text
INVALID_FILE_TYPE
FILE_TOO_LARGE
MUSICXML_PARSE_FAILED
PDF_READ_FAILED
LOW_CONFIDENCE_SCORE
TRANSPOSITION_FAILED
RENDER_FAILED
ARTIFACT_STORAGE_FAILED
PROCESSING_TIMEOUT
```

Mensagens públicas devem ser amigáveis e não revelar stacktrace, path físico ou logs do worker.
