# Konzept Fassung 3: Kaffee-Simulation, schlank und passend zum Blatt Fassung 3

> Stand 08.11.2026, Claude (Cloud-Sitzung, Zweig `claude/kaffee-simulation-v3-qw4zb2`). Auftrag: Startprompt Fassung 3 der TL mit Startpaket vom 08.11.2026. Grundlagen: Blatt, Lösung und Hinweise Fassung 3, Entscheidungsvorlage B01 bis B24 (Fassung 3), `werte.py`, unverändertes `kaffee_modell.py`, Dossiers L1 und L2, Entwürfe A, B, C und Variante 0 (`simulation/DESIGN_ENTWUERFE.md` auf `claude/simulation-design-assignment-w01on3`). Der **Hauptteil (Abschnitte 1 bis 7) ist die Entscheidungsgrundlage**; die Anhänge A bis D sind Nachschlagematerial. Jede Gestaltungsentscheidung mit Quelle steht zusätzlich in `simulation/ENTSCHEIDUNGEN_F3.md`. **Fragen an Lukas: Abschnitt 7 (D1 bis D10).**

## 1 Zweck und Lernziele

**Zweck (oben auf der Seite):** „Die Seite klärt, welche Tasse nach einer Stunde wärmer ist und warum.“ Dazu der Satz: gedacht für die Zeit nach Teil e (Leitlinien 1 und 3; L2 C2.3, D1 S1).

Nach der Seite kannst du …

1. **erklären**, warum Tasse 1 trotz Energieerhaltung wärmer ist: Der schwarze Kaffee gibt bis zur Zugabe mehr Wärme ab (Säulen, $Q_2 - Q_1$). Leitet zu Teil f über (B09).
2. **unterscheiden**, was Rechnung, Simulation und Messung zeigen: Übereinstimmung mit der Rechnung bestätigt die Rechnung; ob das Modell stimmt, zeigt nur der Versuch (B05, B12; L2 C0.2, C2.4).
3. in kleinen Aufträgen **vorhersagen und prüfen**, wie Milchtemperatur und Zeitpunkt der Zugabe den Unterschied ändern (L1 S4).

## 2 Ablauf in Zuständen

Eine Seite ohne Reiter. Laptop und Beamer: links die Schritte, rechts die angeheftete Bühne (Kernzahlen, Diagramm, Regler). Handy: eine Spalte, die Regler direkt unter dem Diagramm. Pflichtweg: 01, 02, 03, 05 (Schätzung 1,5 + 3 + 2 + 1 = 7,5 min; Ziel höchstens 8 min, beim ersten Einsatz stoppen, O4).

| Zustand | Auslöser | sichtbar | gesperrt |
|:--|:--|:--|:--|
| **Z0 Start** | Öffnen, „Von vorn“ | Kopf, Zweck, **01 Vorhersage**: Wahl (Tasse 1, Tasse 2, gleich), Grund (drei typische Gründe oder eigener Satz), freiwillig ϑ₁ und ϑ₂ aus Teil e; am Laptop leerer Diagrammrahmen mit Achsen und Raumlinie | alles mit Ergebnis: Kurven, Zahlen, Säulen, Modell, Regler |
| **Z1 Ergebnis** | „Festhalten und Kurven zeigen“ (Wahl und Grund nötig) | 01 als Zeile; Kernzahlen nach 60 min; Kurven mit Direktbeschriftung; eigene Rechnung als Kreuze; Kernsatz (Leitlinie 6); Annahmenzeile; **02 Warum?** mit Säulen **ohne Zahlen** und drei Erklärungen zur Wahl | Zahlen an den Säulen, Regler, 03 bis 05 |
| **Z2 Erklärt** | Antwort in 02 | Rückmeldung zur gewählten Erklärung mit Begründung, dann $Q_1$, $Q_2$, $Q_2 - Q_1$ und Verweis auf f1, f2; Regler (sichtbar: Milchtemperatur, Zugabe; zugeklappt: Ausgangswerte); **03 Messung dazulegen**, **04 Weiterdenken**, **05 Zum Schluss**, Modell | Milchtemperatur über 30 °C (D3) |
| **Z3 Auftrag n** | „Vermutung festhalten, dann prüfen“ in 04 | Werte des Blatts eingestellt, Zeile „Auftrag n, deine Vermutung …“ über dem Diagramm; danach „Gedanken dazu“ | Auftrag 3 erst hebt die 30-°C-Grenze auf |
| **Z4 Schluss** | Antwort in 05 | „Gedanken dazu“ (Simulation, Versuch, Rechnung) | |

