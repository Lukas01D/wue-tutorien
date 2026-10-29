# -*- coding: utf-8 -*-
"""Nichtlineare Gegenrechnung: 4/3-Gesetz mit Becher (Rech2) und Verdunstungsmodell (Tech2)."""
import math
from kaffee_modell import P, rechne

K = 273.15
r = rechne(P)
C_K, C_M = r["C_K"], r["C_M"]
Tu = 20.0


def psat(th):  # Magnus, Pa
    return 611.2 * math.exp(17.62 * th / (243.12 + th))


def sim(th0, C, t_end, qdot, dt=1.0):
    th = th0
    for _ in range(int(t_end / dt)):
        th -= qdot(th) / C * dt
    return th


def eichen(qform, C_mess):
    """Skalierungsfaktor s so, dass schwarzer Kaffee (C_mess) nach 10 min 67 °C hat."""
    lo, hi = 1e-4, 100.0
    for _ in range(70):
        mid = math.sqrt(lo * hi)
        if sim(80.0, C_mess, 600.0, lambda th: mid * qform(th)) > 67.0:
            lo = mid
        else:
            hi = mid
    return math.sqrt(lo * hi)


def fall(qform, C_T=0.0, thM1=5.0, thM2=5.0, kA1faktor=1.0):
    CKT = C_K + C_T
    CGT = CKT + C_M
    s = eichen(qform, CKT)
    q = lambda th: s * qform(th)
    th10 = (CKT * 80.0 + C_M * thM1) / CGT
    th1 = sim(th10, CGT, 3600.0, lambda th: kA1faktor * q(th))
    th2K = sim(80.0, CKT, 3600.0, q)
    th2 = (CKT * th2K + C_M * thM2) / CGT
    return th1, th2, th1 - th2


# Rech2: n = 4/3 mit Becher; Becher 1, 2, 3 (Milch 20 °C)
n43 = lambda th: max(th - Tu, 0) ** (4 / 3)
b1, b2, d = fall(n43, C_T=255.0)
_, b3, _ = fall(n43, C_T=255.0, thM2=20.0)
print(f"Rech2 n=4/3 mit Becher: B1 {b1:.2f}, B2 {b2:.2f}, B3 {b3:.2f}, B1-B2 {d:.2f}, B1-B3 {b1-b3:.2f}")

# Tech2: Verdunstung nach Dampfdruck, Anteil f_v bei 80 °C; Rest linear oder 4/3
phi = 0.5
for rest_name, rest in (("linear", lambda th: th - Tu), ("4/3", n43)):
    for f_v in (0.0, 0.3, 0.5, 0.6):
        # Verdunstung: c (psat(th) - phi psat(Tu)); Gewicht so, dass Anteil bei 80 °C = f_v
        ev = lambda th: max(psat(th) - phi * psat(Tu), 0.0)
        if f_v > 0:
            w = f_v / (1 - f_v) * rest(80.0) / ev(80.0)
        else:
            w = 0.0
        qform = lambda th, w=w, rest=rest, ev=ev: rest(th) + w * ev(th)
        th1, th2, d = fall(qform)
        _, _, dB = fall(qform, C_T=255.0)
        th1k, th2k, dk = fall(qform, kA1faktor=1.05)
        print(f"Tech2 Rest {rest_name:6s} f_v {f_v:.1f}: th1 {th1:.2f}, th2 {th2:.2f}, diff {d:.2f} K; "
              f"mit Becher {dB:.2f} K; Tasse 1 kA*1,05: diff {dk:.2f} K")
