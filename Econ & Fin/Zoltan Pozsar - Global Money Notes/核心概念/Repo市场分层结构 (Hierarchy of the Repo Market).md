# Repo市场分层结构 (Hierarchy of the Repo Market)

## 核心命题

Post-Basel III，repo市场不是一个统一市场，它天生就是分层的，不同参与者在不同层级，价格严格分层，每层价差约5bps。

---

## 分层结构（从现金出借人角度）

| 层级 | 参与者 | 利率基点（相对于o/n RRP） |
|------|------------|--------------------------|
| 1 | 货币基金（non-FICC） | +0 bps → o/n RRP |
| 2 | 三方repo | +5 bps → 三方repo利率 |
| 3 | 对冲基金（non-FICC） | +10 bps → 普通GC repo |
| 4 | FICC成员清算 | +15 bps → 清算后GC repo |
| 5 | FICC成员抵押品借款人 | +20 bps → 清算GC repo对借款人 |

每层比下一层便宜大约5bps，分层严格，这就是repo市场的hierarchy。

> [[FICC (Fixed Income Clearing Corporation)]]

---

## 为什么分层重要

- 只有理解分层，才能理解失衡如何传导，谁在最后兜底
- 失衡分两种：准备金过剩抵押品不足 vs 抵押品过剩准备金不足
- 不同失衡对应不同兜底机构：
  - 准备金过剩 → 美联储RRP兜底（floor）
  - 抵押品过剩 → 美联储repo facility兜底（ceiling）

> [[Global Money Notes #25 - Design Options for an o/n Repo Facility]]

---

## 相关链接

- [[Standing Repo Facility]]
- [[Equalizer Bazooka]]

---

*Zoltan Pozsar, 2019*
