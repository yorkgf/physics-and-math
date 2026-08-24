#!/usr/bin/env python3
"""Export Vocab Review Booklet to a beautifully designed PDF."""

import markdown
import weasyprint
from pathlib import Path

VAULT = Path("/home/yorkgf/Documents/Obsidian Vault")
SOURCE = VAULT / "AP Business with Personal Finance" / "Vocab Review Booklet.md"
OUTPUT = VAULT / "AP Business with Personal Finance" / "Vocab Review Booklet.pdf"

# ── Read & convert markdown ──────────────────────────────────────────────────
md_text = SOURCE.read_text(encoding="utf-8")

# Remove \newpage commands (we handle page breaks via CSS)
md_text = md_text.replace("\\newpage", "")

html_body = markdown.markdown(
    md_text,
    extensions=["tables", "fenced_code", "toc"],
)

# ── CSS ──────────────────────────────────────────────────────────────────────
CSS = """
@page {
    size: A4;
    margin: 22mm 20mm 25mm 20mm;
    @bottom-center {
        content: counter(page);
        font-family: "Noto Sans CJK SC", sans-serif;
        font-size: 9pt;
        color: #94a3b8;
    }
}

@page :first {
    margin: 0;
    @bottom-center { content: none; }
}

/* ── Cover ────────────────────────────────────────────────────────────────── */

.cover {
    page-break-after: always;
    width: 210mm;
    height: 297mm;
    box-sizing: border-box;
    background: linear-gradient(135deg, #0f172a 0%, #1e3a5f 40%, #0f172a 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    position: relative;
    overflow: hidden;
    padding: 40mm 25mm;
}

/* decorative circles */
.cover::before {
    content: "";
    position: absolute;
    top: -80mm;
    right: -60mm;
    width: 260mm;
    height: 260mm;
    border-radius: 50%;
    border: 1.5mm solid rgba(255, 255, 255, 0.06);
}
.cover::after {
    content: "";
    position: absolute;
    bottom: -100mm;
    left: -70mm;
    width: 300mm;
    height: 300mm;
    border-radius: 50%;
    border: 1.5mm solid rgba(255, 255, 255, 0.04);
}

.cover-rule-top {
    width: 30mm;
    height: 1mm;
    background: linear-gradient(90deg, transparent, #60a5fa, transparent);
    margin-bottom: 12mm;
}

.cover-label {
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 11pt;
    letter-spacing: 4pt;
    text-transform: uppercase;
    color: #60a5fa;
    margin-bottom: 8mm;
}

.cover-title {
    font-family: "Noto Serif CJK SC", "Nimbus Roman", serif;
    font-size: 30pt;
    font-weight: 700;
    color: #f1f5f9;
    line-height: 1.25;
    margin: 0 0 6mm 0;
}

.cover-subtitle {
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 13pt;
    color: #94a3b8;
    line-height: 1.6;
    margin-bottom: 14mm;
    max-width: 130mm;
}

.cover-rule-bottom {
    width: 50mm;
    height: 0.6mm;
    background: linear-gradient(90deg, transparent, #334155, transparent);
    margin-bottom: 10mm;
}

.cover-meta {
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 9pt;
    color: #64748b;
    letter-spacing: 1pt;
}

/* ── Body ─────────────────────────────────────────────────────────────────── */

body {
    font-family: "Noto Sans CJK SC", "Nimbus Sans", sans-serif;
    font-size: 9.5pt;
    line-height: 1.55;
    color: #1e293b;
}

h1 {
    font-family: "Noto Serif CJK SC", "Nimbus Roman", serif;
    font-size: 20pt;
    font-weight: 700;
    color: #0f172a;
    border-bottom: 0.8mm solid #1e3a5f;
    padding-bottom: 3mm;
    margin-top: 10mm;
    margin-bottom: 6mm;
    page-break-before: always;
}

h1:first-of-type {
    page-break-before: auto;
}

h2 {
    font-family: "Noto Sans CJK SC", sans-serif;
    font-size: 14pt;
    font-weight: 700;
    color: #1e3a5f;
    margin-top: 8mm;
    margin-bottom: 4mm;
    padding-bottom: 2mm;
    border-bottom: 0.3mm solid #cbd5e1;
    page-break-before: always;
}

h3 {
    font-size: 11pt;
    font-weight: 700;
    color: #334155;
    margin-top: 6mm;
    margin-bottom: 3mm;
}

p {
    margin: 2mm 0;
}

strong {
    font-weight: 700;
    color: #0f172a;
}

hr {
    border: none;
    border-top: 0.3mm solid #e2e8f0;
    margin: 6mm 0;
}

/* ── Tables ───────────────────────────────────────────────────────────────── */

table {
    width: 100%;
    border-collapse: collapse;
    margin: 4mm 0 6mm 0;
    font-size: 8.5pt;
    page-break-inside: auto;
}

thead {
    display: table-header-group;
}

tr {
    page-break-inside: avoid;
    page-break-after: auto;
}

th {
    background: #1e3a5f;
    color: #f1f5f9;
    font-weight: 700;
    text-align: left;
    padding: 2.5mm 3mm;
    font-size: 8pt;
    letter-spacing: 0.3pt;
}

td {
    padding: 2mm 3mm;
    border-bottom: 0.2mm solid #e2e8f0;
    vertical-align: top;
}

tr:nth-child(even) td {
    background: #f8fafc;
}

tr:nth-child(odd) td {
    background: #ffffff;
}

/* First column (#) — center and shrink */
td:first-child, th:first-child {
    text-align: center;
    width: 8mm;
    color: #94a3b8;
}

/* Second column (Term) — bold */
td:nth-child(2) {
    font-weight: 600;
    color: #0f172a;
    white-space: nowrap;
}

/* ── Print helpers ────────────────────────────────────────────────────────── */

.content-start {
    page-break-before: auto;
}
"""

# ── Cover HTML ───────────────────────────────────────────────────────────────
cover_html = """
<div class="cover">
    <div class="cover-rule-top"></div>
    <div class="cover-label">AP Exam Review</div>
    <div class="cover-title">Business with<br>Personal Finance</div>
    <div class="cover-subtitle">Complete Vocabulary Reference &mdash; Units 1&ndash;5<br>Definitions &middot; Trap Pairs &middot; Key Formulas</div>
    <div class="cover-rule-bottom"></div>
    <div class="cover-meta">2025&ndash;2026</div>
</div>
"""

# ── Assemble full HTML ───────────────────────────────────────────────────────
full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<style>{CSS}</style>
</head>
<body>
{cover_html}
<div class="content-start">
{html_body}
</div>
</body>
</html>
"""

# ── Generate PDF ─────────────────────────────────────────────────────────────
print("Generating PDF...")
doc = weasyprint.HTML(string=full_html)
doc.write_pdf(str(OUTPUT))
print(f"Done → {OUTPUT}")
