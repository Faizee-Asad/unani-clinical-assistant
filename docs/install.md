# Installation

## Clone the repository

```bash
git clone https://github.com/your-org/unani-clinical-assistant.git
cd unani-clinical-assistant
```

## Install development dependencies

```bash
python -m pip install -e .[dev]
```

## Validate

```bash
python scripts/validate_skill.py skills/unani-clinical-assistant
python -m pytest
```

## Build the upload skill ZIP

```bash
python scripts/make_skill_zip.py
```

Upload:

```text
dist/unani-clinical-assistant-skill.zip
```

The upload ZIP contains `SKILL.md` at the package root.

## Claude Code local install

```bash
cp -R skills/unani-clinical-assistant ~/.claude/skills/
```
