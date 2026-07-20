# Verificador de tocabilidade e dificuldade

> Status: canônico para trilhas A, H e E. Capacidade desabilitada no Core.

## Objetivo

Separar integridade musical de viabilidade física e idiomatismo.

## Tipos de regra

```text
HARD_IMPOSSIBLE
HARD_PROFILE_LIMIT
SOFT_DIFFICULTY
SOFT_IDIOMATIC
EDITORIAL_SUGGESTION
UNKNOWN_TECHNIQUE
```

## Entradas

- eventos escritos e soantes;
- andamento e mapa métrico;
- perfil instrumental versionado;
- nível do intérprete;
- articulações, dinâmica e duração;
- contexto de frase;
- posição/dedilhado quando disponível;
- configuração do instrumento, afinação/capo/baquetas.

## Findings

```ts
type PlayabilityFinding = {
  finding_id: string
  instrument_profile_version: string
  severity: 'blocking' | 'warning' | 'suggestion'
  category: string
  source_event_ids: string[]
  region: MusicalRange
  evidence_codes: string[]
  possible_options: AdaptationOption[]
}
```

## Regras transversais

- extensão absoluta;
- faixa confortável;
- polifonia simultânea;
- span;
- saltos por unidade de tempo;
- densidade de ataques;
- sustain necessário;
- duração sem respiração;
- repetição/fadiga;
- legibilidade de clave/registro.

## Regras específicas

Cada família usa plugin/solver próprio. `max_simultaneous_notes` não prova que um acorde é executável. Para cordas/violão, a combinação de pitches e posições importa; para sopros, respiração, registro e dedilhado; para teclado, mãos e span.

## Perfil de nível

O mesmo trecho pode ser possível para profissional e inadequado para iniciante. O nível escolhido altera warnings, nunca a física absoluta.

## Resultado

```text
PLAYABLE
PLAYABLE_WITH_WARNINGS
ADAPTATION_RECOMMENDED
ADAPTATION_REQUIRED
UNMODELED_TECHNIQUE_REVIEW
UNPLAYABLE_IN_PROFILE
```

## Gate

- regras derivadas de fontes/revisão de instrumentistas;
- fixtures positivas e negativas;
- medição de falso bloqueio e falso aceite;
- benchmark por andamento;
- explicação e alternativas;
- override auditável apenas para warnings, não para estrutura inválida.
