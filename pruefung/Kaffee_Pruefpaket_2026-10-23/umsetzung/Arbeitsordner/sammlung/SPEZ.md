# Spezifikation: Aufgabensammlung der Tutorien im Lehrstuhl-Format

Stand 21.10.2026. Für alle Teilaufträge verbindlich. Arbeitsordner: `/home/claude/work/sammlung/`.

## 1. Ziel

Alle bisher erarbeiteten Tutoriumsaufgaben werden in eine einheitliche, schlanke Struktur nach dem Vorbild der Lehrstuhl-Tutorien gebracht und zu einer großen Aufgabensammlung (PDF und Word) zusammengesetzt. Die Tutoriumsleitung hat entschieden:

- Struktur wie die Aufgaben des Lehrstuhls (Vorbilder: Tutorium 3, Aufgabe 3 und Tutorium 6, Aufgabe 1), minimalistisch, nicht zu komplex, aber didaktisch fordernd.
- **Neu:** Ganz am Anfang jedes Aufgabenblocks steht eine **Ausgangssituation**: ein entspannter, anschaulicher Text mit einer **Skizze**, damit sich die Studierenden in die Situation hineindenken können. Danach kommen die **Frage(n)** (zuerst die Vorab-Frage), danach die **Aufgabe** mit Annahmen, gegebenen Größen und Aufgabenstellung.

**Musterbeispiel (genau so aufbauen):** `teile/t5a_kaffee.md` (erzeugt von `rechnung/t5_kaffee_teil.py`). Bitte zuerst lesen und als PDF ansehen (Abschnitt 7).

Weitere Orientierung (nur lesen):
- Strukturvorlage: `/home/claude/work/kaffee/Strukturvorlage_Aufgaben_Lehrstuhl.md`
- Lehrstuhl-Vorbilder: `/home/claude/work/lehrstuhl/md/Tutorium_3_W#U00e4rmedurchgang.md` (Aufgabe 3) und `/home/claude/work/lehrstuhl/md/Tutorium_6_Bilanzen_Teil_II.md` (Aufgabe 1 und 3)

## 2. Quellen der Inhalte (nur lesen, nicht ändern)

- Ideensammlung „Leitaufgaben aus Klima und Erde“: `/home/claude/work/doc2/Leitaufgaben_Klima_Erde_2026-10-17.md` (Abschnitt 4: Aufgabenskizzen je Tutorium mit Arbeitswerten, Teilaufgaben, Kernzahlen, Zusatzaufgaben, Vorab-Fragen; Abschnitt 12: Quellen; Anhang A: Rechenprotokoll)
- Pilotblatt Tutorium 1 mit Musterlösung: `/home/claude/work/pilot/Pilot_Tutorium1_Eisschild.md`, Skript `/home/claude/work/pilot/pilot_tutorium1.py`, Grafikskript `/home/claude/work/scripts/pilot_t1_grafiken.py`
- Aufgabenideen Ozean und Atmosphäre: `/home/claude/work/ozean/Aufgabenideen_Ozean_Atmosphaere.md`
- Rechenskripte: `/home/claude/work/rechnung/nachrechnung_leitphaenomene.py` (Ausgabe `nachrechnung_ausgabe.txt`), `/home/claude/work/rechnung/nachrechnung_ozean_atmosphaere.py` (Ausgabe `nachrechnung_ozean_atmosphaere_ausgabe.txt`)
- Formelsammlung (Text): `/home/claude/work/lehrstuhl/md/00_2026_Formelsammlung_final.md`

Inhalte, Arbeitswerte und Teilaufgaben werden **übernommen**, nicht neu erfunden. Kürzen und Umformulieren ist erlaubt und erwünscht, wenn es der Struktur dient. Jede inhaltliche Änderung (Wert, gestrichener Teil, neue Frage) gehört in den Bericht (Abschnitt 8).

## 3. Deine Ausgaben (nur im Arbeitsordner)

