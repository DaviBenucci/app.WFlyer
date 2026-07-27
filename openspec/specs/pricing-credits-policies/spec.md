# Pricing, credits and public policies

## Status

Canonical documentation contract for future commercial readiness. Implementation and production publication remain disabled.

## Requirements

### Requirement: unresolved commercial values remain explicit

The repository SHALL provide fillable fields and machine-readable templates for prices, plan quotas, credit costs, expiration and financial assumptions.

#### Scenario: documentation is used before benchmarks

- **GIVEN** product costs have not been measured
- **WHEN** an agent reads billing documentation
- **THEN** it finds `PENDENTE` or `null` values instead of invented numbers
- **AND** production enablement is blocked.

### Requirement: credit lifecycle is documented end to end

The documentation SHALL define quote, reservation, consumption, release, expiration, reversal, concurrency, reconciliation and user-visible states.

#### Scenario: a processing job fails internally

- **GIVEN** credits were reserved
- **WHEN** the job cannot publish a billable result
- **THEN** the reservation is released idempotently
- **AND** the original ledger history is preserved.

### Requirement: public policies have a dedicated hub

The product SHALL plan a public `/politicas` page that links to versioned policies for terms, privacy, cookies, billing, refunds, copyright, acceptable use, retention, support and security.

#### Scenario: company data is not available

- **GIVEN** the company has not been formally opened
- **WHEN** policy documents are generated
- **THEN** legal name, CNPJ, address and contacts remain explicit placeholders
- **AND** documents remain marked as drafts not ready for publication.

### Requirement: policy publication is gated

A policy SHALL NOT be published as final until legal review, company identification, effective date, version and operational controls are complete.

#### Scenario: a policy is materially changed

- **GIVEN** a material change affects rights, billing or data use
- **WHEN** the new version becomes effective
- **THEN** version history is preserved
- **AND** acceptance is requested in the appropriate product context when required.
