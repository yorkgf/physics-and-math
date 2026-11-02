#!/usr/bin/env python3
"""Render "Review Case Of Unit 1" (Xibei practice case, Section C) into a single PDF.

    cd "AP Business with Personal Finance/Mid-Term Exam"
    python3 build_practice_case_pdf.py

输出：Review Case Of Unit 1.pdf
* 第 1 页：案例阅读材料
* 第 2 页：Section C 题目（无答题横线、无分值）
"""

from __future__ import annotations

import build_exam_pdf as base

STEM = "Review Case Of Unit 1"

EXTRA_CSS = """
body { font-size: 9.9pt; line-height: 1.5; word-break: keep-all; }
h1:first-of-type { font-size: 16pt; margin-bottom: 6pt; }
h2 { font-size: 11.5pt; margin: 12pt 0 6pt; }
p { margin: 0 0 4pt; }
li { margin: 0 0 4pt; }
"""


def main() -> int:
    src = base.HERE / f"{STEM}.md"
    out = base.HERE / f"{STEM}.pdf"
    if not src.exists():
        print(f"找不到源文件: {src}")
        return 1
    base.render_pdf(
        src.read_text(encoding="utf-8"),
        out,
        footer="Review Case Of Unit 1 · Section C · Xibei",
        teacher_mark="## 出题说明",   # 本文件无此段，不影响
        extra_css=EXTRA_CSS,
        title="Review Case Of Unit 1 — Xibei",
    )
    print(f"已生成: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())