# Hessian Matrix

> **Hessian matrix** — the matrix of second-order partial derivatives of a multivariable function. It is the second-order companion to the gradient: the gradient tells you the slope, the Hessian tells you the curvature.

*Status: overview note — recorded for later deep study (2026-11-08).*

## Knowledge Map

```mermaid
%%{init: {'themeVariables': {'edgeLabelBackground': 'transparent'}}}%%
graph LR
    A[Hessian Matrix] --> B[Definition]
    A --> C[Three main uses]
    A --> D[Relation to gradient]

    B --> B1[Matrix of second partials]
    B --> B2[Symmetric when f_xy = f_yx]
    B --> B3[n x n for n variables]

    C --> C1[Second directional derivative]
    C --> C2[Extremum (second derivative) test]
    C --> C3[Curvature / geometry]

    D --> D1[Gradient = 1st order info]
    D --> D2[Hessian = 2nd order info]
    D --> D3[Newton's method uses H^-1]

    C2 --> C1[Max/min/saddle classification]
    C3 --> C1[Eigenvalues = principal curvatures]
```

---

## 1. Definition

For a function $f(x,y)$ with continuous second partials:

$$H_f = \begin{pmatrix} f_{xx} & f_{xy} \\ f_{yx} & f_{yy} \end{pmatrix} = \begin{pmatrix} \dfrac{\partial^2 f}{\partial x^2} & \dfrac{\partial^2 f}{\partial x \partial y} \\[6pt] \dfrac{\partial^2 f}{\partial y \partial x} & \dfrac{\partial^2 f}{\partial y^2} \end{pmatrix}$$

- By **Clairaut's theorem** (mixed partials continuous), $f_{xy} = f_{yx}$, so $H_f$ is **symmetric**.
- For $n$ variables it is the $n \times n$ matrix $H_{ij} = \partial^2 f / \partial x_i \partial x_j$.
- Notation: sometimes $H_f(\mathbf{x})$, $\nabla^2 f$ (also called the Laplacian operator when traced), or $\mathrm{Hess}(f)$.

