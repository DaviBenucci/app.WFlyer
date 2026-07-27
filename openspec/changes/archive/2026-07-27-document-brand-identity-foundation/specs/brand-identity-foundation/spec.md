# Brand identity foundation specification

## Requirement: pending brand state

The repository SHALL represent the official visual identity as pending until explicit human approval is recorded.

### Scenario: agent renders the product before approval

- **WHEN** no approved assets exist in `brand/brand-manifest.yaml`
- **THEN** the interface uses the textual label `W_Flyer`
- **AND** it does not invent a symbol, favicon, wordmark or final palette.

## Requirement: controlled asset structure

The repository SHALL keep master, variant, favicon and guideline assets in separated directories under `brand/`.

### Scenario: a logo is approved

- **WHEN** the product owner approves a visual identity
- **THEN** the manifest records the approved paths, reviewers and date
- **AND** application and institutional site exports are generated from the approved master.

## Requirement: legacy assets remain rejected

The repository SHALL NOT restore or use the removed legacy logo as an implementation reference.

### Scenario: an old image is discovered

- **WHEN** an agent finds an old logo in history, cache or external material
- **THEN** it ignores the asset
- **AND** requests explicit approval before adding any visual identity file.
