# Marca d'água e proveniência de partituras

> Status: canônico para saída renderizada. Capacidade condicionada ao renderer.

## Objetivos

1. Identificar que o arquivo foi gerado pelo W_Flyer.
2. Desestimular redistribuição não autorizada.
3. Permitir rastrear uma cópia por token pseudônimo.
4. Detectar alteração por assinatura/hash.
5. Não prejudicar leitura, ensaio, impressão ou acessibilidade.

## Limite técnico

Nenhuma marca d'água visual é impossível de remover por alguém com tempo e ferramenta de edição. A estratégia correta combina **dissuasão**, **rastreabilidade** e **detecção de alteração**, sem prometer DRM infalível.

## Camadas

### 1. Marca visível distribuída

- vetor incorporado ao content stream, não annotation opcional;
- repetição moderada entre sistemas, margens e rodapé;
- baixa opacidade e contraste validado em tela/impressão;
- token curto por página;
- nunca cobrir cabeças de nota, acidentes, claves, armaduras, letras ou dinâmica.

### 2. Token forense pseudônimo

```text
WF-7K3D-9Q2M
```

O token referencia um registro de verificação e não contém e-mail, nome ou ID sequencial.

### 3. Metadados e manifesto

- XMP/propriedades do PDF;
- hash do PDF e do MusicXML de origem;
- versão do renderer, watermark e job;
- manifesto assinado.

Metadados são removíveis e, portanto, complementares.

### 4. Assinatura/certificação digital

A assinatura do PDF permite detectar modificação posterior. Ela não impede edição nem substitui a marca visível.

## Posicionamento orientado por geometria

O renderer deve fornecer bounding boxes de:

```text
systems
staves
notes
lyrics
text/dynamics
page margins
```

O `WatermarkPlanner` calcula safe zones. Se não houver espaço seguro, usa rodapé/margens e reduz repetição; nunca invade símbolos para aumentar resistência.

## Perfis

| Perfil | Uso | Intensidade |
|---|---|---|
| `preview` | visualização antes de baixar/aceitar | mais visível e repetida. |
| `personal_download` | arquivo final do usuário | discreta, token por página e assinatura. |
| `internal_review` | QA/suporte | inclui build/correlation token não público. |

## MusicXML

MusicXML é editável. Pode conter `identification`, `credit` e manifesto externo, mas qualquer metadado pode ser removido. O W_Flyer não deve alegar watermark resistente no arquivo MusicXML. A proteção principal aplica-se ao PDF/imagem renderizada e à prova server-side.

## Direitos, autoria e mensagem da marca

A marca identifica a geração ou a cópia emitida pelo serviço; ela não transfere direitos sobre a composição, o arranjo ou a edição enviada pelo usuário. Portanto:

- não usar `© W_Flyer` sobre a obra, salvo quando houver titularidade comprovada daquele conteúdo;
- preferir texto como `Gerado com W_Flyer · WF-7K3D-9Q2M`;
- exigir que o usuário declare possuir autorização para processar e exportar a partitura;
- preservar créditos do autor, compositor, arranjador e editor presentes na fonte;
- não remover avisos de copyright do documento original;
- separar política de watermark por plano/produto de qualquer alegação de propriedade intelectual.

## Acessibilidade e privacidade

- marcar conteúdo visual como artifact na estrutura PDF quando suportado;
- não inserir texto repetido na ordem de leitura;
- não usar PII visível;
- permitir verificação por token sem revelar a partitura;
- documentar retenção do vínculo token-hash.

## Testes

- leitura por músico em tela, impressão P&B e baixa qualidade;
- zoom, crop, reimpressão e conversão imagem/PDF;
- token aparece em todas as páginas previstas;
- assinatura falha após edição;
- watermark não altera bounding boxes musicais nem conteúdo semântico;
- contraste não confunde símbolo musical;
- ausência de PII em bytes, metadata e texto visível.
