# Registro de riscos e pre-mortem do W_Flyer

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Antecipar falhas antes do início do código e transformar cada risco relevante em contrato, teste, observabilidade ou gate. A matriz detalhada de cenários está em `../qa/19-matriz-falhas-pre-mortem.md`.

Não existe lista finita capaz de prever todo defeito futuro. Por isso, esta documentação define também uma política para falhas desconhecidas: qualquer incidente novo gera um `risk_id`, fixture de regressão, causa raiz e atualização do gate correspondente.

## Escala

```text
Impacto: 1 baixo | 2 moderado | 3 alto | 4 crítico
Probabilidade: 1 rara | 2 possível | 3 provável | 4 frequente
Prioridade = impacto x probabilidade
```

Risco com impacto crítico não pode ser aceito apenas por baixa probabilidade quando puder alterar música silenciosamente, expor arquivo ou atribuir conteúdo ao autor errado.

## Riscos prioritários

| ID | Risco | I | P | Controle principal | Gate |
|---|---|---:|---:|---|---|
| RISK-MUS-001 | altura de concerto alterada silenciosamente | 4 | 2 | verificador independente e round trip | Core |
| RISK-MUS-002 | dupla transposição por `<transpose>` de origem | 4 | 2 | normalização e snapshot do instrumento | Core |
| RISK-MUS-003 | melodia confundida com voz superior/acompanhamento | 4 | 3 | candidatos por frase e revisão | L |
| RISK-MUS-004 | mudança de voz ou cross-staff perdida | 4 | 3 | grafo de eventos multipauta | M/L |
| RISK-MUS-005 | harmonização altera a melodia bloqueada | 4 | 2 | hash/invariante por evento | H |
| RISK-MUS-006 | acorde ou voicing impossível no destino | 4 | 3 | perfil instrumental e solver de tocabilidade | A/H |
| RISK-MUS-007 | análise tonal ignora modulação/modalidade | 3 | 3 | mapa por região e revisão | H |
| RISK-MUS-008 | cadência ou suspensão destruída | 3 | 3 | análise de frase e notas não harmônicas | H |
| RISK-MUS-009 | score e partes divergem | 4 | 2 | grafo canônico único e teste de consistência | E |
| RISK-MUS-010 | áudio segue ordem diferente da partitura | 3 | 3 | mapa de execução de repetições/jumps | D/Q |
| RISK-OMR-001 | OMR publica nota/ritmo incorreto como verificado | 4 | 3 | origem não verificada, revisão e gate de corpus | P |
| RISK-ENG-001 | renderização cria colisão que muda leitura | 4 | 2 | detector geométrico e revisão humana | R |
| RISK-UX-001 | UI mistura transpor, extrair e harmonizar | 4 | 3 | operação explícita e resumo persistente | todas |
| RISK-UX-002 | warning crítico fica escondido em toast | 4 | 2 | painel persistente e bloqueio de ação | todas |
| RISK-UX-003 | referência visual externa é copiada literalmente | 2 | 3 | pacote interno e revisão de licença | F |
| RISK-UX-004 | IA inventa card, fluxo ou estado ausente | 3 | 4 | manifesto de referências e diff visual | F |
| RISK-BE-001 | retry duplica artefato ou revisão | 3 | 3 | idempotência e constraints | Core |
| RISK-BE-002 | job preso publica saída parcial | 4 | 2 | lease, heartbeat e publicação atômica | Core |
| RISK-BE-003 | modelo/solver muda sem reprodutibilidade | 4 | 2 | manifest, seed e rollout versionado | H/A |
| RISK-BE-004 | confidence global oculta região ambígua | 4 | 3 | decisão por evento/região | L/H |
| RISK-SEC-001 | IDOR entre sessões | 4 | 2 | autorização por `session_id` | Core |
| RISK-SEC-002 | XML/PDF hostil esgota recursos | 4 | 3 | sandbox e limites | Core/P/R |
| RISK-SEC-003 | título/letra injeta instrução em modelo | 4 | 2 | metadado tratado como dado não confiável | H |
| RISK-SEC-004 | partitura enviada é usada para treino sem consentimento | 4 | 2 | política de finalidade e opt-in separado | todas |
| RISK-LGL-001 | créditos/copyright do original são removidos | 4 | 2 | preservação e diff de metadados | todas |
| RISK-LGL-002 | watermark sugere titularidade do W_Flyer | 3 | 2 | texto neutro e manifesto | W |
| RISK-OPS-001 | custo de OMR/harmonia gera negação de serviço | 3 | 3 | quotas por complexidade e fila separada | P/H |
| RISK-OPS-002 | corpus de avaliação vaza para treino | 4 | 2 | split congelado e controles de acesso | L/H |

## Tratamento obrigatório

Cada risco deve ter:

```text
risk_id
owner
status
control_design
control_evidence
test_ids
metrics
residual_risk
review_date
```

Estados:

```text
identified | designed | implemented | evidenced | accepted | retired
```

`accepted` exige justificativa explícita; não significa resolvido.

## Política de falha desconhecida

Quando ocorrer falha não prevista:

1. impedir publicação quando houver dúvida sobre integridade musical ou autorização;
2. preservar artefatos internos mínimos para investigação, sem ampliar retenção de conteúdo além da política;
3. criar código público apenas se houver ação útil para o usuário;
4. registrar `incident_id` e `risk_id` novo;
5. adicionar fixture mínima reproduzível;
6. corrigir transformador e validador quando aplicável;
7. revisar se o problema afeta outros instrumentos, formatos ou operações;
8. executar regressão no corpus congelado;
9. atualizar documentação e changelog antes do rollout.

## Gate pré-código

Antes da primeira implementação, os riscos `RISK-MUS-001`, `RISK-UX-001`, `RISK-BE-001`, `RISK-SEC-001` e `RISK-SEC-002` devem possuir controles desenhados, testes planejados e owner definido. Os demais entram conforme a trilha correspondente.
