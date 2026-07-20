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

O W_Flyer pode declarar uma **transformação verificada dentro da matriz suportada** quando a fonte simbólica foi validada e todos os invariantes independentes passaram. Para entradas OMR, extração de melodia ou harmonização, o produto deve expor o nível de garantia e exigir revisão quando houver ambiguidade. Não deve prometer leitura perfeita de todo PDF, melodia infalível em toda polifonia ou uma harmonização universalmente correta.

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

## Trilhas avançadas preservadas para evolução

Não fazem parte do aceite do MVP Core, mas possuem arquitetura própria:

- multipauta/multiparte;
- extração de melodia e redução monofônica;
- harmonização e arranjo;
- perfis instrumentais de tocabilidade;
- watermark, manifesto e verificação de PDF.

Essas capacidades não devem ser implementadas como exceções dentro do motor Core. Seguem `../music/06-taxonomia-transformacoes-musicais.md` e `02-roadmap-fases.md`.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Fundação obrigatória para não bloquear a evolução

Mesmo sem expor recursos avançados, o Core deve nascer com:

- IDs internos estáveis para eventos suportados;
- manifesto de processamento e hashes de artefatos;
- mapeamento de origem e saída suficiente para auditoria;
- `operation` explícita no job;
- capabilities vindas do backend;
- revisão visual baseada no pacote `../design-reference/`;
- catálogo de riscos e códigos de erro extensível;
- versões de parser, catálogo, política e motor registradas.

Esses itens não significam que extração, harmonização, áudio ou ensemble estejam habilitados.

## Limites da promessa

O Core pode provar uma transposição dentro do perfil suportado. Ele não pode prometer:

- reconhecer toda partitura de imagem/PDF;
- localizar melodia em qualquer textura;
- adaptar automaticamente qualquer obra a qualquer instrumento;
- produzir harmonia que represente a intenção subjetiva do autor;
- gerar engraving profissional sem gate do renderer;
- detectar todos os defeitos possíveis.

Quando uma capability futura for ativada, a promessa pública deve nomear matriz, nível de garantia e necessidade de revisão.

## Proteção contra expansão por documentação futura

A expansão crítica descreve a arquitetura futura para evitar decisões irreversíveis, mas não altera o MVP Core. Permanecem fora do Core até gates próprios:

- extração automática de melodia polifônica;
- harmonização e arranjo;
- adaptação idiomática automática;
- análise de forma/cadência/tensão;
- áudio sincronizado e score following;
- modo de ensaio completo;
- score multiparte e geração de partes;
- colaboração e aprovação multiusuário;
- OMR/PDF público.

Protótipos visuais dessas capacidades são referências de arquitetura e UX, não evidência de que o backend esteja pronto.
