# Konzept: Simulation „Kaffee mit Milch“ als eigene Website

> Stand 04.11.2026, Phase 1 nach `simulation/AUFTRAG_Simulation_Kaffee.md`, geschrieben von Claude (Cloud-Sitzung) für die Tutoriumsleitung (TL) und zur Prüfung durch Codex (Rolle X4). Entwurf: Die TL entscheidet über die Punkte in Abschnitt 12. Belege und Rechnungen liegen in `simulation/recherche/` (R1 Lernen mit Simulationen, R2 Gestaltung und Bedienbarkeit, R3 Fach und Modell, eigene Nachrechnung in `claude_nachrechnung/`). Skizzen in `simulation/skizzen/`.

PLATZHALTER_KURZFASSUNG

## 1 Ausgangslage

**Heutiges Werkzeug.** `Kaffee_Simulation.html` (Zweig `claude/kaffee-pruefung-sgvo1r`, `ergebnisse/kaffee/fertig/`, 30 KB, eine Datei, offline): Diagramm beider Tassen mit Schnittpunkt und Raumlinie, Kennzahlen, sechs Regler und zwei Schalter, fünf weitere Größen aufklappbar, Messwerte aus dem Versuch als Punkte (einzeln eingetragen, im Browser gespeichert), Übernahme in die Einstellungen, vier Fragen mit Vorhersage zu zweit (D114, D116, D124). Das Modell steht zwischen `MODELL-ANFANG` und `MODELL-ENDE` und entspricht `rechne()` und `zwei_tassen()` aus `kaffee_modell.py`; Codex hat es in X3 an 9338 Kurvenwerten bestätigt, die sechs Befunde sind behoben (D116).

**Was bleibt.** Das Modell, die Gültigkeitsprüfungen (ungültige Einstellung blendet Ergebnisse aus), die geprüfte Übernahme der Messwerte (ungerundet oder gar nicht), die Zahleneingabe mit Komma und Punkt, die Fragen mit Vorhersage zu zweit und die Testskripte (`test_simulation.py`, `browsertest.js`) als Grundlage der neuen Tests.

**Was fehlt oder stört** (eigene Sichtung und X3):

1. Die Seite ist eine lange Spalte; am Handy liegen Regler und Fragen weit unter dem Diagramm, man sieht die Wirkung eines Reglers nicht (X3: „Die mobile Bedienung benötigt zusätzliche Scrollwege“).
2. Frage 4 ist ohne eigene Messwerte nicht lösbar (X3), und Messwerte einzeln einzutippen kostet in 10 bis 15 Minuten zu viel Zeit, erst recht beim neuen Versuch mit Messung alle 10 Minuten.
3. Die Energie (Teil e, Kern des Denkfehlers „Die Energie bleibt ja erhalten“) erscheint nur als zwei Zahlen.
4. Die Seite verrät die Antwort auf die Vorab-Frage, sobald sie geöffnet ist.
5. Die Vorhersagen werden nur auf Papier notiert; das Werkzeug zeigt sie nicht neben dem Ergebnis.
6. Aussehen und Ablauf weichen von den Simulationsseiten des Lernzentrums ab.

