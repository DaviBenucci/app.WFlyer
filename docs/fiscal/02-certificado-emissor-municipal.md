# Certificado digital, município e emissor

> Status: proposta pré-CNPJ; integração fiscal permanece desabilitada. Revisão: 2026-07-27.

## 1. Não presumir uma solução única

A exigência de certificado, tipo de assinatura, autenticação e endpoint varia conforme:

- emissor nacional ou municipal;
- perfil do contribuinte;
- município;
- regime;
- integração direta ou provedor intermediário;
- versão da documentação.

## 2. Antes de contratar certificado

Confirmar com contador e emissor:

- A1 ou A3;
- uso por API;
- titular correto;
- validade;
- armazenamento e rotação;
- homologação;
- procuração quando aplicável;
- processo de revogação.

## 3. Segurança de A1

Se adotado:

- armazenar em secret manager/KMS;
- acesso somente ao worker fiscal;
- não incluir na imagem;
- rotação e alerta de expiração;
- senha separada;
- auditoria de uso;
- backup criptografado conforme política.

## 4. A3

Pode exigir dispositivo ou serviço de assinatura incompatível com execução totalmente automática. Deve ser avaliado antes da escolha.

## 5. Gate

Nenhuma biblioteca fiscal é implementada até existir documento de decisão com município, emissor, autenticação, ambiente de homologação e exemplos aprovados pelo contador.
