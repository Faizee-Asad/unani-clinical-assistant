# Release checklist

Use this before publishing a GitHub release or sharing a ZIP.

## Validation

- [ ] `python scripts/validate_skill.py skills/unani-clinical-assistant`
- [ ] `python scripts/check_no_phi.py examples skills docs README.md DISCLAIMER.md`
- [ ] `python scripts/make_skill_zip.py`
- [ ] `python -m pytest`

## Safety review

- [ ] No autonomous diagnosis wording
- [ ] No autonomous prescribing wording
- [ ] No procedure instructions that replace qualified supervision
- [ ] Red-flag and urgent-care language is present where needed
- [ ] Drug monograph template requires verification
- [ ] Regimenal therapy consent template requires qualified supervision
- [ ] Patient handout template includes warning signs
- [ ] Disclaimer and safety policy are included

## Privacy review

- [ ] No real names
- [ ] No phone numbers
- [ ] No emails
- [ ] No addresses
- [ ] No exact birth dates
- [ ] No hospital IDs, MRNs, UHIDs, or government IDs
- [ ] No patient images/scans

## Packaging review

- [ ] Repository ZIP includes docs, scripts, tests, license, disclaimer, and skill source
- [ ] Skill upload ZIP exists at `dist/unani-clinical-assistant-skill.zip`
- [ ] Skill upload ZIP contains `SKILL.md` at package root
- [ ] Version and changelog updated
