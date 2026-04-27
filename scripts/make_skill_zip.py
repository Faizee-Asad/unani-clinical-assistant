#!/usr/bin/env python3
"""Build a Claude.ai upload zip with SKILL.md at the package root."""
from __future__ import annotations

import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = ROOT / "skills" / "unani-clinical-assistant"
DIST_DIR = ROOT / "dist"
OUT = DIST_DIR / "unani-clinical-assistant-skill.zip"

def main() -> int:
    DIST_DIR.mkdir(exist_ok=True)
    if OUT.exists():
        OUT.unlink()
    with zipfile.ZipFile(OUT, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in sorted(SKILL_DIR.rglob("*")):
            if path.is_file():
                zf.write(path, path.relative_to(SKILL_DIR))
    print(f"Created {OUT}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
