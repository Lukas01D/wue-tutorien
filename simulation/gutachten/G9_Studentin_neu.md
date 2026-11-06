# Gutachten G9: neue Studentin (Handy, zu zweit)

| | |
|:--|:--|
| Rolle | G9 „neue Studentin“, 3. Semester Maschinenbau, hat die Kaffee-Aufgabe gerechnet, öffnet die Seite zum ersten Mal |
| Datum | 06.11.2026 |
| Runde | 2 |
| Art | getrennte Rollenprüfung desselben Modells (eine unabhängige Prüfung mit einem anderen Modell folgt) |
| Gegenstand | `simulation/site/index.html`, SHA-256 `ea6d3ad224030ff9a783517b7c6af059c8bba48600c80c83819c41db85ea9c31` (mit `sha256sum` geprüft, 394 754 Byte), Fuß der Seite: „Stand 2026-11-05 · Version 47d14331af“ |
| Umgebung | Playwright 1.63.0, Chromium 153.0.8010.12 (`chromium.launch()` ohne Optionen), Node 22.23.4; Kontext `viewport 390 × 844`, `isMobile`, `hasTouch`, `locale de-DE`; Seite als `file:`; Bedienung mit `tap`, `fill`, `type`. Keine echte Bildschirmtastatur (Emulation), kein echtes Gerät, kein Bildschirmleser. |
| Grundlage | `simulation/KONZEPT.md` (Abschnitte 2, 3, 4.1, 5, 6, 12), Aufgabenblatt `ergebnisse/kaffee/fertig/Kaffee_Aufgabe_Tutorium5_2026-10-31.pdf` |
| Skripte, Bilder | `/tmp/claude-0/-home-user/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/r2_G9/` (s1.js bis s22.js, Bilder 01 bis 29) |

## Ablaufbericht

Zeiten sind eine **Expertenschätzung** für ein Paar an einem Handy, nicht gemessen.

