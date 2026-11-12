# Aufarbeitung des Simulationscodes: Haltepunkt (12.11.2026)

> Nach `simulation/AUFTRAG_Aufarbeitung_Code.md`, Schritte 1 bis 4. Geprüfter Stand: `main` mit Merge von PR #17 (`3c2c0d2`). Am Code wurde nichts geändert; alle Prüfskripte und Ergebnisse liegen in `simulation/aufarbeitung/`. CONFIRMED heißt in dieser Sitzung selbst geprüft, INFERRED heißt aus Dokumenten geschlossen.
>
> **Vor Präsentation und Bericht brauche ich von der TL:** Rückmeldung zur Folienliste (Abschnitt 7) und zu den Befunden (Abschnitt 6), siehe Fragen in Abschnitt 8.

## 1 Kurz

| Frage | Antwort |
|:--|:--|
| Wie sieht der Code aus? | Eine einzige HTML-Datei (172 829 Bytes) ohne Abhängigkeiten. Gebaut aus einem Python-Modell (Quelle aller Zahlen), einem Rechenkern in JavaScript, eigenem Seitencode der schlanken Seite und 11 Bausteinen der Hauptseite. |
| Wie funktioniert er? | Jeder Regler ändert einen Zustand; daraus rechnet `modell()` geschlossene Formeln (Exponentialfunktionen), daraus entstehen Diagramm, Kasten, Säulen und eine Bildbeschreibung für Bildschirmleser. |
| Ist er valide? | **Rechnung: valide für den Zweck.** Alle Werte des Blatts unabhängig bestätigt; über 61 049 Einstellungen weicht die Seite von einer numerischen Lösung der Differentialgleichung höchstens 7·10⁻¹¹ K ab; 10 von 10 physikalischen Proben bestanden. **Seite als Ganzes: valide mit Einschränkungen**, weil in seltenen Extremeinstellungen das Bild falsch wird (A-01, A-02) und die neue Physik der schlanken Seite noch keine unabhängige Prüfung durch Codex hatte (A-03). |
| Wie wurde er gebaut? | In 9 Tagen (04. bis 12.11.2026), 108 Commits im Ordner `simulation/`, 13 Pull Requests, 5 Sites-Versionen. Die TL entscheidet, Claude baut, Codex prüft und veröffentlicht. |

## 2 Bestandsaufnahme (Schritt 1)

### Teile und Umfang (CONFIRMED, `wc -l`, `git log`)

| Teil | Dateien | Zeilen | Rolle |
|:--|:--|--:|:--|
| Modell des Blatts | `modell/kaffee_modell.py`, `modell/werte.py` | 134 + 223 | Rechnung der Aufgabe; gleich den Dateien des Blatts (diff leer) |
| Rechenkern im Browser | `site/src/modell.js` | 63 | gleiche Gleichungen wie `kaffee_modell.rechne`, Standardwerte des Blatts |
| Schlanke Seite (online) | `minimal/src/schlank.js`, `schlank.css`, `vorlage.html`, `texte_schlank_de.txt`, `texte_schlank_en.txt` | 333 + 59 + 55 + 77 + 77 | eigene Rechnung (Zeit bis 180 min, Tassenwärmer, Tasse), Diagramm, Kasten, Säulen, Abspielen, Regler |
| Bau der schlanken Seite | `minimal/bauen_minimal.py` | 137 | übernimmt `modell.js`, `stil.css`, Texte und 11 Bausteine (69 Zeilen) aus der Hauptseite |
| Hauptseite (bis Version 3 online) | `site/src/oberflaeche.js`, `stil.css`, `vorlage.html`, Texte, `site/bauen.py`, `zahlen.py`, `tex2mathml.py`, `schriften_teilen.py` | 624 + 198 + 155 + 673 + 224 + 69 + 158 + 98 | Seite mit Vorhersage, Fragen und Aufträgen |
| Vergleichswerte | `minimal/vergleichswerte.py`, `QUELLEN_Vergleichswerte.md` | 135 | Alltagsvergleiche für kA und Wärmekapazität, 13 Quellen |
| Tests | `tests/test_kern.py`, `test_texte.py`, `browsertest.js`, `minimal_test.js`, `bilder.js` | 167 + 97 + 349 + 106 + 70 | 214 Prüfungen zusammen |

