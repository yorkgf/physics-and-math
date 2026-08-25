#!/usr/bin/env python3
"""
Generate a professionally typeset PDF of Case Handouts - Student Print Edition.
Uses a two-pass markdown -> HTML -> WeasyPrint -> PDF pipeline:
  Pass 1: render body only -> extract each case's starting page number
  Pass 2: build cover TOC with accurate page numbers -> render final PDF
"""

import re
import subprocess
import tempfile
from pathlib import Path

import markdown
from weasyprint import HTML

# ── Paths ──────────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).parent
INPUT_MD  = BASE_DIR / "Case Handouts - Student Print Edition.md"
OUTPUT_PDF = BASE_DIR / "Case Handouts - Student Print Edition.pdf"

# ── Fonts ──────────────────────────────────────────────────────────────────────
NOTO_SANS_CJK    = "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"
NOTO_SERIF_CJK   = "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"
SOURCE_HAN_SANS  = "/usr/share/fonts/opentype/source-han-cjk/SourceHanSansSC-Regular.otf"
DEJAVU_SANS      = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DEJAVU_SERIF     = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
DEJAVU_MONO      = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
OPEN_SANS        = "/usr/share/fonts/truetype/open-sans/OpenSans-Regular.ttf"

# ── Step 1: Read & pre-process Markdown ───────────────────────────────────────

raw = INPUT_MD.read_text(encoding="utf-8")

# Remove the leading TOC block (lines 1-50 up to the first \newpage or the
# first embedded YAML block) — we'll render our own cover + TOC.
# The file starts with a title heading + TOC then the case sections.
# We keep everything but strip the top-of-file TOC list since we have our own cover.

# 1. Split off the preamble (title + numbered TOC list)
#    The cases start at the first embedded YAML frontmatter block (--- key: val ... ---).
#    We detect that by finding the first occurrence of a YAML block opener after line 1.
yaml_start = re.search(
    r"(?m)^---\s*\nsubject:",  # first YAML block that begins with "subject:"
    raw
)
if yaml_start:
    preamble_end = yaml_start.start()
    # Walk back to trim trailing whitespace / horizontal rules before YAML
    preamble_end = raw.rfind("\n", 0, preamble_end)
else:
    preamble_end = 0
cases_raw = raw[preamble_end:]

# 2. Remove embedded YAML frontmatter blocks that appear between cases.
#    Pattern: a --- line, followed by key: value lines, followed by another --- line.
#    These appear right after \newpage markers and before the # heading.
yaml_block_re = re.compile(
    r"(?m)^---\s*\n"           # opening ---
    r"(?:[\w_]+:[ \t]*.+\n)+"  # one or more key: value lines
    r"---\s*\n",                # closing ---
)
cases_clean = yaml_block_re.sub("", cases_raw)

# 3. Replace \newpage markers with an HTML page-break div placeholder.
#    We use a sentinel that won't appear in the markdown itself.
cases_clean = cases_clean.replace("\\newpage", "\n\n<div class=\"page-break\"></div>\n\n")

# 4. Remove the triple-dash horizontal rules that immediately follow the preamble
#    "---" separators that the template uses decoratively between sections;
#    keep only meaningful ones.
# Actually, the --- lines serve as <hr> in HTML and we style them lightly — keep them.

# ── Step 2: Extract TOC labels and case titles ────────────────────────────────

# Full H1 case titles in order (skip the document title at index 0)
case_titles = re.findall(r"^# (.+)", raw, re.MULTILINE)[1:]

# Build short TOC labels: parse every YAML block for topic+case_company,
# then align with H1 titles by position. Cases without a YAML block fall
# back to a shortened form of the H1 title.
def shorten_title(title):
    for suffix in [" — Case Handout", " — Case Handouts"]:
        title = title.replace(suffix, "")
    return title.strip()

# Map each H1 position → short label derived from its preceding YAML block
yaml_block_re_pos = re.compile(
    r"(?m)^---\s*\n((?:[\w_]+:[ \t]*.+\n)+)---\s*\n"
)
h1_matches = list(re.finditer(r"(?m)^# (.+)", raw))[1:]  # skip doc title