Keine Punkte, keine Uhr, keine Bewertung „richtig/falsch“ (L2 C2.8); Rückmeldung immer mit Grund (L1 S5).

## 3 Bleibt, geht, Entscheidung

| Bereich | Fassung 2 | Fassung 3 | Grund und Quelle |
|:--|:--|:--|:--|
| Pflichtweg | Start, Frage 1 Zeitpunkt, Frage 2 Versuch mit Kurslink | 01 Vorhersage mit Grund, 02 Warum mit Säulen, 03 Messung, 05 Schlussfrage | Leitlinien 2, 4, 7, 10; L1 S1, S2, S6; L2 C2.2 |
| Vertiefung | V1 bis V6 | drei Aufträge „erst vermuten, dann prüfen“ (D8) | L1 S4; G1; O6 entfällt |
| Regler | zehn Regler, zwei Schalter, sechs kA-Voreinstellungen, kA-Quelle | Milchtemperatur, Zugabe; Ausgangswerte: Kaffee bei $t_0$, Raum, $kA$ der Tasse in W/K, Milchmenge (D1, D2) | SE2; G1; L2 E5 (nicht möglichst viele Funktionen) |
| Texte | drei Reiter, rund 830 Textzeilen je Sprache | ein Bereich „Modell“: Annahmen, Bilanz, so rechnet die Seite, Grenzen | Leitlinie 5; Mayer Kohärenz |
| Messwerte | Messblatt, Kurslink, Übernahme, Becher 3 | ein Eingabefeld je Tasse, nur auf dem Gerät; Beispielwerte einblendbar; kein Übernahmeknopf (D7) | SE3, SE4, G2 |
| ln-Ansicht | Ansicht mit Ausgleichsgerade | schlank für Versuch 1 (D6) | Blatt Versuch 1 nennt das Werkzeug |
| entfällt ganz | | Becher (nur Satz unter „Grenzen“), Wärmestrom-Ansicht, Bilanzraum-Skizze, Vergleichslauf, CSV, Trinkzeit, kalter Becher, $kA_1$ relativ, Milch für Tasse 2 bei Raumtemperatur, Anheften am Handy, Kurslink | G1; L2 E5 |

## 4 Standardwerte und Prüfwerte

Eine Stelle in der Seite (`STANDARD`), mit Test gegen `werte.py`; „vorläufig“ gekennzeichnet (SE6). Nach der Messung im Januar ändert sich nur diese Stelle.

| Größe | Wert | Kennzeichnung |
|:--|:--|:--|
| Kaffee 200 ml, 80 °C; Milch 30 ml, 5 °C; Raum 20 °C | Blatt | Kaffee, Milch, Mengen vorläufig (M1, M2) |
| Messwert nach 10 min (Deckel) | 72 °C, daraus $kA$ = 0,1994 W/K | vorläufig (M3), auf der Seite sichtbar |
| nach 60 min: Tasse 1; schwarzer Kaffee; Tasse 2 nach der Milch | 43,85; 45,43; 40,29 °C; Unterschied 3,56 K | Test relativ unter 1e-9 |
| $Q_1$, $Q_2$, Differenz | 25,49; 28,90; 3,41 kJ | ebenso |
| Mischtemperatur Tasse 1; Schnittpunkt; Zeit bis 60 °C | 70,47 °C; 95,1 min; 18,6 min | ebenso |
| erwärmte Milch 70 °C: Tasse 1, Tasse 2; Kipppunkt | 47,76; 48,55 °C; 58,2 °C | nur in Auftrag 3 |
| Beispielwerte (Kontrollseite) | Tasse 1: 72,5 66,1 60,6 55,7 51,4 47,6 44,2; Tasse 2: 80,0 72,0 65,1 59,1 53,9 49,3 45,4, nach der Milch 41,4 °C | „berechnet mit Tasse, vorläufig, keine Messung“ |

Selbst nachgerechnet (Modell, unverändert): Milch 20 °C 2,56 K; größter Unterschied 3,86 K bei Zugabe nach 95 min, Rest bei sehr später Zugabe 1,91 K; Kipppunkt 68,1 / 58,2 / 49,9 °C bei Zugabe nach 30 / 60 / 90 min. **Korrektur zum Auftrag:** Die Milchmenge ändert den Unterschied stark (10 ml 1,37 K, 60 ml 5,85 K, 100 ml 7,70 K), den Kipppunkt aber kaum (58,0 bis 58,6 °C).

Der Bau prüft alle Abnahmekriterien aus Abschnitt 4 des Auftrags, dazu die Sperren (vor Z1 keine Ergebniszahl im DOM und in Ansagen; Säulenzahlen erst nach 02; Milch über 30 °C erst nach Auftrag 3) und die Prüfliste D1 (Anhang C).

