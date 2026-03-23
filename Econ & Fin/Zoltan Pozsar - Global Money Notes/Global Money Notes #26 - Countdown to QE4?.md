# Global Money Notes #26: Countdown to QE4?
**Zoltan Pozsar**  
**Date**: December 9, 2019  
**Credit Suisse**

---

## 核心命题

> The Fed’s liquidity operations have not been sufficient to relax the constraints banks will face in the upcoming year-end turn. Reserves are still insufficient; there are no true “excess” reserves; and large U.S. banks’ G-SIB scores are shaping up to be a severe binding constraint heading into the year-end turn... We have never had a year-end without a comfortable buffer of excess reserves or when G-SIB scores could force most U.S. banks to turn off market making... QE4 by year-end is increasingly likely.

---

## 核心论证：Basel III彻底改变了支付体系

### 旧体系（pre-Basel III）：信用体系

- 银行可以使用日内透支（daylight overdrafts）
- 美联储日内提供信贷，支付体系不需要银行预先持有准备金
- 晚上结算，在联邦基金市场拆借平盘

**结果：** 不需要大资产负债表，不需要大量超额准备金。

### 新体系（post-Basel III）：token体系

- 巴塞尔III要求G-SIBs预先满足：
  - 30-day outflow liquidity → LCR
  - intraday liquidity needs → 必须持有准备金
  - resolution liquidity needs → 必须持有准备金

因此，**所有流动性需求都必须用准备金满足**，没有日内透支了 → 这就是token体系：你的余额必须一直≥0，不允许透支。

> [[LCR (流动性覆盖率)]]
> [[日内流动性 (Intraday Liquidity)]]
> [[RLAP (处置流动性规划)]]
> [[G-SIBs (全球系统重要性银行)]]

---

### 谁是最后贷款人/最后做市商

在token体系里：

- J.P. Morgan 是整个体系的**lender of next-to-last resort（倒数第二个贷款人）**
- JPM 持有最多超额准备金，当其他银行/机构需要流动性，JPM 出借准备金
- JPM 持有超额准备金就是体系的**shock absorber**，就像过去美联储的日内透支

**问题来了：**

- taper 不断抽走准备金，JPM的超额准备金越来越少
- IOR降息也是故意抽走准备金，让银行出借，但是同时也消耗了JPM的缓冲
- 到2019年底，JPM已经把大部分超额准备金都花了，换了国债 → **真的没有超额准备金了**

> 因此，"excess reserves"这个词已经是oxymoron（矛盾修饰法）：每一分准备金都是满足监管要求必须持有的，没有"多余"的。

> [[Global Money Notes #5 - What Excess Reserves]]

---

## G-SIB得分的问题

G-SIB得分决定附加资本要求，得分越高附加资本越多，所以每个银行都想压低得分：

- G-SIB得分 = 规模 + 关联性 + 复杂性...
- 年末得分，** repo/FX swap 做市活动会增加得分**，因为增加了资负表规模
- 所以，临近年末，每个银行都有动机缩减做市规模，降低得分

2019年特殊情况：

- 股市上涨 → 银行股权市值增加 → G-SIB得分自动上升
- 曲线平坦化 → 银行必须持有更多国债inventory → 资负表扩大 → G-SIB得分自动上升
- 因此，银行都被迫缩减repo/FX swap做市 → 流动性供给进一步收缩

> 今年已经没有超额准备金缓冲，G-SIB得分又逼着银行收缩做市 → **最坏情况组合**

---

## 为什么现在形势已经很严峻

1. **美联储的流动性操作没有增加真正的excess reserves**
   - 美联储买bill，bill原本就在银行HQLA里，买了之后换成准备金 → 看似增加了准备金，其实还是在HQLA，没有创造出"excess"准备金给JPM做缓冲

2. **bill买盘没用**
   - bill买盘推低bill收益率到o/n RRP利率以下 → 货币基金直接把钱放去RRP → 准备金又被sterilize了 → 还是没创造出excess reserves

3. **G-SIB得分导致FX swap市场最先出问题**
   - 美国银行更愿意用有限的excess准备金做repo，不愿意做FX swap → 因为repo对G-SIB得分影响更小
   - 所以FX swap市场会先断流动性 → 外国机构得不到美元，可能引发forced selloff of Treasuries

---

## 结论：只有QE4能解决问题

QE4就是美联储直接买coupon Treasuries（中长期国债），从银行/交易商手里买：

- 银行卖出国债给美联储 → 得到excess reserves → 释放出准备金用于做市 → 问题解决
- 这就是reverse the taper mistake，taper抽走了准备金，QE4再放回来
- 只有买coupon才能真正释放excess reserves，买bill没用

如果不做QE4，会发生：

- 年末FX swap市场流动性断供
- RV对冲基金无法roll their basis trades → forced sell Treasuries
- 收益率短期spike，然后美联储被迫救市 → QE4还是会来，只是更晚，更被动

> "If carry makes the world go 'round, and reserves make carry possible... the day we run out of reserves would be the day when the world would stop spinning."

---

## 最终一句话

> "When Southeast Asia ran out of U.S. dollar reserves in 1997, the world did stop spinning – in Southeast Asia. Back then, the binding constraint was FX reserves... Today, the binding constraint is excess reserves – the reserves that G-SIBs hold in their reserve accounts at the Fed in excess of their regulatory requirements. When the money runs out, pegs get broken... In Southeast Asia, we broke FX pegs. In September, we broke o/n pegs – that is, the target range for the o/n rates complex."

---

## 相关链接

- 上一篇：[[Global Money Notes #25 - Design Options for an o/n Repo Facility]]
- 下一篇：继续整理...
- 概念链接：
  - [[token system vs credit system (post-Basel III)]]
  - [[lender of next-to-last resort]]

---

**原始位置**: `zoltan-pozsar-global-money-notes.pdf`
