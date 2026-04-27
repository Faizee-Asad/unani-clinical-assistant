#!/usr/bin/env python3
"""Validate a Claude Skill directory and required safety files."""
from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]{1,64}$")
RESERVED = {"anthropic", "claude"}


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with YAML frontmatter")
    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError("SKILL.md frontmatter must be closed with ---")
    fm = parts[1]
    data: dict[str, str] = {}
    for raw_line in fm.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            raise ValueError(f"Invalid frontmatter line: {raw_line!r}")
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return data


def validate(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.exists():
        return [f"Missing {skill_file}"]

    try:
        text = skill_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = fm.get("name", "")
    description = fm.get("description", "")

    if not name:
        errors.append("Missing frontmatter field: name")
    elif not NAME_RE.fullmatch(name):
        errors.append("Skill name must use only lowercase letters, numbers, and hyphens, max 64 chars")
    elif any(part in RESERVED for part in name.split("-")):
        errors.append("Skill name must not contain reserved words: anthropic or claude")

    if not description:
        errors.append("Missing frontmatter field: description")
    elif len(description) > 1024:
        errors.append("Description must be <= 1024 characters")

    required_paths = [
        "safety-policy.md",
        "reference/red-flags.md",
        "reference/unani-terminology.md",
        "reference/curriculum-map.md",
        "reference/evidence-and-references.md",
        "templates/case-sheet.md",
        "templates/opd-note.md",
        "templates/follow-up-note.md",
        "templates/patient-handout.md",
        "templates/referral-letter.md",
        "templates/consent-form-regimenal-therapy.md",
        "templates/drug-monograph.md",
        "templates/viva-prep.md",
        "templates/research-question.md",
    ]
    for rel in required_paths:
        path = skill_dir / rel
        if not path.exists():
            errors.append(f"Missing referenced file: {rel}")
        elif path.stat().st_size == 0:
            errors.append(f"Referenced file is empty: {rel}")

    must_include = ["diagnose", "prescribe", "emergency", "red flag", "qualified"]
    safety_text = (skill_dir / "safety-policy.md").read_text(encoding="utf-8", errors="ignore").lower() if (skill_dir / "safety-policy.md").exists() else ""
    for term in must_include:
        if term not in safety_text:
            errors.append(f"Safety policy should mention: {term}")

    return errors


def validate_zip(zip_path: Path) -> list[str]:
    errors: list[str] = []
    if not zip_path.exists():
        return [f"Missing zip: {zip_path}"]
    with zipfile.ZipFile(zip_path) as zf:
        names = set(zf.namelist())
        if "SKILL.md" not in names:
            errors.append("Skill upload zip must contain SKILL.md at root")
        if any(name.startswith("dist/") for name in names):
            errors.append("Skill upload zip should not include nested dist directory")
    return errors


def main() -> int:
    skill_dir = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("skills/unani-clinical-assistant")
    errors = validate(skill_dir)
    if errors:
        print("Skill validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Skill validation passed: {skill_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
