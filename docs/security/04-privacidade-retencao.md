# Privacidade e retenção

## Minimização

Coletar somente o necessário para processar e operar:

```text
sessão anônima em hash
filename sanitizado quando necessário
formatos/tamanho/hash
instrumentos e job
artefatos e eventos categóricos
telemetria técnica minimizada
```

Não usar partituras para treinamento, benchmark externo ou compartilhamento com terceiros sem base, transparência e consentimento/contrato apropriado.

## Janela padrão

- original validado: 15 dias;
- resultado: 15 dias após conclusão;
- `expires_at` é exibido ao usuário;
- sessão deve permitir a janela anunciada enquanto não for apagada/revogada.

## Direitos e ações

- baixar resultado;
- apagar recurso do servidor antes da expiração;
- limpar preferências/histórico local separadamente;
- receber explicação de indisponibilidade após expiração/purge.

## Após expiração

- bloquear acesso imediatamente;
- purgar bytes de forma idempotente;
- reduzir metadados ao mínimo operacional/legal;
- não manter cópia em cache/log/observabilidade;
- reconciliar storage e banco.

## Logs e terceiros

- conteúdo de arquivo não entra em log/APM;
- nomes/tokens/URLs são omitidos ou mascarados;
- processadores externos de SaaS não podem receber documento sem decisão específica;
- retenções de backup precisam ser documentadas antes de produção.

## Texto ao usuário

```text
Seus arquivos ficam disponíveis por até 15 dias após o processamento. Você pode apagá-los antes desse prazo. Limpar o histórico deste navegador não apaga automaticamente os arquivos do servidor.
```

## Dados de revisão, modelo e verificação

Seleções de melodia e variantes podem revelar conteúdo musical derivado e seguem a mesma retenção do job. Dados não podem ser reaproveitados para treino sem consentimento/base explícita. Após purge, o registro de verificação deve conter apenas hash/token/versões/status mínimos; não manter eventos, títulos ou PII por conveniência.

## Política pública relacionada

A redação pública planejada está em `../policies/02-politica-privacidade.md` e `../policies/08-politica-retencao-exclusao.md`. Os controles técnicos deste documento prevalecem sobre textos resumidos de interface.
