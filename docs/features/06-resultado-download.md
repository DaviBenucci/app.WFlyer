# Resultado e download

## Objetivo

Apresentar o resultado validado, os avisos e os artefatos públicos do job pertencente à sessão.

## Condições

Artefatos só são listados quando:

```text
status = completed | completed_with_warnings
retention_status = active
visibility = public
```

Resultado obrigatório do Core:

```text
transposed_musicxml
```

`rendered_pdf` só aparece quando solicitado, habilitado e gerado com sucesso conforme política do produto.

## Tela

Mostrar:

- origem, destino e intervalo vetorial em linguagem musical;
- status/expiração;
- warnings categóricos;
- botão por formato disponível;
- recomendação de revisão antes de ensaio/apresentação;
- ações “transpor outra” e “apagar do servidor”.

Não mostrar métricas brutas, hashes internos, paths, engine stderr ou artefatos internos.

## Download

- endpoint autoriza sessão/propriedade novamente;
- resposta usa attachment e headers de segurança;
- item expirado retorna `410`;
- falha de rede não remove o histórico;
- filename é sanitizado pelo servidor.

## Deleção

“Remover do histórico” apaga somente metadados locais. “Apagar arquivos do servidor” chama a API e antecipa purge. A UI deve diferenciar as ações.

## Critérios de aceite

- job em andamento não oferece artefato final;
- warning não é escondido;
- expirado/purged não baixa;
- sessão B não baixa artefato de A;
- MusicXML baixado corresponde ao hash/metadado do job;
- nenhum caminho interno aparece na resposta ou UI.

## Garantia e conteúdo derivado

A tela de resultado deve apresentar:

- operação executada;
- nível de garantia;
- se a fonte foi confirmada pelo usuário;
- se existem notas geradas;
- link para relatório de garantia;
- token de verificação quando PDF assinado estiver ativo.

Harmonização deve exibir “proposta escolhida” e permitir baixar também a melodia original/confirmada. Não usar selo “100% correto”.
