# Prüfbericht B: Tutorium 4 (Strahlung) und Tutorium 5 (Wärmebilanzen, instationär global)

Stand 21.10.2026. Geprüft nach `pruefung/PRUEFAUFTRAG.md` und `SPEZ.md`. Tutorium 5 wurde wie in `build/sammlung_bauen.py` zusammengesetzt (Kaffee, Fragen an der Markierung, Ozean) und als Ganzes gebaut. Prüfbilder, eigene Nachrechnung und Rundungskette liegen im Scratch-Ordner `pruefung_B/` (Dateien `nachrechnung_B.py`, `rundungskette_B.py` mit Ausgaben, Seitenbilder in `bilder/`).

## 1. Erledigte Korrekturen

| Nr. | Datei, Stelle | vorher | nachher | Grund |
|:---|:---|:---|:---|:---|
| 1 | `teile/t4.md`, Aufgabe 1, Ergebniszeile d | „…; Zu (2): …“ | „…; zu (2): …“ | Kleinschreibung nach Semikolon, wie in Tutorium 5 und 8 |
| 2 | `teile/t4.md`, Aufgabe 1, Ergebniszeile g | „…; Zu (2): …“ | „…; zu (2): …“ | wie Nr. 1 |
| 3 | `teile/t4.md`, Satz unter der Tabelle | „Die Stefan-Boltzmann-Konstante beträgt σ = …“ | „Die Stefan-Boltzmann-Konstante σ = … ist hier gegeben (nicht in der Formelsammlung).“ | SPEZ 4.1: σ steht nicht in der Formelsammlung; gleicher Satz wie in Tutorium 5 |
| 4 | `teile/t4.md`, Tabelle „Gegebene Größen“ | „Mittlere Temperatur:“, „Wärme aus dem Erdinneren:“, Gruppenkopf „Verdopplung von CO₂:“ | „Mitteltemperatur:“, „Erdwärme:“, Gruppenkopf „CO₂ verdoppelt:“ | brachen im PDF zweizeilig um, der Gruppenkopf ebenfalls (Prüfauftrag G, SPEZ 4.1 „kurze Bezeichnungen“). Folge: Teil a bis c passen jetzt auf Seite 2 |
| 5 | `skripte/abb_t4_erde.py`, `grafik/t4_erde.png` und `.svg` | kein Hinweis | „nicht maßstäblich“ unten links, Grafik neu erzeugt | Atmosphärenschicht ist stark überhöht gezeichnet (Prüfauftrag C), wie bei den Skizzen in Tutorium 5 |
| 6 | `rechnung/t5_kaffee_teil.py`, daraus `teile/t5a_kaffee.md`, Teil h (1) | „Ab welcher Milchtemperatur ist es egal, …“ | „Bei welcher Milchtemperatur ist es egal, …“ | Gleichstand gilt nur bei 47,0 °C; darüber ist Tasse 2 wärmer. „Ab welcher“ behauptet eine Schwelle, ab der es egal ist. Skript neu laufen lassen, Zahlen unverändert |
| 7 | `teile/t5_fragen.md`, Frage 3 (6 Zeilen) | `- $\square$ …` | `- [ ] …` | wurde als Aufzählungspunkt plus Kästchen gesetzt; jetzt nur Kästchen wie in Tutorium 3 und 4 |
| 8 | `skripte/abb_t5_kaffee.py` | Standardausgabe `.`, Docstring „abb_kaffee.py“ | Standardausgabe `../grafik`, Docstring „abb_t5_kaffee.py“ | `cd skripte && python3 abb_t5_kaffee.py` schrieb sonst nach `skripte/`. Grafik neu erzeugt, pixelgleich zur bisherigen |
| 9 | `rechnung/t4_rechnung.py`, `rechnung/t4_rechnung_ausgabe.txt` | Tabellenwerte fehlten in der Ausgabe, kein Abgleich mit dem Blatt | Abschnitt „Tabellenwerte“, Hilfswerte als „nur Info“ markiert, Abgleich aller Anzeigen mit `teile/t4.md` (Abbruch bei Fehlen) | SPEZ 3 und 6 (jede Zahl der Tabellen in der Ausgabe); alle Rechenwerte unverändert, Abgleich besteht |
| 10 | `quellen/t5_quellen.md`, Eintrag „Flächen zwischen 40° und 70° N“ | ohne Hinweis auf Rundung | Ergänzt: Skript rechnet mit 7,572·10¹³ und 1,893·10¹³ m², die Aufgabe mit den gerundeten Flächen der Tabelle (63,2 statt 63,4 W/m², 21,9 statt rund 22 K, −12,6 statt −12,7 W/m²) | macht den bekannten Punkt „Flächenrundung“ nachvollziehbar |

