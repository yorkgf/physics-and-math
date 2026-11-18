#!/usr/bin/env python3
"""Extract the income statement from each company's latest 10-K on SEC EDGAR
and render a clean one-page PDF in the 3.6.D package's house style.

Pipeline: submissions API → latest 10-K accession → FilingSummary.xml →
the R-file for the income statement → parsed table → WeasyPrint PDF.

Usage:  python3 fetch_income_statements.py            # all companies
        python3 fetch_income_statements.py MCD UAL    # only these tickers
"""
from __future__ import annotations

import json
import re
import sys
import time
import urllib.request
from html import escape, unescape
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

UA = {"User-Agent": "Research york@ghedu.com"}

# ticker -> (CIK, display name, clean statement title for the file name).
COMPANIES = {
    "MCD": (63908, "McDonald's Corporation", "Consolidated Statement of Income"),
    "DAL": (27904, "Delta Air Lines, Inc.", "Consolidated Statements of Operations"),
    "UAL": (100517, "United Airlines Holdings, Inc.", "Consolidated Statements of Operations"),
    "WMT": (104169, "Walmart Inc.", "Consolidated Statements of Income"),
    "TGT": (27419, "Target Corporation", "Consolidated Statements of Operations"),
    "JPM": (19617, "JPMorgan Chase & Co.", "Consolidated Statements of Income"),
    "BAC": (70858, "Bank of America Corporation", "Consolidated Statement of Income"),
}

# File-name prefix per ticker (the filing's ShortName is inconsistent).
FILE_PREFIX = {
    "MCD": "McDonalds", "DAL": "Delta", "UAL": "United", "WMT": "Walmart",
    "TGT": "Target", "JPM": "JPMorgan", "BAC": "Bank of America",
}

# Which comparison group each statement feeds (for the README index).
GROUPS = {
    "MCD": "Restaurants",
    "DAL": "Airlines",
    "UAL": "Airlines",
    "WMT": "Big-box retail",
    "TGT": "Big-box retail",
    "JPM": "Banks",
    "BAC": "Banks",
}


def get(url: str, binary: bool = False):
    req = urllib.request.Request(url, headers=UA)
    data = urllib.request.urlopen(req, timeout=60).read()
    return data if binary else data.decode("utf-8", "ignore")


def latest_10k(cik: int) -> dict:
    d = json.loads(get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json"))
    r = d["filings"]["recent"]
    for form, acc, date, doc in zip(
        r["form"], r["accessionNumber"], r["filingDate"], r["primaryDocument"]
    ):
        if form == "10-K":
            return {
                "acc": acc,
                "filed": date,
                "doc": doc,
                "name": d["name"].title(),
                "cik": d["cik"],
            }
    raise SystemExit(f"no 10-K found for CIK {cik}")


def income_statement_rfile(cik: int, accn: str) -> tuple[str, str]:
    """Find the R-file for the income statement.

    Filings name it inconsistently: "Consolidated Statement of Income",
    "Consolidated Statements of Operations", "STATEMENTS OF CONSOLIDATED
    OPERATIONS (UAH)", "CONSOLIDATED STATEMENTS OF INCOME AND COMPREHENSIVE
    INCOME" — sometimes with a parenthetical suffix. Normalise, then match the
    income statement itself while rejecting a standalone "Statements of
    Comprehensive Income", parentheticals, tables and details.
    """
    xml = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/FilingSummary.xml")
    for m in re.finditer(r"<Report[^>]*>(.*?)</Report>", xml, re.S):
        b = m.group(1)
        name = re.search(r"<ShortName>(.*?)</ShortName>", b)
        fn = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", b)
        if not (name and fn):
            continue
        raw = name.group(1).strip()
        n = re.sub(r"\(.*?\)", "", raw).strip()  # drop (UAH) etc.
        n = re.sub(r"\s+", " ", n).lower()
        if not re.search(r"statement", n):
            continue
        if any(k in n for k in ("parenthetical", "cash flow",
                                "equity", "tax", "(tables)", "details")):
            continue
        # The income statement itself, however the filer words it — but not a
        # standalone "Statements of Comprehensive Income".
        is_income = bool(
            re.search(r"statements? of (consolidated )?income", n)
            or re.search(r"income and comprehensive", n)
        )
        is_ops = bool(re.search(r"statements? of (consolidated )?operations", n))
        if is_income or is_ops:
            return fn.group(1).strip(), raw
    raise SystemExit(f"no income-statement R-file for CIK {cik}")


def parse_rfile(cik: int, accn: str, rfile: str) -> tuple[str, str, list[list[str]]]:
    """Return (title-with-units, period-header, rows)."""
    h = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/{rfile}")
    t = re.search(r"<table.*?</table>", h, re.S).group(0)
    rows: list[list[str]] = []
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S):
        cells = re.findall(r"<t[hd][^>]*>(.*?)</t[hd]>", tr, re.S)
        clean = []
        for c in cells:
            txt = re.sub(r"<[^>]+>", "", c)
            txt = unescape(txt).replace("\xa0", " ")
            clean.append(re.sub(r"\s+", " ", txt).strip())
        if any(c for c in clean):
            rows.append(clean)
    title = rows[0][0] if rows else ""
    header = rows[1] if len(rows) > 1 else []
    return title, header, rows[2:]


def is_section(row: list[str]) -> bool:
    """Section headers carry no numbers (REVENUES, OPERATING EXPENSES, …)."""
    return all(not re.search(r"\d", c) for c in row[1:])


