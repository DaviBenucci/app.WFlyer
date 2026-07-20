# Funcionalidade de modo de ensaio

> Status: canônico para trilha Q. Capacidade futura.

## Objetivo

Oferecer prática orientada à partitura aprovada com áudio, loop, contagem e anotações.

## Recursos

- abrir versão específica;
- loop por compasso/frase;
- andamento e metrônomo;
- count-in;
- solo/mute;
- cursor opcional;
- anotações;
- page turn assistido;
- atalhos/pedal;
- setlist futuro.

## Regra de dados

O modo de ensaio referencia versão imutável. Uma nova transposição/harmonização não altera sessão de ensaio existente sem ação do usuário.

## Offline

Feature flag separada. O cache não inclui tokens e respeita licença/retenção. A UI informa quando o arquivo é apenas local e quando a versão foi revogada/expirada no servidor.
