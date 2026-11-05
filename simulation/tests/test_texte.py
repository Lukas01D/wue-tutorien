# -*- coding: utf-8 -*-
"""Prüfung der Texte und Zahlen in Texten (BAU_AUFTRAG.md, Teil 2.3).

Aufruf: python3 simulation/tests/test_texte.py
Geprüft (Toleranzen gibt es hier keine: Gleichheit der Zeichenketten):
  T1  Deutsch und Englisch haben dieselben Schlüssel.
  T2  Jeder Platzhalter {{z:..}}, {{e:..}}, {{v:..}} ist bekannt; nach dem Bau bleibt keiner übrig (bauen.texte_bauen).
  T3  Jede Formel lässt sich umsetzen; kein einzelnes $ bleibt übrig.
  T4  Jede literale Zahl in einem Text (außerhalb der Platzhalter) hat einen Herkunftseintrag in zahlen.LITERALE.
  T5  Keine Gedankenstriche (U+2013, U+2014) in Texten, Skripten, Vorlage und Stil.
  T6  Rundung und Dezimalzeichen: Deutsch mit Komma, Englisch mit Punkt; jede {{z:..}}-Zahl gleich dem nach der
      Stellenregel gerundeten ungerundeten Referenzwert, in beiden Sprachen mit gleichen Ziffern.
  T7  Gegenprobe der Kernzahlen gegen die unabhängig nachgerechneten Werte im Konzept (Abschnitte 6 und 8.2).
  T8  Vorgaben stimmen mit dem Code überein (Abtastpunkte in oberflaeche.js, Zufallssätze in test_kern.py).
  T9  Jeder Text-Schlüssel, den die Oberfläche fest anspricht, existiert; keine Schlüssel ohne Verwendung.
"""
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(os.path.dirname(HIER), "site")
sys.path.insert(0, SITE)
import bauen  # noqa: E402
import zahlen  # noqa: E402

ERG = []


def pruefe(name, ok, info=""):
    ERG.append((name, bool(ok), info))
    print(("ok    " if ok else "FEHLT ") + name + ("  " + info if info else ""))


