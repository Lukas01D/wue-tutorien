# Gutachten G3: Fachgutachter Wärmeübertragung

> **Abgeschlossen am 06.11.2026** (Fortsetzung des Zwischenstands vom 05.11.2026; nachgeholt: Messblatt mit Becher 3 und „mit Deckel gemessen“, Kurslink hin und zurück, CSV mit den Testwerten aus M11, Wertetabelle und Lage der Kurven im Bild, Vergleichslauf, englische Texte, Suche nach Gedankenstrichen). Die Abschnitte 1 bis 6 vom 05.11.2026 sind unverändert; die Nachträge stehen in Abschnitt 4a, neue Befunde ab G3-14. **Ergebnisse der Nachträge:**
>
> - Messblatt mit Becher 3: Übernahme (Mittel von Becher 2 und 3 bei 0 und 10 min) und alle Rechenwerte stimmen; im Diagramm fehlt aber der zweite Mischsprung (G3-14), und Becher 3 trägt in den Rechenwerten das Zeichen $\vartheta_2$ (G3-15). „mit Deckel gemessen“: richtig, kein zweiter Deckelfaktor, Hinweis „Der Deckel steckt schon im gemessenen *kA*“.
> - Kurslink: hin und zurück gleiche Werte und Bedingungen (auch Becher 3 und Deckel), ungültige Links ändern nichts und nennen den Grund; zwei Bedienlücken (G3-23, G3-24).
> - CSV: Testwerte M11 genau getroffen, alle Modellwerte in 1-min-Schritten stimmen (0 Abweichungen in 5 Fällen); englische Kopfzeile hat ein Feld zu viel (G3-16); Bedingungen fehlen (G3-17).
> - Wertetabelle: alle Werte stimmen; Darstellung bei der Zugabe und bei Zugabezeiten mit Nachkommastelle (G3-18, G3-19). Lage der Kurven: höchstens 0,017 K von meiner Rechnung (1 px = 0,27 K), Schnittkreis, Mischsprung bei *t* = 0 und Messpunkte an der richtigen Stelle.
> - Vergleichslauf: blasse Kurven richtig, aber ohne Mischsprung und ohne Zahl (G3-21).
> - Englische Texte: Physik und Zahlen richtig; G3-04 bis G3-06 gelten dort ebenso; neue Punkte G3-16, G3-22, G3-24.
> - Ausgleichsgerade mit Becher 3: Ursprungsgerade richtig, Gerade mit freiem Achsenabschnitt gewichtet den Startpunkt anders (G3-20).
> - Gedankenstriche: keine in diesem Gutachten (Suche nach U+2013 und U+2014: 0 Treffer; „ - “ nur als Minus im Programmtext).
> - Nicht Aufgabe dieser Rolle und nicht geprüft: Handy-Ansicht, Barrierefreiheit, Tastaturbedienung

| | |
|:--|:--|
| Rolle | G3 „Fachgutachter Wärmeübertragung“ |
| Datum | 05.11.2026, fortgesetzt und abgeschlossen am 06.11.2026 |
| Art | getrennte Rollenprüfung desselben Modells (eine unabhängige Prüfung mit einem anderen Modell folgt) |
| Gegenstand | `simulation/site/index.html` (Fuß: „Stand 2026-11-05 · Version d2ce37a8e5“) |
| SHA-256 | `f519052cadf6745eeeb4eb97f5a0042c74688f3495cada09c059970b25016707` (369 081 Byte; vor und nach der Prüfung gleich, am 06.11.2026 vor und nach der Fortsetzung erneut geprüft) |
| Umgebung | Linux-Container der Cloud-Sitzung, Node v22.23.4, Playwright mit Chromium (`chromium.launch()` ohne Optionen), Python 3.13.18; Seite als `file:`-Aufruf, Fenster 1366 × 900 px |
| Maßstab | `simulation/KONZEPT.md` Fassung 2 (Abschnitte 6, 8, Anhang A, C); Aufgabe und Lösung in der **fertigen Fassung vom 31.10.2026** (`ergebnisse/kaffee/fertig/`, dort Teil f = erwärmte Milch $\vartheta_\mathrm{M,h}$ = 60 °C, Teil g = vorgewärmter Keramikbecher); Versuch für die Website 60 min (E8) |

