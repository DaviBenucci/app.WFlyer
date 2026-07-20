# Versionamento musical e ramificações

> Status: canônico para recursos avançados. Revisão: 2026-07-20.

## Objetivo

Manter fontes, transformações, revisões e variantes sem sobrescrita destrutiva.

## Modelo

```text
source version
├── transposition version
├── melody selection version
│   ├── harmony variant A
│   └── harmony variant B
└── adaptation branch
```

## Regras

- versões são imutáveis;
- branch registra parent e operação;
- nova decisão humana cria revision;
- regenerar não substitui variante;
- merge automático só para alterações independentes e comprováveis;
- conflito musical exige revisão;
- aprovação, diff e artefatos são vinculados ao version_id;
- purge de bytes preserva metadado mínimo conforme política.

## Nomeação

A UI usa títulos compreensíveis e não expõe apenas UUID. Exemplo:

```text
Original
Transposição para Trompete Bb
Melodia revisada v2
Harmonia conservadora — Variante B
Adaptação para nível intermediário
```
