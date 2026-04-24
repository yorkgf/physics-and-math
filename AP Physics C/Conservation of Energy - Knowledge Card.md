# 能量守恒 · 知识卡片

> [!summary]+ 核心概念
> **孤立系统的总能量保持不变**。当只有保守力做功时，机械能（动能+势能）守恒。

---

## 公式速查

| 类型 | 公式 | 说明 |
|------|------|------|
| 总能量守恒 | $E_{total} = \text{constant}$ / $\Delta E = 0$ | 孤立系统 |
| 机械能守恒 | $K + U = \text{constant}$ | 仅保守力做功 |
| 含转动机械能 | $E = K_{trans} + K_{rot} + U$ | 刚体转动系统 |
| 平动动能 | $K_{trans} = \frac{1}{2}mv_{CM}^2$ | 质心运动 |
| 转动动能 | $K_{rot} = \frac{1}{2}I\omega^2$ | 绕轴转动 |
| 势能 | $U$ | 重力 / 弹性 / 引力势能 |

## 成立条件

```
孤立系统 (Q=0, W=0) ──→ 总能量守恒
        │
        └── 仅保守力做功 ──→ 机械能守恒
                │
                └── 非保守力存在 ──→ 机械能不守恒，总能量仍守恒
```

| 条件 | 守恒量 | 典型场景 |
|------|--------|----------|
| 孤立系统，无外力做功 | $E_{total}$ | 封闭力学系统 |
| 仅保守力（重力/弹力/引力） | $K + U$ | 抛体、弹簧、轨道 |
| 有摩擦/阻力 | 无机械能守恒 | 含 $W_{nc} = \Delta E$ |

## 常见应用

| 场景 | 关键点 | 参考例题 |
|------|--------|----------|
| 弹簧 + 轨道 | $U_s \to K \to U_g$ 连续转化 | [[Example 10 - Spring-Launch into Semicircular Track\|Ex.10]] |
| 天体轨道 | $E = -\frac{GMm}{2r}$（圆轨道总能） | [[Satellite Orbital Motion]] |
| 碰撞 + 弹簧 | 动量守恒 → 能量守恒，两步求解 | [[Example 19 - Ballistic Measurement with Spring\|Ex.19]] |
| 变质量系统 | 功-能定理处理质量变化 | [[Example 6 - Sliding Rope\|Ex.6]] |
| 势能 → 运动 | $F = -dU/dx$，转折点 $K=0$ | [[Example 9 - Potential Energy and Turning Points\|Ex.9]] |

## 解题策略

> [!tip]- 解题三步法
> 1. **选系统** — 确定系统边界（含地球？含弹簧？）
> 2. **判条件** — 是否有非保守力？确定守恒类型
> 3. **列方程** — 选取初末状态，$E_i = E_f$（或加 $W_{nc}$）

## 易错提醒

- ❌ 转动系统中**漏写** $K_{rot} = \frac{1}{2}I\omega^2$
- ❌ 有非保守力时直接写 $K+U$ 守恒（应加 $W_{nc}$）
- ❌ 忘记滚动条件 $v_{CM} = R\omega$ 来关联平动和转动
- ❌ 混淆引力势能 $U = -\frac{GMm}{r}$ 与 $U = mgh$

## 相关链接

- [[Conservation of Rotational Energy]] — 转动能量守恒
- [[Gravitational Potential Energy]] — 引力势能详解
- [[Satellite Orbital Motion]] — 轨道力学中的应用
- [[Unit 6 Energy and Momentum of Rotating Systems Index]] — Unit 6 索引
- [[../知识库导航|知识库总导航]]
