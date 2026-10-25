# Prüfbericht A: Tutorien 1 bis 3

Prüfer A, Stand 21.10.2026. Geprüft: `teile/t1.md`, `teile/t2.md`, `teile/t3.md`, die Rechenskripte `rechnung/t1_rechnung.py` bis `t3_rechnung.py` mit Ausgaben, die sechs Skizzen-Skripte und Skizzen (PNG angesehen), `quellen/t1_quellen.md` bis `t3_quellen.md`. Gelesen zum Vergleich: SPEZ, Musterbeispiel Kaffee, Formelsammlung, Pilotblatt Tutorium 1 mit Musterlösung, Ideensammlung (Abschnitte 4.1 bis 4.3), Lehrstuhl-Tutorium 3, `teile/t6.md` und `quellen/t6_quellen.md` (nur lesen).

Kurzfassung: Kein Zahlenfehler. Alle Kernergebnisse lassen sich unabhängig reproduzieren. Neun kleine Korrekturen (Eindeutigkeit, Querverweis, Layout, Quellen, Selbstprüfung). Eine wichtige offene Entscheidung: die Temperatur des Wostoksees in Tutorium 1.

## 1. Erledigte Korrekturen

| Nr. | Datei, Stelle | vorher | nachher | Grund |
|---|---|---|---|---|
| 1 | `teile/t1.md`, Aufgabe 1 e) | „… Welche Temperatur ϑ_B ergibt sich an der Basis?“ | „… ergibt sich an der Basis (λ_m aus d)?“ | Die Ergebniszeile 33,2 °C gilt nur mit λ_m. Ohne Angabe sind andere Wege ebenso richtig: exakt mit λ(T) (Kirchhoff) 44,1 °C, mit λ(ϑ_O) 20,7 °C. Formulierung wie in Teil g. |
| 2 | `teile/t1.md`, Aufgabe 1 h) (2) | „… und um welchen Faktor?“ | „… und um welchen Faktor (Eis mit λ_m)?“ | Faktor 2,43 gilt mit λ_m (so auch die Musterlösung des Pilotblatts). Mit λ(ϑ_O) des Eises direkt unter dem Firn ergäbe sich 2,83. |
| 3 | `teile/t3.md`, Tabelle Aufgabe 2 | „Kinematische Viskosität:“ | „Kinem. Viskosität:“ | Die Bezeichnung brach im PDF auf zwei Zeilen um (SPEZ 4.1: kurze Bezeichnungen). Kurzform wie in Tutorium 2. |
| 4 | `teile/t3.md`, Aufgabe 1 e) (3) | „aus Tutorium 2 ergaben sich α = 19,6 W/(m² K) und 554 W/m²“ | „aus Tutorium 2 (Aufgabe 1, Teil e) ergaben sich α = 19,6 W/(m² K) und q̇ = 554 W/m²“ | Verweis auf die genaue Stelle, Formelzeichen zur Zahl. Die Zahlen stimmen mit Tutorium 2, Teil e überein. |
| 5 | `teile/t3.md`, Ergebniszeile Aufgabe 1 e) | „Faktor 26; Zu (3): …“ | „Faktor 26; zu (3): …“ | Kleinschreibung nach Semikolon (wie „zu (2)“ in Tutorium 1, Teil h). |
| 6 | `teile/t3.md`, Ergebniszeile Aufgabe 2 b) | nur R_th,Iso, R_th,ges und Q̇ | zusätzlich R_th,i = 5,34·10⁻⁴ K/W, R_th,St = 8,39·10⁻⁵ K/W, R_th,a = 0,0112 K/W (Ergebnis jetzt in zwei Zeilen) | Teil b verlangt alle vier Widerstände. Werte aus der Skriptausgabe; in Aufgabe 1 c stehen ebenfalls alle Widerstände. Passt in den Satzspiegel. |
| 7 | `quellen/t1_quellen.md` | kein Eintrag für s_F | neuer Eintrag: Dicke der Firnschicht 100 m, Arbeitswert des Pilotblatts („obere 100 m“) | Tabellenwert ohne Quelle (Prüfpunkt F). |
| 8 | `quellen/t3_quellen.md`, Eintrag Arbeitswerte | ohne s_J und A | ergänzt: Jungeis s_J = 0,1 m ohne Schnee (Teil f; Kernzahlen 4.3); A = 1 m² als frei gewählte Bezugsfläche | Tabellenwerte ohne Quelle. |
| 9 | `rechnung/t3_rechnung.py` und `t3_rechnung_ausgabe.txt` | kein Abgleich mit dem Blatt (nur Asserts gegen die Kernzahlen der Ideensammlung) | Abgleich wie in t1 und t2: 61 Zeichenketten (alle Tabellenwerte und Ergebnisse, aus den Variablen formatiert) müssen in `teile/t3.md` stehen; Ergebnis „alles gefunden“; Docstring ergänzt | Einheitliche Selbstprüfung für alle drei Tutorien. Gegentest in einer Kopie: zwei absichtlich verfälschte Werte werden als FEHLT gemeldet. Alle berechneten Zahlen unverändert. |

