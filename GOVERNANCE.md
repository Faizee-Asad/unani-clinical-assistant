# Project governance

This project uses a safety-first maintainer model.

## Maintainer responsibilities

Maintainers should:

- Protect patient privacy.
- Require clinical review for high-risk content.
- Reject unsupported cure claims.
- Reject autonomous prescribing or diagnosis workflows.
- Keep documentation transparent about limitations.
- Prefer conservative, referral-aware language.

## Clinical review

A clinical reviewer should review changes that involve:

- Medicines, formulations, or doses
- Regimenal procedures
- Emergency symptoms
- Pregnancy/lactation
- Pediatrics or geriatrics
- Serious chronic disease
- Contraindications/interactions
- Patient-facing instructions

## Release approval

Before release:

1. Run validation and tests.
2. Run PHI scan helper.
3. Review safety policy and disclaimer.
4. Build the skill ZIP.
5. Check that examples are synthetic/de-identified.
6. Confirm no generated content is represented as final medical advice.