Keine Zahl in Ergebniszeilen oder Tabellen musste geändert werden. Alle Skripte laufen: `t4_rechnung.py` (Abgleich besteht), `t5_rechnung.py` („alle Anzeigen gefunden“), `t5_kaffee_teil.py` (Ausgabe unverändert), alle fünf Skizzenskripte (Tutorium 5 pixelgleich).

## 2. Offene Entscheidungen

1. **Kaffee h (2): Begründung „ohne Rechnung“ trägt nicht, Musterlösung nennt eine falsche Zahl.** *(Aufgabentext umgesetzt, siehe Abschnitt 5; Musterlösung korrigiert die Koordination.)*
   *Befund:* Die Lösung (`/home/claude/work/kaffee/Kaffee_Loesung.md`, Teil h, außerhalb meines Teils) sagt: „Dann fällt der Milch-Effekt weg, aber der Kaffee-Effekt bleibt: Tasse 2 ist immer noch um 2,48 K kühler.“ Das gilt nur, wenn **beide** Tassen Milch mit Raumtemperatur bekämen. In h (2) bekommt Tasse 1 aber weiter Milch mit 5 °C. Mit Milch von höchstens 20 °C in Tasse 2: ϑ₁ = 34,05 °C, ϑ₂ = 32,10 °C, Tasse 2 also um **mindestens 1,95 K** kühler; gleich warm wäre sie erst mit 35,3 °C warmer Milch. Der Kipppunkt aus h (1) allein entscheidet die Frage nicht, weil er für gleich warme Milch in beiden Tassen gilt.
   *Folgen:* Die Antwort „Nein“ stimmt, aber die erwartete Begründung ist ein Fehlschluss, und Studierende können „ohne Rechnung“ nicht sauber begründen.
   **Empfehlung:** Im Aufgabentext „Begründen Sie ohne Rechnung.“ ersetzen durch „Begründen Sie mit einer Abschätzung und den Ergebnissen aus e).“ In der Lösung schreiben: „Nein. Die Milch kann aus der Raumluft höchstens m_M c_p,M · 15 K = 1,83 kJ aufnehmen, Tasse 2 hat nach e) aber 3,69 kJ mehr abgegeben. Sie bleibt um mindestens (3,69 − 1,83) kJ / 957,7 J/K = 1,95 K kühler.“

2. **Zwei Himmelstemperaturen in Tutorium 4 (Zusatzaufgaben).** *(Umgesetzt, siehe Abschnitt 5.)*
   *Befund:* „Eis aus der Nacht“: klarer Himmel −20 °C bei 5 °C Luft. „Autoscheibe“: Himmel −5 °C; Frage 2 spricht von einer „klaren Nacht“, und Zusatzaufgabe 2 beginnt mit „Rechnen Sie Frage 2 nach“. Für Studierende sind das zwei klare Nächte mit 15 K Unterschied ohne Erklärung. Physikalisch passt −20 °C zu einer klaren Nacht (Faustformel nach Swinbank etwa −18 °C bei 4 °C Luft); die −5 °C stammen aus V08 Teil g (Solarpanel am Tag bei 20 °C Luft). Mit −20 °C läge die Vereisungsgrenze der Scheibe bei 15,7 °C Luft, also unrealistisch.
   *Folgen:* aufmerksame Studierende sehen einen Widerspruch; die Zahlen selbst sind brauchbar.
   **Empfehlung:** In Zusatzaufgabe 2 den Halbsatz „tauscht Strahlung mit dem Himmel aus, der für die Strahlung wie ein schwarzer Körper mit ϑ_H = −5 °C wirkt“ ersetzen durch „tauscht Strahlung mit ihrer Umgebung aus. Die schräge Scheibe sieht neben dem klaren Himmel auch Häuser und Bäume; zusammen wirkt diese Umgebung für die Strahlung wie ein schwarzer Körper mit ϑ_H = −5 °C.“ Werte und Ergebnisse bleiben; Teil c behält seinen Sinn.

