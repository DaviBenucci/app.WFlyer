# DEC-001 — Engine OMR de produção

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-001`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual engine OMR pode converter PDFs e imagens suportadas para MusicXML com qualidade, segurança, licença e custo aceitáveis?

## Por que esta decisão existe

A engine escolhida define cobertura, taxa de revisão, custo por página e superfície de ataque do pipeline PDF.

## Prazo e gate

- trilha: `P`;
- fase: `P0`;
- gate: `exit`;
- owner: `engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_CORPUS`
- `BLOCKED_BY_LICENSE_REVIEW`

## Opções conhecidas

- Audiveris em sandbox
- outra engine a identificar por pesquisa
- pipeline híbrido somente após benchmark

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-001`](../../evidence-register.yaml) — Corpus e benchmark OMR (`PLANNED`); devido antes de `P0/P2`.
- [`EVID-002`](../../evidence-register.yaml) — Revisão de licença, sandbox, segurança e custo OMR (`PLANNED`); devido antes de `P0`.

## Critérios de aprovação pré-definidos

- [ ] corpus representativo e licenciado aprovado antes do teste
- [ ] métricas de notas, ritmos, acidentes, armaduras e vozes pré-registradas
- [ ] zero publicação automática de falso resultado verificado no corpus congelado
- [ ] execução automatizável em sandbox sem rede
- [ ] licença e obrigações de distribuição aprovadas
- [ ] custo e latência dentro de campos aprovados, ainda PENDENTE

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `product_owner`
- `music_director`
- `security_lead`
- `legal_reviewer`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Construir o corpus P0 e executar spike comparativo sem habilitar pdf_omr.

## Sequência obrigatória

```text
requisitos congelados
→ plano de experimento
→ evidência bruta
→ comparação
→ risco/rollback
→ aprovação humana
→ ADR/MDR/FDR
→ OpenSpec de implementação
→ implementação
→ validação pós-implementação
```
