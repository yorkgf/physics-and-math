# 物理摆 SHM · 知识卡片

> [!summary]+ 核心概念
> **物理摆**是绕非质心轴摆动的刚体。在小角度下，重力产生的回复力矩导致角简谐运动：$\alpha = -\omega^2\theta$，其中 $\omega = \sqrt{mgd/I}$。

---

## 推导链

$$\tau = -mgd \sin\theta \quad \xrightarrow{\sin\theta \approx \theta} \quad I\alpha = -mgd\,\theta \quad \xrightarrow{\tau = I\alpha} \quad \alpha = -\frac{mgd}{I}\theta$$

$$\xrightarrow{\text{SHM标准形式} \ \alpha = -\omega^2\theta} \quad \boxed{\omega = \sqrt{\frac{mgd}{I}}} \quad \xrightarrow{T = 2\pi/\omega} \quad \boxed{T = 2\pi\sqrt{\frac{I}{mgd}}}$$

---

## 公式速查

| 公式 | 说明 |
|------|------|
| $\tau = -mgd\sin\theta$ | 回复力矩 |
| $\alpha = -\frac{mgd}{I}\theta$ | 角 SHM 微分方程 |
| $\omega = \sqrt{mgd/I}$ | 角频率 |
| $T = 2\pi\sqrt{I/mgd}$ | **物理摆周期（核心）** |
| $I = I_{CM} + md^2$ | 平行轴定理求 $I$ |

---

## 参数

| 符号 | 含义 |
|------|------|
| $m$ | 刚体质量 |
| $d$ | 转轴到质心距离 |
| $I$ | 绕转轴的转动惯量 |
| $\theta$ | 角位移（须 $\theta \ll 1$） |

---

## 特例：单摆

$$I = mL^2,\ d = L \quad \Rightarrow \quad \boxed{T = 2\pi\sqrt{\frac{L}{g}}}$$

---

## 与弹簧振子对比

| | 弹簧振子 | 物理摆 |
|------|----------|--------|
| **方程** | $a = -\frac{k}{m}x$ | $\alpha = -\frac{mgd}{I}\theta$ |
| **$\omega$** | $\sqrt{k/m}$ | $\sqrt{mgd/I}$ |
| **$T$** | $2\pi\sqrt{m/k}$ | $2\pi\sqrt{I/mgd}$ |
| **近似条件** | 胡克定律 | 小角度 $\theta \ll 1$ |

---

## 常见几何体的 $I_{CM}$ 和 $d$

| 刚体形状 | $I_{CM}$ | 典型 $d$ | 平行轴后 $I$ |
|----------|----------|---------|-------------|
| 均匀细杆（端点悬挂） | $\frac{1}{12}mL^2$ | $L/2$ | $\frac{1}{3}mL^2$ |
| 均匀圆盘（边缘悬挂） | $\frac{1}{2}mR^2$ | $R$ | $\frac{3}{2}mR^2$ |
| 质点（单摆） | $0$ | $L$ | $mL^2$ |

---

## 易错提醒

- ❌ 忘记用**平行轴定理**：$I \neq I_{CM}$，必须加 $md^2$
- ❌ 混淆 $d$（转轴到质心）和摆长
- ❌ 大角度时仍用 SHM 公式（$\sin\theta \approx \theta$ 仅在 $\theta < 15^\circ$ 时误差 $<1\%$）
- ❌ 物理摆周期公式写反：$T = 2\pi\sqrt{I/mgd}$，不是 $2\pi\sqrt{mgd/I}$

---

## 相关链接

- [[Simple Harmonic Motion]] — SHM 基础
- [[Physical Pendulum]] — 物理摆详解
- [[Conservation of Rotational Energy]] — 转动能量守恒
- [[Unit 7 Oscillations Index]] — Unit 7 索引
