# Testes do backend

> Status: canônico por referência. Revisão: 2026-07-20.

A matriz executável está em:

- `../qa/03-testes-backend.md` — API, persistência, fila e ciclo de vida;
- `../qa/05-testes-musicais.md` — invariantes do motor;
- `../qa/08-testes-seguranca-arquivos.md` — corpus hostil e autorização.

## Gate mínimo do backend Core

- migrations aplicam e revertem em ambiente de teste;
- OpenAPI e cliente gerado não divergem;
- sessão/CSRF/propriedade são testados em toda rota de objeto;
- upload MusicXML passa por parsing seguro;
- criação de job é idempotente;
- outbox, reentrega e retry não duplicam resultado;
- máquinas de estado rejeitam transições inválidas;
- invariantes musicais aprovam o corpus Core;
- download e purge respeitam retenção;
- respostas/logs não vazam dados internos;
- falhas são categorizadas e observáveis.

Nenhum teste de aplicação é considerado executado apenas porque a documentação existe.
