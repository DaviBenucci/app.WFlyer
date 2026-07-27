# Critérios de aceite do MVP Core W_Flyer

> Status: canônico. Revisão: 2026-07-20.

O MVP é um produto executável e testado. Documentação completa, isoladamente, não satisfaz estes critérios.

## 1. Escopo e capabilities

- [ ] Core aceita `.musicxml` e XML que seja MusicXML válido.
- [ ] PDF, MXL e imagens são rejeitados quando suas capabilities estão desabilitadas.
- [ ] Uma parte/uma pauta é aceita; estruturas fora da matriz são rejeitadas explicitamente.
- [ ] Saída principal é `transposed_musicxml`.
- [ ] Recursos futuros não aparecem como funcionais.

## 2. Sessão e fluxo funcional

- [ ] Sessão anônima é criada/renovada por cookie `HttpOnly`.
- [ ] CSRF protege mutações.
- [ ] Usuário envia arquivo, escolhe origem/destino e cria job idempotente.
- [ ] Job é processado fora da request.
- [ ] Status/stage/progresso/warnings são recuperáveis após refresh na mesma sessão.
- [ ] Resultado válido pode ser baixado.
- [ ] Usuário pode cancelar job ativo e apagar bytes do servidor.
- [ ] Histórico local funciona sem virar mecanismo de autorização.

## 3. Correção musical

- [ ] Instrumentos usam componentes diatônico, cromático e de oitava.
- [ ] Catálogo inicial coincide com o documento canônico e é versionado.
- [ ] Todos os pares de instrumentos preservam altura de concerto em property tests.
- [ ] Piano→tenor e violão→piano comprovam transposição de oitava.
- [ ] Notas, acordes, armaduras, acidentes, mudanças de tonalidade e harmony suportada são transpostos.
- [ ] Ritmo, medidas, vozes, ties e tuplets são preservados.
- [ ] `<transpose>` do resultado representa o destino e não há dupla transposição.
- [ ] Comparador semântico e corpus/goldens passam.
- [ ] Violação obrigatória impede publicação do artefato.

## 4. MusicXML e arquivos

- [ ] Original, normalized e transposed MusicXML são artefatos distintos e imutáveis.
- [ ] Parser desabilita recursos externos/rede e impõe limites estruturais.
- [ ] Output é parseado e validado novamente.
- [ ] Upload usa streaming, quarentena, nome interno, hash e storage privado.
- [ ] Extensão/MIME/assinatura não são tratados isoladamente como prova.
- [ ] Filename não controla path, header ou comando.

## 5. Autorização e segurança

- [ ] Toda operação de upload/job/artefato filtra por `session_id`.
- [ ] Sessão B não descobre nem acessa recursos de A.
- [ ] Cookie, CSRF, path, `storage_key`, task id, stderr e stacktrace não vazam.
- [ ] Rate limits/quotas/limites de recursos estão configurados e testados.
- [ ] Downloads têm autorização e headers seguros.
- [ ] Corpus hostil de XML e testes de IDOR/CSRF passam.
- [ ] Dependências/containers são fixados e escaneados conforme política.

## 6. Assíncrono, consistência e retenção

- [ ] Banco é fonte de verdade; outbox evita job perdido.
- [ ] Reentrega/retry não duplica artefatos.
- [ ] Erros determinísticos não entram em retry infinito.
- [ ] Heartbeat/lease e reconciliação tratam jobs presos.
- [ ] Estado, stage e retenção são separados e transições inválidas falham.
- [ ] Cancelamento/crash não publicam resultado parcial.
- [ ] Expiração bloqueia download antes do purge.
- [ ] Purge e reconciliação de objetos são idempotentes.

## 7. Frontend, identidade e acessibilidade