| Datei | Inhalt |
|---|---|
| `teile/tN.md` (bzw. die im Auftrag genannten Namen) | Markdown des Tutoriums |
| `skripte/abb_tN_<kurz>.py` | je Skizze ein Skript, Stil aus `skripte/skizze_stil.py` |
| `grafik/tN_<kurz>.png` und `.svg` | die Skizzen (von den Skripten erzeugt) |
| `rechnung/tN_rechnung.py` und `rechnung/tN_rechnung_ausgabe.txt` | Skript, das **jede Zahl** der Ergebniszeilen und der Tabellen berechnet bzw. ausgibt (Name, Wert, Einheit) |
| `quellen/tN_quellen.md` | Quellen der verwendeten Arbeitswerte und Fakten, je Aufgabe, als Liste (aus den Quellenverzeichnissen der Ausgangsdokumente übernehmen, mit DOI oder Link) |

Dateien anderer Tutorien nicht anfassen. Außerhalb des Arbeitsordners nichts ändern (Scratch-Ordner für Prüfbilder ist erlaubt).

## 4. Aufbau einer Teildatei

```
# Tutorium N: Thema

## Titel des ersten Aufgabenblocks

**[Ausgangssituation]{.underline}**

Text ...

![](grafik/tN_kurz.png){width=85%}

**Abb. 1:** Kurzer Titel

**[Frage 1]{.underline}** (Vorab-Frage)

Text ...

**[Frage 2]{.underline}**

Text ...

**[Aufgabe 1]{.underline}** (neu)

Optional ein Satz Überleitung.

**Annahmen:**

- ...

***Gegebene Größen:***

| Tabelle wie im Musterbeispiel |

**Aufgabenstellung:**

a) Text ...\
   $Ergebnis$

b) ...

## Titel des zweiten Aufgabenblocks

**[Ausgangssituation]{.underline}**
...
**[Aufgabe 2]{.underline}** (neu, technischer Zwilling)
...

## Zusatzaufgaben

**[Zusatzaufgabe 1]{.underline}** (neu): Titel

Text mit Werten, Teile a) bis c) mit Ergebniszeilen.
```

Titel der Tutorien (H1, genau so): 1 Wärmeleitung · 2 Konvektion · 3 Wärmedurchgang · 4 Strahlung · 5 Wärmebilanzen (instationär global) · 6 Wärmebilanzen (stationär differentiell) · 7 Wärmebilanzen (instationär differentiell) · 8 Wärmeübertrager und Verdampfer

### 4.1 Bausteine

