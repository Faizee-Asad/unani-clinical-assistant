#!/usr/bin/env python3
"""Generate a blank OPD note Markdown file from template.

This helper does not generate medical advice. It only copies a template and stamps a title.
"""
from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "skills" / "unani-clinical-assistant" / "templates" / "opd-note.md"

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", help="Output Markdown file")
    parser.add_argument("--patient-code", default="[CODE]")
    args = parser.parse_args()

    text = TEMPLATE.read_text(encoding="utf-8")
    text = text.replace("- Date:", f"- Date: {date.today().isoformat()}")
    text = text.replace("- Patient code:", f"- Patient code: {args.patient_code}")
    Path(args.output).write_text(text, encoding="utf-8")
    print(f"Created {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
