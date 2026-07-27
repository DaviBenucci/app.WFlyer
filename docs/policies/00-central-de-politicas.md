# Central de políticas

> Status: especificação de conteúdo da página pública `/politicas`. Revisão jurídica pendente.

## 1. Finalidade

A página deve reunir, em linguagem clara, os documentos que explicam como o W_Flyer opera, trata dados, cobra, recebe conteúdo musical e oferece suporte.

Ela não pode esconder documentos em menus profundos nem exigir login.

## 2. Identificação da empresa

Campos obrigatórios antes da publicação:

| Campo | Valor |
|---|---|
| Razão social | `PENDENTE APÓS ABERTURA` |
| Nome empresarial ou marca | `W_Flyer` |
| CNPJ | `PENDENTE APÓS ABERTURA` |
| Endereço empresarial | `PENDENTE` |
| E-mail de suporte | `PENDENTE` |
| E-mail de privacidade | `PENDENTE` |
| E-mail de segurança | `PENDENTE` |
| Responsável jurídico | `PENDENTE` |

A página não deve ser publicada como final enquanto esses campos estiverem pendentes.

## 3. Seções públicas

### Uso da aplicação

- Termos de Uso;
- Política de Uso Aceitável;
- Direitos Autorais e Conteúdo Enviado.

### Dados e segurança

- Política de Privacidade;
- Política de Cookies;
- Retenção e Exclusão;
- Segurança e Incidentes.

### Comercial

- Pagamentos, Assinaturas e Créditos;
- Cancelamento e Reembolso;
- Suporte e Disponibilidade.

## 4. Metadados exibidos

Cada documento mostra:

- título;
- resumo em uma frase;
- versão;
- data de vigência;
- data da última atualização;
- histórico de alterações materiais;
- contato relacionado;
- opção de impressão ou download.

## 5. Aceite

Nem toda política exige caixa de aceite.

O sistema deve registrar aceite explícito quando houver:

- criação de conta para os Termos de Uso e Uso Aceitável;
- primeiro upload para a política de conteúdo e direitos autorais;
- checkout para regras comerciais aplicáveis;
- alteração material que exija novo consentimento ou aceite.

O registro contém:

```text
user_or_session_id
policy_id
policy_version
accepted_at
acceptance_context
locale
ip_hash_or_equivalent_minimized
user_agent_category
```

A necessidade de cada campo deve ser revisada à luz da minimização de dados.

## 6. Mudanças de política

- mudanças editoriais podem manter a mesma versão material;
- mudanças de direitos, deveres, cobrança ou tratamento de dados recebem nova versão;
- usuários impactados devem ser comunicados antes ou na data aplicável;
- quando novo aceite for necessário, a capability relacionada permanece limitada até o aceite;
- versões antigas são preservadas para auditoria.

## 7. Linguagem e acessibilidade

- português do Brasil como idioma inicial;
- frases diretas;
- termos jurídicos acompanhados de explicação simples;
- headings semânticos;
- navegação por teclado;
- impressão legível;
- contraste adequado;
- links identificáveis;
- sem obrigar o usuário a aceitar cookies não essenciais para ler as políticas.

## 8. Estados da página

- documentos em vigor;
- documento atualizado e aguardando vigência;
- documento histórico;
- política indisponível por erro técnico;
- empresa ainda não formalizada: somente preview interno, nunca publicação final.