## 5 Medienprofil (L2 C2.1)

**Gestaltungsart:** Computersimulation als eine HTML-Datei, offline, ohne fremde Server. **Formen:** Aufgabe (Vorhersage, Warum, drei Aufträge, Schlussfrage), Simulation (Kurven, Säulen), Werkzeug (Regler, Messpunkte), kurzer Lehrtext (Modell). **Codierung:** Kurven, Säulen, Formeln, kurze Texte; schematisch, keine Bilder von Tassen (L2 C2.7). **Ablauf:** ruhend, selbst gesteuert, nicht adaptiv, keine Animation. **Bedingungen:** Deutsch und Englisch, WCAG 2.2 AA, offener Code, nichts wird gesendet; entstanden mit KI (Claude), geprüft durch Codex (X6), entschieden von der TL. **Auswertung** im Tutorium, nicht auf der Seite: Strichliste zur Vorab-Frage (Vortest), Umfrage vor g, Austrittsfrage (B21, Z3; L2 C2.11).

## 6 Gestaltungssynthese (SE1)

Optik von **A „Messprotokoll“** (Papier, Tinte, Tintenblau, IBM Plex, Mono-Zahlen), je Element das Beste aus A, B, C und 0 (Tabelle mit Quellen: Anhang A). Kern:

- **Anordnung:** A für Laptop und Beamer (Schritte links, Diagramm rechts, jetzt angeheftet); am Handy die Regler direkt unter dem Diagramm (Lehre aus C) statt Anheften.
- **Regler:** Bedienung von **C** in der Optik von **A**: Lineal mit beschrifteten Hauptmarken, Griff 22 × 38 px in 48 px hoher Fläche, Plus und Minus 48 × 48 px, Zahlenfeld daneben, Tastatur nach APG. Belegt mit WCAG 2.5.7, 2.5.8, 2.5.5, Apple (44 pt), Android (48 dp), Microsoft und PatternFly.
- **Auswahl:** ganze Zeile mit rundem Marker (B, C), weil die Kästchen von A Mehrfachauswahl nahelegen.
- **Kernzahlen:** Messwertzeile von A mit den großen Zahlen von C; Unterschied in Tintenblau.
- **Diagramm:** Raster 10 und 5 statt Millimeterpapier (Daten-Tinte); Direktbeschriftung; gleiche Farben und Linienarten in Kurven und Säulen; Klammer $Q_2 - Q_1$ hervorgehoben.
- **Ablauf:** nummerierte Abschnitte 01 bis 05 (A), keine eigene Schrittleiste, keine Reiter.

Bilder des Musters (`simulation/f3_entwurf/muster.html`, 114 kB mit Schriften, kein fertiger Bau): `simulation/bildschirmfotos/f3_entwurf/` (Startkarte und Ergebnis bei 390 × 844 und 1366 × 768, Ergebnis am Beamer 1280 × 720; alle ohne Querscrollen; am Beamer Kernzahlen, ganzes Diagramm und beide Regler im Bild). Erwartete Größe der fertigen Seite: 150 bis 200 kB (heute 433 kB).

## 7 Fragen an Lukas (je mit Empfehlung)

