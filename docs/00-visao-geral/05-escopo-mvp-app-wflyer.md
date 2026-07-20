# Escopo técnico do MVP W_Flyer

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Entregar uma aplicação web capaz de transpor corretamente uma parte musical estruturada entre instrumentos, sem exigir conta, com processamento assíncrono, acesso privado e resultado revisável.

## MVP Core obrigatório

1. Aceitar MusicXML não comprimido conforme a matriz de suporte.
2. Validar e normalizar o documento sem executar recursos externos.
3. Permitir seleção manual de instrumento de origem e destino.
4. Calcular intervalo diatônico, cromático e de oitava.
5. Transpor alturas, armaduras, acidentes e símbolos harmônicos suportados.
6. Preservar ritmo, vozes, compassos, ties, tuplets e metadados não musicais suportados.
7. Atualizar o metadado MusicXML de instrumento transpositor para o destino.
8. Executar o pipeline em job assíncrono.
9. Exibir status, estágio, avisos e erros seguros.
10. Entregar MusicXML transposto para download.
11. Proteger uploads, jobs e artefatos por sessão anônima.
12. Expirar e purgar arquivos após 15 dias, com exclusão antecipada pelo usuário.
13. Manter testes semânticos e de segurança como gates de release.

## Perfil musical do Core

- uma parte;
- uma pauta;
- instrumento afinado;
- sistema temperado de 12 semitons;
- armaduras convencionais;
- notas, pausas, acordes notados, vozes, ties e tuplets;
- mudanças de clave, compasso e tonalidade dentro da parte;
- cifras MusicXML simples, quando presentes e suportadas pelo parser.

## Fora do Core

- PDF de entrada antes do gate OMR;
- `.mxl` antes do gate de arquivos compactados;
- imagens JPG/PNG;
- scores multiparte;
- partes com duas ou mais pautas;
- percussão não afinada;
- tablatura;
- microtons;
- armaduras não convencionais;
- mudança de instrumento dentro da mesma parte;
- manuscritos;
- reconstrução visual idêntica ao original;
- editor de partitura completo;
- login, cobrança, biblioteca, compartilhamento e Spotify.

## PDF de entrada

PDF é uma capacidade adicional, não uma simples extensão de upload. Ele depende de rasterização, OMR, normalização e avaliação de qualidade. Enquanto `pdf_omr` estiver desabilitado, o backend deve rejeitar PDF com `FORMAT_NOT_ENABLED`.

## Saídas

Obrigatória no Core:

```text
transposed_musicxml
```

Condicional:

```text
rendered_pdf, somente quando o adapter de renderização estiver aprovado
```

## Garantia do produto

O W_Flyer garante correção dentro da matriz suportada e dos testes aprovados. Para entradas OMR, o produto deve comunicar incerteza e recomendar revisão. Não deve prometer leitura perfeita de todo PDF.

## Fluxo principal

```text
upload validado
-> seleção origem/destino
-> criação idempotente do job
-> normalização
-> transposição
-> validação semântica
-> renderização opcional
-> resultado e avisos
-> download
```

## Critério de não ambiguidade

Quando uma entrada não estiver na matriz suportada, o sistema deve rejeitá-la de modo explícito. Processamento parcial silencioso não é aceitável.
