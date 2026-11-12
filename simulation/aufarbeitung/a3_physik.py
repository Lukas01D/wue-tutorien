# -*- coding: utf-8 -*-
"""A3: Physikalische Proben an der schlanken Seite (Code der gebauten Seite über js_rechnen.js; Aufarbeitung vom 12.11.2026).

Jede Probe ist eine Aussage, die aus der Physik folgt und nicht aus dem Code. Fällt eine durch, ist der Code falsch oder die
Aussage gilt nicht allgemein; beides wird ausgegeben.
Aufruf: python3 simulation/aufarbeitung/a3_physik.py   (Ausgabe nach ergebnisse/a3_physik.txt)
"""
import itertools
import json
import os
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HIER)
from a2_vergleich import js, obergrenze_QW, KA_BLATT  # noqa: E402

BASIS = dict(t=45, tZ=45, thM=5, VM_ml=100, thK0=80, VK_ml=200, thU=20, QW=0.0, kA=KA_BLATT, CT=0)
WERTE = dict(thM=[2, 5, 50, 95], VM_ml=[10, 100, 200], thK0=[60, 80, 95], VK_ml=[50, 200, 400], thU=[10, 20, 30], CT=[0, 255, 600])
ZEITEN = [(1, 1), (45, 45), (90, 45), (180, 1), (180, 180)]


def faelle(**fest):
    """Alle Kombinationen von WERTE und ZEITEN; Felder in fest werden gesetzt (Zahl oder Funktion der Einstellung)."""
    aus = []
    for (t, tZ) in ZEITEN:
        for kombi in itertools.product(*WERTE.values()):
            e = dict(BASIS, **dict(zip(WERTE.keys(), kombi)), t=t, tZ=tZ)
            for k, v in fest.items():
                e[k] = v(e) if callable(v) else v
            aus.append(e)
    return aus