Nicht gelesen: Code der Seite (Skript in `index.html`, `simulation/site/src/`, `simulation/modell/kaffee_erweitert.py`), `BAU_BERICHT.md`, `PROTOTYPEN.md`, `ZUSTAENDE.md`, `tests/`, `recherche/`, andere Gutachten, Git-Protokoll. Gelesen wurde nur, was die Seite anzeigt (sichtbarer Text, Beschriftungen, Formeln im DOM).

**Kurzurteil.** Alle 30 Zustände stimmen in jeder angezeigten Zahl mit meiner unabhängigen Rechnung überein, ebenso die Auflösungen von Start, Frage 1, Frage 2 und V1 bis V5 (deutsch und englisch), die Teilflächen der Wärmestrom-Ansicht, die Ausgleichsgerade und die Übernahme einer Messreihe. Die Physik der Seite ist richtig. Es bleiben drei mittlere Befunde (Bewertung der Startvorhersage, ein ungenauer Satz in der Start-Auflösung, Darstellung „Becher kalt“) und mehrere kleine Text- und Begriffsbefunde.

*Nachtrag 06.11.2026:* Auch Messblatt (mit Becher 3 und Deckel), Kurslink, CSV, Wertetabelle, Kurvenlage und Vergleichslauf zeigen in jeder geprüften Zahl die richtigen Werte. Dazu kommen zwei mittlere Befunde: Becher 3 hat im Diagramm keinen eigenen Mischsprung (M-7 nicht erfüllt, G3-14), und die englische CSV-Kopfzeile verschiebt die Spaltennamen (G3-16). Dazu neun kleine Befunde.

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

## 4a Nachgeholte Prüfungen (06.11.2026)

Gleiche Seite (SHA-256 vor und nach unverändert), gleiche Umgebung, gleiche Fehlerschwelle (2.3). Eigene Werte aus `g3_rechnung.py` über `g3_f_rechnung.py`, `g3_f_csvcheck.py` und `g3_f_lage.py`; der Code der Seite wurde nicht gelesen.

**Messdatensatz F1 (Becher 3).** Becher 1: 70,9; 61,6; 54,2; 48,4; 43,6; 39,8; 36,7 °C. Becher 2: 80,1; 67,3; 56,9; 49,1; 42,7; 37,4; 33,7; nach der Milch 30,1 °C. Becher 3: 79,7; 66,9; 56,5; 48,8; 42,5; 37,3; 33,6; nach der Milch 32,0 °C. Raum 20 °C, Milch 5 °C. Erwartet nach M-7: Start und 10-min-Wert als Mittel von Becher 2 und 3, also 79,90 und 67,10 °C, Becher an, *kA* aus der Messung.

| Größe | eigene Werte | Anzeige | Urteil |
|:--|:--|:--|:--|
| Übernahme | 79,90 / 67,10 °C, Raum 20,0, Milch 5,0 | „Übernommen (Mittel der Becher vor der Milch, ungerundet): Start 79,90 °C, nach 10 min 67,10 °C …“ | stimmt |
| *kA*, $\vartheta_{1,0}$ | 0,43713 W/K; 72,3809 °C | 0,4371; 72,38 | stimmt |
| $\vartheta_1$ / $\vartheta_2$ / Becher 3 / Δ | 34,3095 / 31,2306 / 32,7364 (Milch 20 °C) / 3,0789 | 34,31 / 31,23 / 32,74 / 3,08 | stimmt |
| $Q_1$ / $Q_2$, Schnitt | 46,1709 / 49,9049 kJ; 55,58 min bei 35,74 °C | 46,17 / 49,90; 55,6 min; Kreis bei 55,58 min und 35,76 °C (Pixel) | stimmt |
| Kasten 30 min | 49,12 °C, τ = 1091 J/K / 0,43713 W/K = 41,60 min | „from 79.9 to 49.12 °C in 30 min (time constant 41.6 min)“ | stimmt |
| Ansicht ln | Ursprungsgerade aus 12 Punkten 0,44698 W/K | 0,4470 W/K, „Becher 2 und Becher 3, 12 Punkte, 10 bis 60 min“ | stimmt |
| Ansicht ln, freier Achsenabschnitt | 14 Punkte (Startpunkt je Becher): 0,44932; 12 Punkte ohne Start: 0,45135; 13 Punkte (Start einmal): 0,45003 W/K | 0,4500 W/K | siehe G3-20 |