### Bauweg (CONFIRMED, `aufarbeitung/a5_bau.sh`)

```
kaffee_modell.py, werte.py ──(gleiche Gleichungen, test_kern.py prüft)──> site/src/modell.js
site/src/modell.js, stil.css, texte_*.txt, 11 Bausteine aus oberflaeche.js ─┐
minimal/src/schlank.js, schlank.css, vorlage.html, texte_schlank_*.txt ─────┼─> bauen_minimal.py ─> Kaffee_Simulation_schlank.html
Schriften (IBM Plex, eingebettet), Formeln als MathML (tex2mathml.py) ──────┘      (eine Datei, CSP mit Prüfsummen)
                                                                                          │
                                                       Codex lädt sie unverändert als index.html zu Sites hoch (Version 5)
```

| Prüfung | Ergebnis |
|:--|:--|
| zwei Bauten in leere Ordner | bytegleich, SHA-256 `5ffb4424…c034` (schlank), `9a1f65d5…1d55` (Hauptseite) |
| Datei auf `main` gleich dem Bau | ja, beide |
| gleich der veröffentlichten Sites-Version 5 | ja, gleiche SHA-256 wie im Nachweis von Codex (Zweig `codex/kaffee-schlank-nachbesserung-veroeffentlichung`); Fuß „Stand 2026-11-12 · Version b5d8b9e52e“ |
| Abruf der Live-Seite aus dieser Umgebung | nicht möglich (Proxy 403); letzte Live-Abnahme durch Claude im Chrome der TL in der Nacht zum 12.11. nach der Veröffentlichung (Version b5d8b9e52e), INFERRED aus dem Verlauf dieser Sitzung, nicht im Repository dokumentiert (A-04) |
| Inhalt der Datei | Skript 69 405 Zeichen (davon Texte 38 003), Stil 99 907 Zeichen (davon Schriften 65 504) |

## 3 Wie er funktioniert (Schritt 2)

### Physik zu Code (CONFIRMED, Zeilen auf `3c2c0d2`)

| Gleichung (Blatt) | Python `kaffee_modell.py` | Hauptseite `modell.js` | Schlanke Seite `schlank.js` | Vorlesung |
|:--|:--|:--|:--|:--|
| Wärmekapazitäten $C_K = \rho_K V_K c_{p,K}$, $C_G = C_K + C_M$ | Z. 31 bis 35 | Z. 8 bis 12 | über `rechne`, Z. 64; mit Tasse $C_K + C_T$, $C_G + C_T$: Z. 65 | |
| kA aus der Messung nach 10 min | Z. 39 bis 40 | Z. 15 bis 16; Regler: Z. 47 (gleichwertiger Messwert) | Z. 63 (gleicher Kniff) | Vorlesung 05, Folie 29 ($\dot Q = kA\,\Delta T$) |
| Mischtemperatur $\vartheta_{1,0} = (C_K\vartheta_{K,0} + C_M\vartheta_M)/C_G$ | Z. 45, 47 | Z. 19 bis 20 | Z. 66; Tasse 2 bei der Zugabe Z. 70 | |
| Bilanz $C\,\mathrm{d}\vartheta/\mathrm{d}t = -kA(\vartheta - \vartheta_u) + \dot Q_W$ | | | | Vorlesung 05, Folie 8 ($\mathrm{d}U/\mathrm{d}t = \dot Q_{zu} - \dot Q_{ab}$) |
| Lösung $\vartheta = \vartheta_u + (\vartheta_0 - \vartheta_u)\,e^{-kA\,t/C}$ | Z. 48 bis 52 | Z. 21 bis 24 | Z. 69, 71 (mit Wärmer: Ziel $\vartheta_\infty = \vartheta_u + \dot Q_W/kA$, Z. 68) | gleichmäßige Temperatur wie bei $Bi \ll 1$: Vorlesung 02, Folie 16 |
| Tasse 2 nach der Zugabe kühlt mit $C_G$ weiter | | | Z. 72 | |
| abgegebene Wärme $Q_1 = C_G(\vartheta_{1,0} - \vartheta_1)$, $Q_2 = C_K(\vartheta_{K,0} - \vartheta_K)$ | Z. 56 bis 57 | Z. 27 bis 28 | Z. 74 bis 75, mit Wärmer $+\dot Q_W t$ | |
| $Q_2 - Q_1 = C_G(\vartheta_1 - \vartheta_2)$ | `werte.py` Z. 166 (Prüfung) | | folgt aus Z. 74 bis 75 (A3 prüft) | |
| Obergrenze Wärmer $\vartheta_u + \dot Q_W/kA \le 95\,°C$ | | | Z. 83 | |

