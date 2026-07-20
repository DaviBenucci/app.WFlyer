# Sessão anônima e autorização

> Status: canônico. Revisão: 2026-07-20.

## Objetivo

Permitir um MVP sem conta de usuário, mas não sem autenticação, propriedade ou proteção contra acesso indevido.

## Modelo

1. O navegador chama `POST /api/v1/sessions/anonymous`.
2. A API cria token opaco aleatório e persiste somente seu hash.
3. O token é entregue em cookie `HttpOnly`.
4. A API entrega um CSRF token separado para header.
5. Uploads, jobs e artefatos recebem `session_id`.
6. Toda rota de objeto consulta por `(id, session_id)`.

Um UUID difícil de adivinhar é defesa adicional, não autorização.

## Cookie

```text
HttpOnly
Secure em HTTPS
SameSite=Lax
Path=/
Max-Age coerente com retenção
sem Domain amplo desnecessário
```

A rotação/renovação não pode trocar a propriedade dos recursos. Sessões revogadas ou expiradas retornam `401` em rotas protegidas.

## Renovação e janela de acesso

A sessão usa expiração deslizante controlada pelo servidor:

- `POST /api/v1/sessions/anonymous` cria ou renova a sessão e sempre devolve um CSRF token válido;
- respostas autenticadas podem renovar `expires_at` e emitir novo `Set-Cookie` quando a sessão estiver próxima do limite;
- ao concluir um job, a API deve garantir que a sessão permaneça válida pelo menos até o maior `expires_at` de seus artefatos ativos, respeitado o limite máximo de sessão definido pela política;
- a expiração persistida no banco e o `Max-Age` do cookie devem permanecer coerentes;
- renovar a sessão não altera `session_id`, propriedade, IDs nem retenção dos recursos;
- se a política máxima impedir cobrir toda a retenção, a UI deve comunicar a janela real e a decisão deve ser registrada em ADR antes do lançamento.

A renovação é feita pelo backend; o frontend nunca calcula nem estende a validade do cookie por conta própria.

## CSRF

Métodos `POST`, `PUT`, `PATCH` e `DELETE` exigem `X-CSRF-Token`. O valor:

- é vinculado à sessão;
- não é colocado em cookie legível como única verificação;
- é rotacionável;
- é comparado em tempo constante quando aplicável;
- não é logado.

Downloads `GET` são side-effect free; deleção nunca usa `GET`.

## Política de resposta

- sessão ausente/inválida: `401 SESSION_REQUIRED`;
- CSRF ausente/inválido: `403 CSRF_INVALID`;
- objeto de outra sessão ou inexistente: `404 RESOURCE_NOT_FOUND`;
- sessão válida, recurso expirado: `410 ARTIFACT_EXPIRED` ou erro equivalente.

Não revelar se um ID pertence a outra sessão.

## Histórico e perda de sessão

O histórico local não concede acesso. Ele apenas guarda IDs/metadados. Se o cookie for apagado, o navegador pode conservar itens no histórico, mas não recuperará recursos do servidor. A UI deve informar:

```text
Este item pertence a uma sessão anterior deste navegador e não está mais acessível.
```

Não criar “token permanente de download” no localStorage para contornar essa regra.

## Limites

Rate limit combina sessão e sinais de rede de forma conservadora. IP não é identidade e não substitui a sessão.

## Evolução para contas

Autenticação com conta é futura. Uma migração pode associar recursos ainda ativos a um usuário somente mediante fluxo explícito, reautenticação e ADR. Não deixar `user_id` fictício como autorização implícita no Core.

## Testes obrigatórios

- A cria recurso e A acessa;
- B recebe `404` para IDs de A;
- UUID conhecido sem cookie recebe `401`;
- CSRF inválido bloqueia mutação;
- cookie não aparece em JS, URL ou log;
- apagar cookie invalida acesso apesar do histórico local;
- renovação preserva recursos;
- sessão revogada não cria nem baixa artefatos.
