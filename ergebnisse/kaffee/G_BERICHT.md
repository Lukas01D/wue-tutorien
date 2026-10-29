# Bericht Prüfer G: Gestaltung

> Rolle: Kommunikationsdesignerin. Geprüft am 29.10.2026: Kaffee-Aufgabe und Lösung (PDF und Word), Abb. 1, L1, L2, verglichen mit den Original-Tutoriumsblättern 5 und 6, der Original-Lösung zu Tutorium 5 und der FVT-Aufgabenvorlage. Alle Word-Dateien mit LibreOffice gerendert, Schriften und Maße aus PDF und DOCX ausgelesen (Skripte `notizen/analyse_docx.py`, `notizen/pdf_schriften.py`). Websuchen: 5 von 5 verbraucht.
>
> **Einschränkung beim Rendern:** In dieser Umgebung fehlt das Paket `libreoffice-math`. Beim Umwandeln von Word nach PDF verschwinden deshalb **alle Word-Formeln (OMML)**, bei den Originalen wie beim Kaffee-Blatt (siehe `notizen/w_Kaffee_Aufgabe-2.png`). Formeln in den Word-Fassungen habe ich deshalb im XML geprüft, nicht im Bild.

## 1. Gesamturteil

Das Blatt ist inhaltlich gut gegliedert: Die Bausteine der Strukturvorlage (Ausgangssituation mit Skizze, Frage 1, Aufgabe 1 mit Annahmen, Tabelle und Teilen a bis h, Versuch) stehen in der richtigen Reihenfolge, und Abb. 1 zeigt die Situation klar, ohne die Lösung zu verraten. Das größte gestalterische Problem ist die **fehlende Hierarchie**: Im PDF sind Titel, Baustein-Überschriften und Fließtext alle 10,9 pt groß (Original-Tutoriumsblatt: 18/14/12 pt), Abbildungsunterschrift und nächste Überschrift kleben ohne Abstand aneinander, und PDF und Word weichen voneinander ab (Titel 10,9 pt gegen 14 pt). Praktisch hakt die **Versuchstabelle**: Sie hat keine Felder für die Werte, die der Versuch selbst verlangt (Start, 10 min, Milch, kA), und die Zeilen sind zum Schreiben zu niedrig. Das Blatt folgt bisher dem älteren Tutoriumslook ohne Logos; ich empfehle, den Rahmen der FVT-Vorlage zu übernehmen und die Tutoriums-Bausteine zu behalten, was sich mit `pandoc --reference-doc` fast ohne Mehraufwand bauen lässt (Probe in `notizen/probe_pandoc_referenzdoc_FVT.png`). Mit den Vorschlägen Gest1 bis Gest6 (überwiegend kleiner Aufwand) ist die Aufgabe gestalterisch einsatzbereit.

## 2. Änderungsvorschläge

**Gest1: Versuchstabelle zum Ausfüllen tauglich machen**
- Ebene: praktisch (Durchführung), gestalterisch
- Stelle: Aufgabe (und Wiederholung in der Lösung), „Versuch zu Aufgabe 1“, Tabelle am Ende
- Befund: Die Schritte 2, 3 und 5 verlangen Starttemperaturen aller Becher, ϑ(10 min) in Becher 2, daraus kA, und die Milchtemperaturen in Kühltasche und Glas. Die Tabelle hat aber nur „Vorhersage nach 60 min“ und „Messung nach 60 min“. Die Datenzeilen sind so hoch wie eine Textzeile (etwa 6 mm), ohne innere Linien; Zeile 2 bricht im Becher-Feld um, die Wertefelder bleiben trotzdem einzeilig (`notizen/zoom_versuch-3.png`). Handschriftliche Zahlen mit Komma passen knapp, Korrekturen gar nicht. Die Tabelle widerspricht damit den eigenen Arbeitsschritten.
- Vorschlag: Tabelle mit sechs Spalten, alle Temperaturen in °C:

  | Becher | Start ϑ(0) | ϑ(10 min) | Milch ϑ_M | Vorhersage ϑ(60 min) | Messung ϑ(60 min) |
  |---|---|---|---|---|---|
  | 1: Milch sofort | | (grau) | | | |
  | 2: Milch nach 60 min aus der Kühltasche | | | | | |
  | 3: Milch nach 60 min aus dem Glas | | (grau) | | | |

  Maße: Spaltenbreiten 4,6 / 2,1 / 2,3 / 2,0 / 2,4 / 2,4 cm (zusammen 15,8 cm); Kopfzeile 9 pt fett, zweizeilig (Wort oben, Symbol unten); Datenzeilen mindestens 10 mm hoch; alle Zellränder 0,5 pt in #808080, Linie unter der Kopfzeile 1 pt; nicht benötigte Felder mit #E6E6E6 hinterlegen. Darunter eine Zeile „kA aus Becher 2 (wie Teil f): ______ W/K“. Mock-up: `notizen/mockup_FVT_Versuchstabelle.png` (Skript `notizen/mockup/mockup_fvt.py`).
