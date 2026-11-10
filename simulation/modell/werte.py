# -*- coding: utf-8 -*-
"""Alle Zahlen der überarbeiteten Kaffee-Aufgabe (Tutorium 5, Variante B mit Deckel).

Quelle der Rechnung ist kaffee_modell.py (unverändert). Geändert sind nur zwei Eingaben
gegenüber den dort hinterlegten Standardwerten:
    th_mess = 72 °C  (Messung in Tasse 2 nach 10 min, jetzt mit Deckel; Prüfbericht R, B.2)
    th_Mh   = 70 °C  (erwärmte Milch in Teil g; Prüfbericht R, B.3)
Neu: Trinktemperatur 50 °C (Teile h1 bis h3); 100 ml Milch und 45 min Wartezeit (Entscheidung TL 10.11.2026).

Aufruf: python3 werte.py            (Tabelle aller Werte und Prüfung der Textaussagen)
Import: from werte import werte     (Wörterbuch mit Zahlen und fertig formatierten Texten)
Ändert die Tutoriumsleitung einen Wert, genügt es, ihn unten zu ändern und neu zu bauen
(bash bauen.sh). Werte mit (v) sind VORLÄUFIG: Abschätzungen, die mit dem Messplan
(Januar 2027) empirisch bestimmt werden. Die Liste VORLAEUFIG unten nennt Stelle und Messung.
"""
import math
from kaffee_modell import P, rechne, zwei_tassen, gleichstand

# Eingaben des Blatts. (v) = vorläufig, mit dem Messplan zu bestimmen; (g) = gewählt; (L) = Literatur
KAFFEE_START = 80.0   # (v) °C, Kaffee in der vorgewärmten Tasse direkt nach dem Eingießen (Messplan M2)
MILCH_KALT = 5.0      # (v) °C, Milch aus dem Kühlschrank (M1)
RAUM = 20.0           # (g) °C, Raumtemperatur auf dem Blatt (am Messtag messen und umrechnen, M3)
V_KAFFEE = 200e-6     # (v) m³, Kaffee je Tasse (M1)
V_MILCH = 100e-6      # (g) m³, Milch je Tasse (Entscheidung TL 10.11.2026; M1 prüft die Menge)
MESSWERT = 72.0       # (v) °C nach 10 min, Tasse 2 ohne Milch, mit Deckel (M3; Umrechnung: messwert_fuer_blatt)
MILCH_HEISS = 70.0    # (g) °C, Teil g (Temperatur beim Zugießen prüfen, M6)
TRINK = 50.0          # (g) °C, Teile h1 bis h3 (Tasse 1 startet mit 100 ml Milch bei etwa 55 °C)
DAUER_MIN = 45.0      # (g) min, Wartezeit bis zur Milch in Tasse 2 (Entscheidung TL 10.11.2026)
ZEITEN_MIN = [0, 10, 20, 30, 40, 45]   # Messzeitpunkte im Experiment (alle 10 min und am Ende)
M_TASSE = 0.300       # (v) kg, Keramiktasse (M1)
C_KERAMIK = 850.0     # (L) J/(kg K), Keramik (M4 prüft die Wirkung der Tasse beim Zugießen)
C_BECHER = M_TASSE * C_KERAMIK   # J/K, vorgewärmte Tasse (nur Versuchserwartung und h, Hinweise)
D_TASSE = 0.08        # (v) m, Innendurchmesser für Füllhöhe und Fläche (nur Einordnung in der Lösung, M1)
TH_OFFEN = 64.0       # (v) °C nach 10 min ohne Deckel (nur für den Deckelvergleich in h, M7);
                      # unabhängige Prüfung H: plausibel 57 bis 67 °C, 64 °C trifft die Abschätzung von Q_V

