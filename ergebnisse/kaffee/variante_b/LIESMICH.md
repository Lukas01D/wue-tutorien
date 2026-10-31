# Variante B des Kaffee-Aufgabenblatts (Entwurf, nicht mergen)

Wunsch der TL vom 31.10.2026: nur das Einzelblatt, PDF und Word. Sammlung, Lösung und das bisherige Einzelblatt bleiben unverändert. R29 gilt für diese Variante nicht.

| Datei | Inhalt |
|---|---|
| `Kaffee_Aufgabe_Variante_B.pdf` | Blatt (XeLaTeX), Schild als Vektorgrafik aus der SVG |
| `Kaffee_Aufgabe_Variante_B.docx` | Blatt (Word), Schild als PNG (300 dpi) |
| `Kaffee_Aufgabe_Variante_B.md` | Markdown, aus dem beide gebaut sind |

Gebaut mit `python3 build_variante_b.py` im Ordner `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/variante_b/` (eigener Lua-Filter `build/lehrstuhl_b.lua`; Kopfzeile und Word-Vorlage aus `kaffee/build/`). Ausgangssituation, Frage 1, Annahmen, Tabelle, Teile a bis g und Versuch liest das Skript aus `sammlung/teile/t5a_kaffee.md`, damit die Variante nicht vom Original abweicht.

## Aufbau

1. **Grundlagen** (Energiebilanz: instationär, global): links Text (65 % der Breite), rechts das Schild Variante 3 (`vorlagen/bilanzformen/kompakt/Bilanzformen_kompakt_3_instationaer_global`, im PDF 5,3 cm, in Word 5,2 cm breit). Voraussetzung (homogen: durchmischt oder *Bi* ≪ 1), Bilanz d*U*/d*t* = *Q̇*<sub>zu</sub> − *Q̇*<sub>ab</sub> und d*U* = *m c<sub>p</sub>* d*T*, Wärmeabgabe *Q̇*<sub>ab</sub> = *kA* (*T* − *T*<sub>u</sub>) mit Bedeutung von *kA*, Lösungsweg (gewöhnliche DGL, Trennung der Variablen in allgemeiner Form). Keine Ergebnisse der Teile a bis g, keine Lösung *T*(*t*).
2. **Lernziele**: zwei Ziele aus dem Lernziel-Auszug, Abschnitt 4.5 (Ziel 1 berechnen, Ziel 2 beurteilen), auf die Kaffee-Aufgabe zugeschnitten.
3. **Einführung**: Ausgangssituation, Abb. 1, Frage 1 (Vorab-Frage).
4. **Gegeben**: Satz zur Messung, Annahmen, Tabelle.
5. **Gesucht**: zwei Sätze, dann a) bis g) wie bisher.
6. **Versuch** als Messblatt auf eigener Seite.

## Änderungen an Texten der TL (gekennzeichnet)

| Stelle | bisher | Variante B |
|---|---|---|
| Frage 1, letzter Satz | „…, bevor Sie Aufgabe 1 rechnen.“ | „…, bevor Sie rechnen.“ (es gibt keinen Baustein „Aufgabe 1“ mehr) |
| Versuch, Überschrift | „Versuch zu Aufgabe 1“ | „Versuch“ |
| Aufgabe 1 | Überschrift „Aufgabe 1 (neu)“, Zwischenzeilen „Gegebene Größen:“ und „Aufgabenstellung:“ | entfallen; Abschnitte „Gegeben“ und „Gesucht“, Tabelle unter „Werte:“ |
| Frage 1 | eigener Baustein | fette Zwischenzeile im Abschnitt „Einführung“ |
| neu | | Grundlagen, Lernziele, die zwei Sätze unter „Gesucht“ |

Unverändert: Ausgangssituation, Abb. 1, Text von Frage 1 bis auf den letzten Satz, Annahmen, Tabelle, Teile a bis g mit Ergebniszeilen, Versuch mit Messtabelle.

## Umfang

| Abschnitt | Wörter |
|---|---:|
| Grundlagen | 172 |
| Lernziele | 52 |
| Einführung (Ausgangssituation 81, Frage 1 49) | 130 |
| Gegeben | 122 |
| Gesucht (davon Ergebniszeilen 23) | 296 |
| Versuch | 164 |
| **gesamt** (mit Titel, 5 Wörter) | **941** |

Zählweise wie bisher (`woerter_b.py`, Formeln zählen als ein Wort). Zum Vergleich das bisherige Einzelblatt: 699 Wörter (Ausgangssituation 81, Frage 1 51, Aufgabe 1 400, Versuch 167). Gegeben und Gesucht zusammen (418) entsprechen der bisherigen Aufgabe 1.

**Seiten:** PDF 5, Word 5 (Ansicht über LibreOffice).

| Seite | PDF | Word |
|---|---|---|
| 1 | Titel, Grundlagen, Lernziele | Titel, Grundlagen |
| 2 | Einführung mit Abb. 1 und Frage 1, Gegeben (Messung, Annahmen) | Lernziele, Einführung mit Abb. 1 und Frage 1 |
| 3 | Werte (Tabelle), Gesucht a bis e | Gegeben (Messung, Annahmen, Werte), Gesucht a |
| 4 | Teile f und g (Seite zu etwa einem Drittel gefüllt) | Teile b bis g |
| 5 | Versuch (Messblatt) | Versuch (Messblatt) |

Für vier Seiten im PDF müssten etwa 5 cm entfallen (Tabelle und Abb. 1 lassen sich nicht teilen); das ist nicht gemacht.

## Hinweise für die Entscheidung

- **Fundstellen:** Foliensatz 05, Folie 8 ist am Foliensatz im Paket geprüft. „Foliensatz 02, Folie 16“ für *Bi* ≪ 1 stammt aus dem Lernziel-Auszug (Auflösung der Vorab-Frage); Foliensatz 02 liegt nicht im Paket, die Folie ist also nicht am Original geprüft. Für die Trennung der Variablen gibt es in Foliensatz 05, Folien 1 bis 21, keine Fundstelle; deshalb der Verweis „zur Kontrolle: Formelsammlung, Kap. 5, Gl. 5.1“ (allgemeine Lösung von d*y*/d*x* + *ay* = *b*). Diese Gleichung enthält die Form der Lösung; soll Teil b streng über die Trennung der Variablen laufen, den Verweis streichen.
- **Lernziel 2** (Biot-Zahl, Durchmischung) übt das Blatt nur mittelbar (Annahme „ideal durchmischt“, Becher in Teil g); voll geübt wird es mit der Biot-Hausaufgabe. Das optionale Blockziel (Grundform zuordnen) ist nicht aufgenommen: Das Schild markiert die Form schon.
- **Word-Ansicht:** LibreOffice setzt Einheiten in Formeln kursiv und schluckt Abstände (\qquad); das betrifft das bisherige Einzelblatt genauso, Word zeigt die Formeln aufrecht wie im PDF.
- **Protokolle** sind nicht fortgeschrieben (erst nach der Entscheidung der TL).
