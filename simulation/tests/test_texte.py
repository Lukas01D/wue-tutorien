# -*- coding: utf-8 -*-
"""Texte der Kaffee-Seite Fassung 3. Aufruf: python3 simulation/tests/test_texte.py (Ergebnis nach test_texte_ergebnis.txt)."""
import os
import re
import sys

HIER = os.path.dirname(os.path.abspath(__file__))
SIM = os.path.dirname(HIER)
sys.path.insert(0, os.path.join(SIM, "site"))
import bauen  # noqa: E402
import zahlen  # noqa: E402

ergebnisse = []
KERNSATZ = ("Stimmt die Simulation mit deiner Rechnung überein, ist die Rechnung bestätigt, nicht das Modell. "
            "Ob das Modell stimmt, zeigt nur der Versuch.")
# Ergebnisse von Teilaufgaben des Blatts (DE-Schreibweise): dürfen auf der Startkarte nicht stehen
ERGEBNISSE = ["43,85", "40,29", "3,56", "45,43", "70,47", "25,49", "28,90", "3,41", "0,1994", "18,6", "58,2", "47,76", "48,55", "2,56"]
# Zahlen in den Texten, die keine Modellzahl sind (Herkunft): Nummern, Zeiten und Werte des Blatts, Grenzen der Seite
LITERALE = {"0": "Ziffer, Unterschied 0, Index", "1": "Tasse 1, Index, Annahme 1", "2": "Tasse 2, Index", "3": "Auftrag 3",
            "6": "Annahmen 1 bis 6", "01": "Schritt 01", "02": "Schritt 02", "03": "Schritt 03", "04": "Schritt 04",
            "10": "Messung nach 10 min (Blatt), Messblatt", "20": "Messblatt 20 min", "30": "Grenze 30 °C (D3), Zugabe 30 min",
            "60": "60 min (Blatt), Trinktemperatur 60 °C (d2)", "90": "Zugabe 90 min (Auftrag 3)", "100": "Bereich 0 bis 100 °C",
            "5": "Tutorium 5", "1,0": "Index", "4": "Teil g4"}


def pruefe(name, ok, info=""):
    ergebnisse.append((name, bool(ok), info))


def sichtbar(t):
    """Text ohne Tags und ohne Formeln."""
    return re.sub(r"<[^>]+>", " ", re.sub(r"<math.*?</math>", " ", t, flags=re.S))


