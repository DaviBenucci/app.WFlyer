# Escopo técnico do MVP app.WFlyer

## Objetivo

Definir, sem ambiguidade, o que a aplicação `app.WFlyer` deve fazer no primeiro ciclo de desenvolvimento.

O MVP é uma aplicação web de transposição musical. Ele deve receber uma partitura, permitir seleção manual de instrumento de origem e destino, calcular a transposição correta, processar o arquivo em job assíncrono e entregar um arquivo final baixável.

## Função principal

1. Receber arquivos de partitura.
2. Permitir seleção manual do instrumento de origem.
3. Permitir seleção manual do instrumento de destino.
4. Calcular a transposição musical correta.
5. Alterar notas, acordes, acidentes, armadura de clave e tonalidade escrita.
6. Processar a transposição de forma assíncrona.
7. Gerar arquivo final baixável.
8. Exibir status de processamento ao usuário.
9. Tratar erros de leitura, validação e processamento.
10. Permitir evolução futura para login, histórico em nuvem, biblioteca e planos, sem tornar isso obrigação do MVP.

## MVP obrigatório

- Aplicação sem login obrigatório.
- Upload de arquivo.
- Seleção manual do instrumento de origem.
- Seleção manual do instrumento de destino.
- Criação de job de processamento.
- Acompanhamento de status.
- Motor de transposição musical.
- Resultado final baixável.
- Mensagens claras de erro.
- Validação de arquivo.
- Testes musicais automatizados.
- Testes básicos de backend.
- Testes básicos de frontend.

## Fora do MVP inicial

- Login.
- Biblioteca em nuvem.
- Planos pagos.
- Assinatura.
- Dashboard administrativo.
- Colaboração entre usuários.
- Editor visual completo de partitura.
- Detecção automática perfeita de instrumento.
- Detecção automática perfeita de tonalidade.
- OMR perfeito para qualquer PDF.
- Aplicativo mobile nativo.
- Integração Spotify.
- Site institucional ou landing page.

## Estratégia MusicXML/PDF

O início do código deve priorizar MusicXML para reduzir risco técnico e validar a regra musical antes de lidar com leitura difícil de PDF.

```text
Fase 1: MusicXML-first para validar o motor musical.
Fase 2: PDF simples com pipeline de leitura controlado.
Fase 3: PDF real com validação, avisos e revisão assistida.
```

Motivos:

- MusicXML é estruturado e mais seguro para testar regra musical.
- PDF é melhor para o usuário final, mas tem risco técnico maior.
- O MVP não deve prometer leitura perfeita de qualquer PDF.
- PDFs escaneados, manuscritos, tortos ou com baixa qualidade devem gerar erro amigável.
- A aplicação deve informar quando não conseguir ler a partitura com confiança.

## Fluxo do usuário

```text
1. Tela inicial da aplicação.
2. Upload da partitura.
3. Seleção do instrumento de origem.
4. Seleção do instrumento de destino.
5. Confirmação da transposição.
6. Tela de processamento.
7. Tela de resultado.
8. Download.
9. Transpor outra partitura.
```

## Estados da aplicação

```text
idle
uploading
uploaded
configuring
queued
processing
completed
failed
expired
```

## Regra musical obrigatória

```text
intervalo_escrito = origem.written_to_concert - destino.written_to_concert
```

Exemplos obrigatórios:

```text
Piano C -> Trompete Bb
origem.written_to_concert = 0
destino.written_to_concert = -2
intervalo = 0 - (-2) = +2 semitons
```

```text
Trompete Bb -> Piano C
origem.written_to_concert = -2
destino.written_to_concert = 0
intervalo = -2 - 0 = -2 semitons
```

## Partes que devem ser alteradas

- Notas.
- Acordes.
- Acidentes.
- Armadura de clave.
- Tonalidade escrita.
- Partes individuais quando houver múltiplos instrumentos.
- Metadados musicais relevantes.

## Escopo técnico coberto

- Arquitetura interna.
- Organização do código.
- Frontend.
- Backend.
- Banco de dados.
- APIs.
- Processamento assíncrono.
- Regra musical.
- Upload de arquivos.
- Segurança.
- Testes.
- UX da ferramenta.
- Acessibilidade.
- Critérios de aceite.
- Guia de implementação para o Codex.

## Escopo técnico não coberto

Esta etapa não documenta publicação online, domínio, DNS, hospedagem, servidor de produção ou integração Spotify.
