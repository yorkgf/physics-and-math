# Global Money Notes #22: Collateral Supply and o/n Rates
**Zoltan Pozsar**  
**Date**: May 31, 2019  
**Credit Suisse**

---

## 核心命题

> In this edition of Global Money Notes, we explain, in never-before-seen detail, the mechanics of intra-day Fed balance sheet operations. These mechanics show why reserves can be scarce enough on some days to create volatility and problems even after trillions of dollars in quantitative easing. We study the detail of how balance sheet reduction (colloquially referred to as "taper") has worked.

> Reserves are scarce... and this scarcity now feeds through to daily volatility in the o/n fed funds rate. The volatility of the o/n FF rate is driven by the supply of Treasury collateral and some banks' increased reliance on daylight overdrafts on settlement days. The flipside of daylight overdrafts are temporary daylight reserves which banks have to pay back to the Fed everyday by sunset, and these payments are funded by borrowing "permanent" reserves during the day through the o/n FF market.

---

## 核心框架：taper的日内流动机制

Pozsar这篇论文级报告详细拆解了美联储缩表如何影响日内流动性和隔夜利率，是**货币市场微观结构**分析的经典。

### 谁来清算一级承销商？

一级承销商（primary dealers）不是银行，不能直接在美联储开户，必须通过**Bank of New York (BoNY)** 清算：

- 一级承销商在BoNY有清算账户
- BoNY在美联储有清算账户
- 承销商承销新发国债，每日清算都离不开BoNY

### 四个情景，谁最终持有国债？

| 情景 | 最终买家 | 对储备/回购的影响 |
|--------|------------|-------------------|
| **Scenario 1** | 非银行买家 | 储备减少，不需要一级承销商回购融资 |
| **Scenario 2** | 银行买家 | 储备减少，不需要额外融资 |
| **Scenario 3** | 一级承销商自己持有（买家罢工） | 储备不变，inventory增加，需要repo融资 |
| **Scenario 4** | 一级承销商持有，通过repo向银行融资 | 储备减少，dealer inventory增加，**o/n repo需求增加** |

当**曲线inversion**，最终买家罢工，越来越多国债落入情景4 → repo需求持续增加 → 利率上行压力。

> [[曲线 inversion]]
> [[Global Money Notes #20 - Lost in Transmission]]

---

## 关键：日内流动性和RLAP

### LCR vs RLAP

- **LCR**：覆盖**日末**流动性要求，只看日末快照
- **RLAP (Resolution Liquidity and Planning)**：覆盖**日内**峰值流动性要求，G-SIBs必须预先持有足够准备金应对日内流出

因此：
- RLAP比LCR要求**更多**准备金
- 缩表在破坏储备供给 → 储备越来越稀缺 → 日内流动性越来越紧张

> [[日内流动性 (Intraday Liquidity)]]
> [[G-SIBs (全球系统重要性银行)]]

### 日内透支如何传导到隔夜利率

流程：

1. 新发国债拍卖 → 一级承销商必须承接 → 清算账户需要支出 → 如果账户余额不够，**BoNY必须提供日内透支**
2. BoNY在美联储也需要透支 → 日内美联储提供透支
3. 日落之前，BoNY必须还给美联储 → 所以BoNY必须在**o/n FF市场**借入准备金
4. 如果所有银行储备都已经被RLAP占满，没人能贷 → BoNY必须更激进竞价 → o/n FF利率跳升

因此，**抵押品供给增加 → 透支增加 → 竞价 → 利率走高**。

> [[Daylight Overdrafts (日内透支)]]

---

## 关键数据：自由浮动储备已经接近零

Pozsar计算了"free float of reserves"（可自由用于repo贷款的储备）：

```
总储备
减去 法定准备金要求
减去 日内流动性要求（RLAP） → ~$3000亿
减去 外国银行持有（他们要留着给自己日内流动性）
减去 已经贷给dealer的 repo
= free float → ~ZERO
```

结论：**已经没有margin了**。任何额外的抵押品供给增长都会直接导致利率波动，超过美联储目标区间。

---

## 主要结论

1. **taper时机不对**：在曲线已经inversion之后继续taper是错误，因为inversion意味着最终买家罢工，dealer必须inventory增加，需要更多repo融资，但free float已经没了

2. **为什么free float没了**：
   - 缩表不断销毁储备
   - RLAP要求银行持有更多储备应对日内流动性
   - 外国央行在外国RRP工具囤积了$2500亿储备，不贷出来

3. **IOR降息没用**：IOR降息只是再分配储备，不能创造额外储备，也解决不了问题

4. **解决方案：cap外国RRP工具**，释放$2000亿储备回银行体系 → 增加free float → 缓解压力

> [[Global Money Notes #21 - It's Time to Use the Exorbitant Privilege]]

---

## 最终结论

> "Dealer of Last Resort is nigh… and a fixed price, full allotment o/n repo facility or a framework to administer mini-QEs better be ready by the fourth quarter when the summer collateral reprieve is over and the Treasury will once again flood the market with another round of $300 billion of bills."

美联储必须准备好成为**最后交易商（Dealer of Last Resort）**，推出固定价格、全额分配的隔夜回购工具，否则四季度还会出事。

> [[Dealer of Last Resort (最后交易商)]]

---

## 相关链接

- 上一篇：[[Global Money Notes #21 - It's Time to Use the Exorbitant Privilege]]
- 下一篇：继续整理...
- 概念链接：
  - [[美联储缩表 (balance sheet taper)]]
  - [[RLAP (处置流动性规划)]]

---

**原始位置**: `zoltan-pozsar-global-money-notes.pdf`