| Nr. | Frage | Empfehlung |
|:--|:--|:--|
| D1 | **Anordnung der Regler (SE2):** Milchtemperatur und Zugabe sichtbar unter dem Diagramm; Kaffee bei $t_0$, Raum, $kA$, Milchmenge als **zugeklappte** Gruppe mit Zusammenfassung „Kaffee 80 °C · Raum 20 °C · kA 0,1994 W/K (vorläufig) · Milch 30 ml“ und Knopf „Werte des Blatts“. Oder offen, aber kleiner? | **zugeklappt** (G1; am Beamer passt sonst das Diagramm nicht mit den Reglern ins Bild) |
| D2 | **Milchmenge** als vierter Ausgangswert (10 bis 100 ml)? Sie ändert den Unterschied stark, den Kipppunkt kaum. | **ja** |
| D3 | **Warme Milch erst nach g3:** Regler bis 30 °C; darüber erst nach der Vermutung in Auftrag 3 (Hinweis am Regler). Schützt die Umfrage vor g (Z3) und g1 bis g3. | **ja** |
| D4 | **Zahlen an den Säulen** ($Q_1$, $Q_2$, Differenz) erst nach der Antwort in 02, damit f1 und f2 eigene Rechnungen bleiben. | **ja** |
| D5 | **Startkarte:** Grund Pflicht (Auswahl oder eigener Satz); ϑ₁ und ϑ₂ aus Teil e freiwillig, dann Kreuze im Diagramm und Satz „stimmen überein“ oder „weicht ab, siehe Kontrollseite“. Das Feld „etwa … K“ entfällt. | **ja** |
| D6 | **ln-Ansicht** für Versuch 1 (Blatt: „auf Papier oder im Simulationstool“): Schalter in 03, nur Tasse 2 vor der Milch, Gerade des Modells, keine Ausgleichsgerade. Oder streichen und das Blatt ändern. | **behalten, schlank** |
| D7 | **Kein Knopf „aus den Messwerten übernehmen“:** Kaffee, Raum und eigenes $kA$ (Versuch 1) stellt man selbst ein, ein Satz sagt wie. | **kein Knopf** (das eigene $kA$ ist die Rechnung der Studierenden) |
| D8 | **Drei Aufträge:** 1 Milch mit Raumtemperatur (ist der Zeitpunkt dann egal?), 2 Zeitpunkt (wann ist der Unterschied am größten?), 3 erwärmte Milch nach g3 (hängt der Kipppunkt vom Zeitpunkt ab?). Oder nur 1 und 3. | **alle drei** |
| D9 | **Speichern nur auf dem Gerät:** Fortschritt und Messpunkte im Browser, nichts wird gesendet; „Von vorn“ löscht. | **ja** |
| D10 | **Gestaltungssynthese** nach Anhang A und den Bildern bestätigen, darin IBM Plex aus A statt Fira Sans des Lernzentrums. | **bestätigen** |

**Hinweise zum Blatt (nicht Teil des Baus):** H1: Kurzantwort 1 der Kontrollseite („die späteren Punkte liegen leicht über der Geraden“) passt zu echten Messungen; mit den Beispielwerten liegt Tasse 2 genau auf der Geraden, weil sie mit festem $kA$ berechnet sind. Vorschlag: Halbsatz „(mit den Beispielwerten genau auf der Geraden)“. H2: Der Absatz „Stand der Seite“ in den Hinweisen wird nach dem Merge ersetzt.

---

## Anhang A: Gestaltungssynthese Element für Element

Quellen (selbst geöffnet, Anhang D): WCAG = WCAG 2.2; APG = ARIA Authoring Practices „Slider“; MS = Microsoft-Richtlinien „Sliders“; PF = PatternFly „Slider“; Apple = Human Interface Guidelines, Accessibility; Android = Android Developers „Make apps more accessible“; Mayer = Mayer 2024, Tabelle 6 (Effektstärke d); EU = EU-Leitfaden Datenvisualisierung „Direct labelling“; NNg = Moran 2022 „Clutter-Free“. Kontraste der Synthese gemessen (WCAG-Formel): Text 16,3; leiser Text 7,4; Akzent 8,0; Weiß auf Hauptknopf 8,1; Tasse 1 6,7; Raumlinie 4,8; Feldrand 15,6.