# Vorläufige und gewählte Werte: (Größe, Wert, Stelle, Status, Messung im Messplan)
VORLAEUFIG = [
    ("Kaffee in der vorgewärmten Tasse", "80 °C", "Werte; alle Teile", "vorläufig", "M2"),
    ("Tasse 2 nach 10 min mit Deckel", "72 °C", "Werte; d und alles danach", "vorläufig", "M3"),
    ("Milch aus dem Kühlschrank", "5 °C", "Werte; a2, e3, g", "vorläufig", "M1"),
    ("Kaffee und Milch je Tasse", "200 ml und 100 ml", "Werte; alle Teile", "vorläufig", "M1"),
    ("Raumtemperatur", "20 °C", "Werte", "gewählt", "M3 (umrechnen)"),
    ("Erwärmte Milch", "70 °C", "Werte; g", "gewählt", "M6"),
    ("Trinktemperatur", "50 °C", "Werte; h1, h3", "gewählt", "keine"),
    ("Tasse: Masse, Innendurchmesser", "300 g, 8 cm", "Lösung d; Hinweise; j", "vorläufig", "M1, M4"),
    ("Offene Tasse nach 10 min", "64 °C", "Lösung j (Deckelvergleich)", "vorläufig", "M7"),
    ("Verdunstete Masse in 60 min (offen)", "7 bis 12 g", "Lösung j; Hinweise", "vorläufig", "M7"),
    ("kA der volleren Tasse 1", "bis etwa 25 % größer", "Lösung d, Experiment 4", "Schätzung", "M5"),
    ("Streuung zweier gleicher Tassen", "unbekannt", "Hinweise, Experiment", "offen", "M5"),
    ("Ablesegenauigkeit des Thermometers", "etwa ±0,5 K", "Hinweise, Experiment", "Schätzung", "M0"),
    ("Beispielwerte für das Experiment", "Modell mit Tasse", "Blatt, Kontrollseite", "berechnet", "M5 (durch Messwerte ersetzen)"),
]


def messwert_fuer_blatt(kA, th_K0=KAFFEE_START, th_U=RAUM, V_K=V_KAFFEE, t=600.0):
    """Rechnet ein gemessenes kA (W/K, aus dem Probelauf mit den dortigen Start- und Raumtemperaturen)
    in den Messwert nach 10 min um, der auf dem Blatt zu den Blattwerten passt."""
    C_K = P["rho_K"] * V_K * P["cp_K"]
    return th_U + (th_K0 - th_U) * math.exp(-kA * t / C_K)


def de(x, n=2):
    """Zahl mit Dezimalkomma."""
    s = f"{x:.{n}f}"
    return s.replace("-", "−").replace(".", ",") if x < 0 else s.replace(".", ",")


def de_tex(x, n=2):
    """Zahl für LaTeX-Formeln (Minus als normales Minus)."""
    return f"{x:.{n}f}".replace(".", ",")


