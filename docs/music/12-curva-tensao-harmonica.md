# Curva de tensão musical

> Status: canônico para harmonização e arranjo. Capacidade inferencial/paramétrica.

## Objetivo

Representar crescimento, repouso, suspensão, clímax e resolução sem afirmar que o sistema conhece automaticamente a emoção do compositor.

## Modelo

```ts
type TensionAnchor = {
  position: MusicalPosition
  level: number
  source: 'observed' | 'user' | 'imported'
  confidence?: 'low' | 'medium' | 'high'
  label?: 'rest' | 'growth' | 'suspension' | 'climax' | 'release'
}
```

O nível é relativo dentro da obra e não uma escala universal de emoção.

## Evidências observáveis

- dissonância e estabilidade tonal/modal;
- registro e tessitura;
- densidade e polifonia;
- dinâmica e articulação;
- ritmo harmônico;
- cromatismo;
- pedal/suspensões;
- contorno e repetição;
- andamento e aceleração;
- cadências e frases.

Nenhuma feature isolada determina tensão. Pesos são versionados e dependem do perfil estilístico.

## Uso na harmonização

O motor tenta respeitar âncoras escolhidas:

- não resolver antes de ponto marcado como suspensão;
- não saturar região de repouso;
- aumentar densidade/cromatismo somente dentro do orçamento;
- preservar cadência estrutural;
- oferecer variantes com curvas diferentes quando solicitado.

## Controle do usuário

O usuário pode mover/editar âncoras e comparar impacto. Rótulos como “feliz”, “triste” ou “épico” não são inferidos automaticamente; podem existir como intenção declarada e não como diagnóstico.

## Validação

- a curva não pode justificar violação de melodia bloqueada;
- a alteração deve aparecer no diff;
- a variante registra distância em relação à curva alvo;
- baixa confiança por região é visível;
- avaliação humana usa preferência comparativa, não “verdade única”.
