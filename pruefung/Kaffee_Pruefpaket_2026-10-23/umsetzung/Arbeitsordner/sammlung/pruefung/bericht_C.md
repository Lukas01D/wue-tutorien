# Prüfbericht C: Tutorium 6, 7 und 8

Stand 21.10.2026, Prüfer C. Geprüft habe ich `teile/t6.md`, `t7.md` und `t8.md`, die Rechenskripte mit ihren Ausgaben, die vier Skizzenskripte mit den Skizzen und die drei Quellendateien. Zum Abgleich habe ich die Formelsammlung gelesen (`00_2026_Formelsammlung_final.md`, dazu die Textfassung `Formelsammlung_2026.txt`), außerdem die Textfassungen der Foliensätze 2026 (`/home/claude/work/quellen/`). Die Teile habe ich mit `build/teil_bauen.py` gebaut und jede Seite angesehen. Während meiner Prüfung hat die Koordination `build/kopf.tex` (17:07, Strafen gegen Hurenkinder und Schusterjungen) und `build/lehrstuhl.lua` (17:10, Platzfaktor vor „Gegebene Größen“ von 1,9 auf 1,5) geändert; der letzte Bau lief mit diesem Stand. Die eigene Nachrechnung, die Prüfbilder und die Tests liegen im Scratch-Ordner `/tmp/claude-0/-home-claude/a56bbd5d-81a7-5a60-a23a-c27d8d2dbb05/scratchpad/pruefung_C/` (`nachrechnung_C.py`, `nachrechnung_C_ausgabe.txt`, `bilder_final/`, `bilder_final2/`).

## 1. Erledigte Korrekturen

| Nr. | Datei, Stelle | vorher | nachher | Grund |
|:---|:---|:---|:---|:---|
| 1 | `teile/t6.md`, Aufgabe 2 f | „Vergleichen Sie dazu q̇_O mit q̇_S.“ | „Vergleichen Sie dazu q̇_O aus d) mit q̇_S.“ | q̇_O ist in Aufgabe 1 mit 65 mW/m² gegeben; damit ergäbe sich 3700 statt der Ergebniszeile 2600. Der Querverweis macht den Teil eindeutig. |
| 2 | `teile/t7.md`, Aufgabe 1 d, Ergebniszeile; `rechnung/t7_rechnung.py` (Format und zwei Kontrollzeilen) | d_T = 0,12 m | d_T = 0,117 m | Mit dem gerundeten Wert 0,12 m ergibt Teil e für den Tagesgang in 0,5 m 1,6 % statt der Ergebniszeile 1,4 %. Mit drei gültigen Ziffern (SPEZ 5) passen d und e zusammen. Skript neu gelaufen: „alle Werte gefunden“. |
| 3 | `teile/t8.md`, Tabelle Aufgabe 2, Gruppenkopf | „Atmosphäre bei 40° N:“ | „Atmosphäre, 40° N:“ | Der Gruppenkopf brach in zwei Zeilen um. „Atmosphäre (40° N):“ bricht ebenfalls um (getestet). |
| 4 | `teile/t8.md`, Tabelle Aufgabe 1, Verdampfer | „Wärmedurchgangs-koeffizient:“ (fester Bindestrich) | „Wärmedurchgangskoeffizient:“ mit weichem Trennstrich (U+00AD) | Ohne Umbruch, z. B. in Word, stünde ein falsch geschriebenes Wort. Im PDF bleibt die Trennung gleich, so wie in Tutorium 7. |
| 5 | `teile/t8.md`, Tabelle Aufgabe 2, Wasserdampf | „Verdampfungs-enthalpie:“ | „Verdampfungsenthalpie:“ mit weichem Trennstrich | wie Nr. 4 |
| 6 | `quellen/t7_quellen.md`, Frage 3 | „Foliensatz 02, F. 25“ | „Foliensatz 02, F. 26“ | Die Größenordnungen der Temperaturleitfähigkeit stehen in V02 (SoSe 2026) auf F. 26; auf F. 25 steht die Wärmeleitungsgleichung. |
| 7 | `quellen/t7_quellen.md`, Zusatzaufgabe 1 | kein Eintrag | „Erdradius R = 6371 km (Teil b): mittlerer Erdradius wie in Tutorium 6“ | Zahl im Aufgabentext ohne Eintrag |
| 8 | `quellen/t8_quellen.md`, Arbeitswerte Aufgabe 1 | Liste ohne Sondenlänge | „Sondenlänge 100 m“ ergänzt | Tabellenwert L ohne Eintrag |
| 9 | `quellen/t8_quellen.md`, Arbeitswerte Aufgabe 2 | ohne Höhe | „Höhe der betrachteten Luftschicht H = 10 km“ ergänzt | Tabellenwert H ohne Eintrag |
| 10 | `quellen/t8_quellen.md`, Eintrag Formelsammlung | nur Δ*T*~ln~ und ε-NTU genannt | Satz ergänzt: Die Carnot-Leistungszahl steht weder in der Formelsammlung noch in den Foliensätzen 01 bis 08. | Ergebnis meiner Suche in den Textfassungen 2026 (siehe offene Entscheidung 1) |