3. **Gegenstrahlung 152 W/m² im Modell gegen 342 W/m² gemessen (Tutorium 4, Teil g).** *(Umgesetzt, siehe Abschnitt 5.)*
   *Befund:* Physikalisch widerspruchsfrei, und die Lücke ist mit den gegebenen Zahlen vollständig erklärbar: 342 − 152 = 190 W/m² ≈ 80 (Sonne, die im Modell an der Oberfläche statt in der Atmosphäre ankommt) + 103 (Konvektion und Verdunstung) + 8 (398 statt 390 W/m²) = 191 W/m². Der Auftrag „vergleichen Sie“ fordert diese Erklärung aber nicht ausdrücklich, und „Gegenstrahlung“ kommt im Foliensatz V04 nicht vor.
   *Folgen:* Die gewollte Modellkritik kann als „ich habe falsch gerechnet“ ankommen.
   **Empfehlung:** „eine Gegenstrahlung (Wärmestrahlung der Atmosphäre zur Oberfläche) von 342 W/m²“ schreiben und nach „und vergleichen Sie“ ergänzen: „Erklären Sie den Unterschied mit einer Energiebilanz der Oberfläche aus den Messwerten.“

4. **Tiefgang des Eisbergs 220 m (Tutorium 5, Zusatzaufgabe 2).** *(Umgesetzt, siehe Abschnitt 5.)*
   *Befund:* Text, Skript und Quellen stimmen überein (220 m = 0,88 · 250 m aus `nachrechnung_leitphaenomene.py`). Nach Auftrieb mit ρ_E = 917 kg/m³ (in derselben Zusatzaufgabe gegeben) und Meerwasser 1025 kg/m³ (Aufgabe 2 und 3) ergeben sich 223,7 m.
   *Folgen:* Wer mit Archimedes nachprüft, findet 224 m; die Ergebnisse ändern sich nur in der letzten Stelle.
   **Empfehlung:** h_T = 224 m setzen (Skript `T_G`, Text, Quellen „aus dem Auftrieb mit 917 und 1025 kg/m³“). Dann A = 1,90·10⁶ m², Q̇ = 75,8 bis 284 MW, t = 31,9 bzw. 8,5 Jahre.

5. **Versuch zu Aufgabe 1.** *(Umgesetzt, siehe Abschnitt 5.)*
   *Befund:* (a) Schritt 4 verlangt die Vorhersage für Becher 3, dessen Milchtemperatur erst in Schritt 5 (t = 60 min) gemessen wird. (b) Die Becher werden vorgewärmt, das passt zu Teil f; Schritt 3 verweist auf Teil c. Erwartung mit Bechern (Modell f): Becher 1 gegen 2: 3,08 K; Becher 1 gegen 3: mindestens 1,57 K (Milch höchstens 20 °C).
   *Folgen:* Vorhersage für Becher 3 ist ohne Zusatzannahme nicht möglich; Vorhersage für Becher 2 mit Teil c liegt etwa 0,8 K unter dem Bechermodell.
   **Empfehlung:** Schritt 3: „… und daraus kA wie in Teil f (mit Becher) bestimmen.“ Schritt 4: „… vorhersagen; für Becher 3 mit Milch bei Raumtemperatur.“

6. **Überleitungssatz von Aufgabe 3** („Dasselbe Modell steckt in den letzten Teilen von Aufgabe 2 (g und h); die beiden Aufgaben können einander ersetzen.“).
   *Befund:* Hinweis an die Tutoriumsleitung, kein Text für Studierende.
   **Empfehlung:** In der Sammlung zur Auswahl stehen lassen, im Blatt für die Studierenden streichen.