- Begründung: Ein Messblatt muss die Messgrößen in der Reihenfolge der Schritte abfragen; 10 mm Zeilenhöhe ist für Handschrift mit Ziffer, Komma und Nachkommastelle üblich. Die Spalte „Milch ϑ_M“ macht sichtbar, dass Becher 2 und 3 sich nur in der Milchtemperatur unterscheiden, was der Kern von Teil h (2) ist.
- Priorität: muss · Aufwand: klein
- Folgen: Versuchsabschnitt wird etwa 2 cm länger; passt auf Seite 3 (dort ist ein Viertel frei). Lösung: Hinweis „Versuch“ kann auf die Spalten verweisen. Keine Zahlen ändern sich.

**Gest2: Erscheinungsbild: Rahmen der FVT-Vorlage, Bausteine der Tutoriumsblätter**
- Ebene: gestalterisch
- Stelle: Aufgabe und Lösung, Kopf, Fuß, Seitenränder, Schrift, Farbe
- Befund (Vergleich, ausgelesen aus den DOCX):

  | Merkmal | Tutoriumsblatt 6 (Original) | Tutoriumsblatt 5 (Original) | Kaffee PDF | Kaffee Word | FVT-Vorlage |
  |---|---|---|---|---|---|
  | Ränder o/r/u/l | 2,5/2,5/2,0/2,5 cm | wie T6 | 2,6/2,5/2,5/2,5 cm | wie PDF | 3,75/1,83/2,22/2,37 cm |
  | Kopfzeile | Text, Cambria 9 pt, „Wärmeübertragung“ Mitte, Semester rechts, Linie | wie T6 | Carlito 10 pt, „Entwurf, Stand …“ | Calibri 9 pt | drei Grafiken (UPB, FVT, Dreiecke) |
  | Fußzeile | Seitenzahl rechts | wie T6 | Seitenzahl rechts | Seitenzahl | Fachname 8 pt fett links, Seitenzahl nur ab 2 Seiten |
  | Fließtext | Calibri 12 pt, 1,5-zeilig, 6 pt vor/nach | Cambria 11 pt | Carlito 10,9 pt | Calibri 11 pt, 1,3-zeilig | Segoe UI 10 pt, Blocksatz, 3 pt vor/nach |
  | Titel | Calibri 18 pt fett unterstrichen, zentriert | wie T6 | **10,9 pt** fett unterstrichen | **14 pt** | 20 pt fett, #0025AA, linksbündig |
  | Baustein-Überschriften | 14 pt fett unterstrichen | Aufgabe 13 pt Cambria | **10,9 pt** | 11 pt | Überschrift 1: 15 pt fett #0025AA, nummeriert |
  | Abb.-Unterschrift | „Abbildung 1:“ 10 pt, zentriert | | 10,9 pt, linksbündig | 10 pt | |

  Die beiden Originalblätter sind untereinander nicht einheitlich (T5 Cambria 11 pt, T6 Calibri 12 pt). Das Kaffee-Blatt folgt T6 im Aufbau, aber nicht in den Größen. Logos, Lehrstuhlfarbe und Fachname im Fuß fehlen.