Nicht geändert: `t6_rechnung.py` und `t8_rechnung.py` (laufen, Ausgaben inhaltlich gleich) sowie alle Skizzenskripte und Skizzen (alle vier Skripte laufen und erzeugen pixelgleiche Bilder). Eine vorübergehende Zusammenlegung der beiden Ergebniszeilen in T7, Teil e (gegen eine verwaiste Zeile auf Seite 5) habe ich zurückgenommen, nachdem die Koordination den Platzfaktor gesenkt hatte; T7 hat jetzt auch in der ursprünglichen Form 4 Seiten.

## 2. Offene Entscheidungen

1. **Tutorium 8: Formeln außerhalb der Formelsammlung sind nicht gekennzeichnet.**
   Befund: Die Formelsammlung enthält nur Kennzahlen, Nußelt-Korrelationen (mit den *Re*-Bereichen der Rohrströmung), charakteristische Längen und Lösungen von DGL. Δ*T*~ln~ steht in V06 auf F. 26 bis 29, das ε-NTU-Konzept auf F. 35 bis 44 (ε = 1 − exp(−NTU) für *C*\* = 0 und die Formeln für *C*\* = 1 auf F. 41). Die Carnot-Leistungszahl steht weder in der Formelsammlung noch in V01 bis V08. Der Aufgabentext kennzeichnet nur Sverdrup als „nicht in der Formelsammlung“.
   Folgen: Die Teile d bis f sind nur mit Vorlesungswissen lösbar, Teil g (2) nur mit Vorwissen aus der Thermodynamik.
   **Empfehlung:** Unter die Tabelle von Aufgabe 1 diesen Satz setzen: „Die Carnot-Leistungszahl einer Wärmepumpe, $COP_{\mathrm{C}} = T_{\mathrm{K}}/(T_{\mathrm{K}} - T_{\mathrm{V}})$, ist hier gegeben (nicht in der Formelsammlung); $\Delta T_{\mathrm{ln}}$ und das $\varepsilon$-NTU-Konzept stehen in der Vorlesung, nicht in der Formelsammlung.“ Die Beziehung ε(NTU) für *C*\* = 0 nicht angeben, denn sie beantwortet die Vorab-Frage 1. In Zusatzaufgabe 1 hinter die beiden ε-Formeln ebenfalls „(nicht in der Formelsammlung)“ setzen.

