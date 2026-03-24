---
tags:
  - 电磁学
  - 互感
  - 磁矢势
created: 2026-03-22
---


# Neumann 公式（Neumann Formula）

**Neumann 公式**将两个载流导线回路之间的[[电磁学/互感]]用纯几何的双路径积分表达出来，是计算任意形状线圈互感的普遍方法。

$$\boxed{M = \frac{\mu_0}{4\pi} \oint_{C_1} \oint_{C_2} \frac{d\boldsymbol{l}_1 \cdot d\boldsymbol{l}_2}{|\boldsymbol{r}_1 - \boldsymbol{r}_2|}}$$

---

## 推导

### 第一步：矢量势表达磁通量

线圈 $C_2$（电流 $I_2$）在空间产生的[[电磁学/磁矢势]]为（Biot-Savart 积分形式）：

$$\mathbf{A}(\mathbf{r}) = \frac{\mu_0 I_2}{4\pi} \oint_{C_2} \frac{d\boldsymbol{l}_2}{|\mathbf{r} - \mathbf{r}_2|}$$

### 第二步：磁通量化为线积分

$C_2$ 在线圈 $C_1$ 中产生的磁通量，用斯托克斯定理转化：

$$\Phi_{12} = \iint_{S_1} \mathbf{B} \cdot d\mathbf{S} = \iint_{S_1} (\nabla \times \mathbf{A}) \cdot d\mathbf{S} \xlongequal{\text{Stokes}} \oint_{C_1} \mathbf{A} \cdot d\boldsymbol{l}_1$$

### 第三步：代入 $\mathbf{A}$ 的表达式

$$\Phi_{12} = \oint_{C_1} \left(\frac{\mu_0 I_2}{4\pi} \oint_{C_2} \frac{d\boldsymbol{l}_2}{|\boldsymbol{r}_1 - \boldsymbol{r}_2|}\right) \cdot d\boldsymbol{l}_1 = \frac{\mu_0 I_2}{4\pi} \oint_{C_1}\oint_{C_2} \frac{d\boldsymbol{l}_1 \cdot d\boldsymbol{l}_2}{|\boldsymbol{r}_1 - \boldsymbol{r}_2|}$$

由 $M = \Phi_{12} / I_2$ 即得 Neumann 公式。$\square$

---

## 三个核心性质

### 1. 对称性：$M_{12} = M_{21}$ ⭐

公式对 $C_1 \leftrightarrow C_2$ 完全对称，因此

$$\text{"} C_2 \text{ 对 } C_1 \text{ 的互感"} = \text{"} C_1 \text{ 对 } C_2 \text{ 的互感"}$$

这在物理上并不显然（两个线圈角色不同），但 Neumann 公式给出了严格证明。

### 2. 纯几何性

$M$ 只取决于两回路的**形状、相对位置与方向**，与电流大小无关。

### 3. 点积的几何含义

$$d\boldsymbol{l}_1 \cdot d\boldsymbol{l}_2 = |dl_1|\,|dl_2|\cos\theta_{12}$$

$\theta_{12}$ 是两电流元方向的夹角：

| 相对方向 | $\cos\theta_{12}$ | 对 $M$ 的贡献 |
|---------|------------------|-------------|
| 平行同向 | $+1$ | 正（增强耦合） |
| 平行反向 | $-1$ | 负（削弱耦合） |
| 垂直 | $0$ | 零 |

---

## $M = 0$ 的对称性判据

Neumann 公式提供了判断 $M = 0$ 的简洁方法：

**若对 $C_1$ 上任意一点 $\mathbf{r}_1$，沿 $C_2$ 的积分 $\displaystyle\oint_{C_2} \frac{d\boldsymbol{l}_2 \cdot d\boldsymbol{l}_1}{|\boldsymbol{r}_1-\boldsymbol{r}_2|}=0$，则 $M=0$。**

### 应用：两垂直共径线圈的 $M = 0$

线圈 I 在 $xy$ 平面，线圈 II 旋转 $90°$ 至 $xz$ 平面，两者共享 $x$ 轴直径。

对线圈 II 上的参数化 $\boldsymbol{r}_2 = R(\cos\phi, 0, \sin\phi)$，$d\boldsymbol{l}_2 = R(-\sin\phi, 0, \cos\phi)\,d\phi$：

对 $C_1$ 上一点 $\boldsymbol{r}_1 = (x, y, 0)$，点积 $d\boldsymbol{l}_1 \cdot d\boldsymbol{l}_2$ 中来自 $z$ 方向的分量为零（$dl_{1z}=0$），来自 $x$ 方向的分量经积分后：

$$\oint_{C_2} \frac{-\sin\phi \cdot dl_{1x}}{(x^2+y^2+R^2-2xR\cos\phi)^{1/2}} d\phi = 0$$

（$\sin\phi$ 为奇函数，分母关于 $\phi\to2\pi-\phi$ 对称，积分为零）

$$\therefore \; M = 0 \qquad \checkmark$$

这正是[[电磁学/例题/题2.11-同轴超导线圈的磁通守恒与电流演化|题 2.11]] 中 (b) 步骤的数学根据。

---

## 特殊情形

### 共轴圆形线圈（Neumann 积分 → 椭圆积分）

两个半径分别为 $a, b$、轴向距离为 $d$ 的共轴圆形线圈，Neumann 公式化为：

$$M = \frac{\mu_0}{\pi}\sqrt{ab}\left[\left(\frac{2}{k}-k\right)K(k) - \frac{2}{k}E(k)\right]$$

其中 $k^2 = \dfrac{4ab}{(a+b)^2+d^2}$，$K, E$ 是第一、二类完全椭圆积分。

> 这说明对有限大线圈，Neumann 公式一般**无解析闭合解**，需数值积分。

### 长直导线与矩形回路

可解析计算，结果含对数项，常作为教材练习题。

---

## 推导工具链

```
Biot-Savart 定律
       ↓
磁矢势 A（线积分形式）    ← [[电磁学/磁矢势]]
       ↓
斯托克斯定理               ← [[矢量分析/斯托克斯定理]]
       ↓
通量 → 边界线积分
       ↓
Neumann 公式（双路径积分）
       ↓
互感对称性 M₁₂ = M₂₁      ← [[电磁学/互感]]
```

---

## 相关概念

- [[电磁学/互感]] — Neumann 公式是互感定义的计算实现
- [[电磁学/磁矢势]] — 推导的中间工具：$\mathbf{B}=\nabla\times\mathbf{A}$
- [[矢量分析/斯托克斯定理]] — 将面积分转为线积分的关键步骤
- [[电磁学/磁通量]] — $\Phi_{12}$ 的定义
- [[电磁学/麦克斯韦方程组]] — Biot-Savart 的背景方程
- [[电磁学/例题/题2.11-同轴超导线圈的磁通守恒与电流演化|题 2.11]] — Neumann $M=0$ 对称性判据的直接应用