def main():
    roh, fertig = bauen.texte_bauen()
    de, en = fertig["de"], fertig["en"]
    pruefe("Schlüssel DE und EN gleich", set(de) == set(en), str(set(de) ^ set(en)))
    platz = lambda t: sorted(re.findall(r"\{(\w+)\}", sichtbar(t)))
    pruefe("Laufzeit-Platzhalter DE und EN gleich", all(platz(de[k]) == platz(en[k]) for k in de),
           ", ".join(k for k in de if platz(de[k]) != platz(en[k])))
    # Gedankenstriche in Texten und allen Quellen der Fassung 3
    dateien = [os.path.join(SIM, "site", "src", n) for n in os.listdir(os.path.join(SIM, "site", "src")) if n.endswith((".txt", ".js", ".html", ".css"))]
    dateien += [os.path.join(SIM, "site", n) for n in ("bauen.py", "zahlen.py", "schriften_teilen.py")]
    dateien += [os.path.join(SIM, n) for n in ("KONZEPT_F3.md", "ENTSCHEIDUNGEN_F3.md")]
    dateien += [os.path.join(HIER, n) for n in os.listdir(HIER) if n.endswith((".py", ".js"))]
    mit = [os.path.relpath(f, SIM) for f in dateien if os.path.exists(f) and re.search("[\u2013\u2014]", open(f, encoding="utf-8").read())]
    pruefe("keine Gedankenstriche (Texte, Quellen, Konzept, Entscheidungen, Tests)", not mit, ", ".join(mit))
    # Dezimalzeichen
    de_punkt = [k for k, t in de.items() if re.search(r"\d\.\d", sichtbar(t))]
    en_komma = [k for k, t in en.items() if re.search(r"\d,\d", sichtbar(t))]
    pruefe("Deutsch mit Dezimalkomma", not de_punkt, ", ".join(de_punkt))
    pruefe("Englisch mit Dezimalpunkt", not en_komma, ", ".join(en_komma))
    # du-Form durchgehend (G2: auch allein zu Hause)
    sie = [k for k, t in de.items() if re.search(r"\b(Sie|Ihre?[nmrs]?|Ihnen|euer|eure[nmrs]?|euch|Wählt|Legt|Stellt|Schreibt|Notiert)\b", sichtbar(t))]
    pruefe("Deutsch in du-Form", not sie, ", ".join(sie))
    pruefe("Kernsatz wörtlich nach Leitlinie 6", de["kernsatz"] == KERNSATZ, de["kernsatz"])
    pruefe("Vertiefung gekennzeichnet: nach dem Tutorium oder zu Hause (T1)", "nach dem Tutorium oder zu Hause" in de["w_titel"]
           and "after the tutorial or at home" in en["w_titel"])
    nummern = [sichtbar(de["s%d_nr" % i]).split()[0] for i in range(1, 5)]
    pruefe("Pflichtweg durchgehend 01 bis 04 (T2), Vertiefung ohne Nummer", nummern == ["01", "02", "03", "04"]
           and not re.match(r"\s*0\d", sichtbar(de["w_titel"])), str(nummern))
    start = ["zweck", "s1_nr", "s1_titel", "s1_lage", "s1_wahl", "s1_wahl_1", "s1_wahl_2", "s1_wahl_0", "s1_grund", "s1_grund_e",
             "s1_grund_s", "s1_grund_h", "s1_grund_x", "s1_freitext", "s1_e", "s1_knopf", "s1_fehlt", "kopf_zeile", "kopf_titel", "dia_leer"]
    verrat = [k for k in start for z in ERGEBNISSE if z in de[k]]
    pruefe("Startkarte verrät nichts (keine Ergebniszahl)", not verrat, ", ".join(verrat))
    pruefe("Startkarte ohne Antwortwort", not any(re.search(r"\b(kälter|bestätigt|abgegeben)\b", sichtbar(de[k])) for k in start))
    pruefe("Simulationswerte nicht als Messwerte bezeichnet (B05)", "keine Messung" in de["s3_beispiel"] and "nicht gemessen" in de["annahmen"]
           and "berechnet" in de["leg_beispiel"])
    pruefe("Startkarte: Grund per Tipp, Freitext freiwillig (T3)", "tippe" in de["s1_grund"] and "freiwillig" in de["s1_freitext"])
    # Herkunft jeder Zahl: Modellzahl aus zahlen.py oder Literal mit Herkunft
    erlaubt = set(zahlen.alle("de").values()) | set(LITERALE)
    fremd = {}
    for k, t in de.items():
        for z in re.findall(r"\d+(?:,\d+)?", sichtbar(t)):
            if z not in erlaubt:
                fremd.setdefault(z, []).append(k)
    pruefe("jede Zahl in den Texten aus zahlen.py oder mit Herkunft", not fremd, "; ".join("%s: %s" % (z, ", ".join(v)) for z, v in fremd.items()))
    gleich = all(sorted(re.findall(r"\d+", sichtbar(de[k]))) == sorted(re.findall(r"\d+", sichtbar(en[k]))) for k in de)
    pruefe("dieselben Zahlen in DE und EN", gleich, ", ".join(k for k in de if sorted(re.findall(r"\d+", sichtbar(de[k]))) != sorted(re.findall(r"\d+", sichtbar(en[k])))))
    pruefe("Säulenzahlen nicht in den Texten der Säulen vor der Antwort", not re.search(r"\d,\d|kJ", de["s2_saeulen"] + de["s2_saeulen_aria"] + de["s2_frage"]))

    zeilen = ["Texte Fassung 3", ""]
    for n, ok, info in ergebnisse:
        zeilen.append(("bestanden   " if ok else "FEHLGESCHLAGEN ") + n + ("  [" + info + "]" if info and not ok else ""))
    gut = sum(1 for _, ok, _ in ergebnisse if ok)
    zeilen += ["", "%d von %d bestanden" % (gut, len(ergebnisse))]
    text = "\n".join(zeilen) + "\n"
    open(os.path.join(HIER, "test_texte_ergebnis.txt"), "w", encoding="utf-8").write(text)
    print(text)
    sys.exit(0 if gut == len(ergebnisse) else 1)


if __name__ == "__main__":
    main()
