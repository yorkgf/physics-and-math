#!/usr/bin/env python3
"""Build clean, print-ready PDFs from the 3.7.D question sheets.

Two products, one script:

  student/  one PDF per sheet, questions only — no answers, no frontmatter,
            no teacher notes. Ready to hand out.
  teacher/  same question pages, then a hard page break and the ANSWERS
            section in a visually distinct amber style, so a teacher can
            print just the front pages for class.

Inputs
  Student/*.md                                  -> Student PDF/
  *.md with "(with answers)" in the name        -> Teacher PDF/

Usage
  python3 build_question_sheets.py                # both products
  python3 build_question_sheets.py --mode student
  python3 build_question_sheets.py --mode teacher

Needs pandoc on PATH. Uses the system python3, whose weasyprint works;
page counts are reported when pypdf is importable and skipped otherwise.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from html import escape
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
STUDENT_DIR = BASE_DIR / "Student"
TEACHER_DIR = BASE_DIR                      # the "(with answers)" md files live here
DEFAULT_OUT = {"student": BASE_DIR / "Student PDF", "teacher": BASE_DIR / "Teacher PDF"}

import shutil
WEASY_PYTHON = shutil.which("python3") or "python3"
WEASY_PACKAGES = None

TOTAL_SENTINEL = "\x00TOTAL\x00"
ANSWERS_SENTINEL = "\x00ANSWERS\x00"

CSS = """
@page {
  size: A4; margin: 13mm 15mm 14mm 15mm;
  @bottom-center { content: counter(page) " / " counter(pages);
                   font-family: 'Liberation Sans', sans-serif; font-size: 7.5pt; color: #94a3b8; }
}
* { box-sizing: border-box; }
body { font-family: 'Liberation Sans', 'DejaVu Sans', sans-serif; font-size: 9pt;
       color: #111827; line-height: 1.38; }
h1 { font-size: 13.5pt; color: #0f2c4d; margin: 0 0 1mm 0; line-height: 1.2; }
.rule { border-bottom: 1.4pt solid #0f2c4d; margin: 0 0 2.5mm 0; }
.nameline { font-size: 9pt; margin: 0 0 2mm 0; }
.nameline b { color: #0f2c4d; }
.meta { font-size: 7.8pt; color: #475569; margin: 0 0 0.7mm 0; line-height: 1.35; }
h2 { font-size: 10pt; color: #0f2c4d; margin: 3.2mm 0 1.5mm 0;
     padding-bottom: 0.7mm; border-bottom: 0.6pt solid #cbd5e1;
     page-break-after: avoid; }
h3 { font-size: 9pt; color: #0f2c4d; margin: 2.2mm 0 1mm 0; page-break-after: avoid; }
p { margin: 0 0 1.5mm 0; orphans: 2; widows: 2; }
table { width: 100%; border-collapse: collapse; margin: 1mm 0 2mm 0;
        font-size: 8pt; page-break-inside: avoid; }
th { background: #eef2f7; color: #0f2c4d; font-size: 7.5pt; font-weight: bold;
     text-align: left; padding: 1mm 1.5mm; border: 0.5pt solid #cbd5e1; }
td { padding: 1mm 1.5mm; border: 0.5pt solid #dde3ea; vertical-align: top; }
td:empty { height: 5.5mm; }
ol, ul { margin: 0.5mm 0 1.5mm 4.5mm; padding: 0; }
li { margin-bottom: 0.8mm; }
hr { border: none; border-top: 0.5pt solid #e2e8f0; margin: 2.5mm 0; }
strong { color: #0f2c4d; }
code { font-family: 'DejaVu Sans Mono', monospace; font-size: 7.5pt; color: #334155; }
.ansline { display: block; border-bottom: 0.75pt solid #64748b; height: 5.5mm;
           margin: 0.3mm 0 2mm 0; }
.total { margin-top: 3mm; padding: 1.5mm 3mm; border: 0.8pt solid #0f2c4d;
         font-size: 9.5pt; font-weight: bold; color: #0f2c4d; display: inline-block; }
.gap { display: inline-block; width: 16mm; border-bottom: 0.6pt solid #0f2c4d; }

/* ---- teacher-only ---- */
.answers { page-break-before: always; }
.answers .banner { background: #7c2d12; color: #fff; font-size: 9pt; font-weight: bold;
                   padding: 1.5mm 2.5mm; margin: 0 0 3mm 0; letter-spacing: 0.4px; }
.answers h3 { color: #7c2d12; border-bottom: 0.6pt solid #e7c9b5;
              padding-bottom: 0.6mm; margin: 3mm 0 1.5mm 0; }
.answers strong { color: #7c2d12; }
.answers table th { background: #fdf1e7; color: #7c2d12; border-color: #e7c9b5; }
.answers table td { border-color: #f0e0d4; }
.answers hr { border-top-color: #f0e0d4; }
"""


# ---------------------------------------------------------------- markdown -> parts
def split_sheet(md: str, name: str = "") -> tuple[str, str, str, str]:
    """Return (title, use_with, meta, body_md) from a question sheet."""
    md = re.sub(r"\A---.*?---\n", "", md, flags=re.S)          # frontmatter
    md = md.lstrip("\n")
    # some teacher sheets carry a teacher-only note above the H1 - drop it
    m = re.search(r"^#[ \t]+(.+?)[ \t]*$", md, flags=re.M)      # H1 -> title
    if not m:
        raise RuntimeError(f"no H1 title found in {name}")
    if md[:m.start()].strip():
        print(f"  - {name}: dropped a teacher note above the title", file=sys.stderr)
    title = re.sub(r"\s*\(with answers\)\s*$", "", m.group(1).strip(), flags=re.I)
    md = md[m.end():]
    md = re.sub(r"\*\*Name:\*\*[^\n]*\n", "", md, count=1)      # name line is in the template

    # the "Pairs with … / Time … Marks …" block is one or two lines up to a blank
    use_with, meta = "", ""
    m = re.search(r"\*\*Pairs with:\*\*.*?(?=\n[ \t]*\n|\Z)", md, flags=re.S)
    if m:
        block = m.group(0)
        md = md[:m.start()] + md[m.end():]
        parts = re.split(r"\*\*Time:\*\*", block, maxsplit=1)
        use_with = re.sub(r"\A\*\*Pairs with:\*\*", "", parts[0])
        if len(parts) == 2:
            meta = parts[1]
    else:
        m = re.search(r"\*\*Time:\*\*.*?(?=\n[ \t]*\n|\Z)", md, flags=re.S)
        if m:
            meta = m.group(0)
            md = md[:m.start()] + md[m.end():]

    def tidy(s: str) -> str:
        s = s.replace("`", "")
        s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
        s = re.sub(r"\s*\n\s*", " ", s)
        s = re.sub(r"[ \t]*[　]\s*", " · ", s)      # full-width spaces -> separators
        return re.sub(r"[ \t]{2,}", " ", s).strip(" .·")

    return title, tidy(use_with), tidy(meta), md.strip() + "\n"


def fix_tables(md: str) -> str:
    """Pandoc's pipe tables need a blank line above them. The ANSWERS blocks
    start a table right after a bold label (**A1.**), so insert one."""
    out: list[str] = []
    for line in md.split("\n"):
        if (line.lstrip().startswith("|") and out and out[-1].strip()
                and not out[-1].lstrip().startswith("|")):
            out.append("")
        out.append(line)
    return "\n".join(out)


def markdown_to_html(md: str) -> str:
    md = fix_tables(md)
    proc = subprocess.run(
        ["pandoc", "--from=gfm+hard_line_breaks", "--to=html5"],
        input=md, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr)
    return proc.stdout


def polish(html: str) -> str:
    # boxed total first, with a sentinel the underscore rule cannot eat
    html = re.sub(
        r"<p><strong>Total:</strong>\s*_*\s*/\s*(\d+)</p>",
        r'<div class="total">Total: ' + TOTAL_SENTINEL + r' / \1</div>',
        html,
    )
    # real ruled writing lines instead of underscore runs
    html = re.sub(r"_{8,}", '<span class="ansline"></span>', html)
    html = html.replace(TOTAL_SENTINEL, '<span class="gap"></span>')
    # a lone rule at the very end is noise
    html = re.sub(r"(?:<hr\s*/?>\\s*)+$", "", html)
    return html


# ---------------------------------------------------------------- pdf
def render(py: str, html_path: Path, pdf_path: Path) -> None:
    code = (
        "from weasyprint import HTML;"
        f"HTML(filename={str(html_path)!r}).write_pdf({str(pdf_path)!r})"
    )
    proc = subprocess.run([py, "-c", code], capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr or proc.stdout)


def page_count(pdf_path: Path) -> int:
    try:
        from pypdf import PdfReader
    except ImportError:
        return 0
    return len(PdfReader(str(pdf_path)).pages)


def build(md_path: Path, out_dir: Path, mode: str, py: str,
          pdf_name: str | None = None) -> tuple[Path, int]:
    title, use_with, meta, body = split_sheet(md_path.read_text(encoding="utf-8"), md_path.name)

    answers_html = ""
    if mode == "teacher":
        # everything from the "## ANSWERS" heading down goes behind a page break
        m = re.search(r"^##\s+ANSWERS.*$", body, flags=re.M)
        if m:
            answers_md = body[m.end():]
            body = body[:m.start()]
            answers_html = (
                '<div class="answers">'
                '<div class="banner">TEACHER COPY — ANSWERS BELOW. '
                'Print the preceding pages only for the class.</div>'
                + markdown_to_html(answers_md)
                + "</div>"
            )
        else:
            print(f"  ! no ANSWERS section in {md_path.name}", file=sys.stderr)

    doc = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><title>{escape(title)}</title>
<style>{CSS}</style></head><body>
<h1>{escape(title)}</h1>
<div class="rule"></div>
<div class="nameline"><b>Name:</b> ______________________________　<b>Class:</b> __________　<b>Date:</b> ____________</div>
{''.join(f'<div class="meta">{escape(b)}</div>' for b in (use_with, meta) if b)}
{polish(markdown_to_html(body))}
{answers_html}
</body></html>"""

    out_dir.mkdir(parents=True, exist_ok=True)
    if pdf_name is None:
        pdf_name = re.sub(r"\s*\(with answers\)\s*$", "", md_path.stem, flags=re.I) + ".pdf"
    pdf = out_dir / pdf_name
    tmp = out_dir / f".{pdf.stem}.html"
    tmp.write_text(doc, encoding="utf-8")
    try:
        render(py, tmp, pdf)
    finally:
        tmp.unlink(missing_ok=True)

    return pdf, page_count(pdf)


# ---------------------------------------------------------------- cli
def canonical(stem: str) -> str:
    """Fold 'Income Statement Question Sheet' and 'Income Statement - Question
    Sheet' onto one key so the student and teacher folders line up 1:1."""
    s = re.sub(r"\s*Question\s+Sheet\s*$", "", stem, flags=re.I)
    s = re.sub(r"[\s\-]+", " ", s).strip().lower()
    return s


def output_name(md_path: Path, mode: str, student_stems: dict[str, str]) -> str:
    stem = re.sub(r"\s*\(with answers\)\s*$", "", md_path.stem, flags=re.I)
    if mode == "teacher":
        stem = student_stems.get(canonical(stem), stem)
    return f"{stem}.pdf"


def sources(mode: str) -> list[Path]:
    if mode == "student":
        return sorted(STUDENT_DIR.glob("*.md"))
    return sorted(TEACHER_DIR.glob("* (with answers).md"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["student", "teacher", "both"], default="both")
    ap.add_argument("--out", default=None, help="override output directory")
    ap.add_argument("--python", default=WEASY_PYTHON)
    args = ap.parse_args()

    modes = ["student", "teacher"] if args.mode == "both" else [args.mode]
    student_stems = {canonical(p.stem): p.stem for p in sources("student")}
    for mode in modes:
        out_dir = Path(args.out) if args.out else DEFAULT_OUT[mode]
        sheets = sources(mode)
        if not sheets:
            print(f"!! no sheets for mode={mode}", file=sys.stderr)
            return 1
        print(f"\n[{mode}] {len(sheets)} sheets -> {out_dir}")
        for md_path in sheets:
            pdf, pages = build(md_path, out_dir, mode, args.python,
                               output_name(md_path, mode, student_stems))
            print(f"  ✓ {pdf.name}  ({pdf.stat().st_size // 1024} KB, {pages}p)")
    print("\nDone.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