Im Diagramm stehen die Messpunkte an der richtigen Stelle (Kreise, Quadrate, Dreiecke je auf ±0,02 K), aber es gibt nur einen Mischsprung bei der Zugabe (Becher 2, 34,16 auf 31,22 °C nach Pixeln); Becher 3 hat keinen gepunkteten Sprung, keine Linie und keine Beschriftung, nur ein randloses Dreieck bei etwa 32,7 °C zwischen den Messdreiecken (G3-14). Die Dreiecke von Becher 3 überdecken die fast gleich liegenden Quadrate von Becher 2.

**Messdatensatz F2 (mit Deckel, Kurslink des Konzeptformats).** `#kurs1=u:21.5;m:6;d:1;b:1.2;b1:68.2,62.0,56.6,52.0,48.0,44.6,41.6,;b2:79.0,70.4,63.1,57.0,51.7,47.2,43.4,39.0`. Eigene Werte (Becher an, *kA* aus 79,0 und 70,4 °C): *kA* 0,29458 W/K, $\vartheta_{1,0}$ 71,6716, $\vartheta_1$ 42,4259, $\vartheta_2$ 39,5130, Δ 2,9129, $Q_1$ 35,4677, $Q_2$ 39,0003 kJ, Schnitt erst bei 83,83 min, 30-min-Wert 56,865 °C, τ 61,73 min. Anzeige: 0,2946; 71,67; 42,43 / 39,51 / 2,91; 35,47 / 39,00; „kein Schnitt bis zur Zugabe“; 56,87 °C, 61,7 min. Stimmt. Mit `d:0` und denselben Werten gleiche Zahlen; mit `d:1` zusätzlich der Satz „Mit Deckel gemessen: Der Deckel steckt schon im gemessenen *kA*.“ Auch wenn vorher „Keramik mit Deckel“ gewählt war, rechnet die Übernahme mit 0,2946 W/K, also ohne zweiten Deckelfaktor (M-7, M1). Richtig.

**Kurslink hin und zurück.** F1 und F2 als Link geöffnet: Abfrage „Kurswerte aus dem Link übernehmen? Eure bisherigen Kurswerte werden ersetzt.“, nach „Übernehmen“ stehen alle Werte, Raum, Milch, Deckel und „Becher 3 zeigen“ im Messblatt; der danach erzeugte Link ist zeichengleich (F1) bzw. bis auf weggelassene Endnullen gleich (F2: `62` statt `62.0`). Ungültige Links (Raum `abc`, Formatversion `kurs2`, 999 °C, zu wenige Werte, `Unsinn`) ändern nichts und nennen den Grund. Lücken: G3-23.

**CSV (M11).** Deutsch: UTF-8 mit BOM, CRLF, Semikolon, Dezimalkomma, Kopfzeile mit Einheiten; Herunterladen liefert dieselbe Datei wie `window.KAFFEE.csv()` (`kaffee_simulation.csv`, englisch `coffee_simulation.csv`). Testwerte M11 genau: `0;70,47;80,00`, `1;69,40;78,55`, `2;68,36;77,14`, `10;60,78;67,00` (eigene 70,4662 / 80,0000; 69,4019 / 78,5526; 68,3600 / 77,1400; 60,7782 / 67,0000). Alle Modellwerte jeder Minute geprüft für Standard (deutsch und englisch), F1, Zugabe 56 und 120 min: 0 Abweichungen; Zeile „60 nach der Milch“ jeweils gleich meinen Werten. Messwerte stehen in den Zeilen 0, 10, … 60 und „60 nach der Milch“ unverändert. Befunde G3-16, G3-17.

