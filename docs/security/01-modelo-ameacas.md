# Modelo de ameaças

## Ativos protegidos

- Arquivos originais enviados pelos usuários.
- MusicXML e PDFs finais.
- Metadados de jobs.
- Artefatos gerados.
- Métricas internas de processamento.
- Fila e worker.

## Upload malicioso

Risco: arquivo explorando ferramenta de parsing, OMR ou renderização.

Mitigações:

- validação real de MIME;
- validação de extensão;
- limite de tamanho;
- renomeação interna;
- worker com timeout;
- isolamento por job quando houver arquivo temporário.

## Path traversal

Risco: filename com `../` gravando fora do local esperado.

Mitigações:

- nunca usar filename original como path;
- usar identificador interno;
- `storage_key` gerada pela aplicação.

## Vazamento de artefato

Risco: artefato acessível sem validação.

Mitigações:

- download controlado;
- expiração;
- validação do artefato;
- bloqueio de expirado.

## Exposição de detalhes internos

Risco: usuário ver métricas internas, stacktrace, path físico ou logs.

Mitigações:

- DTO público separado;
- envelope de erro seguro;
- testes de contrato;
- logs com `correlation_id`.

## Abuso de processamento

Risco: muitos jobs consumindo recursos.

Mitigações:

- rate limiting;
- limite de tamanho;
- timeout;
- retentativas limitadas;
- erro público seguro.

## Logs sensíveis

Risco: nomes de arquivos sensíveis, tokens, paths ou exceções brutas em logs.

Mitigações:

- mascaramento;
- não logar payload completo;
- registrar `correlation_id`;
- manter logs internos fora dos DTOs públicos.
