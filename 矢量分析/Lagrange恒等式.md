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

直接展开，利用 BAC-CAB 规则（见 [[矢量分析/矢量恒等式总结]]）：

$$|\mathbf{A}\times\mathbf{B}|^2 = (\mathbf{A}\times\mathbf{B})\cdot(\mathbf{A}\times\mathbf{B})$$

用向量四重积恒等式 $(\mathbf{P}\times\mathbf{Q})\cdot(\mathbf{R}\times\mathbf{S}) = (\mathbf{P}\cdot\mathbf{R})(\mathbf{Q}\cdot\mathbf{S}) - (\mathbf{P}\cdot\mathbf{S})(\mathbf{Q}\cdot\mathbf{R})$，令 $\mathbf{P}=\mathbf{R}=\mathbf{A}$，$\mathbf{Q}=\mathbf{S}=\mathbf{B}$：

$$|\mathbf{A}\times\mathbf{B}|^2 = (\mathbf{A}\cdot\mathbf{A})(\mathbf{B}\cdot\mathbf{B}) - (\mathbf{A}\cdot\mathbf{B})(\mathbf{B}\cdot\mathbf{A}) = |\mathbf{A}|^2|\mathbf{B}|^2 - (\mathbf{A}\cdot\mathbf{B})^2 \qquad \square$$

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

## 相关概念

- [[矢量分析/矢量恒等式总结]] — 所属章节：代数恒等式 §1.2，BAC-CAB 是其证明工具
- [[矢量分析/矢量分析索引]] — 矢量分析全览