toc_items = []
for h1_match in h1_matches:
    h1_pos = h1_match.start()
    h1_title = h1_match.group(1)
    # Find the nearest YAML block that ends just before this H1
    label = None
    for m in yaml_block_re_pos.finditer(raw):
        if m.end() <= h1_pos and m.end() > h1_pos - 300:
            block = m.group(1)
            topic = re.search(r"topic:\s*(.+)", block)
            company = re.search(r"case_company:\s*(.+)", block)
            if topic and company:
                label = f"{topic.group(1).strip()} {company.group(1).strip()}"
            elif topic:
                label = topic.group(1).strip()
            elif company:
                label = company.group(1).strip()
    toc_items.append(label if label else shorten_title(h1_title))

# ── Step 3: Convert Markdown → HTML ──────────────────────────────────────────

md_processor = markdown.Markdown(
    extensions=[
        "tables",
        "fenced_code",
        "attr_list",
        "nl2br",
        "sane_lists",
    ]
)

body_html = md_processor.convert(cases_clean)

# ── Step 4: CSS ───────────────────────────────────────────────────────────────

FONT_FACE_CSS = f"""
@font-face {{
  font-family: 'Noto Sans CJK SC';
  src: url('{NOTO_SANS_CJK}');
  font-weight: normal;
}}
@font-face {{
  font-family: 'Noto Serif CJK SC';
  src: url('{NOTO_SERIF_CJK}');
  font-weight: normal;
}}
@font-face {{
  font-family: 'Source Han Sans SC';
  src: url('{SOURCE_HAN_SANS}');
  font-weight: normal;
}}
"""