**Wertetabelle und Lage der Kurven.** Tabelle je 5 min für Standard, Zugabe 56 und 120 min, „Keramik mit Deckel“ und F1: jeder Wert gleich meiner Rechnung auf 0,01 K (zum Beispiel Standard 55 min 35,63 / 35,66, 60 min 34,05 / 30,19; Zugabe 120 min: 115 min 24,35 / 23,62, 120 min 23,91 / 20,89). Vor der Vorhersage zeigt sie „erscheint nach eurer Vorhersage“ (M-2). Kurven als Pixel ausgelesen und über die Achsenteilung (0 und 60 min, 0 und 100 °C) zurückgerechnet: Standard, F1 und Vergleichslauf mit Deckel weichen höchstens 0,017 K ab (ein Pixel sind 0,27 K); Mischsprung bei *t* = 0 von 80,00 auf 70,48 °C, Schnittkreis Standard 55,75 min bei 35,38 °C (eigene 55,745 min, 35,380 °C). Befunde G3-18, G3-19.

**Vergleichslauf.** „Lauf zum Vergleich merken“ (in der Vertiefung) bei Standardwerten, dann „Keramik mit Deckel“: blasse Kurven (Deckkraft 0,28) liegen auf den Standardkurven (höchstens 0,016 K), kräftige Kurven auf den Deckelkurven; Knopf wird zu „Vergleich entfernen“. Befund G3-21.

