# Gutachten G3: Fachgutachter Wärmeübertragung

| | |
|:--|:--|
| Rolle | G3 „Fachgutachter Wärmeübertragung“ |
| Datum | 05.11.2026 |
| Art | getrennte Rollenprüfung desselben Modells (eine unabhängige Prüfung mit einem anderen Modell folgt) |
| Gegenstand | `simulation/site/index.html` |
| SHA-256 | `f519052cadf6745eeeb4eb97f5a0042c74688f3495cada09c059970b25016707` (369 081 Byte) |
| Umgebung | Linux-Container der Cloud-Sitzung, Node v22.23.4, Playwright mit Chromium (`chromium.launch()` ohne Optionen), Python 3.13.18 |
| Maßstab | `simulation/KONZEPT.md` Fassung 2 (Abschnitte 6, 8, Anhang A, C); Aufgabe und Lösung in der **fertigen Fassung vom 31.10.2026** (`ergebnisse/kaffee/fertig/`, dort Teil f = erwärmte Milch $\vartheta_\mathrm{M,h}$ = 60 °C, Teil g = vorgewärmter Keramikbecher); Versuch für die Website 60 min (E8) |

Nicht gelesen: Code der Seite (Skript in `index.html`, `simulation/site/src/`, `simulation/modell/kaffee_erweitert.py`), `BAU_BERICHT.md`, `PROTOTYPEN.md`, `ZUSTAENDE.md`, `tests/`, `recherche/`, andere Gutachten, Git-Protokoll.

## 2 Eigene Gleichungen und Prüffälle (vor dem Blick auf die Seite festgelegt)

*Festgelegt und gerechnet am 05.11.2026 vor dem ersten Öffnen der Seite. Ein Hinweis der Koordination (Maßstab ist die fertige Fassung vom 31.10.2026) kam während dieser Phase; er ändert keine Zahl, nur die Teilbezüge (erwärmte Milch Teil f, Becher Teil g).*

### 2.1 Gleichungen

Bezeichnungen wie Aufgabe und Vorlesung; Wärmekapazitäten $C_\mathrm{K} = \rho_\mathrm{K} V_\mathrm{K} c_{p,\mathrm{K}}$, $C_\mathrm{M} = \rho_\mathrm{M} V_\mathrm{M} c_{p,\mathrm{M}}$, Becher $C_\mathrm{B} = m_\mathrm{B} c_\mathrm{B}$ (aus: 0), $C_\mathrm{KB} = C_\mathrm{K} + C_\mathrm{B}$, $C_\mathrm{GB} = C_\mathrm{KB} + C_\mathrm{M}$. *kA* von Tasse 1 ist $f_1\,kA$.