Zahlenfehler: keine. Kein Wert in Tabellen oder Ergebniszeilen wurde verändert. Die Skripte t1, t2 und t3 laufen, alle drei Abgleiche melden „alles gefunden“, die Asserts in t3 bestehen. Skizzen wurden nicht geändert (kein Befund).

## 2. Offene Entscheidungen

1. **Wostoksee: „etwa −3 °C“ oder „−2,52 °C“ (Tutorium 1, Ausgangssituation und Teil f)**
   - Befund: Text, Tabelle und Ergebnis sind jeweils richtig gerechnet, aber nicht widerspruchsfrei.
     - Ausgangssituation: Die Bohrung erreicht den Wostoksee in 3769 m Tiefe, das Wasser ist „etwa −3 °C“ kalt (Literaturwert, Jones 2012 über die Ideensammlung; auch andernorts als „berechnet, rund −3 °C“ angegeben).
     - Tabelle: γ = 0,0742 K/MPa (reines Eis) und H = 3700 m (allgemeiner Standort, nicht Wostok).
     - Ergebnis f): ϑ_pm = −2,47 °C. Mit denselben Werten liegt der Druckschmelzpunkt in 3769 m bei −2,52 °C; daher stammt diese Zahl.
     - Wer vergleicht, findet Seewasser von −3 °C rund 0,5 K unter dem Schmelzpunkt des Modells: Es müsste gefrieren. Der Literaturwert passt zu luftgesättigtem Eis (0,098 K/MPa ergibt −3,26 °C in 3700 m und −3,32 °C in 3769 m).
     - 0,098 K/MPa ist keine Lösung: Dann läge der Dome-C-Messwert −2,34 °C über dem Schmelzpunkt in z_2 (−2,88 °C), und Teil h (3) wäre unsinnig. Deshalb hat das Pilotblatt 0,0742 K/MPa gewählt.
     - Die Zahl −3 °C wird in keiner Rechnung gebraucht; Teil f fragt nur „kälter als 0 °C“ (SPEZ 4.1: nur Fakten einweben, deren Zahl später vorkommt).
   - Folgen: Aufmerksame Studierende stoßen in Teil f auf einen Widerspruch, den das Blatt nicht auflöst. Die Erklärung (Luftgehalt des Eises) steht nicht in der Vorlesung.
   - **Empfehlung:** Weder −3 °C noch −2,52 °C nennen, sondern die Zahl aus der Ausgangssituation nehmen: „… den Wostoksee erreichte, war das Wasser kälter als 0 °C und trotzdem flüssig.“ Tabelle, Teil f und alle Ergebnisse bleiben, wie sie sind; in `quellen/t1_quellen.md` im Eintrag Jones (2012) „etwa −3 °C“ streichen. −2,52 °C bitte nicht verwenden: Ein Modellwert würde mit falscher Genauigkeit als Messwert ausgegeben und widerspräche der zitierten Quelle. Für die Tutoriumsleitung genügt der Hinweis: Mit luftgesättigtem Eis (0,098 K/MPa) ergibt sich rund −3,3 °C, daher der Literaturwert.