def main():
    zeilen = ["A3: Physikalische Proben an der schlanken Seite", ""]
    proben = []

    def probe(name, ok, info):
        proben.append((name, ok, info))

    # 1 Energiebilanz nach der Zugabe: Q2 − Q1 = C_G (θ1 − θ2), auch mit Wärmer und Tasse
    f1 = faelle(QW=lambda e: obergrenze_QW(e["kA"], e["thU"]) / 2)
    r1 = js({"schlank": f1})["schlank"]
    d1 = max(abs((r["Q2"] - r["Q1"]) - r["CG"] * (r["th1"] - r["th2"])) for r in r1)
    probe("Energiebilanz Q₂ − Q₁ = C_G·(θ₁ − θ₂) bei t ≥ t_Z (%d Fälle, mit Wärmer und Tasse)" % len(f1), d1 < 1e-6, "größte Abweichung %.1e J" % d1)

    # 2 Milch so warm wie der Kaffee: kein Sprung in Tasse 1
    f2 = faelle(thM=lambda e: e["thK0"])
    r2 = js({"schlank": f2})["schlank"]
    d2 = max(abs(r["th10"] - e["thK0"]) for r, e in zip(r2, f2))
    probe("Milch so warm wie der Kaffee: Tasse 1 ohne Sprung (%d Fälle)" % len(f2), d2 < 1e-9, "größter Sprung %.1e K" % d2)

    # 3 Milch so warm wie der Kaffee in Tasse 2 bei der Zugabe: kein Sprung in Tasse 2
    pre = js({"schlank": faelle()})["schlank"]
    f3 = [dict(e, thM=r["th2K"]) for e, r in zip(faelle(), pre)]
    r3 = js({"schlank": f3})["schlank"]
    d3 = max(abs(r["th2Z"] - r["th2K"]) for r in r3)
    probe("Milch so warm wie Tasse 2 bei der Zugabe: Tasse 2 ohne Sprung (%d Fälle)" % len(f3), d3 < 1e-9, "größter Sprung %.1e K" % d3)

    # 4 Milch mit Raumtemperatur, ohne Wärmer: Tasse 1 ist wärmer (größere Wärmekapazität während der Wartezeit)
    f4 = [e for e in faelle(thM=lambda e: e["thU"]) if e["t"] >= e["tZ"]]
    r4 = js({"schlank": f4})["schlank"]
    schlecht4 = [(e, r["th1"] - r["th2"]) for e, r in zip(f4, r4) if not r["th1"] - r["th2"] > 0]
    probe("Milch mit Raumtemperatur: Tasse 1 wärmer (%d Fälle)" % len(f4), not schlecht4,
          "kleinster Unterschied %.2e K" % min(r["th1"] - r["th2"] for r in r4))

    # 5 Größeres kA kühlt schneller (bei Inhalt wärmer als der Raum), gleiche Wärmerleistung
    schlecht5, n5 = [], 0
    for QW in (0.0, 0.5):
        reihen = [faelle(kA=k, QW=QW) for k in (0.01, 0.05, KA_BLATT, 0.5, 1.0)]
        rr = [js({"schlank": f})["schlank"] for f in reihen]
        for i in range(len(reihen[0])):
            if rr[0][i]["th10"] <= reihen[0][i]["thU"]:
                continue
            n5 += 1
            th = [rr[j][i]["th1"] for j in range(5)]
            if any(th[j + 1] > th[j] + 1e-12 for j in range(4)):
                schlecht5.append(reihen[0][i])
    probe("Größeres kA kühlt schneller: Tasse 1 bei t sinkt mit kA (%d Reihen, 5 Werte von kA, Wärmer 0 und 0,5 W)" % n5, not schlecht5,
          "%d Reihen nicht fallend" % len(schlecht5))

    # 6 Tassenwärmer an der Obergrenze: nie über 95 °C, Grenzwert θu + Q̇W/kA höchstens 95 °C
    f6 = [dict(e, kA=k, QW=obergrenze_QW(k, e["thU"])) for e in faelle() for k in (0.01, KA_BLATT, 0.5, 1.0)]
    r6 = js({"schlank": f6})["schlank"]
    hoch = max(max(max(r["k1"]), max(r["k2"])) for r in r6)
    grenz = max(e["thU"] + e["QW"] / e["kA"] for e in f6)
    cap_ok = all(abs(r["QWmax"] - obergrenze_QW(e["kA"], e["thU"])) < 1e-12 for e, r in zip(f6, r6))
    probe("Tassenwärmer an der Obergrenze der Seite: höchstens 95 °C (%d Fälle)" % len(f6), hoch <= 95 + 1e-9 and grenz <= 95 + 1e-9 and cap_ok,
          "höchste Temperatur %.3f °C, höchster Grenzwert %.3f °C, Obergrenze wie Formel: %s" % (hoch, grenz, cap_ok))

    # 7 Keine Werte außerhalb des physikalisch möglichen Bereichs (Stichproben der Kurven, 61 Punkte je Kurve)
    f7 = faelle(QW=lambda e: obergrenze_QW(e["kA"], e["thU"]))
    r7 = js({"schlank": f7})["schlank"]
    raus = 0
    for e, r in zip(f7, r7):
        inf = e["thU"] + e["QW"] / r["kA"]
        lo = min(e["thM"], e["thU"], e["thK0"]) - 1e-9
        hi = max(e["thM"], e["thK0"], inf) + 1e-9
        raus += any(not lo <= x <= hi for x in r["k1"] + r["k2"])
    probe("Temperaturen zwischen kältestem und wärmstem Beteiligten (Milch, Raum, Kaffee, Grenzwert des Wärmers) (%d Fälle)" % len(f7), raus == 0,
          "%d Fälle außerhalb; höchster Wert %.2f °C" % (raus, max(max(r["k1"] + r["k2"]) for r in r7)))

    # 8 Kipppunkt: zwischen kalter Milch (Tasse 1 wärmer) und heißer Milch (Tasse 2 wärmer) gibt es genau einen Wechsel
    r8 = js({"schlank": [dict(BASIS, thM=m) for m in [2 + i * 0.5 for i in range(187)]]})["schlank"]
    vz = [r["th1"] - r["th2"] for r in r8]
    wechsel = sum(1 for a, b in zip(vz, vz[1:]) if (a > 0) != (b > 0))
    probe("Werte des Blatts, Milch 2 bis 95 °C: genau ein Vorzeichenwechsel des Unterschieds", wechsel == 1 and vz[0] > 0 and vz[-1] < 0,
          "%d Wechsel, Unterschied bei 2 °C %.2f K, bei 95 °C %.2f K" % (wechsel, vz[0], vz[-1]))

    # 9 Wärmeaufnahme aus dem Raum: Fälle, in denen die angezeigte „abgegebene Wärme“ negativ wird
    f9 = faelle()
    r9 = js({"schlank": f9})["schlank"]
    neg = [(e, r) for e, r in zip(f9, r9) if r["Q1min"] < -1e-9 or r["Q2min"] < -1e-9]
    bsp = neg[0][0] if neg else None
    probe("Hinweis (keine Fehlerprobe): Mischung kälter als der Raum, Säule wird negativ", True,
          "%d von %d Rasterfällen; z. B. %s" % (len(neg), len(f9), json.dumps({k: bsp[k] for k in ("VK_ml", "VM_ml", "thK0", "thM", "thU", "CT")}) if bsp else "-"))

    # 10 Die Vergleichsbereiche decken den ganzen Regler ab, ohne Lücke
    j = js({"schlank": [dict(BASIS, kA=k, CT=c) for k in (0.01, 0.0199, 0.02, 0.06, 0.12, 0.4, 1.0) for c in (0, 0.5, 1, 50, 110, 200, 350, 600)]})
    nr = [(r["bereich_kA"], r["bereich_CT"]) for r in j["schlank"]]
    probe("Vergleichsbereiche: jeder Reglerwert hat genau einen Bereich", all(a >= 0 and b >= 0 for a, b in nr),
          "kA-Bereiche %s, C_T-Bereiche %s" % (sorted({a for a, _ in nr}), sorted({b for _, b in nr})))

    ok = 0
    for name, gut, info in proben:
        zeilen.append(("bestanden   " if gut else "FEHLER      ") + name + "  [" + info + "]")
        ok += gut
    zeilen += ["", "%d von %d bestanden" % (ok, len(proben))]
    text = "\n".join(zeilen) + "\n"
    print(text, end="")
    open(os.path.join(HIER, "ergebnisse", "a3_physik.txt"), "w", encoding="utf-8").write(text)
    return 0 if ok == len(proben) else 1


if __name__ == "__main__":
    raise SystemExit(main())
