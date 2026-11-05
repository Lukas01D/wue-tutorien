# Gutachten G3: Fachgutachter Wärmeübertragung

> **Zwischenstand, nicht abgeschlossen.** Abgebrochen am 05.11.2026 auf Anweisung der Koordination (Pause der TL wegen Nutzungslimit). Die Abschnitte 1 bis 6 sind vollständig ausgearbeitet; die 30 Zustände und alle Auflösungen sind verglichen. **Noch nicht geprüft:**
>
> - Messblatt mit „Becher 3 zeigen“ (zwei Mischsprünge, Rechenwerte mit verglichenem Paar Becher 2 oder 3) und mit Häkchen „mit Deckel gemessen“
> - Link mit Kurswerten (hin und zurück) und CSV-Ausgabe (Testwerte M11)
> - Aufklappbare Wertetabelle des Diagramms (Werte je 5 min) und Lage der Kurven im Bild (geprüft wurden nur die Texte, keine Pixelpositionen)
> - Vergleichslauf („Lauf zum Vergleich merken“)
> - Englische Texte über die Auflösungen und eine Stichprobe der Rechenwerte hinaus
> - Abschließende Suche nach Gedankenstrichen in diesem Gutachten
> - Nicht Aufgabe dieser Rolle und nicht geprüft: Handy-Ansicht, Barrierefreiheit, Tastaturbedienung

| | |
|:--|:--|
| Rolle | G3 „Fachgutachter Wärmeübertragung“ |
| Datum | 05.11.2026 |
| Art | getrennte Rollenprüfung desselben Modells (eine unabhängige Prüfung mit einem anderen Modell folgt) |
| Gegenstand | `simulation/site/index.html` (Fuß: „Stand 2026-11-05 · Version d2ce37a8e5“) |
| SHA-256 | `f519052cadf6745eeeb4eb97f5a0042c74688f3495cada09c059970b25016707` (369 081 Byte; vor und nach der Prüfung gleich) |
| Umgebung | Linux-Container der Cloud-Sitzung, Node v22.23.4, Playwright mit Chromium (`chromium.launch()` ohne Optionen), Python 3.13.18; Seite als `file:`-Aufruf, Fenster 1366 × 900 px |
| Maßstab | `simulation/KONZEPT.md` Fassung 2 (Abschnitte 6, 8, Anhang A, C); Aufgabe und Lösung in der **fertigen Fassung vom 31.10.2026** (`ergebnisse/kaffee/fertig/`, dort Teil f = erwärmte Milch $\vartheta_\mathrm{M,h}$ = 60 °C, Teil g = vorgewärmter Keramikbecher); Versuch für die Website 60 min (E8) |

Nicht gelesen: Code der Seite (Skript in `index.html`, `simulation/site/src/`, `simulation/modell/kaffee_erweitert.py`), `BAU_BERICHT.md`, `PROTOTYPEN.md`, `ZUSTAENDE.md`, `tests/`, `recherche/`, andere Gutachten, Git-Protokoll. Gelesen wurde nur, was die Seite anzeigt (sichtbarer Text, Beschriftungen, Formeln im DOM).

**Kurzurteil.** Alle 30 Zustände stimmen in jeder angezeigten Zahl mit meiner unabhängigen Rechnung überein, ebenso die Auflösungen von Start, Frage 1, Frage 2 und V1 bis V5 (deutsch und englisch), die Teilflächen der Wärmestrom-Ansicht, die Ausgleichsgerade und die Übernahme einer Messreihe. Die Physik der Seite ist richtig. Es bleiben drei mittlere Befunde (Bewertung der Startvorhersage, ein ungenauer Satz in der Start-Auflösung, Darstellung „Becher kalt“) und mehrere kleine Text- und Begriffsbefunde.

## 2 Eigene Gleichungen und Prüffälle (vor dem Blick auf die Seite festgelegt)

*Festgelegt und gerechnet am 05.11.2026 vor dem ersten Öffnen der Seite. Ein Hinweis der Koordination (Maßstab ist die fertige Fassung vom 31.10.2026) kam während dieser Phase; er ändert keine Zahl, nur die Teilbezüge (erwärmte Milch Teil f, Becher Teil g). Das Rechenskript `simulation/modell/kaffee_modell.py` (Fassung der fertigen Lösung) weicht vom Skript im Prüfpaket nur durch Zusätze ab (`zwei_tassen`, geschlossene Lösung in `nichtlinear`); die Grundgleichungen sind gleich.*

### 2.1 Gleichungen

Bezeichnungen wie Aufgabe und Vorlesung; Wärmekapazitäten $C_\mathrm{K} = \rho_\mathrm{K} V_\mathrm{K} c_{p,\mathrm{K}}$, $C_\mathrm{M} = \rho_\mathrm{M} V_\mathrm{M} c_{p,\mathrm{M}}$, Becher $C_\mathrm{B} = m_\mathrm{B} c_\mathrm{B}$ (aus: 0), $C_\mathrm{KB} = C_\mathrm{K} + C_\mathrm{B}$, $C_\mathrm{GB} = C_\mathrm{KB} + C_\mathrm{M}$. *kA* von Tasse 1 ist $f_1\,kA$.