- Vorschlag: **Variante A (empfohlen):** Blatt und Lösung übernehmen den **Rahmen** der FVT-Vorlage unverändert: Kopf mit den drei Grafiken, Ränder, Fußzeile „Wärmeübertragung, Tutorium 5“ (8 pt fett) mit Seitenzahl, Schrift Segoe UI, Titel in der Formatvorlage „Titel Inhaltsseiten“ (20 pt fett #0025AA). Die **Bausteine** bleiben wie in den Tutoriumsblättern und der Strukturvorlage, aber ohne Unterstreichung und ohne automatische Nummer: „Ausgangssituation“, „Frage 1“, „Aufgabe 1“, „Versuch zu Aufgabe 1“ als Überschrift 1 mit abgeschalteter Nummerierung (15 pt fett #0025AA; Zusatz wie „(neu)“ oder „(Vorab-Frage)“ in 11 pt normal). „Annahmen:“, „Gegebene Größen:“, „Aufgabenstellung:“ als fette Zeile im Fließtext. Fließtext 10 pt Blocksatz, Teile a) bis h) als eingerückte Liste wie in der Vorlage. Mock-up: `notizen/mockup_FVT_Seite1.png`. **Variante B (falls die übrigen sieben Tutorien im alten Look bleiben):** strikt Tutoriumsblatt 6: Titel 18 pt fett unterstrichen zentriert, Bausteine 14 pt fett unterstrichen, Fließtext 12 pt 1,5-zeilig, Ränder 2,5/2,5/2,0/2,5 cm, Kopf wie im Original. Für beide Varianten gilt Gest3.
- Begründung: Die FVT-Vorlage ist das offizielle Erscheinungsbild des Lehrstuhls; Logos und Fachname im Fuß weisen das Blatt als Lehrstuhlmaterial aus, wenn es als PDF weitergegeben wird. Die Bausteine der Strukturvorlage passen in die Hierarchie der Vorlage (Titel, Überschrift 1, Fließtext) ohne Umbau. Die automatische Nummerierung von Überschrift 1 („1. Teil 1“) würde mit „Frage 1“ und „Aufgabe 1“ doppelt zählen, deshalb aus. Der Titel steht in der Vorlage linksbündig; die Strukturvorlage verlangt „zentriert und fett“: **Vorgabe in Frage gestellt (nur die Ausrichtung des Kopfs)**, weil ein zentrierter blauer Titel unter drei Kopfgrafiken unruhig wirkt und die Vorlage alle Überschriften linksbündig setzt. Wer zentriert behalten will, ändert nur die Ausrichtung des Titels.
- Priorität: sollte · Aufwand: mittel (einmalig für alle acht Tutorien; je Blatt danach klein, siehe Gest8)
- Folgen: Satzspiegel 16,8 × 23,7 cm statt 16,0 × 24,6 cm; mit 10 pt Segoe UI bleibt der Umfang nach meiner Schätzung etwa gleich (drei Seiten Aufgabe). Abb. 1 auf 13,5 cm Breite. Die Entscheidung sollte für alle acht Tutorien gleich fallen (offene Frage 1).

**Gest3: Hierarchie und Abstände klären**
- Ebene: gestalterisch
- Stelle: Aufgabe und Lösung, alle Überschriften, Abbildungen, Ergebnisse
- Befund: Im PDF sind Titel, Überschriften und Text gleich groß (10,9 pt, ausgelesen mit pdfminer). „Abb. 1: Die beiden Tassen“ und „Frage 1“ stehen ohne Abstand untereinander (Seite 1), ebenso „Abb. L1“ und „a)“ (Lösung S. 4) sowie „Abb. L2“ und „f)“ (S. 6). Abb. L1 und L2 stehen linksbündig, die Unterschriften auch; in Tutoriumsblatt 6 sind Bild und Unterschrift zentriert. In der Lösung sind auf Seite 4 sieben Beschriftungen unterstrichen (Lösung, Frage 1, Aufgabe 1, Geg., Ges., Skizze, Annahmen, Ansatz); Unterstreichung trägt so keine Rangfolge mehr.
- Vorschlag: Drei Ebenen, sonst nichts:
  1. Titel (Variante A 20 pt blau; Variante B 18 pt fett unterstrichen), 0 pt davor, 12 pt danach.
  2. Baustein (Ausgangssituation, Frage n, Aufgabe n, Versuch; in der Lösung zusätzlich „Lösung“ und „Hinweise für die Tutoriumsleitung“, „Quellen der Arbeitswerte“): Variante A 15 pt, Variante B 14 pt; **18 pt Abstand davor, 6 pt danach**, „mit nächstem Absatz zusammenhalten“.
  3. Fettes Stichwort im Fließtext („Annahmen:“, „Gegebene Größen:“, „Aufgabenstellung:“, in der Lösung „Geg.:“, „Ges.:“, „Skizze:“, „Annahmen:“, „Ansatz:“ und „a)“ bis „h)“): fett, **nicht unterstrichen**, 6 pt davor.
  Abbildungen zentriert; Unterschrift zentriert, 9 bis 10 pt, „Abb. 1:“ fett, 4 pt davor und 12 pt danach. Ergebnisse am Ende der Teile mit 3 pt Abstand davor (optional rechtsbündig, damit sie nicht wie ein Teil des Fragetexts gelesen werden).
