# -*- coding: utf-8 -*-
"""Python-Referenz der Kaffee-Simulation (Bau nach simulation/BAU_AUFTRAG.md, Teil 2.1).

Importiert kaffee_modell.py unverändert (Kopie aus dem Arbeitsordner der Kaffee-Aufgabe, Herkunft in HERKUNFT.md)
und rechnet die Erweiterungen aus KONZEPT.md Fassung 2, Abschnitt 8.2, als eigene Funktionen:

- M8  kA festhalten: gleichwertiger Messwert nach 10 min, damit das Grundmodell genau dieses kA rechnet
- M3  Energie: Q1, Q2, Milchbeitrag, Teilflächen der Wärmeströme vor und nach dem Schnitt
- M2  Ausgleichsgerade durch den Ursprung und mit freiem Achsenabschnitt
- M4  Kurven nach der Zugabe (kann)
- M9  Becher beim Eingießen kalt (kann)
- M10 Trinkzeit bis zu einer Trinktemperatur (kann)
- größter Unterschied über dem Zeitpunkt der Zugabe (Konzept 8.1)

Einstellungen e (Einheiten wie in der Oberfläche): VK_ml, VM_ml, thK0, thM, thU (°C), tEnd_min (Zugabe, min), becher (bool),
mB_g (g), milch2Raum (bool), kA1Faktor (1 = gleich), kAQuelle ("fest" oder "messung"), kA (W/K, bei "fest"), thMess (°C, bei "messung").
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kaffee_modell as km  # noqa: E402

K = 273.15
STANDARD = dict(tEnd_min=60.0, thM=5.0, milch2Raum=False, VM_ml=30.0, thU=20.0, becher=False, thK0=80.0, thMess=67.0,
                VK_ml=200.0, kA1Faktor=1.0, mB_g=300.0, kAQuelle="fest", kA=None)

# Voreinstellungen für kA (Konzept Tabelle 8.2.1): Faktor zu "Keramik offen" (Arbeitswert der Aufgabe)
VOREINSTELLUNGEN = [
    ("keramik", 1.00, "belegt"),
    ("keramik_deckel", 0.56, "belegt"),
    ("glas", 1.00, "richtwert"),
    ("pappe", 1.00, "richtwert"),
    ("edelstahl", 0.90, "richtwert"),
    ("thermo_offen", 0.44, "richtwert"),
]


def einstellung(**abw):
    e = dict(STANDARD)
    e.update(abw)
    if e["kAQuelle"] == "fest" and "kA" not in abw:
        e["kA"] = kA_aufgabe()
    return e


def kapazitaeten(e):
    p = km.P
    C_K = p["rho_K"] * e["VK_ml"] * 1e-6 * p["cp_K"]
    C_M = p["rho_M"] * e["VM_ml"] * 1e-6 * p["cp_M"]
    C_B = e["mB_g"] / 1000.0 * p["c_B"] if e["becher"] else 0.0
    return dict(C_K=C_K, C_M=C_M, C_B=C_B, C_KB=C_K + C_B, C_GB=C_K + C_M + C_B)


def kA_aufgabe():
    """kA der Aufgabe (Teil c): 80 auf 67 °C in 10 min, 200 ml, ohne Becher."""
    return km.rechne(km.P)["kA"]


def messwert_fuer(kA, e):
    """Gleichwertiger Messwert nach 10 min (M8): das Grundmodell rechnet daraus genau dieses kA."""
    c = kapazitaeten(e)
    return e["thU"] + (e["thK0"] - e["thU"]) * math.exp(-kA * 600.0 / c["C_KB"])


def fehler(e):
    """Gültigkeit wie im geprüften Werkzeug (D116), für kA festhalten zusätzlich kA > 0. Leer heißt gültig."""
    zahl = lambda v: isinstance(v, (int, float)) and not isinstance(v, bool) and v == v   # None und NaN gelten als keine Zahl
    if not (zahl(e["thK0"]) and zahl(e["thU"]) and e["thK0"] > e["thU"]):
        return "anfang_ueber_raum"
    if e["kAQuelle"] == "fest":
        if not (zahl(e["kA"]) and e["kA"] > 0):
            return "kA_positiv"
        return ""
    if not (zahl(e["thMess"]) and e["thU"] < e["thMess"] < e["thK0"]):
        return "messung_zwischen"
    return ""


def _p(e):
    p = dict(km.P)
    th_mess = messwert_fuer(e["kA"], e) if e["kAQuelle"] == "fest" else e["thMess"]
    p.update(V_K=e["VK_ml"] * 1e-6, V_M=e["VM_ml"] * 1e-6, th_K0=e["thK0"], th_M=e["thM"], th_U=e["thU"],
             th_mess=th_mess, m_B=e["mB_g"] / 1000.0, t_end=e["tEnd_min"] * 60.0)
    return p


def auswerten(e):
    """Alle Größen der Oberfläche aus dem Grundmodell (zwei_tassen) und den Erweiterungen."""
    p = _p(e)
    c = kapazitaeten(e)
    th_M2 = p["th_U"] if e["milch2Raum"] else p["th_M"]
    z = km.zwei_tassen(p, C_T=c["C_B"], th_M1=p["th_M"], th_M2=th_M2, kA1_faktor=e["kA1Faktor"], t_end=p["t_end"])
    z3 = km.zwei_tassen(p, C_T=c["C_B"], th_M1=p["th_M"], th_M2=p["th_U"], kA1_faktor=e["kA1Faktor"], t_end=p["t_end"])
    T_U, T_K0 = p["th_U"] + K, p["th_K0"] + K
    kA = z["kA"]
    a1 = e["kA1Faktor"] * kA / c["C_GB"]
    a2 = kA / c["C_KB"]
    Q1 = c["C_GB"] * (z["T1_0"] - z["T1"])
    Q2 = c["C_KB"] * (T_K0 - z["T2_K"])
    milch = c["C_M"] * (p["th_M"] - th_M2)

    def T1(t):
        return T_U + (z["T1_0"] - T_U) * math.exp(-a1 * t)

    def T2K(t):
        return T_U + (T_K0 - T_U) * math.exp(-a2 * t)

    def dQ(t):  # Q2(t) - Q1(t), abgegebene Wärme bis t
        return c["C_KB"] * (T_K0 - T2K(t)) - c["C_GB"] * (z["T1_0"] - T1(t))

    # Zeitpunkt gleicher Wärmeströme: kA (T2K - TU) = f1 kA (T1 - TU)
    t_q = math.inf
    zaehler = (T_K0 - T_U) / (e["kA1Faktor"] * (z["T1_0"] - T_U))
    if a2 != a1 and zaehler > 0:
        tq = math.log(zaehler) / (a2 - a1)
        if tq > 0:
            t_q = tq
    tz = p["t_end"]
    if t_q < tz:
        flaeche_vor, flaeche_nach = dQ(t_q), dQ(tz) - dQ(t_q)
    else:
        flaeche_vor, flaeche_nach = dQ(tz), 0.0
    # Schnitt der Temperaturkurven (wie berechne im Werkzeug, beide Richtungen)
    q = (T_K0 - T_U) / (z["T1_0"] - T_U)
    t_s = math.inf
    if a2 != a1 and q > 0:
        ts = math.log(q) / (a2 - a1)
        if ts > 0:
            t_s = ts
    return dict(kA=kA, thMess_modell=p["th_mess"], th10=z["T1_0"] - K, th1=z["th1"], th2=z["th2"], th2K=z["T2_K"] - K,
                th2_raum=z3["th2"], dT=z["dT"], Q1=Q1 / 1e3, Q2=Q2 / 1e3, milch=milch / 1e3,
                energie_rest=(c["C_GB"] * z["dT"] - (Q2 - Q1) - milch) / 1e3,
                t_schnitt=t_s / 60.0, t_waermestrom=t_q / 60.0, flaeche_vor=flaeche_vor / 1e3, flaeche_nach=flaeche_nach / 1e3,
                qdot1_0=e["kA1Faktor"] * kA * (z["T1_0"] - T_U), qdot2_0=kA * (T_K0 - T_U),
                qdot1_Z=e["kA1Faktor"] * kA * (z["T1"] - T_U), qdot2_Z=kA * (z["T2_K"] - T_U),
                schwarz30=T2K(1800.0) - K, tau_min=c["C_KB"] / kA / 60.0,
                kurve1=lambda t_min: T1(t_min * 60.0) - K, kurve2=lambda t_min: T2K(t_min * 60.0) - K, **c)


def nach_zugabe(e, tV_min):
    """M4 (kann): beide Tassen nach der Zugabe bis tV, je mit eigenem kA (f1 für Tasse 1)."""
    r = auswerten(e)
    c = kapazitaeten(e)
    dt = (tV_min - e["tEnd_min"]) * 60.0
    th1 = e["thU"] + (r["th1"] - e["thU"]) * math.exp(-e["kA1Faktor"] * r["kA"] * dt / c["C_GB"])
    th2 = e["thU"] + (r["th2"] - e["thU"]) * math.exp(-r["kA"] * dt / c["C_GB"])
    return dict(th1=th1, th2=th2, dT=th1 - th2)


def becher_kalt(e):
    """M9 (kann): Becher (C_B) beim Eingießen auf Raumtemperatur, sofortiger Ausgleich bei t = 0; nur mit kA festhalten."""
    assert e["kAQuelle"] == "fest" and e["becher"]
    c = kapazitaeten(e)
    kA = e["kA"]
    th1_0 = (c["C_K"] * e["thK0"] + c["C_M"] * e["thM"] + c["C_B"] * e["thU"]) / c["C_GB"]
    thK_0 = (c["C_K"] * e["thK0"] + c["C_B"] * e["thU"]) / c["C_KB"]
    t = e["tEnd_min"] * 60.0
    th1 = e["thU"] + (th1_0 - e["thU"]) * math.exp(-e["kA1Faktor"] * kA * t / c["C_GB"])
    thK = e["thU"] + (thK_0 - e["thU"]) * math.exp(-kA * t / c["C_KB"])
    thM2 = e["thU"] if e["milch2Raum"] else e["thM"]
    th2 = (c["C_KB"] * thK + c["C_M"] * thM2) / c["C_GB"]
    return dict(th1_0=th1_0, thK_0=thK_0, th1=th1, th2=th2, dT=th1 - th2)


def trinkzeit(e, thT=60.0):
    """M10 (kann): Zeit in min, bis Tasse 1 und der schwarze Kaffee thT erreichen (unendlich, wenn nie)."""
    r = auswerten(e)

    def zeit(th0, C, f):
        if th0 <= thT:
            return 0.0
        if thT <= e["thU"]:
            return math.inf
        return C / (f * r["kA"]) * math.log((th0 - e["thU"]) / (thT - e["thU"])) / 60.0
    return dict(tasse1=zeit(r["th10"], r["C_GB"], e["kA1Faktor"]), schwarz=zeit(e["thK0"], r["C_KB"], 1.0))


def ausgleich(punkte, th0, thU, C_KB):
    """M2: punkte = [(t_min, theta)], ohne den Startpunkt. Ursprungsgerade und Gerade mit freiem Achsenabschnitt."""
    xs = [t * 60.0 for t, _ in punkte]
    ys = [math.log((th - thU) / (th0 - thU)) for _, th in punkte]
    b0 = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
    X = [0.0] + xs
    Y = [0.0] + ys
    n = len(X)
    mx, my = sum(X) / n, sum(Y) / n
    sxx = sum((x - mx) ** 2 for x in X)
    b1 = sum((x - mx) * (y - my) for x, y in zip(X, Y)) / sxx
    a1 = my - b1 * mx
    return dict(kA_ursprung=-C_KB * b0, kA_frei=-C_KB * b1, achsenabschnitt=a1, n=len(punkte))


def groesster_unterschied(e, t_max_min=600.0):
    """Konzept 8.1: Maximum des Unterschieds direkt nach der Zugabe über t_Z (gleiches kA). Analytisch über den Schnitt."""
    c = kapazitaeten(e)
    r = auswerten(dict(e, tEnd_min=1.0))
    T_U, T_K0, T10 = e["thU"], e["thK0"], r["th10"]
    q = (T_K0 - T_U) / (T10 - T_U)
    thx = T_U + (T_K0 - T_U) * q ** (-c["C_GB"] / c["C_M"])
    d_max = c["C_M"] * (thx - e["thM"]) / c["C_GB"]
    a2, a1 = r["kA"] / c["C_KB"], r["kA"] / c["C_GB"]
    t_stern = math.log(q) / (a2 - a1) / 60.0
    return dict(dT_max=d_max, th_x=thx, t_min=t_stern)


def groesster_unterschied_numerisch(e, t_max_min=600.0, schritte=60000):
    """Kontrolle ohne Formel: Raster über t_Z in Sekundenbruchteilen."""
    best = (-math.inf, 0.0)
    for i in range(1, schritte + 1):
        t = t_max_min * i / schritte
        d = auswerten(dict(e, tEnd_min=t))["dT"]
        if d > best[0]:
            best = (d, t)
    return dict(dT_max=best[0], t_min=best[1])
