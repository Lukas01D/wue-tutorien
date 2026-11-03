# Variante B des Kaffee-Aufgabenblatts (Entwurf, nicht mergen)

Wunsch der TL vom 31.10.2026, überarbeitet nach ihrer Rückmeldung vom 03.11.2026 (Entscheidungsprotokoll D117 bis D125). Nur das Einzelblatt, PDF und Word. Die Sammlung bleibt unverändert, bis die TL zwischen A und B entschieden hat. Die Lösung mit den Hinweisen gilt für beide Varianten und liegt bei Variante A (`ergebnisse/kaffee/fertig/`). R29 gilt für diese Variante nicht.

| Datei | Inhalt |
|---|---|
| `Kaffee_Aufgabe_Variante_B.pdf` | Blatt (XeLaTeX), Schild als Vektorgrafik aus der SVG |
| `Kaffee_Aufgabe_Variante_B.docx` | Blatt (Word), Schild als PNG (300 dpi), vom Text umflossen |
| `Kaffee_Aufgabe_Variante_B.md` | Markdown, aus dem beide gebaut sind |

Gebaut wird mit `python3 build_variante_b.py` im Ordner `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/variante_b/`.
- Das Skript nutzt einen eigenen Lua-Filter (`build/lehrstuhl_b.lua`) und einen eigenen Kopf mit `wrapfig` (`build/kopf_b.tex`). Kopfzeile und Word-Vorlage kommen aus `kaffee/build/`.
- Ausgangssituation, Frage 1, Annahmen, Tabelle, Teile a bis g und Versuch liest das Skript aus `sammlung/teile/t5a_kaffee.md`. Die Hausaufgabe liest es aus `kaffee/hausaufgabe_verdunstung.md`, dieselbe Datei wie bei Variante A.
- Für das PDF erzeugt Pandoc nur das LaTeX; XeLaTeX ruft das Skript selbst auf. Pandocs Vorlage lädt `babel` mit `bidi=default`, und damit setzt `wrapfig` das Schild ans Ende des Blatts. Das Skript lädt `babel` deshalb ohne diese Option; sie wird nur für Rechts-nach-links-Schrift gebraucht.

## Aufbau

1. **Grundlagen** (Energiebilanz: instationär, global): Rechts steht das Schild Variante 3, 6 cm breit (`vorlagen/bilanzformen/kompakt/Bilanzformen_kompakt_3_instationaer_global`). Der Text fließt daneben und darunter weiter.
   - Inhalt: Voraussetzung (homogen: durchmischt oder *Bi* ≪ 1, Foliensatz 02, Folie 16), die Bilanz d*U*/d*t* = *Q̇*<sub>zu</sub> − *Q̇*<sub>ab</sub> mit d*U* = *m c<sub>p</sub>* d*T*, die Wärmeabgabe *Q̇*<sub>ab</sub> = *kA* (*T* − *T*<sub>u</sub>) mit der Bedeutung von *kA*, ein Satz zu den Formelzeichen und der Lösungsweg (Trennung der Variablen in allgemeiner Form).
   - Kein Verweis auf die Formelsammlung (D24). Es stehen keine Ergebnisse der Teile a bis g und keine Lösung *T*(*t*) im Text.
2. **Lernziele:**
   - Ziel 1: *T*(*t*) aus einer instationären globalen Energiebilanz berechnen.
   - Ziel 2: Abweichungen zwischen der Vorhersage des Modells und den eigenen Messwerten (Versuch und Simulationstool) mit den Annahmen des Modells begründen.
3. **Einführung:** Ausgangssituation, Abb. 1, Frage 1 (Vorab-Frage).
4. **Gegeben:** Satz zur Messung, Annahmen, Tabelle.
5. **Gesucht:** zwei Sätze, dann a) bis g) wie bisher.
6. **Hausaufgabe** zur Verdunstung (wie in A).
7. **Versuch** als Messblatt auf eigener Seite.

## Änderungen an Texten der TL (gekennzeichnet)