7. **Linearisierung 4σT_e³ (Tutorium 4 h, Tutorium 5 Aufgabe 3 f).**
   *Befund:* Werte und Verweise stimmen: T_e = 254,6 K (T4 d), ε_A = 0,78 (T4 f), 4σT_e³ = 3,74 W/(m² K) und ΔT = 1,05 K (T4 h = T5 Aufgabe 3 f), Schichtmodellformel in T5 Aufgabe 2 d wie T4 f. Physikalisch beschreibt 4σT_e³ die Änderung der Emissionstemperatur; für die Oberfläche im Schichtmodell gälte 4σT_O³(1 − ε_A/2) = 3,31 W/(m² K) und ΔT = 1,19 K (nahe der Planck-Antwort von rund 1,2 K nach Forster et al.). Genau diese Form nutzt T5 Aufgabe 2 g. Der Name „Emissionstemperatur“ kommt in Tutorium 4 nicht vor (dort „Gleichgewichtstemperatur ohne Atmosphäre“).
   **Empfehlung:** Text belassen (bewusste Vereinfachung der Ideensammlung, als gegeben gekennzeichnet); in der Musterlösung zu T4 h den Unterschied in einem Satz nennen.

8. **Mehrfach belegte Formelzeichen in Tutorium 5.**
   *Befund:* ρ_M, c_p,M (Milch in Aufgabe 1, Meerwasser in 2 und 3), q̇_V (Viertel in Aufgabe 2, Verdunstung in Aufgabe 4), T_e (Paderborn in Aufgabe 2 d, Erde in Aufgabe 3), α_S (2,89 in Aufgabe 2, 3,74 in Aufgabe 3). Jede Aufgabe definiert ihre Zeichen selbst in Tabelle oder Text; die Umbenennung λ zu α_S ist in Aufgabe 2 vollständig (g, h, Ergebnis, Skriptanzeige).
   **Empfehlung:** Belassen.

9. **Rundungsketten (letzte Stelle).**
   *Befund:* Die Skripte rechnen durchgehend ungerundet (Prüfauftrag A erfüllt). Wer mit den gedruckten Zwischenwerten weiterrechnet, erhält: Kaffee d ϑ₂ = 30,20 statt 30,19 °C, g 36,00 und 37,19 statt 35,99 und 37,18 °C (mit kA = 0,3402), f ϑ₂ = 30,97 statt 30,96 °C (mit kA = 0,4440); Deckschicht τ = 6,97 statt 6,98 Jahre und 4,53 statt 4,54 Jahre (mit C = 2,86·10⁸); Amazonas V̇_N = 0,419 statt 0,418 Sv mit 365 statt 365,25 Tagen.
   **Empfehlung:** Belassen; in den Musterlösungen ±1 in der letzten Stelle als richtig werten und 1 Jahr = 365,25 d nennen.

10. **„V08“ in Frage 3 (Tutorium 5).** *(Umgesetzt, siehe Abschnitt 5.)*
   *Befund:* Der Verweis stimmt (Foliensatz 08, Teil e: Form 30 cm hoch, Wärme nur über die Oberseite), „V08“ ist aber eine interne Abkürzung der Ideensammlung.
   **Empfehlung:** „Käse aus Foliensatz 08, Teil e (…)“ schreiben.

11. **Layout Tutorium 5, Seite 2.**
   *Befund:* Nach den Annahmen zu Aufgabe 1 bleiben etwa zwei Drittel der Seite leer, weil der Lua-Filter vor der Kaffee-Tabelle 27 Zeilen reserviert (1,9 je Tabellenzeile + 4); die Tabelle braucht etwa 20. Nicht mein Teil (`build/`).
   **Empfehlung:** Belassen; die Tabelle bleibt dadurch zusammen, sonst ist das Layout von Tutorium 4 und 5 ohne Überlauf.

## 3. Unabhängige Nachrechnung

