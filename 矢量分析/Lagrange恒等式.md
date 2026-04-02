---
tags:
  - 矢量分析
  - 恒等式
created: 2026-03-22
---

# Lagrange 恒等式（Lagrange Identity）

$$\boxed{|\mathbf{A} \times \mathbf{B}|^2 + (\mathbf{A} \cdot \mathbf{B})^2 = |\mathbf{A}|^2|\mathbf{B}|^2}$$

等价写法（移项）：

$$|\mathbf{A} \times \mathbf{B}|^2 = |\mathbf{A}|^2|\mathbf{B}|^2 - (\mathbf{A} \cdot \mathbf{B})^2$$

---

## 本质：三维勾股定理

把 $\mathbf{A}$ 沿 $\mathbf{B}$ 方向分解为平行分量与垂直分量：

$$\mathbf{A} = \mathbf{A}_\parallel + \mathbf{A}_\perp, \qquad |\mathbf{A}_\parallel| = |\mathbf{A}|\cos\theta,\quad |\mathbf{A}_\perp| = |\mathbf{A}|\sin\theta$$

则：

| 向量运算 | 几何含义 | 数值 |
|---------|---------|------|
| $\mathbf{A}\cdot\mathbf{B}$ | $\mathbf{A}$ 在 $\mathbf{B}$ 方向的**投影** × $\lvert\mathbf{B}\rvert$ | $\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\cos\theta$ |
| $\lvert\mathbf{A}\times\mathbf{B}\rvert$ | $\mathbf{A}$、$\mathbf{B}$ 张成的平行四边形**面积** | $\lvert\mathbf{A}\rvert\lvert\mathbf{B}\rvert\sin\theta$ |

代入恒等式：

$$\underbrace{|\mathbf{A}|^2|\mathbf{B}|^2\sin^2\theta}_{\text{垂直分量}^2} + \underbrace{|\mathbf{A}|^2|\mathbf{B}|^2\cos^2\theta}_{\text{平行分量}^2} = |\mathbf{A}|^2|\mathbf{B}|^2$$

即 $\sin^2\theta + \cos^2\theta = 1$，**Lagrange 恒等式本质上就是勾股定理的向量语言版本**。

---

## 证明

### 向量四重积的一般证明

先证一般形式（对应习题 52）：
$$\boxed{(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d}) = \begin{vmatrix} \mathbf{a}\cdot\mathbf{c} & \mathbf{b}\cdot\mathbf{c} \\ \mathbf{a}\cdot\mathbf{d} & \mathbf{b}\cdot\mathbf{d} \end{vmatrix} = (\mathbf{a}\cdot\mathbf{c})(\mathbf{b}\cdot\mathbf{d})-(\mathbf{a}\cdot\mathbf{d})(\mathbf{b}\cdot\mathbf{c})}$$

#### 证法一：Levi-Civita 指标法

$$(\mathbf{a}\times\mathbf{b})_i=\varepsilon_{ijk}a_jb_k,\qquad (\mathbf{c}\times\mathbf{d})_i=\varepsilon_{ilm}c_ld_m$$

于是
$$\begin{aligned}
(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d})
&= \varepsilon_{ijk}\varepsilon_{ilm}\,a_jb_kc_ld_m \\
&= (\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl})a_jb_kc_ld_m \\
&= (\mathbf{a}\cdot\mathbf{c})(\mathbf{b}\cdot\mathbf{d})-(\mathbf{a}\cdot\mathbf{d})(\mathbf{b}\cdot\mathbf{c}).
\end{aligned}$$

#### 证法二：BAC–CAB 规则

**第一步：把左边改写成标量三重积的形式。**

标量三重积（混合积）定义为 $(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}$，它有一个关键性质——**轮换不变性**：
$$\boxed{(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w} = \mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})}$$

