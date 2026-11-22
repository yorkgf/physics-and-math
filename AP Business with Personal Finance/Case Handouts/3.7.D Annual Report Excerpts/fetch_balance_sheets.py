#!/usr/bin/env python3
"""Extract the consolidated balance sheet from each company's latest 10-K on
SEC EDGAR and render a clean one-page PDF in the 3.7.D package's house style.

Pipeline: submissions API -> latest 10-K accession -> FilingSummary.xml ->
the R-file for the balance sheet -> parsed table -> WeasyPrint PDF.

Adapted from 3.6.D's fetch_income_statements.py. Differences:
  * the target report is the balance sheet, which filers word inconsistently:
    "CONSOLIDATED BALANCE SHEETS", "Consolidated Balance Sheet",
    "CONSOLIDATED STATEMENTS OF FINANCIAL POSITION" (Target, JPMorgan) —
    while rejecting the "(Parenthetical)" share-count twin and "Details".
  * balance sheets are two-sided; empty spacer columns are dropped.
  * slightly smaller type: a balance sheet carries ~40 rows, not ~25.

Usage:  python3 fetch_balance_sheets.py            # all companies
        python3 fetch_balance_sheets.py AAPL DAL   # only these tickers
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

# ticker -> (CIK, display name, statement title used on the PDF).
COMPANIES = {
    "AAPL": (320193, "Apple Inc.", "Consolidated Balance Sheets"),
    "WMT": (104169, "Walmart Inc.", "Consolidated Balance Sheets"),
    "TGT": (27419, "Target Corporation", "Consolidated Statements of Financial Position"),
    "DAL": (27904, "Delta Air Lines, Inc.", "Consolidated Balance Sheets"),
    "UAL": (100517, "United Airlines Holdings, Inc.", "Consolidated Balance Sheets"),
    "KO": (21344, "The Coca-Cola Company", "Consolidated Balance Sheets"),
    "MCD": (63908, "McDonald's Corporation", "Consolidated Balance Sheet"),
    "NKE": (320187, "NIKE, Inc.", "Consolidated Balance Sheets"),
}

# Banks are deliberately excluded: a bank's balance sheet has no
# current/long-term split in the CED's sense (deposits have no stated due
# date), and 3.6.D already uses JPM/BAC for the income statement.

# File-name prefix per ticker (the filing's ShortName is inconsistent).
FILE_PREFIX = {
    "AAPL": "Apple", "WMT": "Walmart", "TGT": "Target", "DAL": "Delta",
    "UAL": "United", "KO": "Coca-Cola", "MCD": "McDonalds", "NKE": "Nike",
}

# Which knowledge point(s) each statement feeds (for the README index).
KP_MAP = {
    "AAPL": "KP1 equation · KP3 debt split · KP4 equity",
    "WMT": "KP2 current assets · KP5-7 working capital",
    "TGT": "KP2 current assets · KP5-7 working capital (pairs with WMT)",
    "DAL": "KP2 fixed assets · KP3 debt split · KP5-7 leverage",
    "UAL": "KP2 fixed assets · KP3 debt split · KP5-7 leverage (pairs with DAL)",
    "KO": "KP2 intangibles · KP4 retained earnings/dividends",
    "MCD": "KP2 intangibles · KP6 comparable debt (pairs with KO)",
    "NKE": "KP2 intangibles · KP4 equity",
}

# EDGAR's R-file renderer occasionally emits a few lines out of statement
# order — a line lands after the grand total (Delta's air traffic liability;
# Nike's Class A/B stock lines). Each entry is
# (label, value_fragment_or_None, anchor_label): move the first still-unplaced
# tail row whose label matches (and whose first value contains the fragment,
# if given) to immediately before the anchor row. Only rows sitting after the
# "Total liabilities … equity" row are eligible, so the in-place copy stays.
ROW_SURGERY = {
    "DAL": [
        ("Air traffic liability", None, "Total current liabilities"),
        ("Loyalty program deferred revenue", "4,876", "Total current liabilities"),
        ("Loyalty program deferred revenue", "4,386", "Total noncurrent liabilities"),
    ],
    "NKE": [
        ("Class A Convertible Common Stock", None, "Capital in excess of stated value"),
        ("Class B Common Stock", None, "Capital in excess of stated value"),
    ],
}

# Display labels where the R-file's XBRL element label differs from the label
# printed in the filing (Nike tags its stock lines with element names that
# mention "Convertible"; the statement prints plain "Class A Common Stock").
LABEL_FIX = {
    "NKE": {"Class A Convertible Common Stock": "Class A Common Stock"},
}

# Only Delta's and Nike's R-files render lines as [abstract, abstract, values]
# triples — and only in the misplaced tail after the grand total (Delta's
# air-traffic and loyalty deferred-revenue lines; Nike's Class A/B stock
# lines, where the detail row carries the XBRL element name "Common stock at
# stated value" instead of the display label). The merge heuristic is harmful
# in statement bodies — on Apple it would glue "Commitments and contingencies"
# onto the common-stock values — so it is opt-in AND tail-only.
MERGE_TRIPLES = {"DAL", "NKE"}


def merge_tail_triples(rows: list[list[str]]) -> list[list[str]]:
    """Apply merge_abstract_triples to the rows after the grand total only."""
    grand = next(
        (i for i, r in enumerate(rows)
         if r[0].lower().startswith("total liabilities")),
        len(rows) - 1,
    )
    return rows[: grand + 1] + merge_abstract_triples(rows[grand + 1 :])


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


def balance_sheet_rfile(cik: int, accn: str) -> tuple[str, str]:
    """Find the R-file for the balance sheet.

    Wording across filers: "CONSOLIDATED BALANCE SHEETS" (Apple, Delta,
    United, Coca-Cola, McDonald's, Nike), "Consolidated Balance Sheets"
    (Walmart), "CONSOLIDATED STATEMENTS OF FINANCIAL POSITION" (Target,
    JPMorgan). Reject the "(Parenthetical)" twin, tables, details, schedules
    and the other three statements.
    """
    xml = get(f"https://www.sec.gov/Archives/edgar/data/{cik}/{accn}/FilingSummary.xml")
    for m in re.finditer(r"<Report[^>]*>(.*?)</Report>", xml, re.S):
        b = m.group(1)
        name = re.search(r"<ShortName>(.*?)</ShortName>", b)
        fn = re.search(r"<HtmlFileName>(.*?)</HtmlFileName>", b)
        if not (name and fn):
            continue
        raw = name.group(1).strip()
        n = re.sub(r"\(.*?\)", "", raw).strip()  # drop (Parenthetical) etc.
        n = re.sub(r"\s+", " ", n).lower()
        if any(k in n for k in (
            "parenthetical", "(tables)", "details", "schedule", "cash flow",
            "equity", "tax", "acquisition", "segment", "unclassified",
        )):
            continue
        if "balance sheet" in n or "financial position" in n:
            return fn.group(1).strip(), raw
    raise SystemExit(f"no balance-sheet R-file for CIK {cik}")


def parse_rfile(cik: int, accn: str, rfile: str) -> tuple[str, str, list[list[str]]]:
    """Return (title-with-units, period-header, rows).

    R-files are not uniform: some put the period dates in the same <tr> as the
    title (Apple), others give the title its own row and the dates the next
    one. Find the first row whose data cells contain a year and treat that as
    the header; everything after it is the statement body."""
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
    hi = next(
        (i for i, r in enumerate(rows) if any(re.search(r"20\d\d", c) for c in r[1:])),
        0,
    )
    header = rows[hi] if hi < len(rows) else []
    return title, header, rows[hi + 1 :]


def is_section(row: list[str]) -> bool:
    """Section headers carry no numbers (ASSETS, Current liabilities:, …)."""
    return all(not re.search(r"\d", c) for c in row[1:])


def is_total(label: str) -> bool:
    return label.lower().startswith("total")


def apply_surgery(rows: list[list[str]], moves: list) -> tuple[list[list[str]], list[str]]:
    """Restore the filing's own presentation order for the lines the R-file
    renderer emitted after the grand total. Returns (rows, warnings); warnings
    flag any move that did not find its row (the filing changed — re-check)."""
    warnings: list[str] = []
    out = list(rows)

    def grand_total_idx() -> int:
        return next(
            (i for i, r in enumerate(out)
             if r[0].lower().startswith("total liabilities")),
            len(out) - 1,
        )

    for label, frag, anchor in moves:
        grand = grand_total_idx()
        idx = next(
            (i for i, r in enumerate(out)
             if i > grand and r[0] == label
             and (frag is None or (len(r) > 1 and frag in r[1]))),
            None,
        )
        if idx is None:
            warnings.append(f"surgery: no tail row for {label!r} ({frag})")
            continue
        row = out.pop(idx)
        dst = next((i for i, r in enumerate(out) if r[0] == anchor), None)
        if dst is None:
            warnings.append(f"surgery: no anchor {anchor!r} for {label!r}")
            out.append(row)
            continue
        out.insert(dst, row)
    return out, warnings


def fy_label(header: list[str]) -> str:
    """Derive a fiscal-year tag from the first dated column, e.g. 'FY2026'."""
    for c in header[1:] if header else []:
        m = re.search(r"(20\d\d)", c)
        if m:
            return f"FY{m.group(1)}"
    return "FY-latest"


def merge_abstract_triples(rows: list[list[str]]) -> list[list[str]]:
    """Some R-files render a line as two label-only abstract rows followed by
    the value row (United does this). Merge [abstract, abstract, values] into
    one row carrying the first abstract's label. A single abstract before a
    value row ("Current liabilities:" -> "Accounts payable") is left alone."""
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


def drop_empty_columns(rows: list[list[str]], header: list[str]) -> tuple[list[str], list[list[str]]]:
    """Two-sided statements often carry an empty spacer column; drop columns
    that are empty in every row."""
    ncol = max(len(r) for r in rows)
    keep = []
    for j in range(ncol):
        if j == 0 or any(j < len(r) and r[j] for r in rows):
            keep.append(j)
    return (
        [header[j] if j < len(header) else "" for j in keep],
        [[r[j] if j < len(r) else "" for j in keep] for r in rows],
    )


def render_pdf(ticker: str, name: str, meta: dict, title: str, header: list[str],
               rows: list[list[str]], out: Path, stmt_title: str, kp: str) -> None:
    header, rows = drop_empty_columns(rows, header)
    ncol = max(len(r) for r in rows)
    units = ""
    m = re.search(r"\$ in (Millions|Thousands|Billions)", title)
    if m:
        units = f" · $ in {m.group(1).lower()}"

    body_rows = []
    for r in rows:
        label = r[0] if r else ""
        vals = r[1:]
        section = is_section(r)
        total = is_total(label)
        # A no-number label whose cells are all "0" (e.g. Delta's
        # "Commitments and Contingencies") is a section header, not a line of
        # zeroes.
        if (not section and not total and not re.search(r"\d", label)
                and all(v in ("", "0", "$ 0", "$0") for v in vals)):
            section = True
        if section:
            vals = [""] * len(vals)
        cls = "sec" if section else ("tot" if total else "det")
        tds = "".join(
            f'<td class="num">{escape(v)}</td>' for v in (vals + [""] * (ncol - len(vals)))
        )
        body_rows.append(
            f'<tr class="{cls}"><td class="lbl">{escape(label)}</td>{tds}</tr>'
        )

    html = f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><style>
@page {{ size: A4; margin: 13mm 14mm; }}
body {{ font-family: 'DejaVu Sans', sans-serif; font-size: 7.6pt; color: #1a1a1a; }}
.kicker {{ font-size: 7.5pt; letter-spacing: 1.5px; color: #64748b; margin-bottom: 3mm; }}
h1 {{ font-size: 12pt; color: #1a3557; margin: 0 0 1mm 0; }}
.meta {{ font-size: 7.5pt; color: #444; margin-bottom: 0.8mm; }}
.meta b {{ color: #1a3557; }}
.src {{ font-size: 6.6pt; color: #64748b; margin-bottom: 3mm; word-break: break-all; }}
table {{ width: 100%; border-collapse: collapse; }}
caption {{ text-align: left; font-size: 7.5pt; color: #64748b; padding-bottom: 1.2mm; }}
th {{ background: #1a3557; color: #fff; padding: 1.2mm 1.8mm; font-size: 7pt; text-align: right; }}
th.lbl {{ text-align: left; }}
td {{ padding: 0.75mm 1.8mm; border-bottom: 0.4px solid #e8edf3; }}
td.lbl {{ text-align: left; }}
td.num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
tr.tot td {{ font-weight: bold; background: #f0f5fb; }}
tr.sec td {{ font-weight: bold; color: #1a3557; border-top: 0.8px solid #cbd5e1; }}
tr.det td.lbl {{ padding-left: 4mm; color: #333; }}
</style></head><body>
<div class="kicker">SOURCE EXCERPT — as reported in the filing</div>
<h1>{escape(name)} ({ticker})</h1>
<div class="meta">Form 10-K · <b>{escape(stmt_title)}</b> · filed {escape(meta['filed'])}</div>
<div class="meta">Accession No. {escape(meta['acc'])} · Item 8 · <b>{escape(kp)}</b></div>
<div class="src">Source: https://www.sec.gov/Archives/edgar/data/{meta['cik']}/{meta['acc'].replace('-', '')}/{meta['doc']}</div>
<table>
<caption>{escape(stmt_title)}{escape(units)}</caption>
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
        rfile, short = balance_sheet_rfile(cik, accn)
        title, header, rows = parse_rfile(cik, accn, rfile)
        rows = merge_tail_triples(rows) if tk in MERGE_TRIPLES else rows
        rows, warns = apply_surgery(rows, ROW_SURGERY.get(tk, []))
        for w in warns:
            print(f"  ! {tk}: {w}", file=sys.stderr)
        for r in rows:
            if r and r[0] in LABEL_FIX.get(tk, {}):
                r[0] = LABEL_FIX[tk][r[0]]
        fy = fy_label(header)
        out = BASE_DIR / f"{FILE_PREFIX[tk]} 10-K {fy} - {stmt_title}.pdf"
        render_pdf(tk, name, meta, title, header, rows, out, stmt_title, KP_MAP[tk])
        print(f"  ✓ {out.name}  ({len(rows)} rows, {out.stat().st_size // 1024} KB) [{short}]")
        time.sleep(0.4)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
