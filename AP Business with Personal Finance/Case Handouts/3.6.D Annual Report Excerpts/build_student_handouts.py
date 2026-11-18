#!/usr/bin/env python3
"""Build four self-contained student handouts: the real income statements
(the material) plus the comparison questions, with no answers.

Each handout is one PDF per industry pair:
  page 1..n   the statements, exactly as filed (source line on every page)
  last pages  the questions, with answer space and a total line

Reuses the EDGAR parser from fetch_income_statements.py and the student
question sheets in Student/ (answers already removed).

Usage:  python3 build_student_handouts.py
"""
from __future__ import annotations

import re
import subprocess
import sys
from html import escape
from pathlib import Path

from fetch_income_statements import (
    COMPANIES, FILE_PREFIX, income_statement_rfile, latest_10k,
    merge_abstract_triples, parse_rfile, is_section, is_total, fy_label,
)

BASE_DIR = Path(__file__).resolve().parent
STUDENT_DIR = BASE_DIR / "Student"

PAIRS = [
    ("Restaurant Pair (CMG vs MCD)", ["CMG", "MCD"]),
    ("Airline Pair (DAL vs UAL)", ["DAL", "UAL"]),
    ("Retail Pair (WMT vs TGT)", ["WMT", "TGT"]),
    ("Bank Pair (JPM vs BAC)", ["JPM", "BAC"]),
]

# Chipotle already ships in this folder as its own PDF (built from the htm by
# hand); the handout builder only needs its metadata to render the same
# statement inline. Kept out of fetch_income_statements.COMPANIES so a full
# refresh run never overwrites that file.
EXTRA = {
    "CMG": (1058090, "Chipotle Mexican Grill, Inc.", "Consolidated Statements of Income"),
}
ALL = {**COMPANIES, **EXTRA}

CSS = """
@page { size: A4; margin: 15mm 14mm 16mm 14mm;
  @bottom-center { content: counter(page); font-family: 'DejaVu Sans', sans-serif;
                   font-size: 8pt; color: #94a3b8; } }
body { font-family: 'DejaVu Sans', sans-serif; font-size: 9pt; color: #1a1a1a; line-height: 1.45; }
.kicker { font-size: 7.5pt; letter-spacing: 1.5px; color: #64748b; margin-bottom: 3mm; }
h1 { font-size: 13pt; color: #1a3557; margin: 0 0 2mm 0; }
.nameline { font-size: 9pt; margin: 2mm 0 3mm 0; }
.stmt { page-break-inside: avoid; margin-bottom: 6mm; }
.stmt h2 { font-size: 10.5pt; color: #1a3557; margin: 0 0 1mm 0; }
.meta { font-size: 7.5pt; color: #444; }
.src { font-size: 6.5pt; color: #64748b; word-break: break-all; margin-bottom: 2mm; }
table { width: 100%; border-collapse: collapse; margin-bottom: 2mm; }
caption { text-align: left; font-size: 7.5pt; color: #64748b; padding-bottom: 1mm; }
th { background: #1a3557; color: #fff; padding: 1.2mm 2mm; font-size: 7pt; text-align: right; }
th.lbl { text-align: left; }
td { padding: 0.8mm 2mm; border-bottom: 0.5px solid #e8edf3; font-size: 8pt; }
td.lbl { text-align: left; }
td.num { text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }
tr.tot td { font-weight: bold; background: #f0f5fb; }
tr.sec td { font-weight: bold; color: #1a3557; border-top: 1px solid #cbd5e1; }
tr.det td.lbl { padding-left: 5mm; color: #333; }
.q h2 { font-size: 11.5pt; color: #1a3557; border-bottom: 2px solid #1a3557;
        padding-bottom: 1.5mm; margin: 0 0 3mm 0; }
.q h3 { font-size: 9.5pt; color: #1a3557; margin: 4mm 0 1.5mm 0; }
.q p { margin: 0 0 2mm 0; }
.q table { font-size: 8pt; }
.q table th { font-size: 7pt; }
.q ol, .q ul { margin: 1mm 0 2mm 5mm; padding-left: 4mm; }
.q li { margin-bottom: 1mm; }
.total { margin-top: 5mm; font-size: 9.5pt; font-weight: bold; }
.pagebreak { page-break-before: always; }
.footnote { font-size: 7pt; color: #64748b; margin-top: 4mm; }
"""


