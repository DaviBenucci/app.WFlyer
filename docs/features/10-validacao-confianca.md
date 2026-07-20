# Validação, warnings e confiança

## Princípio

Métricas brutas de engine são diagnósticas e não devem ser apresentadas como verdade compreensível ao usuário. Porém, esconder risco material também é incorreto.

## Saída pública

O usuário pode receber warnings categóricos:

```text
OMR_REVIEW_RECOMMENDED
LAYOUT_MAY_DIFFER
ENHARMONIC_SIMPLIFICATION
TARGET_CLEF_REVIEW_RECOMMENDED
OUT_OF_RECOMMENDED_RANGE
SOURCE_METADATA_ASSUMED
```

Cada warning possui:

```text
code
message
action opcional
location opcional (página/medida, quando confiável)
```

Não incluir score numérico, símbolo interno, stacktrace, quantidade bruta do parser ou versão do engine na UI comum.

## Regra de entrega

- sem violação obrigatória e sem warning material: `completed`;
- sem violação obrigatória, com warning: `completed_with_warnings`;
- qualquer invariante obrigatório violado: `failed`;
- OMR abaixo do gate: falha, não “resultado com confiança baixa” enganoso.

## Diagnóstico interno

Pode registrar:

```text
engine/version/config
confidence agregada e por região
símbolos não reconhecidos
medidas/eventos parseados
resultado de cada invariante
tempo e recursos por stage
```

Acesso é restrito, retenção minimizada e nenhum dado é enviado a terceiros sem decisão de privacidade.

## Mensagem padrão

```text
Revise a partitura transposta antes de usá-la em ensaio ou apresentação.
```

A mensagem geral não substitui avisos específicos.

## Testes

- DTO público contém apenas warning allowlisted;
- warning material aparece na tela e no resultado;
- score bruto não aparece;
- violação semântica bloqueia publicação;
- localização imprecisa não é apresentada como exata.

## Nível de garantia público

Além de warnings, a API retorna um dos níveis definidos em `../backend/19-confiabilidade-musical-fail-closed.md`. Warnings não elevam garantia. Uma ambiguidade que muda notas deve pausar o job; não pode virar apenas banner amarelo com download ativo.

Para harmonização, separar:

```text
restrições validadas
melodia preservada
variante escolhida pelo usuário
```

Isso não equivale a afirmar intenção autoral ou superioridade estética.
