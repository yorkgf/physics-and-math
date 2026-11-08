"""Plot surface + tangent plane + normal line for Stewart exercises 47-48."""

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401

OUT = "/home/yorkgf/Documents/Obsidian Vault/img"


# ---- Exercise 47: xy + yz + zx = 3 at (1,1,1) -----------------------------
# z = (3 - xy)/(x + y), tangent plane z = 3 - x - y, normal dir (1,1,1)
fig = plt.figure(figsize=(8, 6.5))
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(-0.4, 3.6, 160)
y = np.linspace(-0.4, 3.6, 160)
X, Y = np.meshgrid(x, y)
den = X + Y
Z = (3 - X * Y) / den
Z = np.ma.masked_where((np.abs(den) < 0.6) | (Z < -3.5) | (Z > 5.5), Z)

# plot_surface needs Z(X, Y); build plane grid explicitly
XP, YP = np.meshgrid(np.linspace(-0.4, 3.6, 40), np.linspace(-0.4, 3.6, 40))
ZP = 3 - XP - YP
ZP = np.ma.masked_where(np.abs(XP + YP) < 0.6, ZP)

ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8,
                linewidth=0, antialiased=True)
ax.plot_surface(XP, YP, ZP, color="tab:orange", alpha=0.4,
                linewidth=0, antialiased=True)

t = np.linspace(-1.1, 1.1, 50)
ax.plot(1 + t, 1 + t, 1 + t, color="red", linewidth=3.5, label="normal line")
ax.scatter(1, 1, 1, color="red", s=70, depthshade=False, zorder=6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_zlim(-3.5, 5.5)
ax.set_title("47: $xy+yz+zx=3$  ·  tangent plane $x+y+z=3$  at $(1,1,1)$",
             fontsize=12)
ax.view_init(elev=26, azim=-58)
fig.tight_layout()
fig.savefig(f"{OUT}/ex47.png", dpi=200)
plt.close(fig)

# ---- Exercise 48: xyz = 6 at (1,2,3) -------------------------------------
# z = 6/(xy), tangent plane 6x + 3y + 2z = 18, normal dir (6,3,2)
fig = plt.figure(figsize=(8, 6.5))
ax = fig.add_subplot(111, projection="3d")

x = np.linspace(0.3, 4.2, 160)
y = np.linspace(0.3, 4.2, 160)
X, Y = np.meshgrid(x, y)
Z = 6.0 / (X * Y)
Z = np.ma.masked_where(Z > 30, Z)

XP, YP = np.meshgrid(np.linspace(0.3, 4.2, 40), np.linspace(0.3, 4.2, 40))
ZP = (18 - 6 * XP - 3 * YP) / 2.0

ax.plot_surface(X, Y, Z, cmap="viridis", alpha=0.8,
                linewidth=0, antialiased=True)
ax.plot_surface(XP, YP, ZP, color="tab:orange", alpha=0.45,
                linewidth=0, antialiased=True)

t = np.linspace(-0.55, 0.75, 50)
ax.plot(1 + 6 * t, 2 + 3 * t, 3 + 2 * t, color="red", linewidth=3.5,
        label="normal line")
ax.scatter(1, 2, 3, color="red", s=70, depthshade=False, zorder=6)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_zlim(-4, 16)
ax.set_title("48: $xyz=6$  ·  tangent plane $6x+3y+2z=18$  at $(1,2,3)$",
             fontsize=12)
ax.view_init(elev=24, azim=-58)
fig.tight_layout()
fig.savefig(f"{OUT}/ex48.png", dpi=200)
plt.close(fig)

print("saved ex47.png, ex48.png")