Eigenes Skript `nachrechnung_B.py` (Scratch-Ordner), nur aus den Tabellenwerten, ohne die Rechenskripte. Gleichgewichte der Zusatzaufgaben und der Kipppunkt h (1) zusätzlich numerisch per Bisektion.

| Aufgabe | Kernergebnis | Text | eigene Rechnung | Abweichung |
|:---|:---|:---|:---|:---|
| T4 A1 a, c | S₀/4; q̇_abs | 340; 238 W/m² | 340,25; 238,18 | keine |
| T4 A1 d | T_e; T nur Erdwärme | 254,6 K = −18,6 °C; 35,5 K | 254,58 K = −18,57 °C; 35,49 K | keine |
| T4 A1 f | ε_A; T_A | 0,78; 242,2 K | 0,7789; 242,18 K | keine |
| T4 A1 g | Grenzfälle; q̇_G; Anteil | 254,6/302,7 K; 152 W/m²; 26 % | 254,58/302,74; 151,9 (152,1 mit 0,78); 25,9 | keine |
| T4 A1 h | 4σT_e³; ΔT | 3,74 W/(m² K); 1,05 K | 3,742; 1,050 | keine |
| T4 ZA1 b | ϑ bei α_L 2 und 5 | −11,3; −5,9 °C | −11,26; −5,86 | keine |
| T4 ZA2 a, b | Grenzluft bei α_L 5 und 10 | 4,27; 2,14 °C | 4,272; 2,136 | keine |
| T5 A1 a, c | ϑ₁,₀; kA | 70,47 °C; 0,3402 W/K | 70,466; 0,34025 | keine |
| T5 A1 d, e | ϑ₁, ϑ₂; Q₁, Q₂ | 34,05/30,19 °C; 34,88/38,57 kJ | 34,047/30,193; 34,881/38,571 | keine |
| T5 A1 f | kA; ϑ₁, ϑ₂ mit Becher | 0,4440 W/K; 34,04/30,96 °C | 0,44403; 34,044/30,965 | keine |
| T5 A1 g | ϑ₁, ϑ₂ mit Schaum 60 °C | 35,99/37,18 °C | 35,992/37,185 | keine |
| T5 A1 h (1) | Kipppunkt | 47,0 °C | 47,003 (Bisektion) | keine |
| T5 A1 h (2) | Unterschied, Milch höchstens 20 °C | (kein Ergebnis im Text; Lösung 2,48 K) | 1,95 K | Lösung falsch, siehe 2.1 |
| T5 A2 a, b | V̇; ṁ; V̇/V̇_A; Ċ; ΔT; Kontrolle | 1,7·10⁷; 1,74·10¹⁰; 82,5; 69,5 TW/K; 17,3 K; 1,18 PW | 1,7·10⁷; 1,7425·10¹⁰; 82,52; 69,53; 17,26; 1,182 | keine |
| T5 A2 c | q̇_G; q̇_V | 15,8; 63,2 W/m² | 15,79; 63,16 (mit 1,893·10¹³: 63,39) | keine (Rundung der Fläche gewollt) |
| T5 A2 d | q̇_abs; ϑ_e; ϑ_O | 55,8 W/m²; −96,0; −72,7 °C | 55,8; −96,04; −72,74 | keine |
| T5 A2 e | Abstrahlung; q̇_zu; Anteile | 198,5; 142,7 W/m²; 11 bis 44 %; 133,4/152,0; 10 bis 47 % | 198,55; 142,75; 11,1/44,2; 133,45/152,05; 10,4 bis 47,3 | keine |
| T5 A2 g | α_S; ΔT_G, ΔT_V; Δq̇; ΔT bei −20 % | 2,89; 5,5/21,9 K; −3,2/−12,6 W/m²; −1,1/−4,4 K | 2,885; 5,47/21,89; −3,16/−12,63; −1,09/−4,38 | keine |
| T5 A2 h | C, τ, Anteil (100 m; 350 m) | 4,09·10⁸, 4,5 a, 89 %; 1,43·10⁹, 15,7 a, 47 % | 4,090·10⁸, 4,49, 89,2; 1,431·10⁹, 15,72, 47,1 | keine |
| T5 A3 c, e | C; C_B; C/C_B; τ; ΔT(10 a); ΔT∞ | 2,86·10⁸; 4,4·10⁶; 65; 6,98 a; 2,30 K; 3,02 K | 2,863·10⁸; 4,4·10⁶; 65,06; 6,978; 2,302; 3,023 | keine |
| T5 A3 f, g | α_S, τ, ΔT∞; a; Leitzeit; τ, ΔT∞ mit Tiefsee | 3,74, 2,42 a, 1,05 K; 1,47·10⁻⁷; 1,1·10³ a; 4,54 a, 1,97 K | 3,743, 2,423, 1,050; 1,467·10⁻⁷; 1058; 4,536, 1,965 | keine |
| T5 A4 a | Sv-Werte; V̇_A/V̇_R; V̇_AMOC/V̇_A | 5·10⁻⁶ bis 0,206; 91; 82,5 | gleich; 91,15; 82,52 | keine |
| T5 A4 b | Ċ_A; Q̇ höchstens; ΔT für 19 TW | 0,861 TW/K; 0,861 TW; 22,1 K | 0,8611; 0,8611; 22,07 | keine |
| T5 A4 c | V̇_N; V̇_V; Verdunstung; Abweichung | 0,418; 0,212 Sv; 1117 mm/a; 3 % | 0,4183; 0,2123; 1116,5; 3,1 | keine |
| T5 A4 d | q̇_V; Q̇_V; Verhältnisse; Anteile | 86 W/m²; 516 TW; 599; 27; 56 bis 73 % | 85,97; 515,8; 599,1; 27,1; 56,2/73,5 | keine |
| T5 ZA1 | ΔT; ϑ_aus | 2,39 K; 28,39 °C | 2,392; 28,392 | keine |
| T5 ZA2 | m_E; Q; A; Q̇; t | 2,29·10¹¹ kg; 7,65·10¹⁶ J; 1,88·10⁶ m²; 75,2 bis 282 MW; 32,2/8,6 a | 2,2925·10¹¹; 7,645·10¹⁶; 1,88·10⁶; 75,2/282,0; 32,22/8,59 | keine (mit h_T aus Auftrieb siehe 2.4) |

