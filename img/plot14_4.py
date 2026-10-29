import math, os

def norm3(v):
    l = math.sqrt(sum(c*c for c in v)) or 1.0
    return [c/l for c in v]

def cmap(t):
    stops = [(0.0,(48,18,90)),(0.22,(46,86,150)),(0.45,(32,150,140)),
             (0.68,(120,200,90)),(0.86,(250,215,80)),(1.0,(253,244,160))]
    t = min(1.0, max(0.0, t))
    for k in range(len(stops)-1):
        a, ca = stops[k]; b, cb = stops[k+1]
        if a <= t <= b:
            u = (t-a)/(b-a)
            return [ca[i]+(cb[i]-ca[i])*u for i in range(3)]
    return list(stops[-1][1])

def render(f, T, cx, cy, hw, out, el_deg=30.0, az_deg=-58.0, N=40,
           W=620, H=470, zshow=0.90):
    xs = [cx-hw + 2*hw*i/(N-1) for i in range(N)]
    ys = [cy-hw + 2*hw*j/(N-1) for j in range(N)]
    F = [[f(x,y) for x in xs] for y in ys]
    e = 1.28                       # tangent plane extends past the surface window
    gx = [cx-e*hw + 2*e*hw*i/(N-1) for i in range(N)]
    gy = [cy-e*hw + 2*e*hw*j/(N-1) for j in range(N)]
    G = [[T(x,y) for x in gx] for y in gy]
    vals = [v for row in F+G for v in row if v == v and abs(v) < 1e6]
    zmin, zmax = min(vals), max(vals)
    if zmax-zmin < 1e-12: zmax = zmin+1e-12
    rx = 2*hw; rz = zmax-zmin
    zs = zshow*rx/rz          # vertical scale
    zmid = 0.5*(zmin+zmax)

    el = math.radians(el_deg); az = math.radians(az_deg)
    d = [math.cos(el)*math.cos(az), math.cos(el)*math.sin(az), math.sin(el)]
    r = [-math.sin(az), math.cos(az), 0.0]
    u = [-math.sin(el)*math.cos(az), -math.sin(el)*math.sin(az), math.cos(el)]

    def proj(x,y,z):
        p = [x-cx, y-cy, (z-zmid)*zs]
        sx = p[0]*r[0]+p[1]*r[1]+p[2]*r[2]
        sy = p[0]*u[0]+p[1]*u[1]+p[2]*u[2]
        dp = p[0]*d[0]+p[1]*d[1]+p[2]*d[2]
        return sx, -sy, dp

    mesh = [[proj(xs[i], ys[j], F[j][i]) for i in range(N)] for j in range(N)]
    gmesh = [[proj(gx[i], gy[j], G[j][i]) for i in range(N)] for j in range(N)]

    allp = [p for row in mesh+gmesh for p in row]
    sxs = [p[0] for p in allp]; sys = [p[1] for p in allp]
    minx, maxx = min(sxs), max(sxs); miny, maxy = min(sys), max(sys)
    m = 34.0
    sc = min((W-2*m)/(maxx-minx or 1), (H-2*m)/(maxy-miny or 1))
    ox = m - minx*sc + ((W-2*m)-(maxx-minx)*sc)/2
    oy = m - miny*sc + ((H-2*m)-(maxy-miny)*sc)/2
    def S(p): return (p[0]*sc+ox, p[1]*sc+oy)

    light = norm3([-0.45,-0.55,0.72])
    polys = []   # (depth, svgstring)

    for j in range(N-1):
        for i in range(N-1):
            q = [mesh[j][i], mesh[j][i+1], mesh[j+1][i+1], mesh[j+1][i]]
            zc = 0.25*(F[j][i]+F[j][i+1]+F[j+1][i+1]+F[j+1][i])
            a = [q[1][0]-q[0][0], q[1][1]-q[0][1], q[1][2]-q[0][2]]
            b = [q[2][0]-q[0][0], q[2][1]-q[0][1], q[2][2]-q[0][2]]
            n = norm3([a[1]*b[2]-a[2]*b[1], a[2]*b[0]-a[0]*b[2], a[0]*b[1]-a[1]*b[0]])
            it = 0.34 + 0.66*abs(n[0]*light[0]+n[1]*light[1]+n[2]*light[2])
            c = cmap((zc-zmin)/rz)
            col = "rgb(%d,%d,%d)" % (int(min(255,c[0]*it)), int(min(255,c[1]*it)), int(min(255,c[2]*it)))
            pts = " ".join("%.1f,%.1f" % S(p) for p in q)
            dep = sum(p[2] for p in q)/4
            polys.append((1, dep, '<polygon points="%s" fill="%s" stroke="%s" stroke-width="0.35"/>' % (pts, col, col)))

    # tangent plane (subdivided so depth sorting works)
    M = 12
    bias = 0.0
    for j in range(M):
        for i in range(M):
            ii0 = int(round(i*(N-1)/M)); ii1 = int(round((i+1)*(N-1)/M))
            jj0 = int(round(j*(N-1)/M)); jj1 = int(round((j+1)*(N-1)/M))
            if ii1 <= ii0 or jj1 <= jj0: continue
            q = [gmesh[jj0][ii0], gmesh[jj0][ii1], gmesh[jj1][ii1], gmesh[jj1][ii0]]
            pts = " ".join("%.1f,%.1f" % S(p) for p in q)
            dep = sum(p[2] for p in q)/4 - bias
            polys.append((0, dep, '<polygon points="%s" fill="#e8622a" fill-opacity="0.50" stroke="#d4551f" stroke-width="0.35"/>' % pts))

    polys.sort(key=lambda t: (t[0], t[1]))
    body = "\n".join(s for _, _, s in polys)
    px, py = S(proj(cx, cy, f(cx, cy)))
    dot = ('<circle cx="%.1f" cy="%.1f" r="4.6" fill="#111" stroke="#fff" stroke-width="1.4"/>' % (px, py))
    svg = ('<svg xmlns="http://www.w3.org/2000/svg" width="%d" height="%d" viewBox="0 0 %d %d">\n'
           '<rect width="100%%" height="100%%" fill="#ffffff"/>\n%s\n%s\n</svg>\n') % (W, H, W, H, body, dot)
    with open(out, "w") as fh:
        fh.write(svg)
    # relative deviation: how far the plane is from the surface in this window
    dev = max(abs(F[j][i]-T(xs[i],ys[j])) for j in range(N) for i in range(N))
    print("%-28s zrange=%.3e  maxdev=%.3e  rel=%.2e" % (os.path.basename(out), rz, dev, dev/rz))

P = math.pi

problems = [
 ("7",  lambda x,y: x*x + x*y + 3*y*y,
        lambda x,y: 3*x + 7*y - 5,           1.0, 1.0, 1.30),
 ("8",  lambda x,y: math.atan(x*y*y),
        lambda x,y: x/2 + y + P/4 - 1.5,     1.0, 1.0, 1.20),
 ("9",  lambda x,y: x*y*math.sin(x-y)/(1+x*x+y*y),
        lambda x,y: (x-y)/3,                 1.0, 1.0, 0.90),
 ("10", lambda x,y: math.exp(-x*y/10)*(math.sqrt(x)+math.sqrt(y)+math.sqrt(x*y)),
        lambda x,y: math.exp(-0.1)*(0.7*x+0.7*y+1.6), 1.0, 1.0, 0.60),
]

outdir = "/home/feng/文档/Obsidian Vault/img"
os.makedirs(outdir, exist_ok=True)
for name, f, T, a, b, hw in problems:
    render(f, T, a, b, hw, os.path.join(outdir, "14.4_ex%s.svg" % name))
    z = hw/12.0      # zoom: window shrunk 12x
    render(f, T, a, b, z, os.path.join(outdir, "14.4_ex%s_zoom.svg" % name))