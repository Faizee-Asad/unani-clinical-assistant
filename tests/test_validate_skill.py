from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_skill import validate  # noqa: E402


def test_skill_validates():
    assert validate(ROOT / "skills" / "unani-clinical-assistant") == []
