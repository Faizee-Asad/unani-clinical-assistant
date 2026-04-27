# Unani Clinical Assistant — open-source clinical documentation skill

A GitHub-ready open-source project for **BUMS students, Unani practitioners, medical educators, interns, and clinic teams** who need safer, structured assistance for Unani medicine education and clinical documentation.

This repository contains a reusable `unani-clinical-assistant` skill package plus Markdown templates, reference checklists, examples, Python helper scripts, tests, and GitHub Actions validation.

> **Clinical safety note**  
> This project supports education, documentation, research framing, patient communication, and red-flag awareness. It does **not** diagnose, prescribe, replace emergency care, replace a registered practitioner, or override institutional protocol or local law.

## What this project helps with

- Structured Unani case-taking
- OPD note drafting for clinician review
- Follow-up notes
- Patient education handouts
- Referral letter drafting
- Red-flag and urgent referral checks
- Mizaj and Asbab-e-Sitta Zarooriya documentation
- Moalajat-style study notes and viva preparation
- Ilaj Bit Tadabeer / regimenal therapy documentation support
- Drug monograph drafting with strict verification fields
- Research question, PICO/PECO, and case-presentation support
- Basic de-identification/anonymization helper scripts

## What this project must not be used for

- Autonomous diagnosis
- Autonomous prescribing or dose selection
- Emergency triage or emergency management
- Giving procedural instructions without qualified supervision
- Replacing a qualified practitioner, supervisor, hospital policy, or local regulation
- Making guaranteed cure or guaranteed safety claims
- Storing or publishing real patient identifiers
- Fabricating classical references, evidence, dosages, indications, or safety data

## Repository layout

```text
unani-clinical-assistant/
  skills/
    unani-clinical-assistant/
      SKILL.md
      safety-policy.md
      reference/
      templates/
      examples/
  docs/
  examples/
  scripts/
  tests/
  .github/
    workflows/
    ISSUE_TEMPLATE/
```

## Quick start

### 1. Validate the skill

```bash
python scripts/validate_skill.py skills/unani-clinical-assistant
```

### 2. Run tests

```bash
python -m pip install -e .[dev]
python -m pytest
```

### 3. Build the upload ZIP

```bash
python scripts/make_skill_zip.py
```

This creates:

```text
dist/unani-clinical-assistant-skill.zip
```

The ZIP has `SKILL.md` at the root, which is the expected layout for skill upload.

## Example skill prompts

```text
/unani-clinical-assistant
Create a structured case sheet for an adult patient with chronic constipation, low appetite, poor sleep, and sedentary lifestyle. Include red flags, missing questions, and patient education. Do not prescribe.
```

```text
/unani-clinical-assistant
I am a BUMS student. Prepare a viva plan for Zeequn Nafas with Unani concepts, modern correlation, common questions, and a model case-presentation outline.
```

```text
/unani-clinical-assistant
Draft an OPD follow-up note from this de-identified case. Do not prescribe. Highlight missing details and when to refer.
```

## For doctors and clinic teams

Before using in a real clinic, review:

- [`docs/clinical-governance.md`](docs/clinical-governance.md)
- [`docs/safety.md`](docs/safety.md)
- [`docs/privacy-deidentification.md`](docs/privacy-deidentification.md)
- [`docs/doctor-workflows.md`](docs/doctor-workflows.md)
- [`DISCLAIMER.md`](DISCLAIMER.md)

Recommended safe workflow:

1. Use only de-identified patient information.
2. Generate a draft note, handout, or checklist.
3. Have the registered practitioner review every output.
4. Verify any classical reference, drug information, contraindication, dose, or safety claim from authoritative sources.
5. Keep final clinical decisions inside the qualified clinical team’s normal process.

## Privacy reminder

Do not commit or upload real patient data. Remove names, phone numbers, addresses, emails, government IDs, hospital IDs, exact birth dates, and images/scans with identifiers.

A lightweight helper is included:

```bash
python scripts/anonymize_case.py input.txt output.txt
```

This helper is not perfect. Manual review is required.

## Development commands

```bash
python scripts/validate_skill.py skills/unani-clinical-assistant
python scripts/check_no_phi.py examples skills docs
python scripts/make_skill_zip.py
python -m pytest
```

## Release checklist

See [`docs/release-checklist.md`](docs/release-checklist.md) before tagging a release or publishing a package.

## Contributing

Contributions are welcome from BUMS students, registered Unani practitioners, medical educators, clinic teams, patient-safety reviewers, and documentation maintainers. Read [`CONTRIBUTING.md`](CONTRIBUTING.md) first.

## License

MIT License. See [`LICENSE`](LICENSE).

## Citation

If you use this project in teaching, research, or clinic documentation design, see [`CITATION.cff`](CITATION.cff).