2. **Tutorium 8, Block „Wer bringt die Wärme zum Pol“: keine Vorab-Frage, die Leitfrage ist nicht lösbar, und der Verweis auf Tutorium 5 fehlt.**
   Befund: Der Block hat keine Frage (nach SPEZ 4.1 erlaubt, nach Prüfauftrag B vorgesehen). Die Ausgangssituation endet mit „Welches Förderband trägt mehr Wärme nach Norden?“. Für den Ozean gibt die Aufgabe aber nur den Volumenstrom der AMOC an, nicht ihren Wärmestrom; Teil b vergleicht Massenströme. Die Werte stimmen mit `teile/t5b_ozean.md` überein (17 Sv bei 26,5° N, 1025 kg/m³, 3990 J/(kg K), ṁ = 1,74·10¹⁰ kg/s; der Wärmestrom steht dort mit 1,2 PW). Einen ausdrücklichen Verweis auf Tutorium 5 gibt es im Text nicht.
   Folgen: Die Leitfrage bleibt ohne Rechnung offen, außer die Studierenden erinnern sich an Tutorium 5.
   **Empfehlung:** (a) In die Gruppe „Meerwasser“ den Wärmestrom der AMOC aufnehmen, „Q̇_AMOC = 1,2 PW (Tutorium 5)“, und Teil b um „Vergleichen Sie Q̇_A mit Q̇_AMOC.“ ergänzen. (b) Vor Aufgabe 2 eine Vorab-Frage als Frage 3 setzen, die Teil a auflöst, z. B.: „Wie dick müsste eine Wasserschicht auf dem ganzen Ozean sein, um so viel Wärme zu speichern wie die ganze Atmosphäre: etwa 3 cm, 3 m oder 300 m? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 2 rechnen.“

3. **Tutorium 7, Zusatzaufgabe 1: ϑ_0 neben ϑ_O.**
   Befund: Die Anfangstemperatur heißt ϑ_0 (Ziffer null), die Oberflächentemperatur ϑ_O (Buchstabe O); die Formel enthält T_0 − T_O. In Aufgabe 1 ist ΔT_0 außerdem die Amplitude.
   Folgen: Im Druck sind die Zeichen leicht zu verwechseln.
   **Empfehlung:** Die Anfangstemperatur in ϑ_A bzw. T_A umbenennen (Text, Formel und Schreibweise in `t7_rechnung.py`).

4. **Tutorium 8, Aufgabe 2 a: g fehlt in der Tabelle.**
   Befund: Für die Masse der Luftsäule p_0/g braucht man g. Das Ergebnis h_O = 3,57 m liegt auf der Rundungskante: Mit g = 9,80665 m/s² oder mit dem gerundeten h_W = 2,54 m ergeben sich 3,58 m.
   Folgen: kleine, aber vermeidbare Abweichungen zwischen den Rechnungen der Studierenden und der Ergebniszeile.
   **Empfehlung:** „Erdbeschleunigung: g = 9,81 m/s²“ in die Gruppe „Luft am Boden“ aufnehmen, so wie in Tutorium 1.

5. **Tutorium 7, Teil g: frostfreie Gründungstiefe 0,8 m.**
   Befund: Der Aufgabentext nennt zu Recht keine Zahl; 0,8 m steht nur im Quellenverzeichnis „für die Lösung“, die Norm ist nicht eingesehen. Meine Websuche fand nur Forenbeiträge mit 80 cm, keinen Primärbeleg. √(a·t_K) = 0,78 m ist eine Größenordnung: Nach der erf-Lösung liegt die Frostgrenze (0 °C) nach 14 Tagen je nach Temperaturen bei 0,55 m (Boden +8 °C, Oberfläche −5 °C) bis 1,06 m (+5 °C, −10 °C), und die Schmelzwärme bremst zusätzlich.
   Folgen: keine für den Aufgabentext; die Musterlösung braucht einen Beleg.
   **Empfehlung:** Den Text so lassen. Vor der Musterlösung DIN 1054 mit DIN EN 1997-1/NA einsehen und dort schreiben: „Größenordnung; passt zur üblichen Mindesttiefe von 0,8 m“.

6. **Tutorium 8, Zusatzaufgabe 2 (Rekordflug) enthält keine Wärmeübertragung.**
   Befund: Die Aufgabe ist reine Kinematik. Die Aufgabenideen „Ozean und Atmosphäre“ sahen C5 nur als Exkurs vor (Entscheidung E20).
   Folgen: Sie kostet Zeit ohne Bezug zu den Lernzielen von Tutorium 8.
   **Empfehlung:** Den Titel in „Exkurs: Der Rekordflug“ ändern, damit sie bei Zeitmangel als erste entfällt.

