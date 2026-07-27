# Business launch readiness

## Requirement: pre-company status is explicit

The repository SHALL state that the company is not yet opened and SHALL NOT represent unconfirmed corporate, tax or fiscal data as existing.

### Scenario: public documentation before company opening

- **GIVEN** the planned opening is at the end of August 2026
- **WHEN** an agent updates public or technical documentation
- **THEN** it uses project/company-in-formation language
- **AND** keeps production billing and fiscal issuance disabled.

## Requirement: digital properties are isolated

The company website, SaaS application and client websites SHALL use separate repositories and deployment boundaries.

### Scenario: application domain

- **WHEN** the SaaS is deployed
- **THEN** `app.wflyer.com.br` resolves by DNS to the application infrastructure
- **AND** the institutional site and client sites are outside the SaaS production blast radius.

## Requirement: payment provider remains proposed

Stripe SHALL remain the preferred candidate and Mercado Pago the documented alternative until a sandbox spike and business validation approve an ADR.

### Scenario: agent proposes payment implementation

- **WHEN** no accepted billing ADR exists
- **THEN** the agent SHALL NOT install a production payment SDK or enable billing.

## Requirement: fiscal rules require professional validation

The system SHALL NOT infer CNAE, tax regime, NFS-e issuer, certificate type, service code or tax rates.

### Scenario: fiscal implementation request

- **WHEN** corporate and municipal decisions are unavailable
- **THEN** the capability remains disabled
- **AND** the missing decision is recorded.

## Requirement: production architecture anticipates failure

The production target SHALL separate state, compute, queues and object storage, use idempotent processing, backup/restore and documented runbooks.

### Scenario: a worker terminates during a job

- **WHEN** lease/visibility expires
- **THEN** another worker may retry safely
- **AND** duplicate results or credit effects are prevented.