def is_total(label: str) -> bool:
    l = label.lower()
    return l.startswith("total") or any(
        k in l for k in ("net income", "income before", "net increase", "profit")
    )


def fy_label(header: list[str]) -> str:
    """Derive a fiscal-year tag from the first column date, e.g. 'FY2025'."""
    m = re.search(r"(20\d\d)", header[0]) if header else None
    return f"FY{m.group(1)}" if m else "FY-latest"


def merge_abstract_triples(rows: list[list[str]]) -> list[list[str]]:
    """Some R-files (e.g. United) render a line as two label-only abstract rows
    followed by the value row, where the value row's own label is the XBRL
    element name ("Total operating revenue") rather than the display label
    ("Passenger revenue"). Merge [abstract, abstract, values] into one row
    carrying the first abstract's label. A single abstract before a value row
    ("Operating expense:" -> "Salaries and related costs") is left alone."""
    out: list[list[str]] = []
    i = 0
    while i < len(rows):
        cur = rows[i]
        nxt = rows[i + 1] if i + 1 < len(rows) else None
        nxt2 = rows[i + 2] if i + 2 < len(rows) else None
        if (
            nxt and nxt2
            and is_section(cur) and is_section(nxt) and not is_section(nxt2)
            and cur[0] != nxt[0]
        ):
            out.append([cur[0]] + nxt2[1:])
            i += 3
            continue
        out.append(cur)
        i += 1
    return out


def render_pdf(ticker: str, name: str, meta: dict, title: str, header: list[str],
               rows: list[list[str]], out: Path, stmt_title: str) -> None:
    rows = merge_abstract_triples(rows)
    ncol = max(len(r) for r in rows)
    units = ""
    m = re.search(r"\$ in (Millions|Thousands|Billions)", title)
    if m:
        units = f" · $ in {m.group(1).lower()}"
    stmt_name = stmt_title

    body_rows = []
    for r in rows:
        label = r[0] if r else ""
        vals = r[1:]
        section = is_section(r)
        total = is_total(label)
        cls = "sec" if section else ("tot" if total else "det")
        tds = "".join(
            f'<td class="num">{escape(v)}</td>' for v in (vals + [""] * (ncol - len(vals)))
        )
        body_rows.append(
            f'<tr class="{cls}"><td class="lbl">{escape(label)}</td>{tds}</tr>'
        )

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 16mm 15mm; }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 8.5pt; color: #1a1a1a; }}
.kicker {{ font-size: 8pt; letter-spacing: 1.5px; color: #64748b; margin-bottom: 4mm; }}
h1 {{ font-size: 13pt; color: #1a3557; margin: 0 0 1mm 0; }}
.meta {{ font-size: 8pt; color: #444; margin-bottom: 1mm; }}
.meta b {{ color: #1a3557; }}
.src {{ font-size: 7pt; color: #64748b; margin-bottom: 4mm; word-break: break-all; }}
table {{ width: 100%; border-collapse: collapse; }}
caption {{ text-align: left; font-size: 8pt; color: #64748b; padding-bottom: 1.5mm; }}
th {{ background: #1a3557; color: #fff; padding: 1.5mm 2mm; font-size: 7.5pt; text-align: right; }}
th.lbl {{ text-align: left; }}
td {{ padding: 1mm 2mm; border-bottom: 0.5px solid #e8edf3; }}
td.lbl {{ text-align: left; }}
td.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
tr.tot td {{ font-weight: bold; background: #f0f5fb; }}
tr.sec td {{ font-weight: bold; color: #1a3557; border-top: 1px solid #cbd5e1; }}
tr.det td.lbl {{ padding-left: 5mm; color: #333; }}
</style></head><body>
<div class="kicker">SOURCE EXCERPT — as reported in the filing</div>
<h1>{escape(name)} ({ticker})</h1>
<div class="meta">Form 10-K · <b>{escape(stmt_name)}</b> · filed {escape(meta['filed'])}</div>
<div class="meta">Accession No. {escape(meta['acc'])} · Item 8</div>
<div class="src">Source: https://www.sec.gov/Archives/edgar/data/{meta['cik']}/{meta['acc'].replace('-', '')}/{meta['doc']}</div>
<table>
<caption>{escape(stmt_name)}{escape(units)}</caption>
<tr><th class="lbl">{escape(header[0]) if header else ''}</th>{''.join(f'<th>{escape(h)}</th>' for h in header[1:ncol])}</tr>
{''.join(body_rows)}
</table>
</body></html>"""
    from weasyprint import HTML

    tmp = out.with_suffix(".html")
    tmp.write_text(html, encoding="utf-8")
    HTML(string=html).write_pdf(str(out))
    tmp.unlink()


def main(argv: list[str]) -> int:
    tickers = argv or list(COMPANIES)
    for tk in tickers:
        if tk not in COMPANIES:
            print(f"  ! unknown ticker {tk}")
            continue
        cik, name, stmt_title = COMPANIES[tk]
        print(f"· {tk} …", flush=True)
        meta = latest_10k(cik)
        accn = meta["acc"].replace("-", "")
        rfile, short = income_statement_rfile(cik, accn)
        title, header, rows = parse_rfile(cik, accn, rfile)
        fy = fy_label(header)
        out = BASE_DIR / f"{FILE_PREFIX[tk]} 10-K {fy} - {stmt_title}.pdf"
        render_pdf(tk, name, meta, title, header, rows, out, stmt_title)
        print(f"  ✓ {out.name}  ({len(rows)} rows, {out.stat().st_size // 1024} KB)")
        time.sleep(0.4)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
