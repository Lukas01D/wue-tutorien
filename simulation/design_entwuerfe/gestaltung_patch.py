# -*- coding: utf-8 -*-
"""Kleine, gestaltungsbedingte Änderungen an simulation/site/src/oberflaeche.js für die Entwürfe (beim Bau angewendet).

Jede Ersetzung muss genau einmal (bzw. die angegebene Zahl) passen, sonst bricht der Bau ab. So bleibt die Übertragung auf
einen neueren Stand der Seite prüfbar: Passt eine Stelle nicht mehr, meldet der Bau sie.
Was sich ändert (nur Darstellung, keine Rechnung, keine Texte, keine Abläufe):
  G1  Diagrammgröße, Diagrammschrift und Ränder kommen aus CSS-Variablen des Entwurfs (--dia-...), mit den heutigen Werten als Vorgabe.
  G2  Geschätzte Zeichenbreite der Beschriftungen (für die Kollisionsprüfung) aus --dia-zeichenbreite, passend zur Schrift.
  G3  Schrittleiste (Start, Zeitpunkt, Versuch, Vertiefung) über der Frage, nur wenn die Vorlage data-schritte="1" setzt.
      Sie ist aria-hidden: die Frageleiste nennt den Schritt schon in Worten („Frage 1 von 2“). Texte: vorhandene Schlüssel.
Die Farben des Diagramms ändert keine Zeile hier: Die CSS des Entwurfs überschreibt die SVG-Attribute über Attributselektoren.
"""

ERSETZUNGEN = [
    # G1: Größe und Ränder
    ("    const W = Math.round(Math.min(780, Math.max(280, halter.getBoundingClientRect().width || 640)));\n"
     "    const H = Math.round(W < 520 ? W * 0.78 : Math.min(W * 0.56, Math.max(window.innerHeight < 500 ? 170 : 280, window.innerHeight * 0.5)));",
     "    const W = Math.round(Math.min(GV(\"--dia-max-breite\", 780), Math.max(280, halter.getBoundingClientRect().width || 640)));   // GESTALTUNG G1\n"
     "    const H = Math.round(W < 520 ? Math.min(W * GV(\"--dia-handy-verhaeltnis\", 0.78), window.innerHeight * GV(\"--dia-handy-hoehe\", 1)) :\n"
     "      Math.min(W * GV(\"--dia-verhaeltnis\", 0.56), Math.max(window.innerHeight < 500 ? 170 : 280, window.innerHeight * GV(\"--dia-hoehe\", 0.5))));", 1),
    ("    const fs = 12, L = 52, Rr = 14, O = 16, U = 44;",
     "    const fs = GV(\"--dia-schrift\", 12), L = GV(\"--dia-rand-links\", 52), Rr = 14, O = 16, U = GV(\"--dia-rand-unten\", 44);   // GESTALTUNG G1", 1),
    # G2: Zeichenbreite
    ("text.length * fs * 0.56", "text.length * fs * ZB", 1),
    ("txt.length * 11 * 0.56", "txt.length * 11 * ZB", 1),
    ("txt.length * fs * 0.56", "txt.length * fs * ZB", 1),
    ("tl.length * fs * 0.56", "tl.length * fs * ZB", 1),
    ("  function diagrammZeichnen() {\n",
     "  function diagrammZeichnen() {\n    const ZB = GV(\"--dia-zeichenbreite\", 0.56);   // GESTALTUNG G2\n", 1),
    # Hilfsfunktion für G1 und G2
    ("  const REG = Object.fromEntries(REGLER_DEF.regler.map(r => [r.id, r]));\n",
     "  const REG = Object.fromEntries(REGLER_DEF.regler.map(r => [r.id, r]));\n"
     "  // GESTALTUNG: Zahl aus einer CSS-Variablen des Entwurfs, sonst Vorgabe\n"
     "  const GV = (n, d) => { const v = parseFloat(getComputedStyle(document.documentElement).getPropertyValue(n)); return isFinite(v) ? v : d; };\n"
     "  function schritteHtml(f) {      // GESTALTUNG G3\n"
     "    if (document.documentElement.getAttribute(\"data-schritte\") !== \"1\") return \"\";\n"
     "    const st = [[\"start\", \"leiste_start\"], [\"f1\", \"f1_titel\"], [\"f2\", \"f2_titel\"], [\"v\", \"leiste_vertiefung\"]];\n"
     "    const jetzt = f.id[0] === \"v\" ? \"v\" : f.id;\n"
     "    const fertig = id => id === \"v\" ? false : (S.antworten[id].fest || (id === \"f2\" && S.f2Uebersprungen));\n"
     "    return '<ol class=\"schritte\" aria-hidden=\"true\">' + st.map(([id, k]) => '<li class=\"' + (id === jetzt ? \"jetzt\" : (fertig(id) ? \"fertig\" : \"offen\")) + '\"><span>' + nurText(t(k)) + \"</span></li>\").join(\"\") + \"</ol>\";\n"
     "  }\n", 1),
    # G3: Schrittleiste als erstes Element der Frageleiste (vor dem Rückblick auf die Startfrage)
    ("    let h = \"\";\n    const st = S.antworten.start;\n    if (f.id === \"f1\" && st.fest && !a.fest) {",
     "    let h = schritteHtml(f);   // GESTALTUNG G3\n    const st = S.antworten.start;\n    if (f.id === \"f1\" && st.fest && !a.fest) {", 1),
]


class PatchFehler(Exception):
    pass


def anwenden(js):
    for alt, neu, anzahl in ERSETZUNGEN:
        n = js.count(alt)
        if n != anzahl:
            raise PatchFehler("Stelle passt %d-mal statt %d-mal: %r" % (n, anzahl, alt[:70]))
        js = js.replace(alt, neu)
    return js
