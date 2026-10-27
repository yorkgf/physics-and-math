#!/usr/bin/env python3
"""Render the reading material sheet (Section C) to A4 PDF.

    cd "AP Business with Personal Finance/Mid-Term Exam"
    python3 build_case_pdf.py

* 丢掉文末「## 教师备注」（只发给学生）
* 正文字号略放大、行距放宽，方便学生现场 2 分钟读完
* 页脚：Patagonia Case · Section C · Reading Material · Page n / N
"""

from __future__ import annotations

import build_exam_pdf as base

STEM = "Mid_Term_AP Business and Personal Finance_Reading_Marterial_40_Copies"  # 由 Obsidian 导出时改名
SRC = base.HERE / f"{STEM}.md"
OUT = base.HERE / f"{STEM}.pdf"

EXTRA_CSS = """
body { font-size: 10.4pt; line-height: 1.62; }
h1:first-of-type { font-size: 16pt; margin-bottom: 4pt; }
h2 { font-size: 11.5pt; margin: 14pt 0 6pt; }
p { margin: 0 0 4pt; }
strong { color: #000; }
"""


def main() -> int:
    base.render_pdf(
        SRC.read_text(encoding="utf-8"),
        OUT,
        footer="Patagonia Case · Section C · Reading Material",
        teacher_mark="## 教师备注",
        extra_css=EXTRA_CSS,
        title="Patagonia Case — Section C Reading Material",
    )
    print(f"已生成: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
