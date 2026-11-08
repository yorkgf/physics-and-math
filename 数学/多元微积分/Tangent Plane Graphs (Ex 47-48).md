# Tangent Plane Graphs — Exercises 47–48

> Stewart §14.6, exercises 47–48: graph the surface, the tangent plane, and the normal line on the same screen, choosing the domain to avoid extraneous vertical planes.

**Method:** for a surface \(F(x,y,z) = \text{const}\), the gradient \(\nabla F\) at the point is the normal vector of the tangent plane.

---

## Exercise 47 — \(xy + yz + zx = 3\) at \((1,1,1)\)

\[
F = xy + yz + zx - 3, \qquad \nabla F = (y+z,\; x+z,\; x+y)
\]

At \((1,1,1)\): \(\nabla F = (2,2,2) \propto (1,1,1)\)

| Item | Equation |
|------|----------|
| **Tangent plane** | \(x + y + z = 3\) |
| **Normal line** | \(x = 1+t,\; y = 1+t,\; z = 1+t\) |

**Plot setup:** explicit form \(z = \dfrac{3-xy}{x+y}\). The denominator vanishes on the line \(x+y=0\) (an extraneous vertical plane), so the domain excludes a strip around it: \(x, y \in [-0.4,\, 3.6]\) with \(|x+y| \ge 0.6\), and \(z\) clipped to \([-3.5,\, 5.5]\).

![[ex47.png]]

*Surface \(z=(3-xy)/(x+y)\) (colored), tangent plane \(x+y+z=3\) (orange), normal line (red) through \((1,1,1)\).*

---

## Exercise 48 — \(xyz = 6\) at \((1,2,3)\)

\[
F = xyz - 6, \qquad \nabla F = (yz,\; xz,\; xy)
\]

At \((1,2,3)\): \(\nabla F = (6,3,2)\)

| Item | Equation |
|------|----------|
| **Tangent plane** | \(6(x-1) + 3(y-2) + 2(z-3) = 0 \;\Rightarrow\; 6x + 3y + 2z = 18\) |
| **Normal line** | \(x = 1+6t,\; y = 2+3t,\; z = 3+2t\) |

**Plot setup:** explicit form \(z = \dfrac{6}{xy}\). The extraneous vertical planes are \(x = 0\) and \(y = 0\); restrict to the first quadrant \(x, y \in [0.3,\, 4.2]\), clip \(z \le 30\) to suppress the asymptotic spike, and set \(z \in [-4,\, 16]\) so the tangent plane is fully visible.

![[ex48.png]]

*Surface \(z=6/(xy)\) (colored), tangent plane \(6x+3y+2z=18\) (orange), normal line (red) through \((1,2,3)\).*

---

## Reading the figures

- The tangent plane touches the surface only at the marked point and has the same slope there — first-order contact.
- The normal line is perpendicular to the plane (direction \(\nabla F\)) and pierces the surface at the point of tangency.
- In 47, \(\nabla F = (1,1,1)\) makes the normal line the diagonal \(x=y=z\); the plane \(x+y+z=3\) is perpendicular to it.
- In 48, the normal direction \((6,3,2)\) is steepest in \(x\), reflecting that \(xyz\) grows fastest along \(x\) at \((1,2,3)\) (since \(yz = 6 > xz = 3 > xy = 2\)).

## Reproduce

Script: [[img/plot_47_48.py]] (matplotlib, run `python3 img/plot_47_48.py`). Outputs `img/ex47.png`, `img/ex48.png`.

## Related Notes

- [[数学/多元微积分/Hessian Matrix]] — second-order companion to the gradient
- Exercises 41–46 (tangent plane / normal line drill) and 51–53 (quadric tangent-plane formulas) solved in the same section