- Begründung: Leserinnen und Leser finden auf einen Blick die vier Bausteine nur, wenn diese sich in Größe oder Farbe vom Text abheben. Abstand davor größer als danach bindet die Überschrift an ihren Inhalt (Gesetz der Nähe). Unterstreichung nur auf einer Ebene, oder in Variante A gar nicht.
- Priorität: sollte · Aufwand: klein (vier Formatvorlagen)
- Folgen: Blatt wird etwa 1 bis 2 cm länger; Seitenumbrüche neu prüfen (Tabelle der gegebenen Größen bleibt geschlossen, das ist schon so).

**Gest4: Lösung von Anfang an als Lösung kenntlich machen**
- Ebene: praktisch, gestalterisch
- Stelle: Lösung, Seiten 1 bis 3 und Kopfzeile
- Befund: Die Seiten 1 bis 3 der Lösung sind **pixelgleich** mit dem Aufgabenblatt (Bildvergleich `notizen/aufgabe-n.png` gegen `loesung-n.png`). Erst Seite 4 zeigt „Lösung:“. Wer nur die ersten Seiten druckt oder auf dem Tablet blättert, kann Blatt und Lösung nicht unterscheiden; beim Austeilen aus einem Stapel droht eine Verwechslung. Die Original-Lösung hebt den Lösungstext grau (#808080) ab; das hat einen Kontrast von nur 3,95 : 1 zu Weiß (eigene Rechnung, unter dem üblichen Richtwert 4,5 : 1 für Text) und ist am Beamer schwach.
- Vorschlag: Kopfzeile rechts „Lösung“ statt Semester (oder „Sommersemester 20xx, Lösung“), Titel „Tutorium 5: Wärmebilanzen (instationär global), Lösung“; in Variante A zusätzlich die Fußzeile „Wärmeübertragung, Tutorium 5, Lösung“. „Lösung“ als Baustein-Überschrift (Gest3, Ebene 2) auf neuer Seite wie bisher. Lösungstext **schwarz lassen**, nicht grau wie im Original. Optional wie in der Original-Lösung die zentralen Gleichungen rechts nummerieren ((1) Mischbilanz, (2) Differentialgleichung, (3) Lösung T(t)), damit man im Tutorium „Gl. (3)“ sagen kann.
- Begründung: Kennzeichnung auf jeder Seite ist die einfachste Absicherung gegen Verwechslung. Gleichungsnummern sind in der Original-Lösung Standard (dort stehen alle Formeln in 32 Tabellen mit der Nummer rechts).
- Priorität: sollte · Aufwand: klein
- Folgen: Keine Zahlen; Querverweise in der Lösung können auf Gleichungsnummern umgestellt werden (optional).

**Gest5: Tabelle der gegebenen Größen straffen**
- Ebene: gestalterisch
- Stelle: Aufgabe, „Gegebene Größen“
- Befund: Die Bezeichnungsspalte ist 2,95 cm breit; „Spez. Wärmekapazität:“ braucht in Carlito 11 pt 3,6 cm (gemessen) und bricht in allen drei Gruppen um, „Temperatur bei t = 0:“ und „Temperatur nach 10 min:“ ebenfalls. Die Gruppen sind durch leere Zeilen getrennt (Tabelle knapp 12 cm hoch, gemessen am Seitenbild). Nur die erste Gruppe („Kaffee/Milch“) hat eine Linie darunter, die anderen nicht; in Word ist die Zeile „Kaffee/Milch“ als Wiederholungszeile markiert und würde bei einem Seitenumbruch fälschlich oben wiederholt. Die Werte (Formeln 12,1 pt) sind größer als die Bezeichnungen (10,9 pt). Teil f und g brauchen „Becher“ und „Milchschaum“, das sieht man der Tabelle nicht an.
- Vorschlag: Spalten 3,9 / 4,1 / 3,9 / 4,1 cm (16,0 cm), Bezeichnungen ohne Doppelpunkt, kürzer: „Anfangstemperatur“ statt „Temperatur bei t = 0“, Gruppe „Messung in Tasse 2“ mit Zeile „nach 10 min“. Gruppenköpfe fett (Variante A in #0025AA), mit einer 0,5-pt-Linie darüber statt einer Leerzeile, Zeilen 1 pt Abstand vor und nach. Gruppenköpfe „Becher (ab Teil f)“ und „Milchschaum (Teil g)“. In Word die Wiederholungszeile abschalten. Formeln auf Textgröße (Gest6). Mock-up: `notizen/mockup_FVT_Seite1.png` (Tabelle dort etwa 5 cm hoch).
- Begründung: Eine Zeile je Größe liest sich schneller; die Strukturvorlage verlangt „je Zeile Bezeichnung: Symbol = Wert“. Der Verweis auf den Teil hilft, die Zusatzdaten nicht schon in a) bis e) zu suchen.
- Priorität: sollte · Aufwand: klein
- Folgen: Etwa 3 bis 4 cm Platzgewinn (geschätzt); kleine Textänderung in zwei Bezeichnungen (sprachlich, von der TL zu bestätigen).

