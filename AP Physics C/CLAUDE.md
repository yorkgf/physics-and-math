# AP Physics C Obsidian Vault — 项目规范

## 文件夹结构

```
AP Physics C/
├── Question Review/
│   ├── 题库/          ← 所有题目文件（QQ01-QQ20, FE01-FE30, ...）
│   ├── Student Analysis.md       ← 全体学生分析（唯一一份）
│   ├── Quarter Quiz Mar 31 Analysis.md
│   └── Final Exam Jan 20 Analysis.md
└── Examples/          ← 例题文件
```

## 题目文件命名规范

- **所有题目统一放在 `题库/` 文件夹**，不按考试分子文件夹
- 命名格式：`{前缀}{两位数字}.md`
  - Quarter Quiz: `QQ01`, `QQ02`, ... `QQ20`
  - Final Exam: `FE01`, `FE02`, ... `FE30`
  - 新考试依此类推（如 Midterm → `MT01` 等）

## 题目文件内容格式

每个题目文件包含：
1. **Answer Key**（正确答案）
2. **Student Responses**（学生答题表格）
3. **Analysis**（题目分析，含正确率）
4. **Key Concepts**（涉及知识点）
5. **Metadata**（含 `id` 字段）

## Wiki 链接规范（重要！）

**在 Markdown 表格中使用双链时，禁止使用带显示文本的格式 `[[file|alias]]`**，因为 `|` 与表格分隔符冲突。

✅ 正确：`[[题库/QQ06]]`
❌ 错误：`[[题库/QQ06|Q6]]`（表格中会破坏格式）

- 题目文件使用短 ID 命名，就是为了让链接可以直接用 `[[题库/QQ06]]` 而不需要显示文本

## 学生分析文件规范

**唯一一份**：`Student Analysis.md`

### 表格格式
- **列** = 各次考试（如 Quarter Quiz Mar 31、Final Exam Jan 20）
- **行** = 知识点
- 同一知识点在不同考试中出错，显示在同一行
- 题号用双链：`[[题库/QQ06]]`、`[[题库/FE02]]`

### 包含内容
1. 每位学生的知识点错误表格
2. 每位学生的薄弱环节总结
3. 全班共性难点汇总（按两次考试对比）
4. 教学建议（含推荐例题链接，如 `[[Examples/Example 5 - Atwood Machine with Leaking Bucket]]`）
5. 重点关注学生列表

## 考试概览文件规范

每次考试一份单独文件（如 `Quarter Quiz Mar 31 Analysis.md`），包含：
1. 班级成绩汇总表
2. 全班薄弱点排名（含题目链接）
3. 每位学生的个人建议
4. 教学建议（含推荐例题链接）
5. 题库问题列表

## 当前考试记录

| 考试 | 文件前缀 | 题目数 | 日期 |
|------|----------|--------|------|
| Quarter Quiz | QQ | 20 | 2026-03-31 |
| Final Exam | FE | 30 | 2026-01-20 |
