# -*- coding: utf-8 -*-
import math
from kaffee_modell import P, rechne
from nachrechnen_koord import lauf
from nachrechnen_nichtlinear import sim, eichen, psat, n43
K = 273.15
r = rechne(P); C_K, C_M, C_G, kA = r["C_K"], r["C_M"], r["C_G"], r["kA"]
Tu = 20.0
# Kipppunkt mit n = 4/3
s = eichen(n43, C_K)
q = lambda th: s * n43(th)
th2K = sim(80.0, C_K, 3600.0, q)
def d(thM):
    th1 = sim((C_K*80 + C_M*thM)/C_G, C_G, 3600.0, q)
    return th1 - (C_K*th2K + C_M*thM)/C_G
lo, hi = 20.0, 80.0
for _ in range(40):
    mid = (lo+hi)/2
    if d(mid) > 0: lo = mid
    else: hi = mid
print(f"Kipppunkt n=4/3: {mid:.2f} °C")
# Tech t6: Schaumschicht senkt kA in Tasse 1 um 30 % für 15 min
T10 = (C_K*(80+K) + C_M*(60+K))/C_G - K
th = 20 + (T10-20)*math.exp(-0.7*kA*900/C_G)
th = 20 + (th-20)*math.exp(-kA*2700/C_G)
th2 = lauf(thM1=60.0)[1]
print(f"Tech t6: Tasse 1 {th:.2f}, Tasse 2 {th2:.2f}, diff {th-th2:.2f} K")
# Verdunstete Masse im Verdunstungsmodell (f_v = 0,5 bei 80 °C, Rest linear bzw. 4/3), Tasse 2
phi = 0.5
for name, rest in (("linear", lambda th: th - Tu), ("4/3", n43)):
    ev = lambda th: max(psat(th) - phi*psat(Tu), 0.0)
    w = 1.0 * rest(80.0)/ev(80.0)
    qf = lambda th: rest(th) + w*ev(th)
    s2 = eichen(qf, C_K)
    th, Qv = 80.0, 0.0
    for _ in range(3600):
        Qv += s2*w*ev(th)
        th -= s2*qf(th)/C_K
    print(f"Verdunstung Rest {name}: Q_v {Qv/1e3:.1f} kJ, m_v {Qv/2380e3*1e3:.1f} g, Anteil an Q {Qv/(C_K*(80-th)):.2f}")
# Rech8: Becherbereich
for mB in (0.25, 0.30, 0.40):
    print(f"Becher {mB} kg:", "  ".join(f"c={c:.0f}: {lauf(C_T=mB*c)[2]:.2f}" for c in (800.0, 850.0, 900.0, 1080.0)))
# Versuch 40 min mit 50 ml und Abkürzung
print("40 min, 50 ml, Becher: B1-B2 %.2f" % lauf(t_end=2400.0, C_T=255.0, m_M=51.5e-3)[2])
print("Abkürzung: theta_K(40 min) = %.2f, (47/60)^4 = %.4f" % (20+60*(47/60)**4, (47/60)**4))
print("40 min mit Becher: B1-B3 (Milch 20) %.2f; Glas 15 °C: %.2f" % (lauf(t_end=2400.0, C_T=255.0)[0]-lauf(t_end=2400.0, C_T=255.0, thM2=20.0)[1],
      lauf(t_end=2400.0, C_T=255.0)[0]-lauf(t_end=2400.0, C_T=255.0, thM2=15.0)[1]))
print("40 min ohne Becher: B1-B3 (Milch 20) %.2f" % (lauf(t_end=2400.0)[0]-lauf(t_end=2400.0, thM2=20.0)[1]))
