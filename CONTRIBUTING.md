# Contributing

Contributions are welcome from BUMS students, registered Unani practitioners, medical educators, clinic teams, researchers, privacy reviewers, and patient-safety reviewers.

## Safety-first contribution rules

Do **not** add:

- Unsupported cure claims
- Autonomous diagnosis instructions
- Autonomous prescribing instructions
- Patient-specific doses without verification requirements
- Emergency-management guidance that replaces urgent medical care
- Procedural instructions that could cause harm without supervision
- Fabricated classical references, citations, page numbers, trial results, or safety data
- Real or potentially identifiable patient data

## Good contributions

- Better red-flag and referral checklists
- Better patient handout templates
- More BUMS viva/exam examples
- Hindi/Urdu/plain-language patient education examples
- Safer documentation workflows
- Drug monograph verification checklists
- De-identification improvements
- More tests and validation rules
- Clinical governance improvements

## Pull request checklist

Before opening a pull request:

- [ ] I removed patient identifiers.
- [ ] I avoided final diagnosis/prescribing language.
- [ ] I marked uncertain evidence clearly.
- [ ] I did not invent references.
- [ ] I added or updated tests when changing scripts or validation.
- [ ] I ran `python -m pytest`.
- [ ] I ran `python scripts/validate_skill.py skills/unani-clinical-assistant`.
- [ ] I ran `python scripts/check_no_phi.py examples skills docs`.

## Clinical content review

Clinical additions should be reviewed by a qualified practitioner or educator before release. If a contribution includes drugs, procedures, contraindications, pregnancy/lactation, pediatrics, geriatrics, emergencies, or serious illness, label the pull request as `clinical-safety-review-needed`.