MAIN_CSS = """
/* ── Page setup ─────────────────────────────────────────────────────────── */
@page {
  size: A4;
  margin: 20mm 20mm 22mm 22mm;

  @bottom-center {
    content: counter(page);
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 10pt;
    color: #888;
  }
  @top-right {
    content: "AP Business with Personal Finance — Case Handouts";
    font-family: 'DejaVu Sans', sans-serif;
    font-size: 8.5pt;
    color: #aaa;
  }
}

/* Suppress running header and page number on cover and TOC pages */
@page cover-page {
  @bottom-center { content: none; }
  @top-right     { content: none; }
}
@page toc-page {
  @bottom-center { content: none; }
  @top-right     { content: none; }
}

/* ── Reset / base ───────────────────────────────────────────────────────── */
* { box-sizing: border-box; }

body {
  font-family: 'DejaVu Sans', 'Noto Sans CJK SC', sans-serif;
  font-size: 11pt;
  line-height: 1.6;
  color: #1a1a1a;
  background: #fff;
}

/* ── Page breaks ────────────────────────────────────────────────────────── */
.page-break {
  page-break-after: always;
  break-after: page;
}

/* ── Cover page ─────────────────────────────────────────────────────────── */
.cover {
  page: cover-page;
  page-break-after: always;
  break-after: page;
  /* Force exactly one A4 page height so page-break-after fires correctly.
     A4 = 297mm, margins top+bottom = 20+22 = 42mm → content height = 255mm */
  min-height: 255mm;
  position: relative;
}

/* Teal gradient strip at very top */
.cover-band-top {
  height: 4mm;
  background: #2a7fba;
  margin-bottom: 0;
}

/* Dark hero section */
.cover-hero {
  background: #1a3557;
  padding: 14mm 14mm 10mm 14mm;
}

.cover-eyebrow {
  font-size: 9pt;
  font-weight: bold;
  color: rgba(255,255,255,0.45);
  text-transform: uppercase;
  letter-spacing: 0.2em;
  margin-bottom: 10mm;
}

.cover-title {
  font-family: 'DejaVu Serif', 'Noto Serif CJK SC', serif;
  font-size: 50pt;
  font-weight: bold;
  color: #ffffff;
  line-height: 1.0;
  margin-bottom: 5mm;
}

.cover-subtitle {
  font-size: 17pt;
  color: rgba(255,255,255,0.6);
  margin-bottom: 10mm;
}

/* Decorative ruled lines */
.cover-hero-rule1 { height: 2px; background: rgba(255,255,255,0.3); margin-bottom: 3px; }
.cover-hero-rule2 { height: 1px; background: rgba(42,127,186,0.65); margin-bottom: 3px; width: 55%; }
.cover-hero-rule3 { height: 1px; background: rgba(255,255,255,0.10); width: 30%; }

/* White body section */
.cover-body {
  background: #fff;
  padding: 9mm 14mm 0 14mm;
}

/* 3-column stats */
.cover-stats {
  display: table;
  width: 100%;
  margin-bottom: 8mm;
  border-collapse: collapse;
}

.cover-stats-row { display: table-row; }

.cover-stat {
  display: table-cell;
  width: 33%;
  border-left: 3px solid #2a7fba;
  padding: 0 0 0 4mm;
  vertical-align: top;
}

.cover-stat + .cover-stat {
  padding-left: 4mm;
}

.cover-stat-label {
  font-size: 7.5pt;
  color: #999;
  text-transform: uppercase;
  letter-spacing: 0.12em;
  display: block;
  margin-bottom: 1.5mm;
}

.cover-stat-value {
  font-size: 14pt;
  font-weight: bold;
  color: #1a3557;
  display: block;
}

/* Unit topic chips */
.cover-units-row {
  margin-bottom: 0;
  line-height: 2;
}

.cover-unit-tag {
  display: inline-block;
  font-size: 8pt;
  color: #1a3557;
  background: #e8f0f8;
  border-radius: 2px;
  padding: 1mm 3mm;
  margin-right: 2mm;
  font-weight: bold;
  letter-spacing: 0.03em;
}

/* Footer pinned to bottom with large margin-top */
.cover-footer {
  margin-top: 88mm;
  border-top: 1px solid #e0e0e0;
  padding-top: 3mm;
  font-size: 8.5pt;
  color: #bbb;
  text-align: center;
}

/* ── TOC page ────────────────────────────────────────────────────────────── */
.toc-page {
  page: toc-page;
  page-break-after: always;
  break-after: page;
}

.toc-header {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  margin-bottom: 5mm;
  padding-bottom: 2mm;
  border-bottom: 2px solid #1a3557;
}

.toc-header-title {
  font-family: 'DejaVu Serif', 'Noto Serif CJK SC', serif;
  font-size: 18pt;
  font-weight: bold;
  color: #1a3557;
}

.toc-header-sub {
  font-size: 9pt;
  color: #888;
}

.toc-list {
  column-count: 2;
  column-gap: 10mm;
  list-style: none;
  padding: 0;
  margin: 0;
}

.toc-list li {
  display: flex;
  align-items: baseline;
  justify-content: space-between;
  gap: 2mm;
  padding: 1.2mm 0;
  border-bottom: 1px dotted #dde3ea;
  font-size: 9pt;
  line-height: 1.4;
  break-inside: avoid;
}

.toc-num {
  color: #aaa;
  font-size: 8pt;
  min-width: 5mm;
  flex-shrink: 0;
}

.toc-label {
  flex: 1;
  color: #222;
}

.toc-pg {
  font-size: 9pt;
  color: #1a3557;
  font-weight: bold;
  white-space: nowrap;
  min-width: 7mm;
  text-align: right;
  flex-shrink: 0;
}

/* ── Headings ───────────────────────────────────────────────────────────── */
h1 {
  font-family: 'DejaVu Serif', 'Noto Serif CJK SC', serif;
  font-size: 22pt;
  color: #1a3557;
  margin-top: 0;
  margin-bottom: 4mm;
  padding-bottom: 2mm;
  border-bottom: 2px solid #1a3557;
  line-height: 1.25;
  page-break-after: avoid;
}

h2 {
  font-size: 14pt;
  color: #1a3557;
  margin-top: 7mm;
  margin-bottom: 2mm;
  page-break-after: avoid;
}

h3 {
  font-size: 12pt;
  color: #2c5282;
  margin-top: 5mm;
  margin-bottom: 1.5mm;
  page-break-after: avoid;
}

h4 {
  font-size: 11pt;
  color: #333;
  margin-top: 4mm;
  margin-bottom: 1mm;
  page-break-after: avoid;
}

/* ── Paragraphs ─────────────────────────────────────────────────────────── */
p {
  margin: 0 0 4mm 0;
  orphans: 3;
  widows: 3;
}

/* ── Blockquote (topic/unit callouts) ──────────────────────────────────── */
blockquote {
  background: #f0f5fb;
  border-left: 3px solid #1a3557;
  margin: 4mm 0 5mm 0;
  padding: 2.5mm 4mm;
  color: #1a3557;
  font-size: 10.5pt;
  font-style: italic;
  border-radius: 0 3px 3px 0;
}
blockquote p { margin: 0; }

/* ── Horizontal rule ────────────────────────────────────────────────────── */
hr {
  border: none;
  border-top: 1px solid #ddd;
  margin: 5mm 0;
}

/* ── Tables ─────────────────────────────────────────────────────────────── */
table {
  width: 100%;
  border-collapse: collapse;
  font-size: 10pt;
  margin: 3mm 0 5mm 0;
  page-break-inside: avoid;
}

thead tr {
  background: #1a3557;
  color: #fff;
}

thead th {
  padding: 2.5mm 3mm;
  text-align: left;
  font-weight: bold;
  font-size: 9.5pt;
}

tbody tr:nth-child(odd)  { background: #f7f9fc; }
tbody tr:nth-child(even) { background: #fff; }

tbody td {
  padding: 2mm 3mm;
  border-bottom: 1px solid #e8edf3;
  vertical-align: top;
}

/* Bold text in table cells (for year / key values) */
tbody td strong, tbody th strong { color: #1a3557; }

/* ── Lists ──────────────────────────────────────────────────────────────── */
ul, ol {
  margin: 1mm 0 4mm 5mm;
  padding-left: 4mm;
}
li { margin-bottom: 1.5mm; }

/* ── Strong / em ────────────────────────────────────────────────────────── */
strong { color: #1a1a1a; font-weight: bold; }
em     { font-style: italic; color: #444; }

/* ── Inline code ────────────────────────────────────────────────────────── */
code {
  font-family: 'DejaVu Sans Mono', monospace;
  font-size: 9.5pt;
  background: #f4f4f4;
  padding: 0 1.5pt;
  border-radius: 2px;
}

/* ── The "keep this handout" footer lines ───────────────────────────────── */
p em:only-child {
  color: #888;
  font-size: 9.5pt;
}

/* ── Questions section styling ──────────────────────────────────────────── */
/* Q1, Q2 … bold bold paragraphs get a left accent */
h2 + p strong:first-child,
h2 + p > strong:first-child {
  color: #1a3557;
}
"""