2. **Tutorium 2 ohne technischen Zwilling**
   - Befund: Die Ideensammlung (4.2, Zusatzaufgaben) nennt als technischen Zwilling V03 Beispiel 3 (heiße Luft über einer Platte). `teile/t2.md` hat nur den L-Block und die Zusatzaufgabe Windchill.
   - Folgen: Als einziges der drei Tutorien ohne technischen Fall; die Platte wird nur am Klimabeispiel geübt.
   - **Empfehlung:** So lassen und als bewusste Kürzung festhalten. Der Zwilling wäre ein bekanntes Vorlesungsbeispiel ohne neue Physik; die Rinne deckt die Platte bei erzwungener und freier Konvektion vollständig ab, der Windchill den Zylinder, und mit neun Teilen und vier Fragen ist das Tutorium voll.

3. **Zwei Abbildungen im ersten Block von Tutorium 1**
   - Befund: SPEZ 4.1 verlangt genau eine Abbildung je L-Block. „Seen unter dem Eisschild“ hat Abb. 1 (Situation) und Abb. 2 (Profile zu Frage 3).
   - Folgen: formale Abweichung von der SPEZ.
   - **Empfehlung:** Beibehalten. Frage 3 („Profile lesen“, in SPEZ 4.1 ausdrücklich vorgesehen) ist ohne Abb. 2 nicht lösbar.

4. **Seitenumbrüche im Einzelbau**
   - Befund: Die Tabelle „Gegebene Größen“ springt in Tutorium 1 (Seite 2) und Tutorium 3 (Seite 4) als Ganzes auf die nächste Seite und lässt rund eine halbe Seite frei. In Tutorium 3 steht die Ergebniszeile von Aufgabe 1 d) allein oben auf Seite 3.
   - Folgen: nur optisch; im Gesamtbau liegen die Umbrüche anders.
   - **Empfehlung:** Im Gesamt-PDF ansehen. Tritt es dort ebenso auf, im Build lösen (zum Beispiel `\needspace` vor Tabellen und Ergebniszeilen), nicht in den Teildateien.

## 3. Unabhängige Nachrechnung

Eigenes Skript ohne die Rechenskripte der Sammlung, nur mit den Tabellenwerten und den Korrelationen der Formelsammlung: `/tmp/claude-0/-home-claude/a56bbd5d-81a7-5a60-a23a-c27d8d2dbb05/scratchpad/pruefung_A/nachrechnung_A.py`, Ausgabe `/tmp/claude-0/-home-claude/a56bbd5d-81a7-5a60-a23a-c27d8d2dbb05/scratchpad/pruefung_A/nachrechnung_A_ausgabe.txt`. λ_m numerisch (Simpson) statt mit der geschlossenen Formel; Luftstoffwerte zusätzlich mit CoolProp und grob mit Sutherland geprüft.

**Tutorium 1, Aufgabe 1 (Eisschild)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| λ(ϑ_O), λ(0 °C), λ_m | 2,83; 2,07; 2,43 W/(m K) | 2,8343; 2,0715; 2,4330 | Rundung |
| ϑ_B | 33,2 °C | 33,20 °C | keine |
| p; ϑ_pm | 33,3 MPa; −2,47 °C | 33,284 MPa; −2,470 °C | Rundung |
| q̇_leit; v_schm | 34,5 mW/m²; 2,42 mm/a | 34,54; 2,421 (mit 365 d: 2,419) | Rundung |
| H_krit | ≈ 2200 m | 2203,5 m | Rundung |
| Faktor Firn/Eis | 2,43 | 2,433 | Rundung |
| dT/dz; q̇_C | 26,5 K/km; 55,8 mW/m² | 26,50; 55,83 | Rundung |
| ϑ_pm(z_2); Δz | −2,18 °C; ≈ 6 m | −2,183 °C; 5,93 m | Rundung |

