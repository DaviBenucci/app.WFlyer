# Segurança de colaboração e compartilhamento

> Status: canônico para recurso futuro. Revisão: 2026-07-20.

## Convites

- token aleatório de alta entropia;
- hash persistido;
- escopo por work/version/review;
- papel mínimo;
- expiração e revogação;
- uso único quando aplicável;
- não aparecer em logs/referrers.

## Autorização

Cada request valida participant e scope. Conhecer `review_session_id` não concede acesso.

## Conteúdo

Comentários são sanitizados, limitados e tratados como dados não confiáveis. Upload de anexo fica desabilitado até política própria.

## Privacidade

Participantes veem somente identidade necessária. Links pseudônimos e notificações não expõem título/obra além do consentido.

## Auditoria

Registrar convite, aceitação, comentário, mudança, aprovação, revogação e download, sem armazenar conteúdo musical em log.
