#!/usr/bin/env python3
"""Generate the student versions of the 3.7.D question sheets.

Each teacher sheet (root, "(with answers)" in the name) loses everything from
the "## ANSWERS" heading down, drops "(with answers)" from its title, and is
written to Student/ under the plain name — the same numbers, so teacher
answers grade them directly. Change a number and you must change both.

Usage:  python3 make_student_sheets.py
"""
from __future__ import annotations

import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STUDENT_DIR = BASE_DIR / "Student"


def student_version(md: str) -> str:
    md = re.sub(r"\A---.*?---\n", "", md, flags=re.S)          # frontmatter
    m = re.search(r"^##\s+ANSWERS.*$", md, flags=re.M)        # answers -> gone
    if m:
        md = md[: m.start()].rstrip() + "\n"
    md = re.sub(r"\s*\(with answers\)\s*$", "", md, flags=re.M | re.I)  # any line
    return md.lstrip("\n")


def main() -> int:
    STUDENT_DIR.mkdir(exist_ok=True)
    for src in sorted(BASE_DIR.glob("* (with answers).md")):
        dst = STUDENT_DIR / re.sub(r"\s*\(with answers\)\s*$", "", src.stem, flags=re.I)
        dst = dst.with_suffix(".md")
        dst.write_text(student_version(src.read_text(encoding="utf-8")), encoding="utf-8")
        print(f"  ✓ {dst.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
