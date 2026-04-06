---
tags:
  - 矢量分析
  - 证明
  - 叉积
created: 2026-04-02
---

# BAC–CAB 规则证明（叉积性质 6）

> 教材习题 50：证明
> $$\mathbf{a} \times (\mathbf{b} \times \mathbf{c}) = (\mathbf{a}\cdot\mathbf{c})\,\mathbf{b} - (\mathbf{a}\cdot\mathbf{b})\,\mathbf{c}$$

---

## 证明（分量法）

设
$$\mathbf{a}=\langle a_1,a_2,a_3\rangle,\qquad \mathbf{b}=\langle b_1,b_2,b_3\rangle,\qquad \mathbf{c}=\langle c_1,c_2,c_3\rangle.$$

### 第一步：计算内层叉积

$$\mathbf{b}\times\mathbf{c}=\langle b_2c_3-b_3c_2,\; b_3c_1-b_1c_3,\; b_1c_2-b_2c_1\rangle.$$

### 第二步：计算外层叉积的第一分量

$$\begin{aligned}
\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_1
&= a_2(b_1c_2-b_2c_1)-a_3(b_3c_1-b_1c_3) \\
&= a_2b_1c_2-a_2b_2c_1-a_3b_3c_1+a_3b_1c_3 \\
&= b_1(a_2c_2+a_3c_3)-c_1(a_2b_2+a_3b_3).
\end{aligned}$$

为了凑出完整的点积，加减 $a_1b_1c_1$：

$$\begin{aligned}
\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_1
&= b_1(a_1c_1+a_2c_2+a_3c_3)-c_1(a_1b_1+a_2b_2+a_3b_3) \\
&= (\mathbf{a}\cdot\mathbf{c})\,b_1-(\mathbf{a}\cdot\mathbf{b})\,c_1.
\end{aligned}$$

### 第三步：同理验证其余分量

**第二分量：**
$$\begin{aligned}
\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_2
&= a_3(b_2c_3-b_3c_2)-a_1(b_1c_2-b_2c_1) \\
&= (\mathbf{a}\cdot\mathbf{c})\,b_2-(\mathbf{a}\cdot\mathbf{b})\,c_2.
\end{aligned}$$

**第三分量：**
$$\begin{aligned}
\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_3
&= a_1(b_3c_1-b_1c_3)-a_2(b_2c_3-b_3c_2) \\
&= (\mathbf{a}\cdot\mathbf{c})\,b_3-(\mathbf{a}\cdot\mathbf{b})\,c_3.
\end{aligned}$$

### 结论

三个分量均与右端一致，故

$$\boxed{\mathbf{a}\times(\mathbf{b}\times\mathbf{c})=(\mathbf{a}\cdot\mathbf{c})\,\mathbf{b}-(\mathbf{a}\cdot\mathbf{b})\,\mathbf{c}}$$

证毕。

---

## 证明二：Levi-Civita 指标法（最优雅）

### 前置知识

**爱因斯坦求和约定**：当同一个指标在一项中出现两次时，默认对该指标从 1 到 3 求和，省略 $\sum$ 符号。例如
$$\mathbf{a}\cdot\mathbf{b} = a_ib_i \equiv \sum_{i=1}^{3}a_ib_i.$$

**Levi-Civita 符号（完全反对称张量）** $\varepsilon_{ijk}$：
- 若 $(i,j,k)$ 是 $(1,2,3)$ 的**偶排列**（如 123, 231, 312），则 $\varepsilon_{ijk}=+1$；
- 若 $(i,j,k)$ 是 $(1,2,3)$ 的**奇排列**（如 132, 213, 321），则 $\varepsilon_{ijk}=-1$；
- 任意两个指标相同，则 $\varepsilon_{ijk}=0$。

用它可以把叉积写成分量形式：
$$\boxed{(\mathbf{u}\times\mathbf{v})_i = \varepsilon_{ijk} u_j v_k}$$

> 验证：取 $i=1$，则 $\varepsilon_{1jk}a_jb_k = a_2b_3 - a_3b_2$，正是叉积第一分量。

### 证明过程

左边第 $i$ 个分量为
$$\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_i
= \varepsilon_{ijk} a_j (\mathbf{b}\times\mathbf{c})_k
= \varepsilon_{ijk} a_j \varepsilon_{klm} b_l c_m.$$

