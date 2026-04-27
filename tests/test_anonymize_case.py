from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from anonymize_case import anonymize  # noqa: E402

def test_anonymize_basic_identifiers():
    text = "Patient John Smith phone 9876543210 email john@example.com DOB 01/02/1990 MRN: ABC123"
    out = anonymize(text)
    assert "John Smith" not in out
    assert "9876543210" not in out
    assert "john@example.com" not in out
    assert "01/02/1990" not in out
    assert "ABC123" not in out