| Element | A Messprotokoll | B Kaffeehaus | C Hörsaal | 0 heute | Kriterium mit Quelle | Wahl |
|:--|:--|:--|:--|:--|:--|:--|
| Grundton | Papier, Tinte, Tintenblau | Milchschaum, Espresso | Weiß, Schwarz, Signalblau | Marine (Lernzentrum) | SE1; WCAG 1.4.3 und 1.4.11 (alle erfüllt) | **A** |
| Textschrift | IBM Plex Sans | Source Sans 3, Fraunces | Atkinson (Null mit Strich) | Fira Sans | SE1; Ziffern in Temperaturen gewohnt lesbar | **A** |
| Zahlen | Plex Mono, springt nicht | Serifenziffern | fett | Fira | MS: Wert beim Ziehen sichtbar halten | **A** |
| Laptop, Beamer | Frage links, Diagramm rechts, ganz im Bild | Diagramm oben, Frage darunter | Diagramm links, Frage rechts | Frage oben, Diagramm halb im Bild | Mayer räumliche Nähe (d = 0,82); Beamer-Befund Fassung 2 | **A**, Diagrammspalte angeheftet |
| Handy | Kernzahlen über angeheftetem Diagramm | große Karten | größte Ziele | angeheftet | WCAG 1.4.10, 2.4.11; Mayer Kohärenz (0,86) | eine Spalte, Regler direkt unter dem Diagramm, **kein Anheften** |
| Ablauf | Schrittleiste 01 bis 04 | keine | Schrittleiste mit Nummern | Frageleiste | Mayer Signalisierung (0,69), Segmentierung (0,67); G1 | **nummerierte Abschnitte (A)**, keine Leiste |
| Auswahl | Kästchen (wirkt wie Mehrfachwahl) | Kacheln mit Kreis | dicke Blöcke | Kreise | WCAG 2.5.8; Apple 44 pt; Android 48 dp | ganze Zeile 48 px, **runder Marker (B, C)**, Formularlinien (A) |
| Eingabefeld | Unterstrich | gerundet | dicker Rahmen | Rahmen | WCAG 1.4.11 (Rand 3:1) | Unterstrich 2 px auf getöntem Feld (A) |
| Kernzahlen | kleine Messwerttabelle | große Serifenzahlen unten | große Kacheln, Δ blau | Zeile | Lesbarkeit am Beamer; Signalisierung | Messwertzeile **(A)** mit großen Zahlen **(C)**, Unterschied blau |
| Raster | Millimeter 1, 5, 10 | nur waagerecht | dünn | dünn | NNg (Daten-Tinte); Ablesen der Messpunkte braucht Raster | **10 und 5**, kein Millimeterraster |
| Kurven | 2,5 px | 3,2 px | 4 px | 2,5 px | WCAG 1.4.11 (3:1); Beamer | 3 px (Handy 2,5 px); Tasse 1 braun durchgezogen, Tasse 2 schwarz gestrichelt (alle) |
| Beschriftung | direkt, Mono | direkt | direkt, fett | direkt | EU; L2 C2.6 | **direkt**, halbfett in Kurvenfarbe; Legende nur für Punktformen |
| Säulen | wie 0 | wie 0 | wie 0 | neben dem Diagramm | L2 C2.6 (gleiche Farben, Differenz hervorheben); Mayer räumliche Nähe zur Frage | **bei der Warum-Frage**, Farben wie Kurven, Klammer $Q_2 - Q_1$ blau |
| Reglerspur | Lineal mit Strichen | dicke Spur mit Verlauf | schwarze Spur 10 px | schlank | MS: Skalenmarken und Wert bei genauen Werten; PF: Min und Max zeigen | **Lineal (A)** mit beschrifteten Hauptmarken |
| Griff, Tasten, Wert | Griff 16 px, Tasten 44 px | runder Griff 28 px | Griff 34 px, Tasten 52 px | Tasten 44 px | WCAG 2.5.7, 2.5.8, 2.5.5; Apple; Android; APG (Pfeile, Bild auf/ab, Pos1/Ende); PF (Feld und Tasten) | **Bedienung C**: Griff 22 × 38 px in 48 px Fläche, Tasten 48 px, Zahlenfeld |
| Navigation | Karteireiter | Pillen | volle Breite | drei Reiter | G1; Mayer Kohärenz | **keine Reiter**, ein Bereich „Modell“ |
| Knöpfe | Rahmen, Tintenblau | gefüllt Espresso | gefüllt Blau | ein dunkler Hauptknopf | WCAG 1.4.11 | ein gefüllter Hauptknopf je Schritt, sonst Rahmen (A) |
| Fokus | 3 px blau | grün | schwarz mit gelbem Saum | 2 px | WCAG 2.4.7, 2.4.11 | 3 px Tintenblau mit Abstand (A); nie verdeckt |
| Ecken, Schatten | 2 px, kaum | 16 bis 20 px, weich | 6 px, keine | 4 px | G1; L2 C2.6 (keine Zierelemente) | **eckig, ohne Schatten (A)** |
| Rückmeldung | blaue Kante | grüner Kasten | gelber Kasten | Kante | Mayer Signalisierung | blaue Kante auf Hellblau (A) |

## Anhang B: Texte (Deutsch, kurz; Englisch entsteht im Bau nach dem Glossar von Fassung 2)

