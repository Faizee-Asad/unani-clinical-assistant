from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_no_phi import scan_file  # noqa: E402


def test_scan_file_detects_email(tmp_path):
    sample = tmp_path / "sample.md"
    sample.write_text("Patient email private.patient@example.org", encoding="utf-8")
    findings = scan_file(sample)
    assert findings


def test_scan_file_allows_normal_markdown(tmp_path):
    sample = tmp_path / "sample.md"
    sample.write_text("Adult patient age range 30-40. No identifiers.", encoding="utf-8")
    findings = scan_file(sample)
    assert findings == []