def werte(messwert=MESSWERT, milch_heiss=MILCH_HEISS, trink=TRINK):
    p = dict(P, th_mess=messwert, th_Mh=milch_heiss, th_K0=KAFFEE_START, th_M=MILCH_KALT,
             th_U=RAUM, V_K=V_KAFFEE, V_M=V_MILCH, t_end=DAUER_MIN * 60.0)
    r = rechne(p)
    K = 273.15
    w = {}
    # Grunddaten
    w["mK"] = r["m_K"]; w["mM"] = r["m_M"]
    w["CK"] = r["C_K"]; w["CM"] = r["C_M"]; w["CG"] = r["C_G"]
    # a) Mischen
    w["T10"] = r["T1_0"]; w["th10"] = r["T1_0"] - K
    w["sprung_a"] = p["th_K0"] - w["th10"]
    # d) kA
    w["kA"] = r["kA"]; w["ln_mess"] = r["ln_mess"]
    w["tauK_min"] = r["tau_K"] / 60; w["tauG_min"] = r["tau_G"] / 60
    hK = p["V_K"] / (math.pi * D_TASSE ** 2 / 4); hG = (p["V_K"] + p["V_M"]) / (math.pi * D_TASSE ** 2 / 4)
    w["h_K_cm"] = hK * 100; w["h_G_cm"] = hG * 100
    A = math.pi * D_TASSE * hK + 2 * math.pi * D_TASSE ** 2 / 4      # Wand bis Füllhöhe, Boden, Oberseite
    w["A_cm2"] = A * 1e4; w["kA_je_A"] = r["kA"] / A
    w["kA_kipp_proz"] = (gleichstand(lambda f: zwei_tassen(p, kA1_faktor=f)["dT"], lo=1.0, hi=3.0) - 1) * 100
    # d2) Zeit bis Trinktemperatur (Tasse 1)
    w["t_tr_s"] = -r["tau_G"] * math.log((trink - p["th_U"]) / (w["th10"] - p["th_U"]))
    w["t_tr_min"] = w["t_tr_s"] / 60
    w["t_tr_schwarz_min"] = -r["tau_K"] * math.log((trink - p["th_U"]) / (p["th_K0"] - p["th_U"])) / 60
    w["d_tr"] = trink - p["th_U"]; w["d_10"] = w["th10"] - p["th_U"]
    # h2, h3) Tassenwärmer
    w["QW"] = r["kA"] * (trink - p["th_U"])
    w["th_w60"] = trink + (w["th10"] - trink) * r["e_G"]      # Tasse 1 auf dem Wärmer nach 60 min
    # e) nach 60 min
    w["eG"] = r["e_G"]; w["eK"] = r["e_K"]
    w["T1"] = r["T1"]; w["th1"] = r["T1"] - K
    w["T2K"] = r["T2_K"]; w["th2K"] = r["T2_K"] - K
    w["T2"] = r["T2"]; w["th2"] = r["T2"] - K
    w["dT"] = r["dT"]; w["sprung_e"] = w["th2K"] - w["th2"]
    # f) Wärmen
    w["Q1"] = r["Q1"]; w["Q2"] = r["Q2"]; w["dQ"] = r["Q2"] - r["Q1"]
    w["Qd1"] = r["Qdot1_0"]; w["Qd2"] = r["Qdot2_0"]
    w["t_schnitt_min"] = r["t_schnitt"] / 60
    # g) heiße Milch
    h = zwei_tassen(p, th_M1=milch_heiss)
    w["T10h"] = h["T1_0"]; w["th10h"] = h["T1_0"] - K
    w["T1h"] = h["T1"]; w["th1h"] = h["th1"]; w["T2h"] = h["T2"]; w["th2h"] = h["th2"]
    w["dTh"] = h["dT"]
    w["kipp"] = r["th_M_gleich"]
    w["eff_kaffee"] = r["C_K"] * (r["T_K0"] - r["T_U"]) * (r["e_G"] - r["e_K"]) / r["C_G"]
    w["eff_milch_kalt"] = r["C_M"] * (p["th_M"] - p["th_U"]) * (r["e_G"] - 1) / r["C_G"]
    w["eff_milch_heiss"] = r["C_M"] * (milch_heiss - p["th_U"]) * (r["e_G"] - 1) / r["C_G"]
    w["kipp_linear"] = p["th_M"] + (milch_heiss - p["th_M"]) * w["dT"] / (w["dT"] - w["dTh"])
    # h) Deckelvergleich im linearen Modell (offen: kA aus TH_OFFEN nach 10 min, vorläufig)
    # Teil j hat eine eigene Dauer von 60 min (eigenes Experiment, unabhängig von der Wartezeit)
    p60 = dict(p, t_end=3600.0); r60 = rechne(p60)
    po = dict(p60, th_mess=TH_OFFEN); ro = rechne(po)
    th_offen60 = ro["T2_K"] - K
    w["h_th2K60"] = r60["T2_K"] - K
    Q_offen = ro["C_K"] * (ro["T_K0"] - ro["T2_K"])
    QV_wahr = (ro["kA"] - r60["kA"]) / ro["kA"] * Q_offen
    QV_naiv = r60["C_K"] * (w["h_th2K60"] - th_offen60)
    w["h_kA_offen"] = ro["kA"]; w["h_th_offen60"] = th_offen60; w["h_Q_offen"] = Q_offen
    w["h_QV_wahr"] = QV_wahr; w["h_QV_naiv"] = QV_naiv; w["h_zuwenig_proz"] = (1 - QV_naiv / QV_wahr) * 100
    w["h_dm_g"] = QV_wahr / p["dh_v"] * 1000
    # Versuch: Erwartung mit Blattmodell und mit vorgewärmtem Becher
    def reihe(C_T):
        CKT, CGT = r["C_K"] + C_T, r["C_G"] + C_T
        kA_b = -CKT / p["t_mess"] * r["ln_mess"]
        T10b = (CKT * r["T_K0"] + r["C_M"] * r["T_M"]) / CGT
        b1 = [r["T_U"] + (T10b - r["T_U"]) * math.exp(-kA_b * 60 * t / CGT) - K for t in ZEITEN_MIN]
        b2 = [r["T_U"] + (r["T_K0"] - r["T_U"]) * math.exp(-kA_b * 60 * t / CKT) - K for t in ZEITEN_MIN]
        b2m = (CKT * (b2[-1] + K) + r["C_M"] * r["T_M"]) / CGT - K
        return kA_b, b1, b2, b2m
    w["V_blatt"] = reihe(0.0); w["V_becher"] = reihe(C_BECHER)
    w["p"] = p; w["r"] = r
    return w