- **Kopf:** „Tutorium 5 · Wärmebilanzen, instationär global“ · „Kaffee mit Milch: Simulation“ · „DE ↔ EN“.
- **Zweck:** „Wozu? Die Seite klärt, welche Tasse nach einer Stunde wärmer ist und warum. Gedacht für die Zeit nach Teil e des Blatts: erst die Temperaturen beider Tassen nach 60 min selbst rechnen.“
- **01 Vorhersage:** „Welche Tasse ist nach 60 min wärmer?“ · „Zwei gleiche Tassen mit Deckel, je 200 ml Kaffee mit 80 °C, Raum 20 °C. Tasse 1 bekommt 30 ml Milch aus dem Kühlschrank sofort, Tasse 2 erst nach 60 min.“ · Wahl: „Tasse 1 (Milch sofort)“, „Tasse 2 (Milch später)“, „beide gleich warm“ · Grund: „Die Energie bleibt erhalten.“, „Der schwarze Kaffee bleibt länger heiß.“, „Heißer Kaffee gibt mehr Wärme ab.“, „eigener Grund: …“ · „Deine Ergebnisse aus Teil e (freiwillig): ϑ₁ … °C, ϑ₂ … °C“ · Knopf „Festhalten und Kurven zeigen“ · Hinweis „Wähle eine Tasse und einen Grund.“ · danach „Deine Vorhersage: …“.
- **Bühne:** „nach 60 min“ · „Tasse 1“, „Tasse 2, nach der Milch“, „Unterschied“ · Kernsatz ohne eigene Werte: „Stimmt die Simulation mit deiner Rechnung überein, ist die Rechnung bestätigt, nicht das Modell. Ob das Modell stimmt, zeigt nur der Versuch.“ · mit passenden Werten (bis 0,1 K): „Simulation und deine Rechnung stimmen überein: bestätigt ist damit die Rechnung, nicht das Modell. Ob das Modell stimmt, zeigt nur der Versuch.“ · sonst: „Deine Rechnung weicht ab (ϑ₁: … statt … °C). Prüfe Zeit in Sekunden und Rundung; häufige Fehler stehen auf der Kontrollseite.“ · Annahmenzeile: „Berechnet, nicht gemessen. Annahmen wie im Blatt: Inhalt ideal durchmischt, Deckel dicht (keine Verdunstung), Wärmeabgabe kA(ϑ − ϑu) mit festem kA, Tasse ohne Wärmekapazität, Raum konstant. Modell“ · Kurven „Tasse 1: Milch sofort“, „Tasse 2: Milch nach … min“, „Raum … °C“ · Legende „× deine Rechnung · ○ □ Beispielwerte des Blatts (berechnet, vorläufig) · ● ■ eure Messung“.
- **Regler:** „Milchtemperatur ϑM [°C]“ mit Hinweis „über 30 °C erst in Auftrag 3 (nach Teil g3)“ · „Zugabe in Tasse 2 nach tZ [min]“ · Gruppe „Ausgangswerte des Blatts“: „Kaffee bei t0 ϑK,0 [°C]“, „Raum ϑu [°C]“, „kA der Tasse [W/K]“ mit „entspricht … °C nach 10 min (Blatt: 72 °C, vorläufig)“, „Milchmenge VM [ml]“, Knopf „Werte des Blatts“.
- **02 Warum?:** „Wohin ist die Energie gegangen?“ · „Beide Tassen starten mit derselben Energie in Kaffee und Milch. Warum ist Tasse 2 am Ende trotzdem kälter? Wählt die Erklärung, die die Säulen zeigen.“ · Säulentitel „An den Raum abgegebene Wärme bis zur Zugabe“ · a „Tasse 2 hat in der Stunde mehr Wärme an den Raum abgegeben.“ · b „Die kalte Milch kühlt Tasse 2 am Ende stärker ab als Tasse 1 am Anfang.“ · c „Beim Mischen geht Energie verloren.“ · Rückmeldung a: „Ja. Der schwarze Kaffee in Tasse 2 war die ganze Stunde heißer als Tasse 1 und hat deshalb mehr Wärme abgegeben: Q₁ = 25,49 kJ, Q₂ = 28,90 kJ. Die 3,41 kJ fehlen Tasse 2; geteilt durch 957,7 J/K (Kaffee und Milch) sind das 3,56 K.“ · b: „Das denken viele. Der Sprung beim Zugießen ist bei Tasse 2 sogar kleiner (5,1 K gegen 9,5 K), weil ihr Kaffee dann kühler ist. Entscheidend ist die Wärme, die beide vorher abgeben: …“ (weiter wie a) · c: „Beim Mischen geht im Modell nichts verloren (Annahme 1). Entscheidend ist die Wärme, die beide an den Raum abgeben: …“ (weiter wie a) · Überleitung: „Weiter auf dem Blatt: In f1 und f2 rechnet ihr das nach.“
- **03 Messung dazulegen:** „Legt eure Messwerte über die Kurven: Werte in der Reihenfolge des Messblatts (0, 10, 20, … min), getrennt durch Leerzeichen; Komma oder Punkt.“ · Felder „Tasse 1“, „Tasse 2 (letzter Wert: 60 min, nach der Milch)“ · Anzeige „erkannt: …“ · Schalter „Beispielwerte des Blatts zeigen (berechnet mit dem Modell und vorgewärmter Tasse, vorläufig, keine Messung)“ · „Damit die Kurven zu eurem Versuch passen: unter Ausgangswerte Kaffee bei t0, Raum und euer kA aus Versuch 1 einstellen, oben die Milchtemperatur.“ · „Wo weichen Punkte und Kurven am stärksten ab? (Versuch 3)“ · D6: Schalter „Tasse 2 als ln-Darstellung (Versuch 1)“.
- **04 Weiterdenken:** Auftrag 1 „Milch mit Raumtemperatur: Ist der Zeitpunkt dann egal?“ (ja, beide gleich warm · nein, Tasse 1 bleibt wärmer · nein, jetzt ist Tasse 2 wärmer) · Prüfen „Stellt die Milchtemperatur auf 20 °C.“ · Gedanken „Tasse 1 bleibt wärmer, der Unterschied sinkt aber von 3,56 auf 2,56 K. Auch ohne kalte Milch gibt der heißere schwarze Kaffee bis zur Zugabe mehr Wärme ab. Wie die Milch wirkt, klärt g4.“ · Auftrag 2 „Zeitpunkt: Bei welcher Zugabe ist der Unterschied am größten?“ (Zahl in min) · „Verschiebt die Zugabe in Tasse 2.“ · „Am größten bei Zugabe nach etwa 95 min (3,86 K), dort schneiden sich die Kurven. Solange der schwarze Kaffee wärmer ist als Tasse 1, gibt er mehr Wärme ab, und der Unterschied wächst; danach gibt er weniger ab. Bei sehr später Zugabe bleiben 1,91 K, weil die kalte Milch Tasse 2 beim Mischen abkühlt.“ · Auftrag 3 „Erwärmte Milch (nach Teil g3): Hängt die Milchtemperatur, bei der beide Tassen gleich warm sind, vom Zeitpunkt der Zugabe ab?“ (später: höher · später: niedriger · gleich) · „Stellt eine Zugabe ein, zum Beispiel 30 oder 90 min, und sucht mit der Milchtemperatur den Unterschied 0.“ · „Je später die Zugabe, desto niedriger: 68,1 °C nach 30 min, 58,2 °C nach 60 min, 49,9 °C nach 90 min. Die warme Milch gibt in Tasse 1 bis zur Zugabe Wärme an den Raum ab, je länger, desto mehr; Tasse 2 bekommt sie erst bei der Zugabe.“ · Knöpfe „Vermutung festhalten, dann prüfen“, „Gedanken dazu“, „ohne Vermutung aufdecken“.
- **05 Zum Schluss:** „Was zeigt die Simulation, was der Versuch nicht zeigen kann, und umgekehrt? Notiert je einen Satz.“ · Gedanken: „Simulation: den ganzen Verlauf, die abgegebene Wärme, viele Fälle in Sekunden, aber nur, was im Modell steht. Versuch: ob das Modell die echten Tassen trifft, mit Tasse, Dampf und Raum, aber nur einen Fall und mit Messunsicherheit. Die Rechnung zeigt, warum.“ · „Von vorn (für die nächste Gruppe)“.
- **Modell:** Annahmen 1 bis 6 wie Kontrollseite · Bilanz $m c_p\,\mathrm{d}\vartheta/\mathrm{d}t = -kA(\vartheta - \vartheta_\mathrm{u})$ · Lösung $\vartheta(t) = \vartheta_\mathrm{u} + (\vartheta_0 - \vartheta_\mathrm{u})\,\mathrm{e}^{-kA\,t/(m c_p)}$ · Mischen $\vartheta_{1,0} = (C_\mathrm{K}\vartheta_\mathrm{K,0} + C_\mathrm{M}\vartheta_\mathrm{M})/(C_\mathrm{K} + C_\mathrm{M})$ · Wärme $Q = C(\vartheta_0 - \vartheta)$ · „So rechnet die Seite: dieselben Gleichungen wie das Blatt, Zeit in Sekunden. Prüfwerte: kA = 0,1994 W/K aus 72 °C nach 10 min (d1, vorläufig); Tasse 1 erreicht 60 °C nach 18,6 min (d2).“ · Grenzen: „Die Tasse speichert Wärme (im Versuch höhere Mischtemperatur, kleinerer Unterschied); kA ist nicht ganz konstant; ohne Deckel kommt Verdunstung dazu (Teil h). Die Seite zeigt Rechenwerte, keine Messwerte.“
- **Fuß:** „Stand …, Version … · Rechnung aus kaffee_modell.py · erstellt mit KI-Unterstützung, entschieden von der Tutoriumsleitung.“

