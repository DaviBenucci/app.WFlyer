# Testes de backend

## Sessão e autorização

- criar/renovar/revogar/expirar sessão;
- cookie possui flags esperadas;
- CSRF ausente/inválido bloqueia mutações;
- sessão A não lê/apaga upload, job ou artefato de B;
- IDs inexistentes e de outra sessão produzem resposta indistinguível;
- token/cookie não aparece em logs.

## API e contratos

- `/health` e `/health/ready` têm semânticas distintas;
- capabilities refletem configuração;
- catálogo retorna o schema vetorial;
- erros seguem taxonomia;
- OpenAPI gera cliente sem diff;
- campos internos nunca aparecem.

## Upload

- MusicXML válido aceito;
- XML não MusicXML, vazio, excessivo, assinatura incoerente e hostil rejeitados;
- PDF/MXL desabilitados retornam `FORMAT_NOT_ENABLED`;
- streaming respeita limite e não usa memória ilimitada;
- upload rejeitado não cria job;
- hash/tamanho divergente bloqueiam worker.

## Jobs/fila

- criação exige upload da sessão e `validated`;
- idempotency key igual + payload igual retorna mesmo job;
- chave igual + payload diferente conflita;
- outbox publica após commit;
- reentrega não duplica tentativa/artefato indevidamente;
- retry determinístico não repete;
- retry transitório respeita máximo/backoff;
- crash em cada fronteira é reconciliado;
- heartbeat/lease detecta job preso;
- cancelamento não publica resultado.

## Estados

- todas as transições válidas passam;
- transições inválidas falham/geram conflito;
- stage não é confundido com status;
- retenção evolui independentemente;
- progresso é monotônico e 100 apenas em sucesso.

## Storage/artefatos

- chave não usa filename;
- gravação/publicação atômicas;
- artefato público pertence ao job/tentativa correta;
- download autorizado, headers corretos;
- expiração bloqueia antes do purge;
- purge/reconciliação idempotentes;
- objeto órfão é detectado.

## Motor

Executar a suíte de `05-testes-musicais.md` e falhar o job quando qualquer invariante obrigatório falhar.

## Revisão, garantia e watermark

- review A não acessa job de B;
- revision conflict não sobrescreve;
- job em espera não mantém lease;
- assurance repara arquivos e detecta saída adulterada;
- manifesto/hash/assinatura correspondem ao artefato;
- token inválido não enumera registros;
- falha do watermarker não publica PDF parcial.
