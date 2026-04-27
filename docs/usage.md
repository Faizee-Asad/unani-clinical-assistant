# Usage guide

## Modes

The skill supports:

1. Case-taking
2. OPD documentation
3. Follow-up documentation
4. Patient education
5. Referral letter drafting
6. BUMS viva/exam prep
7. Drug monograph drafting
8. Regimenal therapy documentation
9. Research support
10. General Unani study support

## Prompt pattern

```text
/unani-clinical-assistant
Mode: OPD documentation
Role: BUMS intern
Case: [de-identified case details]
Need: structured OPD note, missing questions, red flags, patient education, and referral triggers.
```

## Include

- Age range
- Chief complaint and duration
- Relevant symptoms and negatives
- Past history
- Current medicines
- Allergies
- Pregnancy/lactation status where relevant
- Vitals/exam/investigations if available
- Purpose: note, handout, referral, viva, etc.

## Do not include

- Names
- Phone numbers
- Address
- Hospital ID
- Exact date of birth
- Photos/scans with identifiers

## Good output expectations

A good output should:

- Start with safety and red-flag review when a patient case is involved
- Mark missing information clearly
- Separate Unani framing from modern clinical correlation
- Avoid final diagnosis and prescribing
- Include clinician verification reminders
- Use patient-friendly language for handouts