| Schritt | Was wir tun und sehen | Schätzung |
|:--|:--|--:|
| 0 Öffnen | Kopf, Karte „Erst vorhersagen“ ganz oben, darunter leere Achsen mit Raumlinie und Startpunkt 80 °C. Klar, was zu tun ist. | 0,5 min |
| 1 Start: Vorhersage | Jede notiert für sich, wir einigen uns. Erst falsch probiert: „Tasse 2 (Milch später)“, Unterschied „4 K“. Die Eingabe „4 K“ wird angenommen („etwa 4 K“), ebenso „4,5“ und „ca. 4“; „vier“ und „-4“ sperren den Knopf mit „Bitte nur eine Zahl, zum Beispiel 4 oder 3,5.“ Ohne Auswahl bleibt der Knopf grau („Wähle zuerst eine Vorhersage.“). | 1,5 min |
| 2 Start: aufdecken und erklären | Nach „Vorhersage festhalten und Kurven zeigen“ springt der Fokus auf **Frage 1**; die Startkarte schrumpft zu „Start: Eure Vorhersage … Erklärt den Unterschied mit *Q*₁ und *Q*₂. [Auflösung zeigen]“. Diagramm mit 34,05 / 30,19 / 3,85 K ist oben angeheftet. Unsere falsche Vorhersage steht in einem **grünen** Kasten unter dem Regler, im Diagramm gibt es keine Marke dafür. Erst „Auflösung zeigen“ sagt „× Auswahl passt nicht“. Die Säulen *Q*₁ = 34,88 kJ, *Q*₂ = 38,57 kJ suchen wir: sie liegen etwa 1000 px tiefer, unter Regler, Legendentext, „Werte als Tabelle“ und zwei Knöpfen. **Hier hängen wir kurz** (G9-02, G9-03, G9-04). | 2,5 min |
| 3 Frage 1: Vorhersage | Text klar. „ca. 30 min“ wird angenommen. Ob Tasse 1 bei 60 min oder direkt nach der Zugabe verglichen wird, steht nur in der „?“-Hilfe (G9-08). Vorhersage 30 min wird als grüne Marke mit senkrechter Linie im Diagramm gezeigt, „Schnitt“ erscheint jetzt beschriftet. | 1 min |
| 4 Frage 1: prüfen | Regler mit Minus, Plus und Zahlenfeld liegt direkt unter der Karte und bleibt mit dem angehefteten Diagramm (376 px, 44,5 % der Höhe) gleichzeitig sichtbar. Δ steigt bis 3,86 K (53 bis 59 min) und fällt danach (3,50 K bei 90, 2,35 K bei 180 min); „Schnitt der Kurven nach 55,7 min“. Auflösung: „Eure Zahl: 30 min · Modell: etwa 56 min“, Erklärung mit Grenzwert 1,91 K. Gut. | 2 min |
| 5 Frage 2: Messwerte eintragen | „Noch keine Kurswerte“; ohne Link tippen wir unsere erfundene Messreihe ein (Tabelle unten). 18 Felder mit Dezimaltastatur, Komma und Punkt gehen; „5x“ wird sofort mit Feldnamen und Beispiel abgelehnt. Vor der Vorhersage erscheinen die Punkte **nicht** im Diagramm (gut). | 3 min (mit Link der TL etwa 0,5 min) |
| 6 Frage 2: Vorhersage und prüfen | „über den Kurven“, Begründung „Becher speichert Wärme“. Festhalten übernimmt die Einstellungen selbst (*kA* aus 0 und 10 min = 0,3278 W/K, Becher an, Raum 21,5 °C). Punkte und Kurven sind zu sehen; bei 60 min liegen zwei Quadrate, zwei Ringe und ein Kreis auf etwa 15 px (G9-09). „Werte als Tabelle“ zeigt Modell und Messung nebeneinander, damit können wir es beschreiben: Becher 1 erst unter, ab 40 min über der Kurve, Becher 2 ab 20 min über der Kurve. Auflösung offen formuliert, passt. „Geschafft. Weiter geht es in der Vertiefung.“ | 2 min |
| **Summe Pflichtweg** | mit Link der TL | **etwa 9,5 min** |
| | mit selbst eingetippten Messwerten | **etwa 12 min** |
| 7 Vertiefung V1 (kurz) | „Vertiefung öffnen“, Frage Milchtemperatur, Vorhersage 40 °C. **Erster Tipp auf „Vorhersage festhalten, dann prüfen“ tut nichts**, erst der zweite wirkt (G9-01). Danach Standardwerte gesetzt, Milchregler gefunden: 47 °C ergibt 0,00 K und *Q*₂ − *Q*₁ = 0,00 kJ; Auflösung „Modell: 47,0 °C“. Unsere Kurs-Messpunkte bleiben dabei im Diagramm, passen aber nicht zu den Standardwerten (G9-05). | 3 min |

**Unsere erfundene Messreihe** (vorgewärmte Keramikbecher, offen; Raum 21,5 °C, Milch 6 °C; teils mit Punkt eingegeben):

| *t* [min] | 0 | 10 | 20 | 30 | 40 | 50 | 60 vor | 60 nach |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| Becher 1 [°C] | 71,2 | 63.9 | 58,1 | 53,0 | 48,9 | 45,4 | 42,5 | (gesperrt) |
| Becher 2 [°C] | 80,3 | 70,6 | 63,2 | 57,4 | 52,5 | 48,6 | 45,3 | 41,4 |

**Nachgerechnet** (Hand, Werte der Seite stimmen): Standard: ϑ₁,₀ = 70,47 °C, *kA* = 0,3402 W/K, ϑ₁ = 34,05 °C, ϑ₂ = 30,19 °C (schwarz 33,86 °C), Δ = 3,85 K, (*m c*)gesamt = 957,7 J/K, 3,69 kJ / 957,7 J/K = 3,85 K, Schnitt 55,7 min, Grenzwert 20 − 18,09 = 1,91 K, V1 ≈ 47,0 °C. Kurswerte: *kA* = 1091 J/K · ln(58,8/49,1) / 600 s = 0,3278 W/K, ϑ₁,₀ = 72,84 °C, ϑ₁(60) = 40,90 °C, ϑ₂ = 41,43 → 37,88 °C, Modellwerte der Tabelle bei 10 bis 50 min (65,15; 58,62; 53,06; 48,34; 44,32 °C).

