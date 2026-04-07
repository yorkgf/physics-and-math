# AP CSA Obsidian Vault — 项目规范

## 文件夹结构

```
AP CSA/
├── Question Review/
│   ├── 题库/          ← 所有题目文件（QA01-QA25, ...）
│   ├── Student Analysis.md       ← 全体学生分析（唯一一份）
│   └── Quarter Quiz Apr 1 Analysis.md
```

## 题目文件命名规范

- **所有题目统一放在 `题库/` 文件夹**，不按考试分子文件夹
- 命名格式：`{前缀}{两位数字}.md`
  - Quarter Quiz April 1: `QA01`–`QA25`
  - 新考试依此类推（如 May Quiz → `QM01` 等）

## 题目文件内容格式

每个题目文件包含：
1. **Question**（题目描述）
2. **Answer Key**（正确答案与解释）
3. **Student Responses**（学生答题表格 + 正确率）
4. **Key Concepts**（涉及知识点）
5. **Metadata** frontmatter（id, exam, topic, correct_answer）

## Wiki 链接规范（重要！）

**在 Markdown 表格中使用双链时，禁止使用带显示文本的格式 `[[file|alias]]`**，因为 `|` 与表格分隔符冲突。

✅ 正确：`[[题库/QA23]]`
❌ 错误：`[[题库/QA23|Q23]]`（表格中会破坏格式）

## 学生分析文件规范

**唯一一份**：`Student Analysis.md`

### 表格格式
- **列** = 各次考试（如 Quarter Quiz Apr 1）
- **行** = 知识点
- 同一知识点在不同考试中出错，显示在同一行
- 题号用双链：`[[题库/QA23]]`

### 包含内容
1. 每位学生的知识点错误表格
2. 每位学生的薄弱环节总结
3. 全班共性难点汇总
4. 教学建议
5. 重点关注学生列表

## 当前考试记录

| 考试 | 文件前缀 | 题目数 | 日期 |
|------|----------|--------|------|
| Quarter Quiz April 1 | QA | 25 | 2026-04-01 |

## AP CSA 知识点分类

- 变量类型/数据类型
- OOP（类、构造函数、属性vs行为）
- 字符串（substring, indexOf, length）
- 数学方法（Math.random, Math.abs）
- Scanner/文件I/O
- 循环（for, while, nested）
- 数组（1D, 2D）
- ArrayList（add, remove, set, get）
- 递归（追踪、调试、base case）
- 排序算法（归并排序、选择排序）
- 二分查找
- 数据分析概念
