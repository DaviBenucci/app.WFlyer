# Visão crítica musical e diferenciação do W_Flyer

> Status: canônico para evolução do produto. Revisão: 2026-07-20.

## Tese do produto

O diferencial defensável do W_Flyer não é apenas “transpor partituras com IA”. Editores de notação já executam transposição quando recebem dados estruturados corretos. O W_Flyer deve combinar cinco capacidades:

```text
transformar
+ explicar
+ verificar
+ adaptar ao instrumento
+ devolver controle ao músico
```

A aplicação deve se comportar como um assistente de preparação musical, não como um gerador opaco de arquivos.

## Pilares

### 1. Exatidão comprovável

Transformações determinísticas devem preservar invariantes mensuráveis e produzir um `Musical Diff` com proveniência por evento. “Concluído” não significa “correto”; somente um resultado aprovado por todos os gates aplicáveis pode receber nível de garantia correspondente.

### 2. Inferência revisável

Extração de melodia, análise formal e reconhecimento de harmonia são inferenciais. A aplicação deve apresentar alternativas por região, explicar evidências e solicitar confirmação quando a ambiguidade for material.

### 3. Criatividade condicionada

Harmonização, revoicing e arranjo criam material novo. O sistema entrega variantes, declara o orçamento de alteração, mantém a melodia bloqueada quando solicitado e nunca apresenta uma proposta estética como verdade única.

### 4. Escrita idiomática

Uma nota pode estar dentro da extensão absoluta e ainda ser inadequada ao instrumento, ao andamento ou ao nível do intérprete. O W_Flyer deve distinguir:

```text
impossível
tecnicamente possível
difícil
idiomático
confortável
```

### 5. Continuidade entre partitura e performance

Comparação A/B, mapa de reprodução, modo de ensaio, loops e score following devem usar o mesmo grafo de eventos que originou a partitura. Áudio é uma representação derivada; não substitui a validação semântica da notação.

## Correções conceituais obrigatórias

### Instrumento melódico versus harmônico

Essa classificação isolada é insuficiente. O produto deve modelar polifonia prática, extensão, registro, sustain, respiração, span, acordes executáveis, técnicas especiais, dificuldade e convenções de notação.

### Clave de Sol versus melodia

A melodia não está necessariamente na pauta superior nem na nota mais aguda. Ela pode migrar entre vozes e pautas, ser dobrada, aparecer em voz interna ou alternar com contracantos. O sistema analisa o documento inteiro dentro do perfil habilitado.

### Transposição versus transcrição

- **Transposição:** muda a escrita para preservar o som de concerto.
- **Extração/redução:** escolhe material existente e reduz textura.
- **Adaptação instrumental:** altera oitavas, voicings, articulação ou distribuição para tornar a escrita executável.
- **Arranjo/orquestração:** redistribui e pode criar material entre partes.
- **Harmonização:** cria suporte harmônico novo.

Nenhuma dessas operações pode ser escondida dentro de outra.

## Diferenciais prioritários

1. `Musical Diff` navegável entre origem e resultado.
2. revisão assistida de melodia por frase e não apenas por voz global;
3. verificador de tocabilidade sensível a andamento e nível;
4. adaptação idiomática com alternativas e preview;
5. análise de forma, fraseado, cadências e centros tonais/modais;
6. harmonização por variantes explicáveis e comparáveis;
7. audição A/B sincronizada com a partitura;
8. pacote de score e partes para conjuntos;
9. modo de ensaio com loop, contagem e anotações;
10. revisão colaborativa por compasso e aprovação musical.

## Limites de honestidade

O W_Flyer não deve afirmar que:

- conhece a intenção emocional do compositor apenas por andamento, modo ou tonalidade;
- identifica automaticamente a melodia de toda partitura complexa sem possibilidade de erro;
- transforma qualquer peça em escrita idiomática sem revisão humana;
- uma harmonização gerada é “a correta”;
- a reprodução sonora prova que a notação está correta;
- uma marca d'água visual é impossível de remover.

## Critério de produto

Cada nova capacidade deve responder a estas perguntas:

1. Qual decisão musical está sendo tomada?
2. Ela é determinística, inferencial ou criativa?
3. Quais evidências sustentam a decisão?
4. Quais falhas podem alterar notas, ritmo, função ou tocabilidade?
5. O que bloqueia publicação?
6. Quando o usuário precisa confirmar?
7. Como a alteração aparece no diff e no manifesto?
8. Como o resultado é testado por músicos e por software?

Uma capacidade sem respostas documentadas permanece desabilitada.