**Verrät die Seite vor der eigenen Vorhersage etwas?** Nein (CONFIRMED). Geprüft: sichtbarer Text, gesamter DOM-Text ohne Skripte (keine Zahl 34,0/30,1/3,8x/3,69/34,88/38,57/70,4/0,34, kein „Schnittpunkt“), Diagramm (nur Achsen, Raumlinie, 80 °C), „Werte als Tabelle“ und Rechenwerte („erscheint nach eurer Vorhersage“), Säulen, `aria-live` (leer bzw. „Erst die Startfrage beantworten.“), Reiter „Modell“ und „So rechnet der Code“ (gesperrt bis auf „Physikalisches Problem“), Fragenliste (alle „nach der Startfrage verfügbar“), „?“-Hilfe, Knöpfe „Standardwerte“ und „Wie im Versuch“ (zeigen nur eine Info), englische Fassung `?lang=en`. „ohne Vorhersage aufdecken“ fragt erst nach. Einziger Hinweis: Im Reiter „Modell“ steht „umso mehr, je wärmer der Inhalt als der Raum ist“; das ist das gegebene Gesetz der Aufgabe, keine Lösung. Nach der Startfrage zeigen die Kurven den Schnitt bei etwa 56 min schon vor der Vorhersage zu Frage 1 (unbeschriftet, liegt in der Sache).

## Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G9-01 | medium | Erster Tipp auf „Vorhersage festhalten, dann prüfen“ geht verloren, wenn das Zahlenfeld noch den Fokus hat und der Knopf weit unten steht: Beim Verlassen des Feldes wird das Diagramm wieder angeheftet, der Knopf rutscht um 45 px nach unten, der Tipp trifft daneben. Man denkt, es klemmt, und tippt nochmal. | s16.js (V1, nach Pflichtweg): `fill` → 1. Tipp ohne Wirkung, 2. Tipp wirkt; mit vorherigem `blur` wirkt der 1. Tipp. s17.js: Knopf y = 767 px bei Fokus (Diagramm `position: relative`), y = 813 px nach `blur` (`sticky`). Bei Start und Frage 1 trat es in meinen Läufen nicht auf (Knopf höher). | Beim Ab- und Anheften die Höhe des Diagramms als Platzhalter halten, oder das Wiederanheften erst nach dem Tipp (z. B. nach `click`) bzw. erst beim Scrollen ausführen. Am echten Gerät mit schließender Tastatur nachprüfen. | CONFIRMED (Emulation); Gerät INFERRED |
| G9-02 | high | Die Startvorhersage erscheint nach dem Festhalten **nicht als beschriftete Marke im Diagramm** (M-2). Frage 1, Frage 2 und V1 haben eine Marke, die Startfrage nur eine Textzeile unter dem Regler und in den Rechenwerten. Gerade beim Start fehlt so der direkte Vergleich „4 K, Tasse 2“ gegen 3,85 K, Tasse 1. | s5.js: SVG-Text nach Start enthält kein „Vorhersage“; Bild 04_nach_fest.png. Zum Vergleich Bild 07 (Frage 1, Marke „Eure Vorhersage: 30 min“). | Marke am rechten Rand bei 60 min, z. B. „Eure Vorhersage: Tasse 2 wärmer, 4 K“ als Kasten, mit Pfeil oder Klammer neben dem tatsächlichen Abstand. | CONFIRMED |
| G9-03 | medium | Eine **falsche** Vorhersage wird grün dargestellt (Kasten unter dem Regler; Marken der Fragen im Diagramm ebenfalls grün). Grün liest man als „richtig“. Ob die Vorhersage stimmt, steht erst nach „Auflösung zeigen“ („× Auswahl passt nicht“). | s5.js: Klasse `vorhersage-zeile`, Hintergrund rgb(232, 245, 239), Schrift rgb(20, 96, 63), Rand rgb(34, 123, 72); Bilder 04, 07, 15. | Neutrale Farbe für die eigene Vorhersage (Marine oder Grau); Grün und Kreuz nur im Abgleich nach der Auflösung. | CONFIRMED (Farbe); Wirkung INFERRED |
| G9-04 | medium | Nach dem Festhalten der Startfrage springt der Fokus auf Frage 1, die Startkarte wird klein. Der Erklärauftrag „Erklärt den Unterschied mit *Q*₁ und *Q*₂“ sagt nicht, wo *Q*₁ und *Q*₂ stehen, und fragt nicht „Stimmt eure Vorhersage?“ (Frage 1 und V1 tun das). Die Säulen liegen etwa 1000 px tiefer. Zu zweit sind wir fast gleich zu Frage 1 übergegangen. | s4.js: Fokus `frage-titel` „Zeitpunkt“; Bild 04_full_0/1 (Säulen unter Regler, Legendentext, „Werte als Tabelle“, zwei Knöpfen). | In der Startkarte nach dem Festhalten „Stimmt eure Vorhersage? Erklärt den Unterschied mit *Q*₁ und *Q*₂ (Säulen „Energie bis zur Zugabe“)“ mit Sprunglink zu den Säulen, oder die beiden Säulen klein in die Karte; Frage 1 erst nach „Weiter“. | CONFIRMED |
| G9-05 | low | In der Vertiefung (V1, Ausgangslage Standardwerte, Raum 20 °C) bleiben die Messpunkte des Kurses (Raum 21,5 °C, Becher) im Diagramm. Sie liegen dann deutlich über den Kurven, obwohl sie zu anderen Bedingungen gehören. | Bild 27_v1_regler.png. | Punkte blass zeigen mit Hinweis „Messpunkte gehören zu den Kurswerten“, oder nur bei übernommenen Kurswerten zeigen. | CONFIRMED |
| G9-06 | medium | Messblatt und Seite sagen „Becher 2 (Milch nach 60 min)“ und Zeilen bis 60 min; das Aufgabenblatt, das wir in der Hand haben, sagt „Becher 2 und 3 erst nach 40 Minuten“ und hat die Spalte ϑ(40 min). Wer mit dem Blatt misst, weiß nicht, welche Zeile gilt. | PDF S. 4 („Versuch zu Aufgabe 1“); Messblatt (Bild 01_full_1). KONZEPT Abschnitt 12, offener Punkt 3 nennt die Abweichung. | Blatt an den Versuch bis 60 min anpassen (eigener Auftrag laut KONZEPT), bis dahin ein Satz im Messblatt: „Neuer Ablauf: Milch nach 60 min (das Blatt sagt noch 40 min).“ | CONFIRMED |
| G9-07 | high | Reiterleiste hat **drei** Reiter („Versuche · Modell · So rechnet der Code“) statt neun (M-18), und der Fragen-Reiter heißt „Versuche“ statt „Auflösungen“ (E6). Als Studentin erwarte ich unter „Versuche“ den Becherversuch, nicht die Fragenliste. Für Studierende eher medium; nach dem Schema high, weil Muss. | s2.js: `role=tab` nur Versuche, Modell, So rechnet der Code; Bild 01_full_1/2. | Falls die TL das bewusst so entschieden hat, KONZEPT nachziehen; sonst neun Reiter (am Handy Akkordeon) und „Auflösungen“. Mindestens den Namen „Versuche“ ändern. | CONFIRMED (Abweichung); ob freigegeben INFERRED |
| G9-08 | low | Frage 1 sagt nicht, dass beide Tassen **direkt nach der Zugabe** verglichen werden; das steht nur in der „?“-Hilfe. Wer die Aufgabe kennt (Vergleich nach 60 min), kann denken, Tasse 1 werde weiter bei 60 min verglichen. Die Zeitachse endet je nach Regler bei *t*Z. | s20.js: Hilfe „Verglichen werden beide Tassen direkt danach.“; Fragetext in s6.js. | Fragetext ergänzen: „… ist der Unterschied direkt nach der Zugabe am größten?“ | INFERRED |
| G9-09 | low | Bei 60 min liegen Messpunkt Becher 1, zwei Messpunkte Becher 2 (vor und nach der Milch) und zwei Modellringe auf etwa 15 px; am Handy kaum zu unterscheiden, gerade dort, wo Frage 2 „Wo liegen die Punkte?“ fragt. | Bild 15_f2_nach_fest.png. | Punkt „60 nach der Milch“ leicht nach rechts versetzen oder als hohles Quadrat; Hinweis auf „Werte als Tabelle“ in der Frage 2. | CONFIRMED |
| G9-10 | low | Frage 2 sagt nach dem Festhalten weiter „Ladet die Messwerte … und übernehmt die Einstellungen“, obwohl das Festhalten sie schon übernommen hat; selbst eingetippte Werte heißen „Kurswerte geladen: 15 Messwerte“. | s8.js, Kartentext nach dem Festhalten. | Nach dem Festhalten nur „Beschreibt, wo die Punkte liegen …“ stehen lassen; „Messwerte eingetragen“ statt „geladen“, wenn getippt. | CONFIRMED |
| G9-11 | low | Die Ansage (`aria-live`) nach dem Festhalten ist bei allen Fragen derselbe Satz „Vorhersage festgehalten, Kurven und Rechenwerte sind sichtbar …“; die Ausgangslage der Frage (z. B. „Standardwerte gesetzt“, „Kurswerte übernommen“) wird nicht genannt (M-3: „setzt den Ausgangszustand und sagt das an“). | s6.js, s12.js, s19.js: `#ansage`. | Ansage je Frage: „Frage 1: Vorhersage 30 min festgehalten, Standardwerte gesetzt.“ | CONFIRMED |
| G9-12 | low | Hinweis bei Frage 1 (Minuten) lautet „Bitte nur eine Zahl, zum Beispiel 4 oder 3,5.“; „-4“ beim Start wird ohne Erklärung abgelehnt (gemeint: Tasse 2 um 4 K kälter). | s21.js. | Beispiel je Frage („zum Beispiel 45“); beim Start „Richtung oben wählen, hier nur den Betrag“. | CONFIRMED |
| G9-13 | low | Die grüne senkrechte Vorhersagelinie von Frage 1 läuft durch die Kurvenbeschriftungen „Tasse 2: Milch nach 56 min“ und „Tasse 1: Milch sofort“. | Bild 09_slider56.png. | Beschriftungen mit hellem Hintergrund oder Linie hinter die Schrift. | CONFIRMED |