### Datenfluss der schlanken Seite (CONFIRMED)

```
Regler bewegen ─> input-Ereignis (Z. 103) ─> setze() [Baustein] ─> begrenze() mit obergrenze() (Z. 81)
   ─> Zustand S.e ─> aktualisiere() (Z. 315): Zugabe ≤ t, Wärmer ≤ Obergrenze, angezeigte Zeit = t
   ─> reglerAnzeigen() (Z. 122): Schieber, Felder, Skalen, Band der Alltagsvergleiche
   ─> zeigen() (Z. 309) ─> modell(S.e) (Z. 61) ─┬─> zeichne() (Z. 179): Gitter, Kurven, Sprünge, Endpunkte, Bildbeschreibung
                                                ├─> kasten() (Z. 255): Werte bei der angezeigten Zeit
                                                └─> saeulenZeigen() (Z. 262) ─> saeulen() [Baustein]
Loslassen ─> ansage() (Z. 267): Satz für Bildschirmleser (aria-live)
Abspielen ─> requestAnimationFrame: angezeigte Zeit läuft von 0 bis t, Zukunft verdeckt (Z. 276 bis 297)
```

Hauptseite (kurz): gleicher Kern (`auswerten`), dazu ein Pflichtweg mit Vorhersage, Fragen und Aufträgen, Lernstand im lokalen Speicher des Browsers, ln-Diagramm und Messteil.

### Geplante Erklärkästen (je 2 bis 3 Minuten)

| Nr. | Stelle | Was man lernt |
|:--|:--|:--|
| 1 | `modell.js` Z. 43 bis 49, `schlank.js` Z. 63 | Der Kniff mit dem gleichwertigen Messwert: alter, geprüfter Code bleibt unverändert, neue Eingabe passt trotzdem |
| 2 | `schlank.js` Z. 68 bis 72 | Kurven als Funktionen (`t => …`), stückweise für Tasse 2 |
| 3 | `schlank.js` Z. 74 bis 75 | Wärme aus der Energiebilanz statt aus einem Integral |
| 4 | `schlank.js` Z. 45 bis 46 | Logarithmischer Regler in zwei Zeilen |
| 5 | `bauen_minimal.py` Z. 39 bis 50 | Code aus einer anderen Datei herausschneiden, und warum ein Kommentar am Zeilenende den Bau gebrochen hat |
| 6 | `bauen_minimal.py` Z. 111 bis 113 | Inhaltssicherheitsrichtlinie mit Prüfsummen: warum fremde Skripte nicht laufen |
| 7 | `bauen_minimal.py` Z. 75 bis 82 | Deterministischer Bau und Versionskennung im Fuß |
| 8 | `tests/minimal_test.js` Z. 39 bis 41 | Testen im echten Browser: Zahl ablesen, Bilanz prüfen |

## 4 Ist er valide? (Schritt 3, alle Skripte in `aufarbeitung/`, Ausgaben in `aufarbeitung/ergebnisse/`)