## 3. Unabhängige Nachrechnung

Eigenes Skript `nachrechnung_C.py` (Scratch-Ordner), nur aus den Werten der Tabellen und Texte, ohne die Rechenskripte: 87 Größen geprüft, 0 Abweichungen. Die gegebene Lösung T(z,t) habe ich numerisch in die Wärmeleitungsgleichung eingesetzt (relativer Rest unter 10⁻⁶, d = √(2a/ω) bestätigt). Den Gradienten der erf-Lösung in Zusatzaufgabe 1 habe ich ebenfalls numerisch bestätigt.

| Aufgabe | Kernergebnisse im Text | eigene Rechnung | Abweichung |
|:---|:---|:---|:---|
| T6, A1 | ϑ(10/20/30 km) = 250/450/610 °C, ohne Quelle 270/530/790 °C | 250,0/450,0/610,0 bzw. 270,0/530,0/790,0 °C | keine |
| T6, A1 | ϑ(z_B) = 230 °C; q̇_M = 35 mW/m²; Granit z_max = 26 km, q̇_M = −10 mW/m² | 230,04 °C; 35,0 (Profil und globale Bilanz gleich); 26,0 km; −10,0 mW/m² | keine |
| T6, A2 | q̇_KV = 4,34·10⁻⁸ W/m³; ΔT = 97 800 bzw. 73 400 K; q̇_O = 92,1 mW/m²; q̇_S/q̇_O ≈ 2600 | 4,339·10⁻⁸; 97 843 bzw. 73 382 K; 92,145 (Profil gleich globale Bilanz); 2585 | keine |
| T6, Z1 | T = 35,7 K bzw. 35,2 K | 35,70 K bzw. 35,19 K | keine |
| T6, Kontrollen | KTB: 9,1 km, 265 °C; T1: 9101 m, 28 K/km | 10 °C + 28 K/km · 9,101 km = 264,8 °C; die Parabel weicht in 100 m nur 2 mK von der Geraden ab | passt |
| T7, A1 d | ω_T = 7,27·10⁻⁵ 1/s, d_T = 0,117 m; ω_J = 1,99·10⁻⁷ 1/s, d_J = 2,24 m | 7,272·10⁻⁵; 0,1173 m; 1,991·10⁻⁷; 2,241 m | keine (vor Korrektur 2 führte d_T = 0,12 m in e zu 1,55 %) |
| T7, A1 e, f | 64 %, 11 %, 1,2 %, 0,12 K; Tagesgang 1,4 %; 52/78/130 Tage | 64,0 %, 10,7 %, 1,15 %, 0,115 K; 1,41 %; 51,9/77,8/129,7 Tage | keine |
| T7, A1 g bis i | 0,78 m; z_0 = 1,41 m bzw. 2,46 m; 56 m | 0,778 m; 1,409 m bzw. 2,462 m; 56,2 m | keine |
| T7, Frage 3 | a von Granit 1,0 bis 1,5·10⁻⁶, Ton 4,9 bis 7,1·10⁻⁷ m²/s | 0,97 bis 1,50·10⁻⁶ und 4,86 bis 7,06·10⁻⁷; Kupfer 1,14·10⁻⁴, Luft 2,15·10⁻⁵, Wasser 1,43·10⁻⁷ m²/s | keine |
| T7, Z1 | t = 9,6·10⁷ Jahre; √(a·t) = 59,8 km | 9,61·10⁷ Jahre; 59,82 km; Eingangswerte passen zu Kelvin (7000 °F = 3871 °C, 1 °F je 50 ft = 36,45 K/km, 400 ft²/a = 1,178·10⁻⁶ m²/s) | keine |
| T8, A1 b, c | Q̇_V = 6,00 kW, P_el = 2,00 kW, ṁ_S = 0,526 kg/s; w = 0,95/0,48 m/s, Re = 6200/3100 | 6,000 kW; 2,000 kW; 0,5263 kg/s; 0,953/0,477 m/s; 6196/3098 (Übergangsbereich) | keine |
| T8, A1 d, e | ΔT_ln = 6,38 K, (kA)_V = 940 W/K, A_V = 0,94/0,47 m²; ε_V = 0,375, NTU_V = 0,470 | 6,383 K; 940,0 W/K (auf beiden Wegen); 0,940/0,470 m²; 0,375; 0,4700 | keine |
| T8, A1 f | ε = 0,250, NTU = 0,288, (kA)_Sonde = 575 W/K; ϑ_S,unten = 0,61 °C, 53,6 % | 0,250; 0,2877; 575,4 W/K; 0,608 °C; 53,59 % | keine (mit dem gerundeten 0,61 °C ergäben sich 53,7 %, tolerierbar) |
| T8, A1 g, h | 60 W/m; COP_C = 6,81, 59 %; 9,23 ha; 86 (mit JAZ 80) und 213 g/kWh | 60,0 W/m; 6,808; 58,8 %; 9,231 ha; 86,0; 80,0; 212,6 g/kWh | keine |
| T8, A2 a | 3390; h_W = 2,54 m; h_O = 3,57 m; 84 % | 3391; 2,538 m; 3,575 m (mit g = 9,80665 m/s²: 3,576 m); 83,9 % | keine (Rundungskante, siehe offene Entscheidung 4) |
| T8, A2 b, c | ṁ_L = 2,49·10¹¹ kg/s, V̇_L = 2,07·10⁵ Sv, 12 200, 14,3; ΔT_lat = 12,1 K, ṁ_L = 1,55·10¹¹ kg/s, 38 % | 2,488·10¹¹; 2,073·10⁵; 12 194; 14,28; 12,09 K; 1,550·10¹¹; 37,7 % | keine |
| T8, A2 d | ṁ_H/ṁ_L = 0,52; w_N = 1,33 m/s | 0,516; 1,329 m/s; Umfang 2πR cos 40° = 30 665 km (Tabelle 30 700 km) | keine |
| T8, Z1 | ε = 0,80/0,50; Faktor 2,5 bzw. 5; 15 bis 35 % | 0,800/0,4998; 2,501 bzw. 5,0; 15 bis 35 % | keine |
| T8, Z2 | 59,9 m/s = 216 km/h; 69,3 m/s; 6,11 h | 59,94 m/s = 215,8 km/h; 69,30 m/s; 6,107 h; Großkreis JFK nach LHR 5540 km und Mach 0,85 in 10,7 km = 251,9 m/s bestätigt | keine |