def make_body_html(front_matter_html, body_html_fragment):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>AP Business with Personal Finance — Case Handouts</title>
  <style>
    {FONT_FACE_CSS}
    {MAIN_CSS}
  </style>
</head>
<body>
  {front_matter_html}
  {body_html_fragment}
</body>
</html>"""


def build_cover_html(n_cases=38):
    """Designed cover page — hero dark panel + white stats body."""
    return f"""
<div class="cover">
  <div class="cover-band-top"></div>

  <!-- Dark hero panel -->
  <div class="cover-hero">
    <div class="cover-eyebrow">AP Business with Personal Finance</div>
    <div class="cover-title">Case<br>Handouts</div>
    <div class="cover-subtitle">Student Print Edition</div>
    <div class="cover-hero-rule1"></div>
    <div class="cover-hero-rule2"></div>
    <div class="cover-hero-rule3"></div>
  </div>

  <!-- White body -->
  <div class="cover-body">

    <!-- 3-column stats -->
    <div class="cover-stats">
      <div class="cover-stats-row">
        <div class="cover-stat">
          <span class="cover-stat-label">Academic Year</span>
          <span class="cover-stat-value">2025–2026</span>
        </div>
        <div class="cover-stat">
          <span class="cover-stat-label">Units</span>
          <span class="cover-stat-value">1 – 4</span>
        </div>
        <div class="cover-stat">
          <span class="cover-stat-label">Total Cases</span>
          <span class="cover-stat-value">{n_cases}</span>
        </div>
      </div>
    </div>

    <!-- Unit topic chips -->
    <div class="cover-units-row">
      <span class="cover-unit-tag">1.1–1.8 · Business Foundations</span>
      <span class="cover-unit-tag">2.1–2.7 · Marketing</span>
      <span class="cover-unit-tag">3.4–3.9 · Finance</span>
      <span class="cover-unit-tag">4.1–4.4 · Management &amp; Strategy</span>
    </div>

  </div>

  <!-- Footer -->
  <div class="cover-footer">
    For classroom distribution only &nbsp;·&nbsp; Read each handout before class &nbsp;·&nbsp; Be ready to discuss
  </div>