1. *kA* aus der Messung (Teil c, mit Becher Teil g): $kA = -\dfrac{C_\mathrm{KB}}{600\,\mathrm{s}}\ln\dfrac{\vartheta_\mathrm{mess} - \vartheta_\mathrm{u}}{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}$. Standard ungerundet $kA_0 = 0{,}340246$ W/K.
2. Mischen (Teil a, Becher vorgewärmt): $\vartheta_{1,0} = (C_\mathrm{KB}\vartheta_\mathrm{K,0} + C_\mathrm{M}\vartheta_\mathrm{M1})/C_\mathrm{GB}$.
3. Abkühlen (Teil b): Tasse 1 $\vartheta_1(t) = \vartheta_\mathrm{u} + (\vartheta_{1,0} - \vartheta_\mathrm{u})\exp(-f_1 kA\,t/C_\mathrm{GB})$; schwarzer Kaffee $\vartheta_\mathrm{2,K}(t) = \vartheta_\mathrm{u} + (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})\exp(-kA\,t/C_\mathrm{KB})$.
4. Zugabe bei $t_\mathrm{Z}$: $\vartheta_2 = (C_\mathrm{KB}\vartheta_\mathrm{2,K}(t_\mathrm{Z}) + C_\mathrm{M}\vartheta_\mathrm{M2})/C_\mathrm{GB}$ mit $\vartheta_\mathrm{M2} = \vartheta_\mathrm{M}$ oder $\vartheta_\mathrm{u}$ (Schalter „Milch für Tasse 2 bei Raumtemperatur“).
5. Abgegebene Wärme bis zur Zugabe (Teil e): $Q_1 = C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1)$, $Q_2 = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K})$; Bilanz $C_\mathrm{GB}(\vartheta_1 - \vartheta_2) = Q_2 - Q_1 + C_\mathrm{M}(\vartheta_\mathrm{M1} - \vartheta_\mathrm{M2})$ (selbst hergeleitet aus 2 bis 5; Rest im Skript < 1e−13 kJ).
6. Schnittpunkt: $t_\mathrm{s} = \ln\dfrac{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}{\vartheta_{1,0} - \vartheta_\mathrm{u}} \Big/ \left(\dfrac{kA}{C_\mathrm{KB}} - \dfrac{f_1 kA}{C_\mathrm{GB}}\right)$.
7. Größter Unterschied über $t_\mathrm{Z}$: $\dfrac{\mathrm{d}(\vartheta_1 - \vartheta_2)}{\mathrm{d}t_\mathrm{Z}} = \dfrac{kA(\vartheta_\mathrm{2,K} - \vartheta_\mathrm{u}) - f_1 kA(\vartheta_1 - \vartheta_\mathrm{u})}{C_\mathrm{GB}}$, also Maximum bei gleichen Wärmeströmen; nur bei $f_1 = 1$ ist das der Schnittpunkt, dann $\Delta_\mathrm{max} = C_\mathrm{M}(\vartheta_\mathrm{x} - \vartheta_\mathrm{M})/C_\mathrm{GB}$ unabhängig von *kA*. Im Skript zusätzlich durch Abtasten in 1-s-Schritten und über ganze Minuten 1 bis 180 bestimmt.
8. Kipp-Milchtemperatur (Zusatzfrage (1), V1): $\vartheta_\mathrm{M} = \vartheta_\mathrm{u} + \dfrac{C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})(e_\mathrm{G} - e_\mathrm{K})}{C_\mathrm{M}(1 - e_\mathrm{G})}$.
9. Becher kalt (M9, nur *kA* fest): $\vartheta_\mathrm{2,K}(0) = (C_\mathrm{K}\vartheta_\mathrm{K,0} + C_\mathrm{B}\vartheta_\mathrm{u})/C_\mathrm{KB}$, $\vartheta_{1,0} = (C_\mathrm{K}\vartheta_\mathrm{K,0} + C_\mathrm{M}\vartheta_\mathrm{M} + C_\mathrm{B}\vartheta_\mathrm{u})/C_\mathrm{GB}$.
10. Trinkzeit (M10): $t_\mathrm{T} = \dfrac{C}{kA}\ln\dfrac{\vartheta_0 - \vartheta_\mathrm{u}}{\vartheta_\mathrm{T} - \vartheta_\mathrm{u}}$ für Tasse 1 ($C_\mathrm{GB}$, $\vartheta_{1,0}$) und den schwarzen Kaffee ($C_\mathrm{KB}$, $\vartheta_\mathrm{K,0}$).
11. Anzeige „von … auf … °C in 30 min“: $\vartheta_\mathrm{2,K}(30\,\mathrm{min})$, Zeitkonstante $C_\mathrm{KB}/kA$.
12. Wärmestrom-Teilflächen (M3): $\int_0^{t}(\dot{Q}_2 - \dot{Q}_1)\,\mathrm{d}t = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K}(t)) - C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1(t))$, geteilt beim Vorzeichenwechsel von $\dot{Q}_2 - \dot{Q}_1$ (Skript `g3_flaechen.py`).
13. Ausgleichsgerade (M2): $y_i = \ln\frac{\vartheta_i - \vartheta_\mathrm{u}}{\vartheta_0 - \vartheta_\mathrm{u}}$, $b = \sum t_i y_i/\sum t_i^2$, $kA = -C_\mathrm{KB}\,b$; dazu Gerade mit freiem Achsenabschnitt.

### 2.2 Prüffälle (30 Zustände)

Standardwerte, wenn nicht anders gesagt: 200 ml, 80 °C, 30 ml, 5 °C, 20 °C, Zugabe 60 min, *kA* fest $kA_0$, ohne Becher. Voreinstellungen als Faktor × $kA_0$ (Tabelle 8.2.1). Begründung je Fall: Z01 bis Z02 Aufgabe d/e; Z03 bis Z06 Frage 1 (Zeitpunkt, Maximum, Abfall, Grenzwert); Z07 bis Z10 Milchtemperatur (Lösung „Zum Weiterdenken“, Pflichttest M3, Teil f, Zusatzfrage (1)); Z11 bis Z21 Konzept 8.5 (Volumina, Temperaturen, *kA* fest gegen aus der Messung, Reglergrenzen); Z22 bis Z23 Teil g und typischer Fehler der Lösung; Z24 V4 und M-22 (ungleiches *kA*); Z25 bis Z28 Tabelle 8.2.1; Z29 M9; Z30 M10.

### 2.3 Fehlerschwelle (vorab festgelegt)

- Angezeigt werden laut Anhang A.2 Temperaturen auf 0,01 K und Wärmen auf 0,01 kJ. Übereinstimmung: angezeigter Wert gleich meinem Wert, gerundet auf die angezeigten Stellen.
- Abweichung um genau eine Einheit der letzten Stelle gilt **nicht** als Fehler, wenn mein ungerundeter Wert höchstens 0,0015 von einer Rundungsgrenze entfernt liegt oder wenn die Seite erkennbar mit *kA* = 0,3402 W/K (gerundet) statt $kA_0$ rechnet (Rundungsvariante; dann Befund „low“, falls dadurch ein Wert der Aufgabe abweicht).
- Jede andere Abweichung, und jede ab zwei Einheiten der letzten Stelle, ist ein Fehler (Schwere „blocker“, falsche Zahl).
- Zeiten in min: Abweichung ab 0,2 min ist ein Fehler. *kA*: vier Nachkommastellen, gleiche Regel wie oben.
- Zahlen in Auflösungstexten werden gegen meine Werte in der Genauigkeit des Textes geprüft.

