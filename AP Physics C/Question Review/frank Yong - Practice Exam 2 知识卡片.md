# frank Yong · Practice Exam 2 知识卡片

> [!abstract]+ 考试总览
> 你在 MCQ 和 FRQ 两部分表现均衡且扎实，已有冲击 **AP 5** 的实力。本次暴露的问题是通往满分路上的精准突破点——主要集中在物理摆、逃逸速度、2D 冲量、动量守恒（运动摆）和弹簧连接体能量分析这五个微观盲区。

---

## 一、物理摆 · $\alpha = -C\theta$ 法求 $\omega$ 和 $T$

> [!important]+ 核心方法：写成 $\alpha = -\omega^2\theta$ 标准形式
> 
> **第 1 步**：写出回复力矩（小角度 $\theta \ll 1$）
> $$\tau = -mgd \sin\theta \approx -mgd\,\theta$$
> 
> **第 2 步**：代入转动方程 $\tau = I\alpha$
> $$I\alpha = -mgd\,\theta$$
> 
> **第 3 步**：写成 $\alpha = -C\theta$ 的 SHM 标准形式
> $$\alpha = -\frac{mgd}{I}\,\theta$$
> 
> **第 4 步**：对比 $\alpha = -\omega^2\theta$，直接读出
> $$\boxed{\omega = \sqrt{\frac{mgd}{I}}} \qquad \boxed{T = \frac{2\pi}{\omega} = 2\pi\sqrt{\frac{I}{mgd}}}$$

> [!warning]+ 你的易错点 — PE205
> 全班无人做对。关键是要**用平行轴定理**求绕转轴的 $I$：
> $$I = I_{CM} + md^2$$
> 对于任意形状刚体（如 45-45-90 三角形板），必须先找质心位置确定 $d$，再算 $I$。不要直接用 $I_{CM}$。

> [!tip]+ 做题检验清单
> - [ ] 是否找到了质心位置？
> - [ ] $d$ = 转轴到质心的距离（不是边长）？
> - [ ] $I$ 用的是绕转轴的值（加过 $md^2$）？
> - [ ] 写成 $\alpha = -C\theta$ 后，$C = mgd/I$ 对吗？
> - [ ] $\omega = \sqrt{C}$，$T = 2\pi/\omega$，没有写反？
> 
> 参考：[[Physical Pendulum SHM - Knowledge Card]]

---

## 二、逃逸速度 vs 轨道速度

> [!important]+ 核心概念
> **逃逸条件**：天体表面物体机械能恰好为零
> $$\frac{1}{2}mv_{esc}^2 - \frac{GMm}{R} = 0 \quad\Rightarrow\quad \boxed{v_{esc} = \sqrt{\frac{2GM}{R}} = \sqrt{2gR}}$$

> [!warning]+ 你的易错点 — PE210
> 区分两个速度：
> 
> | | 轨道速度 | 逃逸速度 |
> |---|---------|---------|
> | **公式** | $v_{orb} = \sqrt{GM/R}$ | $v_{esc} = \sqrt{2GM/R}$ |
> | **关系** | $v_{esc} = \sqrt{2}\,v_{orb}$ | — |
> | **物理含义** | 维持圆周轨道 | 脱离引力束缚 |
> 
> 最常犯的错误是把逃逸速度当成 $\sqrt{gR}$（那是圆轨道速度的近似，只在地表成立）。

---

## 三、2D 冲量积分

> [!important]+ 核心概念
> 冲量是力对时间的积分，**2D 情况下各分量独立计算**：
> $$\vec{J} = \int \vec{F}\,dt = \left(\int F_x\,dt\right)\hat{i} + \left(\int F_y\,dt\right)\hat{j}$$

> [!warning]+ 你的易错点 — PE232
> 当力是时间的函数（如 $\vec{F} = \alpha t\,\hat{i} + \beta t^2\,\hat{j}$）时：
> 1. **分别积分** $x$ 和 $y$ 分量
> 2. 注意积分上下限（从 $t=0$ 到给定时间）
> 3. 冲量 = 末动量 − 初动量：$\vec{J} = \Delta\vec{p}$

---

## 四、动量守恒 · 运动摆（弹道摆）

> [!important]+ 核心概念
> 弹道摆是**两阶段问题**：
> 
> **阶段 1**（碰撞，$\Delta t \to 0$）：子弹嵌入摆锤 → **动量守恒**
> $$mv_0 = (m+M)v'$$
> 
> **阶段 2**（摆上升）：摆+子弹系统摆动 → **机械能守恒**
> $$\frac{1}{2}(m+M)v'^2 = (m+M)gh$$

> [!warning]+ 你的易错点 — PE233
> - ⚠️ 碰撞阶段**不能**用能量守恒（非弹性碰撞有能量损失）
> - ⚠️ 摆上升阶段**可以**用机械能守恒（只有重力做功）
> - 分清楚哪段用动量守恒、哪段用能量守恒，不要混用

---

## 五、弹簧连接体 · 能量分配

> [!important]+ 核心概念
> 弹簧连接两物体的系统中，总能量 = 弹簧势能 + 两物体动能：
> $$E_{total} = \frac{1}{2}kx^2 + \frac{1}{2}m_1v_1^2 + \frac{1}{2}m_2v_2^2 = \text{常数}$$

> [!warning]+ 你的易错点 — PE236
> 容易遗漏其中一个物体的动能。系统能量有三种形式：
> 1. 弹簧弹性势能 $U_s = \frac{1}{2}kx^2$
> 2. 物体 A 的动能 $K_A = \frac{1}{2}m_Av_A^2$
> 3. 物体 B 的动能 $K_B = \frac{1}{2}m_Bv_B^2$
> 
> 当有**外力**做功或**摩擦力**存在时，机械能不再守恒。

---

## 六、运动学补充

> [!tip]+ PE209 · 圆周运动频率
> $$f = \frac{v}{2\pi R}$$
> 周长 $= 2\pi R$，频率 = 单位时间转的圈数。关键是先求周长。

> [!tip]+ PE217 · 自由落体位移比
> 从静止开始自由落体，连续等时间间隔的位移比为：
> $$1 : 3 : 5 : 7 : \dots$$
> 推导：$\Delta y_n = \frac{1}{2}g(t_n^2 - t_{n-1}^2)$，代入 $t_n = n\Delta t$

---

## FRQ 保持策略

你的 FRQ 表现与 MCQ 一致（双高），这说明你的**解题框架很完整**。建议：

- [ ] 确保每一步推导都有**文字说明**（"由牛顿第二定律…""由机械能守恒…"）
- [ ] 检查**量纲一致性**——这是 FRQ 中容易被扣分的地方
- [ ] FRQ 第三问（justify/explain）要用物理原理回答，不只用公式

---

## 推荐复习链接

- [[Physical Pendulum SHM - Knowledge Card]] — 物理摆系统复习
- [[Conservation of Energy - Knowledge Card]] — 能量守恒系统复习
- [[Simple Harmonic Motion]] — SHM 基础
- [[Satellite Orbital Motion]] — 逃逸速度与轨道速度
- [[题库/PE205]] · [[题库/PE210]] · [[题库/PE232]] · [[题库/PE233]] · [[题库/PE236]]
