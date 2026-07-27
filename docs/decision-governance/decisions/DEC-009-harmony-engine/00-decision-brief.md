# DEC-009 — Engine ou solver de harmonização

> Status: `REQUIREMENTS_DEFINED`. ID(s) legado(s): `PEND-009`. Implementação autorizada: **não**.

## Pergunta de decisão

Qual abordagem gera variantes reproduzíveis, explicáveis e tocáveis sem modificar a melodia bloqueada?

## Por que esta decisão existe

Um gerador pode produzir música plausível, mas inválida, inexequível ou incoerente com a proposta escolhida.

## Prazo e gate

- trilha: `H`;
- fase: `H1`;
- gate: `exit`;
- owner: `music_engineering_lead`.

## Bloqueios atuais

- `BLOCKED_BY_BENCHMARK`
- `BLOCKED_BY_MUSICAL_REVIEW`
- `BLOCKED_BY_LICENSE_REVIEW`

## Opções conhecidas

- regras + busca
- constraint solver
- modelo apenas como proponente
- abordagem híbrida com verificador independente

Uma alternativa nova só entra na comparação depois de registrar fonte, versão, licença, compatibilidade, custo e motivo de inclusão.

## Evidências obrigatórias

- [`EVID-010`](../../evidence-register.yaml) — Comparativo de motores de harmonização (`PLANNED`); devido antes de `H1-H4`.
- [`EVID-009`](../../evidence-register.yaml) — Perfis harmônicos e revisão musical (`PLANNED`); devido antes de `H0`.

## Critérios de aprovação pré-definidos

- [ ] melodia preservada por invariante
- [ ] planos reproduzíveis e provenance completa
- [ ] restrições rígidas independentes do gerador
- [ ] avaliação cega por músicos
- [ ] licença/dados/custo aprovados
- [ ] variante só publicada após escolha do usuário

Valores ainda não medidos permanecem `PENDENTE`. Thresholds não podem ser ajustados depois do resultado apenas para favorecer uma opção.

## Aprovadores humanos

- `music_director`
- `security_lead`
- `product_owner`

A IA pode preparar pesquisa, experimento e recomendação; não pode assinar aprovação nem mudar o estado para `DECIDED`.

## Próxima ação autorizada

Comparar abordagens somente após DEC-008 e DEC-015.

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