**Gest6: Formelgröße und PDF/Word angleichen**
- Ebene: technisch, gestalterisch
- Stelle: Aufgabe und Lösung, Bausystem
- Befund: Im PDF ist der Text Carlito 10,9 pt, die Formeln aber Latin Modern 12,1 pt (pdfminer); Inline-Formeln wirken dadurch größer und dünner als der Text (sichtbar in `notizen/zoom_tabelle-2.png`). PDF und Word unterscheiden sich: Titel 10,9 pt gegen 14 pt, Kopfzeile 10 pt gegen 9 pt, Listenabstände. Im Blocksatz werden Inline-Formeln gesperrt („t = 0:“ im Versuch, „ϑ₂ = 32,10 °C“ und „τ ≈ 41 min“ in der Lösung S. 8 und 9).
- Vorschlag: In der LaTeX-Vorlage Grundgröße und Formelschrift gleich setzen (z. B. `\setmathfont{Latin Modern Math}[Scale=MatchLowercase]` oder Grundschrift ohne Skalierung auf 11 pt bzw. 10 pt in Variante A); Inline-Formeln nicht dehnen (`\mathsurround` bzw. Gleichheitszeichen in Inline-Formeln mit festem Abstand, notfalls diese Absätze linksbündig). Titel, Überschriften und Kopf in PDF und Word aus denselben Maßen (Tabelle in Gest2/Gest3) erzeugen.
- Begründung: In den Originalen (Word, Cambria Math) haben Formeln die Textgröße. Zwei Fassungen desselben Blatts dürfen nicht unterschiedlich aussehen, sonst ist unklar, welche gilt.
- Priorität: sollte · Aufwand: klein
- Folgen: Keine Zahlen; Umbruch kann sich leicht verschieben.

