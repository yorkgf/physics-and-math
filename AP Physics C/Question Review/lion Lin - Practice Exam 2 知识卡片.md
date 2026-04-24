# lion Lin · Practice Exam 2 知识卡片

> [!abstract]+ 考试总览
> MCQ 基础还可以，但 **FRQ 与 MCQ 之间有巨大差距**（约 23 个百分点），说明你的方程建立和推导书写需要系统训练。概念理解有基础，但一到需要自己从头推导的题目就容易出错。需要在势能图（两题全错）、运动学中的积分思想以及万有引力三个领域重点突破。

> [!danger]+ 最优先：FRQ 书写提升
> 你的 FRQ 问题不在物理概念，而在**推导过程写不完整**。练习方法：
> - 找一道做过的 FRQ，遮住答案，自己从头写一遍完整推导
> - 与标准答案对比，找出自己跳了哪些步骤
> - 每周至少练 2 道完整 FRQ

---

## 一、势能图（2 题全错）— 最优先

### PE230 · 粒子在 $U$-$x$ 图中的行为

> [!important]+ 核心直觉
> 粒子在势能图中**趋向势能低处运动**，就像小球滚向山谷。
> $$F = -\frac{dU}{dx}$$
> - 粒子加速方向 = 力的方向 = 势能下降最快的方向
> - 稳定平衡点 = 势能极小值（谷底）

### PE231 · 从 $U$-$x$ 图求力

> [!important]+ 图像读法
> **力 = 斜率取负**：
> 
> | 斜率 | $F$ | 含义 |
> |------|-----|------|
> | 正（$U$ 上升） | 负 | 力向左 |
> | 负（$U$ 下降） | 正 | 力向右 |
> | 零 | 零 | 平衡点 |
> 
> > [!tip]+ 做法
> > 1. 在给定 $x$ 处画切线
> > 2. 求切线斜率 $= dU/dx$
> > 3. $F = -(\text{斜率})$

---

## 二、万有引力与圆周（3 题全错）

### PE210 · 逃逸速度

> [!important]+ 推导
> 逃逸条件：天体表面物体总机械能 = 0
> $$\frac{1}{2}mv_{esc}^2 - \frac{GMm}{R} = 0 \;\Rightarrow\; \boxed{v_{esc} = \sqrt{\frac{2GM}{R}}}$$
> 
> ⚠️ $v_{esc} = \sqrt{2}\,v_{orb}$，不是 $\sqrt{gR}$。

### PE229 · 转弯向心力

> [!important]+ 核心关系
> 车辆在弯道：**静摩擦力**提供**向心力**
> $$f_s = \frac{mv^2}{R}$$
> 不滑出的条件：$f_s \leq \mu_s mg$。转弯半径 $R$ 越小 → 所需 $f_s$ 越大 → 越容易打滑。

### PE235 · 星球内部引力

> [!important]+ 关键结论
> 均匀球体内部，距球心 $r$ 处只有**半径 $r$ 以内的质量**产生引力：
> $$g(r) = g_{surface} \cdot \frac{r}{R}$$
> 引力随 $r$ **线性减小**（不是反比平方！反比平方只在球外成立）。

---

## 三、运动学（3 题错误）

### PE201 · $a$-$t$ 图积分为 $v$

> [!important]+ 积分思想
> 速度是加速度的积分：$\Delta v = \int_{t_1}^{t_2} a(t)\,dt$
> $a$-$t$ 图下的**面积** = 速度变化量。初速为零时，$v$ = 面积。

### PE217 · 自由落体位移比

> [!important]+ 核心规律
> $\Delta y_n \propto t_n^2 - t_{n-1}^2 \;\Rightarrow\;$ 连续等时间间隔位移比 $= 1:3:5:7:\dots$
> 
> 推导：第 $n$ 个 $\Delta t$ 内：$\Delta y = \frac{1}{2}g[(n\Delta t)^2 - ((n-1)\Delta t)^2] = \frac{1}{2}g(2n-1)(\Delta t)^2$

