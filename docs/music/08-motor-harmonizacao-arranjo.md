# Motor de harmonização e arranjo

> Status: canônico para a trilha futura de harmonização. Capacidade desabilitada no MVP Core.

## Princípio

Harmonizar é criar material musical novo. A aplicação não deve apresentar uma proposta harmônica como única resposta correta nem afirmar que inferiu com certeza a intenção emocional do autor.

O sistema deve preservar características observáveis da obra, respeitar parâmetros declarados pelo usuário e entregar alternativas comparáveis.

## Pré-condição obrigatória

A linha melódica deve estar confirmada e bloqueada. Para entrada polifônica, isso exige `EXTRACT_MELODY` aprovado ou seleção explícita da voz/parte melódica.

## Perfil de intenção musical

O usuário escolhe ou confirma um perfil tipado:

```ts
type HarmonyProfile = {
  style: 'tonal_classical' | 'popular' | 'jazz_light' | 'modal'
  tonal_center?: string
  mode?: 'ionian' | 'dorian' | 'phrygian' | 'lydian' | 'mixolydian' | 'aeolian' | 'locrian'
  harmonic_density: 'sparse' | 'balanced' | 'rich'
  harmonic_rhythm: 'one_per_bar' | 'half_bar' | 'beat' | 'adaptive'
  tension: 'stable' | 'moderate' | 'expressive'
  voicing: 'close' | 'open' | 'keyboard' | 'guitar' | 'choral'
  difficulty: 'basic' | 'intermediate' | 'advanced'
  preserve_melody: true
  allowed_chromaticism: 'diatonic' | 'secondary_dominants' | 'modal_interchange' | 'extended'
}
```

Andamento, modo, dinâmica, articulação, contorno e ritmo podem gerar sugestões, mas não determinam sozinhos “sentimento” ou intenção autoral. A UI deve pedir confirmação de linguagem e densidade.

## Contrato de fidelidade autoral

A harmonização deve registrar um orçamento de alteração explícito. O perfil padrão é conservador:

```ts
type FidelityProfile = {
  level: 'strict' | 'conservative' | 'expressive'
  preserve_melody: true
  preserve_phrase_boundaries: boolean
  preserve_existing_harmony: 'all' | 'structural' | 'none_present'
  allow_reharmonization: boolean
  allow_modal_interchange: boolean
  allow_chromatic_approach: boolean
  max_harmonic_events_per_measure?: number
}
```

- `strict`: mantém toda harmonia existente e apenas completa lacunas autorizadas.
- `conservative`: preserva melodia, frases, cadências e acordes estruturais; oferece variações locais.
- `expressive`: permite reharmonização mais ampla, sempre como variante separada e opt-in.

O sistema não pode usar andamento, modo ou tonalidade para declarar sozinho que a obra é “feliz”, “triste”, “épica” ou equivalente. Descritores expressivos são entrada confirmada pelo usuário, não verdade extraída da partitura. Toda divergência da harmonia original precisa aparecer no diff e no manifesto.

## Pipeline

```text
melodia confirmada
-> análise de métrica, andamento e frases
-> detecção de centros tonais/modais por região
-> classificação de notas estruturais e não harmônicas
-> candidatos de ritmo harmônico
-> candidatos de função/acorde
-> geração de voicings para o instrumento
-> avaliação de restrições rígidas
-> otimização de condução de vozes
-> ranking por objetivos estéticos
-> 2 a 4 variantes
-> revisão, audição e escolha do usuário
-> MusicXML derivado + manifesto
```

## Restrições rígidas

Uma variante é inválida quando:

- altera pitch, onset ou duração da melodia bloqueada sem autorização;
- produz notas fora da extensão absoluta do destino;
- excede polifonia física ou span configurado;
- cria medidas temporalmente inválidas;
- viola o modo/perfil que o usuário bloqueou;
- gera vozes cruzadas ou colisões proibidas pela política;
- produz cifras/voicings incompatíveis entre si;
- perde provenance de notas geradas;
- não pode ser renderizada/parseada no perfil aprovado.

## Objetivos flexíveis

O ranker pode favorecer:

- movimento conjunto e manutenção de notas comuns;
- cadências coerentes com a frase;
- distribuição equilibrada de tensão e resolução;
- variedade sem romper a linguagem escolhida;
- condução de baixo adequada ao estilo;
- menor salto e melhor tocabilidade;
- densidade compatível com andamento e textura;
- preservação de espaço para a melodia.

Regras de contraponto clássico, paralelas, dissonâncias e resoluções são aplicadas somente quando o perfil estilístico exigir; não devem ser universalizadas para jazz, música modal ou popular.

## Estratégia de implementação

### Primeira versão

Motor de regras + busca/otimização com candidatos explicáveis. Cada decisão registra função, acorde, inversão, voicing, regra aplicada e custo.

### Modelo generativo opcional

Um modelo pode atuar como **gerador de candidatos**, nunca como validador final. A saída passa pelas mesmas restrições, recebe versão/seed/parâmetros e pode ser rejeitada integralmente.

## Instrumentos monofônicos

Se o destino não suporta acordes, `HARMONIZE` não deve escrever várias notas impossíveis na mesma parte. As saídas permitidas são:

- cifras sobre a melodia;
- parte adicional de acompanhamento para outro instrumento;
- score multiparte futuro;
- sugestão harmônica sem inserção na parte monofônica.

## Versões e alternativas

A harmonização nunca sobrescreve a fonte. Cada variante possui:

```text
harmony_plan
harmonized_musicxml
rendered_preview
engine_manifest
random_seed
user_selection_status
```

O usuário pode comparar, regenerar com parâmetros diferentes, editar a seleção e retornar à melodia original.

## Aceite musical

- `preserve_melody` passa em 100% dos eventos bloqueados;
- todas as restrições rígidas passam;
- extensão e polifonia do destino passam;
- pelo menos duas variantes são diferentes semanticamente quando solicitado;
- músico revisor avalia corpus por estilo;
- o produto chama a saída de “proposta de harmonização”, não de “harmonia correta”.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## Análise que precede a geração

O motor não deve harmonizar apenas a partir de escala global. Requer mapa regional de:

- frase e cadência;
- centro tonal/modal;
- notas estruturais e não harmônicas;
- baixo existente;
- símbolos harmônicos existentes;
- ritmo harmônico;
- métrica e andamento;
- curva de tensão confirmada ou editável.

## Orçamento de alteração

Cada perfil declara o que pode mudar:

```text
melodia: locked
ritmo da melodia: locked
acordes existentes: preserve | complete | replace_with_approval
baixo: preserve | vary_within_range | regenerate
vozes internas: add | revoice | preserve
cadências estruturais: preserve | suggest_alternative
cromatismo: bounded
```

## Explicação por variante

A variante deve expor função/linguagem, acordes preservados/criados/substituídos, voice leading, tensões, findings de tocabilidade e diferença semântica em relação às outras variantes.

## Falhas sem variante

Quando nenhuma proposta satisfizer constraints, o resultado correto é `NO_VALID_HARMONY_VARIANT`. É proibido relaxar uma restrição rígida sem nova aprovação do usuário e novo job/manifesto.
