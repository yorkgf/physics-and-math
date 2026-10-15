#!/usr/bin/env python3
"""Render a Business Canvas assignment (Markdown) to a print-ready A4 PDF.

Pipeline: Markdown -> pandoc (gfm) -> HTML fragment -> WeasyPrint -> PDF

Setup (once — pin 3.13; this box's default 3.14 has no prebuilt Pillow wheel,
so `uv run --with weasyprint` stalls building it from source):

    uv venv --python 3.13 /tmp/pdfenv
    uv pip install --python /tmp/pdfenv/bin/python weasyprint

Usage:
    /tmp/pdfenv/bin/python make_pdf.py "Business Canvas Project - Assignment 1C (Task 7).md"
    /tmp/pdfenv/bin/python make_pdf.py     # every *.md here lacking a .pdf

Notes:
    - Markdown task-list boxes are converted to the literal glyph U+25A1 (□).
      Do NOT use U+2610 (☐): it renders as tofu in the fonts available here.
    - The source .md is never modified; all rewriting happens in memory.
"""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# U+25A1 WHITE SQUARE — renders in DejaVu Sans / Liberation Sans.
# U+2610 BALLOT BOX does not.
CHECKBOX = "□"

RUNNING_HEADER = "AP Business with Personal Finance — Business Canvas Project"

CSS = """
@page {
  size: A4;
  margin: 18mm 17mm 18mm 17mm;
  @bottom-center {
    content: counter(page);
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 9pt;
    color: #94a3b8;
  }
  @top-right {
    content: "AP Business with Personal Finance \\2014 Business Canvas Project";
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8pt;
    color: #b0b8c4;
  }
}

body {
  font-family: 'DejaVu Sans', sans-serif;
  font-size: 10pt;
  line-height: 1.5;
  color: #1a1a1a;
}

h1 {
  font-size: 17pt;
  color: #1a3557;
  margin: 0 0 3mm 0;
  padding-bottom: 2mm;
  border-bottom: 2px solid #1a3557;
  line-height: 1.25;
  page-break-after: avoid;
}

h2 {
  font-size: 12.5pt;
  color: #1a3557;
  margin: 7mm 0 2mm 0;
  page-break-after: avoid;
}

h3 {
  font-size: 11pt;
  color: #2c5282;
  margin: 5mm 0 1.5mm 0;
  page-break-after: avoid;
}

p { margin: 0 0 3mm 0; orphans: 3; widows: 3; }

blockquote {
  background: #f0f5fb;
  border-left: 3px solid #1a3557;
  margin: 3mm 0 4mm 0;
  padding: 2mm 4mm;
  color: #1a3557;
  font-size: 9.5pt;
  border-radius: 0 3px 3px 0;
}
blockquote p { margin: 0 0 1.5mm 0; }
blockquote p:last-child { margin-bottom: 0; }

hr { border: none; border-top: 1px solid #dde3ea; margin: 5mm 0; }

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 9pt;
  margin: 3mm 0 4mm 0;
}
thead { display: table-header-group; }
tr { page-break-inside: avoid; }
thead tr { background: #1a3557; color: #fff; }
thead th { padding: 2mm 3mm; text-align: left; font-size: 8.5pt; }
tbody tr:nth-child(odd)  { background: #f7f9fc; }
tbody tr:nth-child(even) { background: #fff; }
tbody td {
  padding: 2mm 3mm;
  border-bottom: 1px solid #e8edf3;
  vertical-align: top;
}
tbody td strong { color: #1a3557; }

ul, ol { margin: 1mm 0 3mm 5mm; padding-left: 4mm; }
li { margin-bottom: 1mm; }

strong { font-weight: bold; }
em { font-style: italic; color: #444; }

code {
  font-family: 'DejaVu Sans Mono', monospace;
  font-size: 9pt;
  background: #f4f4f4;
  padding: 0 1pt;
}
"""

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head><meta charset="utf-8"><title>{title}</title><style>{css}</style></head>
<body>
{body}
</body>
</html>
"""

CJK_RE = re.compile(r"[㐀-䶿一-鿿豈-﫿]")


def preprocess(md_text: str) -> str:
    """Turn task-list checkboxes into a literal square the local fonts can draw."""
    md_text = re.sub(r"(?m)^(\s*)-\s\[ \]\s", rf"\1- {CHECKBOX} ", md_text)
    md_text = re.sub(r"(?m)^(\s*)-\s\[[xX]\]\s", rf"\1- {CHECKBOX} ", md_text)
    return md_text


def md_to_html_fragment(md_text: str) -> str:
    # hard_line_breaks matches Obsidian's default: a single newline is a <br>.
    # Without it the "Due / Team size / Submission" header collapses onto one line.
    proc = subprocess.run(
        ["pandoc", "--from=gfm+hard_line_breaks", "--to=html5"],
        input=md_text,
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"pandoc failed:\n{proc.stderr}")
    return proc.stdout


def render(md_path: Path) -> Path:
    from weasyprint import HTML

    md_text = md_path.read_text(encoding="utf-8")

    if CJK_RE.search(md_text):
        print(
            f"  ! {md_path.name} contains CJK characters but no CJK font is "
            "installed here — those glyphs will render as boxes."
        )

    fragment = md_to_html_fragment(preprocess(md_text))
    title_match = re.search(r"(?m)^#\s+(.+)$", md_text)
    title = title_match.group(1).strip() if title_match else md_path.stem

    html = HTML_TEMPLATE.format(title=title, css=CSS, body=fragment)

    out = md_path.with_suffix(".pdf")
    HTML(string=html, base_url=str(BASE_DIR)).write_pdf(str(out))
    print(f"  ✓ {out.name}  ({out.stat().st_size / 1024:.0f} KB)")
    return out


def default_targets() -> list[Path]:
    return [
        p
        for p in sorted(BASE_DIR.glob("Business Canvas Project - *.md"))
        if not p.with_suffix(".pdf").exists() and "SUPERSEDED" not in p.name
    ]


def main(argv: list[str]) -> int:
    if argv:
        targets = [Path(a) if Path(a).is_absolute() else BASE_DIR / a for a in argv]
    else:
        targets = default_targets()

    if not targets:
        print("Nothing to render — every assignment already has a PDF.")
        return 0

    for target in targets:
        if not target.exists():
            print(f"  ! missing: {target}")
            return 1
        render(target)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
