# Integridade, proveniência e segurança da marca d'água

> Status: canônico. Revisão: 2026-07-20.

## Ameaças

- remoção/crop da marca visual;
- falsificação de token do W_Flyer;
- reutilização do token em outro arquivo;
- edição musical após geração;
- remoção de metadados;
- vazamento de identidade pelo token;
- comprometimento da chave de assinatura;
- watermark que encobre informação musical;
- ataque ao renderer por conteúdo hostil.

## Controles

- token aleatório/pseudônimo, não derivado de PII;
- vínculo server-side entre token, hash e manifesto;
- assinatura com chave em KMS/HSM e rotação;
- verificação por hash do arquivo apresentado;
- watermark distribuído e incorporado ao content stream;
- safe zones calculadas por geometria musical;
- sandbox do renderer/watermarker;
- logs sem partitura, token completo ou PII;
- revogação de chave/manifesto e trilha de auditoria;
- capability desabilitada se assinatura ou watermark falhar.

## Proibições

- alterar pitch, duração, espaçamento crítico ou símbolo para esconder watermark;
- codificar identidade em notas/acidentes/ritmos;
- usar e-mail/nome no PDF sem escolha explícita;
- afirmar que o arquivo não pode ser copiado ou editado;
- considerar metadata isolada como proteção;
- substituir ou ocultar créditos e avisos de copyright da fonte;
- apresentar a marca como prova de que o W_Flyer é titular da obra;
- manter chave privada em variável acessível ao frontend ou ao worker geral.

## Verificação

O endpoint de verificação não deve revelar sessão, nome do arquivo, título da obra ou conteúdo. Rate limit, logs antifraude e resposta neutra para tokens inexistentes são obrigatórios.

## Incidente de chave

Em comprometimento:

1. revogar key id;
2. interromper assinatura de novos artefatos;
3. manter validação histórica com status de comprometimento;
4. gerar nova chave e versão de manifesto;
5. notificar conforme política;
6. não reassinar silenciosamente arquivos antigos.