### PE221 · 抛体射程=高度

> [!important]+ 推导条件
> $R = v_0\cos\theta \cdot t_{flight}$，$h_{max} = v_0^2\sin^2\theta/(2g)$
> 令 $R = h_{max}$，结合 $t_{flight} = 2v_0\sin\theta/g$，解得 $\tan\theta = 4$。

---

## 四、力矩与转动

### PE205 · 物理摆

> [!important]+ $\alpha = -C\theta$ 法推导
> 
> **第 1 步**：回复力矩 $\tau = -mgd\sin\theta \approx -mgd\,\theta$
> **第 2 步**：转动方程 $I\alpha = -mgd\,\theta$
> **第 3 步**：写成 $\alpha = -\frac{mgd}{I}\theta$
> **第 4 步**：对比 $\alpha = -\omega^2\theta$，直接读出
> $$\boxed{\omega = \sqrt{\frac{mgd}{I}}} \qquad \boxed{T = 2\pi\sqrt{\frac{I}{mgd}}}$$
> 
> ⚠️ **必须用平行轴定理** $I = I_{CM} + md^2$。
> 
> 参见 [[Physical Pendulum SHM - Knowledge Card]]

### PE237 · 最小转动惯量

> [!important]+ 原理
> $I$ 最小的轴通过**质心**。任何偏离质心的轴都因 $md^2$ 项使 $I$ 增大。角动量守恒下，$I$ 最小 → $\omega$ 最大 → 旋转最稳定。

---

## 五、动量与冲量

### PE207 · $F$-$t$ 图面积

> [!important]+ 冲量计算
> $J = \int F\,dt$ = $F$-$t$ 图下的**面积** = $\Delta p$
> 对于简单图形（矩形、三角形），直接算面积；复杂形状分段计算。

### PE232 · 2D 冲量积分

> [!important]+ 分量独立
> $\vec{J} = \left(\int F_x\,dt\right)\hat{i} + \left(\int F_y\,dt\right)\hat{j}$
> 每个分量单独积分，然后矢量合成。

---

## 六、功与能量

### PE225 · SHM 最大势能

> [!important]+ 核心公式
> $E_{total} = \frac{1}{2}kA^2$
> 最大势能 = 总能量 = $\frac{1}{2}kA^2$（在最大位移处，动能 = 0）。

### PE226 · 转动能量与摩擦

> [!important]+ 能量损失
> 有摩擦时：$\Delta E = -f_k \cdot d$（摩擦力做功 = 机械能损失）
> 无摩擦时：机械能守恒，$K_{trans} + K_{rot} + U =$ 常数。

---

## 七、简谐运动 · 质心补充

> [!tip]+ PE227 · $a$-$t$ 图求振幅
> $a_{max} = \omega^2 A \;\Rightarrow\; A = a_{max}/\omega^2$。从图上读 $a_{max}$，$\omega$ 从周期得到。

> [!tip]+ PE240 · 质心位置
> $\vec{r}_{CM} = \frac{\sum m_i\vec{r}_i}{\sum m_i}$。机械臂+手：分别算质量与位置，加权平均。

---

## 推荐复习链接

- [[Physical Pendulum SHM - Knowledge Card]]
- [[Conservation of Energy - Knowledge Card]]
- [[Simple Harmonic Motion]]
- [[Satellite Orbital Motion]]
- [[题库/PE201]] · [[题库/PE205]] · [[题库/PE207]] · [[题库/PE210]] · [[题库/PE217]] · [[题库/PE221]] · [[题库/PE225]] · [[题库/PE226]] · [[题库/PE227]] · [[题库/PE229]] · [[题库/PE230]] · [[题库/PE231]] · [[题库/PE232]] · [[题库/PE235]] · [[题库/PE237]] · [[题库/PE240]]
