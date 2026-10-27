#!/usr/bin/env python3
"""Render the mid-term exam Markdown (Obsidian note) into a print-ready PDF.

用法 / Usage:
    cd "AP Business with Personal Finance/Mid-Term Exam"
    python3 build_exam_pdf.py                 # 生成 "Mid-Term Exam (Sections A + B + C).pdf"
    python3 build_exam_variants.py            # 生成 A / B / C 三份卷

Requires: pandoc + weasyprint (`uv run --with weasyprint weasyprint`).
The Markdown note stays the single source of truth; this module only
(a) drops the teacher-only section, (b) turns the ```answer2x blocks into
ruled answer lines, (c) adds print CSS (page break before Section B/C,
hanging-indent options, page numbers) and (d) renders the PDF.
"""

from __future__ import annotations

import re
import shutil
import sys
import subprocess
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "Mid-Term Exam (Sections A + B + C).md"
OUT = HERE / "Mid-Term Exam (Sections A + B + C).pdf"
TMP_HTML = Path(tempfile.gettempdir()) / "midterm_exam.html"

COVER = HERE / "Cover.pdf"     # 封面（考前须知 + 诚信承诺），存在才会拼接
RULE_HEIGHT_MM = 8.6        # 答题横线间距（≈ 单倍行距的两倍，适合手写）
TEACHER_MARK = "## 出题说明"  # 教师专用段落，导出时整段丢弃

CSS_TEMPLATE = """
@page {
  size: A4;
  margin: 15mm 15mm 14mm 15mm;
  @bottom-center {
    content: "AP Business with Personal Finance · __FOOTER__ · Page " counter(page) " / " counter(pages);
    font-size: 7.5pt; color: #777;
  }
}
html { -weasy-hyphens: none; }
body {
  font-family: "DejaVu Sans", "Noto Sans", "Noto Sans CJK SC", sans-serif;
  font-size: 9.8pt; line-height: 1.5; color: #111; margin: 0;
}
h1:first-of-type { font-size: 15pt; text-align: center; margin: 0 0 12pt; }
h1 {
  font-size: 12pt; margin: 14pt 0 8pt; padding-bottom: 3pt;
  border-bottom: 0.9pt solid #333; break-after: avoid;
}
h1.newpage { break-before: page; margin-top: 0; }
h2 { font-size: 10.5pt; margin: 12pt 0 5pt; break-after: avoid; }
p { margin: 0 0 3pt; }
ul { margin: 0 0 6pt; padding-left: 1.1em; }
li { margin: 0 0 2.5pt; }
em { color: #444; }
/* Section A：题干与选项 */
div.qblock { break-inside: avoid; margin: 0 0 19pt; }
p.q { margin: 0 0 4pt; }
p.opt { margin: 0 0 2pt 17pt; text-indent: -17pt; }
span.circ { font-size: 1.4em; line-height: 0.8; }
/* 答题横线：无底色，行距 = 单倍 ×2 */
div.rules { margin: 6pt 0 10pt; }
div.rule { height: __RULE__mm; border-bottom: 0.6pt solid #999; }
/* 示例表格 */
table { border-collapse: collapse; width: 100%; font-size: 9pt; margin: 4pt 0 8pt; }
th, td { border: 0.5pt solid #bbb; padding: 3pt 5pt; text-align: left; vertical-align: top; }
th { background: #f2f2f2; }
hr { border: none; border-top: 0.6pt solid #ccc; margin: 10pt 0; }
blockquote {
  margin: 0 0 10pt; padding: 3pt 0 3pt 9pt;
  border-left: 1.6pt solid #999; color: #333; font-size: 9pt;
}
blockquote p { margin: 0 0 2pt; }
code { font-family: "DejaVu Sans Mono", monospace; }
"""


def css(footer: str) -> str:
    return (
        CSS_TEMPLATE
        .replace("__FOOTER__", footer)
        .replace("__RULE__", f"{RULE_HEIGHT_MM:g}")
    )