*Wichtig für die Fehlerschwelle:* Mit genau 0,3402 W/K ergäbe sich $\vartheta_2$ = 30,1958 °C, angezeigt 30,20 °C statt 30,19 °C der Aufgabe. Die Seite zeigt 30,19 °C und bei Edelstahl 35,96 °C (gerundete Basis gäbe 35,97 °C): Sie rechnet mit dem ungerundeten $kA_0$. Die Rundungsvariante kam deshalb nirgends zur Anwendung.

## 3 Die 30 Zustände: eigene Werte gegen Anzeige

Bedienung: Startfrage (Tasse 1) und Frage 1 festgehalten, dann „Vertiefung“ geöffnet, Zahlenfelder mit Enter, Schalter und Voreinstellungsknöpfe angeklickt; je Zustand ein frischer Browserkontext. Gelesen wurden die angezeigten Texte: Rechenwerte, Energie bis zur Zugabe, Kasten „Schwarzer Kaffee: von … auf …“, Diagrammbeschreibung, Zusatzzeile. Eigene Werte ungerundet (4 Stellen), Anzeige wörtlich.

| Nr. | Einstellung | Eigene Werte ($\vartheta_1$ / $\vartheta_2$ / Δ in °C bzw. K; $Q_1$ / $Q_2$ in kJ; weitere) | Anzeige der Seite | Urteil |
|:--|:--|:--|:--|:--|
| Z01 | Standard, *kA* fest | 34,0465 / 30,1933 / 3,8532; 34,8809 / 38,5712; $\vartheta_{1,0}$ 70,4662; Schnitt 55,745 min; *kA* 0,340246; 30 min: 48,840, τ 40,95 min; Trinkzeit 60 °C 10,904 / 16,604 min | 34,05 / 30,19 / 3,85; 34,88 / 38,57; $Q_2 - Q_1$ = 3,69 kJ „entspricht 3,85 K“; 70,47; 55,7 min; 0,3402 festgehalten; 48,84 °C, 41,0 min; Trinkzeit 10,9 / 16,6 min | stimmt |
| Z02 | Standard, *kA* aus der Messung | wie Z01 | wie Z01, „aus der Messung nach 10 min“ | stimmt |
| Z03 | Zugabe 30 min | 46,6247 / 43,2669 / 3,3577; 22,8341 / 26,0500; Schnitt 55,7 min liegt nach der Zugabe | 46,62 / 43,27 / 3,36; 22,83 / 26,05; „kein Schnitt bis zur Zugabe“ | stimmt |
| Z04 | Zugabe 56 min | 35,2966 / 31,4349 / 3,8618; 33,6835 / 37,3821; Maximum 3,8618 K bei 55,75 min, gerundet 3,86 K für 53 bis 59 min | 35,30 / 31,43 / 3,86; 33,68 / 37,38; Abtastung 1 bis 180 min in der Seite: 3,86 K bei 53 bis 59 min | stimmt |
| Z05 | Zugabe 120 min | 23,9096 / 20,8888 / 3,0208; 44,5894 / 47,4826; Teilflächen +3,6987 / −0,8055 kJ | 23,91 / 20,89 / 3,02; 44,59 / 47,48; Wärmestrom: 3,70 / −0,81, Summe 2,89 kJ | stimmt |
| Z06 | Zugabe 180 min | 21,0882 / 18,7391 / 2,3491; 47,2916 / 49,5414; Teilflächen +3,6987 / −1,4488; Grenzwert $t_\mathrm{Z} \to \infty$: 1,9068 K | 21,09 / 18,74 / 2,35; 47,29 / 49,54; 3,70 / −1,45 / 2,25; Auflösung Frage 1: „Grenzwert 1,91 K (20 °C gegen 18,09 °C)“ | stimmt |
| Z07 | Milch 20 °C in beiden Tassen | 34,5772 / 32,1000 / 2,4772; $Q_1$ 36,1987; $\vartheta_{1,0}$ 72,3730; Schnitt 43,80 min | 34,58 / 32,10 / 2,48; 36,20 / 38,57; 72,37; 43,8 min | stimmt |
| Z08 | Milch für Tasse 2 bei Raumtemperatur (Pflichttest M3) | 34,0465 / 32,1000 / 1,9464; Milchbeitrag −1,8262 kJ; 3,6903 − 1,8262 = 1,8641 kJ | 34,05 / 32,10 / 1,95; „3,69 kJ, dazu Milchbeitrag −1,83 kJ, zusammen 1,86 kJ: entspricht 1,95 K“ | stimmt |
| Z09 | Milch 60 °C (Teil f) | 35,9924 / 37,1847 / −1,1923; $Q_1$ 39,7131; $\vartheta_{1,0}$ 77,4577; Schnitt 13,95 min | 35,99 / 37,18 / −1,19 „Tasse 2 wärmer“; 39,71 / 38,57; −1,14 kJ; 77,46; 13,9 min | stimmt |
| Z10 | Milch 47 °C (Zusatzfrage (1)) | 35,5325 / 35,5322 / 0,0003; $\vartheta_{1,0}$ 75,8051; Kipppunkt 47,003 °C | 35,53 / 35,53 / 0,00 „gleich warm“; 75,81; Auflösung V1 „47,0 °C“ | stimmt |
| Z11 | Kaffee 100 ml, *kA* fest | 24,4537 / 19,0968 / 5,3569; 20,8499 / 23,7413; 30 min 33,862, τ 20,48 min; Schnitt 30,07 min | 24,45 / 19,10 / 5,36; 20,85 / 23,74; 33,86 °C, 20,5 min; 30,1 min | stimmt |
| Z12 | Kaffee 400 ml, *kA* fest | 47,7385 / 45,8642 / 1,8742; 48,7381 / 52,1000; 61,598, τ 81,90 | 47,74 / 45,86 / 1,87; 48,74 / 52,10; 61,60, 81,9 min | stimmt |
| Z13 | Kaffee 100 ml, *kA* aus der Messung | *kA* 0,17012; 33,8520 / 27,3520 / 6,5001; 15,7772 / 19,2856 | 0,1701; 33,85 / 27,35 / 6,50; 15,78 / 19,29 | stimmt |
| Z14 | Kaffee 95 °C, *kA* fest | 37,6908 / 33,2183 / 4,4725; 43,9305 / 48,2140; 56,050; $\vartheta_{1,0}$ 83,5594 | 37,69 / 33,22 / 4,47; 43,93 / 48,21; 56,05; 83,56 | stimmt |
| Z15 | Kaffee 95 °C, *kA* aus der Messung | *kA* 0,65116; 25,4979 / 22,0582 / 3,4398; 55,6082 / 58,9026; 38,457, τ 21,40 | 0,6512; 25,50 / 22,06 / 3,44; 55,61 / 58,90; 38,46, 21,4 min | stimmt |
| Z16 | Raum 30 °C, *kA* fest | 41,2631 / 36,9054 / 4,3577; 27,9691 / 32,1427; 54,033 | 41,26 / 36,91 / 4,36; 27,97 / 32,14; 54,03 | stimmt |
| Z17 | Raum 10 °C, *kA* aus der Messung | *kA* 0,286275; 30,6169 / 27,1765 / 3,4404; 38,1655 / 41,4605; 47,794, τ 48,68; Schnitt 56,06 | 0,2863; 30,62 / 27,18 / 3,44; 38,17 / 41,46; 47,79, 48,7 min; 56,1 min | stimmt |
| Z18 | Milch 100 ml | 33,2354 / 24,4302 / 8,8052; 27,6367 / 38,5712; $\vartheta_{1,0}$ 55,4904 | 33,24 / 24,43 / 8,81; 27,64 / 38,57; 55,49 | stimmt |
| Z19 | 300 ml, 50 ml, 90 °C, Milch 10 °C, Raum 25 °C, *kA* 0,25 | 54,0380 / 50,2059 / 3,8321; 36,1606 / 41,7436; 70,401, τ 83,6; $\vartheta_{1,0}$ 78,8581 | 54,04 / 50,21 / 3,83; 36,16 / 41,74; 70,40, 83,6 min; 78,86 | stimmt |
| Z20 | *kA* 0,05 W/K | 61,8195 / 60,3211 / 1,4984; 8,2813 / 9,7165; 73,876, τ 278,67 | 61,82 / 60,32 / 1,50; 8,28 / 9,72; 73,88, 278,7 min | stimmt |
| Z21 | *kA* 1,00 W/K | 21,1764 / 18,7995 / 2,3770; 47,2071 / 49,4836; 26,967, τ 13,93; Schnitt 18,97 | 21,18 / 18,80 / 2,38; 47,21 / 49,48; 26,97, 13,9 min; 19,0 min | stimmt |
| Z22 | Becher an, *kA* aus der Messung (Teil g, V3) | *kA* 0,44403; 34,0436 / 30,9647 / 3,0788; 46,6025 / 50,3364; $\vartheta_{1,0}$ 72,4709; Schnitt 54,70; Trinkzeit 12,353 / 16,604; Maximum 3,09 K bei 52 bis 58 min | 0,4440; 34,04 / 30,96 / 3,08; 46,60 / 50,34; 3,73 kJ „entspricht 3,08 K“; 72,47; 54,7 min; 12,4 / 16,6 min; Abtastung 3,09 K bei 52 bis 58 min; Knopf „Wie im Versuch“ gibt dieselben Werte | stimmt |
| Z23 | Becher an, *kA* fest 0,3402 | 39,1106 / 36,0578 / 3,0528; 40,4575 / 44,1598; 54,226, τ 53,44 | 39,11 / 36,06 / 3,05; 40,46 / 44,16; 54,23, 53,4 min (passt zum typischen Fehler der Lösung „39,1 und 36,1 °C“) | stimmt |
| Z24 | *kA* von Tasse 1 = 105 % | 33,1764 / 30,1933 / 2,9831; $Q_1$ 35,7142; Temperaturschnitt erst bei 84,89 min; Maximum 2,9834 K bei 60,96 min (gleiche Wärmeströme), gerundet 2,98 K für 56 bis 66 min; Wärmeströme vor der Zugabe 4,707 / 4,717 W | 33,18 / 30,19 / 2,98; 35,71 / 38,57; „kein Schnitt bis zur Zugabe“; Abtastung 2,98 K bei 56 bis 66 min; Bilanzraum 4,71 / 4,72 W; bei Zugabe 120 min „Schnitt der Kurven nach 84,9 min“, Teilflächen 2,86 / −0,41 kJ (eigene Teilung am Wärmestromwechsel: 2,8573 / −0,4136) | stimmt |
| Z25 | Voreinstellung Keramik mit Deckel | *kA* 0,190538; 44,6580 / 41,1484 / 3,5096; 24,7177 / 28,0790; 59,809, τ 73,13; Maximum 3,86 K bei 94 bis 106 min | 0,1905 „Voreinstellung Keramik mit Deckel“; 44,66 / 41,15 / 3,51; 24,72 / 28,08; 59,81, 73,1 min; Abtastung 3,86 K bei 94 bis 106 min | stimmt |
| Z26 | Voreinstellung Edelstahl einwandig offen* | *kA* 0,306221; 35,9629 / 32,1026 / 3,8603; 33,0454 / 36,7426; 51,032, τ 45,50 | 0,3062; 35,96 / 32,10 / 3,86; 33,05 / 36,74; 51,03, 45,5 min; Stern und „Richtwert, geschätzt, nicht gemessen“ | stimmt |
| Z27 | Voreinstellung Thermobecher offen* | *kA* 0,149708; 48,7482 / 45,5802 / 3,1680; 20,8004 / 23,8345; 63,467, τ 93,07; Maximum 3,86 K bei 119 bis 135 min (genau 126,7 min) | 0,1497; 48,75 / 45,58 / 3,17; 20,80 / 23,83; 63,47, 93,1 min; Abtastung 3,86 K bei 119 bis 135 min | stimmt |
| Z28 | Voreinstellungen Glas offen* und Pappbecher offen* | wie Z01 | beide wie Z01, Herkunft „Voreinstellung Glas offen“ bzw. „Pappbecher offen“, Stern und Richtwert-Satz | stimmt |
| Z29 | Becher kalt (M9), *kA* fest 0,444, Becher 300 g | kalt: Start 59,8549 / schwarzer Kaffee 65,9762; nach 60 min 30,6680 / 28,0510 / 2,6170; vorgewärmt bei 0,444: 34,0449 / 30,9660 / 3,0788, 46,6010 / 50,3348 | Zusatzzeile: „Start Tasse 1 59,85 °C, schwarzer Kaffee 65,98 °C; nach 60 min 30,67 und 28,05 °C, Unterschied 2,62 K (vorgewärmt 3,08 K)“; Rechenwerte, Kurven und Energie zeigen den **vorgewärmten** Becher: 34,04 / 30,97 / 3,08; 46,60 / 50,33 | Zahlen stimmen; Darstellung siehe G3-03 |
| Z30 | Trinkzeit 60 °C mit Deckel | 19,4714 / 29,6500 min (Grenzfall der Rundung) | 19,5 / 29,7 min; Linie „Trinktemperatur 60 °C“ im Diagramm | stimmt |

