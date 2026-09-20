---
tags: [学习, 进度追踪, 计算机系统, CSAPP]
科目: CSAPP 深入理解计算机系统
平台: B站
状态: ⚪ 未开始
progress: 0
total: 23
created: 2026-09-20
updated: 2026-09-20
上次学到:
下次起点: P1 L01b.01 how_program_run - overview
教程: Dr.Dng陪跑CSAPP bigONE《深入理解计算机系统》
链接: https://www.bilibili.com/video/BV1hf4y1P7qW/
---

# 💻 CSAPP《深入理解计算机系统》— Dr.Dng 陪跑

> UP：清华邓博士 · 共 **23 P** · 总时长约 **33.7 小时**
> 蓝本：CMU B&H *CSAPP*（豆瓣 9.8），融合 UCB / MIT / ETHZ 名校内容补齐硬件与体系结构
> 播放列表：[BV1hf4y1P7qW](https://www.bilibili.com/video/BV1hf4y1P7qW/)

---

## 🔖 快速定位

| 项目 | 内容 |
| --- | --- |
| **当前状态** | ⚪ 未开始 |
| **总进度** | **0 / 23 P** |
| **📍 下次从这里开始** | **P1 L01b.01 how_program_run - overview** |
| **⏱ 上次学习日期** | — |
| **预计总时长** | 约 33.7 小时（含大量长视频，建议按块推进） |

> 💡 每次学完更新「下次从这里开始」+ 下表打勾。

---

## 🗺 课程结构（按主题分块）

课程前半偏「程序如何跑起来 + C 语言基础」，后半进入 CSAPP 经典章节（位/浮点/汇编）。

### 块一：How Program Runs（链接与加载，P1–P7）

> 程序从源码到运行的完整链路：编译、链接、符号解析、重定位、动态链接。

| # | 讲次 | 时长 | 状态 |
| --- | --- | --- | --- |
| 1 | L01b.01 how_program_run - overview | 59:38 | ⬜ |
| 2 | L01b.02 how_program_run - riscv simulation | 34:38 | ⬜ |
| 3 | L01b.03 how_program_run - ELF format | 105:20 | ⬜ |
| 4 | L01b.04 how_program_run - symbol resolution | 94:42 | ⬜ |
| 5 | L01b.05 how_program_run - link & symbol relocation | 105:20 | ⬜ |
| 6 | L01b.06 how_program_run - dynamic link | 121:48 | ⬜ |
| 7 | [BOOK:CSAPP:7] linking | 159:45 | ⬜ |

### 块二：C Intro（C 语言精讲，P8–P15）

| # | 讲次 | 时长 | 状态 |
| --- | --- | --- | --- |
| 8 | L01c.03 C_intro - basic syntax | 87:54 | ⬜ |
| 9 | L01c.01 C_intro - num repr | 81:34 | ⬜ |
| 10 | L01c.02 C_intro - float repr | 66:33 | ⬜ |
| 11 | L01c.04 C_intro - pointer | 91:57 | ⬜ |
| 12 | L01c.05 C_intro - the lost art of struct packing | 99:43 | ⬜ |
| 13 | L01c.06 C_intro - memory fault | 88:11 | ⬜ |
| 14 | L01c.07 C_intro - malloc principle | 75:23 | ⬜ |
| 15 | [BOOK:CSAPP:9.9] dynamic memory allocation | 83:43 | ⬜ |

### 块三：CSAPP 核心章节（位 / 浮点 / 汇编，P16–P23）

| # | 讲次 | 时长 | 状态 | CSAPP 章节 |
| --- | --- | --- | --- | --- |
| 16 | L02 bits bytes integers | 56:53 | ⬜ | Ch 2.1–2.3 |
| 17 | L03 bits bytes integers 2 | 86:17 | ⬜ | Ch 2.3 |
| 18 | L04 floating point | 72:26 | ⬜ | Ch 2.4 |
| 19 | L05 machine level programming 1 - basics | 75:24 | ⬜ | Ch 3.1–3.4 |
| 20 | L06 machine level programming 2 - control | 89:15 | ⬜ | Ch 3.6 |
| 21 | L07 machine level programming 3 - procedures | 103:07 | ⬜ | Ch 3.7 |
| 22 | L08 machine level programming 4 - data | 122:23 | ⬜ | Ch 3.8–3.9 |
| 23 | L09b.01 intro to riscv by krste 2020 | 61:59 | ⬜ | RISC-V 补充 |

**状态**：⬜ 未看 · ⏳ 进行中 · ✅ 已看完

---

## ✍️ 实验 / 练习进度

> CSAPP 学习**必须动手**，推荐配合官方 Labs（需在指定机器上运行）。

| # | 实验 / 练习 | 状态 | 完成日期 | 备注 |
| --- | --- | --- | --- | --- |
| 1 | 手写/跟踪一个简单程序的编译链接过程（`gcc -c` + `ld` + `readelf`） | ⬜ 未做 | | 对应 P1–P7 链接部分 |
| 2 | C 语言基础练习（语法/指针/struct packing 复现） | ⬜ 未做 | | 对应 P8–P14 |
| 3 | 自己实现一个简易 malloc | ⬜ 未做 | | 对应 P14–P15，经典难题 |
| 4 | **Data Lab**（位运算/补码/浮点） | ⬜ 未做 | | 对应 P16–P18，CSAPP 官方 Lab |
| 5 | **Bomb Lab**（汇编逆向拆炸弹） | ⬜ 未做 | | 对应 P19–P22，最经典 Lab |
| 6 | **Attack Lab**（缓冲区溢出） | ⬜ 未做 | | 对应 P19–P22 |
| 7 | 读 *CSAPP* 原书对应章节 | ⬜ 未做 | | 教材：Bryant & O'Hallaron |

**状态**：⬜ 未做 · 🔵 进行中 · ✅ 已完成 · 🔁 需重做

---

## 📝 学习日志

> 每次学完追加一条，倒序（最新在最上面）。

### 2026-09-20 —— 开始学习

- **学了**：
- **懂了**：
- **卡住**：
- **下次开始**：P1 L01b.01 how_program_run - overview

---

## ❗ 本课易忘点 / 错题

| 日期 | 知识点 | 我的问题 | 复习后是否掌握 |
| --- | --- | --- | --- |
| | | | ⬜ |

---

## 🗂 关联笔记

- [[学习进度/学习进度总览]]
- [[]]
