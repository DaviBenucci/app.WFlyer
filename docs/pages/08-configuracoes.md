# Tela Configurações locais

## Rota

```text
/configuracoes
```

## Objetivo

Permitir preferências locais simples sem criar conta, sincronização ou serviços externos.

## Escopo MVP

```text
Instrumento de origem padrão opcional
Instrumento de destino padrão opcional
Preferência de formato de resultado
Preferência de redução de movimento
Limpeza de histórico local
```

## Componentes

- `DefaultInstrumentSettings`.
- `MotionSettings`.
- `ResultFormatSettings`.
- `ClearLocalDataButton`.

## Regras

- Configurações ficam locais.
- Não guardar segredos.
- Não guardar arquivo original.
- Respeitar `prefers-reduced-motion`.
- Limpar histórico local exige confirmação.

## Fora do MVP

- Notificações push.
- Sincronização em nuvem.
- Preferências por conta.
- Planos pagos.

## Critérios de aceite

- Preferências locais são salvas.
- Usuário consegue limpar histórico local.
- Redução de movimento é respeitada.