Formelprüfung: Schichtmodell (Bilanzen Oberfläche und Schicht, T_A = T_O/2^(1/4), Abstrahlung nach oben σ(1 − ε_A/2)T⁴), Kirchhoff α_A = ε_A, Linearisierung, Mischtemperatur nach m c_p gewichtet, T(t) und τ = C/α wie Formelsammlung 5.1, Massenbilanz des Beckens, Q̇ = ṁ Δh_v, t ≈ h²/a mit a = λ/(ρ c_p): alle richtig, Einheiten und Vorzeichen stimmen (Δq̇_AMOC negativ, Wärmestrom Fluss gegen Meer als Kühlung des Meeres). Die Formelsammlung enthält keine Strahlungsformeln; σ ist in beiden Tutorien gegeben, die Linearisierung als „hier gegeben“ gekennzeichnet. Jede Teilaufgabe ist mit den gegebenen Größen lösbar.

## 4. Geprüft ohne Befund

- Struktur je Block (H2, Ausgangssituation, Skizze mit „Abb. n:“, Fragen mit Vorab-Frage zuerst, Aufgabe, Annahmen, Tabelle, Aufgabenstellung, Ergebniszeilen), höchstens neun Teile, Zusatzaufgaben am Ende.
- Wortzahlen der Ausgangssituationen: T4 120; Kaffee 71; AMOC 115; Deckschicht 110; Amazonas 84 (alle im Rahmen).
- Nummernfolge Tutorium 5 über drei Dateien: Frage 1 bis 5, Aufgabe 1 bis 4, Abb. 1 bis 4, Zusatzaufgabe 1 und 2; alle internen Verweise (Teile, Abbildungen, Fragen, „bis Teil e“, „bis Teil f“) zeigen auf die richtigen Stellen.
- Vorab-Fragen werden durch Rechnungen beantwortet: T4 Frage 1 durch Teil d und f; T5 Frage 1 durch d, Frage 4 durch Aufgabe 2 g (2) (1,1 bis 4,4 K, also „1 bis 5 K“), Frage 5 durch Aufgabe 3 c (C/C_B = 65).
- Querverweise auf Tutorium 4 aus Tutorium 5 (T_e, ε_A, Schichtmodellformel, Linearisierung) mit denselben Zahlen; keine Verweise anderer Tutorien auf Tutorium 4 oder 5.
- Käse-Verweis gegen Foliensatz 08 Teil e geprüft; Autoscheiben-Werte gegen V08 Teil g (Glas 0,95, Himmel −5 °C, α = 5 W/(m² K)); σ = 5,6705·10⁻⁸ wie V04.
- Skizzen (PNG angesehen): keine Lösung verraten (kein Bilanzraum in Abb. 1 bis 3 von Tutorium 5, kein Abfuhrpfeil in der Deckschicht), Formelzeichen wie in den Tabellen, keine Gedankenstriche (auch SVG-Texte), „nicht maßstäblich“ jetzt in allen Klima-Skizzen.
- Schreibweise: keine Gedankenstriche in Teilen, Quellen, Skizzen und Skripten; Minuszeichen U+2212 im Fließtext; Dezimalkomma in Mathe; °C als `\mathrm{°C}`; ϑ in °C und T in K; typografische Anführungszeichen; keine Tausenderpunkte; Kurzbelege nur bei ausdrücklichem Literaturvergleich.
- Quellen: jeder Tabellenwert und jeder Fakt der Ausgangssituationen belegt oder als Arbeitswert gekennzeichnet; Links in `<…>`, keine absoluten Pfade.
- Layout (Teile gebaut, alle Seiten angesehen): keine Formeln über den Rand, keine zu breiten Tabellen, keine Ergebniszeile als Liste, Bilder mit Bildunterschrift zusammen.

