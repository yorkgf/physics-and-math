# Jerry Chen · Practice Exam 2 知识卡片

> [!abstract]+ 考试总览
> 你的 MCQ 基础不错，但 **FRQ 得分远低于 MCQ**，说明写解题过程的能力需要重点训练。FRQ 中即便知道答案，如果缺少完整的方程建立、推导步骤和文字说明，会大量失分。

> [!danger]+ 最优先：FRQ 解题框架
> FRQ 每题都有"建立方程 → 推导 → 检核"的结构分。你需要一个**固定解题模板**：
> 1. **列出已知量和未知量**（given/find）
> 2. **画出受力图/示意图**
> 3. **写出相关物理方程**（先符号，后代入数字）
> 4. **代数推导**（不要跳步）
> 5. **检查量纲和边界情况**
> 
> 从现在开始，每道题都按这个模板写，形成肌肉记忆。

---

## 一、动量与碰撞（3 题错误）

### PE203 · 爆炸动量守恒

> [!important]+ 核心概念
> 爆炸瞬间内力 ≫ 外力 → **动量守恒**。如果初始动量为零（自由落体到爆炸瞬间？**不对**，砖已在运动）：
> $$m\vec{v}_{before} = m_1\vec{v}_1 + m_2\vec{v}_2$$

> [!warning]+ 注意
> 爆炸前物体有速度！不要默认初动量为零。爆炸后各碎片速度用动量守恒矢量方程求解。

### PE233 · 弹道摆（运动摆）

> [!important]+ 两阶段法
> $$
> \begin{aligned}
> \text{碰撞：}&\quad mv_0 = (m+M)v' \quad\text{（动量守恒）}\\[4pt]
> \text{上升：}&\quad \frac{1}{2}(m+M)v'^2 = (m+M)gh \quad\text{（能量守恒）}
> \end{aligned}
> $$

> [!warning]+ 致命错误
> 在碰撞阶段使用机械能守恒——这是**完全非弹性碰撞**，机械能一定不守恒！碰撞过程只能用动量守恒。

### PE219 · 2D 碰撞动能损失

> [!important]+ 核心方法
> 1. 用动量守恒求末速度（$x$ 和 $y$ 方向分别）
> 2. 计算末动能 $K_f = \frac{1}{2}mv_f^2$
> 3. $\Delta K = K_f - K_i$（负值 = 损失）
> 
> 完全弹性碰撞：$\Delta K = 0$；完全非弹性：$\Delta K$ 最大（负值）。

---

## 二、力矩与转动（3 题错误）

### PE205 · 物理摆（全班覆没）

> [!important]+ $\alpha = -C\theta$ 法求 $\omega$ 和 $T$
> 
> **第 1 步**：回复力矩 $\tau = -mgd\sin\theta \approx -mgd\,\theta$
> **第 2 步**：转动方程 $I\alpha = -mgd\,\theta$
> **第 3 步**：写成 $\alpha = -\frac{mgd}{I}\theta$
> **第 4 步**：对比 $\alpha = -\omega^2\theta$，直接读出
> $$\boxed{\omega = \sqrt{\frac{mgd}{I}}} \qquad \boxed{T = 2\pi\sqrt{\frac{I}{mgd}}}$$
> 
> ⚠️ **必须用平行轴定理**：$I = I_{CM} + md^2$
> 
> 参见 [[Physical Pendulum SHM - Knowledge Card]]

### PE237 · 最小转动惯量

> [!important]+ 核心概念
> 给定总质量和形状，绕**质心轴**的转动惯量最小。
> $$I \geq I_{CM}$$
> 任何偏离质心的轴都会因平行轴定理使 $I$ 增大 $md^2$。

### PE238 · 力矩与角加速度

> [!important]+ 核心公式
> $$\alpha = \frac{\tau}{I}$$
> 相同力矩下，**转动惯量越大，角加速度越小**。圆盘半径不同 → $I = \frac{1}{2}MR^2$ 不同 → $\alpha$ 不同。

---

## 三、简谐运动（2 题错误）

### PE220 · 平衡位置加速度

> [!important]+ 核心概念
> SHM 中 $a = -\omega^2 x$，在**平衡位置** $x = 0$：
> $$a = 0$$
> 不管振幅多大、弹簧多硬，平衡位置的加速度恒为零。此时速度最大。

### PE227 · 从 $a$-$t$ 图求振幅

> [!important]+ 核心方法
> $$a_{max} = \omega^2 A \quad\Rightarrow\quad A = \frac{a_{max}}{\omega^2}$$
> 步骤：
> 1. 从 $a$-$t$ 图读 $a_{max}$
> 2. 找出 $\omega$（可从 $T$ 得到：$\omega = 2\pi/T$）
> 3. 代入 $A = a_{max}/\omega^2$

---

## 四、势能图（PE231）

> [!important]+ $F = -dU/dx$
> 保守力 = 势能曲线**斜率的负值**：
> - 斜率 > 0 → $F < 0$（力指向 $-x$ 方向）
> - 斜率 < 0 → $F > 0$（力指向 $+x$ 方向）
> - 斜率 = 0 → $F = 0$（平衡点）
>   - $U$ 极小值 → **稳定**平衡
>   - $U$ 极大值 → **不稳定**平衡

---

## 五、其他需注意

> [!tip]+ PE221 · 抛体运动射程=高度
> 当水平射程等于最大高度时：$R = h_{max}$
> $$\frac{v_0^2\sin 2\theta}{g} = \frac{v_0^2\sin^2\theta}{2g} \;\Rightarrow\; 2\sin\theta\cos\theta = \frac{1}{2}\sin^2\theta$$
> 解出 $\tan\theta = 4$，即 $\theta \approx 76^\circ$。

> [!tip]+ PE229 · 转弯向心力
> 车辆转弯：静摩擦力提供向心力 $f_s = mv^2/R$。转弯半径越小，所需向心力越大。滚动条件 $v_{CM} = R\omega$。

> [!tip]+ PE218 · 功 $W = Fd\cos\theta$
> 绳子角度不同 → $\cos\theta$ 不同 → 同样 $F$ 和 $d$ 做的功不同。$\theta$ 越小（越平行于位移），$W$ 越大。

> [!tip]+ PE239 · 受力图与加速度方向
> **"向上加速"** = 合力向上。看 FBD 中哪个合力方向向上：$F_{net,y} > 0$。

---

## FRQ 专项建议

你的 FRQ 薄弱主要在于**解题写得太简略**。改正方向：

- [ ] **不要跳步**：每个方程写出来，代入前先写符号表达式
- [ ] **每个子问题之间检查一致性**：FRQ 常要求用 (a) 的结果推导 (b)
- [ ] 练习"解释为什么"类题目：用物理原理（如"由牛顿第三定律…"），不用日常语言

---

## 推荐复习链接

- [[Physical Pendulum SHM - Knowledge Card]]
- [[Conservation of Energy - Knowledge Card]]
- [[Simple Harmonic Motion]]
- [[题库/PE203]] · [[题库/PE205]] · [[题库/PE218]] · [[题库/PE219]] · [[题库/PE220]] · [[题库/PE221]] · [[题库/PE227]] · [[题库/PE229]] · [[题库/PE231]] · [[题库/PE233]] · [[题库/PE237]] · [[题库/PE238]] · [[题库/PE239]]
