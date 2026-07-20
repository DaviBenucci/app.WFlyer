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
