#!/usr/bin/env python3
"""Simple text anonymizer for demo case files.

This is a lightweight helper, not a perfect de-identification tool. Review output manually.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

PATTERNS = [
    (re.compile(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b"), "[NAME]"),
    (re.compile(r"\b\d{10}\b"), "[PHONE]"),
    (re.compile(r"\b[\w.+-]+@[\w-]+(?:\.[\w-]+)+\b"), "[EMAIL]"),
    (re.compile(r"\b\d{1,2}[/.-]\d{1,2}[/.-]\d{2,4}\b"), "[DATE]"),
    (re.compile(r"\b(?:MRN|UHID|ID)[:\s-]*[A-Za-z0-9-]+\b", re.I), "[PATIENT_ID]"),
]

def anonymize(text: str) -> str:
    result = text
    for pattern, repl in PATTERNS:
        result = pattern.sub(repl, result)
    return result

def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/anonymize_case.py input.txt output.txt")
        return 2
    src, dst = Path(sys.argv[1]), Path(sys.argv[2])
    dst.write_text(anonymize(src.read_text(encoding="utf-8")), encoding="utf-8")
    print(f"Wrote anonymized file to {dst}")
    print("Reminder: review manually before sharing or committing.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