def main():
    roh = {s: bauen.texte_lesen("texte_%s.txt" % s) for s in bauen.SPRACHEN}
    # T1
    nur = set(roh["de"]) ^ set(roh["en"])
    pruefe("T1 gleiche Schlüssel in DE und EN (%d)" % len(roh["de"]), not nur, ", ".join(sorted(nur)))
    # T2, T3
    try:
        _, fertig = bauen.texte_bauen()
        pruefe("T2/T3 Platzhalter bekannt, Formeln umsetzbar, kein $ übrig", True)
    except bauen.BauFehler as e:
        pruefe("T2/T3 Platzhalter bekannt, Formeln umsetzbar, kein $ übrig", False, str(e))
        fertig = None
    if fertig:
        rest = [s + "/" + k for s in fertig for k, t in fertig[s].items() if re.search(r"\{\{|\}\}", t)]
        pruefe("T2 nach dem Bau kein Platzhalter übrig", not rest, ", ".join(rest[:5]))
    # T4
    lit = {}
    for k, n, _ in zahlen.LITERALE:
        lit.setdefault(n, set()).add(k)
    ohne = []
    for s in roh:
        for k, t in roh[s].items():
            t2 = re.sub(r"\{\{[zev]:\w+\}\}", " ", t)
            t2 = re.sub(r"\{\w+\}", " ", t2)
            t2 = re.sub(r"<[^>]+>", " ", t2)
            for m in re.finditer(r"(?<![\w.,])\d+(?:[.,]\d+)?", t2):
                n = m.group(0)
                if not (n in lit and ("*" in lit[n] or k in lit[n])):
                    ohne.append("%s/%s: %s" % (s, k, n))
    pruefe("T4 jede literale Zahl hat eine Herkunft", not ohne, "; ".join(ohne[:8]))
    # T5
    striche = []
    for n in ["texte_de.txt", "texte_en.txt", "oberflaeche.js", "erweiterung.js", "hilfen.js", "vorlage.html", "stil.css", "regler.json"]:
        for i, z in enumerate(bauen.lies(n).split("\n"), 1):
            if "–" in z or "—" in z:
                striche.append("%s:%d" % (n, i))
    pruefe("T5 keine Gedankenstriche in den Quellen", not striche, ", ".join(striche[:8]))
    # T6
    mz = zahlen.modellzahlen()
    fehl = []
    for name, (w, st) in mz.items():
        de, en = zahlen.formatiere(w, st, "de"), zahlen.formatiere(w, st, "en")
        soll = ("%." + str(st) + "f") % round(w, st) if st > 0 else str(int(round(w)))
        soll = soll.replace("-", "−")
        if en != soll or de != soll.replace(".", ","):
            fehl.append("%s: de %s en %s soll %s" % (name, de, en, soll))
        if st > 0 and ("," not in de or "." in de or "." not in en or "," in en):
            fehl.append("%s: Dezimalzeichen" % name)
    pruefe("T6 Rundung und Dezimalzeichen der Modellzahlen (%d)" % len(mz), not fehl, "; ".join(fehl[:5]))
    falsch_dez = []
    for s, zeichen in (("de", r"\d\.\d"), ("en", r"\d,\d")):
        for k, t in fertig[s].items():
            ohne_math = re.sub(r"<math.*?</math>", " ", t, flags=re.S)
            ohne_math = re.sub(r"<code>.*?</code>", " ", ohne_math, flags=re.S)
            if re.search(zeichen, ohne_math):
                falsch_dez.append(s + "/" + k)
    pruefe("T6 Dezimalzeichen im fertigen Text je Sprache", not falsch_dez, ", ".join(falsch_dez[:6]))
    # T7: Werte aus KONZEPT.md (Abschnitte 6.1, 6.2, 8.2), dort unabhängig nachgerechnet (recherche/claude_f2)
    erwartet = {"th1": "34,05", "th2": "30,19", "dT": "3,85", "dQ": "3,69", "CG": "957,7", "Q1": "34,88", "Q2": "38,57",
                "dTmax": "3,86", "kA": "0,3402", "v3_Q1": "46,60", "v3_Q2": "50,34", "th10": "70,47"}
    abw = ["%s: %s statt %s" % (k, zahlen.formatiere(*mz[k], "de"), v) for k, v in erwartet.items() if zahlen.formatiere(*mz[k], "de") != v]
    pruefe("T7 Kernzahlen gleich den Konzeptwerten (%d)" % len(erwartet), not abw, "; ".join(abw))
    konzept = open(os.path.join(os.path.dirname(HIER), "KONZEPT.md"), encoding="utf-8").read()
    nicht_im_konzept = [v for v in erwartet.values() if v not in konzept]
    pruefe("T7 jede Vergleichszahl steht im Konzept", not nicht_im_konzept, ", ".join(nicht_im_konzept))
    # T8
    ui = bauen.lies("oberflaeche.js")
    m = re.search(r"const N_ABTAST = (\d+);", ui)
    pruefe("T8 Abtastpunkte im Text = Code", m and int(m.group(1)) == zahlen.VORGABEN["abtastpunkte"][0], m.group(1) if m else "nicht gefunden")
    tk = open(os.path.join(HIER, "test_kern.py"), encoding="utf-8").read()
    m = re.search(r"def test_zufall\(n=(\d+)\)", tk)
    pruefe("T8 Zufallssätze im Text = Test", m and int(m.group(1)) == zahlen.VORGABEN["testwerte"][0], m.group(1) if m else "nicht gefunden")
    # T9
    fest = set(re.findall(r'\bt\("([A-Za-z0-9_]+)"', ui)) | set(re.findall(r'data-t(?:-aria)?="([A-Za-z0-9_]+)"', bauen.lies("vorlage.html")))
    fest |= set(re.findall(r'(?:titel|text|aufl|ausgang|label|grundlage)": "([A-Za-z0-9_]+)"', ui + bauen.lies("regler.json")))
    fest |= set(re.findall(r'\w+: "([a-z0-9]+_[a-z0-9_]+)"', ui))
    wahl_ids = {"thermo_offen", "keramik_deckel"}
    fest = {k for k in fest if not k.endswith("_") and not re.search(r"_b$", k) and k not in wahl_ids}
    import json
    rj = json.loads(bauen.lies("regler.json"))
    dyn = ["regler_" + r["id"] for r in rj["regler"]] + ["hilfe_" + r["id"] for r in rj["regler"]] + [r["grundlage"] for r in rj["regler"]]
    dyn += ["hilfe_" + r["id"] for r in rj["schalter"]] + ["mess_kopf_b%d" % i for i in (1, 2, 3)]
    vor = re.findall(r'id: "(\w+)", faktor', bauen.lies("erweiterung.js"))
    dyn += ["vor_" + v for v in vor] + ["vor_text_" + v for v in vor]
    dyn += ["fehler_" + c for c in re.findall(r'"(anfang_ueber_raum|kA_positiv|messung_zwischen|\w+_\w+)"', bauen.lies("erweiterung.js").split("function fehler")[1].split("}")[0])]
    dyn += ["link_grund_" + g for g in ("zu_lang", "u", "m", "d", "b")]
    dyn += ["lesehinweis_" + a for a in re.findall(r'data-ansicht="(\w+)"', bauen.lies("vorlage.html")) if a != "temperatur"]
    pruefe("T9 Schlüsselfamilien vollständig (Regler, Hilfen, Voreinstellungen %d, Fehlercodes)" % len(vor),
           len(vor) == 6 and all(k in roh["de"] for k in dyn), ", ".join(k for k in dyn if k not in roh["de"]))
    fest |= set(dyn)
    fehlt = sorted(k for k in fest if k not in roh["de"] and re.match(r"^[a-z]", k) and "_" in k)
    pruefe("T9 jeder fest angesprochene Schlüssel existiert", not fehlt, ", ".join(fehlt[:10]))
    unbenutzt = sorted(k for k in roh["de"] if k not in fest and '"' + k + '"' not in ui)
    pruefe("T9 keine Schlüssel ohne Verwendung", not unbenutzt, ", ".join(unbenutzt[:12]))

    n_ok = sum(1 for _, ok, _ in ERG if ok)
    print("\nErgebnis: %d von %d Prüfungen bestanden." % (n_ok, len(ERG)))
    return 0 if n_ok == len(ERG) else 1


if __name__ == "__main__":
    sys.exit(main())
