# 力学微分方程 · 知识卡片

> [!summary]+ 核心概念
> 力学中求解 $v(t)$、$x(t)$ 等运动函数的**两种核心方法**：分离变量法（变量可分离时）和积分因子法（一阶线性方程通用解法）。

---

## 方法选择

```
已知 dv/dt = f(v, t)
        │
        ├── 可写成 dv/dt = f(v)·g(t) ──→ 分离变量法
        │
        └── 形如 dy/dt + P(t)y = Q(t) ──→ 积分因子法
```

---

## 方法 1：分离变量法

| 步骤 | 操作 | 示例：$m\dot{v} = mg - bv$ |
|------|------|---------------------------|
| ① 分离 | $\frac{dy}{f(y)} = g(t)\,dt$ | $\frac{dv}{mg-bv} = \frac{dt}{m}$ |
| ② 积分 | $\int \frac{dy}{f(y)} = \int g(t)\,dt$ | $-\frac{1}{b}\ln\|mg-bv\| = \frac{t}{m}+C$ |
| ③ 求解 | 解出 $y(t)$ | $v = \frac{mg}{b} - Ce^{-bt/m}$ |
| ④ 初条件 | 代入 $t=0$ | $v(0)=0 \to C=\frac{mg}{b}$ |

> [!tip]+ 最终解
> $$v(t) = \frac{mg}{b}\left(1 - e^{-bt/m}\right), \quad v_\infty = \frac{mg}{b}$$

---

## 方法 2：积分因子法

| 步骤 | 操作 |
|------|------|
| ① 标准化 | $\frac{dy}{dt} + P(t)y = Q(t)$ |
| ② 求因子 | $\mu(t) = e^{\int P(t)\,dt}$ |
| ③ 乘因子 | $\frac{d}{dt}[\mu y] = \mu Q$ |
| ④ 积分 | $\mu y = \int \mu Q\,dt + C$ |
| ⑤ 解出 | $y = \frac{1}{\mu}\left(\int \mu Q\,dt + C\right)$ |

> [!example]+ RL 电路示例
> $L\frac{di}{dt} + Ri = \mathcal{E}$
> → $\mu = e^{Rt/L}$ → $i(t) = \frac{\mathcal{E}}{R}(1 - e^{-Rt/L})$

---

## 两法对比

| | 分离变量法 | 积分因子法 |
|------|------------|------------|
| **适用** | $\frac{dy}{dt} = f(y)g(t)$ | $\frac{dy}{dt} + P(t)y = Q(t)$ |
| **关键操作** | 分离后分别积分 | 乘以 $\mu = e^{\int P dt}$ |
| **典型场景** | 速度相关阻力、衰变 | RL 电路、受迫振动 |
| **难度** | 直观简单 | 需识别标准形式 |

---

## 常见解的结构

$$v(t) = v_{\infty} + (v_0 - v_{\infty})e^{-t/\tau}$$

| 参数 | 含义 | 线性阻力示例 |
|------|------|-------------|
| $v_{\infty}$ | 终速 | $mg/b$ |
| $\tau$ | 时间常数 | $m/b$ |
| $v_0$ | 初速 | 初始条件确定 |

### 时间常数规律

| 时间 | 接近终值的程度 |
|------|--------------|
| $t = \tau$ | 63% |
| $t = 3\tau$ | 95% |
| $t = 5\tau$ | 99% |

---

## 易错提醒

| # | 错误 | 正确 |
|---|------|------|
| 1 | $\ln(mg-bv)$ 遗漏绝对值 | $\ln\|mg-bv\|$ |
| 2 | 积分前代入初条件 | 积分后代入，求常数 $C$ |
| 3 | 指数 $\frac{bt}{m}$ 带量纲 | 检查指数无量纲 |
| 4 | 符号方向不一致 | 统一正方向再列方程 |
| 5 | 强行用分离变量 | 检查是否需积分因子 |

---

## 例题索引

| 例题 | 方法 | 关键方程 |
|------|------|----------|
| [[Example 1 - Sphere with Air Resistance\|Ex.1]] | 分离变量 | $\dot{v} = -g - \frac{b}{m}v$ |
| [[Example 2 - Box with Time-Varying Force\|Ex.2]] | 直接积分 | $\dot{v} = \frac{F_0}{M}e^{-Bt} - \mu_k g$ |
| [[Example 3 - Stone in Water\|Ex.3]] | 分离变量 | $\dot{v} = g - \frac{B}{m} - \frac{k}{m}v$ |

## 相关链接

- [[Friction Forces]] — 阻尼运动中的应用
- [[Atwood Machine]] — 变质量系统
- [[Unit 2 Force and Translational Dynamics Index]] — Unit 2 索引
- [[Unit 7 Oscillations Index]] — Unit 7（受迫振动）
- [[../经典力学/曲线坐标系加速度推导]] — 曲线坐标中的微分方程
