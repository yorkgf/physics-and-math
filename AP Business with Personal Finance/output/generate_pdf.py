#!/usr/bin/env python3
"""Generate A4 PDF from Vocab Review Booklet markdown."""

import subprocess
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
MD_FILE = BASE.parent / "Vocab Review Booklet.md"
CSS_FILE = BASE / "style.css"
HTML_FILE = BASE / "booklet.html"
PDF_FILE = BASE / "Vocab Review Booklet.pdf"

# ── 1. Read markdown ──────────────────────────────────────────
md = MD_FILE.read_text(encoding="utf-8")

# ── 2. Preprocess markdown ────────────────────────────────────
# Replace \newpage with a page-break div
md = md.replace("\\newpage", "\n\n<div class='page-break'></div>\n\n")

# Remove the first H1 title + description (we'll use a cover instead)
lines = md.split("\n")
cut = 0
for i, line in enumerate(lines):
    if line.startswith("# ") and "Vocabulary Review Booklet" in line:
        # Skip title, blank line, description, blank line, ---
        cut = i
        break

# Find the first --- after the title to cut everything before Unit 1
rest = "\n".join(lines[cut:])
# Find the first # Unit marker
unit_idx = rest.find("# Unit 1:")
if unit_idx > 0:
    md_body = rest[unit_idx:]
else:
    md_body = rest

# ── 3. Convert to HTML fragment via pandoc ─────────────────────
proc = subprocess.run(
    ["pandoc", "--from=markdown", "--to=html5"],
    input=md_body,
    capture_output=True,
    text=True,
)
if proc.returncode != 0:
    print(f"Pandoc error:\n{proc.stderr}", file=sys.stderr)
    sys.exit(1)

html_body = proc.stdout

# ── 4. Read CSS ───────────────────────────────────────────────
css = CSS_FILE.read_text(encoding="utf-8")

# ── 5. Assemble full HTML document ────────────────────────────
cover_html = """
<div class="cover-page">
  <div class="cover-inner">
    <div class="cover-badge">AP Exam Review</div>
    <h1 class="cover-title">Business with<br>Personal Finance</h1>
    <p class="cover-subtitle">Vocabulary Review Booklet</p>
    <div class="cover-divider"></div>
    <div class="cover-meta">
      <strong>Units 1 &ndash; 5</strong> &middot; Complete Vocabulary Reference<br>
      Core Terms &middot; Additional Terms &middot; Trap Pairs &middot; Formulas
    </div>
  </div>
  <div class="cover-footer">
    <div class="cover-footer-line"></div>
    <div class="cover-footer-text">Study Smart &middot; Score High</div>
  </div>
</div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AP Business with Personal Finance — Vocabulary Review Booklet</title>
  <style>
{css}
  </style>
</head>
<body>
{cover_html}
{html_body}
</body>
</html>"""

# ── 6. Write HTML for debugging ───────────────────────────────
HTML_FILE.write_text(full_html, encoding="utf-8")
print(f"HTML written to {HTML_FILE}")

# ── 7. Generate PDF with WeasyPrint ──────────────────────────
result = subprocess.run(
    ["weasyprint", str(HTML_FILE), str(PDF_FILE)],
    capture_output=True,
    text=True,
)
if result.returncode != 0:
    print(f"WeasyPrint error:\n{result.stderr}", file=sys.stderr)
    sys.exit(1)

print(f"PDF generated: {PDF_FILE}")