## 5. Nachträglich umgesetzt

Auf Wunsch der Koordination umgesetzt (Punkte 2.1 bis 2.5 und 2.10). Die Punkte 2.6 bis 2.9 und 2.11 bleiben unverändert. Die Musterlösung in `/home/claude/work/kaffee/` wurde nicht angefasst.

| Nr. | Datei, Stelle | vorher | nachher | Bezug, Anmerkung |
|:---|:---|:---|:---|:---|
| 1 | `rechnung/t5_kaffee_teil.py`, daraus `teile/t5a_kaffee.md`, Teil h (2) | „Begründen Sie ohne Rechnung.“ | „Begründen Sie mit einer Abschätzung und den Ergebnissen aus e).“ | 2.1. Neue Info-Zeilen in `t5_kaffee_ausgabe.txt` (stehen nicht im Blatt): ϑ₂ mit Milch bei Raumtemperatur 32,10 °C, Tasse 2 mindestens 1,95 K kühler, Milch nimmt höchstens 1,83 kJ auf, Q₂ − Q₁ = 3,69 kJ, Gleichstand erst bei 35,3 °C Milch; Selbstprüfung: Energieargument und direkte Rechnung stimmen überein. Keine Ergebniszeile zu (2), damit die Ja/Nein-Antwort nicht vorweggenommen wird |
| 2 | `teile/t4.md`, Zusatzaufgabe 2 | „… tauscht Strahlung mit dem Himmel aus, der für die Strahlung wie ein schwarzer Körper mit ϑ_H = −5 °C wirkt.“ | „… tauscht Strahlung mit ihrer Umgebung aus. Die schräge Scheibe sieht neben dem klaren Himmel auch Häuser und Bäume; zusammen wirkt diese Umgebung für die Strahlung wie ein schwarzer Körper mit ϑ_H = −5 °C.“ | 2.2. Werte und Ergebnisse unverändert (4,27 und 2,14 °C). Angepasst auch `quellen/t4_quellen.md` (Frage 2 und Zusatzaufgabe 2: −5 °C als wirksame Umgebungstemperatur, Arbeitswert nach V08 Teil g) sowie Docstring und Kopfzeile in `rechnung/t4_rechnung.py` |
| 3 | `teile/t4.md`, Aufgabe 1, Teil g | „eine Gegenstrahlung von 342 W/m²“; „… und vergleichen Sie. Welchen Anteil …“ | „eine Gegenstrahlung (Wärmestrahlung der Atmosphäre zur Oberfläche) von 342 W/m²“; „… und vergleichen Sie. Erklären Sie den Unterschied mit einer Energiebilanz der Oberfläche aus den Messwerten. Welchen Anteil …“ | 2.3. Ergebniszeile unverändert. `rechnung/t4_rechnung.py`: Info-Zeilen jetzt mit den Zahlen der Aufgabe (Sonne an der Oberfläche 238 − 80 = 158 W/m², Bilanz der Oberfläche mit Messwerten −0,8 W/m², Lücke 342 − 152 = 190 W/m², Erklärung 80 + 21 + 82 + 8 = 191 W/m²) statt der bisherigen Zeile mit 160 W/m² |
| 4 | `teile/t5b_ozean.md`, Zusatzaufgabe 2; `rechnung/t5_rechnung.py`; `quellen/t5_quellen.md` | h_T = 220 m; A = 1,88·10⁶ m², Q̇ = 75,2 bis 282 MW, t = 32,2 bzw. 8,6 Jahre | h_T = 224 m; A = 1,90·10⁶ m², Q̇ = 75,8 bis 284 MW, t = 31,9 bzw. 8,5 Jahre | 2.4. Einfachere Variante gewählt: Tiefgang bleibt im Text gegeben (die Meerwasserdichte steht in der Zusatzaufgabe nicht, ein Rechenschritt bräuchte einen weiteren Wert). Das Skript berechnet 223,7 m aus H ρ_E/ρ_M mit ρ_M = 1025 kg/m³ aus Aufgabe 2, rundet auf 224 m und rechnet damit weiter; Abgleich mit dem alten Wert der Ideensammlung (−0,8 % und −0,9 %). Quelle: Hinweis auf den Auftrieb und auf die 220 m (88 % der Dicke) der alten Rechnung |
| 5 | `rechnung/t5_kaffee_teil.py`, daraus `teile/t5a_kaffee.md`, Versuch Schritte 3 und 4 | „… daraus kA wie in Teil c bestimmen.“; „Mit den gemessenen Werten die Temperaturen nach 60 Minuten vorhersagen.“ | „… daraus kA wie in Teil f (mit Becher) bestimmen.“; „… vorhersagen, für Becher 3 mit Milch bei Raumtemperatur.“ | 2.5. Info-Zeilen für die Vorhersagen mit Becher: Becher 1 34,04 °C, Becher 2 30,96 °C, Becher 3 32,47 °C (Unterschiede zu Becher 1: 3,08 und 1,57 K) |
| 6 | `teile/t5_fragen.md`, Frage 3; `quellen/t5_quellen.md` | „Käse aus V08, Teil e“ | „Käse aus Foliensatz 08, Teil e“ | 2.10 |

Prüfungen nach der Umsetzung: `t4_rechnung.py` (Abgleich mit dem Blatt besteht), `t5_rechnung.py` („alle Anzeigen gefunden“), `t5_kaffee_teil.py` (alle Zahlen von a bis h unverändert, nur die beiden Textstellen geändert). Unabhängige Nachrechnung Eisberg mit 224 m: A = 1,896·10⁶ m², Q̇ = 75,84 bis 284,4 MW, t = 31,94 bzw. 8,52 Jahre, keine Abweichung zum Text. Tutorium 4 und das zusammengesetzte Tutorium 5 neu gebaut, die geänderten Seiten angesehen: alles sauber gesetzt; mit dem inzwischen angepassten Filter passt die Kaffee-Tabelle auf Seite 2 (Punkt 2.11 damit erledigt). Keine Gedankenstriche in den geänderten Dateien.
