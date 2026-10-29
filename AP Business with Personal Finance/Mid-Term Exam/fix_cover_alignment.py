#!/usr/bin/env python3
"""修正 Cover.pdf 第 1 页 "Instructions to students" 列表的左侧缩进不齐。

原文件由 Word/WPS 转出，同一份项目列表里混了两套缩进：
    • 单行项的文字从 x=77.64 开始（项目符号后 1 个空格）
    • 折行项的首行与续行从 x=94.8 开始（悬挂缩进 24pt）
    • "Special instructions" 下的红字项从 x=80.4 开始
于是每条列表文字的左边缘参差不齐（"No food or drink…" 与
"No cell phones/iPods…" 就是最明显的两条）。

本脚本按"整行"平移：同一行的所有文字块位移量相同，行内字距不变；
每行最左侧的文字统一落到 TARGET（77.64），与原本占多数的
"项目符号 + 1 个空格"写法一致。项目符号本身（x≈70.8）与小标题
（"Instructions to students:" 等，x=56.64）不动，续行也落在同一左边缘。
字体、颜色、字号、行距以及页面其余内容（含第 2 页中文）保持原样。

用法:
    uv run --with pypdf python fix_cover_alignment.py            # 修正 Cover.pdf（自动备份）
    uv run --with pypdf python fix_cover_alignment.py --dry-run  # 只显示每行将如何移动
"""

from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import DecodedStreamObject, NameObject

HERE = Path(__file__).resolve().parent
COVER = HERE / "Cover.pdf"
BACKUP = HERE / "Cover.original.pdf"

PAGE_INDEX = 0               # 只改第 1 页（英文考前须知）
TARGET = 77.64               # 目标左边缘
BULLET_X = (70.7, 71.1)      # 项目符号自身的 x（不动）
TEXT_MIN_X = 76.5            # 小于此值的文字是项目符号（不动）
HEADING_MAX_X = 60.0         # 行内出现这个 x 之前的文字 → 小标题行，整行不动
REGION_Y = (500.0, 745.0)    # "Instructions / Special instructions" 列表的 Tm y 区间

TM_RE = re.compile(rb"(0\.05 0 0 -0\.05 )(-?[\d.]+)( -?[\d.]+ Tm)")
BLOCK_RE = re.compile(rb"BT(.*?)ET", re.S)


def parse(data: bytes) -> list[dict]:
    """把内容流里的文字块拆出来：位置、y、x、原始片段。"""
    out = []
    for m in BLOCK_RE.finditer(data):
        body = m.group(1)
        tm = TM_RE.search(body)
        if not tm:
            continue
        out.append({
            "start": m.start(1),
            "end": m.end(1),
            "x": float(tm.group(2)),
            "y": round(float(re.search(rb"0\.05 0 0 -0\.05 -?[\d.]+ (-?[\d.]+) Tm", body).group(1)), 2),
            "x_span": tm.span(2),
            "body": body,
        })
    return out


def main() -> int:
    dry = "--dry-run" in sys.argv[1:]
    reader = PdfReader(str(COVER))
    page = reader.pages[PAGE_INDEX]
    data = page.get_contents().get_data()
    blocks = parse(data)

    # 按 y 分行（同一基线的文字块视为同一行）
    lines: dict[float, list[dict]] = {}
    for b in blocks:
        if REGION_Y[0] < b["y"] < REGION_Y[1]:
            lines.setdefault(b["y"], []).append(b)

    print(f"{COVER.name} 第 {PAGE_INDEX + 1} 页 — 统一列表文字左边缘到 x={TARGET:.2f}")
    edits: list[tuple[int, int, bytes]] = []
    for y in sorted(lines, reverse=True):
        row = lines[y]
        if min(b["x"] for b in row) < HEADING_MAX_X:
            continue                                   # 小标题行（如 "Instructions to students:"）
        texts = [b for b in row if b["x"] > TEXT_MIN_X]
        if not texts:
            continue                                   # 只有小标题 / 只有项目符号
        left = min(b["x"] for b in texts)
        delta = TARGET - left
        if abs(delta) < 0.01:
            continue
        print(f"  y={y:7.2f}  左边缘 {left:7.2f} -> {TARGET:.2f} (Δ {delta:+.2f})，{len(texts)} 段文字")
        for b in texts:
            new_x = b["x"] + delta
            edits.append((b["start"] + b["x_span"][0],
                          b["start"] + b["x_span"][1],
                          f"{new_x:.3f}".encode()))

    if not edits:
        print("无需修改（左边缘已对齐）")
        return 0
    if dry:
        print("--dry-run：未写文件")
        return 0

    new_data = data
    for start, end, repl in sorted(edits, reverse=True):   # 从后往前改，偏移量不失效
        new_data = new_data[:start] + repl + new_data[end:]

    if not BACKUP.exists():
        shutil.copy2(COVER, BACKUP)
        print(f"原文件已备份: {BACKUP.name}")

    stream = DecodedStreamObject()
    stream.set_data(new_data)
    page[NameObject("/Contents")] = stream

    tmp = COVER.with_name(COVER.stem + ".fixed.pdf")
    writer = PdfWriter()
    writer.append(reader)
    writer.pages[PAGE_INDEX].compress_content_streams(9)   # 重新压缩，保持文件体积
    with open(tmp, "wb") as f:
        writer.write(f)
    tmp.replace(COVER)
    print(f"已写回: {COVER.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