**Ergebnis:** 30 von 30 Zuständen stimmen in allen angezeigten Zahlen. Keine Abweichung, auch keine von einer Einheit der letzten Stelle.

Zusätzlich geprüft (alle stimmen): Becher 600 g mit *kA* aus der Messung (0,5478 W/K; 34,03 / 31,47 / 2,56 °C bzw. K; 58,34 / 62,10 kJ; eigene Werte 0,54782; 34,0305 / 31,4681 / 2,5624; 58,3406 / 62,1015); Milch für Tasse 2 bei Raumtemperatur, Maximum 1,96 K bei 56 min (eigene Rechnung gleich); Wärmestrom-Teilflächen bei Zugabe 60 min +3,70 / −0,01 kJ (eigene +3,6987 / −0,0083); Bilanzraum-Pfeile Standard 4,78 / 4,72 W (eigene 4,779 / 4,717); Messreihe T10 des Konzepts (Becher 2: 80,1; 67,3; 56,9; 49,1; 42,7; 37,4; 33,7 °C) übernommen mit Becher: *kA* 0,4355 W/K, 34,43 / 31,34 / 3,09, 46,24 / 49,99 kJ, Schnitt 55,7 min (eigene 0,43549; 34,4289 / 31,3426 / 3,0863; 46,2443 / 49,9872; 55,7496 min); Ausgleichsgerade 0,4467 W/K durch den Ursprung, 0,4495 W/K frei, „6 Punkte, 10 bis 60 min“ (eigene 0,4467 / 0,4495, Abschnitt +0,0067); nach „*kA* aus der Ausgleichsgeraden festhalten“ 33,96 / 30,88 / 3,08, 46,82 / 50,55 kJ, Schnitt 54,4 min (eigene 33,9571 / 30,8765 / 3,0806, 46,8165 / 50,5525, 54,35 min). Ungültige Einstellung (Kaffee 60 °C, *kA* aus der Messung 67 °C) blendet Zahlen und Kurven aus und nennt den Grund. Englische Fassung: gleiche Zahlen mit Dezimalpunkt (Stichprobe *kA* von Tasse 1 = 105 %, Zugabe 120 min, und alle Auflösungen).