## Anhang C: Prüfliste L2 D1 (geplant; Ergebnis nach dem Bau)

| Nr. | Kriterium (kurz) | geplant | wo |
|:--|:--|:--|:--|
| S1 | Zweck am Anfang | erfüllt | Zweck-Satz |
| S2 | Vorhersage mit Grund vor den Kurven | erfüllt | 01, Grund Pflicht (D5) |
| S3 | ersetzt nicht die Rechnung | erfüllt | Hinweis „nach Teil e“; Säulenzahlen erst nach 02 (D4); warme Milch nach g3 (D3) |
| S4 | Zusammenhang sichtbar (Bilanzraum, Wärmestrom, Säulen) | teilweise | Säulen und Bilanz im Modell; Skizze und Wärmestrom-Ansicht bewusst weg (G1) |
| S5 | Startwerte, Bereiche, Herkunft | erfüllt | Ausgangswerte mit „vorläufig“, Skalen mit Min und Max |
| S6 | Annahmen bei den Ergebnissen | erfüllt | Annahmenzeile |
| S7 | wofür das Modell taugt | erfüllt | Modell, Grenzen |
| S8 | Rechenweg offen, Prüfwert aus dem Blatt | erfüllt | Modell: d1, d2 |
| S9 | Vergleich mit Messwerten, nur er prüft das Modell | erfüllt | 03, Kernsatz |
| S10 | Modellvarianten nebeneinander | bewusst nicht | Becher und Voreinstellungen entfallen; Variation über Regler |
| S11 | Form passt zum Inhalt | erfüllt | Anhang A |
| S12 | Ablauf selbst steuern | erfüllt | keine Animation; „Werte des Blatts“, „Von vorn“ |
| S13 | offline, responsiv, barrierearm, zweisprachig | erfüllt | Tests |
| S14 | geteilte Messwerte ohne Personenbezug | erfüllt | kein Teilen; nur auf dem Gerät; Plausibilitätsprüfung |
| S15 | keine Punkte und Uhr, Schluss mit Grenzen | erfüllt | 05 |

