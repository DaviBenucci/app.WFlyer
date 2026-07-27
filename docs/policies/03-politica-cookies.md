# Política de Cookies — estrutura do documento

> Status: rascunho. A versão final depende do inventário técnico real do site e da aplicação.

## 1. Princípio

Não instalar cookies não essenciais antes de a escolha do usuário quando a base aplicável exigir consentimento.

## 2. Categorias

| Categoria | Exemplo de finalidade | Pode ser bloqueada? | Inventário real |
|---|---|---|---|
| Estritamente necessária | sessão, CSRF, segurança | não sem quebrar a função | `PENDENTE` |
| Preferência | tema, idioma | sim | `PENDENTE` |
| Analítica | medição de uso | sim | `PENDENTE` |
| Marketing | campanhas | sim | `PENDENTE` |

A categoria não autoriza automaticamente a ferramenta; cada cookie deve ser inventariado.

## 3. Inventário

Campos obrigatórios:

```text
name
provider
purpose
category
first_or_third_party
retention
secure
http_only
same_site
legal_basis_or_consent_rule
environments
```

## 4. Preferências

A página deve permitir:

- aceitar necessárias;
- aceitar todas as opcionais;
- rejeitar opcionais;
- selecionar categorias;
- alterar decisão posteriormente;
- registrar versão do banner e preferência.

## 5. Proibições

- banner que dificulta rejeitar;
- marcar opcionais por padrão;
- carregar marketing antes da escolha;
- classificar ferramenta de marketing como necessária;
- usar texto genérico sem inventário.
