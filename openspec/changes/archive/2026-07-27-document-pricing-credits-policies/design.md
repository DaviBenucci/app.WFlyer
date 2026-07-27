# Design

## Documentation layers

1. human-readable pricing principles;
2. fillable decision worksheet;
3. machine-readable pricing template and schema;
4. detailed credit lifecycle;
5. central policy hub;
6. specialized policy drafts;
7. machine-readable policy manifest and schema;
8. frontend page specification for `/politicas`.

## Safety rules

- unresolved values remain `null` or `PENDENTE`;
- production is blocked when required values are unresolved;
- policy drafts contain no invented company identity;
- public policy content requires legal review;
- ledger entries are immutable;
- prices are sourced from an internal versioned catalog.
