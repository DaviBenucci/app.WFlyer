# Relatório de integração da visão crítica — 2026-07-20

> Status: relatório técnico. Não substitui os documentos canônicos.

## Objetivo

Transformar a crítica de produto e de prática musical em requisitos, contratos, riscos, gates, referências visuais e plano de evolução antes do início do código.

## O que foi integrado

- tese de produto: transformar, explicar, verificar, adaptar e devolver controle;
- separação entre transposição, extração, redução, adaptação, harmonização e arranjo;
- grafo semântico interno com IDs estáveis e MusicXML interoperável;
- Musical Diff e proveniência por evento;
- análise regional de melodia, forma, tonalidade, cadência e tensão;
- perfis instrumentais e tocabilidade contextual;
- áudio A/B, mapa de playback e modo de ensaio;
- score, partes, ensemble e consistency checker;
- revisão/versionamento/colaboração com concorrência explícita;
- direitos, atribuição, dados de IA e assets licenciados;
- referências visuais internas machine-readable e protótipos originais;
- pre-mortem, FMEA, falhas desconhecidas e conselho musical de release.

## Soluções para falhas centrais

| Problema | Solução documental |
|---|---|
| transposição correta, mas impossível de auditar | manifesto, event mapping, Musical Diff e checker independente |
| melodia confundida com nota mais aguda | candidatos por frase, evidências, ambiguidade regional e revisão |
| piano/harmônico para instrumento monofônico | operação explícita de extração/redução e profile de destino |
| harmonização genérica pela escala | análise de forma/cadência/notas não harmônicas, orçamento de alteração e variantes |
| escrita dentro do range, porém ruim | playability/idiomatic checker contextual e conselho instrumental |
| score e partes divergentes | projeções da mesma revisão e verificador bidirecional |
| áudio não corresponde à notação | playback map por ocorrência e validação de pitch/timing |
| frontend com aparência genérica de IA | reference manifest, specs, protótipos, states e visual gate |
| erro não previsto | kill switch, incidente→risco→fixture→regressão→rollout |

## Limite honesto

Não é possível listar antecipadamente todo defeito que poderá existir. A documentação cobre classes conhecidas/plausíveis e estabelece como detectar, conter e incorporar falhas novas. O projeto ainda precisará implementar e provar cada gate em código, corpus e revisão humana.