</div>
"""


def build_toc_html(toc_items, page_map):
    """Standalone TOC page — compact, fits all 38 entries in one page."""
    items_html = []
    for i, item in enumerate(toc_items, start=1):
        pg = page_map.get(item, "")
        pg_span = f'<span class="toc-pg">{pg}</span>' if pg else '<span class="toc-pg"></span>'
        items_html.append(
            f'<li>'
            f'<span class="toc-num">{i}.</span>'
            f'<span class="toc-label">{item}</span>'
            f'{pg_span}'
            f'</li>'
        )
    toc_html_items = "\n    ".join(items_html)
    return f"""
<div class="toc-page">
  <div class="toc-header">
    <span class="toc-header-title">Table of Contents</span>
    <span class="toc-header-sub">AP Business with Personal Finance — Case Handouts</span>
  </div>
  <ol class="toc-list">
    {toc_html_items}
  </ol>
</div>
"""


def extract_case_pages(pdf_path, case_titles, cover_page_count):
    """
    Run pdftotext on pdf_path and find the first page of each case.
    Returns dict mapping case_title -> absolute_page_number.
    cover_page_count: number of pages occupied by the cover/TOC before body starts.
    """
    result = subprocess.run(
        ["pdftotext", "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        capture_output=True, text=True
    )
    pages = result.stdout.split("\x0c")

    def normalize(s):
        return re.sub(r"[\s\-—–·()[\]'\"]+", "", s).lower()

    page_map = {}
    for title in case_titles:
        norm_title = normalize(title)
        key = norm_title[:28]   # first 28 normalized chars is unique enough
        for i, page in enumerate(pages):
            if i < cover_page_count:
                continue   # skip cover pages
            if key in normalize(page):
                page_map[title] = i + 1   # 1-indexed
                break
    return page_map


# ── Step 5: Two-pass render ───────────────────────────────────────────────────

cover_html = build_cover_html(n_cases=len(case_titles))

# --- Pass 1: render with placeholder TOC (no page numbers) to measure layout
print("Pass 1: rendering draft to measure page numbers…")
placeholder_toc = build_toc_html(toc_items, {})
draft_html = make_body_html(cover_html + placeholder_toc, body_html)

with tempfile.NamedTemporaryFile(suffix=".pdf", delete=False) as tmp:
    tmp_path = Path(tmp.name)

HTML(string=draft_html, base_url=str(BASE_DIR)).write_pdf(str(tmp_path))

# Determine how many pages the cover+TOC occupy (before cases start)
result = subprocess.run(
    ["pdftotext", "-layout", "-enc", "UTF-8", str(tmp_path), "-"],
    capture_output=True, text=True
)
draft_pages = result.stdout.split("\x0c")

first_case_norm = re.sub(r"[\s\-—–·()[\]'\"]+", "", case_titles[0]).lower()[:28]
cover_page_count = 0
for i, pg in enumerate(draft_pages):
    pg_norm = re.sub(r"[\s\-—–·()[\]'\"]+", "", pg).lower()
    if first_case_norm in pg_norm:
        cover_page_count = i
        break
print(f"  Front matter occupies {cover_page_count} page(s); cases start at page {cover_page_count + 1}")

# Map each case title → its page number in the draft PDF
title_to_page = extract_case_pages(tmp_path, case_titles, cover_page_count)
tmp_path.unlink()

# Build label→page map (toc_items and case_titles are in the same order)
assert len(toc_items) == len(case_titles), \
    f"TOC items ({len(toc_items)}) != case titles ({len(case_titles)})"

toc_page_map = {
    label: title_to_page.get(title, "")
    for label, title in zip(toc_items, case_titles)
}

missing = [lbl for lbl, pg in toc_page_map.items() if not pg]
if missing:
    print(f"  ⚠ Could not find page numbers for: {missing}")

# --- Pass 2: render final PDF with accurate page numbers in TOC
print("Pass 2: rendering final PDF with page numbers…")
final_toc = build_toc_html(toc_items, toc_page_map)
final_html = make_body_html(cover_html + final_toc, body_html)

OUTPUT_PDF = BASE_DIR / "Case Handouts - Student Print Edition.pdf"
HTML(string=final_html, base_url=str(BASE_DIR)).write_pdf(str(OUTPUT_PDF))

print(f"✓ PDF saved: {OUTPUT_PDF}")
print(f"  File size: {OUTPUT_PDF.stat().st_size / 1024:.0f} KB")