## 4 Weitere fachliche Prüfungen

**Auflösungen.** Start: „Tasse 1, 3,85 K (34,05 gegen 30,19 °C) … $Q_2 - Q_1$ = 3,69 kJ; 3,69 kJ geteilt durch 957,7 J/K … sind 3,85 K“: Zahlen richtig (3,6903 kJ / 957,7 J/K = 3,853 K); ein Halbsatz ungenau (G3-02). Frage 1: 56 min, 3,86 K, 53 bis 59 min, Begründung über die Wärmeströme, Grenzwert 1,91 K: richtig; „genau am Schnittpunkt“ steht in der Auflösung zur Ausgangslage mit gleichem *kA* und ist dort richtig. Frage 2: Erwartung offen formuliert; die genannten Ursachen (überlineare Wärmeabgabe, Raumtemperatur, Anlauf beim Eingießen, Thermometerlage, ungleiche Becher) erklären die Richtung „spätere Punkte über den Kurven“ physikalisch richtig. V1: 47,0 / 60,9 / 37,3 °C (eigene 47,003 / 60,912 / 37,285): richtig. V2: gleich groß 3,86 K, später, etwa 100 min, Anzeige 94 bis 106 min, nach 60 min 3,51 K, „*kA* steht nur im Produkt *kA t*“, mit Bedingung „gleiches *kA* beider Tassen“: richtig. V3: 3,08 statt 3,85 K, 46,60 und 50,34 kJ, Begründung „weil der Becher mit abkühlt“: richtig; Bezug „wie in Teil g“ passt zur fertigen Fassung. V4: 3,85 auf 2,98 K; ±10 % *kA* ändert um höchstens 0,04 K (eigene +0,007 / −0,037 K): richtig. V5: Thermobecher 63,5 statt 48,8 °C, Maximum 3,86 K nach etwa 127 min: richtig; Satz zu Glas und Pappe siehe G3-11.

**Annahmen und Grenzen (Reiter „Modell“).** Inhaltlich gleich den Annahmen der fertigen Aufgabe (ideal durchmischt, Becher nur in Teil g, $\dot{Q}_\mathrm{ab} = kA(\vartheta - \vartheta_\mathrm{u})$ mit konstantem *kA*, $c_p = c_v$); Zusätze der Simulation (*kA* für beide Tassen, *kA* festhalten ändert die Füllhöhe nicht, Übernahme als Mittel) sind richtig und ehrlich formuliert; „Sie rechnet nicht: Verdunstung …, Temperaturunterschiede in der Tasse, eine Wärmeabgabe, die stärker als linear wächst“ ist zutreffend. Kleine Punkte: G3-05, G3-10.

**Formelzeichen und Indizes (Ä24).** Alle Formeln im DOM geprüft (MathML): beschreibende Indizes aufrecht (K, M, u, Z, B, G, ab, mess, misch, Anfang, Ende, M1, M2, K,0), Größen kursiv ($\vartheta$, *t*, *Q*, *kA*, *c*, *m*, *V*, *C*), Index *p* in $c_p$ und *v* in $c_v$ sowie Laufindex *i* kursiv. Formelzeichen wie Aufgabe und Vorlesung; Teilbezüge (Teil f = 60 °C Milch, Teil g = Becher, Teil c für *kA*) passen zur fertigen Fassung vom 31.10.2026. Kein Befund.