| Prüfung | Skript | Ergebnis | Beleg |
|:--|:--|:--|:--|
| Unabhängige Nachrechnung des Blatts | `a1_nachrechnung.py` (ohne `kaffee_modell.py`) | alle 10 Werte des Blatts gleich (kA 0,1994 W/K, 43,01 °C, 36,31 °C, 6,69 K, 15,50 kJ, 23,82 kJ, 8,31 kJ …); Formeln und numerische Lösung weichen 7·10⁻¹⁴ ab | CONFIRMED |
| Schlanke Seite gegen Differentialgleichung | `a2_vergleich.py` a) | 61 049 Einstellungen (alle Regler, Grenzen, 2 000 Zufallsfälle): höchstens 6,7·10⁻¹¹ K und 1,7·10⁻⁸ J | CONFIRMED |
| Schlanke Seite gegen `kaffee_modell.zwei_tassen` | a) b) | 8 316 Einstellungen: höchstens 9·10⁻¹³ K; 432 Einstellungen nicht vergleichbar, weil das Python-Modell abbricht (A-07) | CONFIRMED |
| Schlanke Seite gegen Hauptseite (Tasse 0, Wärmer 0, t = Zugabe) | a2 c) | 972 Einstellungen: höchstens 1·10⁻¹³ | CONFIRMED |
| Hauptseite gegen `kaffee_modell.rechne` | a2 d) | 972 Einstellungen: höchstens 1·10⁻¹³ | CONFIRMED |
| Physikalische Proben | `a3_physik.py` | 10 von 10: Energiebilanz, kein Sprung bei gleich warmer Milch (Tasse 1 und 2), Milch mit Raumtemperatur macht Tasse 1 wärmer, größeres kA kühlt schneller, Wärmer nie über 95 °C, alle Temperaturen im möglichen Bereich, genau ein Kipppunkt, Vergleichsbereiche lückenlos | CONFIRMED |
| Vorhandene Tests | alle | test_kern 34/34, test_texte 16/16, browsertest 107/107, minimal_test 57/57, vergleichswerte „Bereiche passen“ | CONFIRMED |
| Bedienung, Barrierefreiheit, Sicherheit | `a4_browser.js` | 14 von 15: Tastatur (40 Elemente, sinnvolle Reihenfolge, sichtbarer Fokus), Kontraste (Kurven 3,4 und 13,2), CSP blockiert eingeschleustes Skript, kein Speicher, keine Netzanfragen, reduzierte Bewegung, 320 px ohne Querscrollen, Beamer 1280 × 720 ohne Bildlauf. **Fehler: Kurve unter der Achse (A-01)** | CONFIRMED |
| Bau und Veröffentlichung | `a5_bau.sh` | deterministisch, gleich `main`, gleich Sites-Version 5 | CONFIRMED |

### Was die vorhandenen Tests prüfen und was nicht

| Test | prüft | prüft nicht |
|:--|:--|:--|
| `test_kern.py` (34) | Rechenkern der Hauptseite gegen Python, 2 000 Zufallsfälle, geschützter Block `rechne` per SHA-256, Standardwerte gleich `werte.py` | die Rechnung der schlanken Seite (Wärmer, Tasse, t > Zugabe) |
| `test_texte.py` (16) | Texte der Hauptseite: Kernsatz, keine Ergebnisse auf der Startkarte, Herkunft jeder Zahl, DE und EN | Texte der schlanken Seite (nur der Bau prüft Gedankenstriche, $ und gleiche Schlüssel) |
| `browsertest.js` (107) | Hauptseite in Chromium: Pflichtweg, Zustände, Layouts, axe-core, Leistung | schlanke Seite |
| `minimal_test.js` (57) | schlanke Seite an 8 Rechenpunkten, Grenzen der Regler, Abspielen, Vergleiche, EN, axe-core, CSP, Netz | Rastervergleich, Tastatur, Speicher, Extremeinstellungen (A-01, A-02) |
| `bilder.js` | Bildschirmfotos | kein Test |

### Grenzen des Modells (CONFIRMED aus Code und Blatt)

| Grenze | Wirkung | Wo sichtbar |
|:--|:--|:--|
| Werte vorläufig bis zur Messung im Januar 2027 (kA aus 72 °C nach 10 min, 80 °C Start) | alle Zahlen | Blatt und Hinweise; nicht auf der Seite (A-08) |
| keine Verdunstung, kA konstant | offene Tasse nur grob | Text `vgl_kA_5_text` vorhanden, bei Darstellung 3 nicht angezeigt (A-08) |
| Tasse immer so warm wie der Inhalt, im Blatt ohne Wärmekapazität | Unterschied im Modell eher größer als real | Regler „Wärmekapazität der Tasse“ zeigt die Wirkung |
| ideal durchmischt, gleiches kA für beide Tassen | | Blatt, Aufgabe 4 (Annahmen) |

