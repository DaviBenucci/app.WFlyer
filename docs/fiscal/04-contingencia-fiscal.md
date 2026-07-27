# Contingência fiscal

> Status: proposta pré-CNPJ; integração fiscal permanece desabilitada. Revisão: 2026-07-27.

## Falhas previstas

- API indisponível;
- certificado expirado;
- rejeição de layout;
- dado do tomador inválido;
- código de serviço incorreto;
- duplicidade;
- nota autorizada sem resposta local;
- cancelamento fora do prazo;
- mudança de versão/XSD.

## Comportamento

```text
pagamento confirmado
→ serviço continua válido
→ obrigação fiscal permanece pendente
→ retry apenas para falha transitória
→ erro determinístico vai para revisão
```

## Reconciliação

- consultar notas submetidas sem resposta;
- comparar provedor/emissor com banco;
- impedir emissão duplicada por chave de negócio;
- armazenar protocolo;
- registrar operação manual;
- alertar antes de prazos fiscais.

## Modo manual

Durante implantação inicial, pode existir fila manual controlada. Ela deve registrar:

- quem emitiu;
- quando;
- número/protocolo;
- arquivos;
- vínculo com pagamento;
- erro e correção.

Nunca marcar como emitida apenas porque a tarefa foi criada.