**Englische Texte.** Geprüft: Kopf, Fragen 1 und 2, V1 bis V5 (Fragetexte), Regler und Hilfen, Rechenwerte, Energie, Bilanzraum, Messblatt, Übernahme, Kurslink, Voreinstellungen mit Erklärungen, Trinkzeit, Becher kalt, Milch für Tasse 2 bei Raumtemperatur, Ansicht Wärmestrom, Reiter „Model“ und „How the code calculates“, Fuß. Zahlen mit Thermobecher offen (*kA* 0,1497 W/K) nachgerechnet: Trinkzeit 24,8 / 37,7 min (eigene 24,78 / 37,74), Becher kalt 300 g 45,56 / 43,73 °C, 1,82 K, vorgewärmt 2,21 K (eigene 45,5551 / 43,7317 / 1,8234; 2,2148), Milch 20 °C für Tasse 2: 48,75 / 47,49 °C, 1,26 K, $Q_2 - Q_1$ = 3,03 kJ, Milchbeitrag −1,83 kJ, zusammen 1,21 kJ (eigene 3,0341 − 1,8262 = 1,2079 kJ, 1,2612 K). Physik und Fachbegriffe richtig („transient lumped energy balance“, „heat flow rate“, „control volume“, „time constant“). G3-04 gilt englisch ebenso („Heat loss of the cup *kA*“ in W/K neben „total heat loss … is $\dot{Q}_\mathrm{ab}$“), ebenso G3-05 („divided by $m c_p$ of the mixture“) und G3-06 („mixing jump from 80 to 70.47 °C“). Neue Punkte: G3-16, G3-22, G3-24.

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
| G3-14 | medium | Mit „Becher 3 zeigen“ hat das Diagramm bei der Zugabe nur **einen** Mischsprung (Becher 2). M-7 verlangt zwei (Becher 2 mit kalter Milch, Becher 3 mit Milch bei Raumtemperatur). Für Becher 3 gibt es keinen gepunkteten Sprung von 34,16 auf 32,74 °C, keine Linie, keine Beschriftung und keine Erwähnung in der Diagrammbeschreibung; nur ein randloses Dreieck bei etwa 32,7 °C, das zwischen den Messdreiecken nicht als Modellwert erkennbar ist. Gerade der Vergleich Becher 2 gegen Becher 3 (Zusatzfrage (2), Pflichttest M3) ist damit im Bild nicht zu sehen. Die Zahl 32,74 °C in den Rechenwerten ist richtig. | F1, Abschnitt 4a; `lage_b3.json`: eine gepunktete Sprunglinie bei *t* = 60 min (34,16 → 31,22 °C), SVG-Texte nur „Tasse 2: Milch nach 60 min“, „Tasse 1: Milch sofort“; Bild `zoom_b3.png`; eigene Werte 34,1577 → 32,7364 °C | Zweiten gepunkteten Sprung für Becher 3 zeichnen (strichpunktiert, `#3d70a3` nach M-10) und beschriften („Becher 3: Milch mit Raumtemperatur“); Diagrammbeschreibung um Becher 3 ergänzen | CONFIRMED |
| G3-15 | low | In den Rechenwerten trägt Becher 3 dasselbe Formelzeichen wie Tasse 2: „Tasse 2 $\vartheta_2$ 31,23 °C“ und „Becher 3 $\vartheta_2$ 32,74 °C“ (englisch „Mug 3 $\vartheta_2$“). Zwei verschiedene Werte mit einem Zeichen. Der Unterschied wird nur als $\vartheta_1 - \vartheta_2$ genannt; das Paar Tasse 1 gegen Becher 3 (1,57 K) fehlt, obwohl M-22 verlangt, dass die Rechenwerte das verglichene Paar nennen. | F1; eigene 34,3095 − 32,7364 = 1,5731 K | Becher 3 als $\vartheta_3$ bezeichnen und eine Zeile „Unterschied Tasse 1 − Becher 3: 1,57 K“ ergänzen | CONFIRMED |
| G3-16 | medium | Englische CSV: Die Kopfzeile enthält ein Komma im Spaltennamen „model cup 2, black until the milk [°C]“ ohne Anführungszeichen, bei Komma als Trennzeichen. Die Kopfzeile hat 6 Felder, die Datenzeilen 5 (mit Becher 3: 7 gegen 6). In einer Tabellenkalkulation stehen die Namen ab der dritten Spalte eine Spalte zu weit rechts: Unter „black until the milk“ stehen die Messwerte von Becher 1, unter „measurement mug 1“ die von Becher 2. Wer die Datei auswertet, liest die Spalten falsch zu. Deutsch richtig (Semikolon). | `csv_std_en.csv` (`g3_f_csv.js`, `g3_f_csvcheck.py`: „Kopffelder 6 Datenfelder 5“) | Feld in Anführungszeichen setzen oder umbenennen, zum Beispiel „model cup 2 (black until the milk) [°C]“ | CONFIRMED |
| G3-17 | low | Die CSV enthält nur Zeit, Modellkurven und Messwerte. Es fehlen die Bedingungen, ohne die eine Datei später nicht auswertbar ist: Raum- und Milchtemperatur des Messblatts, Deckel ja oder nein, *kA* mit Herkunft, Becher an oder aus, Mengen. Mit Becher 3 fehlt der Modellwert von Becher 3 nach der Milch (32,74 °C). Bei Zugabe vor 60 min steht die Zeile „56 nach der Milch“ hinter den leeren Zeilen 57 bis 60. | `csv_b3.csv`, `csv_tz56.csv`; KONZEPT.md M11 (Zweck Nachbereitung, K-5) | Bedingungen als eigene Spalten oder als zweiter Block mit Kopfzeile ausgeben; Spalte „Modell Becher 3“; Zeile „nach der Milch“ direkt hinter $t_\mathrm{Z}$ | CONFIRMED |
| G3-18 | low | Wertetabelle des Diagramms: Die Spalte „Tasse 2“ enthält bis 55 min den schwarzen Kaffee und in der letzten Zeile ohne Kennzeichnung den Wert nach der Milch (60 min: 30,19 °C); der Wert vor der Milch (33,86 °C) und damit der Mischsprung fehlen. CSV und Messblatt trennen „60 vor der Milch“ und „60 nach der Milch“. Becher 3 und der Vergleichslauf stehen nicht in der Tabelle (für Bildschirmleser fehlen sie damit ganz). | Standard und F1, Abschnitt 4a | Zwei Zeilen „60 vor der Milch“ und „60 nach der Milch“ wie in CSV und Messblatt; Spalte Becher 3, wenn gezeigt | CONFIRMED |
| G3-19 | low | Zugabezeit mit Nachkommastelle: Das Zahlenfeld nimmt 30,4 an (Tabelle der Regler: Schritt 1 min), gerechnet wird mit 30,4 min, angezeigt wird überall „nach 30 min“ (Rechenwerte, Beschreibung, Tabelle); bei 30,6 steht „nach 31 min“ bei Werten für 30,6 min. Die Wertetabelle hat dann zwei Zeilen „30“ mit verschiedenen Werten für Tasse 1 (46,62 und 46,40 °C); bei 7,5 min heißt die letzte Zeile „8“. | Eigene Werte: 30 min 46,6247 / 43,2669; 30,4 min 46,3986 / 43,0222; 30,6 min 46,2863 / 42,9008; 31 min 46,0632 / 42,6597; Anzeige bei 30,6: 46,29 / 42,90 „nach 31 min“ (`g3_f_t75.js`) | Eingabe auf ganze Minuten runden (wie der Regler) oder die Zeit mit einer Nachkommastelle anzeigen | CONFIRMED |
| G3-20 | low | Ansicht ln mit Becher 2 und 3: Die Gerade mit freiem Achsenabschnitt (0,4500 W/K) gewichtet den Startpunkt anders als bei einem Becher. Mit einem Becher gehen 7 Punkte ein (Start und 6 Messpunkte, 0,4495 W/K, wie am 05.11.2026 nachgerechnet); mit zwei Bechern ergibt sich 0,4500 W/K nur mit 13 Punkten, also dem Startpunkt einmal statt je Becher. Folgerichtig wären 14 Punkte: 0,4493 W/K. Die Abweichung (7 Einheiten der letzten Stelle) folgt aus der Wahl der Punkte, nicht aus einer falschen Rechnung; der Wert wird nur zum Vergleich gezeigt und nicht übernommen. Deshalb nicht blocker. Die Ursprungsgerade (0,4470 W/K) ist richtig. | `g3_f_ln3.js`; eigene Varianten 14 Punkte 0,44932 (Abschnitt +0,0056), 13 Punkte 0,45003 (+0,0073), 12 Punkte 0,45135 (+0,0104) | Startpunkt je Becher mitzählen (14 Punkte) oder im Text „Startpunkt einmal gezählt“ nennen | INFERRED (Wert CONFIRMED, Ursache aus der Nachrechnung erschlossen) |
| G3-21 | low | Der Vergleichslauf zeigt nur die blassen Abkühlkurven bis zur Zugabe, ohne Mischsprung von Tasse 2 und ohne Zahl. Die Größe, um die es geht (Unterschied nach der Zugabe, Standard 3,85 K gegen Deckel 3,51 K), kann man für den gemerkten Lauf nicht ablesen; Beschreibung und Tabelle nennen ihn nicht. Die Kurven selbst liegen richtig. | `g3_f_vergleich.js`, `vergleich.json`: blasse Linien enden bei 33,87 und 34,06 °C, kein blasser Sprung auf 30,19 °C | Blassen Mischsprung zeichnen und in den Rechenwerten eine Zeile „Vergleichslauf: 3,85 K (Standardwerte)“ | CONFIRMED |
| G3-22 | low | Im Kasten der *kA*-Voreinstellungen steht bei den Voreinstellungen mit Stern der Satz „* Richtwert, geschätzt, nicht gemessen.“ zweimal hintereinander (englisch „* estimate, not measured.“ ebenso). | Glas, Pappbecher, Edelstahl, Thermobecher, deutsch und englisch (`g3_f_en3.js`, `g3_f_de_preset.js`) | Satz einmal | CONFIRMED |
| G3-23 | low | *Bedienung, außerhalb der fachlichen Rolle:* (a) Wird der Kurslink in einem Tab geöffnet, in dem die Seite schon offen ist (nur der Teil hinter `#` ändert sich), passiert nichts und es erscheint keine Meldung; erst Neuladen fragt nach der Übernahme. (b) „Kurswerte als Link teilen“ erzeugt auch bei leerem Messblatt einen Link (`u:;m:;…;b2:,,,,,,,`) ohne Hinweis; wer ihn öffnet und „Übernehmen“ wählt, hat danach ein leeres Messblatt. | `g3_f_hash.js` (Felder danach leer, keine Meldung); `g3_f_csv.js`, `g3_f_ungueltig.js` | (a) auf die Änderung hinter `#` reagieren; (b) bei leerem Messblatt keinen Link erzeugen und das sagen | CONFIRMED |
| G3-24 | low | Englisch: Wird nach dem Öffnen eines Kurslinks auf EN umgeschaltet, bevor die Abfrage beantwortet ist, bleibt sie deutsch („Kurswerte aus dem Link übernehmen? … Übernehmen / Nicht übernehmen“); erst die Bestätigung erscheint englisch („Class data from the link used.“). | `g3_f_en.js`, `en_ui.txt` | Abfrage beim Sprachwechsel neu beschriften | CONFIRMED |

