# -*- coding: utf-8 -*-
"""Zahlen in den Texten der Kaffee-Seite (BAU_AUFTRAG.md, Teil 2.3).

- {{z:name}}: modellabhängige Ergebniszahl, aus ungerundeten Werten der Python-Referenz (simulation/modell/kaffee_erweitert.py),
  gerundet nach der Regel in STELLEN; Deutsch mit Dezimalkomma, Englisch mit Dezimalpunkt.
- {{e:name}}: Eingabe der Aufgabe (Standardwerte, kaffee_modell.P), Herkunft: Aufgabenblatt.
- {{v:name}}: Vorgabe mit Herkunftsnachweis in VORGABEN (Konzept, Literatur, Bau).
Literale Zahlen in den Texten, die keine Platzhalter sind, brauchen einen Eintrag in LITERALE (Schlüssel, Zahl, Herkunft);
das prüft simulation/tests/test_texte.py.
"""
import math
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HIER), "modell"))
import kaffee_erweitert as ke  # noqa: E402
import kaffee_modell as km  # noqa: E402


def _anzeige_bereich(e, wert_soll, t_bis=240):
    """Ganze Minuten der Zugabe, bei denen die Anzeige (2 Stellen) den gerundeten Höchstwert zeigt."""
    soll = round(wert_soll, 2)
    ts = [t for t in range(1, t_bis + 1) if round(ke.auswerten(dict(e, tEnd_min=float(t)))["dT"], 2) == soll]
    return min(ts), max(ts)


def modellzahlen():
    """Name -> (ungerundeter Wert, Nachkommastellen). Alles aus der Python-Referenz."""
    E = ke.einstellung
    z = {}
    r = ke.auswerten(E())
    z.update(th1=(r["th1"], 2), th2=(r["th2"], 2), dT=(r["dT"], 2), dQ=(r["Q2"] - r["Q1"], 2), CG=(r["C_GB"], 1),
             Q1=(r["Q1"], 2), Q2=(r["Q2"], 2), th10=(r["th10"], 2), kA=(r["kA"], 4))
    g = ke.groesster_unterschied(E())
    z["dTmax"] = (g["dT_max"], 2)
    z["f1_tmax"] = (g["t_min"], 0)
    von, bis = _anzeige_bereich(E(), g["dT_max"])
    z["f1_von"], z["f1_bis"] = (von, 0), (bis, 0)
    # Grenzwert bei sehr später Zugabe: beide Tassen auf Raumtemperatur, Tasse 2 danach mit kalter Milch gemischt
    c = ke.kapazitaeten(E())
    p = km.P
    th2_grenz = (c["C_K"] * p["th_U"] + c["C_M"] * p["th_M"]) / c["C_GB"]
    z["grenz"] = (p["th_U"] - th2_grenz, 2)
    z["grenz_th2"] = (th2_grenz, 2)
    # V1: Milchtemperatur für gleich warme Tassen (Formel aus kaffee_modell.rechne, th_M_gleich) bei 30, 60, 90 min
    for t in (30, 60, 90):
        pp = dict(km.P, t_end=t * 60.0)
        z["v1_%d" % t] = (km.rechne(pp)["th_M_gleich"], 1)
    # V2: Deckel (kA · 0,56)
    eD = E(kA=0.56 * ke.kA_aufgabe())
    gD = ke.groesster_unterschied(eD)
    z["v2_tmax"] = (gD["t_min"], 0)
    von, bis = _anzeige_bereich(eD, gD["dT_max"])
    z["v2_von"], z["v2_bis"] = (von, 0), (bis, 0)
    z["v2_d60"] = (ke.auswerten(eD)["dT"], 2)
    # V3: Becher wie Teil g (kA aus der Messung)
    rB = ke.auswerten(E(kAQuelle="messung", becher=True))
    z.update(v3_dT=(rB["dT"], 2), v3_Q1=(rB["Q1"], 2), v3_Q2=(rB["Q2"], 2))
    # V4: kA von Tasse 1 um 5 % größer; kA beider um ±10 % falsch
    z["v4_d105"] = (ke.auswerten(E(kA1Faktor=1.05))["dT"], 2)
    d0 = r["dT"]
    d10 = max(abs(ke.auswerten(E(kA=f * ke.kA_aufgabe()))["dT"] - d0) for f in (0.9, 1.1))
    z["v4_d10"] = (math.ceil(d10 * 100) / 100, 2)          # „höchstens“: aufgerundet auf 0,01 K
    # V5: Thermobecher offen (Faktor 0,44) und Keramik offen
    eT = E(kA=0.44 * ke.kA_aufgabe())
    z["v5_thermo30"] = (ke.auswerten(eT)["schwarz30"], 1)
    z["v5_keramik30"] = (r["schwarz30"], 1)
    z["v5_thermo_t"] = (ke.groesster_unterschied(eT)["t_min"], 0)
    return z


def eingaben():
    p = km.P
    return {"VK_ml": (p["V_K"] * 1e6, 0), "VM_ml": (p["V_M"] * 1e6, 0), "thK0": (p["th_K0"], 0), "thM": (p["th_M"], 0),
            "thU": (p["th_U"], 0), "rho_K": (p["rho_K"], 0), "rho_M": (p["rho_M"], 0), "cp_K": (p["cp_K"] / 1000, 2),
            "cp_M": (p["cp_M"] / 1000, 2), "c_B": (p["c_B"] / 1000, 2)}


