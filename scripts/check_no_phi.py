#!/usr/bin/env python3
"""Scan text files for obvious public PHI/identifier patterns.

This helper is intentionally conservative and simple. It does not prove a file is de-identified.
It only catches obvious patterns that should not appear in public examples/docs.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("email address", re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b")),
    ("10 digit phone-like number", re.compile(r"(?<!\d)\d{10}(?!\d)")),
    ("hospital id / MRN / UHID", re.compile(r"\b(?:MRN|UHID|Hospital ID|Patient ID)[ \t]*[:#-][ \t]*[A-Za-z0-9-]{3,}\b", re.I)),
    ("government id label", re.compile(r"\b(?:Aadhaar|Passport|PAN|SSN|Driver'?s License)\b", re.I)),
]

TEXT_EXTENSIONS = {".md", ".txt", ".py", ".yml", ".yaml", ".toml", ".cff"}
IGNORE_DIRS = {".git", "dist", "__pycache__", ".pytest_cache", ".mypy_cache"}
ALLOWLIST = {
    "john@example.com",  # intentionally used in anonymizer unit test
    "https://github.com/your-org/unani-clinical-assistant",
    "https://github.com/security/advisories",
}


def iter_files(paths: list[Path]):
    for start in paths:
        if not start.exists():
            continue
        if start.is_file():
            yield start
            continue
        for path in start.rglob("*"):
            if any(part in IGNORE_DIRS for part in path.parts):
                continue
            if path.is_file() and path.suffix.lower() in TEXT_EXTENSIONS:
                yield path


def scan_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="ignore")
    findings: list[str] = []
    cleaned = text
    for allowed in ALLOWLIST:
        cleaned = cleaned.replace(allowed, "")
    for label, pattern in PATTERNS:
        for match in pattern.finditer(cleaned):
            line_no = cleaned.count("\n", 0, match.start()) + 1
            snippet = match.group(0)
            findings.append(f"{path}:{line_no}: possible {label}: {snippet}")
    return findings


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Scan public files for obvious PHI-like patterns.")
    parser.add_argument("paths", nargs="+", help="Files or directories to scan")
    args = parser.parse_args(argv)
    findings: list[str] = []
    for file in iter_files([Path(p) for p in args.paths]):
        findings.extend(scan_file(file))
    if findings:
        print("Potential identifier patterns found:")
        for finding in findings:
            print(f"- {finding}")
        print("Review manually. If these are synthetic test data, add a narrow allowlist entry.")
        return 1
    print("No obvious PHI-like patterns found. Manual review is still required.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