**Zählung:** blocker 0, high 2 (G9-02, G9-07), medium 4 (G9-01, G9-03, G9-04, G9-06), low 7.

## Was gut funktioniert

- Startzustand verrät nichts (siehe oben), auch nicht in Tabelle, Ansage, Reitern und englischer Fassung; „ohne Vorhersage aufdecken“ fragt nach.
- Eingaben verzeihen: „4 K“, „ca. 4“, „4,5“, „63.9“; Unsinn wird mit Feldname und Beispiel abgelehnt, der Knopf bleibt grau, bis die Eingabe passt.
- Angeheftetes Diagramm (376 px, 44,5 %) mit drei Kernzahlen; Regler direkt darunter, Wirkung sofort sichtbar. Plus, Minus und Zahlenfeld sind 44 px hoch, Eingabefelder 16 px Schrift, Dezimaltastatur.
- Alle nachgerechneten Zahlen stimmen (Standard, Schnitt 55,7 min, Grenzwert 1,91 K, V1 47,0 °C, Kurswerte mit Becher).
- Messpunkte erscheinen erst nach der Vorhersage zu Frage 2; „Werte als Tabelle“ stellt Modell und Messung nebeneinander, damit lässt sich Frage 2 sauber beantworten.
- Auflösungen vergleichen die eigene Zahl mit dem Modell („Eure Zahl: 30 min · Modell: etwa 56 min“) und erklären knapp mit dem Wärmestrom.
- Frage 2 lässt sich sichtbar überspringen („Versuch ausgefallen“); der Link aus der Datei wird ehrlich erklärt („gilt nur auf diesem Rechner“).
- Stand bleibt beim Neuladen erhalten; „Für die nächste Gruppe zurücksetzen“ ist vorhanden.

## Nicht geprüft

Echte Bildschirmtastatur und Querformat, echtes iPhone oder Android, Bildschirmleser, Link mit Kurswerten von einer veröffentlichten Adresse, V2 bis V5, Ansichten „Wärmestrom“ und „ln“.
