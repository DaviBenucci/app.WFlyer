# Matriz de suporte do MVP

> Status: canônico. Revisão: 2026-07-20.

## Formatos de entrada

| Formato | Core | Condição |
|---|---|---|
| `.musicxml` | Suportado | XML seguro, uma parte e uma pauta. |
| `.xml` | Suportado com inspeção | Aceito apenas se o elemento raiz e a estrutura forem MusicXML. |
| `.mxl` | Desabilitado por padrão | Exige gate de ZIP/MXL e feature flag. |
| `.pdf` | Desabilitado por padrão | Exige gate OMR e feature flag `pdf_omr`. |
| `.png`, `.jpg`, `.jpeg` | Fora do MVP | Não aceitar. |

## Estrutura musical

| Capacidade | Core | Comportamento |
|---|---|---|
| Uma parte e uma pauta | Sim | Perfil principal. |
| Múltiplas vozes na mesma pauta | Sim | Ritmo e voz devem ser preservados. |
| Acordes de notas simultâneas | Sim | Todas as alturas são transpostas. |
| Cifras/harmony simples | Sim, quando parseadas | Transpor raiz e baixo. |
| Mudança de tonalidade | Sim | Transpor cada região. |
| Mudança de clave | Preservar | A clave não é automaticamente redesenhada para o destino no Core. |
| Ties e tuplets | Sim | Estrutura temporal preservada. |
| Letras, dinâmica e articulações | Preservar | Não são transpostas. |
| Duas pautas na mesma parte | Não | Rejeitar com `UNSUPPORTED_SCORE_STRUCTURE`. |
| Múltiplas partes | Não | Rejeitar com `UNSUPPORTED_SCORE_STRUCTURE`. |
| Percussão não afinada | Não | Rejeitar. |
| Tablatura | Não | Rejeitar. |
| Microtons | Não | Rejeitar. |
| Instrument change | Não | Rejeitar. |

## Saída e fidelidade

| Item | Compromisso |
|---|---|
| Altura de concerto | Deve ser invariável após a transposição. |
| Grafia das notas | Deve seguir o intervalo diatônico e a política enarmônica. |
| Ritmo e compassos | Devem ser preservados semanticamente. |
| Layout/paginação | Melhor esforço; não precisa ser idêntico ao original. |
| MusicXML `<transpose>` | Deve representar o instrumento de destino. |
| PDF de saída | Somente com adapter habilitado. |

## Regra de expansão

Qualquer nova capacidade exige:

1. alteração desta matriz;
2. ADR ou decisão registrada;
3. fixtures positivas e negativas;
4. critérios de segurança;
5. atualização de API/UX quando aplicável.
