#!/usr/bin/env python3
"""Generate three shuffled exam papers (A / B / C) from the master note.

    cd "AP Business with Personal Finance/Mid-Term Exam"
    python3 build_exam_variants.py              # 自动拼上 Cover.pdf
    python3 build_exam_variants.py --no-cover   # 不要封面

每份卷与母卷的区别只在 Section A（选择题）：
  * 30 道题的**题目顺序**完全随机（固定随机种子，可复现，且会检查不出现按单元成段排列）
  * 每题的 4 个**选项顺序**各自随机，再重新标 A–D
Section B / C（简答与案例题）三份完全相同。
页脚分别注明 A卷 / B卷 / C卷；每份 md 末尾的教师区附本卷答案。
"""

from __future__ import annotations

import random
import re
import sys
from pathlib import Path

import build_exam_pdf as base

HERE = base.HERE
SRC = base.SRC
KEY_MD = HERE / "Mid-Term Exam Answer Key.md"
SECTION_A = re.compile(r"(?m)^# SECTION A — MULTIPLE CHOICE \(45 points\)\s*$")
LETTERS = "ABCD"

# 固定种子：想重排就改这里（同一个种子永远得到同一份卷）
# 每个种子占用互不重叠的 1000 号段，保证三份卷的排列一定不同
SEEDS = {"A": 1_000_000, "B": 2_000_000, "C": 3_000_000}


# ---------------------------------------------------------------- 解析母卷
def split_paper(md: str) -> tuple[str, str, str]:
    m = SECTION_A.search(md)
    if not m:
        raise SystemExit("找不到 SECTION A 标题")
    head = md[: m.end()]
    rest = md[m.end():]
    k = rest.index('<div class="page-break"></div>')
    return head, rest[:k], rest[k:]


def parse_questions(body: str) -> list[dict]:
    questions = []
    for chunk in re.split(r"(?m)^(?=\*\*Q\d+\.\*\*)", body):
        if not chunk.strip():
            continue
        lines = chunk.split("\n")
        qm = re.match(r"\*\*Q(\d+)\.\*\*(.*)", lines[0])
        if not qm:
            continue
        opts = re.findall(r"(?m)^◯ ([A-D])\. (.*)$", chunk)
        if len(opts) != 4:
            raise SystemExit(f"Q{qm.group(1)} 选项数不是 4：{len(opts)}")
        questions.append(
            {"no": int(qm.group(1)), "stem": qm.group(2).strip(), "opts": dict(opts)}
        )
    if len(questions) != 30:
        raise SystemExit(f"解析到 {len(questions)} 道题，预期 30")
    return questions


def parse_answer_key() -> dict[int, dict]:
    """从答案 key md 读取 Q -> {ans, topic, concept}（表格两栏并排）。"""
    key: dict[int, dict] = {}
    for line in KEY_MD.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 8 or not cells[0].isdigit():
            continue
        for q, ans, topic, concept in (cells[:4], cells[4:]):
            if q.isdigit() and ans in LETTERS:
                key[int(q)] = {"ans": ans, "topic": topic, "concept": concept}
    if len(key) != 30:
        raise SystemExit(f"答案 key 解析到 {len(key)} 条，预期 30")
    return key


# ---------------------------------------------------------------- 打乱
def mixed_order(questions: list[dict], key: dict[int, dict], seed: int) -> list[dict]:
    """随机排列题目，并要求同单元（topic）不出现连续 3 题以上。"""
    for s in range(seed, seed + 1000):
        rng = random.Random(s)
        order = questions[:]
        rng.shuffle(order)
        topics = [key[q["no"]]["topic"] for q in order]
        run = best = 1
        for a, b in zip(topics, topics[1:]):
            run = run + 1 if a == b else 1
            best = max(best, run)
        if best <= 2 and topics[0] != topics[1] and topics[-1] != topics[-2]:
            return order
    raise SystemExit("找不到足够打散的排列")


def shuffle_options(q: dict, rng: random.Random) -> tuple[list[tuple[str, str]], dict[str, str]]:
    """返回 (新选项列表[(新letter, 文本)], {原letter: 新letter})。"""
    perm = list(range(4))
    rng.shuffle(perm)                      # perm[pos] = 原选项下标
    originals = [q["opts"][L] for L in LETTERS]
    new_opts = [(LETTERS[pos], originals[i]) for pos, i in enumerate(perm)]
    new_letter = {LETTERS[i]: LETTERS[pos] for pos, i in enumerate(perm)}
    return new_opts, new_letter


def build_variant(questions, key, name: str, seed: int):
    rng = random.Random(seed + 777)
    order = mixed_order(questions, key, seed)

    chunks, rows, mapping = [], [], []
    for idx, q in enumerate(order, 1):
        new_opts, new_letter = shuffle_options(q, rng)
        chunk = f"**Q{idx}.** {q['stem']}\n\n" + "\n\n".join(
            f"◯ {L}. {text}" for L, text in new_opts
        )
        chunks.append(chunk)
        k = key[q["no"]]
        rows.append((idx, q["no"], new_letter[k["ans"]], k["topic"], k["concept"]))
        mapping.append((idx, q["no"], k["topic"]))

    body = "\n\n\n\n".join(chunks)
    return body, rows, mapping


def key_table(rows) -> str:
    out = ["| 卷内题号 | 原题号 | 答案 | Topic | 考点 |", "|---|---|---|---|---|"]
    out += [f"| {i} | Q{o} | **{a}** | {t} | {c} |" for i, o, a, t, c in rows]
    return "\n".join(out)


def main() -> int:
    md = SRC.read_text(encoding="utf-8")
    head, body_a, tail = split_paper(md)
    questions = parse_questions(body_a)
    key = parse_answer_key()

    combined = ["# Mid-Term Exam — Answer Keys (A / B / C 卷)", "",
                "> **教师用。** Section A 的题目顺序与选项顺序三卷各不相同；"
                "Section B / C 三份完全相同，答案见 [[Mid-Term Exam Answer Key]]。", ""]

    for name, seed in SEEDS.items():
        body, rows, mapping = build_variant(questions, key, name, seed)
        variant_md = (
            f"{head}\n\n{body}\n\n\n{tail.rstrip()}\n\n"
            f"## 卷 {name} 选择题答案（教师）\n\n{key_table(rows)}\n"
        )
        md_path = HERE / f"Mid-Term Exam ({name}卷).md"
        md_path.write_text(variant_md, encoding="utf-8")

        pdf_path = HERE / f"Mid-Term Exam ({name}卷).pdf"
        base.render_pdf(variant_md, pdf_path, footer=f"Mid-Term Exam · {name}卷")
        if "--no-cover" not in sys.argv[1:]:
            base.prepend_cover(pdf_path)   # Cover.pdf 作为封面（考前须知 + 诚信承诺）
        print(f"已生成: {md_path.name} + {pdf_path.name}")

        combined += [f"## 卷 {name}", "", key_table(rows), ""]
        seq = " → ".join(f"Q{i}({t})" for i, _, t in mapping[:10])
        print(f"   卷{name} 前 10 题 Topic 顺序: {seq} …")

    (HERE / "Mid-Term Exam Answer Key (A-B-C 卷).md").write_text(
        "\n".join(combined).rstrip() + "\n", encoding="utf-8"
    )
    print("已生成: Mid-Term Exam Answer Key (A-B-C 卷).md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