def pruefen(w):
    """Aussagen des Textes, die von den Zahlen abhängen. Schlägt eine fehl, muss der Text angepasst werden."""
    p = w["p"]
    fehler = []
    if not w["t_schnitt_min"] > DAUER_MIN:
        fehler.append("Schnittpunkt liegt innerhalb der Wartezeit: Text in f3 und Abb. L2 anpassen")
    if not w["dT"] > 0:
        fehler.append("Tasse 1 ist nicht wärmer: Kernaussage")
    if not w["dTh"] < 0:
        fehler.append("mit erwärmter Milch ist Tasse 2 nicht wärmer: Teil g")
    if not (p["th_M"] < w["kipp"] < MILCH_HEISS):
        fehler.append("Kipppunkt liegt nicht zwischen kalter und erwärmter Milch")
    if not w["th10"] > TRINK:
        fehler.append("Tasse 1 startet unter der Trinktemperatur: Teil h1")
    if not (TRINK < w["th_w60"] < w["th10"]):
        fehler.append("Tassenwärmer: Temperatur am Ende liegt nicht zwischen Endwert und Start")
    if abs(w["kipp"] - w["kipp_linear"]) > 1e-6:
        fehler.append("lineare und geschlossene Kipppunktformel weichen ab")
    if abs(w["dQ"] / w["CG"] - w["dT"]) > 1e-9:
        fehler.append("Energiebilanz f2 geht nicht auf")
    if abs(w["eff_kaffee"] + w["eff_milch_kalt"] - w["dT"]) > 1e-9:
        fehler.append("Zerlegung kalt geht nicht auf")
    if abs(w["eff_kaffee"] + w["eff_milch_heiss"] - w["dTh"]) > 1e-9:
        fehler.append("Zerlegung heiß geht nicht auf")
    if not w["sprung_e"] < w["sprung_a"]:
        fehler.append("Sprung beim späten Zugießen ist nicht kleiner: Lösung e3, Hinweise")
    if not w["kipp"] > 30.0:
        fehler.append("Kipppunkt unter 30 °C: Beispiel in der Lösung g1 anpassen")
    kA_b, v1, v2, v2m = w["V_becher"]
    if not v1[-1] - v2m > 0:
        fehler.append("Versuchserwartung mit Tasse: Tasse 1 ist nicht wärmer (Lösung Versuch, Hinweise)")
    if not v1[0] > w["th10"]:
        fehler.append("Versuchserwartung: Mischtemperatur mit Tasse liegt nicht über der Rechnung")
    return fehler