**Gest7: Abb. L2 für Schwarzweiß, Beamer und den Schnittpunkt verbessern**
- Ebene: gestalterisch, didaktisch
- Stelle: Lösung, Abb. L2
- Befund: Beide Kurven sind durchgezogen und nur durch Helligkeit unterschieden (Hellbraun #c49a6c gegen Dunkelbraun #8b5a2b, Kontrast untereinander 2,28 : 1, Hellbraun zu Weiß 2,57 : 1; Graustufen in `notizen/grau_AbbL2.png`). Die Hellbraun-Kurve ist am Beamer blass. Der Mischsprung von Tasse 2 bei 60 min (33,86 °C auf 30,19 °C) ist nur ein winziger Strich hinter dem Punkt; bei t = 0 ist der Sprung von Tasse 1 dagegen gepunktet sichtbar. Der Text verweist auf den Schnittpunkt „bis etwa 56 min (Abb. L2)“, doch ab 40 min liegen die Kurven weniger als 1,1 K auseinander (nachgerechnet: 42,59 gegen 41,52 °C bei 40 min; Schnitt bei 55,7 min) und sind im Bild nicht zu trennen. Achsenbeschriftung „Zeit t in min“: t steht aufrecht, in Abb. 1 kursiv.
- Vorschlag: Tasse 1 durchgezogen in #8b5a2b, Tasse 2 gestrichelt (Strich 6 pt, Lücke 3 pt) in #222222, beide 1,6 pt; Sprünge bei 0 und 60 min gepunktet in der Farbe der jeweiligen Tasse, mit kleinem Text „Milch“. Beschriftung direkt an den Kurvenenden statt Legende. Schnittpunkt bei 55,7 min mit offenem Kreis markieren und ein Ausschnittfenster 40 bis 60 min (ϑ 33 bis 43 °C) oben rechts einsetzen, oder als zweites Feld die Differenz ϑ_K − ϑ_1 über t zeigen. Symbole kursiv: „Zeit *t* in min“, „Temperatur *ϑ* in °C“.
- Begründung: Linienstil statt Farbton trägt im Schwarzweißdruck; für Grafikelemente gilt als Richtwert ein Kontrast von 3 : 1 zum Hintergrund (WCAG 2.1, Kriterium 1.4.11, aus dem Gedächtnis). Eine Abbildung, auf die der Text verweist, muss die genannte Stelle zeigen.
- Priorität: sollte · Aufwand: klein (Plotskript)
- Folgen: Nur Abb. L2; keine Zahlen ändern sich.

**Gest8: Bauweg: Word direkt aus der FVT-Vorlage, Ersatzschrift für Segoe UI**
- Ebene: technisch
- Stelle: Bausystem für Aufgabe, Lösung und Sammlung
- Befund: Die Word-Fassungen kommen aus pandoc mit dessen Standardvorlage (englische Formatvorlagen „Body Text“, „Compact“, „First Paragraph“; Schrift fest Calibri statt Designschrift; leerer Kommentarteil). Sie sind trotzdem so bearbeitbar wie die Originale: Formeln als Word-Formeln (OMML, 42 im Blatt, 122 in der Lösung; die Originale nutzen ebenfalls OMML mit Cambria Math), Abbildungen als PNG mit 300 dpi, Auszeichnungen direkt formatiert wie in den Originalen. Segoe UI fehlt unter Linux; LibreOffice ersetzt sie hier durch Inter, die FVT-PDF wurde mit Noto Sans gebaut. Ohne `libreoffice-math` gehen beim Weg Word nach PDF alle Formeln verloren (siehe Einschränkung oben).
- Vorschlag: (1) Eine Kopie von `Vorlage_Aufgabenstellungen_FVT.docx` als `--reference-doc` für pandoc nutzen; darin einmalig die Fußzeile auf „Wärmeübertragung, Tutorium N“ ändern und die pandoc-Formatvorlagen an die FVT-Vorlagen angleichen („Body Text“, „First Paragraph“, „Compact“ wie „Fließtext“; „Title“ wie „Titel Inhaltsseiten“; „Heading 1“ ohne Nummerierung; „Image Caption“ 9 pt zentriert). Probe: pandoc übernimmt Kopf mit allen drei Grafiken, Fuß, Ränder und Designschrift ohne weiteres Zutun (`notizen/probe_pandoc_referenzdoc_FVT.png`). (2) In der Word-Datei bleibt „Segoe UI“ als Schriftname stehen, damit sie am Lehrstuhl richtig erscheint. (3) Für das PDF im Linux-Bausystem **Noto Sans** (OFL, mit griechischen Zeichen; im Paket `fonts-noto-core`) als Ersatz, so wie schon in der FVT-PDF; **Selawik** (Microsofts freie Ersatzschrift für Segoe UI, OFL) nur, wenn gleiche Laufweite wichtiger ist, denn sie deckt laut Microsoft nur lateinische Zeichensätze ab und hat noch nicht das Kerning von Segoe UI. (4) PDF weiter über LaTeX bauen (bessere Formeln); Kopf dort mit `fancyhdr` und den drei Grafiken nachbauen: UPB- und FVT-Logo liegen als JPG vor, die Dreiecksgrafik nur als EMF in der Vorlage (`word/media/image3.emf`), einmalig mit LibreOffice nach PDF wandeln und zuschneiden. Wer Word nach PDF wandelt, muss vorher `libreoffice-math` installieren.
- Begründung: Quellen geöffnet: Selawik bei Microsoft Learn (<https://learn.microsoft.com/en-gb/typography/font-list/selawik>: „open source replacement for Segoe UI“, OFL 1.1, Codepages 1252/1250/1254/1257, kein Griechisch), GitHub (<https://github.com/microsoft/Selawik>: bekanntes Problem „missing kerning to match Segoe UI“); pandoc-Handbuch (<https://pandoc.org/MANUAL.html>, Option `--reference-doc`: Formatvorlagen und Dokumenteigenschaften „including margins, page size, header, and footer“ werden übernommen). Griechisch in Noto Sans: aus dem Gedächtnis, nicht nachgeschlagen.
- Priorität: sollte · Aufwand: mittel (einmalig), danach klein
- Folgen: Gilt für alle Blätter der Sammlung; Word-Fassung wird zur „echten“ Lehrstuhl-Datei, die man mit den Formatvorlagen der Vorlage weiterbearbeiten kann.

**Gest9: Abb. 1 und Abb. L1 vereinheitlichen und etwas Platz zum Einzeichnen**
- Ebene: gestalterisch
- Stelle: Aufgabe Abb. 1, Lösung Abb. L1
- Befund: Abb. 1 ist klar, ruhig und verrät nichts (gleiche Pfeile Q̇_ab, Füllhöhen stimmen: Tasse 1 mit Milch höher als der schwarze Kaffee in Tasse 2). Kleinigkeiten: „Umgebung: ϑ_u“ (Abb. 1) gegen „Umgebung T_u“ (L1, ohne Doppelpunkt); beschreibende Indizes „ab“, „K“, „u“ kursiv statt aufrecht; in „ϑ1, 0“ steht ein Leerraum nach dem Komma, im Text nicht. Teil b) verlangt, den Bilanzraum in Abb. 1 einzuzeichnen; die Tassen sind gedruckt nur 1,5 × 1,65 cm groß (gemessen am PNG). Abb. L1 hat oben und unten viel Leerraum und steht linksbündig. In Graustufen funktionieren beide (Rot #b03a2e wird mittelgrau, die Brauntöne bleiben unterscheidbar; `notizen/grau_Abb1.png`).
- Vorschlag: Beschriftung einheitlich mit Doppelpunkt; Indizes aufrecht (`\mathrm{ab}`, `\mathrm{u}`, `\mathrm{K}`), Komma ohne Leerraum (`1{,}0`); Tassen in Abb. 1 um etwa 20 % größer (Breite 1,8 cm) bei gleicher Gesamtbreite, oder in b) „in Abb. 1 (Tasse 1 bei t = 0)“ präzisieren. Abb. L1 auf den Inhalt zuschneiden (Rand 2 mm) und zentrieren.
- Begründung: Einheitliche Bildsprache zwischen Blatt und Lösung; aufrechte beschreibende Indizes nach DIN 1338 bzw. ISO 80000-2 (aus dem Gedächtnis). Dieselbe Regel sollte dann auch im Text gelten (Hinweis an Rolle S/R).
- Priorität: kann · Aufwand: klein
- Folgen: Nur Abbildungen; im Text ggf. dieselbe Indexschreibweise.

**Gest10: Kopfzeile für die Endfassung und Versuch auf eigener Seite**
- Ebene: praktisch
- Stelle: Aufgabe, Kopfzeile und Seitenumbruch
- Befund: Kopf rechts „Entwurf, Stand 23.10.2026“; die Originale tragen dort das Semester. Seite 1 endet nach den Annahmen mit gut 2 cm Leerraum (die Tabelle rückt geschlossen auf Seite 2, das ist richtig); Seite 3 ist zu einem Viertel leer. Platz für Notizen gibt es nicht; im Tutorium wird ohnehin auf eigenem Papier gerechnet.
- Vorschlag: Endfassung mit Semester („Sommersemester 2027“ o. ä.) statt Entwurfsstand. Den Versuch mit Gest1-Tabelle oben auf Seite 3 beginnen lassen (Seitenumbruch davor), damit Seite 3 als Messblatt einzeln kopiert und am Versuchstisch liegen kann; der Rest von Seite 3 bleibt als Notizfläche.
- Begründung: Ein separates Messblatt ist im Tutorium praktischer als Blättern; das Semester im Kopf ordnet ausgedruckte Blätter zu.
- Priorität: kann · Aufwand: klein
- Folgen: Keine.

## 3. Was bleiben sollte

- Der Aufbau nach der Strukturvorlage und die Reihenfolge Ausgangssituation, Frage 1, Aufgabe 1, Versuch; die Lösung wiederholt die Aufgabe und beginnt auf neuer Seite.
- Abb. 1 als Zeitstrahl mit zwei Zeilen: sofort verständlich, ohne Lösungshinweis, im Schwarzweißdruck lesbar; zurückhaltende Palette (Braun für Kaffee, Rot nur für Wärmeströme, Blau nur für den Bilanzraum in L1). Schrift der Abbildungen (Lato) passt zu Carlito, das aus Lato abgeleitet ist.
- Abbildungen mit 300 dpi und als SVG vorhanden; Tabelle der gegebenen Größen, Abbildung und Unterschrift bleiben beim Umbruch zusammen (in Word über „mit nächstem Absatz zusammenhalten“ gesichert).
- Word-Formeln als OMML: so bearbeitbar wie die Originale.
- Ergebnis am Ende jedes rechnenden Teils, ohne Label; „Hinweise für die Tutoriumsleitung“ und „Quellen“ am Ende der Lösung, Blatt bleibt schlank.
- Tablet: einspaltiges A4 mit eingebetteten Schriften und Textebene, gut lesbar.

## 4. Offene Fragen an die Tutoriumsleitung

1. Sollen alle acht neu gestalteten Tutorien den FVT-Rahmen bekommen (Variante A), oder bleibt der bisherige Tutoriumslook (Variante B)? Ein einzelnes Blatt im neuen Look neben sieben alten wäre uneinheitlich.
2. Ist die FVT-Vorlage für Tutorien freigegeben, oder nur für Übungen? Gibt es eine Fassung mit Fußzeile „Wärmeübertragung“ am Lehrstuhl?
3. Titel linksbündig wie in der Vorlage oder zentriert wie in der Strukturvorlage?
4. Wird der Versuch tatsächlich mit Arbeitsblatt durchgeführt (dann Gest1 und Gest10), oder nur von der TL vorne gemessen (dann reicht eine Tabelle für den Beamer)?
5. Welches Semester steht in der Endfassung im Kopf?