- **Blocktypen:** *L* (große Aufgabe, bisher „Leitaufgabe“), *Z* (mittlere Aufgabe, z. B. technischer Zwilling), *K* (kurze Zusatzaufgabe). L und Z bekommen je einen H2-Titel, eine Ausgangssituation mit Skizze und eine nummerierte Aufgabe. K-Aufgaben stehen gesammelt unter `## Zusatzaufgaben` am Ende des Tutoriums, ohne Skizze und ohne Ausgangssituation.
- **Ausgangssituation:** L 60 bis 150 Wörter, Z 30 bis 90 Wörter. Anschaulich, im Präsens, Sie-Form, ein Fließtext ohne Aufzählung und ohne Formeln. Ein bis drei Fakten aus den „Wussten Sie schon?“-Ideen einweben, aber nur solche, deren Zahl später in der Rechnung oder einem Vergleich vorkommt („Reserve“-Fakten weglassen). Keine Quellenangaben im Text.
- **Skizze:** genau eine Abbildung je L- und Z-Block. Sie zeigt die Situation und die Größen mit den Formelzeichen der Tabelle, aber keine Lösung (keinen Bilanzraum, wenn er gesucht ist). Stil: `skripte/skizze_stil.py` (Carlito, gedeckte Farben, rote Pfeile für Wärmeströme). Im Markdown: `![](grafik/tN_kurz.png){width=85%}` (Breite 55 bis 95 %), direkt danach ein eigener Absatz `**Abb. n:** Titel`. Abbildungen je Tutorium ab 1 nummerieren (in Tutorium 5 hat der Kaffee-Block Abb. 1).
- **Fragen:** Frage 1 ist die Vorab-Frage des ersten Blocks mit dem Zusatz „(Vorab-Frage)“ und dem Auftrag, eine Vermutung zu notieren. Danach höchstens drei kurze Konzeptfragen (aus den Zusatzaufgaben der Ideensammlung: Zuordnen, Ankreuzen, Einheiten, Profile lesen), je ein bis vier Zeilen, Auswahlmöglichkeiten als kurze Liste. Spätere Blöcke dürfen eine eigene Vorab-Frage haben; die Nummern laufen im Tutorium weiter.
- **Aufgabe n (Herkunft):** „(neu)“; beim technischen Zwilling „(neu, technischer Zwilling)“. Nummern laufen im Tutorium weiter.
- **Annahmen:** drei bis sechs kurze Sätze im Lehrstuhlstil („… wird als ideal durchmischt angenommen.“, „… wird vernachlässigt.“). Wo die Ideensammlung einen Teil zum Aufstellen oder Begründen von Annahmen hat, bleibt ein solcher Teil erhalten (z. B. „Begründen Sie zwei der Annahmen“ oder „Welche Annahme ist am fragwürdigsten?“), denn das Aufstellen und Begründen von Annahmen ist ein entschiedenes Lernziel.
- **Gegebene Größen:** Tabelle nach Objekt gruppiert, vier Spalten, Spaltentrenner exakt wie im Musterbeispiel (`|:---------------------|:-----------------------------|:---------------------|:-----------------------------|`), Gruppenkopf `| ***Objekt:*** | | ***Objekt:*** | |`, Leerzeile `| | | | |` zwischen Gruppen, Zeilen `| Bezeichnung: | $Symbol = Wert\,\mathrm{Einheit}$ |`. Kurze Bezeichnungen (sie brechen sonst um). Stoffwerte, die man bei einer bestimmten Temperatur braucht (z. B. Luft bei Filmtemperatur), stehen in der Tabelle. Ist eine Größe nicht in der Formelsammlung und keine Stoffkonstante (z. B. *λ*(*T*) von Eis), steht unter der Tabelle ein Satz „… ist hier gegeben (nicht in der Formelsammlung).“
- **Aufgabenstellung:** Teile a), b), … im Imperativ mit „Sie“, höchstens neun Teile je Aufgabe (sonst auf zwei Aufgaben aufteilen). Unterpunkte als (1), (2) im Fließtext. Das Ergebnis jedes rechnenden Teils steht nach einem Zeilenumbruch `\` in der nächsten Zeile, eingerückt mit drei Leerzeichen, wie im Musterbeispiel. Mehrere Ergebnisse: `$A = …$, $\quad B = …$`. Eine Ergebniszeile darf **nicht** mit „(1)“ beginnen (sonst wird eine Liste daraus); stattdessen „Zu (1): …“. Qualitative Teile haben keine Ergebniszeile. Keine Lernziel-Kennzeichen wie [Q1], keine Phasennamen, keine Kästen „Wussten Sie schon?“, keine Erwartungshorizonte, keine Lösungswege.

## 5. Schreibweise

- Pandoc-Markdown, Mathe in `$…$`. Dezimalkomma in Mathe immer als `{,}` (`$0{,}058$`). Einheiten aufrecht mit `\,\mathrm{…}` (`$q = 58\,\mathrm{mW/m^2}$`, `\,\mathrm{W/(m^2\,K)}`, `\,\mathrm{W/(m\,K)}`). Grad Celsius als `\,\mathrm{°C}` mit echtem Gradzeichen (nicht `^\circ`). Indizes mit Text aufrecht: `T_{\mathrm{O}}` oder kurz `T_O`, einheitlich je Tutorium.
- Keine Tausenderpunkte (in Mathe würde der Punkt als Dezimalpunkt gelesen): vierstellige Zahlen ohne Trenner (`3700`), ab fünf Stellen mit schmalem Abstand (`15\,790` in Mathe, „15 790“ im Text). Zehnerpotenzen als `6{,}7\cdot 10^{6}`.
- ϑ in °C, *T* in K, Index u für Umgebung, Kennzahlen kursiv ($Re$, $Pr$, $Nu$, $Gr$, $Bi$). Formelzeichen wie in Vorlesung und Formelsammlung (Nußelt, *α*, *λ*, *k*, *Q̇* als `\dot{Q}`, *q̇* als `\dot{q}`).
- Ergebnisse mit sinnvoller Genauigkeit (meist zwei Nachkommastellen oder drei bis vier gültige Ziffern), gerundet wie die Skriptausgabe.
- Deutsch, klare kurze Sätze. **Keine Gedankenstriche** (weder – noch —) und kein Bindestrich als Gedankenstrich; stattdessen Komma, Punkt, Doppelpunkt oder Klammern. Bereiche mit „bis“ („20 bis 30 °C“). Typografische Anführungszeichen „…“. „z. B.“ mit Leerzeichen. Minuszeichen in Mathe ist ein normales `-`.
- Keine Quellenangaben im Aufgabentext. Ausnahme: Ein Teil vergleicht ausdrücklich mit einem Literatur- oder Messwert, dann Kurzbeleg in Klammern, z. B. „(Talalay et al., 2020)“.

## 6. Zahlen

- Jede Zahl in Ergebniszeilen und Tabellen muss `rechnung/tN_rechnung.py` reproduzieren. Das Skript darf die vorhandenen Skripte importieren (`sys.path`) oder Formeln nachbauen; es schreibt eine beschriftete Liste aller Werte nach `rechnung/tN_rechnung_ausgabe.txt`.
- Arbeitswerte aus den Ausgangsdokumenten übernehmen. Weicht ein neu berechneter Wert von den dort genannten Kernzahlen ab, die Ursache klären und im Bericht nennen.
- Vor der Abgabe: Ergebniszeilen gegen die Skriptausgabe abgleichen.

## 7. Prüfen vor der Abgabe

1. Skripte laufen fehlerfrei: `python3 rechnung/tN_rechnung.py`, alle `skripte/abb_tN_*.py`.
2. Teil bauen und **jede Seite ansehen**: `python3 /home/claude/work/sammlung/build/teil_bauen.py teile/tN.md <dein Scratch-Ordner>` erzeugt PDF und Seitenbilder (`…-1.png` mit 70 dpi, `…_gross-1.png` mit 110 dpi). Prüfen: Skizzen lesbar und nicht abgeschnitten, Tabellen ohne Überlauf, Ergebniszeilen an der richtigen Stelle, keine leeren Listen oder kaputten Formeln, Ausgangssituation vor den Fragen.
3. `grep -n "–\|—" teile/tN.md quellen/tN_quellen.md` liefert nichts; auch Skizzen ohne Gedankenstrich.
4. Struktur gegen Abschnitt 4 prüfen (Reihenfolge Ausgangssituation, Fragen, Aufgabe; Nummern fortlaufend).

## 8. Bericht (Antwort an den Auftraggeber)

Kurz und auf Deutsch oder Englisch:
- Liste der Blöcke je Tutorium: Typ (L, Z, K), Titel, Zahl der Teile, Abbildungsdatei.
- Änderungen gegenüber den Ausgangsdokumenten: geänderte oder neue Werte (mit Grund), gestrichene oder zusammengelegte Teile, neue Fragen.
- Offene Punkte und Unsicherheiten.
- Bestätigung der Prüfungen aus Abschnitt 7.