| Stelle | bisher (A) | Variante B |
|---|---|---|
| Frage 1, letzter Satz | „…, bevor Sie Aufgabe 1 rechnen.“ | „…, bevor Sie rechnen.“ (es gibt keinen Baustein „Aufgabe 1“ mehr) |
| Versuch, Überschrift | „Versuch zu Aufgabe 1“ | „Versuch“ |
| Annahme zur Wärmeabgabe | *Q̇*<sub>ab</sub> = *kA* (*ϑ* − *ϑ*<sub>u</sub>) | *Q̇*<sub>ab</sub> = *kA* (*T* − *T*<sub>u</sub>), wie in den Grundlagen (R17, D121) |
| Aufgabe 1 | Überschrift „Aufgabe 1 (neu)“, Zwischenzeilen „Gegebene Größen:“ und „Aufgabenstellung:“ | entfallen; Abschnitte „Gegeben“ und „Gesucht“, Tabelle unter „Werte:“ |
| Frage 1 | eigener Baustein | fette Zwischenzeile im Abschnitt „Einführung“ |
| neu | | Grundlagen, Lernziele, die zwei Sätze unter „Gesucht“ |

Unverändert sind: Ausgangssituation, Abb. 1, Text von Frage 1 bis auf den letzten Satz, die übrigen Annahmen, Tabelle, Teile a bis g mit Ergebniszeilen, Hausaufgabe, Versuch mit Messtabelle.

**Formelzeichen (R17):** In Formeln steht *T* (Grundlagen, Annahmen, Teil b). Werte in °C heißen *ϑ* (Tabelle, Ergebnisse). Die Grundlagen sagen das in einem Satz.

## Umfang

| Abschnitt | Wörter |
|---|---:|
| Grundlagen | 181 |
| Lernziele | 43 |
| Einführung (Ausgangssituation 81, Frage 1 49) | 130 |
| Gegeben | 122 |
| Gesucht (davon Ergebniszeilen 23) | 296 |
| Hausaufgabe | 34 |
| Versuch | 164 |
| **gesamt** (mit Titel, 5 Wörter) | **975** |

Gezählt wie bisher mit `woerter_b.py` (eine Formel zählt als ein Wort). Zum Vergleich:
- Variante A: 733 Wörter (Ausgangssituation 81, Frage 1 51, Aufgabe 1 mit Hausaufgabe 434, Versuch 167).
- Erster Entwurf von B am 31.10.2026: 941 Wörter.

**Seiten:** PDF 5, Word 5 (Word über LibreOffice angesehen).

| Seite | PDF | Word |
|---|---|---|
| 1 | Titel, Grundlagen, Lernziele | Titel, Grundlagen, Lernziele |
| 2 | Einführung mit Abb. 1 und Frage 1, Gegeben (Messung, Annahmen) | Einführung mit Abb. 1 und Frage 1, Gegeben (Messung, Annahmen) |
| 3 | Werte (Tabelle), Gesucht a bis e | Werte, Gesucht a bis d |
| 4 | f, g, Hausaufgabe | e bis g, Hausaufgabe |
| 5 | Versuch (Messblatt) | Versuch (Messblatt) |

**4 Seiten mit Messblatt gehen nicht ohne Gedränge.** Die Seiten 1 bis 3 sind voll, und Abb. 1 und die Tabelle lassen sich nicht teilen. Für eine vierte Seite müssten f, g und die Hausaufgabe (etwa 9 cm) auf die Seiten 1 bis 3 rücken (D122).

## Hinweise

- **Silbentrennung:** In der Bauumgebung fehlen deutsche Trennmuster (`texlive-lang-german`), deshalb setzt das PDF ohne Silbentrennung. Das betrifft alle PDFs, auch A und die Sammlung. Damit neben dem Schild keine großen Wortabstände entstehen, steht der umflossene Absatz im Flattersatz.
- **Word-Ansicht:** LibreOffice setzt Einheiten in Formeln kursiv und lässt Abstände (\qquad) weg. Das betrifft A genauso; Word zeigt die Formeln aufrecht wie im PDF.
- **Hinweise der Lösung** sind für beide Varianten geschrieben. Die Tabelle zum Anspruch der Teile nennt bei b, dass b in Variante B näher an die Reproduktion rückt.
