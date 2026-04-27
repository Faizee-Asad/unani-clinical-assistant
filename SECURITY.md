# Security and privacy policy

## Supported versions

This project is currently pre-1.0. Security and privacy fixes should target the latest `main` branch unless a release branch is created.

## Reporting a vulnerability or safety issue

Please open a private security advisory if available on the repository, or contact the maintainers through the repository’s preferred private channel.

Report urgently if you find:

- Patient identifiers in examples, docs, tests, or issues
- Prompt content that encourages diagnosis, prescribing, unsafe procedures, or delayed emergency care
- A workflow that could expose patient data
- Fabricated references or unsafe drug/procedure claims
- A packaging or script issue that leaks local files

## Never commit real patient data

Remove:

- Names
- Phone numbers
- Addresses
- Emails
- Government IDs
- Hospital IDs
- Exact birth dates
- Photos or scans with identifiers
- Rare contextual details that could identify a person

Use the helper:

```bash
python scripts/anonymize_case.py input.txt output.txt
```

Then manually review the result. Automated de-identification is not perfect.

## Public issues and pull requests

Do not paste real patient cases into public issues or pull requests. Use synthetic or heavily de-identified examples.