**Tutorium 1, Aufgabe 2 (Kühlhauswand)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| q̇; Q̇ | 10,23 W/m²; 2,56 kW | 10,231; 2,558 | Rundung |
| ϑ_G; Faktor | 27,11 °C; 92 | 27,110 (auch von innen gerechnet); 92,0 | keine |
| s_D,min; q̇(16 cm) | 15,41 cm; 7,71 W/m² | 15,408; 7,708 | Rundung |
| q̇ mit doppeltem Beton | 10,05 W/m² | 10,052 | Rundung |

**Tutorium 1, Zusatzaufgabe 1 (KTB)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| q̇_KTB | 81,2 mW/m² | 81,20 | keine |
| q̇_KTB/q̇_E; λ_KTB/λ_m | 1,40; 1,19 | 1,400; 1,192 | Rundung |
| ΔT | 254,8 K | 254,83 | Rundung |

Querbezug Tutorium 6: 10 °C (ϑ_O in T6) + 254,8 K = 264,8 °C ≈ 265 °C; umgekehrt (265 − 10) K / 9,101 km = 28,0 K/km. Beide Tutorien nennen 9101 m (T6 gerundet 9,1 km) und dieselbe Quelle (GFZ, 2024).

**Tutorium 2, Aufgabe 1 (Rinne)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| ϑ_m; Re; x_krit | −15,9 °C; 6,69·10⁶; 0,75 m | −15,90; 6,695·10⁶; 0,747 | Rundung |
| Nu; α; q̇; Q̇ | 8488; 19,6 W/(m² K); 554 W/m²; 5,54 MW | 8488; 19,63; 553,6; 5,536 | Rundung |
| α_1 (1 m); α_2 (100 m) | 32,1; 12,1 W/(m² K) | 32,06; 12,10 | Rundung |
| L; Gr | 4,95 m; 9,67·10¹¹ | 4,950; 9,666·10¹¹ | Rundung |
| α frei; q̇ frei | 4,58 W/(m² K); 129 W/m² | 4,577; 129,1 | Rundung |

Stoffwerte der Luft: Tabellenwerte gleich CoolProp 8.0.0 (bei −15,9 °C: 0,02313 W/(m K), 1,1951·10⁻⁵ m²/s, 0,7134; bei −10 °C und −29 °C ebenso). Grobe Gegenprobe mit Sutherland: λ 1,4 % kleiner, ν 0,2 % kleiner, Pr 1 % größer, also plausibel.

**Tutorium 2, Zusatzaufgabe 1 (Windchill)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| α_F; α_K | 68,7; 33,3 W/(m² K) | 68,69 (Re 12 617); 33,28 (Re 113 552) | Rundung |
| α_F/α_K | 2,06 | 2,064 | Rundung |
| α_K(0,5 m/s); Faktor | 7,1 W/(m² K); 4,7 | 7,146; 4,66 | Rundung (zwei gültige Ziffern) |

