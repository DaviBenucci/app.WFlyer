# Estado fiscal antes da abertura

> Status: proposta pré-CNPJ; integração fiscal permanece desabilitada. Revisão: 2026-07-27.

## Situação

Não estão definidos:

- CNPJ;
- natureza jurídica;
- CNAEs;
- regime tributário;
- inscrição municipal;
- município emissor;
- código de serviço;
- alíquotas e retenções;
- certificado digital;
- provedor de NFS-e.

Logo, a aplicação não deve codificar regras fiscais definitivas nem assumir SEFAZ estadual para um serviço SaaS.

## Regra

Para prestação de serviço, o documento esperado tende a ser NFS-e. A implementação concreta depende do município, enquadramento e plataforma vigente. A documentação oficial nacional possui APIs, XSDs e manuais atualizados, mas a adesão e o fluxo do contribuinte precisam ser confirmados.

## Bloqueios

- `fiscal.invoice_issuance=false`;
- sem credencial/certificado em desenvolvimento comum;
- sem emissão simulada marcada como válida;
- sem registrar imposto como valor final antes da contabilidade.
