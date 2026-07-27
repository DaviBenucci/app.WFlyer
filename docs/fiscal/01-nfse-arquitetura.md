# Arquitetura de NFS-e

> Status: proposta pré-CNPJ; integração fiscal permanece desabilitada. Revisão: 2026-07-27.

## Separação

```text
payment paid
→ obligation created
→ fiscal queue
→ FiscalProvider
→ authorized/rejected/pending
→ XML/PDF stored privately
```

Pagamento aprovado não depende da disponibilidade imediata do emissor fiscal. Falha fiscal cria pendência e alerta.

## Adapter

```python
class FiscalProvider:
    def issue(self, request): ...
    def query(self, external_id): ...
    def cancel(self, external_id, reason): ...
    def replace(self, external_id, request): ...
    def download_documents(self, external_id): ...
```

Implementações possíveis:

- emissor nacional;
- emissor municipal;
- provedor fiscal intermediário;
- processo manual assistido durante implantação inicial.

## Estados

```text
not_required
pending_data
queued
submitted
authorized
rejected
cancellation_pending
canceled
replacement_pending
replaced
manual_review
```

## Dados

- tomador;
- serviço;
- competência;
- valores;
- descontos/retenções;
- identificador do pagamento;
- código municipal/nacional;
- XML/DANFSe;
- protocolo;
- eventos.

## Fontes oficiais

- Documentação atual NFS-e: https://www.gov.br/nfse/pt-br/biblioteca/documentacao-tecnica/documentacao-atual
- Serviço de emissão: https://www.gov.br/pt-br/servicos/emitir-nota-fiscal-de-servico-eletronica