**Tutorium 3, Aufgabe 1 (Meereis und Schnee)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| R_th,α; R_th,S; R_th,E | 0,0667; 1,00; 0,667 K/W | 0,06667; 1,000; 0,6667 | Rundung |
| Bereich R_th,S | 0,667 bis 1,43 K/W | 0,6667 bis 1,4286 | Rundung |
| R_th,ges; kA; Q̇ | 1,73 K/W; 0,577 W/K; 16,3 W | 1,7333; 0,5769; 16,27 | Rundung |
| ϑ_O; ϑ_SE | −28,9 °C; −12,6 °C | −28,92; −12,65 (von unten gerechnet) | Rundung |
| Teildifferenzen | 1,08 + 16,3 + 10,8 = 28,2 K | 1,085 + 16,27 + 10,85 = 28,20 | Rundung |
| q̇_W; Faktor | 423 W/m²; 26 | 423,0; 26,0 | keine |
| Q̇ mit α = 19,6 | 16,4 W | 16,42 | Rundung |
| ds_E/dt; q̇_J; ds_J/dt | 0,46 cm/d; 247 W/m²; 6,97 cm/d | 0,460; 246,75; 6,971 | Rundung |

Querbezug Tutorium 2: 19,6 W/(m² K) und 554 W/m² stimmen mit T2, Aufgabe 1 e. Die 554 W/m² folgen aus dem ungerundeten α = 19,63; mit 19,6 gerechnet ergeben sich 552,7 W/m² (unter 0,3 %, unkritisch).

**Tutorium 3, Aufgabe 2 (Ölleitung)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| Re (L = π d_a/2 = 2,215 m); Nu_m; α_a | 1,02·10⁶; 2024; 20,2 W/(m² K) | 1,0188·10⁶; 2024,1; 20,20 | Rundung |
| R_th,i; R_th,St; R_th,a | 5,34·10⁻⁴; 8,39·10⁻⁵; 0,0112 K/W | 5,34·10⁻⁴; 8,39·10⁻⁵; 0,01118 | Rundung |
| R_th,Iso; R_th,ges; Q̇ | 0,576; 0,588 K/W; 102 W | 0,5759; 0,5877; 102,09 | Rundung |
| ϑ_O; ϑ_m | −28,9 °C; −29,4 °C | −28,86; −29,43 | Rundung |
| k_i; k_a; kA | 0,455; 0,384 W/(m² K); 1,70 W/K | 0,4546; 0,3841; 1,7016 | Rundung |
| r_krit | 1,98 mm | 1,980 | keine |

**Tutorium 3, Zusatzaufgabe 1 (schneefreie Stellen)**

| Größe | Blatt | eigene Rechnung | Abweichung |
|---|---|---|---|
| R_th,ges; Q̇ | 1,53 K/W; 18,5 W | 1,5253; 18,49 | Rundung |
| Zunahme; Anteil | 13,6 %; 20,8 % | 13,64; 20,80 | Rundung |

Formeln gegen die Formelsammlung geprüft:
- Längs angeströmte Platte turbulent (0,5 < Pr < 2000, 5·10⁵ < Re < 10⁷): 10 m und 1 m gültig; 100 m mit Re = 6,7·10⁷ außerhalb, danach fragt Teil f.
- Waagerechte Platte, freie Konvektion: Gr Pr f(Pr) = 2,79·10¹¹ > 7·10⁴, also turbulent; β = 1/T_u und L = A/U wie in der Formelsammlung.
- Quer angeströmter Zylinder (Übergangsbereich, 10 < Re < 10⁷) mit L = π d/2 in T2 ZA1 und T3 Aufgabe 2.
- Stoffwerte bei der Filmtemperatur in T2 Aufgabe 1 und T3 Aufgabe 2; in T2 ZA1 ausdrücklich bei ϑ_u (die Hauttemperatur ist nicht gegeben), vertretbar.
- Zylinderwand: Faktor 2π, Radien statt Durchmesser, ln(r_St/r_i) und ln(r_a/r_St) richtig; Vorzeichen und Einheiten (MPa, kJ/kg, s pro Jahr, cm/d) richtig.

## 4. Geprüft ohne Befund