# Vorgaben: Wert, Stellen, Herkunft
VORGABEN = {
    "v4_ungleich": (5, 0, "Konzept 6.2 V4 (Fragestellung)"),
    "v4_falsch": (10, 0, "Konzept 6.2 V4 (Fragestellung)"),
    "biot": (0.035, 3, "R3 Abschnitt 9b, aus Ferreira 2025b (Konzept A.6)"),
    "abtastpunkte": (241, 0, "Bau: Zahl der Abtastpunkte je Kurve in oberflaeche.js"),
    "testwerte": (10000, 0, "Bau: Zahl der Zufallssätze in simulation/tests/test_kern.py"),
}

# Literale Zahlen in Texten: (Schlüssel, Zahl wie im Text, Herkunft). Fragen- und Teilnummern, Jahre, Bibliografie sind ausgenommen.
LITERALE = [
    ("*", "60", "Aufgabe: Zugabe nach 60 min (Standardwert), Versuch bis 60 min (E8)"),
    ("*", "10", "Aufgabe: Messung nach 10 min (Teil c)"),
    ("*", "0", "Zeitpunkt t = 0 bzw. Zeile 0 min"),
    ("*", "1", "Fragen-, Tassen- oder Bechernummer"),
    ("*", "2", "Fragen-, Tassen- oder Bechernummer"),
    ("*", "3", "Bechernummer oder Zahl der Punkte"),
    ("*", "5", "Foliensatz-Nummer 05 oder Vorgabe"),
    ("*", "05", "Foliensatz 05 (Aufgabe Teil b)"),
    ("*", "8", "Folie 8 bzw. Tutorium 8 (Aufgabe, Lösung)"),
    ("*", "30", "Konzept: Vergleich nach 30 min (Anzeige M8, V1)"),
    ("*", "90", "Konzept V1: Zugabe nach 90 min"),
    ("*", "100", "Bereich der Messwerte 0 bis 100 °C (Bau, Kurslink)"),
    ("*", "0,01", "Rundung der Anzeige (Konzept A.2)"),
    ("*", "0.01", "rounding of the display (Konzept A.2)"),
    ("vor_text_keramik", "200", "Aufgabe: 200 ml"),
    ("vor_text_keramik", "80", "Aufgabe: 80 °C"),
    ("vor_text_keramik", "67", "Aufgabe: 67 °C nach 10 min"),
    ("vor_text_keramik_deckel", "44", "Ferreira 2025a, Abb. 6 (Konzept M1, 1 − 0,56)"),
    ("mess_ungueltig", "66,5", "Beispiel einer Eingabe"),
    ("mess_ungueltig", "66.5", "example of an input"),
    ("g_tEnd", "60", "E8: Versuch bis 60 min"),
    ("g_thM", "60", "Aufgabe Teil f: erwärmte Milch 60 °C"),
    ("*", "5", "Tutorium 5"),
    ("rw_misch", "1,0", "Formelindex: Tasse 1 zum Zeitpunkt 0 (Konzept A.3)"),
    ("rw_misch", "1.0", "formula index: cup 1 at time 0 (Konzept A.3)"),
    ("text_code", "360", "Bau: kleinste Breite der Abdeckungsmatrix (BAU_AUFTRAG 3.4)"),
    ("text_code", "1920", "Bau: größte Breite der Abdeckungsmatrix (BAU_AUFTRAG 3.4)"),
    ("link_grund_zu_lang", "400", "Kurslink: höchstens 400 Zeichen (ZUSTAENDE.md 5)"),
    ("link_grund_u", "40", "Kurslink: Raumtemperatur 5 bis 40 °C (ZUSTAENDE.md 5)"),
    ("link_grund_m", "70", "Kurslink: Milchtemperatur 0 bis 70 °C (ZUSTAENDE.md 5)"),
    ("link_grund_b1_8", "60", "Zeile „60 nach der Milch“ (Messblatt)"),
    ("hinweis_zahl", "4", "Beispiel einer Eingabe"),
    ("hinweis_zahl", "3,5", "Beispiel einer Eingabe"),
    ("hinweis_zahl", "3.5", "example of an input"),
    ("*", "2025", "Jahr (Ferreira 2025a)"),
    ("*", "2019", "Jahr (Abraham und Diller 2019)"),
    ("*", "2008", "Jahr (Brown und Diller 2008)"),
]


def formatiere(wert, stellen, sprache):
    if isinstance(wert, float) and stellen == 0:
        wert = int(round(wert))
    s = ("%." + str(stellen) + "f") % wert if stellen > 0 else str(int(wert))
    if stellen == 0 and abs(int(wert)) >= 10000:          # Tausender mit geschütztem Leerzeichen (Leitfaden 4)
        s = "{:,}".format(int(wert)).replace(",", "\u00a0")
    if s.startswith("-"):
        s = "−" + s[1:]
    return s.replace(".", ",") if sprache == "de" else s


def alle(sprache):
    out = {}
    for k, (w, st) in modellzahlen().items():
        out["z:" + k] = formatiere(w, st, sprache)
    for k, (w, st) in eingaben().items():
        out["e:" + k] = formatiere(w, st, sprache)
    for k, (w, st, _) in VORGABEN.items():
        out["v:" + k] = formatiere(w, st, sprache)
    return out


if __name__ == "__main__":
    for k, (w, st) in modellzahlen().items():
        print("%-14s %-22r -> %s / %s" % (k, w, formatiere(w, st, "de"), formatiere(w, st, "en")))
