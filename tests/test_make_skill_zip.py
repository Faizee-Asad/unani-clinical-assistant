from pathlib import Path
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]


def test_make_skill_zip_contains_skill_at_root():
    subprocess.run([sys.executable, "scripts/make_skill_zip.py"], cwd=ROOT, check=True)
    out = ROOT / "dist" / "unani-clinical-assistant-skill.zip"
    assert out.exists()
    with zipfile.ZipFile(out) as zf:
        names = set(zf.namelist())
    assert "SKILL.md" in names
    assert "safety-policy.md" in names
    assert "templates/opd-note.md" in names
