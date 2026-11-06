# -*- coding: utf-8 -*-
"""Erwartete Anzeigewerte für die Browsertests (aus der Python-Referenz, unabhängig vom JavaScript der Seite).

Aufruf: python3 simulation/tests/erwartung_browser.py  -> JSON auf stdout
Rundung wie in der Anzeige (Rechenwerte): Temperaturen 2 Stellen, Unterschied 2, Wärmen 2, kA 4, Schnittzeit 1;
Deutsch mit Komma, Englisch mit Punkt (zahlen.formatiere).
"""
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HIER), "site"))
sys.path.insert(0, os.path.join(os.path.dirname(HIER), "modell"))
import kaffee_erweitert as ke  # noqa: E402
import zahlen  # noqa: E402

# Testdaten für Messblatt und Kurslink (gekennzeichnet als Testdaten, keine Messung der TL)
KURS = {"u": 21.5, "m": 6.0,
        "b1": [80.2, 68.1, 59.0, 52.3, 47.1, 43.0, 39.8, None],
        "b2": [80.0, 67.6, 58.8, 52.0, 46.9, 42.8, 39.6, 35.2],
        "b3": [79.6, 67.2, 58.5, 51.8, 46.6, 42.6, 39.4, 37.9]}


def anzeige(r, sprache):
    f = lambda w, n: zahlen.formatiere(w, n, sprache)
    return {"th1": f(r["th1"], 2), "th2": f(r["th2"], 2), "dT": f(r["dT"], 2), "Q1": f(r["Q1"], 2), "Q2": f(r["Q2"], 2),
            "kA": f(r["kA"], 4), "th10": f(r["th10"], 2), "tSchnitt": f(r["t_schnitt"], 1), "schwarz30": f(r["schwarz30"], 2),
            "th2Raum": f(r["th2_raum"], 2)}


def fall(e):
    r = ke.auswerten(e)
    return {"de": anzeige(r, "de"), "en": anzeige(r, "en")}


def main():
    E = ke.einstellung
    out = {"KURS": KURS}
    out["standard"] = fall(E())
    out["t56"] = fall(E(tEnd_min=56.0))
    # Übernahme aus dem Messblatt: Mittel von Becher 2 (und 3) bei 0 und 10 min, kA aus der Messung, Becher an, 60 min
    for name, becher in (("kurs2", ["b2"]), ("kurs23", ["b2", "b3"])):
        th0 = sum(KURS[b][0] for b in becher) / len(becher)
        th10 = sum(KURS[b][1] for b in becher) / len(becher)
        out[name] = fall(E(thK0=th0, thMess=th10, thU=KURS["u"], thM=KURS["m"], kAQuelle="messung", becher=True, tEnd_min=60.0))
    # Voreinstellung Keramik mit Deckel (kA festhalten, Faktor 0,56)
    out["deckel"] = fall(E(kA=0.56 * ke.kA_aufgabe()))
    # Milch für Tasse 2 bei Raumtemperatur (Pflichttest M3)
    out["milch2raum"] = fall(E(milch2Raum=True))
    # Teilflächen der Ansicht „Wärmestrom“ (Standardwerte), 2 Stellen mit Vorzeichen
    r = ke.auswerten(E())
    out["flaechen"] = {s: [zahlen.formatiere(r["flaeche_vor"], 2, s), zahlen.formatiere(r["flaeche_nach"], 2, s)] for s in ("de", "en")}
    # Ausgleichsgerade (Ansicht ln) nach Übernahme der Kurswerte, unabhängig gerechnet: y = ln((ϑ − ϑu)/(ϑ0 − ϑu)) je Becher
    import math
    for name, becher in (("ln2", ["b2"]), ("ln23", ["b2", "b3"])):
        th0 = sum(KURS[b][0] for b in becher) / len(becher)
        th10 = sum(KURS[b][1] for b in becher) / len(becher)
        c = ke.kapazitaeten(E(thK0=th0, thMess=th10, thU=KURS["u"], thM=KURS["m"], kAQuelle="messung", becher=True))
        xs, ys = [], []
        for b in becher:
            for i in range(1, 7):
                xs.append([0, 10, 20, 30, 40, 50, 60][i] * 60.0)
                ys.append(math.log((KURS[b][i] - KURS["u"]) / (KURS[b][0] - KURS["u"])))
        b0 = sum(x * y for x, y in zip(xs, ys)) / sum(x * x for x in xs)
        out[name] = {s: zahlen.formatiere(-c["C_KB"] * b0, 4, s) for s in ("de", "en")}
        out[name]["n"] = len(xs)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