**Vorbild Lernzentrum** (öffentliche Werkstatt-Seite <https://waermeuebertragung-werkstatt.qarri196.chatgpt.site>, am 04.11.2026 bei 1366 und 390 px angesehen): Schrift Fira Sans; Farben Marine `#102d49` und `#173d5e`, Überschriften `#39718e`, Text `#142337`, Nebentext `#5a6b7f`, Linien `#d8e1ea`, Flächen `#eef5fb`; Ecken 4 px. Über der Simulation Umschaltknöpfe („Stationär · Instationär · Instationär in 2D“), darunter Bild links (bis 780 px) und Knöpfe rechts („Python starten & berechnen“, „Parameter zurücksetzen“), Regler mit Zahlenfeld und Fragezeichen-Hilfe in drei Spalten, Kasten „Rechenwerte“ rechts daneben, dann die Reiterleiste mit neun Reitern. „Probier aus“ ist eine Tabelle (Versuch · Stell dir vor … · Was vermutest du?), die Auflösung steht unter „Versuche“ und „erscheint erst, wenn du sie aufklappst“. Ab dem zweiten Lauf erscheint der vorige Lauf gestrichelt. Am Handy steht das Bild oben, ist aber ein verkleinertes Rasterbild mit sehr kleiner Schrift; Knöpfe und Rechenwerte folgen darunter, die Regler erst nach einer Bildschirmhöhe. Das Lernzentrum duzt; Blatt und heutiges Werkzeug siezen.

## 2 Lernziele der Simulation

Passend zu Tutorium 5 (instationäre globale Bilanz) und zu Lernziel 2 der Variante B (D120). Ein Verb je Ziel.

Nach der Simulation können Sie …

1. erklären, warum Tasse 1 trotz Energieerhaltung wärmer ist, mit der Wärme, die beide Tassen bis zur Zugabe abgeben ($Q_2 - Q_1 = (m_\mathrm{K} c_{p,\mathrm{K}} + m_\mathrm{M} c_{p,\mathrm{M}})(\vartheta_1 - \vartheta_2)$, Teil e).
2. die Wirkung von Zeitpunkt der Zugabe, Milchtemperatur und Deckel auf den Unterschied der Tassen mit dem Wärmestrom $\dot{Q}_\mathrm{ab} = kA\,(\vartheta - \vartheta_\mathrm{u})$ begründen.
3. Abweichungen zwischen Ihren Messwerten und dem Modell mit den Annahmen des Modells begründen (wie Lernziel 2 der Variante B).

Vertiefung für Schnelle und zum Selbstlernen: $kA$ aus einer ganzen Messreihe bestimmen (Ausgleichsgerade von $\ln\frac{\vartheta - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$ über $t$).

## 3 Ablauf in der Sitzung

Minute 75 bis 90 nach dem Zeitplan der Hinweise (D110), zu zweit, ein Gerät je Paar (Handy oder Laptop). Die Studierenden haben a bis e gerechnet und den Versuch bis 40 min gemessen.

| Minute | Studierende (zu zweit) | Tutoriumsleitung |
|:--|:--|:--|
| 75 | Seite über den QR-Code öffnen; Startkarte: Vorhersage antippen (geht schnell, das Ergebnis kennen sie aus d) | QR-Code und Link zeigen; Messwerte des Kurses als Link bereitstellen (Abschnitt 9.4) |
| 76 bis 79 | Frage 1 (Zeitpunkt): Vorhersage notieren und im Feld festhalten, prüfen | Vorhersagen abfragen (Handzeichen), ein Paar mit abweichender Vorhersage begründen lassen (wie D124) |
| 79 bis 82 | Frage 2 (Milchtemperatur) | wie oben |
| 82 bis 85 | Frage 3 (Deckel) | wie oben |
| 85 bis 89 | Frage 4 (Versuch): Messwerte des Kurses laden, Lage der Punkte erklären | zwei Paare erklären lassen; an die Annahmen erinnern |
| 89 bis 90 | Zusammenfassung | Kernsatz: „Wer heißer ist, gibt mehr Wärme ab; deshalb Milch sofort“ |
| für Schnelle | Zusatzfragen (Becher, Abkühlen nach der Zugabe), Ansicht „ln“ | |

Zeitbedarf: Startkarte 1 min, Fragen 1 bis 3 je etwa 3 min, Frage 4 etwa 4 min, zusammen 14 min. Das ist eine Schätzung; X3 hat ausdrücklich keine Lernzeit gemessen. Beim ersten Einsatz die Zeit je Frage messen (offener Punkt im Protokoll, D114).

**Außerhalb der Sitzung** (Selbstlernen, Nachbereitung): Dieselbe Seite funktioniert allein; die Startkarte sichert die Vorhersage vor dem Aufdecken, die Auflösungen erscheinen erst nach dem Festhalten einer Vorhersage.

PLATZHALTER_ANFORDERUNGEN

## 5 Seitenaufbau

### 5.1 Laptop (ab 1024 px, Abnahme bei 1366 px)

![Skizze Laptop](skizzen/skizze_laptop_1366.png)

Von oben nach unten, wie die Simulationsseiten des Lernzentrums, ohne die Seitenleiste mit den Themen (eine Seite, ein Thema):

1. **Kopf** (Marine): Kürzel „WÜ“, Zeile „Tutorium 5 · Wärmebilanzen, instationär global“, Titel „Kaffee mit Milch: Simulation“; rechts Stand und „Werte bleiben nur in diesem Browser“.
2. **Frageleiste** (hellblau, eine Zeile): aktuelle Frage mit Nummer, Vorhersagefeld, Knopf „Vorhersage festhalten, dann prüfen“, vor und zurück. Abweichung vom Lernzentrum (dort stehen die Fragen nur im Reiter „Probier aus“), damit Frage, Vorhersage und Diagramm zugleich zu sehen sind (Abschnitt 4, A6).
3. **Ansicht des Diagramms** als Umschaltknöpfe wie „Stationär · Instationär“: „Temperatur“ (Standard), „Energie“, „Messwerte linear (ln)“ (erst aktiv, wenn mindestens drei Messwerte eines Bechers ohne Milch vorliegen).
4. **Diagramm** links, bis 780 px breit, als SVG in der tatsächlichen Breite gezeichnet (Schrift am Handy so groß wie am Laptop). Kurven direkt beschriftet („Tasse 1: Milch sofort“, „Tasse 2: Milch nach 60 min“), Linienart zusätzlich zur Farbe, Mischsprünge gepunktet, Schnittpunkt als Kreis, Raumtemperatur gestrichelt, Messpunkte mit eigener Form je Becher, die festgehaltene Vorhersage als grüne Marke, ein gemerkter Vergleichslauf blass.
5. **Knöpfe** rechts: „Standardwerte (Aufgabe)“ (Hauptknopf), „Wie im Versuch (40 min, Becher)“, „Lauf zum Vergleich merken“, „Vorhersage neu“. Darunter zwei kleine Darstellungen: **Energie bis zur Zugabe** (Säulen $Q_1$ und $Q_2$ mit Werten und dem Satz „$Q_2 - Q_1$ = 3,69 kJ entspricht 3,85 K Unterschied“) und **Bilanzraum** (beide Tassen mit gestrichelter Bilanzgrenze, Pfeil $\dot{Q}_\mathrm{ab}$, dessen Breite mit dem Wärmestrom am rechten Rand des Diagramms wächst).
6. **Regler** in drei Spalten: *Milch* (Zugabe nach $t_\mathrm{Z}$, Milchtemperatur $\vartheta_\mathrm{M}$, Milchmenge $V_\mathrm{M}$, Schalter „Milch für Tasse 2 bei Raumtemperatur“), *Tasse und Raum* (Raumtemperatur $\vartheta_\mathrm{u}$, Becher ohne/Keramik, Deckel offen/zu, „Weitere Größen“), *Messung und kA* (Anfangstemperatur $\vartheta_\mathrm{K,0}$, Messung nach 10 min, Kaffeemenge $V_\mathrm{K}$, $kA$ von Tasse 1 relativ). Jeder Regler mit Zahlenfeld und Fragezeichen-Hilfe wie im Lernzentrum.
7. **Rechenwerte** rechts neben den Reglern: $\vartheta_1$, $\vartheta_2$, Unterschied mit Satz („Tasse 1 wärmer“), Schnitt der Kurven, $Q_1$ und $Q_2$, $kA$ aus der Messung, Mischtemperatur $\vartheta_{1,0}$, Ihre Vorhersage.
8. **Messwerte aus dem Versuch** als Messblatt: Zeilen alle 10 min (0 bis 60, weitere Zeile möglich), Spalten Becher 1 (sofort), Becher 2 (Kühltasche), Becher 3 (Glas); Raum- und Milchtemperatur; Knöpfe „Einstellungen aus den Messwerten übernehmen“, „kA aus allen Punkten“, „Beispielmessung laden“, „Messwerte als Link teilen“, „Alle löschen“.
9. **Reiterleiste** mit den neun Reitern des Lernzentrums (Texte in Anhang A). „Versuche“ heißt hier „Auflösungen“, damit es nicht mit dem Becherversuch verwechselt wird (Entscheidung E6).
10. **Fuß**: Stand, Version, Prüfsumme der Datei (Baunachweis), Verweis auf Blatt und Lösung, keine Werbung, keine Zählpixel.

### 5.2 Handy (bis 767 px, Abnahme bei 390 px)

| Startzustand | Beim Arbeiten |
|:--:|:--:|
| ![Skizze Handy Start](skizzen/skizze_handy_start.png) | ![Skizze Handy Arbeit](skizzen/skizze_handy_arbeit.png) |

- **Startzustand:** Achsen, Raumlinie und der Startpunkt 80 °C sind zu sehen, die Kurven nicht. Die Karte „Erst vorhersagen“ fragt: Welche Tasse ist nach 60 min wärmer (Tasse 1, Tasse 2, gleich), um etwa wie viel K? Erst „Kurven zeigen“ zeichnet die Kurven; die Vorhersage bleibt als Marke im Diagramm.
- **Beim Arbeiten:** Diagramm und die drei wichtigsten Zahlen ($\vartheta_1$, $\vartheta_2$, Unterschied) bleiben oben angeheftet (höchstens 45 % der Bildschirmhöhe, abschaltbar), darunter scrollen Frageleiste, Regler und alles Weitere. So sieht man beim Verschieben eines Reglers die Wirkung.
- Eine Spalte. Reglergruppen als aufklappbare Abschnitte (*Milch* offen, die anderen zu). Jeder Regler mit Minus- und Plusknopf und Zahlenfeld, Zielgröße mindestens 44 px. Rechenwerte, Messblatt und Erklärungen als aufklappbare Abschnitte; die neun Reiter werden am Handy zu aufklappbaren Abschnitten in derselben Reihenfolge.
- Kein waagerechtes Scrollen bei 320 bis 767 px; Querformat zeigt Diagramm und Regler nebeneinander.

### 5.3 Zustände, die die Abnahme ansieht

Startzustand vor der Vorhersage; Standardwerte; jede Frage nach „Prüfen“; ungültige Einstellung (Diagramm sichtbar durchgestrichen, keine alten Zahlen, wie D116); Messblatt leer, halb und voll; Ansicht „Energie“ und „ln“; Vergleichslauf; Deckel und Becher an; Handy hoch und quer; Tastatur allein; Bildschirmleser (Abschnitt 10).

## 6 Fragen (Probier aus)

Jede Frage beginnt mit „Sagen Sie erst zu zweit voraus und notieren Sie …“ (D124). Neu: Die Vorhersage wird zusätzlich im Werkzeug festgehalten (Zahl oder Auswahl), erst dann gibt „Prüfen“ den Ausgangszustand frei (Standardwerte laden und sagen, dass sie geladen sind; X3, Befund Simulation 4) und schaltet die Auflösung zum Aufklappen frei. Die erwarteten Antworten sind von Claude unabhängig nachgerechnet (`claude_nachrechnung/n1_hoechstwert.txt`, `n2_erweiterungen.txt`, `n3_fragen.txt`); die Zahlen der Fragen 1, 2 und der Zusatzfrage Becher stimmen mit den Hinweisen der Lösung überein.

| Nr. | Stellen Sie sich vor … | Was sagen Sie voraus? (Eingabe) | Erwartung (Auflösung) |
|:--|:--|:--|:--|
| Start | Beide Tassen stehen 60 min, Milch aus dem Kühlschrank. | Welche Tasse ist nach 60 min wärmer, um etwa wie viel K? (Tasse 1, Tasse 2, gleich; Zahl in K) | Tasse 1, 3,85 K (34,05 gegen 30,19 °C). Tasse 2 war vor der Zugabe heißer und hat mehr Wärme abgegeben: $Q_2 - Q_1$ = 3,69 kJ. |
| 1 Zeitpunkt | Die Milch kommt früher oder später in Tasse 2. | Bei welchem Zeitpunkt der Zugabe ist der Unterschied am größten? (Zahl in min) | Etwa nach 56 min (3,86 K; die Anzeige zeigt 3,86 K von 53 bis 59 min), genau am Schnittpunkt. Danach ist der schwarze Kaffee kühler als Tasse 1 und gibt weniger Wärme ab. Der Unterschied geht nicht gegen null: Grenzwert 1,91 K (20 °C gegen 18,09 °C), weil die kalte Milch Tasse 2 beim Mischen erneut abkühlt. |
| 2 Milchtemperatur | Die Milch ist wärmer. | Wie warm müsste die Milch sein, damit beide Tassen nach 60 min gleich warm sind? (Zahl in °C) | 47,0 °C. Der Wert hängt vom Zeitpunkt ab: 60,9 °C bei Zugabe nach 30 min, 37,3 °C nach 90 min. |
| 3 Deckel (neu) | Beide Tassen bekommen einen Deckel; sie kühlen langsamer ab ($kA$ um 44 % kleiner). | Wird der größte mögliche Unterschied größer, kleiner oder bleibt er gleich, und wann tritt er ein? (Auswahl; Zahl in min) | Gleich groß (3,86 K), aber später: bei Zugabe nach etwa 100 min statt 56 min (Anzeige 3,86 K von 94 bis 106 min). Nach 60 min ist der Unterschied mit Deckel sogar kleiner (3,51 K). Grund: $kA$ steht nur im Produkt $kA\,t$; der Deckel streckt die Zeitachse, die Kurven schneiden sich immer bei 35,4 °C des schwarzen Kaffees. |
| 4 Versuch | Sie vergleichen Ihre Messwerte mit dem Modell. | Liegen Ihre Messpunkte über oder unter den Kurven, und warum? (Auswahl) | Meist einige Kelvin darüber, je später, desto mehr: Die Wärmeabgabe wächst stärker als linear mit $\vartheta - \vartheta_\mathrm{u}$ (Verdunstung, freie Konvektion), also wird das wirksame $kA$ mit sinkender Temperatur kleiner. In der Ansicht „ln“ liegen die Punkte nicht auf einer Geraden. Der Unterschied zwischen Becher 1 und 2 passt meist besser als die Einzelwerte. |
| Zusatz Becher | Die Tassen sind vorgewärmte Keramikbecher (Teil g). | Wird der Unterschied größer oder kleiner, und bleibt Tasse 1 wärmer? | Kleiner: 3,08 statt 3,85 K; die abgegebene Wärme steigt (46,60 und 50,34 kJ statt 34,88 und 38,57 kJ), weil der Becher mit abkühlt; Tasse 1 bleibt wärmer. |
| Zusatz Trinken | Sie trinken erst 30 min nach der Zugabe (Zugabe nach 60 min). | Wird der Unterschied bis dahin größer, kleiner oder bleibt er? | Er klingt ab: 2,03 K nach 90 min, 1,07 K nach 120 min, weil nun beide Tassen dasselbe $m\,c_p$ und $kA$ haben (nur mit Erweiterung M4). |

Fragetexte im Werkzeug (Vorschlag; Frage 1, 2 und Becher wörtlich wie heute nach D116 und D124, Frage 3 und 4 neu):

1. **Zeitpunkt.** Sagen Sie erst zu zweit voraus und notieren Sie: Bei welchem Zeitpunkt der Milchzugabe in Tasse 2 ist der Unterschied zwischen den Tassen ungefähr am größten? Prüfen Sie dann: Verschieben Sie die Zugabe der Milch in Tasse 2. Warum wird der Unterschied bei späterer Zugabe wieder kleiner?
2. **Milchtemperatur.** Sagen Sie erst zu zweit voraus und notieren Sie: Wie warm müsste die Milch sein, damit beide Tassen nach 60 Minuten ungefähr gleich warm sind? Prüfen Sie dann: Stellen Sie die Milch so warm ein, dass beide Tassen ungefähr gleich warm sind. Hängt diese Temperatur vom Zeitpunkt der Zugabe ab?
3. **Deckel.** Sagen Sie erst zu zweit voraus und notieren Sie: Mit Deckel kühlen beide Tassen langsamer ab. Wird der größte mögliche Unterschied zwischen den Tassen größer, kleiner, oder bleibt er gleich? Wann tritt er ein? Prüfen Sie dann: Setzen Sie den Deckel auf und suchen Sie wie in Frage 1 den Zeitpunkt der Zugabe mit dem größten Unterschied. Vergleichen Sie mit Frage 1.
4. **Versuch.** Sagen Sie erst zu zweit voraus und notieren Sie: Liegen Ihre Messwerte über oder unter den Kurven des Modells, und warum? Prüfen Sie dann: Laden Sie die Messwerte Ihres Kurses (Link der Tutoriumsleitung) oder tragen Sie sie ein und übernehmen Sie die Einstellungen aus den Messwerten. Wo liegen die Messpunkte? Liegen die Punkte von Becher 2 in der Ansicht „Messwerte linear (ln)“ auf einer Geraden?

Den Satz „Laden Sie zuerst die Standardwerte“ übernimmt der Knopf „Prüfen“ (er lädt sie und sagt es an); in der gedruckten Fassung der Fragen (Reiter „Probier aus“, Druckansicht) bleibt der Satz stehen.

## 8 Modell und Erweiterungen

Regel des Auftrags: Jede Zahl kommt aus `kaffee_modell.py` oder aus einer begründeten, getesteten Erweiterung. Die Erweiterungen ändern das Grundmodell nicht, sie setzen auf ihm auf. Alle Testwerte unten hat Claude mit eigenen Skripten ohne `kaffee_modell.py` gerechnet (`recherche/claude_nachrechnung/`); der Bau prüft sie zusätzlich gegen eine Python-Referenz, die `kaffee_modell.py` importiert.

### 8.1 Grundmodell (unverändert, M0)

Wie `rechne()` und `zwei_tassen()` und wie der geprüfte Block `MODELL-ANFANG` bis `MODELL-ENDE` des heutigen Werkzeugs. Mit $C_\mathrm{K} = \rho_\mathrm{K} V_\mathrm{K} c_{p,\mathrm{K}}$, $C_\mathrm{M} = \rho_\mathrm{M} V_\mathrm{M} c_{p,\mathrm{M}}$, Becher $C_\mathrm{B} = m_\mathrm{B} c_\mathrm{B}$ (sonst 0), $C_\mathrm{KB} = C_\mathrm{K} + C_\mathrm{B}$, $C_\mathrm{GB} = C_\mathrm{K} + C_\mathrm{M} + C_\mathrm{B}$:

- $kA = -\dfrac{C_\mathrm{KB}}{t_\mathrm{mess}} \ln\dfrac{\vartheta_\mathrm{mess} - \vartheta_\mathrm{u}}{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}$ (Teil c, mit Becher Teil g)
- Mischen ohne Wärmeverlust: $\vartheta_{1,0} = \dfrac{C_\mathrm{KB}\,\vartheta_\mathrm{K,0} + C_\mathrm{M}\,\vartheta_\mathrm{M}}{C_\mathrm{GB}}$, ebenso Tasse 2 bei der Zugabe
- Abkühlen: $\vartheta(t) = \vartheta_\mathrm{u} + (\vartheta_0 - \vartheta_\mathrm{u}) \exp(-kA\,t / C)$ mit $C = C_\mathrm{GB}$ (Tasse 1) bzw. $C_\mathrm{KB}$ (schwarzer Kaffee)
- abgegebene Wärme bis zur Zugabe aus der Energiebilanz (Teil e): $Q_1 = C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1)$, $Q_2 = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K})$
- Schnittpunkt beider Kurven vor der Zugabe in beiden Richtungen (D116)