def build_html(md: str, teacher_mark: str = TEACHER_MARK) -> str:
    """Markdown 正文 -> 打印用 HTML 片段。"""
    # 1) 教师专用说明不进学生卷
    md = md.split(teacher_mark)[0]
    md = re.sub(r"\n-{3,}\s*$", "\n", md)

    # 2a) 分页符前的 --- 横线在打印卷上多余，去掉
    md = re.sub(r'(?m)^-{3,}[ \t]*\n+(?=<div class="page-break"></div>)', "", md)

    # 2) ```answer2x / ```answer -> 打印用横线
    def rules(m: re.Match[str]) -> str:
        rows = [ln for ln in m.group(1).splitlines() if ln.strip().startswith("_")]
        body = "".join('<div class="rule"></div>' for _ in rows) or '<div class="rule"></div>'
        return f'\n<div class="rules">\n{body}\n</div>\n'

    md = re.sub(r"```answer2x\n(.*?)```", rules, md, flags=re.S)
    md = re.sub(r"```answer\n(.*?)```", rules, md, flags=re.S)

    # 3) 每个 Qn / Bn / Cn 连同它的答题横线包一层，避免题干和答题区被分页切开
    out: list[str] = []
    open_block = False
    for line in md.split("\n"):
        starts_q = bool(re.match(r"\*\*(?:Q|B|C)\d+\.\*\*", line))
        closes = (
            starts_q
            or line.startswith("# SECTION")
            or line.startswith("---")
            or 'class="page-break"' in line
        )
        if closes and open_block:
            out += ["", "</div>", ""]
            open_block = False
        if starts_q:
            out += ['<div class="qblock">', ""]
            open_block = True
        out.append(line)
    if open_block:
        out += ["", "</div>", ""]
    md = "\n".join(out)

    # 4) Markdown -> HTML
    proc = subprocess.run(
        ["pandoc", "-f", "markdown+raw_html", "-t", "html5"],
        input=md, capture_output=True, text=True, check=True,
    )
    html = proc.stdout

    # 5) 打印细节：圆圈放大、Section B/C 分页、选项悬挂缩进
    html = re.sub(r"◯", '<span class="circ">◯</span>', html)
    html = re.sub(r"●", '<span class="circ">●</span>', html)
    html = re.sub(r'<p>(<span class="circ">)', r'<p class="opt">\1', html)
    html = re.sub(r"<p><strong>((?:Q|B|C)\d+\.)</strong>", r'<p class="q"><strong>\1</strong>', html)
    html = re.sub(r'<div class="page-break"></div>\s*', "", html)
    html = re.sub(
        r"<h1([^>]*)>(\s*SECTION [BC])", r'<h1 class="newpage"\1>\2', html
    )
    return html


def build_doc(
    md: str,
    footer: str = "Mid-Term Exam",
    teacher_mark: str = TEACHER_MARK,
    extra_css: str = "",
    title: str = "Mid-Term Exam — Sections A + B + C",
) -> str:
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{title}</title>
<style>{css(footer)}{extra_css}</style></head>
<body>
{build_html(md, teacher_mark)}
</body></html>
"""


def weasyprint_cmd() -> list[str]:
    cmd = ["uv", "run", "--with", "weasyprint", "weasyprint"]
    local = shutil.which("weasyprint")
    if local:
        try:
            subprocess.run([local, "--version"], capture_output=True, check=True, timeout=60)
            cmd = [local]
        except (subprocess.CalledProcessError, OSError):
            pass  # 本地这个是坏的（模块缺失），改用 uv
    return cmd


def render_pdf(
    md: str,
    out: Path,
    footer: str = "Mid-Term Exam",
    teacher_mark: str = TEACHER_MARK,
    extra_css: str = "",
    title: str = "Mid-Term Exam — Sections A + B + C",
) -> Path:
    html_path = Path(tempfile.gettempdir()) / (out.stem.replace(" ", "_") + ".html")
    doc = build_doc(md, footer, teacher_mark, extra_css, title)
    html_path.write_text(doc, encoding="utf-8")
    subprocess.run(weasyprint_cmd() + [str(html_path), str(out)], check=True)
    return out


def prepend_cover(pdf: Path, cover: Path = COVER) -> Path:
    """把封面 PDF 的页面插到 pdf 最前面（页码仍从正文第 1 页算起）。"""
    if not cover.exists():
        print(f"未找到封面，跳过: {cover}")
        return pdf
    tmp = pdf.with_name(pdf.stem + ".merged.pdf")
    code = (
        "import sys\n"
        "from pypdf import PdfReader, PdfWriter\n"
        "w = PdfWriter()\n"
        "for path in sys.argv[1:3]:\n"
        "    for page in PdfReader(path).pages:\n"
        "        w.add_page(page)\n"
        "with open(sys.argv[3], 'wb') as f:\n"
        "    w.write(f)\n"
    )
    subprocess.run(
        ["uv", "run", "--with", "pypdf", "python", "-c", code, str(cover), str(pdf), str(tmp)],
        check=True,
    )
    tmp.replace(pdf)
    return pdf


def main() -> int:
    if not SRC.exists():
        print(f"找不到源文件: {SRC}")
        return 1
    if not shutil.which("pandoc"):
        print("需要 pandoc")
        return 1
    render_pdf(SRC.read_text(encoding="utf-8"), OUT)
    if "--cover" in sys.argv[1:]:
        prepend_cover(OUT)
    print(f"已生成: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
