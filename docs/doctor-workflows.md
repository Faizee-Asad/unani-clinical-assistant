# Doctor and clinic workflow examples

These workflows are designed to keep the tool in a safe documentation-support role.

## OPD documentation workflow

1. Enter only de-identified case details.
2. Ask for an OPD note draft with missing information and red flags.
3. Review red flags first.
4. Edit the draft using clinical judgment.
5. Add final diagnosis and treatment only outside the tool or after practitioner review.
6. Store only the approved clinical record in the clinic system.

Prompt example:

```text
/unani-clinical-assistant
Mode: OPD note
Role: registered practitioner
Data: de-identified adult patient case below.
Need: structured note, red flags, missing questions, and patient education points. Do not prescribe.
```

## Referral letter workflow

Use when the case is outside scope, has red flags, needs investigation, or requires specialist/emergency assessment.

Prompt example:

```text
/unani-clinical-assistant
Draft a concise referral letter for this de-identified patient. Highlight red flags and reason for referral. Do not include treatment advice.
```

## Patient handout workflow

Use for plain-language education after clinician review.

Prompt example:

```text
/unani-clinical-assistant
Create a patient-friendly handout for clinician review. Include what to monitor, lifestyle points to discuss, and warning signs requiring urgent care. Do not prescribe medicines.
```

## Drug monograph workflow

Use only as a blank verification scaffold. Do not accept invented doses or safety claims.

Prompt example:

```text
/unani-clinical-assistant
Create a drug monograph verification table for [drug name]. Mark all dose, safety, pregnancy/lactation, interaction, and reference fields as needing verification.
```

## Teaching and viva workflow

Prompt example:

```text
/unani-clinical-assistant
Prepare a BUMS viva guide for [topic]. Include Unani concept map, modern correlation, red flags, likely questions, and common mistakes.
```