Die Rechenskripte `t6_rechnung.py`, `t7_rechnung.py` und `t8_rechnung.py` laufen; ihre Selbstprüfung besteht („alle Werte gefunden“ bzw. „0 fehlen im Text“), und der Abgleich mit den Kernzahlen der Ideensammlung ist überall „ok“.

## 4. Geprüft ohne Befund

- Struktur nach SPEZ 4: Reihenfolge der Bausteine; Nummern (T6: Fragen 1 bis 4, Aufgaben 1 und 2, Abb. 1, Zusatzaufgabe 1; T7: Fragen 1 bis 3, Aufgabe 1, Abb. 1, Zusatzaufgabe 1; T8: Fragen 1 und 2, Aufgaben 1 und 2, Abb. 1 und 2, Zusatzaufgaben 1 und 2); höchstens drei Konzeptfragen; drei bis sechs Annahmen; höchstens neun Teile (T7: neun); eine Ergebniszeile nach jedem rechnenden Teil, keine beginnt mit „(1)“. T6 teilt einen L-Block mit über neun Teilen regelgerecht in Aufgabe 1 und 2 (eine Ausgangssituation, eine zweiteilige Abbildung).
- Ausgangssituationen: T6 124, T7 134, T8 129 und 74 Wörter; jeder eingewobene Fakt kommt in einer Rechnung oder einem Vergleich wieder vor.
- Vorab-Fragen werden durch eine Rechnung beantwortet: T6 Frage 1 durch Aufgabe 2 b, T7 Frage 1 durch Teil f, T8 Frage 1 durch Teil e.
- Lösbarkeit und Widerspruchsfreiheit: Ausgangssituation, Tabellen und Ergebniszeilen stimmen überein (9,1 km und 265 °C; 47 TW; 100 m, 11 °C, −6 °C, 60 W/m, JAZ 4,3; 3 m, 5 bis 6 m/s, 50 m/s). Ausnahmen siehe offene Entscheidungen 1, 2 und 4.
- Physik: Vorzeichen mit z nach unten (T6 c, g, h); Randbedingungen; Kugel-DGL mit Faktor 6; Dämpfungstiefe und Phasenverschiebung; Auftautiefe als obere Abschätzung (Schmelzwärme vernachlässigt, passende Annahme vorhanden); Δ*T*~ln~ mit ln(8/5); *C*\* = 0 für Verdampfer und Sonde; Sonde nach halbem Weg mit 1 − exp(−NTU/2); Carnot mit T in K; Entenfuß mit (1 − ε) Ċ (ϑ_Körper − ϑ_Wasser).
- Querverweise: T6 zu T1 (KTB mit 9101 m in T1, 9,1 km und 265 °C in T6; mit 28 K/km aus T1 passen die 265 °C). T7 Frage 2 zu T1 (Eisschild stationär ohne Quelle; dort ist λ temperaturabhängig, das Profil also streng genommen leicht gekrümmt; für Frage 2 mit konstantem λ unerheblich, in der Musterlösung erwähnen). T7 zu T6 (Radioaktivität und Konvektion für Kelvin; nahezu lineares Profil in 100 m). T8 intern (Fragen 1 und 2, Teile d und e, Abb. 2, Teil c).
- Skizzen (alle vier PNG angesehen): keine verratene Lösung. `t7_boden.png` zeigt in z_1 und z_2 nur leere Zeitachsen mit Fragezeichen, also weder Dämpfung noch Phasenverschiebung. `t8_waermepumpe.png` zeigt keinen Bilanzraum, keine Wärmeströme und keine Stromführung im Verdampfer. `t6_erdwaerme.png` zeigt kein T(r)-Profil und keine Kugelschale; das Element dz links ist in Teil b ausdrücklich vorgegeben (in der Ideensammlung war es eine Zeichenaufgabe; SPEZ-konform, so lassen). `t8_pol.png` zeigt keine Wolken und keinen Regen, die Blickrichtung stimmt (Jetstream aus der Ebene heraus, Passat hinein), mit „schematisch, nicht maßstäblich“. Formelzeichen wie in den Tabellen, Rechtschreibung in Ordnung, keine Gedankenstriche (auch nicht in den SVG).
- Sprache und Schreibweise: Sie-Form, Dezimalkomma, keine Tausenderpunkte, °C als `\mathrm{°C}`, Minuszeichen U+2212 im Fließtext, typografische Anführungszeichen; keine Gedankenstriche in Teilen, Quellen, Skripten und Skizzen. q̇_KV wie in V02 F. 25 und V05 F. 7. Kurzbelege nur bei ausdrücklichen Vergleichen (GFZ, Anzellini, VDI 4640, Stoll, Li, Kilgore & Schmidt-Nielsen, NPR).
- Quellen: Alle Arbeitswerte ohne Beleg sind in T6 und T7 als Arbeitswerte gekennzeichnet (Krustendicke, λ, Oberflächentemperatur, Wärmeproduktion, λ der Kugel; a, a_G, Amplituden, Permafrost, Kälteperiode). Die Folienangaben habe ich gegen die Textfassungen 2026 geprüft (V02 F. 21 bis 30, V04 F. 10 mit σ, V05 F. 17 bis 21 und 31 bis 40, V06 F. 35 bis 41, V07 F. 3). Keine absoluten Pfade, Links in <…>.
- Layout mit dem Stand der Koordination (`kopf.tex` 17:07, `lehrstuhl.lua` 17:10): T6 4 Seiten, T7 4 Seiten, T8 7 Seiten. Alle Tabellen der gegebenen Größen stehen direkt nach den Annahmen, keine fast leere Seite, keine Formel über dem Rand, keine als Liste gesetzte Ergebniszeile, keine verwaiste Zeile, kein umbrechender Gruppenkopf. Zeilenbezeichnungen wie „Spez. Wärmekapazität:“ brechen um wie im Musterbeispiel. Vorher (Faktor 1,9) war Seite 2 von T8 fast leer, Seite 2 von T7 halb leer, und die letzte Zeile von T7 stand allein auf Seite 5; der neue Faktor behebt alle drei Stellen (vorab mit einer Kopie des Filters im Scratch-Ordner getestet).