Zahl der Befunde: blocker 0, high 1 (G3-13, außerhalb der fachlichen Rolle, INFERRED), medium 5 (G3-01 bis G3-03, G3-14, G3-16), low 18 (G3-04 bis G3-12, G3-15, G3-17 bis G3-24). Davon am 06.11.2026 neu: medium 2, low 9.

## 6 Anhang: Skripte

Alle Skripte liegen in `/tmp/claude-0/-home-user-wue-tutorien/8bff1287-c5bb-5641-9916-90393029086f/scratchpad/gutachten_G3/`:

- `g3_rechnung.py`: eigene Rechnung der 30 Zustände (Gleichungen 2.1, ohne `kaffee_modell.py` und ohne Code der Seite), Ausgabe `g3_ergebnis.json`
- `g3_flaechen.py`: Teilflächen der Wärmestrom-Ansicht
- `g3_seite.js`: stellt die 30 Zustände in der Seite ein und liest die Anzeige, Ausgabe `g3_seite.json`
- `g3_maxscan.js`: Abtastung der Zugabe 1 bis 180 min in der Seite, Bewertung der Startvorhersage
- `g3_fragen.js`, `g3_vertiefung.js`: Fragen mit Vorhersage, Ausgangslage, Auflösung (deutsch und englisch)
- `g3_waermestrom.js`, `g3_messung.js`, `g3_reiter.js`, `g3_hilfe.js`, `g3_rest.js`: Wärmestrom, Bilanzraum, ungültige Einstellung, Becher kalt, Messreihe und Ausgleichsgerade, Reitertexte und Indizes, Hilfetexte

