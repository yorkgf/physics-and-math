# Global Money Notes #25: Design Options for an o/n Repo Facility
**Zoltan Pozsar**  
**Date**: September 9, 2019  
**Credit Suisse**

---

## 核心命题

> While we don't think the Fed will launch a standing repo facility anytime soon, in this edition of Global Money Notes we explain the optimal design features of such a facility. Our target audience is central bankers and STIR traders, but macro and bank equity investors are encouraged to read our report as well.

> The fundamental problem the Fed will soon have to reckon with is that it has an operating framework where the target range for the o/n rates complex is policed only at the bottom – with an o/n reverse repo facility – but not at the top. The solution is an o/n repo facility priced 25 bps over the o/n reverse repo rate that's open without stigma to large global banks, with the explicit aim to make collateral and reserves equal – the "equalizer bazooka".

---

## 核心洞见：repo市场天生就是分层hierarchy

repo市场不是一个统一市场，它天生就是分层的，不同参与者交易在不同层级，价格严格分层：

### 从现金出借人角度：

| 层级 | 参与者 | 利率 | 价差 |
|------|------------|------|------|
| 1 | 货币基金 (non-FICC) | o/n RRP | +0bps |
| 2 | 三方repo | o/n RRP + 5bps | +5bps |
| 3 | 对冲基金 (non-FICC) | 三方repo + 5bps → GCU | +5+5bps = +10bps |
| 4 | FICC非成员抵押品提供者 → 清算行提供clearing | 普通GC + 5bps | +10+5bps = +15bps |
| 5 | FICC成员抵押品提供者 | 普通GC → cleared GC | +15+5bps = +20bps |

> 价格从低到高，层级分明，每个层级价差5bps，这就是repo市场的**hierarchy**。

---

## 失衡与backstop

失衡分两种：

1. **Excess Reserves（准备金过剩）**：
   - 太多准备金，太少抵押品
   - 谁来吸收？→ **美联储o/n RRP工具**，在target range底部兜底
   - 这就是我们已经有了的floor

2. **Excess Collateral（抵押品过剩）**：
   - 太多抵押品，太少准备金
   - 谁来吸收？→ **美联储o/n RP工具**，在target range顶部兜底
   - 这就是我们现在需要的ceiling

> 现在美联储只有floor，没有ceiling → 这就是问题所在。当抵押品过剩，隔夜利率会冲破top of target range，美联储失去控制。

---

## 三种设计方案

### Design #1：对所有FICC成员开放

- 任何FICC成员都可以来美联储做repo，换取准备金
- 价格：o/n RRP + 25bps → 正好在target range顶部
- 问题：
  - 道德风险：hedge fund也能直接来借，不合适
  - 法律问题：美联储不愿意给non-bank做

### Design #2：只对一级交易商开放

- 历史上TOMOs就是只对一级交易商开放，有经验
- 问题：
  - 公平性问题：一级交易商才有access，非一级交易商（银行）没有
  - 一级交易商有些不需要满足巴塞尔III，存在公平性问题

### Design #3：**只对大型银行（G-SIBs）开放** → Pozsar认为这是最优设计

- 只对G-SIBs开放，因为本来就是G-SIBs吸收了大部分过剩抵押品，它们也需要额外准备金满足日内流动性要求
- 价格：o/n RRP + 25bps → ceiling
- 优势：
  - 没有道德风险
  - 没有公平性问题
  - 符合监管逻辑：只有G-SIBs面临巴塞尔III约束，本来就需要它们吸收抵押品，央行给它们提供daily liquidity backstop
  - 叫**"equalizer bazooka"** → 让抵押品=准备金，两者可以互换，解除银行日内流动性约束

> "Such a facility would have a "Draghi-esque" quality to it... it wouldn't have to be used to have an impact."

仅仅宣布存在它，就能让市场放心，银行就愿意释放闲置准备金，实际上不一定需要使用。**存在就是力量，不用也有作用**。

---

## 为什么这最优

- 解决了问题：抵押品过剩时，提供流动性天花板，保证隔夜利率一直在目标区间内
- 不会过度扩张美联储资产负债表：正常情况下不需要使用，只有压力大的时候才会用
- 解除了银行预防性持有准备金的需求，可以释放出约**$5000亿**闲置准备金自由流通
- 改善repo市场流动性，压缩cross-currency basis，解决全球美元短缺问题

> If we get such a facility, the trade is to receive cross-currency bases → 基差会从负往正走，收益率曲线会陡峭化。

---

## 最终结论

美联储现在只floor（RRP）没有ceiling（repo facility），需要补上ceiling。最优设计是：

- 价格：o/n RRP + 25bps → 正好在target range顶部
- 开放对象：**只有G-SIBs**
- 目的：equalize collateral and reserves → 让两者完全可互换

这种设计解决了道德风险、公平性问题，也符合巴塞尔III后的监管结构。

---

## 相关链接

- 上一篇：[[Global Money Notes #24 - Sagittarius A*]]
- 下一篇：[[Global Money Notes #26 - Countdown to QE4?]]
- 概念链接：
  - [[Standing Repo Facility]]
  - [[Equalizer Bazooka]]
  - [[Hierarchy of the Repo Market]]

---

**原始位置**: `zoltan-pozsar-global-money-notes.pdf`
