# Global Money Notes #18: Fed Funds and the Market for Intraday Liquidity
**Zoltan Pozsar**  
**Date**: October 26, 2018  
**Credit Suisse**

---

## 核心命题

> Our overnight monitors have been missing a brand new interbank market – a market that trades **10 basis points (bps) above IOR and 5 bps outside the Fed’s target range** for the o/n fed funds (FF) rate. The new market is a market for **intraday liquidity** and it exists between U.S. G-SIBs and the FHLB system, and its instrument is **interest bearing deposit accounts (IBDAs)**.

> A growing demand for o/n FF, coupled with the growth of IBDAs that are set to decimate the supply of o/n FF from the FHLBs, suggests an increase in the daily volatility of the o/n FF rate from here, the potential for o/n FF to spike as much as 50 bps on month-ends and the risk that o/n FF jumps outside the target band one day and then never looks back.

---

## 背景：演变的三方博弈

三个阶段的演变：

1. **第一阶段：套利（Arbitrage）**
   - o/n FF 交易由外国银行套利 IOR 驱动
   - 外国银行有自由资产负债表空间，不受流动性约束限制
   - 核心逻辑：套利 IOR - FF 利差

2. **第二阶段：LCR报表粉饰（LCR window dressing）**
   - 区域性银行受月末流动性约束
   - 开始在月末借 o/n FF 来提升期末 LCR 指标
   - 核心逻辑：改善监管报表

3. **第三阶段：日内流动性需求（Intraday Resolution Liquidity）**
   - 美国G-SIBs受**处置流动性要求**约束
   - 这是更高层级的流动性要求
   - 开始通过 IBDAs 从 FHLBs 借资金锁定整天准备金来满足日内流动性要求
   - 新市场诞生，利率在 IOR + 8-10bps 交易

> [[LCR (流动性覆盖率)]]
> [[G-SIBs (全球系统重要性银行)]]
> [[IOER (超额准备金利率)]]

---

## IBDAs：运作机制

**Interest Bearing Deposit Accounts (IBDAs)** 是计息存款账户：

- FHLB 把钱存在 G-SIBs 的 IBDA 账户，整日锁定期
- G-SIBs 得到准备金，整天保持在账户，满足日内流动性要求
- IBDAs 比传统 o/n FF 更好：
  - 传统 o/n FF 清晨还款，FHLB 得在美联储零息账户放几个小时
  - IBDAs 整天计息，对 FHLB 更划算
  - G-SIBs 整天锁定准备金，满足日内流动性要求
- **双赢**

关键：IBDAs 交易在 **IOR 之上 8-10bps**，已经**超出美联储目标区间上限**！

> [[FHLBs (联邦住房贷款银行)]]

---

## 问题：需求增长 vs 供给收缩

- **需求在增长**：
  - 更多银行（外国银行 + 区域性银行 + G-SIBs）因为各种原因需要借 o/n FF
  - 套利需求 + LCR报表粉饰需求 + 日内流动性需求 → 需求越来越多元，总量增长

- **供给在收缩**：
  - FHLB 是 o/n FF 最大供给者
  - 现在 FHLB 越来越多地把钱放进 IBDAs 而不是传统 o/n FF
  - IBDAs 会**吃掉** o/n FF 供给
  - 传统 o/n FF 交易量已经跌破 $600亿，会继续降

---

## 结论：跳升风险（jump risk）真实存在

- o/n FF 波动率会上升
- 月末 spike 可能达到 50bps
- **跳升风险**：o/n FF 有一天跳出目标区间，就再也回不去了
- 解决方案：美联储提前结束缩表，推出固定价格全额分配隔夜回购工具
- 转换目标利率到 SOFR 不一定解决问题

**关键一句话：**

> "A growing demand for o/n FF, coupled with the growth of IBDAs that are set to decimate the supply of o/n FF from the FHLBs, suggests an increase in the daily volatility of the o/n FF rate from here, the potential for o/n FF to spike as much as 50 bps on month-ends and the risk that o/n FF jumps outside the target band one day and then never looks back."

---

## 相关链接

- 上一篇：[[Global Money Notes #17 - No More Dips]]
- 下一篇：[[Global Money Notes #19 - Libor-OIS: A Morbidity Review]]
- 概念链接：
  - [[日内流动性 (Intraday Liquidity)]]
  - [[处置流动性 (Resolution Liquidity)]]

---

**原始位置**: `zoltan-pozsar-global-money-notes.pdf` pages ...