这里 $k$ 是重复指标（求和），$j,l,m$ 也是求和指标。将两个 Levi-Civita 符号合并，用到恒等式
$$\boxed{\varepsilon_{ijk}\varepsilon_{klm} = \delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}}$$

（该恒等式的推导见下节附录。）代入得
$$\begin{aligned}
\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr]_i
&= (\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}) a_j b_l c_m \\
&= \underbrace{\delta_{il}b_l}_{=\,b_i} \cdot \underbrace{\delta_{jm}a_jc_m}_{=\,\mathbf{a}\cdot\mathbf{c}} - \underbrace{\delta_{im}c_m}_{=\,c_i} \cdot \underbrace{\delta_{jl}a_jb_l}_{=\,\mathbf{a}\cdot\mathbf{b}} \\
&= b_i (\mathbf{a}\cdot\mathbf{c}) - c_i (\mathbf{a}\cdot\mathbf{b}).
\end{aligned}$$

即向量等式
$$\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = (\mathbf{a}\cdot\mathbf{c})\,\mathbf{b} - (\mathbf{a}\cdot\mathbf{b})\,\mathbf{c}.$$

### 附录：为什么 $\varepsilon_{ijk}\varepsilon_{klm} = \delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}$？

**第一步：观察对称性。**
左边对 $(i,j)$ 反对称，对 $(l,m)$ 也反对称。右边 $\delta_{il}\delta_{jm} - \delta_{im}\delta_{jl}$ 同样具有这些对称性。两边都是四阶张量。

**第二步：枚举非零情况。**
因为 $\varepsilon_{ijk}$ 只有 $k$ 与 $(i,j)$ 都不同时才非零，所以只需考虑 $i\neq j$ 且 $l\neq m$ 的情况。取一组具体值即可确定系数，例如取 $i=1,j=2,l=1,m=2$：

- 左边：$\varepsilon_{12k}\varepsilon_{k12} = \varepsilon_{123}\varepsilon_{312} = (+1)(+1) = 1$（只有 $k=3$ 有贡献）。
- 右边：$\delta_{11}\delta_{22} - \delta_{12}\delta_{21} = 1\cdot1 - 0\cdot0 = 1$。

再取 $i=1,j=2,l=2,m=1$：
- 左边：$\varepsilon_{12k}\varepsilon_{k21} = \varepsilon_{123}\varepsilon_{321} = (+1)(-1) = -1$。
- 右边：$\delta_{12}\delta_{21} - \delta_{11}\delta_{22} = 0\cdot0 - 1\cdot1 = -1$。

对于指标相同的情况（如 $i=j$），左边因 $\varepsilon_{ijk}=0$ 而为 0，右边 $\delta_{il}\delta_{jl} - \delta_{il}\delta_{jl} = 0$ 也为 0。由于反对称性完全确定，故此恒等式对所有 $i,j,l,m$ 成立。

> **更系统的推导**：利用行列式表示 $\varepsilon_{ijk}=\det(\mathbf{e}_i,\mathbf{e}_j,\mathbf{e}_k)$，以及正交矩阵行列式性质，或直接利用恒等式
> $$\varepsilon_{ijk}\varepsilon_{lmn} = \begin{vmatrix} \delta_{il} & \delta_{im} & \delta_{in} \\ \delta_{jl} & \delta_{jm} & \delta_{jn} \\ \delta_{kl} & \delta_{km} & \delta_{kn} \end{vmatrix}$$
> 然后令 $k=n$ 并收缩（求和），即得上式。

### 为什么它是“万能钥匙”？

几乎所有矢量代数恒等式都可以用它一步推出：

| 恒等式 | 指标法推导 |
|--------|-----------|
| $\mathbf{A}\cdot(\mathbf{B}\times\mathbf{C}) = \mathbf{B}\cdot(\mathbf{C}\times\mathbf{A})$ | $\varepsilon_{ijk}A_iB_jC_k = \varepsilon_{jki}B_jC_kA_i$（轮换指标） |
| $(\mathbf{A}\times\mathbf{B})\cdot(\mathbf{C}\times\mathbf{D}) = (\mathbf{A}\cdot\mathbf{C})(\mathbf{B}\cdot\mathbf{D}) - (\mathbf{A}\cdot\mathbf{D})(\mathbf{B}\cdot\mathbf{C})$ | 两个 $\varepsilon$ 合并后直接出现 $\delta\delta$ |
| $|\mathbf{A}\times\mathbf{B}|^2 = |\mathbf{A}|^2|\mathbf{B}|^2 - (\mathbf{A}\cdot\mathbf{B})^2$ | 上式令 $\mathbf{C}=\mathbf{A},\mathbf{D}=\mathbf{B}$ 即得 |