- Rechenskripte: t1, t2 und t3 laufen fehlerfrei; Abgleich jeweils „alles gefunden“ (T3 nach Korrektur 9); Rundung der Ergebniszeilen wie die Skriptausgabe.
- Lösbarkeit: Jede rechnende Teilaufgabe ist mit Tabelle, Formelsammlung und den gekennzeichneten Zusatzangaben lösbar (nach Korrektur 1 und 2 auch eindeutig); keine fehlende oder überbestimmte Größe.
- Struktur: Ausgangssituation, Abbildung, Fragen (Vorab-Frage zuerst), Aufgabe, Annahmen (drei bis sechs), Tabelle (Trenner exakt, Gruppenköpfe richtig), Aufgabenstellung mit höchstens neun Teilen (T1: 9, 5, 3; T2: 9, 3; T3: 6, 6, 3). Nummern von Fragen, Aufgaben und Abbildungen laufen je Tutorium richtig. Wortzahlen: T1 112 und 64, T2 92, T3 123 und 73. Jede Vorab-Frage wird durch eine Rechnung beantwortet (T1 h (2), T2 f, T3 c und d).
- Skizzen: alle sechs PNG angesehen. Formelzeichen passen zu den Tabellen, keine Lösung verraten (kein Profil, keine Grenzschichten, kein Ersatzschaltbild; ϑ_O, ϑ_SE und α_a nur als „= ?“), „nicht maßstäblich“ wo nötig (die Kühlhauswand ist im Verhältnis 20 : 12 maßstäblich). Keine Gedankenstriche, auch nicht in den SVG. Alle sechs Skripte laufen und erzeugen pixelgleiche Bilder (Lauf in einer Kopie im Scratch-Ordner).
- Sprache und Schreibweise: Sie-Form, keine Gedankenstriche (auch nicht in Quellen und Skripten), echte Minuszeichen im Fließtext, Dezimalkomma als {,}, keine Tausenderpunkte, °C als \mathrm{°C}, typografische Anführungszeichen, Kennzahlen kursiv, „z. B.“ richtig. Indizes je Tutorium einheitlich (T1 und T2 aufrecht, T3 kurz und kursiv; nach SPEZ 5 zulässig).
- Querverweise: Alle Verweise auf Frage n, Abb. n, Teil x und Aufgabe n zeigen auf existierende Stellen; T3 auf T2 und T1 auf T6 siehe Abschnitt 3.
- Quellen: Jeder Tabellenwert und jeder Fakt der Ausgangssituationen hat einen Eintrag oder ist als Arbeitswert gekennzeichnet (nach Korrektur 7 und 8); keine absoluten Pfade; Links in <…>; CoolProp 8.0.0 ist installiert wie angegeben.
- Notation L in T3, Aufgabe 2 (Abschnittslänge und charakteristische Länge der Formelsammlung): Lehrstuhlkonvention (Lehrstuhl-Tutorium 3, Frage 4: Q̇/L); die Ergebniszeile Re = 1,02·10⁶ macht die richtige Länge prüfbar. Keine Änderung.
- T2 f: Für b = 1 m ist Re = 6,7·10⁵ nur knapp turbulent (Umschlag nach 0,75 m); die Formelsammlung ist formal erfüllt, und die VDI-Kombination aus laminarem und turbulentem Anteil ergäbe 34 W/(m² K). 32,1 W/(m² K) ist plausibel.
- T2, Abb. 1 zeigt l nicht (senkrecht zur Bildebene); Tabelle und Aufgabentext nennen l. Vertretbar.
- Layout: keine Formel über den Rand, keine umbrechenden Gruppenköpfe (nach Korrektur 3), keine Ergebniszeile als Liste. Seitenbilder vor und nach den Korrekturen: `/tmp/claude-0/-home-claude/a56bbd5d-81a7-5a60-a23a-c27d8d2dbb05/scratchpad/pruefung_A/bilder_vorher/` und `/tmp/claude-0/-home-claude/a56bbd5d-81a7-5a60-a23a-c27d8d2dbb05/scratchpad/pruefung_A/bilder_nachher/`.
