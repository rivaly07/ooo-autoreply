"""Smoke-test the generated auto-reply using only the Python standard library."""

import os
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path("/tmp/ooo-test")


def test_entry() -> None:
    env = os.environ.copy()
    env["MAKEFUN_OUTPUT_DIR"] = str(OUTPUT_DIR)
    subprocess.run([sys.executable, str(ROOT / "main.py")], env=env, check=True)

    entry_path = OUTPUT_DIR / "entry.txt"
    assert entry_path.is_file(), "entry.txt was not created"
    text = entry_path.read_bytes().decode("utf-8")
    assert 1 <= len(text) <= 159, f"invalid character count: {len(text)}"
    assert text.strip(), "entry must not be whitespace-only"


if __name__ == "__main__":
    test_entry()
    print("test_entry: PASS")