1. *kA* aus der Messung (Teil c, mit Becher Teil g): $kA = -\dfrac{C_\mathrm{KB}}{600\,\mathrm{s}}\ln\dfrac{\vartheta_\mathrm{mess} - \vartheta_\mathrm{u}}{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}$. Standard ungerundet $kA_0 = 0{,}340246$ W/K.
2. Mischen (Teil a, Becher vorgewärmt): $\vartheta_{1,0} = (C_\mathrm{KB}\vartheta_\mathrm{K,0} + C_\mathrm{M}\vartheta_\mathrm{M1})/C_\mathrm{GB}$.
3. Abkühlen (Teil b): Tasse 1 $\vartheta_1(t) = \vartheta_\mathrm{u} + (\vartheta_{1,0} - \vartheta_\mathrm{u})\exp(-f_1 kA\,t/C_\mathrm{GB})$; schwarzer Kaffee $\vartheta_\mathrm{2,K}(t) = \vartheta_\mathrm{u} + (\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})\exp(-kA\,t/C_\mathrm{KB})$.
4. Zugabe bei $t_\mathrm{Z}$: $\vartheta_2 = (C_\mathrm{KB}\vartheta_\mathrm{2,K}(t_\mathrm{Z}) + C_\mathrm{M}\vartheta_\mathrm{M2})/C_\mathrm{GB}$ mit $\vartheta_\mathrm{M2} = \vartheta_\mathrm{M}$ oder $\vartheta_\mathrm{u}$ (Schalter „Milch für Tasse 2 bei Raumtemperatur“).
5. Abgegebene Wärme bis zur Zugabe (Teil e): $Q_1 = C_\mathrm{GB}(\vartheta_{1,0} - \vartheta_1)$, $Q_2 = C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{2,K})$; Bilanz $C_\mathrm{GB}(\vartheta_1 - \vartheta_2) = Q_2 - Q_1 + C_\mathrm{M}(\vartheta_\mathrm{M1} - \vartheta_\mathrm{M2})$ (selbst hergeleitet aus 2 bis 5; Rest im Skript < 1e−13 kJ).
6. Schnittpunkt: $t_\mathrm{s} = \ln\dfrac{\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u}}{\vartheta_{1,0} - \vartheta_\mathrm{u}} \Big/ \left(\dfrac{kA}{C_\mathrm{KB}} - \dfrac{f_1 kA}{C_\mathrm{GB}}\right)$.
7. Größter Unterschied über $t_\mathrm{Z}$: $\dfrac{\mathrm{d}(\vartheta_1 - \vartheta_2)}{\mathrm{d}t_\mathrm{Z}} = \dfrac{kA(\vartheta_\mathrm{2,K} - \vartheta_\mathrm{u}) - f_1 kA(\vartheta_1 - \vartheta_\mathrm{u})}{C_\mathrm{GB}}$, also Maximum bei gleichen Wärmeströmen; nur bei $f_1 = 1$ ist das der Schnittpunkt, dann $\Delta_\mathrm{max} = C_\mathrm{M}(\vartheta_\mathrm{x} - \vartheta_\mathrm{M})/C_\mathrm{GB}$ unabhängig von *kA*. Im Skript zusätzlich durch Abtasten in 1-s-Schritten bestimmt.
8. Kipp-Milchtemperatur (Zusatzfrage (1), V1): $\vartheta_\mathrm{M} = \vartheta_\mathrm{u} + \dfrac{C_\mathrm{KB}(\vartheta_\mathrm{K,0} - \vartheta_\mathrm{u})(e_\mathrm{G} - e_\mathrm{K})}{C_\mathrm{M}(1 - e_\mathrm{G})}$.
9. Becher kalt (M9, nur *kA* fest): $\vartheta_\mathrm{2,K}(0) = (C_\mathrm{K}\vartheta_\mathrm{K,0} + C_\mathrm{B}\vartheta_\mathrm{u})/C_\mathrm{KB}$, $\vartheta_{1,0} = (C_\mathrm{K}\vartheta_\mathrm{K,0} + C_\mathrm{M}\vartheta_\mathrm{M} + C_\mathrm{B}\vartheta_\mathrm{u})/C_\mathrm{GB}$; *Q* ab diesem Ausgleich (der Austausch mit dem Becher liegt im Bilanzraum).
10. Trinkzeit (M10): $t_\mathrm{T} = \dfrac{C}{kA}\ln\dfrac{\vartheta_0 - \vartheta_\mathrm{u}}{\vartheta_\mathrm{T} - \vartheta_\mathrm{u}}$ für Tasse 1 ($C_\mathrm{GB}$, $\vartheta_{1,0}$) und den schwarzen Kaffee ($C_\mathrm{KB}$, $\vartheta_\mathrm{K,0}$).
11. Anzeige „von … auf … °C in 30 min“: $\vartheta_\mathrm{2,K}(30\,\mathrm{min})$, Zeitkonstante $C_\mathrm{KB}/kA$.

### 2.2 Prüffälle (30 Zustände)

Standardwerte, wenn nicht anders gesagt: 200 ml, 80 °C, 30 ml, 5 °C, 20 °C, Zugabe 60 min, *kA* fest $kA_0$, ohne Becher. Voreinstellungen als Faktor × $kA_0$ (Tabelle 8.2.1). Begründung je Fall: Z01 bis Z02 Aufgabe d/e; Z03 bis Z06 Frage 1 (Zeitpunkt, Maximum, Abfall); Z07 bis Z10 Milchtemperatur (Lösung „Zum Weiterdenken“, Pflichttest M3, Teil f, Zusatzfrage); Z11 bis Z21 Konzept 8.5 (Volumina, Temperaturen, *kA* fest gegen aus der Messung, Grenzen); Z22 bis Z23 Teil g und typischer Fehler; Z24 V4 und M-22; Z25 bis Z28 Tabelle 8.2.1; Z29 M9; Z30 M10.

### 2.3 Fehlerschwelle (vorab festgelegt)

- Angezeigt werden laut Anhang A.2 Temperaturen auf 0,01 K und Wärmen auf 0,01 kJ. Übereinstimmung: angezeigter Wert gleich meinem Wert, gerundet auf die angezeigten Stellen.
- Abweichung um genau eine Einheit der letzten Stelle gilt **nicht** als Fehler, wenn mein ungerundeter Wert höchstens 0,0015 von einer Rundungsgrenze entfernt liegt oder wenn die Seite erkennbar mit *kA* = 0,3402 W/K (gerundet) statt $kA_0$ rechnet (Rundungsvariante; dann Befund „low“, falls dadurch ein Wert der Aufgabe abweicht).
- Jede andere Abweichung, und jede ab zwei Einheiten der letzten Stelle, ist ein Fehler (Schwere „blocker“, falsche Zahl).
- Zeiten in min: Abweichung ab 0,2 min ist ein Fehler. *kA*: vier Nachkommastellen, gleiche Regel wie oben.
- Zahlen in Auflösungstexten werden gegen meine Werte in der Genauigkeit des Textes geprüft.