**Kennzeichnung der *kA*-Voreinstellungen.** Glas, Pappbecher, Edelstahl und Thermobecher tragen den Stern und den Satz „Richtwert, geschätzt, nicht gemessen“; Keramik offen und Keramik mit Deckel ohne Stern; „Thermobecher mit Deckel“ ist begründet nicht angeboten. Faktoren 1,00 / 0,56 / 1,00 / 1,00 / 0,90 / 0,44 entsprechen Tabelle 8.2.1, alle Werte dort stimmen mit meiner Rechnung. Die kurzen Erklärungen sind physikalisch richtig (Deckel bremst Verdunstung und Luftbewegung, blankes Metall strahlt weniger ab, Vakuumwand lässt nur die offene Oberfläche). Die Begründungen der Richtwerte sind plausibel: Bei einer dünnen Wand ist der Leitwiderstand (Keramik etwa 0,003 m² K/W, Pappe etwa 0,005 bis 0,01 m² K/W) klein gegen den äußeren Übergang ($1/h$ mit $kA/A$ ≈ 17 W/(m² K) aus der Lösung, also etwa 0,06 m² K/W); dass 0,44 eher die Obergrenze der Wirkung des Thermobechers ist, folgt daraus, dass ein Styropordeckel die Oberseite nicht ganz sperrt. Kleine Punkte: G3-10, G3-11.

**Erklärtexte unter ihren Bedingungen (M-22).** Lesehilfe „Kreis: Schnittpunkt … (bei gleichem *kA* beider Tassen)“ und V2 „Gilt bei gleichem *kA* beider Tassen“ nennen die Bedingung. Mit *kA* von Tasse 1 = 105 % erscheint kein dynamischer Text, der den größten Unterschied an den Schnittpunkt bindet; die Wärmestrom-Ansicht teilt die Flächen physikalisch richtig beim Wechsel der Wärmeströme (61,0 min), nicht am Temperaturschnitt (84,9 min). Begriffliche Doppeldeutigkeit siehe G3-07. Die Energiezeile nennt den Milchbeitrag nur bei verschiedener Milchtemperatur (Z08). Becher kalt ist nur mit festgehaltenem *kA* möglich (mit *kA* aus der Messung gesperrt und abgehakt), wie M9 verlangt.

## 5 Befunde

Schweregrade wie vorgegeben (blocker, high, medium, low). Ein Befund mit falscher Physik oder falscher Zahl (blocker) wurde nicht gefunden.

