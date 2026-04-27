# Privacy and de-identification guide

Do not put real patient identifiers into public repositories, public issues, pull requests, examples, prompts, demos, or teaching files.

## Remove direct identifiers

Remove:

- Name
- Phone number
- Email address
- Home address
- Exact date of birth
- Government ID
- Hospital ID / MRN / UHID
- Photo, scan, audio, video, or image metadata
- Names of relatives or employers when identifying

## Reduce indirect identifiers

Even after removing direct identifiers, rare combinations may identify a person. Generalize details such as:

- Exact age to age range
- Exact date to month/year or relative duration
- Specific village/workplace/school to broad location type
- Rare occupation to broad category
- Rare disease context to only the necessary clinical facts

## Recommended public example format

Use synthetic examples like:

```text
Adult patient, age range 30–40, presents with chronic constipation for several months. No name, phone, address, hospital ID, or exact dates included.
```

## Helper scripts

Run:

```bash
python scripts/anonymize_case.py input.txt output.txt
python scripts/check_no_phi.py examples skills docs
```

The scripts catch obvious patterns only. Manual review is required.