## 5 Wie er gebaut wurde (Schritt 4)

### Zeitleiste (CONFIRMED aus `git log`, Pull Requests und Nachweisen)

| Datum | Schritt | Prüfung |
|:--|:--|:--|
| 31.10. | erstes Simulationstool zur Kaffee-Aufgabe (PR #4) | Codex X3 |
| 04.11. | Auftrag „Simulation als eigene Website“, Konzept mit Recherche R1 bis R3 | Codex X4 zum Konzept: 11 Befunde, „mit Änderungen“ |
| 05. bis 06.11. | Bau Fassung 2 (Pflichtweg mit Vorhersage, DE und EN) | Gutachten G1 bis G10 in 4 Runden (Runde 1: 189 Befunde, Runde 2: 60 neue); Codex X5: 11 Befunde; Korrekturrunde; X5N |
| 06.11. | PR #6, **Sites-Version 1**, Live-Abnahme | |
| 08.11. | Fassung 3, passend zum Blatt Fassung 3 (PR #8 bis #10), **Sites-Version 2** | Codex X6: 4 Befunde; Live-Abnahme |
| 09.11. | Regel R1: Veröffentlichungen immer öffentlich | |
| 10.11. | 100 ml Milch, 45 min, Sprünge gestrichelt (PR #13), **Sites-Version 3** | Live-Abnahme |
| 11.11. | Milch bis 95 °C (PR #14), schlanke Varianten, dann schlanke Seite im Stil der Hauptseite | Tests |
| 12.11. | Alltagsvergleiche (13 Quellen), Tassenwärmer, Band (PR #15), **Sites-Version 4** (00:47); Nachbesserung niedrige Fenster (PR #16), **Sites-Version 5** (01:00) | Live-Abnahme Version 4; Codex: Tests und Anordnung (fand 15 px bei 1280 × 720) |

### Kennzahlen (CONFIRMED)

| Größe | Wert |
|:--|:--|
| Commits im Ordner `simulation/` | 108 (99 Claude, 6 Codex, 3 TL); 54 davon am 06.11. |
| Pull Requests zur Simulation | 13 (#4, #6 bis #17) |
| Sites-Versionen unter der Hauptadresse | 5 |
| Prüfungen durch Codex | X3, X4, X5, X5N, X6 sowie Prüfungen bei jeder Veröffentlichung |
| Tests | 214 Prüfungen in 4 Testdateien, dazu 29 in dieser Aufarbeitung |

### Lehren (Entwurf)

| gut | weniger gut |
|:--|:--|
| Eine Quelle für alle Zahlen (`kaffee_modell.py`), der geprüfte Rechenblock ist per Prüfsumme geschützt | Je schneller die Runden (11. und 12.11.), desto weniger unabhängige Prüfung (A-03) |
| Unabhängige Prüfungen fanden echte Fehler (X4: Energieerklärung bei Milch mit Raumtemperatur; X6: Neustart; Codex: 15 px am Beamer) | PR #14 gemergt, bevor alle Commits drin waren; PR #15 musste nachziehen |
| Eine Datei ohne Netz, ohne Speicher, mit CSP: datenschutzfreundlich und robust | Erste schlanke Varianten im eigenen Design statt im Stil der Hauptseite, neu gebaut |
| Bau reproduzierbar bis aufs Byte, Veröffentlichung belegbar | Nachweise von Codex auf eigenen Zweigen, nicht auf `main` (A-04) |
| Die TL entscheidet jede Gestaltungsfrage, mit Varianten zur Wahl | Viele Begleitdokumente (Konzept 585 Zeilen), Aufwand für Leser groß |

## 6 Befunde

| ID | Schwere | Befund | Beleg | Vorschlag | |
|:--|:--|:--|:--|:--|:--|
| A-01 | medium | Kurven, Sprungpfeil und Endpunkt können unter die untere Achse rutschen. Die Untergrenze des Diagramms hängt nur von der Raumtemperatur ab; die Hauptseite nimmt auch die Kurvenwerte hinein. Tritt auf, wenn viel kalte Milch auf wenig Kaffee trifft (zum Beispiel 50 ml Kaffee, 200 ml Milch mit 2 °C, Raum 20 °C, 180 min: Tasse 2 bei 5,69 °C, Achse bei 10 °C). | `schlank.js` Z. 189 gegen `oberflaeche.js` Z. 228; `a4_browser.js` (tiefster Punkt 20 px unter der Achse); `bilder/fall_kurve_unter_achse.png`; 37 von 4 860 Rasterfällen | Untergrenze wie auf der Hauptseite aus den Kurvenwerten bilden, Test aus `a4_browser.js` übernehmen | CONFIRMED |
| A-02 | low | Ist die Mischung kälter als der Raum, nimmt Tasse 1 Wärme aus dem Raum auf. Die Säule „abgegebene Wärme“ zeigt dann −2,97 kJ bei Höhe 0, die Klammer Q₂ − Q₁ = 8,76 kJ reicht nur über 5,79 kJ. Physik richtig, Bild missverständlich. | `a4_browser.js`, `bilder/fall_mischung_kaelter_als_raum.png`; 70 von 4 860 Rasterfällen (`a3_physik.py`) | Säulen mit Nulllinie nach unten zeichnen, oder so lassen (nur in Extremeinstellungen) | CONFIRMED |
| A-03 | medium | Die neue Physik der schlanken Seite (Tassenwärmer, Wärmekapazität der Tasse, Abkühlung nach der Zugabe, Zeit bis 180 min) hatte keine unabhängige Prüfung durch Codex. X4 bis X6 galten der Hauptseite; bei Version 4 und 5 hat Codex die vorhandenen Tests ausgeführt und die Anordnung geprüft. Diese Aufarbeitung rechnet unabhängig vom Code, stammt aber von der bauenden Rolle. Der Fuß sagt „geprüft durch Codex“. | Nachweis Codex Version 5 („57 von 57 Browsertests“); `site/src/texte_de.txt` Z. 334 | kurze Gegenprüfung durch Codex mit eigener Rechnung; Auftragstext bereite ich vor | CONFIRMED |
| A-04 | low | Nachweise der Sites-Versionen 3, 4 und 5 liegen nur auf Codex-Zweigen; die Live-Abnahme von Version 5 steht nicht in `LIVE_ABNAHME.md`. | `git show origin/codex/kaffee-schlank-nachbesserung-veroeffentlichung:…`; `LIVE_ABNAHME.md` endet bei Version 4 | Codex-Zweig per Pull Request übernehmen, Live-Abnahme Version 5 nachtragen | CONFIRMED |
| A-05 | low | Keine automatische Prüfung bei Pull Requests (kein `.github/workflows`). Tests laufen nur, wenn Claude oder Codex sie starten. | `ls .github` leer | GitHub Action mit `test_kern.py`, `minimal_test.js`, `--pruefen` beider Bauten | CONFIRMED |
| A-06 | low | Die Versionskennung im Fuß der schlanken Seite hängt nicht von `bauen.py`, `tex2mathml.py`, `zahlen.py` und den Schriften ab (anders als bei der Hauptseite). Ändert sich nur dort etwas, ändert sich die Seite, die Kennung aber nicht. | `bauen_minimal.py` Z. 75 bis 82 gegen `bauen.py` Z. 125 bis 136 | Liste der Hauptseite übernehmen | CONFIRMED |
| A-07 | low | `kaffee_modell.rechne` bricht ab, wenn die Mischung kälter als der Raum ist (Logarithmus in `t_schnitt`). Für das Blatt ohne Folgen; die Python-Referenz deckt diese Einstellungen der Seite nicht ab. | `kaffee_modell.py` Z. 62; `a2_vergleich.py` b) (432 Fälle) | so lassen (Modell des Blatts ist geschützt); in Tests die numerische Lösung nutzen | CONFIRMED |
| A-08 | low | Die Grenzen des Modells (vorläufige Werte, keine Verdunstung) stehen nicht auf der schlanken Seite; der vorhandene Satz zur offenen Tasse wird bei Darstellung 3 nicht angezeigt. | `texte_schlank_de.txt` Z. 65; `schlank.js` Z. 129 bis 134 | Entscheidung TL: so lassen (Blatt und Hinweise tragen es) oder eine Zeile im Fuß | CONFIRMED |
| A-09 | low | Skala des Tassenwärmers: Liegt die Obergrenze knapp über 10 W (zum Beispiel 12,5 W bei Raum 30 °C), stehen „10“ und „12,5“ fast aneinander. | `bilder/fall_mischung_kaelter_als_raum.png`; `schlank.js` Z. 158 bis 160 | Endmarke nur bei genug Abstand, sonst letzte Marke ersetzen | CONFIRMED |
| A-10 | low | `minimal_test.js` prüft die Rechnung nur an 8 Punkten; `browsertest_ergebnis.txt` ändert sich bei jedem Lauf (Zeitmessung). | `tests/minimal_test.js`; `git diff` nach dem Lauf | `a2`, `a3`, `a4` als dauerhafte Tests übernehmen; Zeiten nicht in die Ergebnisdatei | CONFIRMED |

**Empfehlung:** A-01 beheben (klein, ein Pull Request mit Test), A-03 mit einer Gegenprüfung durch Codex schließen, A-04 mit erledigen. Alles andere kann warten oder bleiben. Nach A-01 und A-03 lautet das Urteil „valide für den Zweck“.

## 7 Folienliste (Vorschlag, 17 Folien)

| Nr. | Titel | Inhalt |
|:--|:--|:--|
| 1 | Kaffee mit Milch: Wie die Simulation gebaut ist und ob sie stimmt | Bildschirmfoto, QR-Adresse |
| 2 | Die Frage | Milch sofort oder später? Was die Seite zeigt (Kasten, Kurven, Säulen) |
| 3 | Überblick in Zahlen | eine Datei, 172 kB, 0 Netzanfragen; 108 Commits, 13 Pull Requests, 5 Versionen, 214 Tests |
| 4 | Aufbau | Bild: Python-Modell, Rechenkern, Seitencode, Bausteine, Bau, eine Datei, Sites |
| 5 | Physik zu Code | Tabelle Gleichung, Zeile, Vorlesung |
| 6 | Das Herz: `modell()` | 15 Zeilen Code mit Markierungen |
| 7 | Vom Regler bis zum Pixel | Bild Datenfluss |
| 8 | Bau: aus vielen Dateien wird eine | Schriften, MathML, CSP mit Prüfsummen, zweimal bauen ergibt gleiche Bytes |
| 9 | Stimmt die Rechnung? | Blattwerte unabhängig; 61 049 Einstellungen gegen die Differentialgleichung, Abweichung 7·10⁻¹¹ K |
| 10 | Stimmt die Physik? | 10 Proben mit Ergebnis |
| 11 | Was wir gefunden haben | A-01 und A-02 mit Bild |
| 12 | Grenzen des Modells | vorläufige Werte, Verdunstung, Tasse, kA konstant |
| 13 | Entstehung | Zeitleiste 31.10. bis 12.11. |
| 14 | Mensch und KI | Rollen: TL entscheidet, Claude baut, Codex prüft und veröffentlicht; Gutachterrollen |
| 15 | Prüfen lohnt sich | Was X4, X5, X6, Gutachten und Live-Abnahmen gefunden haben |
| 16 | Lehren | gut und weniger gut |
| 17 | Ausblick | Messung im Januar, A-01, Gegenprüfung, automatische Tests |

Bericht: dieselben Abschnitte wie dieser Haltepunkt, ausführlicher, mit den 8 Erklärkästen und allen Belegen; Anhang mit Befunden und Skriptausgaben.

## 8 Fragen an die TL

| Nr. | Frage | Empfehlung |
|:--|:--|:--|
| 1 | Folienliste so? Publikum gemischt (Tutorien, Lehrstuhl, Hochschuldidaktik) oder zwei Fassungen? | eine Fassung mit 17 Folien; Code nur auf Folie 6 und 8 |
| 2 | A-01 vor der Präsentation beheben (eigener Pull Request, neue Veröffentlichung)? | ja, dann zeigt Folie 11 „gefunden und behoben“ |
| 3 | Gegenprüfung durch Codex (A-03)? | ja; ich schreibe den Auftrag, du startest ihn |
| 4 | Bericht als Claude-Dokument (Docs) und Präsentation als Folien (Slides)? | ja, beide als Artefakt, als PDF und PowerPoint exportierbar |