| ID | Schwere | Befund | Beleg | Vorschlag | CONFIRMED/INFERRED |
|:--|:--|:--|:--|:--|:--|
| G3-01 | medium | Die Bewertung der Startvorhersage prüft nur die Tasse, nicht die Größe des Unterschieds. „Tasse 1, etwa 50 K“ und „Tasse 1, etwa 0,5 K“ werden beide mit „passt“ bestätigt, obwohl das Modell 3,85 K ergibt. Die Vorhersage „um etwa wie viel?“ wird abgefragt, aber nicht ausgewertet; eine falsche Größenordnung bekommt ein bestätigendes Zeichen. | Playwright, Startkarte, Auflösung: „Eure Vorhersage: Tasse 1 (Milch sofort), etwa 50 K · passt“; ebenso bei 0,5 K und ohne Zahl; Tasse 2 und „gleich warm“ ergeben „passt nicht“ (Skript `g3_maxscan.js`, englisch „matches“) | Bewertung nach Richtung und Größe trennen, zum Beispiel „Richtung passt; Größe: ihr habt 50 K geschätzt, das Modell gibt 3,85 K“; oder das Zeichen ausdrücklich „Richtung passt“ nennen | CONFIRMED |
| G3-02 | medium | Start-Auflösung: „Tasse 2 war bis zur Zugabe heißer und hat deshalb mehr Wärme abgegeben“ ist sachlich ungenau. Der schwarze Kaffee ist nur bis 55,7 min heißer, die Zugabe ist bei 60 min; das Diagramm daneben zeigt den Schnittkreis vor dem Kurvenende. Die Lösung schreibt richtig „bleibt es bis etwa 56 min“. Die Folgerung ($Q_2 > Q_1$) bleibt richtig. Der Wortlaut stammt aus KONZEPT.md 6.1. | Auflösung Start (deutsch und englisch „Up to the moment the milk is added, cup 2 was hotter“); eigene Rechnung Schnitt 55,745 min; Rechenwerte „Schnitt der Kurven nach 55,7 min“; Lösung vom 31.10.2026, Teil e | „Tasse 2 war fast bis zur Zugabe (bis etwa 56 min) heißer als Tasse 1 und hat deshalb mehr Wärme abgegeben“ (Text in KONZEPT.md 6.1 mitändern; Änderung am Konzepttext kennzeichnen) | CONFIRMED |
| G3-03 | medium | „Becher beim Eingießen kalt“ ändert weder Kurven noch Rechenwerte, Kernzahlen oder Energiesäulen; der kalte Becher erscheint nur in einer Zusatzzeile unter dem Diagramm. Die Rechenwerte zeigen weiter den vorgewärmten Becher (34,04 / 30,97 °C, 3,08 K), ohne das zu sagen. Wer den Schalter setzt, sieht im Diagramm keine Wirkung (Start bei 80 °C statt 65,98 °C). Die Zahlen der Zusatzzeile sind richtig. | Z29: Zusatzzeile „Becher kalt: Start Tasse 1 59,85 °C, schwarzer Kaffee 65,98 °C; nach 60 min 30,67 und 28,05 °C, Unterschied 2,62 K (vorgewärmt 3,08 K)“; Diagrammbeschreibung „Tasse 1 kühlt von 80,0 °C auf 34,04 °C ab“; KONZEPT.md K-4 „kalt statt vorgewärmt“ | Entweder Kurven, Rechenwerte und Energie bei gesetztem Schalter auf den kalten Becher umstellen (Gleichungen M9), oder den Schalter „Vergleich: Becher kalt eingießen“ nennen und die Rechenwerte mit „(Becher vorgewärmt)“ beschriften | CONFIRMED |
| G3-04 | low | Das Wort „Wärmeabgabe“ steht für zwei Größen mit verschiedener Einheit: für $\dot{Q}_\mathrm{ab}$ in W (Annahmen: „Die gesamte Wärmeabgabe … ist $\dot{Q}_\mathrm{ab} = kA(\vartheta - \vartheta_\mathrm{u})$“) und für *kA* in W/K (Regler „Wärmeabgabe der Tasse *kA* [W/K]“, Rechenwerte „Wärmeabgabe *kA*“). Für Studierende, die gerade Wärmestrom und Leitwert unterscheiden lernen, ist das missverständlich. Die Beschriftung folgt KONZEPT.md M-9. | Reiter „Modell“, Annahmen; Regler- und Rechenwertebeschriftung; Hilfetext „Wie stark die Tasse Wärme an den Raum abgibt“ | Zum Beispiel „Wärmeabgabe je Kelvin *kA*“ oder „Produkt *kA* (Wärmedurchgang)“; Entscheidung der TL, da im Konzept festgelegt | CONFIRMED |
| G3-05 | low | Mit Becher gilt die Bilanz mit $C_\mathrm{GB} = C_\mathrm{G} + m_\mathrm{B} c_\mathrm{B}$; mehrere Erklärtexte nennen nur $C_\mathrm{G}$ bzw. „$m\,c_p$ des Gemischs“: Reiter „So rechnet der Code“ ($C_\mathrm{G}(\vartheta_1 - \vartheta_2) = Q_2 - Q_1 + \dots$ und $\mathrm{d}(\vartheta_1 - \vartheta_2)/\mathrm{d}t_\mathrm{Z} = (\dot{Q}_2 - \dot{Q}_1)/C_\mathrm{G}$), Lesehilfe Energie („geteilt durch $m\,c_p$ des Gemischs“), Ansicht ln („Steigung $-kA/(m\,c_p)$“). Die angezeigten Zahlen rechnen richtig mit $C_\mathrm{GB}$ (3,73 kJ / 1212,7 J/K = 3,08 K). | Texte der Reiter (`g3_reiter_de.txt`); Z22 Energiezeile „3,73 kJ entspricht 3,08 K“ | Je einmal „(mit Becher zuzüglich $m_\mathrm{B} c_\mathrm{B}$)“ ergänzen, wie es der Abschnitt „Bilanz“ desselben Reiters schon tut | CONFIRMED |
| G3-06 | low | Lesehilfe „der kurze gepunktete Strich bei *t* = 0 ist der Mischsprung von 80 auf 70,47 °C“ bleibt fest, auch wenn Einstellungen geändert sind (100 ml Milch: Mischtemperatur 55,49 °C laut Rechenwerten). | Reiter „Modell“, „So liest du die Ergebnisse“, bei Milchmenge 100 ml unverändert | Zahlen aus dem aktuellen Zustand einsetzen oder „(bei Standardwerten)“ anfügen | CONFIRMED |
| G3-07 | low | Bei ungleichem *kA* (Tasse 1 = 105 %) meint „Schnitt“ zweierlei: Rechenwerte „Schnitt der Kurven nach 84,9 min“ (Temperaturkurven), Wärmestrom-Ansicht „vor dem Schnitt … 2,86 kJ, nach dem Schnitt … −0,41 kJ“ mit Teilung bei 61,0 min (Wärmestromkurven). Physik richtig, Wort doppeldeutig, gerade dort, wo M-22 die Unterscheidung lehren will. | Zugabe 120 min, *kA* von Tasse 1 = 105 %; eigene Teilflächen 2,8573 / −0,4136 kJ beim Wärmestromwechsel 60,96 min, Temperaturschnitt 84,89 min | Rechenwerte „Schnitt der Temperaturkurven“; in der Wärmestrom-Ansicht „vor bzw. nach dem Schnitt der Wärmeströme“ | CONFIRMED |
| G3-08 | low | Angesagte Ausgangslage stimmt bei V3 nicht mit der eingestellten überein: Frage zeigt „Ausgangslage: Standardwerte“ und nach dem Festhalten „Ausgangslage eingestellt: Standardwerte.“, eingestellt werden aber Becher an und *kA* aus der Messung (wie KONZEPT.md 6.2 verlangt). Nach „Einstellungen aus den Messwerten übernehmen“ bleibt die alte Ansage „Ausgangslage eingestellt: Standardwerte.“ stehen. | V3: Zustand vor und nach dem Festhalten (`g3_vertiefung.js`): becher false→true, *kA*-Quelle fest→messung; Übernahme in `g3_messung.js` | Ausgangslage bei V3 „Standardwerte, Becher an, *kA* aus der Messung“; Ansage bei Übernahme ersetzen | CONFIRMED |
| G3-09 | low | Bei ungültiger Einstellung zeigt der Kasten „Rechenwerte“ „erscheint nach eurer Vorhersage“, obwohl die Vorhersage festgehalten ist; der Grund steht nur unter den Reglern und in der Energiezeile („Keine Rechnung: Einstellung ungültig“). | Kaffee 60 °C, *kA* aus der Messung (67 °C) | Im Kasten „Rechenwerte“ „Einstellung ungültig: …“ anzeigen | CONFIRMED |
| G3-10 | low | Annahmen: „gemessen sind ‚Keramik offen‘ (Aufgabe) und ‚Keramik mit Deckel‘ (ein Becher mit Styropordeckel, Ferreira 2025a)“. Der Wert der Aufgabe (67 °C nach 10 min) ist ein Arbeitswert, der zur gemessenen Zeitkonstante bei Ferreira passt (Lösung: „passt zu Messungen …, τ ≈ 41 min“); der Deckelfaktor 0,56 stammt von einem anderen Becher und ist auf den Becher der Aufgabe übertragen. „gemessen“ ist etwas zu stark. | Reiter „Modell“, Annahmen; Lösung 31.10.2026 Teil c; KONZEPT.md Tabelle 8.2.1 („belegt: Arbeitswert der Aufgabe“) | „belegt sind ‚Keramik offen‘ (Arbeitswert der Aufgabe, passt zu τ ≈ 41 min bei Ferreira 2025a) und ‚Keramik mit Deckel‘ (Faktor 0,56 aus einem Becher mit Styropordeckel, Ferreira 2025a)“ | CONFIRMED |
| G3-11 | low | V5-Auflösung „Glas und Pappe sind etwa wie Keramik“ ist als Ergebnis formuliert, folgt in der Simulation aber nur aus den Richtwerten mit Faktor 1,00, die die Seite selbst setzt; die Simulation kann es nicht zeigen. Die physikalische Begründung (Wand nicht der große Widerstand) ist richtig. | V5-Auflösung; Voreinstellungen Glas und Pappe mit Stern, *kA* 0,3402 | „Nach den Richtwerten (*) sind Glas und Pappe etwa wie Keramik: …“ | CONFIRMED |
| G3-12 | low | Die Trinktemperatur ist fest 60 °C; KONZEPT.md 8.4 empfiehlt „Vorgabe einstellbar“ (Stufe kann). | Schalter „Trinkzeit bis 60 °C zeigen“, kein Eingabefeld | Feld für $\vartheta_\mathrm{T}$ (zum Beispiel 40 bis 75 °C) oder Empfehlung im Konzept anpassen | CONFIRMED |
| G3-13 | high | *Außerhalb der fachlichen Rolle, nur gesehen:* Die Reiterleiste hat drei Reiter („Versuche“, „Modell“, „So rechnet der Code“) statt neun (M-18), und der Reiter heißt „Versuche“ statt „Auflösungen“ (E6). Die Inhalte der neun Reiter sind als aufklappbare Abschnitte vorhanden. Ob eine spätere Entscheidung der TL das erlaubt, konnte ich nicht prüfen (Baubericht nicht gelesen). | Startseite bei 1366 px, `#reiter-leiste` | Mit der Rolle für Aufbau und Bedienung und der TL klären; sonst nach M-18 und E6 umbenennen bzw. aufteilen | INFERRED |