## 5. Nachträglich umgesetzt

Auf Bitte der Koordination habe ich die offenen Entscheidungen 1, 2, 3, 4 und 6 aus Abschnitt 2 umgesetzt. Entscheidung 5 (Gründungstiefe) bleibt bei der Koordination, der Text dazu ist unverändert. Stand vor dieser Runde: Kopien im Scratch-Ordner unter `stand1/`.

| Nr. | Datei, Stelle | vorher | nachher | Grund |
|:---|:---|:---|:---|:---|
| N1 | `teile/t8.md`, Satz unter der Tabelle von Aufgabe 1 | nur „Die CO₂-Emissionen gelten ohne Vorketten, beim Strom für den Strommix des Jahres 2025.“ | ergänzt: „Die Carnot-Leistungszahl einer Wärmepumpe, COP_C = T_K/(T_K − T_V), ist hier gegeben (nicht in der Formelsammlung). ΔT_ln und das ε-NTU-Konzept stehen in der Vorlesung (Foliensatz 06), nicht in der Formelsammlung.“ | Entscheidung 1. ε(NTU) für C* = 0 steht bewusst nicht da, weil es Frage 1 beantworten würde. |
| N2 | `teile/t8.md`, Zusatzaufgabe 1, nach den ε-Formeln | „Rechnen Sie mit NTU = 4.“ | „Die Beziehungen sind hier gegeben (nicht in der Formelsammlung). Rechnen Sie mit NTU = 4.“ | Entscheidung 1; Wortlaut wie in Tutorium 7 |
| N3 | `teile/t8.md`, Tabelle Aufgabe 2, Gruppe „Meerwasser“ | keine Zeile für den Wärmestrom | neue Zeile „Wärmestrom: Q̇_AMOC = 1,2 PW (Tutorium 5)“ | Entscheidung 2 a. Die Bezeichnung „Wärmestrom AMOC:“ bräche um (getestet); deshalb steht „(Tutorium 5)“ in der Wertspalte, dort in einer zweiten Zeile. |
| N4 | `teile/t8.md`, Aufgabe 2 b, Text und Ergebniszeile | Text endet mit „Welcher Vergleich zählt für den Wärmetransport?“; Ergebnis endet mit „ṁ_L/ṁ_AMOC = 14,3“ | Text ergänzt um „Vergleichen Sie Q̇_A mit Q̇_AMOC.“; Ergebnis ergänzt um „Q̇_A/Q̇_AMOC = 4,2“ | Entscheidung 2 a. Skript: 4,17; die Ergebniszeile passt weiter in eine Zeile. |
| N5 | `teile/t8.md`, zwischen Abb. 2 und Aufgabe 2 | keine Frage | „Frage 3 (Vorab-Frage): Wie dick müsste eine Wasserschicht auf dem ganzen Ozean sein, um so viel Wärme zu speichern wie die ganze Atmosphäre: etwa 3 cm, 3 m oder 300 m? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 2 rechnen.“ | Entscheidung 2 b. Die Fragen in T8 laufen jetzt von 1 bis 3, Verweise auf Frage 1 und 2 bleiben gültig. |
| N6 | `teile/t8.md`, Ausgangssituation „Wer bringt die Wärme zum Pol“ | „…; oft heißt es sogar, schon die obersten 3 m des Ozeans speicherten mehr Wärme als die ganze Atmosphäre.“ | „…; oft heißt es sogar, schon eine dünne Schicht an der Oberfläche des Ozeans speichere mehr Wärme als die ganze Atmosphäre.“ | Geht über den Auftrag hinaus, bitte bestätigen: Sonst stünde die Antwort auf Frage 3 direkt darüber. Die Zahl 3 m steht jetzt in Teil a (N7). 76 Wörter statt 74. |
| N7 | `teile/t8.md`, Aufgabe 2 a | „Prüfen Sie damit die Aussage über die obersten 3 m des Ozeans.“ | „Prüfen Sie damit Ihre Vermutung zu Frage 3 und die oft zitierte Aussage, schon die obersten 3 m des Ozeans speicherten mehr Wärme als die ganze Atmosphäre.“ | Teil a löst Frage 3 auf (h_O = 3,57 m, also „etwa 3 m“). Die Ergebniszeile ist unverändert. |
| N8 | `teile/t8.md`, Tabelle Aufgabe 2, Gruppe „Luft am Boden“ | leere Zelle neben „AMOC bei 26,5° N“ | „Erdbeschleunigung: g = 9,81 m/s²“ | Entscheidung 4. Das Skript rechnet mit 9,81: h_W = 2,54 m und h_O = 3,57 m bleiben (mit 9,80665 wären es 3,576 m). |
| N9 | `teile/t8.md`, Zusatzaufgabe 2 | „(neu): Der Rekordflug“ | „(neu, Exkurs): Der Rekordflug“ | Entscheidung 6 |
| N10 | `teile/t7.md`, Zusatzaufgabe 1, Text und Formel | ϑ_0 = 3870 °C; (T_0 − T_O)/√(π a t) | ϑ_A = 3870 °C; (T_A − T_O)/√(π a t) | Entscheidung 3 |
| N11 | `rechnung/t7_rechnung.py` | Variable th_0K, Schreibweise „\vartheta_0“ | Variable th_AK, Schreibweise „\vartheta_A“ | zu N10; Selbstprüfung „alle Werte gefunden“ |
| N12 | `rechnung/t8_rechnung.py` | ohne Q̇_AMOC, g ohne Ausgabe | Q_AMOC = 1,2 PW; Ausgabe und Textprüfung von Q̇_AMOC, g und Q̇_A/Q̇_AMOC; Hinweiszeile h_O mit g = 9,80665 m/s² | zu N3, N4 und N8; Selbstprüfung „55 Schreibweisen geprüft, 0 fehlen im Text“ |
| N13 | `quellen/t8_quellen.md` | AMOC nur mit Volumenstrom; g ohne Eintrag; NASA-Eintrag ohne Stelle; Eintrag Formelsammlung ohne Hinweis auf den Text | AMOC-Wärmestrom 1,20 ± 0,12 PW, Arbeitswert 1,2 PW wie in Tutorium 5 (Johns et al., 2023); g = 9,81 m/s² als Standardwert wie in Tutorium 1; NASA-Eintrag mit „Ausgangssituation ohne Zahl, damit Frage 3 offen bleibt; Teil a“; Carnot-Leistungszahl „im Aufgabentext unter der Tabelle als gegeben“ | Belege zu N1, N3, N6 und N8 |

Prüfung nach dieser Runde:
- Die Skripte von T6, T7 und T8 laufen, die Selbstprüfung besteht.
- Meine Nachrechnung umfasst jetzt 88 Größen, 0 Abweichungen (neu: Q̇_A/Q̇_AMOC = 4,17).
- Gebaut mit dem aktuellen Stand von `build/`: T7 4 Seiten, T8 7 Seiten. Keine Formel über dem Rand, kein umbrechender Gruppenkopf, keine verwaiste Zeile.
- Keine Gedankenstriche in den geänderten Dateien.
- `build/` habe ich nicht geändert und `sammlung_bauen.py` nicht ausgeführt.