Testfälle (aus der Lösung, bestätigt): Standard $kA$ = 0,3402 W/K, $\vartheta_{1,0}$ = 70,47 °C, $\vartheta_1$ = 34,05 °C, $\vartheta_2$ = 30,19 °C, $Q_1$ = 34,88 kJ, $Q_2$ = 38,57 kJ, Schnitt nach 55,8 min; mit Becher $kA$ = 0,4440 W/K, 34,04 und 30,96 °C, $Q_1$ = 46,60 kJ, $Q_2$ = 50,34 kJ; wie im Versuch (40 min, Becher) 41,79 und 38,82 °C.

**Eine Eigenschaft, die das Konzept trägt** (eigene Herleitung, `n1_hoechstwert.txt`): Der Unterschied $\vartheta_1 - \vartheta_2$ ist als Funktion des Zeitpunkts der Zugabe genau dann am größten, wenn Tasse 1 und der schwarze Kaffee gleich warm sind (Ableitung null, weil beide dann denselben Wärmestrom abgeben). Am Schnitt ist $\vartheta_\mathrm{x} - \vartheta_\mathrm{u} = (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})\,q^{-C_\mathrm{GB}/C_\mathrm{M}}$ mit $q = (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})/(\vartheta_{1,0} - \vartheta_\mathrm{u})$, unabhängig von $kA$, und der größte Unterschied ist $C_\mathrm{M}(\vartheta_\mathrm{x} - \vartheta_\mathrm{M})/C_\mathrm{GB}$. Zahlen: ohne Becher $\vartheta_\mathrm{x}$ = 35,38 °C und 3,862 K, mit Becher 35,78 °C und 3,090 K, jeweils für jedes $kA$; nur der Zeitpunkt verschiebt sich (55,8 min; $kA \cdot 0{,}56$: 99,5 min; $kA/2$: 111,5 min; $2\,kA$: 27,9 min). Die Behauptung der Übergabe („rund 3,9 K bei jedem $kA$, schwarzer Kaffee etwa 35 °C, Dämmung verzögert nur“) ist damit bestätigt; sie gilt, solange beide Tassen dasselbe $kA$ haben ($kA$ von Tasse 1 relativ = 100 %).

### 8.2 Erweiterungen

PLATZHALTER_ERWEITERUNGEN

### 8.3 Was das Werkzeug nicht rechnet

- Verdunstung als eigener Vorgang, verdunstete Masse: bleibt pauschal in $kA$ (Annahme der Aufgabe). Eine Zahl dafür im Werkzeug würde die Hausaufgabe zur Verdunstung vorwegnehmen (D123).
- Temperaturverteilung in der Tasse (ideal durchmischt, Annahme der Aufgabe), Wärmeleitung im Becher, Strahlung getrennt.
- Abkühlen des Bechers vor dem Eingießen (vorgewärmt, immer so warm wie der Inhalt, Teil g).


PLATZHALTER_TECHNIK

PLATZHALTER_PRUEFPLAN

PLATZHALTER_AUFWAND

PLATZHALTER_ENTSCHEIDUNGEN

PLATZHALTER_ANHANG