**Example.** $f(x,y) = x^3 + 5x^2 y + y^3$ (Stewart 14.6 #39):

$$f_{xx} = 6x + 10y, \quad f_{xy} = 10x, \quad f_{yy} = 6y \;\Rightarrow\; H_f = \begin{pmatrix} 6x+10y & 10x \\ 10x & 6y \end{pmatrix}$$

At $(2,1)$: $H_f = \begin{pmatrix} 22 & 20 \\ 20 & 6 \end{pmatrix}$.

---

## 2. Main Uses

### 2.1 Second directional derivative (used in Stewart #39)

$$D_{\mathbf{u}}^2 f = \nabla(D_{\mathbf{u}} f)\cdot \mathbf{u} = \mathbf{u}^T H_f\, \mathbf{u}$$

Expanded for a unit vector $\mathbf{u} = (u_1, u_2)$:

$$D_{\mathbf{u}}^2 f = f_{xx}u_1^2 + 2f_{xy}u_1u_2 + f_{yy}u_2^2$$

This compresses "take $D_{\mathbf{u}} f$, then take its gradient, then dot with $\mathbf{u}$" into one quadratic form.

> For #39: $\mathbf{u} = (3/5, 4/5)$ at $(2,1)$ gives
> $22\cdot\tfrac{9}{25} + 40\cdot\tfrac{12}{25} + 6\cdot\tfrac{16}{25} = \dfrac{774}{25} = 30.96$.

### 2.2 Second derivative test for extrema

At a critical point where $\nabla f = \mathbf{0}$, let

$$D = \det H_f = f_{xx}f_{yy} - f_{xy}^2$$

| Condition | Conclusion |
|-----------|------------|
| $D > 0$ and $f_{xx} > 0$ | local **minimum** |
| $D > 0$ and $f_{xx} < 0$ | local **maximum** |
| $D < 0$ | **saddle point** |
| $D = 0$ | test **inconclusive** |

This is the exact multivariable analogue of the single-variable $f''(x)$ test.

### 2.3 Curvature / geometry of the surface

- **Eigenvalues** of $H_f$ give the second-derivative growth rates along the **eigenvector** directions (principal directions).
- All eigenvalues $> 0$ → surface opens upward (bowl / valley, local min).
- All eigenvalues $< 0$ → surface opens downward (hill, local max).
- Mixed signs → saddle.
- Magnitude of eigenvalues = how sharply the surface bends that way.

### 2.4 In optimization (preview for later study)

- **Newton's method:** $\mathbf{x}_{\text{new}} = \mathbf{x} - H_f^{-1}\nabla f$ — uses curvature to take smarter steps than plain gradient descent.
- In machine learning, $H_f$ describes the **loss landscape curvature**; its spectrum governs condition number and convergence speed of gradient methods.

---

## 3. Gradient vs Hessian

| | Gradient $\nabla f$ | Hessian $H_f$ |
|---|---|---|
| Order | first derivatives | second derivatives |
| Type | vector ($n\times 1$) | matrix ($n\times n$) |
| Tells you | direction of steepest ascent, rate | curvature, how slope itself changes |
| Key use | directional derivatives, optimization steps | extremum test, second directional derivative, Newton's method |
| Single-variable analog | $f'(x)$ | $f''(x)$ |

> **One-line summary:** gradient = first-order information; Hessian = second-order information.

---

## Common Confusions

| Concept | Correct | Wrong |
|---------|---------|-------|
| $f_{xy}$ vs $f_{yx}$ | Equal when mixed partials are continuous (Clairaut) | Thinking they can always differ |
| $D = \det H$ at a critical point | $D>0$ with $f_{xx}>0$ → min; $D>0$ with $f_{xx}<0$ → max | Using $f_{xx}>0$ alone (that's only the 1-D rule) |
| $D < 0$ | saddle point | "No conclusion" (only $D=0$ is inconclusive) |
| $\mathbf{u}^T H \mathbf{u}$ | $f_{xx}u_1^2 + 2f_{xy}u_1u_2 + f_{yy}u_2^2$ | Forgetting the factor 2 on the cross term |
| $\nabla^2 f$ | Sometimes means the Hessian matrix, sometimes the **trace** (Laplacian) $f_{xx}+f_{yy}$ | Assuming one meaning everywhere |

---

## Formula Sheet

| Item | Formula |
|------|---------|
| Definition | $H_{ij} = \partial^2 f / \partial x_i \partial x_j$ |
| Second directional derivative | $D_{\mathbf{u}}^2 f = \mathbf{u}^T H_f \mathbf{u}$ |
| Expanded (2D) | $f_{xx}u_1^2 + 2f_{xy}u_1u_2 + f_{yy}u_2^2$ |
| Discriminant | $D = f_{xx}f_{yy} - f_{xy}^2$ |
| Newton step | $\mathbf{x} - H_f^{-1}\nabla f$ |

---

## To Explore Later (deep study backlog)

- [ ] Eigen-decomposition of $H_f$: principal axes, relation to Taylor expansion $f(\mathbf{x}+\mathbf{h}) \approx f(\mathbf{x}) + \nabla f\cdot\mathbf{h} + \tfrac12 \mathbf{h}^T H \mathbf{h}$
- [ ] Positive / negative **semidefinite** definitions and their role in constrained optimization (Lagrange multipliers, KKT)
- [ ] Hessian in statistics: Fisher information, covariance of MLE
- [ ] Why Newton's method converges quadratically; damped / quasi-Newton (BFGS) when $H$ is unavailable or singular
- [ ] Numerical computation of $H$ (finite differences, automatic differentiation)

---

## Related Notes

- [[数学/概率论/核密度估计]] — smoothing / curvature appears in density estimation
- Gradient, directional derivatives, and level curves: see the Stewart §14.6 problem set (exercises 27–39) this note was created alongside