> **为什么成立？** 用指标看最清楚：$(\mathbf{u}\times\mathbf{v})\cdot\mathbf{w}=\varepsilon_{ijk}u_jv_kw_i$，而 $\varepsilon_{ijk}=\varepsilon_{kij}$，所以可以把 $w_i$ 放最前面：$w_i\varepsilon_{ijk}v_jw_k=\mathbf{u}\cdot(\mathbf{v}\times\mathbf{w})$。

现在看原式 $(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d})$。把 $\mathbf{c}\times\mathbf{d}$ **整体当作第三个向量** $\mathbf{w}$，即令 $\mathbf{w}=\mathbf{c}\times\mathbf{d}$，则原式正是 $(\mathbf{a}\times\mathbf{b})\cdot\mathbf{w}$。

利用轮换不变性，把叉号"搬进去"：
$$\boxed{(\mathbf{a}\times\mathbf{b})\cdot(\mathbf{c}\times\mathbf{d})=\mathbf{a}\cdot\bigl[\mathbf{b}\times(\mathbf{c}\times\mathbf{d})\bigr]}$$

**第二步：对中括号使用 BAC–CAB 规则。**

[[矢量分析/BAC-CAB规则证明|BAC–CAB 规则]] 给出：
$$\mathbf{b}\times(\mathbf{c}\times\mathbf{d})=(\mathbf{b}\cdot\mathbf{d})\mathbf{c}-(\mathbf{b}\cdot\mathbf{c})\mathbf{d}.$$

代回即得
$$(\mathbf{a}\cdot\mathbf{c})(\mathbf{b}\cdot\mathbf{d})-(\mathbf{a}\cdot\mathbf{d})(\mathbf{b}\cdot\mathbf{c}).\qquad\square$$

---

### Lagrange 恒等式的特例

在四重积公式中令 $\mathbf{a}=\mathbf{c}=\mathbf{A}$，$\mathbf{b}=\mathbf{d}=\mathbf{B}$：

$$|\mathbf{A}\times\mathbf{B}|^2 = (\mathbf{A}\cdot\mathbf{A})(\mathbf{B}\cdot\mathbf{B})-(\mathbf{A}\cdot\mathbf{B})^2 = |\mathbf{A}|^2|\mathbf{B}|^2-(\mathbf{A}\cdot\mathbf{B})^2.\qquad\square$$

---

## 推论：Cauchy-Schwarz 不等式

由 $|\mathbf{A}\times\mathbf{B}|^2 \geq 0$，立即得到：

$$\boxed{(\mathbf{A}\cdot\mathbf{B})^2 \leq |\mathbf{A}|^2|\mathbf{B}|^2}$$

即 $|\mathbf{A}\cdot\mathbf{B}| \leq |\mathbf{A}||\mathbf{B}|$（Cauchy-Schwarz 不等式）。

Lagrange 恒等式比 Cauchy-Schwarz 更精确：**它不仅说明差值非负，还指出差值恰好是叉积模的平方**，即两向量"不平行程度"的度量。

等号成立 $\Longleftrightarrow$ $\mathbf{A}\times\mathbf{B}=0$ $\Longleftrightarrow$ $\mathbf{A}\parallel\mathbf{B}$。

---

## 几何应用：点到直线的距离

**问题：** 空间中直线过原点，方向单位向量 $\hat{n}$，点 $P$ 的位置向量为 $\mathbf{r}$，求 $P$ 到直线的距离 $d$。

$\mathbf{r}$ 中垂直于 $\hat{n}$ 的分量即为距离：

$$d^2 = |\mathbf{r}|^2 - (\mathbf{r}\cdot\hat{n})^2 \xlongequal{\text{Lagrange}} |\mathbf{r}\times\hat{n}|^2$$

$$\therefore\quad d = |\mathbf{r}\times\hat{n}|$$

---

## 在电磁学中的出现

**Poynting 矢量与能量密度的关系：**