因此，在电动力学、量子场论、流体力学中，记住 $\varepsilon\varepsilon = \delta\delta - \delta\delta$ 这一条，胜过死记十几个恒等式。

---

## 证明三：几何+待定系数法

### 第一步：确定方向

- $\mathbf{b}\times\mathbf{c}$ 垂直于 $\mathbf{b}$ 与 $\mathbf{c}$ 张成的平面（记为 $\Pi$）。
- 再对 $\mathbf{a}$ 做一次叉积，$\mathbf{a}\times(\mathbf{b}\times\mathbf{c})$ 垂直于 $\mathbf{b}\times\mathbf{c}$，因此它**必定落在平面 $\Pi$ 内**。

于是可设
$$\mathbf{a}\times(\mathbf{b}\times\mathbf{c}) = \lambda\,\mathbf{b} + \mu\,\mathbf{c},$$
其中 $\lambda,\mu$ 是与 $\mathbf{a},\mathbf{b},\mathbf{c}$ 有关的标量。

### 第二步：确定系数

将上式两边同时点乘 $\mathbf{a}$：
$$\mathbf{a}\cdot\bigl[\mathbf{a}\times(\mathbf{b}\times\mathbf{c})\bigr] = \lambda(\mathbf{a}\cdot\mathbf{b}) + \mu(\mathbf{a}\cdot\mathbf{c}).$$

左边是混合积 $\mathbf{a}\cdot[\mathbf{a}\times(\cdots)]$，因为有两个相同的 $\mathbf{a}$，故为 $0$。于是
$$\lambda(\mathbf{a}\cdot\mathbf{b}) + \mu(\mathbf{a}\cdot\mathbf{c}) = 0 \quad\Longrightarrow\quad \frac{\lambda}{\mathbf{a}\cdot\mathbf{c}} = -\frac{\mu}{\mathbf{a}\cdot\mathbf{b}} \equiv \alpha.$$

可取
$$\lambda = \alpha\,(\mathbf{a}\cdot\mathbf{c}), \qquad \mu = -\alpha\,(\mathbf{a}\cdot\mathbf{b}).$$

为求常数 $\alpha$，取一个最简特例：令 $\mathbf{a}=\mathbf{b}=\hat{x}$，$\mathbf{c}=\hat{y}$。直接计算得
$$\hat{x}\times(\hat{x}\times\hat{y}) = \hat{x}\times\hat{z} = -\hat{y}.$$

另一方面，按待定系数形式：
$$\lambda\hat{x} + \mu\hat{y} = \alpha(0)\hat{x} - \alpha(1)\hat{y} = -\alpha\hat{y}.$$

比较得 $\alpha=1$。因此
$$\lambda = \mathbf{a}\cdot\mathbf{c}, \qquad \mu = -(\mathbf{a}\cdot\mathbf{b}),$$
即得所求。

---

## 记忆口诀

**BAC–CAB**：中间向量（B）点乘外侧向量（C）的系数，减去后面向量（C）点乘外侧向量（B）的系数。

$$\mathbf{A}\times(\mathbf{B}\times\mathbf{C}) = \mathbf{B}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{C}(\mathbf{A}\cdot\mathbf{B})$$

---

## 相关笔记

- [[矢量分析/矢量恒等式总结]] — 所有常用矢量恒等式速查
- [[矢量分析/Lagrange恒等式]] — 由 BAC–CAB 可推出的 $|\mathbf{A}\times\mathbf{B}|^2$ 恒等式

---

## 导航链接
- [[../知识库导航|知识库总导航]] — 查看所有知识领域
- [[矢量分析索引]] — 矢量分析知识总览

## 跨领域联系
- [[../电磁学/电磁学整理索引|电磁学整理索引]] — 电磁学应用
- [[../经典力学/经典力学索引|经典力学索引]] — 经典力学应用