- [ ] Capabilities governam formatos/outputs na UI.
- [ ] Fluxo funciona em mobile, desktop, teclado e zoom 200%.
- [ ] PublicShell, StudioShell e UtilityShell são aplicados conforme a documentação.
- [ ] A tela Transpor funciona como workspace musical e não como wizard/dashboard genérico.
- [ ] Origem, destino e intervalo possuem componente visual e equivalente textual próprios.
- [ ] Tokens semânticos substituem tema padrão de biblioteca.
- [ ] Componentes de produto possuem stories, estados extremos e testes de interação.
- [ ] Visual regression foi revisada nos viewports definidos.
- [ ] Labels, foco não encoberto, `aria-live`, contraste, forced colors e reduced motion foram validados.
- [ ] Loading, offline/rede, erro de domínio, warning, cancelamento, sucesso e expiração existem.
- [ ] Intervalo é apresentado com diatônica/semitons/oitava quando relevante.
- [ ] Warning material aparece antes do download.
- [ ] Nenhum token é persistido pelo JavaScript.
- [ ] Rotas públicas não carregam preview/renderizador pesado sem necessidade.
- [ ] A revisão de antipadrões de interface gerada por IA não possui bloqueio aberto.
- [ ] CSS, Motion e GSAP possuem fronteiras claras; nenhuma propriedade é disputada.
- [ ] Motion é a engine padrão da UI e GSAP está restrito a cenas lazy-loaded.
- [ ] Anime.js e React Spring não estão instalados no MVP Core.
- [ ] A intro não bloqueia CTA/conteúdo, toca no máximo uma vez por sessão e possui fallback estático.
- [ ] Reduced motion troca a cena por composição reduzida, não apenas acelera a timeline.
- [ ] Strict Mode, navegação antecipada, background e estado terminal não deixam timeline/listener ativo.
- [ ] GSAP não aparece no bundle das rotas que não usam cena.

## 8. Contratos, operação e evidência

- [ ] OpenAPI e cliente TypeScript gerado estão sincronizados.
- [ ] Migrations aplicam em banco vazio e caminho de rollback/forward foi testado.
- [ ] Health/readiness, logs estruturados, métricas e correlação funcionam.
- [ ] Logs não contêm documento/segredo.
- [ ] Suíte unit/property/integration/contract/E2E/security passa em CI.
- [ ] Comandos, versões, fixtures e resultados estão registrados.
- [ ] Falhas conhecidas e riscos residuais estão documentados.

## 9. Itens que não bloqueiam o Core

- PDF de saída;
- PDF de entrada/OMR;
- MXL;
- login, nuvem, pagamento, compartilhamento e push;
- editor interno de partitura.

Se algum desses itens for habilitado, deve satisfazer seu gate adicional antes de ser anunciado como suportado.

## Regra final

O Core só recebe status **ACEITO** quando todos os itens aplicáveis acima possuem evidência. Item “não testado” é pendência; não é aprovação tácita.

## Não expansão acidental do Core

O MVP Core não é reprovado por não conter extração, harmonização ou watermark. Ele é reprovado se tentar simular essas capacidades sem gates. Qualquer implementação antecipada deve permanecer feature-flagged, sem promessa pública e fora do caminho crítico do Core.

<!-- CRITICAL-VISION-INTEGRATION-2026-07-20 -->

## 10. Fundação crítica e pre-mortem

- [ ] `design-reference/reference-manifest.yaml` e seus schemas validam.
- [ ] Golden references do fluxo Core possuem estados desktop, mobile, erro e reduced motion documentados.
- [ ] Nenhuma referência externa foi copiada como branding, código ou asset.
- [ ] Eventos musicais suportados recebem IDs estáveis durante a execução e aparecem no manifesto/mapeamento.
- [ ] O relatório de garantia aponta checks realmente executados, sem percentuais inventados.
- [ ] Riscos críticos do gate pré-código possuem owner, teste planejado e comportamento seguro.
- [ ] Cada erro público possui estado de UI e não depende apenas de toast.
- [ ] A matriz de falhas conhecida está vinculada a testes implementados ou backlog bloqueante.
- [ ] Existe procedimento testado para transformar incidente desconhecido em fixture de regressão.

Esses itens fortalecem o Core sem habilitar as trilhas L, H, I, A, E ou C.

## Critério de não-regressão por capacidades futuras

A documentação avançada não expande o aceite do Core. O MVP somente é aprovado quando:

- capabilities avançadas aparecem `disabled` no contrato;
- UI não oferece ação sem backend/corpus aprovados;
- protótipos não entram acidentalmente no bundle de produção;
- failure catalog do Core possui owner/teste/evidência para entradas aplicáveis;
- qualquer exceção desconhecida no pipeline crítico termina sem artefato público;
- referência visual do Core passou por estados negativos, mobile, zoom e reduced motion.

<!-- DECISION-GOVERNANCE-ACCEPTANCE:START -->
## Critério de aceite de governança

- [ ] todos os gates de decisão da fase retornam sucesso;
- [ ] nenhuma evidência requerida está `REJECTED` ou `STALE`;
- [ ] nenhuma decisão ativa está `SUPERSEDED` sem gate atualizado;
- [ ] decisões implementadas apontam ADR/MDR/FDR e OpenSpec;
- [ ] evidências aceitas possuem artefatos, review, commit, ambiente e datas;
- [ ] Graphify foi atualizado somente depois das fontes canônicas.
<!-- DECISION-GOVERNANCE-ACCEPTANCE:END -->