if __name__ == "__main__":
    w = werte()
    zeilen = [
        ("m_K in kg", w["mK"], 4), ("m_M in kg", w["mM"], 4),
        ("C_K in J/K", w["CK"], 3), ("C_M in J/K", w["CM"], 3), ("C_G in J/K", w["CG"], 3),
        ("a) T_1,0 in K", w["T10"], 3), ("a) th_1,0 in °C", w["th10"], 3), ("a) Sprung in K", w["sprung_a"], 3),
        ("d) ln-Verhältnis", w["ln_mess"], 6), ("d) kA in W/K", w["kA"], 6),
        ("d) tau ohne Milch in min", w["tauK_min"], 3), ("d) tau mit Milch in min", w["tauG_min"], 3),
        ("d) Füllhöhe ohne/mit Milch in cm", w["h_K_cm"], 3), ("", w["h_G_cm"], 3),
        ("d) Fläche in cm²", w["A_cm2"], 2), ("d) kA/A in W/(m²K)", w["kA_je_A"], 3),
        ("d) kA-Zuschlag Tasse 1, der umdreht, in %", w["kA_kipp_proz"], 3),
        ("d2) t bis 60 °C Tasse 1 in s", w["t_tr_s"], 2), ("d2) in min", w["t_tr_min"], 3),
        ("d2) schwarzer Kaffee bis 60 °C in min", w["t_tr_schwarz_min"], 3),
        ("d4) Q_W in W", w["QW"], 4), ("d4) Tasse 1 auf dem Wärmer nach 60 min", w["th_w60"], 3),
        ("e) e_G", w["eG"], 6), ("e) e_K", w["eK"], 6),
        ("e1) T_1 in K", w["T1"], 3), ("e1) th_1 in °C", w["th1"], 3),
        ("e2) T_K(60) in K", w["T2K"], 3), ("e2) th_K(60) in °C", w["th2K"], 3),
        ("e3) T_2 in K", w["T2"], 3), ("e3) th_2 in °C", w["th2"], 3),
        ("e) Unterschied in K", w["dT"], 4), ("e3) Sprung in K", w["sprung_e"], 3),
        ("f1) Q_1 in J", w["Q1"], 2), ("f1) Q_2 in J", w["Q2"], 2), ("f2) Q_2 - Q_1 in J", w["dQ"], 2),
        ("f3) Wärmestrom Beginn Tasse 1 in W", w["Qd1"], 3), ("f3) Tasse 2 in W", w["Qd2"], 3),
        ("f3) Schnittpunkt in min", w["t_schnitt_min"], 2),
        ("g2) T_1,0 heiß in K", w["T10h"], 3), ("g2) th_1,0 heiß in °C", w["th10h"], 3),
        ("g2) T_1 in K", w["T1h"], 3), ("g2) th_1", w["th1h"], 3), ("g2) T_2 in K", w["T2h"], 3), ("g2) th_2", w["th2h"], 3),
        ("g2) Unterschied in K", w["dTh"], 4), ("g3) Kipppunkt in °C", w["kipp"], 3),
        ("g4) Kaffee-Effekt in K", w["eff_kaffee"], 3), ("g4) Milch-Effekt kalt", w["eff_milch_kalt"], 3),
        ("g4) Milch-Effekt heiß", w["eff_milch_heiss"], 3),
        ("h) kA offen in W/K", w["h_kA_offen"], 4), ("h) th offen nach 60 min", w["h_th_offen60"], 3),
        ("h) Q offen in J", w["h_Q_offen"], 1), ("h) Q_V wahr in J", w["h_QV_wahr"], 1),
        ("h) Q_V Endtemperaturvergleich in J", w["h_QV_naiv"], 1), ("h) zu wenig in %", w["h_zuwenig_proz"], 2),
        ("h) Masse in g", w["h_dm_g"], 2),
    ]
    for name, x, n in zeilen:
        print(f"{name:45s} {x:.{n}f}")
    for titel, (kA_b, b1, b2, b2m) in (("Versuch Blattmodell", w["V_blatt"]), ("Versuch mit Becher", w["V_becher"])):
        print(titel, "kA", round(kA_b, 4))
        print("  Becher 1:", " ".join(f"{x:.2f}" for x in b1))
        print("  Becher 2:", " ".join(f"{x:.2f}" for x in b2), "nach Milch", f"{b2m:.2f}", "Unterschied", f"{b1[-1]-b2m:.2f}")
    f = pruefen(w)
    print("Prüfung der Textaussagen:", "alle erfüllt" if not f else f)