## Anhang D: Quellen (selbst geöffnet am 08.11.2026)

- W3C: Web Content Accessibility Guidelines (WCAG) 2.2, Recommendation 12.12.2024, <https://www.w3.org/TR/WCAG22/>: 1.4.1, 1.4.3, 1.4.10, 1.4.11, 2.4.7, 2.4.11, 2.5.5 (44 × 44, AAA), 2.5.7, 2.5.8 (24 × 24, AA).
- W3C WAI: ARIA Authoring Practices Guide, Slider Pattern, <https://www.w3.org/WAI/ARIA/apg/patterns/slider/>: Pfeiltasten ein Schritt, Bild auf/ab größere Schritte, Pos1/Ende; `aria-valuetext` für Einheiten; Warnung zu Touch-Hilfsmitteln.
- Microsoft: Sliders (Windows apps), <https://learn.microsoft.com/en-us/windows/apps/design/controls/slider>: sofortige Rückmeldung, Bereich beschriften, Skalenmarken und Wertanzeige für genaue Werte; Zahlenfeld, wenn Tastatur bevorzugt wird.
- PatternFly: Slider, Design guidelines, <https://www.patternfly.org/components/slider/design-guidelines>: Wert immer sichtbar, Min und Max zeigen, Eingabefeld und Tasten für Schritte, Skalenmarken.
- Apple: Human Interface Guidelines, Accessibility, <https://developer.apple.com/design/human-interface-guidelines/accessibility>: Steuerelemente iOS 44 × 44 pt (Minimum 28 × 28 pt).
- Android Developers: Make apps more accessible, <https://developer.android.com/guide/topics/ui/accessibility/apps>: Touch-Ziele mindestens 48 × 48 dp.
- Mayer, R. E. (2024): The past, present, and future of the cognitive theory of multimedia learning. Educational Psychology Review 36, 8 (CC BY 4.0), Tabelle 6: Kohärenz d = 0,86; Signalisierung 0,69; Redundanz 0,10; räumliche Nähe 0,82; zeitliche Nähe 1,31; Segmentierung 0,67; Vortraining 0,78. Effektstärken aus Lehrbotschaften, nicht aus Simulationen.
- Europäische Union, data.europa.eu: Data visualisation guide, „Direct labelling“, <https://data.europa.eu/apps/data-visualisation-guide/direct-labelling>: Legende zwingt zum Hin- und Herschauen, Direktbeschriftung; Grenze bei eng liegenden Elementen.
- Moran, K. (2022): Clutter-Free: One of the 3 Cs for Better Charts. Nielsen Norman Group, <https://www.nngroup.com/articles/clutter-charts/>: Daten-Tinte nach Tufte; Achsen und Raster nur, wenn sie zum Ablesen gebraucht werden.
- Dossiers L1 (Tulodziecki, Herzig, Blömeke 2017) und L2 (Tulodziecki, Herzig, Grafe 2019) aus dem Startpaket; Kennungen und Seiten wie dort, nur in eigenen Worten.