def statement_html(ticker: str) -> str:
    cik, name, stmt_title = ALL[ticker]
    meta = latest_10k(cik)
    accn = meta["acc"].replace("-", "")
    rfile, _ = income_statement_rfile(cik, accn)
    title, header, rows = parse_rfile(cik, accn, rfile)
    rows = merge_abstract_triples(rows)
    ncol = max(len(r) for r in rows)
    units = ""
    m = re.search(r"\$ in (Millions|Thousands|Billions)", title)
    if m:
        units = f" · $ in {m.group(1).lower()}"

    body = []
    for r in rows:
        label = r[0] if r else ""
        vals = r[1:]
        cls = "sec" if is_section(r) else ("tot" if is_total(label) else "det")
        tds = "".join(
            f'<td class="num">{escape(v)}</td>' for v in (vals + [""] * (ncol - len(vals)))
        )
        body.append(f'<tr class="{cls}"><td class="lbl">{escape(label)}</td>{tds}</tr>')

    return f"""<div class="stmt">
<h2>{escape(name)} ({ticker}) — {escape(stmt_title)}</h2>
<div class="meta">Form 10-K · fiscal year {escape(fy_label(header).replace('FY', ''))} · filed {escape(meta['filed'])} · Accession No. {escape(meta['acc'])}</div>
<div class="src">Source: https://www.sec.gov/Archives/edgar/data/{meta['cik']}/{accn}/{meta['doc']}</div>
<table>
<caption>{escape(stmt_title)}{escape(units)}</caption>
<tr><th class="lbl">{escape(header[0]) if header else ''}</th>{''.join(f'<th>{escape(h)}</th>' for h in header[1:ncol])}</tr>
{''.join(body)}
</table>
</div>"""


def questions_html(pair_name: str) -> str:
    md = (STUDENT_DIR / f"{pair_name} - Comparison Question Sheet.md").read_text(encoding="utf-8")
    # strip frontmatter
    md = re.sub(r"\A---.*?---\n", "", md, flags=re.S)
    # the handout supplies its own title and name line — drop the md's copies
    md = re.sub(r"\A#[^\n]+\n", "", md)
    md = re.sub(r"\*\*Name:\*\*[^\n]*\n", "", md, count=1)
    # the statements are inline now — replace the "Pairs with" PDF reference
    md = re.sub(
        r"\*\*Pairs with:\*\* `[^`]+`(?: and `[^`]+`)?\.",
        "**Source:** the statements above, exactly as filed.",
        md,
    )
    proc = subprocess.run(
        ["pandoc", "--from=gfm+hard_line_breaks", "--to=html5"],
        input=md, capture_output=True, text=True,
    )
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr)
    return f'<div class="q">{proc.stdout}</div>'


def build(pair_name: str, tickers: list[str]) -> Path:
    stmts = "".join(statement_html(t) for t in tickers)
    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="kicker">STUDENT HANDOUT — AP Business with Personal Finance · Topic 3.6</div>
<h1>{escape(pair_name)} — read the statements, answer the questions</h1>
<div class="nameline"><b>Name:</b> ____________________________　<b>Class:</b> ________　<b>Date:</b> ____________</div>
{stmts}
<div class="pagebreak"></div>
{questions_html(pair_name)}
<div class="footnote">All figures are as reported in the companies' latest annual filings (SEC EDGAR). No answers appear in this handout.</div>
</body></html>"""
    from weasyprint import HTML

    out = BASE_DIR / f"{pair_name} - Student Handout.pdf"
    HTML(string=html).write_pdf(str(out))
    return out


def main() -> int:
    for pair_name, tickers in PAIRS:
        out = build(pair_name, tickers)
        print(f"  ✓ {out.name}  ({out.stat().st_size // 1024} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
