#!/usr/bin/env python3
"""把 A / B / C 三份卷按 ABCABC… 循环拼成一个多份试卷的大 PDF（默认 40 份）。

    cd "AP Business with Personal Finance/Mid-Term Exam"
    python3 build_exam_batch.py                # 40 份：A B C A B C …
    python3 build_exam_batch.py --count 36     # 36 份（3 的整数倍 → 三卷等量）
    python3 build_exam_batch.py --order ABCA   # 自定义循环单元
    python3 build_exam_batch.py --no-pad       # 不在每份末尾补空白页

每份卷都带封面（Cover.pdf），发到考生手里的是一本完整小册子。
每份 15 页（奇数），默认在末尾补 1 页空白 → 每份 16 页，双面打印后
下一份正好从新纸的正面开始，不会和上一份印在同一张纸的两面。
"""

from __future__ import annotations

import argparse
import subprocess
from collections import Counter

import build_exam_pdf as base

SERIES = {
    "A": "Mid-Term Exam (A卷).pdf",
    "B": "Mid-Term Exam (B卷).pdf",
    "C": "Mid-Term Exam (C卷).pdf",
}
OUT = base.HERE / "Mid_Term_AP Business and Personal Finance_1_Copy.pdf"  # 导出后的文件名

MERGE_CODE = """
import sys
from pypdf import PdfReader, PdfWriter

letters, count, unit, out = sys.argv[1], int(sys.argv[2]), sys.argv[3], sys.argv[4]
pad_flag = sys.argv[5]
paths = dict(zip(letters, sys.argv[6:6 + len(letters)]))   # A卷/B卷/C卷 的路径
readers = {k: PdfReader(v) for k, v in paths.items()}

pad = pad_flag == "1"                       # 每份补成偶数页，双面打印后下一份从新纸正面开始
writer = PdfWriter()
for i in range(count):
    key = unit[i % len(unit)]
    reader = readers[key]
    for page in reader.pages:
        writer.add_page(page)
    if pad and len(reader.pages) % 2:
        box = reader.pages[0].mediabox
        writer.add_blank_page(width=float(box.width), height=float(box.height))

try:                      # 封面被复制 40 次，去重后文件小很多
    writer.compress_identical_objects(remove_identicals=True, remove_orphans=True)
except Exception as exc:  # 老版本 pypdf 没有这个方法
    print("skip compression:", exc)

with open(out, "wb") as f:
    writer.write(f)
print("ok")
"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--count", type=int, default=40, help="总份数（默认 40）")
    ap.add_argument("--order", default="ABC", help="循环单元（默认 ABC）")
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--no-pad", action="store_true",
                    help="不在每份末尾补空白页（默认补，便于双面打印后分份）")
    args = ap.parse_args()

    missing = [p for p in SERIES.values() if not (base.HERE / p).exists()]
    if missing:
        print(f"缺少试卷 PDF，请先运行 build_exam_variants.py: {missing}")
        return 1

    subprocess.run(
        ["uv", "run", "--with", "pypdf", "python", "-c", MERGE_CODE,
         "".join(SERIES), str(args.count), args.order, args.out,
         "0" if args.no_pad else "1",
         *[str(base.HERE / SERIES[k]) for k in SERIES]],
        check=True,
    )

    tally = Counter(args.order[i % len(args.order)] for i in range(args.count))
    detail = "、".join(f"{k} 卷 ×{n}" for k, n in sorted(tally.items()))
    per = 16 if not args.no_pad else 15
    print(f"已生成: {args.out}\n  {args.count} 份（{detail}），按 {args.order} 循环")
    print(f"  每份 {per} 页（15 页正文+封面{'，末尾补 1 页空白' if not args.no_pad else ''}）"
          f"→ 共 {args.count * per} 页 / {args.count * per // 2} 张纸（双面）")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