电磁场的能量密度 $u \propto |\mathbf{E}|^2 + c^2|\mathbf{B}|^2$，Poynting 矢量 $\mathbf{S} = \frac{1}{\mu_0}\mathbf{E}\times\mathbf{B}$。

当 $\mathbf{E}\perp\mathbf{B}$（平面电磁波）时 $\mathbf{E}\cdot\mathbf{B}=0$，Lagrange 恒等式给出：

$$|\mathbf{S}|^2 = \frac{1}{\mu_0^2}|\mathbf{E}\times\mathbf{B}|^2 = \frac{1}{\mu_0^2}|\mathbf{E}|^2|\mathbf{B}|^2$$

无需展开叉积即可得到 Poynting 矢量的模长。

---

## 引理汇总

### 引理一：共线判定

$$\mathbf{A} \times \mathbf{B} = \mathbf{0} \iff \mathbf{A} \parallel \mathbf{B}$$

**证明**：取恒等式开方：

$$|\mathbf{A} \times \mathbf{B}| = |\mathbf{A}||\mathbf{B}|\sin\theta = 0 \iff \sin\theta = 0 \iff \theta = 0 \text{ 或 } \pi$$

---

### 引理二：$\sin\theta$ 和 $\cos\theta$ 的显式公式

$$\sin\theta = \frac{|\mathbf{A} \times \mathbf{B}|}{|\mathbf{A}||\mathbf{B}|}, \qquad \cos\theta = \frac{|\mathbf{A} \cdot \mathbf{B}|}{|\mathbf{A}||\mathbf{B}|}$$

---

### 引理三：三维格拉斯曼恒等式（Gram 行列式）

$$\boxed{[\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C})]^2 = \det\begin{pmatrix} \mathbf{A}\cdot\mathbf{A} & \mathbf{A}\cdot\mathbf{B} & \mathbf{A}\cdot\mathbf{C} \\ \mathbf{B}\cdot\mathbf{A} & \mathbf{B}\cdot\mathbf{B} & \mathbf{B}\cdot\mathbf{C} \\ \mathbf{C}\cdot\mathbf{A} & \mathbf{C}\cdot\mathbf{B} & \mathbf{C}\cdot\mathbf{C} \end{pmatrix}}$$

**含义**：右边的 Gram 矩阵行列式 = 平行六面体体积的平方。当体积为零（行列式为零）时，三矢量线性相关（共面）。

---

### 引理四：共面判定

$$\mathbf{A} \cdot (\mathbf{B} \times \mathbf{C}) = 0 \iff \mathbf{A}, \mathbf{B}, \mathbf{C} \text{ 共面}$$

---

### 引理五：投影分解

$\mathbf{B}$ 在 $\mathbf{A}$ 方向上的垂直分量：

$$|\mathbf{B}_\perp|^2 = |\mathbf{B}|^2 - \frac{(\mathbf{A} \cdot \mathbf{B})^2}{|\mathbf{A}|^2} = \frac{|\mathbf{A} \times \mathbf{B}|^2}{|\mathbf{A}|^2}$$

---

## 引理链全景图

```
Lagrange 恒等式
│
├── 引理一 → 共线判定
│      └─ |A×B| = 0 ⟺ A ∥ B
│
├── 引理二 → sinθ, cosθ 显式公式
│      └─ sinθ = |A×B|/(|A||B|)
│
├── 引理三 → Gram 行列式（三个矢量）
│      └─ [A·(B×C)]² = det(G)
│
├── 引理四 → 共面判定
│      └─ A·(B×C) = 0 ⟺ 共面
│
└── 引理五 → 投影分解
       └─ |B_⊥|² = |A×B|²/|A|²
```

---

## 相关概念

- [[矢量分析/矢量恒等式总结]] — BAC-CAB 是 Lagrange 恒等式的代数证明工具
- [[矢量分析/矢量分析索引]] — 矢量分析全览
- [[矢量分析/亥姆霍兹定理]] — Gram 行列式在矢量场分解中的应用
