# Global Money Notes #20: Lost in Transmission
**Zoltan Pozsar**  
**Date**: February 15, 2019  
**Credit Suisse**

---

## 核心命题

> The net supply of U.S. Treasuries will increase by over $1 trillion this year, and foreign FX hedged buyers will have to buy a large portion of this supply. But the curve is currently inverted relative to hedging costs, and foreigners won’t increase purchases unless the curve re-steepens relative to FX hedging costs. The required adjustments are huge – at least 100 bps.

> For the 10-year to be attractive relative to other G7 bonds on a hedged basis, yields would have to back up to at least 3.5% and more realistically to 4.0%; alternatively, three-month FX hedging costs would have to come down to 2.0%, either through positive cross-currency bases, much lower bill yields or rate cuts. Yet markets do not expect any of this for 2019. Something just does not add up...

---

## 四个不舒服的事实

2019年美国固定收益市场必须面对四个事实：

1. 美国国债净供给今年会增加**超过一万亿美元**
2. 美国需要外国投资者买其中很大一部分
3. 外国官方买家已经不再贪婪买国债了
4. 外国私人买家因为FX对冲成本，也不太可能买

**关键变化**：从外国官方买家（不对冲，价格不敏感）→ 外国私人买家（对冲，价格敏感）

---

## 问题：收益率曲线已经相对于对冲成本 inverted了

传统 inversion 看 2s/10s 或 3s/10s，Pozsar说这种衡量**已经过时**：

> "we’ve been living with a curve inversion for the past four months – relative to foreign investors’ FX hedging costs."

**真实 inversion 定义**：`3个月FX对冲成本 > 10年期国债收益率` → 对冲后收益率为负，为什么要买？

| 投资者 | 3个月对冲成本 | 10年期收益率 | 对冲后收益率 | 会买吗？ |
|--------|---------------|--------------|--------------|----------|
| 日元投资者 | ~3.0% | ~2.7% | ~-0.15% | ❌ 不买 |
| 欧元投资者 | ~2.7% | ~2.7% | ~-0.05% | ❌ 几乎不买 |

因此，外国对冲投资者**罢工了**，一级承销商必须自己接盘，repo市场融资压力越来越大。

> [[跨货币基差 (cross-currency basis)]]

---

## 怎么调整才能重新吸引外资？

至少需要 **100bps** 调整：

要么：
- 10年期收益率涨到 **至少3.5%，实际需要4.0%** → 熊陡（bear steepening），对股票信用不好

要么：
- 三个月对冲成本降到 **2.0%以下** → 牛陡（bull steepening），对风险资产好

怎么降对冲成本？对冲成本 = OIS + Libor-OIS + 交叉货币基差，所以：
- 交叉货币基差转正 → 降对冲成本
- 国债bill收益率低于OIS → 降Libor-OIS → 降对冲成本
- 美联储降息 → 降OIS → 降对冲成本

---

## 为什么会走到这一步？

美联储加息周期中：

- 加息 → OIS上升 → 对冲成本上升
- 加息 → 曲线平坦化 → 10年期收益率不怎么涨
- 最终 → 对冲成本 > 10年期收益率 →  inversion

日本欧洲投资者本来买美元资产就是因为本地曲线更平收益率更低，现在美国曲线平过他们了，自然不买了。

| 时期 | 美国曲线 vs 其他G7曲线 | 资本流动 |
|------|-----------------------|----------|
| 2015-2017 | 美国曲线最陡 | 资本流入美国买国债 |
| 2018-现在 | 美国曲线最平 | 资本流出美国，买欧日国债 |

---

## 市场现在预期什么？

市场不预期：
- 10年期涨到 3.5-4.0%
- 交叉货币基差转正
- 美联储今年降息

所以问题无解，一级承销商存货会越来越多，repo市场压力越来越大，**美联储提前结束缩表，推出隔夜回购工具是必然的**。

---

## 最可能的调整路径

最省力的路径：交叉货币基差自动转正 → 降对冲成本 → 不需要加息降息也不需要大涨：

- 外国需求减少 → 美元FX swap需求减少 → 美元供给超过需求 → 交叉货币基差从负转正
- 基差转正 → 降对冲成本 → 曲线相对于对冲成本重新陡峭化
- Libor-OIS 会收紧到10bps甚至到负 → 再降对冲成本

这种情况下，不需要美联储干预，市场自己调整，**对风险资产最好**。

如果调整失败，美联储必须出手：
- reverse twist（卖长买短）→ 降短端收益率，陡峭曲线
- cap 外国RRP池子 → 释放$2500亿准备金到bill和FX swap市场 → 推低bill收益率和交叉货币基差

---

## 核心结论

"Something just does not add up"：

- 一万亿新增供给
- 外国价格敏感买家接盘
- 但当前价格下无利可图
- 必须调整至少100bps
- 市场还没price in

调整到位之前，外国买家持续罢工，一级dealer存货累积，repo市场持续有压力，美联储缩表提前结束概率很大。

---

## 相关链接

- 上一篇：[[Global Money Notes #19 - Libor-OIS: A Morbidity Review]]
- 下一篇：继续整理...
- 概念链接：
  - [[FX hedging costs (FX对冲成本)]]
  - [[曲线 inversion]]
  - [[美联储缩表 (balance sheet taper)]]

---

**原始位置**: `zoltan-pozsar-global-money-notes.pdf`
