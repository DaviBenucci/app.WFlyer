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