Fortsetzung 06.11.2026 (gleicher Ordner):

- `g3_f_rechnung.py`: eigene Werte für F1 (Becher 3), F2 (Deckel) und Standard je Minute bzw. je 5 min (nutzt `zustand` aus `g3_rechnung.py`)
- `g3_f_csvcheck.py`: jede Modellzeile der CSV gegen die eigene Rechnung, Zahl der Kopf- und Datenfelder
- `g3_f_lage.py`: Pixel der Kurven, Sprünge, Punkte und des Schnittkreises über die Achsenteilung in (*t*, $\vartheta$) zurückgerechnet und verglichen
- `g3_f_b3.js`, `g3_f_diag.js`, `g3_f_lage.js`, `g3_f_zoom.js`, `g3_f_ln3.js`: Messblatt mit Becher 3, Diagramm, Ansicht ln
- `g3_f_link.js`, `g3_f_ungueltig.js`, `g3_f_hash.js`, `g3_f_deckel.js`, `g3_f_deckel2.js`, `g3_f_finde.js`: Kurslink hin und zurück, ungültige Links, Deckel
- `g3_f_csv.js`, `g3_f_tabelle.js`, `g3_f_t75.js`, `g3_f_vergleich.js`: CSV und Herunterladen, Wertetabelle, Zugabe mit Nachkommastelle, Vergleichslauf
- `g3_f_en.js`, `g3_f_en2.js`, `g3_f_en3.js`, `g3_f_de_preset.js`: englische Oberfläche, Voreinstellungen, Feldgrenzen
- `g3_striche.py`: Suche nach Gedankenstrichen in diesem Gutachten

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
