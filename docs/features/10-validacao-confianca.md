# Validação e confiança

## Objetivo

Separar mensagens públicas de diagnósticos internos, mantendo clareza para o usuário.

## Usuário vê

```text
Origem
Destino
Transposição aplicada
Tonalidade resultante quando disponível
Arquivos disponíveis
Avisos claros
```

## Usuário não vê

```text
confidence_score_omr
confidence_score_instrument_detection
confidence_score_key_detection
unrecognized_symbols_count
parsed_measures_count
warnings_count
processing_duration_ms
engine_version
stacktrace
storage_key
path físico
```

## Validações antes da entrega

- Representação musical final existe.
- Partes musicais detectadas quando aplicável.
- Transposição aplicada.
- Armadura alterada quando esperado.
- Artefato final existe.
- Artefato é baixável.

## Mensagem pública de cautela

```text
Confira o resultado antes de usar a partitura em apresentação ou ensaio.
```

## Testes

- DTO público não contém métricas internas.
- Resultado falha se artefato final não existir.
- Erro técnico é convertido em mensagem segura.