Zahl der Befunde: blocker 0, high 1 (G3-13, außerhalb der fachlichen Rolle, INFERRED), medium 3, low 9.

## 6 Anhang: Skripte

Alle Skripte liegen in `/tmp/claude-0/-home-user-wue-tutorien/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/gutachten_G3/`:

- `g3_rechnung.py`: eigene Rechnung der 30 Zustände (Gleichungen 2.1, ohne `kaffee_modell.py` und ohne Code der Seite), Ausgabe `g3_ergebnis.json`
- `g3_flaechen.py`: Teilflächen der Wärmestrom-Ansicht
- `g3_seite.js`: stellt die 30 Zustände in der Seite ein und liest die Anzeige, Ausgabe `g3_seite.json`
- `g3_maxscan.js`: Abtastung der Zugabe 1 bis 180 min in der Seite, Bewertung der Startvorhersage
- `g3_fragen.js`, `g3_vertiefung.js`: Fragen mit Vorhersage, Ausgangslage, Auflösung (deutsch und englisch)
- `g3_waermestrom.js`, `g3_messung.js`, `g3_reiter.js`, `g3_hilfe.js`, `g3_rest.js`: Wärmestrom, Bilanzraum, ungültige Einstellung, Becher kalt, Messreihe und Ausgleichsgerade, Reitertexte und Indizes, Hilfetexte

Wichtigste Zeilen aus `g3_rechnung.py`:

```python
KA0 = -836.0 / 600.0 * math.log(47.0 / 60.0)   # ungerundet 0,340246 W/K (Teil c)

def zustand(**aend):
    p = dict(STD); p.update(aend)
    C_K = RHO_K * p["V_K"] * 1e-6 * CP_K
    C_M = RHO_M * p["V_M"] * 1e-6 * CP_M
    C_B = p["m_B"] * 1e-3 * C_BS if p["becher"] else 0.0
    C_KB, C_GB = C_K + C_B, C_K + C_M + C_B
    u, K0 = p["th_u"], p["th_K0"]
    if p["quelle"] == "messung":
        kA = -C_KB / T_MESS * math.log((p["th_mess"] - u) / (K0 - u))
    else:
        kA = p["kA"]
    kA1 = p["f1"] * kA
    thM1 = p["th_M"]
    thM2 = u if p["milch2_raum"] else p["th_M"]
    if p["becher_kalt"]:                       # M9
        th2K0 = (C_K * K0 + C_B * u) / C_KB
        th10 = (C_K * K0 + C_M * thM1 + C_B * u) / C_GB
    else:
        th2K0 = K0
        th10 = (C_KB * K0 + C_M * thM1) / C_GB
    tz = p["t_Z"] * 60.0
    th1 = lambda t: u + (th10 - u) * math.exp(-kA1 * t / C_GB)
    th2K = lambda t: u + (th2K0 - u) * math.exp(-kA * t / C_KB)
    mix2 = lambda TK: (C_KB * TK + C_M * thM2) / C_GB
    r["th1"], r["th2K"] = th1(tz), th2K(tz)
    r["th2"] = mix2(r["th2K"]); r["dT"] = r["th1"] - r["th2"]
    r["Q1"] = C_GB * (th10 - r["th1"]) / 1000
    r["Q2"] = C_KB * (th2K0 - r["th2K"]) / 1000
    r["Qmilch"] = C_M * (thM1 - thM2) / 1000
    r["bilanz_rest"] = C_GB * r["dT"] / 1000 - (r["Q2"] - r["Q1"] + r["Qmilch"])
    # Schnitt, 30-min-Wert, Zeitkonstante, Trinkzeit, Maximum durch Abtasten (1 s) ...
```

Wichtigste Zeilen aus `g3_seite.js` (Bedienung wie Studierende, gelesen wird nur die Anzeige):

```js
await p.check('input[name=wahl-start][value="1"]'); await p.fill('#frage-zahl', '3'); await p.click('#knopf-fest');
await p.fill('#frage-zahl', '50'); await p.click('#knopf-fest');          // Frage 1 festhalten
await p.click('#vertiefung-titel');
// Zahlenfeld mit Komma, dann Enter; Schalter und Voreinstellungsknoepfe per Klick
await p.fill('#z-VK', '100'); await p.press('#z-VK', 'Enter');
await p.getByRole('button', { name: 'Keramik mit Deckel', exact: true }).click();
// gelesen: #rechenwerte-liste, #energie-inhalt, #info-kasten, #diagramm-beschreibung, #zusatz-text
```
