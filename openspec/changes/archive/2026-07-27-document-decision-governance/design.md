# Design — governança de decisões

Três YAMLs validados por JSON Schema formam a fonte de verdade: decisões, evidências e gates. Cada decisão possui pacote humano completo; visões resumidas são geradas. Evidência aceita registra artefatos, revisão, commit, ambiente e datas. Rejeitada/stale não satisfaz gate. Aprovação humana gera decision record; implementação só ocorre em OpenSpec posterior.
