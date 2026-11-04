# R3 Fach und Modell: Erweiterungen des Kaffee-Modells

Stand 04.11.2026. Strang „Fach und Modell“ für das Konzept des Simulationstools zur Aufgabe „Kaffee mit Milch“ (Tutorium 5, instationäre globale Energiebilanz).

**Rechnungen:** alle Zahlen aus `simulation/recherche/r3_skripte/r3_rechnungen.py` (eigene Gleichungen, Standardbibliothek und numpy), Ausgabe in `r3_rechnungen_ausgabe.txt` daneben. Das Skript liest `kaffee_modell.py` aus dem Zweig `origin/claude/kaffee-pruefung-sgvo1r` und vergleicht, wo das Modell eine Funktion hat (`rechne`, `becher`, `zwei_tassen`, `nichtlinear`). Alle Vergleiche stimmen auf besser als 1e-13 K überein. Bezeichnungen: θ = ϑ − ϑ_u (Übertemperatur), C_K = m_K c_p,K = 836,00 J/K, C_M = m_M c_p,M = 121,746 J/K, C_G = C_K + C_M = 957,746 J/K, C_B = m_B c_B, Δϑ = ϑ_1 − ϑ_2 (positiv: Tasse 1 wärmer). Testfälle T01 bis T18 stehen am Ende der Ausgabedatei.

## Übersicht

| Nr. | Erweiterung | Grundlage | Wirkung in Zahlen (Standardwerte, 60 min) | Testfall | Empfehlung |
|---|---|---|---|---|---|
| 1 | Deckel | Ferreira 2025a, Abb. 6 (Volltext): Steigungen 0,0241 und 0,0135 1/min | kA · 0,560 (−44,0 %). Deckel auf beiden Tassen: ϑ_1 44,65 °C, ϑ_2 41,14 °C, Δϑ 3,51 K statt 3,85 K; größter Unterschied bleibt 3,86 K, kommt aber bei 99,5 statt 55,7 min | T03, T04 | **sollte**, als kA-Faktor für beide Tassen; besser kA aus eigener Messung mit Deckel |
| 2 | Bechermaterial | C_B = m c: Massen openLCA 2018, c aus Engineering ToolBox und Suleman & Gas 2024; kA-Faktoren aus Ferreira 2025b (Schätzung) | gleiche Messung: Δϑ von 3,81 K (Pappbecher) bis 2,90 K (Porzellan 310 g); ϑ_1 bleibt 34,04 bis 34,05 °C | T02, T05, T06 | **sollte**: Masse und Material des Bechers als Eingabe, kA aus der Messung. kA-Faktor je Material: **kann**, nur als gekennzeichnete Schätzung |
| 3 | Verdunstung als eigener Term | eigene Herleitung (Stoffübergang, Dampfdruck IAPWS-IF97, gegen NIST geprüft), kalibriert am offenen Lauf von Ferreira 2025a; Condoret 2007 nur Sekundärquelle | Anteil 56 % bei 80 °C, 46 % über 60 min; verdunstet 5,4 bis 11,2 g (Referenz 6,84 g); Referenz ϑ_1 37,61 °C, ϑ_2 33,00 °C, Δϑ 4,60 K | T07 (nur Größenordnung) | **nicht** als Zahl im Werkzeug; **kann** als Text mit Bereich (Reiter Annahmen, Hausaufgabe) |
| 4 | Nichtlineare Wärmeabgabe | Ferreira 2025a (Nu = 0,59 (Gr Pr)^1/4, Gr = 3,4·10^6, also laminar), eigene geschlossene und numerische Lösung | n = 5/4: ϑ_1 36,84 °C, ϑ_2 32,63 °C, Δϑ 4,21 K; Konvektion 5/4 mit Strahlung 4,18 K; n = 4/3: 4,31 K | T08, T12 | **kann**: Schalter „Wärmeabgabe nichtlinear (n = 5/4)“ als Formtest; Funktion `nichtlinear` geprüft |
| 5 | kA aus allen Messpunkten | eigene Herleitung, synthetische Reihen, Monte-Carlo | Streuung von kA: 1,9 % (zwei Punkte), 0,5 bis 0,7 % (Ausgleichsgerade); bei n = 1,25 zwei Punkte 0,340 W/K, Ausgleich 0,297 bis 0,307 W/K | T09, T10 | **muss** (Grundlage für die Vorabmessung der TL): Eingabe der Messreihe, ln-Diagramm mit Gerade und Residuen |
| 6 | Energie sichtbar machen | eigene Herleitung aus dem Modell | Q_1 34,88 kJ, Q_2 38,57 kJ, Q_2 − Q_1 = C_G Δϑ = 3,69 kJ = Fläche zwischen den Kurven Q̇_ab(t); Kaffee-Effekt 2,48 K, Milch-Effekt 1,38 K | T11 | **sollte**: Säulen und Fläche unter Q̇_ab(t). Bilanzraum als Bild: **muss** |
| 7 | Größter Unterschied der Tassen | eigene Herleitung (analytisch), numerisch bestätigt | 3,86 K bei ϑ_K* = 35,38 °C, unabhängig von kA; t* = 55,74 min · (0,3402 W/K)/kA. Mit Becher 3,09 K bei 35,78 °C | T13, T14, T15 | **muss** als Erklärung und Prüffall. Aussage der TL stimmt mit zwei Einschränkungen (Becher, gleiches kA) |
| 8 | Abkühlen nach dem Zugießen | eigene Herleitung | Δϑ(t) = Δϑ(t_Z) exp(−(t − t_Z)/τ_G), τ_G = 46,91 min. Zugabe 60 min, Vergleich 90 min: 2,03 K | T16 | **sollte**: Vergleichszeitpunkt getrennt vom Zugabezeitpunkt (passt zur Messreihe der TL) |
| 9a | Füllhöhe (kA von Tasse 1) | `zwei_tassen(kA1_faktor)`, eigene Rechnung | kA_1 +5 %: Δϑ 2,98 K; +10 %: 2,17 K | T18 | **kann** (zeigt: gleiches kA zählt mehr als kA selbst) |
| 9b | Biot-Zahl als Gültigkeitsprüfung | Ferreira 2025a und 2025b (Volltext), eigene Rechnung | Bi der Keramikwand 0,035; wirksame Bi ≈ 0,05 aus gemessenen 3,5 K Wandabstand | kein Zahlentest nötig | **kann** (Text im Reiter Annahmen) |
| 9c | Nicht vorgewärmter Becher | eigene Herleitung | 80 °C fallen sofort auf 65,98 °C (C_B 255 J/K); Zwei-Punkte-kA dann 2,1-mal zu groß | T17 | **sollte** als Hinweis für Vorabmessung und Versuch |

## 1 Deckel

**Prüfung an der Quelle.** Ferreira (2025a) zeigt in Abb. 6 ln(T_w − T_a) über t für denselben Keramikbecher mit Styropordeckel und offen, je mit Regressionsgerade (im Diagramm abgedruckt): offen y = −0,0241x + 4,1422 (R² = 0,99), mit Deckel y = −0,0135x + 4,2152 (R² = 0,9986), x in min. Bei gleicher Wassermasse ist das Verhältnis der Steigungen das Verhältnis der kA-Werte:

$$f_\mathrm{D} = \frac{kA_\mathrm{Deckel}}{kA_\mathrm{offen}} = \frac{0{,}0135}{0{,}0241} = 0{,}5602, \qquad 1 - f_\mathrm{D} = 44{,}0\,\%$$

Gegenprobe über Tab. 1 der Quelle: h = 9,9 W/(m² K) mit Deckel, (18) offen, also 1 − 9,9/18 = 45 %. Zeitkonstanten 41,49 min offen (der Arbeitswert der Aufgabe, τ_K = 40,95 min) und 74,07 min mit Deckel. **Die 44 % stimmen.** Drei Einschränkungen gehören dazu: (a) Es ist ein *scheinbares* kA, gemittelt über 90 bis 40 °C; die offene Kurve ist nach der Quelle keine Exponentialfunktion. (b) Der Deckel ist 18 mm Styropor auf einem fast vollen Becher; er unterdrückt neben der Verdunstung auch Konvektion und Strahlung der Oberfläche. Eine Untertasse oder ein Kunststoffdeckel dämmt schlechter, und Kondensat tropft zurück; der Faktor liegt dann vermutlich zwischen 0,56 und 1 (Schätzung, nicht gemessen). (c) Die 44 % sind nicht der Anteil der Verdunstung, sondern dessen Obergrenze im Mittel; im Verdunstungsmodell (Abschnitt 3) senkt der Deckel das Zwei-Punkte-kA im Bereich 80 bis 67 °C um 53 %.

**Ins Modell.** Der Deckel gehört auf **beide** Tassen, als Faktor auf das gemessene kA (kA_D = 0,5602 · 0,3402 = 0,1906 W/K). Gleichwertig ist eine Messung mit Deckel: ϑ(10 min) = 72,33 °C statt 67 °C. Am ehrlichsten ist, die Messung der TL mit Deckel direkt einzugeben; der Faktor 0,56 ist nur Vorgabe, wenn keine Deckelmessung vorliegt. Ein Deckel nur auf einer Tasse verändert die Frage (welche Tasse ist besser gedämmt?) und überdeckt den Milch-Effekt völlig:

| Fall (60 min) | ϑ_1 in °C | ϑ_2 in °C | Δϑ in K |
|---|---|---|---|
| A beide offen | 34,05 | 30,19 | 3,85 |
| B beide mit Deckel | 44,65 | 41,14 | 3,51 |
| C nur Tasse 2 (schwarz) mit Deckel | 34,05 | 41,14 | −7,10 |
| D nur Tasse 1 mit Deckel | 44,65 | 30,19 | 14,46 |
| A beide offen, 40 min (Versuch) | 41,51 | 37,81 | 3,70 |
| B beide mit Deckel, 40 min | 51,30 | 48,40 | 2,91 |

Fall D stimmt mit `zwei_tassen(kA1_faktor=0.5602)` überein (Abweichung 3e-14 K). Für Fall C gibt es keine Modellfunktion (kA von Tasse 2 lässt sich dort nur über die Messung ändern).

**Grenzen.** Mit Deckel liegt die Abkühlkurve in der Quelle auf einer Geraden (R² 0,9986): Das Modell der Aufgabe passt mit Deckel *besser*. Dafür ist der Unterschied nach 40 bzw. 60 min kleiner, weil der größte Unterschied erst nach 99,5 min kommt (Abschnitt 7). Für einen Versuch mit Deckel und Messung nach 40 min: 2,91 K statt 3,70 K Unterschied.

**Testfall T03:** kA = 0,1906 W/K (oder ϑ(10 min) = 72,33 °C), Standardwerte, 60 min: ϑ_1 = 44,65 °C, ϑ_2 = 41,14 °C, Δϑ = 3,51 K; Maximum 3,86 K bei 99,5 min. **T04:** kA_1 = 0,3402, kA_2 = 0,1906 W/K: ϑ_1 = 34,05 °C, ϑ_2 = 41,14 °C, Δϑ = −7,10 K.

**Quelle:** Ferreira (2025a), Prüfstatus Volltext (akzeptiertes Autorenmanuskript, siehe Quellenliste). Zitate: „y = -0.0241x + 4.1422“ und „y = -0.0135x + 4.2152“ (Abb. 6); „The linear fit is also included for this run, even though not supported by the physical process taking place.“; „Lids to the cup are prepared by cutting a Styrofoam board 18 mm thick.“

## 2 Bechermaterial

**Wärmekapazität.** Wirkung im Modell über C_B = m c (Funktionen `becher`, `zwei_tassen`): Kaffee und Becher bilden eine gemeinsame Speicherkapazität, auch beim Zugießen. Werte mit Herkunft:

| Becher | Masse | c in J/(kg K) | C_B in J/K | C_B/C_K |
|---|---|---|---|---|
| Keramik, Arbeitswert der Aufgabe | 300 g (Aufgabe) | 850 (Aufgabe, Schätzung) | 255,0 | 0,305 |
| Porzellan | 310 g (openLCA 2018, 300-ml-Becher) | 1070 (ETB), 1050 (Suleman & Gas) | 331,7 | 0,397 |
| Steinzeug | 310 g (wie oben angenommen) | 800 (ETB) | 248,0 | 0,297 |
| Glas | 250 g (Beispiel, wiegen) | 840 (ETB, Suleman & Gas) | 210,0 | 0,251 |
| Edelstahl einwandig | 150 g (Beispiel; Händlerangaben 110 bis 245 g, nicht geprüft) | 490 (ETB „Steel“), 460 (Suleman & Gas), 500 (1.4301, nicht geprüft); gerechnet 500 | 75,0 | 0,090 |
| Edelstahl doppelwandig (Vakuum) | nur die Innenwand zählt, etwa 70 g (Schätzung) | 500 | 35,0 | 0,042 |
| Pappbecher | 8,3 g Papier und 0,1 g PE (openLCA 2018) | 1340 (ETB „Paper“) | 11,1 | 0,013 |

Der Arbeitswert c_B = 850 J/(kg K) liegt zwischen Steinzeug (800) und Porzellan (1050 bis 1070). Für einen Porzellanbecher wäre C_B rund 30 % größer (Hinweis für die TL, keine Änderung der Aufgabe).

**Wirkung bei gleicher Messung** (67 °C nach 10 min; kA = −(C_K + C_B)/t_mess · ln(47/60), so rechnet `becher(kA_neu=True)`):

| Becher | kA in W/K | ϑ_1 in °C | ϑ_2 in °C | Δϑ in K | Δϑ_max in K | t* in min |
|---|---|---|---|---|---|---|
| ohne Becher (Aufgabe) | 0,3402 | 34,05 | 30,19 | 3,85 | 3,86 | 55,7 |
| Keramik 255 J/K | 0,4440 | 34,04 | 30,96 | 3,08 | 3,09 | 54,7 |
| Porzellan 331,7 J/K | 0,4752 | 34,04 | 31,14 | 2,90 | 2,91 | 54,5 |
| Steinzeug 248 J/K | 0,4412 | 34,04 | 30,95 | 3,10 | 3,11 | 54,7 |
| Glas 210 J/K | 0,4257 | 34,05 | 30,85 | 3,19 | 3,20 | 54,8 |
| Edelstahl einwandig 75 J/K | 0,3708 | 34,05 | 30,46 | 3,59 | 3,60 | 55,4 |
| Vakuum (Innenwand) 35 J/K | 0,3545 | 34,05 | 30,32 | 3,72 | 3,73 | 55,6 |
| Pappbecher 11,1 J/K | 0,3448 | 34,05 | 30,24 | 3,81 | 3,82 | 55,7 |

Bemerkenswert: ϑ_1 bleibt bei gleicher Messung fast gleich (34,04 bis 34,05 °C). Der Becher verkleinert den Unterschied, weil er beim späten Zugießen seine gespeicherte Wärme in Tasse 2 mitmischt (ϑ_2 steigt).

**Wirkung über kA.** Hier ist Vorsicht nötig: kA kommt im Modell aus der Messung. Ein anderes Material ändert die Messung; ohne neue Messung kann man kA nur begründet schätzen. Die Wand ist bei einwandigen Bechern fast nie der begrenzende Widerstand (Keramik e/k ≈ 0,004 m² K/W nach Ferreira 2025a gegen 1/h ≈ 0,1 m² K/W außen). Das Material wirkt über die Emissivität (Strahlung rund 30 % der Wandabgabe) und über eine Vakuumwand:

- Metall blank: Aluminiumbecher mit Deckel 0,00983 gegen Keramik 0,0135 1/min (Ferreira 2025b, Abb. 5), Faktor 0,728 für die Wand; mit dem offenen Anteil der Oberseite (0,44, Abschnitt 1) für einen offenen Becher etwa 0,44 + 0,56 · 0,728 = 0,85. Edelstahl ist je nach Oberfläche blank (ε 0,075) bis matt (ε 0,54 bis 0,63, Typ 301; ETB); der Faktor liegt also etwa zwischen 0,85 und 1 (Schätzung).
- Glas: ähnlich wie Keramik (Glas mit Deckel 0,0142 1/min, Ferreira 2025b, Abb. 8), Faktor etwa 1.
- Vakuum doppelwandig: Die Wand fällt weg, es bleibt die offene Oberseite; Faktor etwa 0,44 (Schätzung, Obergrenze für die Wirkung).
- Pappbecher: dünne Wand, ε 0,93 (ETB, „Paper“), Faktor etwa 1 (Schätzung).

Mit diesen Faktoren (bezogen auf kA = 0,4440 W/K des Keramikbechers, Becher eingeschlossen) ergäben sich zum Beispiel: Edelstahl einwandig ϑ(10 min) 66,79 °C, Δϑ(60 min) 3,58 K; Vakuumbecher ϑ(10 min) 72,28 °C, ϑ_1 44,61 °C, ϑ_2 41,21 °C, Δϑ 3,41 K, t* 98,6 min; Pappbecher ϑ(10 min) 63,81 °C, Δϑ 3,65 K. Das sind Schätzungen, keine Modellzahlen.

**Was man ehrlich anbieten kann.** (a) Eingabe „Becher: Masse (wiegen) und Material“ mit den c-Werten oben als Vorgabe; (b) kA aus der eigenen Messung mit genau diesem Becher (ϑ nach 10 min oder Messreihe, Abschnitt 5); (c) höchstens als Zusatz ein Schätzfaktor je Material mit sichtbarem Hinweis „Schätzung, nicht gemessen“. Nicht anbieten: eine Materialauswahl, die kA stillschweigend ändert.

**Grenzen.** Der Becher muss immer die Temperatur des Inhalts haben (vorgewärmt, Abschnitt 9c). Henkel, Boden und Rand sind nicht einzeln modelliert. Massen von Glas- und Edelstahlbechern streuen stark; die TL sollte ihre Becher wiegen (Küchenwaage reicht).

**Testfälle:** T02 Keramik 300 g, 850 J/(kg K): kA = 0,4440 W/K, ϑ_1 = 34,04 °C, ϑ_2 = 30,96 °C, Q_1 = 46,60 kJ, Q_2 = 50,34 kJ. T05 Pappbecher C_B = 11,1 J/K, gleiche Messung: kA = 0,3448 W/K, ϑ_1 = 34,05 °C, ϑ_2 = 30,24 °C. T06 Edelstahl C_B = 75,0 J/K: kA = 0,3708 W/K, ϑ_1 = 34,05 °C, ϑ_2 = 30,46 °C, Δϑ = 3,59 K.

**Quellen:** openLCA (2018), Volltext: „which weighs 310 g“; „The cup weighs 8.3 g and has an inner plastic (polyethylene) coating of 0.1 g.“ Engineering ToolBox, Volltext über das Abrufwerkzeug (Tabellenzeilen vom Werkzeug wiedergegeben): „Porcelain 0.26 1.07“, „Stoneware 0.19 0.8“, „Glass, window 0.2 0.84“, „Steel 0.12 0.49“, „Paper 0.33 1.34“; Emissivität „Stainless Steel, polished“ 0,075, „Porcelain, glazed“ 0,92. Suleman & Gas (2024), Volltext, Tab. 1: „Mug (porcelain) 2400 1050 1.500 0.595“, „Mug (steel) 7817 460 16.30 4.533“. Ferreira (2025b), Volltext: „the aluminum cup took considerably longer to reach 40 °C: 127 min vs 90 min.“

## 3 Verdunstung als eigener Term

**Herleitung.** Energiebilanz des offenen Tasseninhalts mit Massenverlust (u ≈ h' für die Flüssigkeit):

$$m c_p \frac{\mathrm{d}\vartheta}{\mathrm{d}t} = -kA_\mathrm{tr}\,(\vartheta - \vartheta_\mathrm{u}) - \dot m_\mathrm{v}\,\Delta h_\mathrm{v}(\vartheta), \qquad \frac{\mathrm{d}m}{\mathrm{d}t} = -\dot m_\mathrm{v}$$

$$\dot m_\mathrm{v} = \beta A\,\bigl[\rho_\mathrm{v,s}(\vartheta) - \varphi\,\rho_\mathrm{v,s}(\vartheta_\mathrm{u})\bigr], \qquad \rho_\mathrm{v,s} = \frac{p_\mathrm{s}(T)\,M_\mathrm{W}}{R\,T}$$

kA_tr fasst Konvektion und Strahlung (trocken) zusammen. p_s nach IAPWS-IF97 (eigene Umsetzung, gegen NIST auf 0,007 % geprüft), Δh_v aus der NIST-Tabelle (2382,0 kJ/kg bei 50 °C, 2308,0 kJ/kg bei 80 °C; der Arbeitswert 2380 kJ/kg passt). Die Temperaturabhängigkeit steckt im Dampfdruck: p_s = 47,41 kPa bei 80 °C, 7,38 kPa bei 40 °C.

**Stoffübergang.** (a) Theoretisch über die Lewis-Analogie (Chilton-Colburn) β = h/(ρ c_p) · Le^(−2/3) mit freier Konvektion über der heißen Oberfläche (Nu = 0,54 Ra^(1/4), L = D/4, Auftrieb aus Temperatur und Wasserdampf, Luftwerte bei 42,5 °C aus Ferreira 2025a, Le = 0,85): β = 0,0120 m/s bei 80 °C bis 0,0084 m/s bei 40 °C, βA = 4,8·10^−5 bis 3,4·10^−5 m³/s für eine randvolle Öffnung (D_i = 7,16 cm, A = 40,3 cm²). (b) Empirisch am offenen Lauf von Ferreira (2025a): Abtastung je 1 K von 90 bis 40 °C wie in der Quelle, m_w c_w = 1020,8 J/K (abgeleitet aus h = 9,9 W/(m² K), A = 232 cm², τ = 74,07 min, also etwa 244 g Wasser), kA_tr aus der Deckelsteigung. Ergebnis (φ = 0,5):

| Kalibrierung | βA in m³/s | Zeit 90 → 40 °C | verdunstet | Steigung |
|---|---|---|---|---|
| ohne Becher-C, Ziel Steigung 0,0241 | 2,32·10^−5 | 52,0 min | 9,6 g | 0,0241 |
| ohne Becher-C, Ziel 11 g | 3,06·10^−5 | 45,8 min | 11,0 g | 0,0274 |
| Becher-C 300 J/K, Ziel Steigung 0,0241 (Referenz) | 3,01·10^−5 | 52,0 min | 12,4 g | 0,0241 |
| Becher-C 300 J/K, Ziel 11 g | 2,42·10^−5 | 56,8 min | 11,0 g | 0,0221 |

Gemessen sind in der Quelle 11 g und rund 55 min. Erst mit der Wärmekapazität des Bechers passen Steigung, Masse und Zeit zusammen (12,4 statt 11 g, 52 statt etwa 55 min). Das kalibrierte βA ist 0,62- bis 0,89-mal der theoretische Wert: gleiche Größenordnung, die Oberfläche liegt unter dem Rand.

**Übertragung auf die Aufgabe.** Die Aufgabe übernimmt τ = 41 min von Ferreiras Becher für 200 ml. Folgerichtig ist die Übertragung proportional zur Wärmekapazität (βA · C_K/1320,8 J/K = 1,90·10^−5 m³/s); kA_tr folgt dann aus der Messung 67 °C nach 10 min. Milch verdunstet nicht eigens, das Wasser im Gemisch schon.

| Variante | kA_tr in W/K | ϑ_1 in °C | ϑ_2 in °C | Δϑ in K | verdunstet Tasse 1 / 2 | Anteil bei 80 °C | Anteil über 60 min |
|---|---|---|---|---|---|---|---|
| Referenz: ohne Becher, proportional, φ 0,5 | 0,1589 | 37,61 | 33,00 | 4,60 | 5,72 / 6,84 g | 56,5 % | 45,9 % |
| wie Referenz, φ 0,3 | 0,1560 | 37,42 | 32,83 | 4,59 | 5,94 / 7,06 g | 57,3 % | 47,2 % |
| wie Referenz, φ 0,7 | 0,1619 | 37,79 | 33,17 | 4,62 | 5,49 / 6,62 g | 55,8 % | 44,6 % |
| ohne Becher, gleiche Öffnung wie Ferreira | 0,0543 | 39,85 | 34,79 | 5,06 | 9,49 / 11,15 g | 85,7 % | 79,7 % |
| ohne Becher, proportional, aus Ziel 11 g | 0,1943 | 36,87 | 32,42 | 4,45 | 4,52 / 5,44 g | 46,1 % | 35,8 % |
| Becher 255 J/K, proportional | 0,2074 | 37,59 | 33,89 | 3,70 | 7,77 / 8,92 g | 56,5 % | 45,9 % |
| Becher 255 J/K, gleiche Öffnung | 0,1577 | 38,39 | 34,55 | 3,83 | 9,57 / 10,93 g | 67,4 % | 57,5 % |

Zum Vergleich linear (Aufgabe): 34,05 °C, 30,19 °C, 3,85 K. Das scheinbare kA = Q̇_ab/(ϑ − ϑ_u) fällt in der Referenz von 0,366 W/K bei 80 °C auf 0,256 W/K bei 40 °C (Anteil der Verdunstung 56,5 % bzw. 37,9 %). Daher liegen Messpunkte nach 60 min einige Kelvin über der linearen Kurve, wie die Lösung für den Versuch erwartet. Bei 79 °C gibt die Referenz 11,93 W Verdunstung von 21,31 W insgesamt (56 %); die Lösung zitiert Condoret mit 12,0 von 22,7 W (53 %). Das passt in der Größenordnung, ist aber kein unabhängiger Beleg, solange Condoret nicht eingesehen ist.

**Grenzen.** Ein Parameter (βA) aus einem fremden Becher, Luftfeuchte nicht bekannt (Einfluss klein: 6,62 bis 7,06 g), Übertragungsregel unsicher (5,44 bis 11,15 g), βA in Wirklichkeit temperaturabhängig (Theorie: 4,8 auf 3,4·10^−5 m³/s von 80 auf 40 °C) und bei hoher Dampfkonzentration größer (Stefan-Faktor 1,24 bei 80 °C, 1,08 bei 60 °C, 1,03 bei 40 °C; nicht im Modell). Umrühren erhöht die Verdunstung (Ferreira 2025a: 11 g auf 15 g, h_schein 18 auf 22 W/(m² K)), die Wand bleibt unbeeinflusst. **Größenordnung belastbar, Einzelzahlen nicht:** Anteil an der Wärmeabgabe zu Beginn etwa 45 bis 60 %, über die Stunde 35 bis 50 %, verdunstete Masse 5 bis 11 g in 60 min (Obergrenze, wenn alle Wärme verdunstete: Q_2/Δh_v = 16,2 g). Die Angabe „höchstens rund 8 g“ der Lösung gilt für die proportionale Übertragung, nicht für einen Becher mit großer Öffnung.

**Passt das zu Tutorium 5?** Formal ja: Q̇_v = ṁ_v Δh_v ist ein Term der globalen Energiebilanz mit Massenstrom über die Systemgrenze. Der Stoffübergangskoeffizient und der Dampfdruck gehen aber über Tutorium 5 hinaus. Empfehlung: kein Regler und keine Kurve „mit Verdunstung“; im Reiter „Annahmen“ ein Absatz mit der Größenordnung (Bereich, als Abschätzung gekennzeichnet) und der Verweis auf die Hausaufgabe (Deckel, Waage). Der Deckel (Abschnitt 1) ist die ehrliche Art, Verdunstung im Werkzeug sichtbar zu machen.

**Testfall T07 (nur Größenordnung, nicht gegen Messung getestet):** βA = 1,903·10^−5 m³/s, φ = 0,5, kA_tr = 0,1589 W/K (aus 67 °C nach 10 min), RK4 mit 2 s: ϑ_1 = 37,61 °C, ϑ_2 = 33,00 °C, Δϑ = 4,60 K, verdunstet 5,72 g und 6,84 g.

**Quellen:** Ferreira (2025a), Volltext: „The mass of water evaporated was also measured, with 11 g and 15 g in the non-stirred and the stirred runs, respectively.“; „Mixing the liquid did accelerate the cooling, from 55 to 45 min, approximately.“ Condoret (2007), Prüfstatus Sekundärquelle (Angabe 12,0 von 22,7 W bei 79 °C, Tab. 2, nach `Kaffee_Loesung.md`, Abschnitt Quellen der Arbeitswerte; die Zeitschriftenseite journals.flvc.org antwortete dem Abrufwerkzeug mit HTTP 403; die bibliografischen Angaben 41(2), 137 bis 143 stehen in der Literaturliste von Suleman & Gas 2024); kein Zitat. NIST WebBook, Volltext (Tabelle über das Abrufwerkzeug): Zeile „80 | 47.414 | 335.01 | 2643.0“ (°C, kPa, h' und h'' in kJ/kg). IAPWS-IF97: nicht geprüft (Koeffizienten aus dem Gedächtnis umgesetzt; die Übereinstimmung mit NIST an neun Stützstellen auf 0,007 % bestätigt die Umsetzung). Nu = 0,54 Ra^(1/4) für die waagerechte Platte, Lewis-Analogie und Le = 0,85: nicht geprüft (Lehrbuchwissen, hier nicht an einer Quelle eingesehen); deshalb dient die theoretische Rechnung nur zur Kontrolle der Größenordnung.

## 4 Nichtlineare Wärmeabgabe

**Herleitung.** Freie Konvektion: Nu ∝ Ra^(1/4) (laminar) gibt h ∝ θ^(1/4), also Q̇ ∝ θ^(5/4); Nu ∝ Ra^(1/3) (turbulent) gibt Q̇ ∝ θ^(4/3). Für die Becherwand ist Gr = 3,423·10^6 (Ferreira 2025a, L = 9 cm), Ra = Gr Pr ≈ 2,5·10^6, weit unter dem Umschlag bei etwa 10^9: **für eine Tasse gilt 5/4.** 4/3 bräuchte eine etwa 0,7 m hohe Wand (eigene Abschätzung über Ra ∝ L³). Strahlung: εσA(T⁴ − T_u⁴); linearisiert h_r = 7,54 W/(m² K) bei 90 °C und 5,88 W/(m² K) bei 40 °C (ε = 0,93), in Ferreira 2025a „7.5 to 6“. Mit C dθ/dt = −c θ^n und Trennung der Variablen:

$$\theta^{1-n} = \theta_0^{1-n} + \frac{(n-1)\,c\,t}{C}, \qquad c = \frac{(\theta_\mathrm{mess}^{1-n} - \theta_{\mathrm{K},0}^{1-n})\,m_\mathrm{K} c_{p,\mathrm{K}}}{(n-1)\,t_\mathrm{mess}}$$

c folgt aus derselben Messung (67 °C nach 10 min), gilt für beide Tassen.

**Nachrechnung.** Eigene geschlossene Lösung, RK4 mit 0,5 s und `nichtlinear(n)` stimmen auf 4e-14 K überein:

| Modell (60 min) | ϑ_1 in °C | ϑ_2 in °C | Δϑ in K |
|---|---|---|---|
| linear (Aufgabe) | 34,05 | 30,19 | 3,85 |
| n = 5/4 (c = 0,12606 W/K^1,25) | 36,84 | 32,63 | 4,21 |
| n = 4/3 (c = 0,09055 W/K^(4/3)) | 37,65 | 33,34 | 4,31 |
| Konvektion 5/4 und Strahlung (33 % bei 65 °C, Ferreira 2025a) | 36,62 | 32,43 | 4,18 |
| Verdunstung (Referenz Abschnitt 3) | 37,61 | 33,00 | 4,60 |

**Wirkung.** Bei gleicher 10-Minuten-Messung kühlen beide Tassen später langsamer ab: ϑ_1 und ϑ_2 steigen um 2,4 bis 2,8 K (n = 5/4), der Unterschied um 0,36 K (9 %). Die Aussage (Tasse 1 wärmer) wird stärker, nicht schwächer. Die Strahlung macht die Wand-Abgabe fast linear (Ferreira findet bei Deckel gerade ln-Kurven); die eigentliche Nichtlinearität des offenen Bechers kommt von der Verdunstung.

**Grenzen.** Formtest mit gemeinsamem Gesetz für beide Tassen; c ist an einen einzigen Punkt angepasst. Die Potenz ersetzt nicht die Verdunstung (deren scheinbares kA fällt stärker, Abschnitt 3).

**Testfall T08:** n = 5/4, c aus der Messung = 0,12606 W/K^1,25: ϑ_1 = 36,84 °C, ϑ_2 = 32,63 °C, Δϑ = 4,21 K.

**Quellen:** Ferreira (2025a), Volltext: „Nu = 0.59 (GrPr)1/4“ (Gl. 5, Hochstellung im Textauszug verloren); „with a contribution of 6.8/10.2 = 67 % for convection and 33 % for radiation“. Vollmer (2009), Abstract: „The cooling of objects is often described by a law, attributed to Newton, which states that the temperature difference“ (Wortlaut über das Abrufwerkzeug). Turbulente Korrelation Nu = 0,10 Ra^(1/3): nicht geprüft (nur Suchergebnis zu Vorlesungsskripten).

## 5 kA aus allen Messpunkten

**Herleitung.** Mit y_i = ln(θ_i/θ_0) gilt im Modell y = −a t, a = kA/(m c_p):

- Ursprungsgerade: a = −Σ t_i y_i / Σ t_i² (t_i > 0), Standardfehler s_a = s/√(Σ t_i²) mit s² = Σ(y_i + a t_i)²/(N − 1).
- Freier Achsenabschnitt: ln θ_i = b − a t_i, gewöhnliche Ausgleichsrechnung; b ≠ ln θ_0 zeigt einen Anlauf (Becher nicht vorgewärmt, Mischen) oder Krümmung.
- Gewichtet: σ(ln θ) = σ_ϑ/θ, also Gewicht θ²; späte Punkte zählen weniger.

**Synthetischer Datensatz** (Messung alle 10 min bis 60 min, Rauschen gleichverteilt ±0,3 K, dann auf 0,1 K gerundet wie ein Thermometer, Samen 20261104):

| t in min | 0 | 10 | 20 | 30 | 40 | 50 | 60 |
|---|---|---|---|---|---|---|---|
| wahr, n = 1 | 80,00 | 67,00 | 56,82 | 48,84 | 42,59 | 37,70 | 33,86 |
| gemessen, n = 1 | 80,1 | 67,3 | 56,9 | 49,1 | 42,7 | 37,4 | 33,7 |
| wahr, n = 1,25 | 80,00 | 67,00 | 57,34 | 50,04 | 44,43 | 40,08 | 36,65 |
| gemessen, n = 1,25 | 80,2 | 67,1 | 57,5 | 50,0 | 44,7 | 39,9 | 36,4 |

| Auswertung | n = 1: kA in W/K | ϑ_K(60) vorhergesagt | n = 1,25: kA in W/K | ϑ_K(60) vorhergesagt |
|---|---|---|---|---|
| zwei Punkte (0, 10 min) | 0,3337 | 34,26 °C | 0,3419 | 33,76 °C |
| Ursprungsgerade | 0,3423 ± 0,0013 | 33,74 °C | 0,3090 ± 0,0038 | 35,86 °C |
| freier Achsenabschnitt | 0,3444 ± 0,0021 (b − ln θ_0 = +0,007) | 33,61 °C | 0,3007 ± 0,0051 (b − ln θ_0 = −0,026) | 36,44 °C |
| gewichtet, frei | 0,3416 | 33,78 °C | 0,3094 | 35,83 °C |
| wahr | 0,3402 | 33,86 °C | (n = 1,25) | 36,65 °C |

kA je 10-Minuten-Intervall, n = 1: 0,334; 0,346; 0,331; 0,346; 0,370; 0,333 (nur Rauschen). n = 1,25: 0,342; 0,318; 0,311; 0,271; 0,301; 0,270 (fallender Trend, aber verrauscht). Residuen der freien Geraden bei n = 1,25: +0,026; −0,004; −0,016; −0,023; −0,002; −0,002; +0,020, also bogenförmig (außen positiv, innen negativ): das Kennzeichen gekrümmter Kurven.

**Unsicherheit (Monte-Carlo, je 20 000 Reihen, Rauschen ±0,3 K gleichverteilt).** n = 1: alle Verfahren erwartungstreu (Mittel 0,3402 W/K); Streuung 0,0065 W/K (1,92 %) mit zwei Punkten, 0,0018 (0,52 %) Ursprungsgerade, 0,0022 (0,66 %) frei, 0,0017 (0,49 %) gewichtet. Fortgepflanzt auf ϑ_K(60 min) (dϑ_K/dkA = −59,7 K/(W/K)): 0,39 K gegen 0,11 bis 0,13 K. n = 1,25: zwei Punkte im Mittel 0,3402, Ausgleich 0,297 (frei) bis 0,307 W/K: ein systematischer Unterschied von 10 %, viel größer als das Rauschen.

**Folgerung.** Das kA aus zwei Punkten gilt für die ersten 10 min; ist die Kurve gekrümmt (offener Becher), sagt es die späten Werte 2 bis 3 K zu tief voraus. Die Ausgleichsgerade über die ganze Reihe trifft im Mittel, beschreibt aber nur den Messbereich (der 60-min-Punkt ist dann keine Vorhersage mehr). Wichtig für die TL: **Der Unterschied Δϑ(60 min) hängt kaum von kA ab** (kA ±10 %: 3,816 bzw. 3,860 K statt 3,853 K), weil 60 min nahe am Maximum liegen (Abschnitt 7). Die Einzeltemperaturen hängen dagegen stark davon ab (ϑ_1 35,96 bzw. 32,36 °C statt 34,05 °C).

**Empfehlung für das Werkzeug (muss):** Eingabe einer Messreihe (Zeit, Temperatur, Raumtemperatur); Auswertung mit Ursprungsgerade als Standard und freiem Achsenabschnitt zum Vergleich; Diagramm ln(θ/θ_0) über t mit Gerade und Residuen; Ausgabe kA mit Standardfehler; Hinweis, wenn die Residuen bogenförmig sind („Kurve gekrümmt, Verdunstung?“). Für die Vorabmessung der TL: Becher vorwärmen, Uhr erst nach dem Temperaturausgleich starten (Abschnitt 9c), Deckelreihe und offene Reihe getrennt auswerten.

**Testfälle:** T09 exakte Daten 80,00; 67,00; 56,82; 48,84; 42,59; 37,70; 33,86 °C: kA = 0,3402 W/K mit allen Verfahren. T10 Reihe 80,1; 67,3; 56,9; 49,1; 42,7; 37,4; 33,7 °C (ϑ_u 20 °C): zwei Punkte 0,3337 W/K, Ursprungsgerade 0,3423 ± 0,0013 W/K, frei 0,3444 ± 0,0021 W/K.

**Quelle:** eigene Herleitung; Ferreira (2025a) wertet ebenso über ln(T_w − T_a) gegen t mit freiem Achsenabschnitt aus (Volltext).

## 6 Energie sichtbar machen

**Herleitung.** Q(t) = ∫ Q̇_ab dt mit Q̇_ab = kA(ϑ − ϑ_u) ergibt im Modell Q = m c_p (ϑ_0 − ϑ(t)). Weil beide Tassen mit derselben Energie beginnen (Kaffee und Milch), gilt zu jedem Zugabezeitpunkt t_Z:

$$\vartheta_1(t_\mathrm{Z}) - \vartheta_2(t_\mathrm{Z}) = \frac{Q_2(t_\mathrm{Z}) - Q_1(t_\mathrm{Z})}{m_\mathrm{K} c_{p,\mathrm{K}} + m_\mathrm{M} c_{p,\mathrm{M}}}$$

**Zahlen (direkt aus dem Modell):** Q_1 = 34,88 kJ, Q_2 = 38,57 kJ (geschlossen und als Trapezfläche mit 1 s gleich auf 0,1 J), Q_2 − Q_1 = 3,69 kJ = C_G · 3,85 K. Q̇_ab,1(0) = 17,17 W, Q̇_ab,2(0) = 20,41 W; bei 60 min 4,78 W und 4,72 W: Die Kurven Q̇_ab(t) schneiden sich bei 55,7 min, genau dort, wo der Unterschied am größten ist. Zerlegung (Teil f): Kaffee-Effekt 2,48 K (2,37 kJ), Milch-Effekt 1,38 K (1,32 kJ) bei 5 °C; bei 60 °C Milch −3,67 K, Summe −1,19 K. Mit Becher: Q_1 = 46,60 kJ, Q_2 = 50,34 kJ, (C_G + C_B) Δϑ = 3,73 kJ; davon gibt der Becher in Tasse 2 C_B(80 °C − ϑ_K) = 11,77 kJ ab.

**Darstellung.** (a) Zwei Säulen Q_1 und Q_2 mit markiertem Unterschied „= C_G · Δϑ“. (b) Diagramm Q̇_ab(t) beider Tassen; die Fläche zwischen den Kurven bis zum Zugabezeitpunkt ist C_G Δϑ, sie wächst bis zum Schnittpunkt und schrumpft danach. Das widerlegt „die Energie bleibt ja erhalten“ (Frage 1) auf einen Blick. (c) Bilanzraum: Tasse mit gestrichelter Grenze um den Inhalt (in Teil g um Inhalt und Becher), Pfeil Q̇_ab nach außen, beim Zugießen ein Pfeil „Milch“ in den Bilanzraum; Pfeilbreite proportional zu Q̇_ab.

**Direkt aus dem Modell:** ϑ(t) beider Tassen, Q̇_ab(t), Q(t), Q_2 − Q_1, Kaffee- und Milch-Effekt, Anteil des Bechers. **Nicht aus dem Modell** (nur mit Erweiterung oder gar nicht): Aufteilung von Q̇_ab auf Konvektion, Strahlung und Verdunstung; verdunstete Masse; Verteilung über die Becherfläche; Erwärmung der Raumluft; Wärme, die die Milch vor dem Zugießen aus der Umgebung aufnimmt (nur über die eingegebene Milchtemperatur). In Tasse 1 lassen sich Kaffee und Milch nach dem Mischen nicht getrennt bilanzieren; die Zerlegung ist eine Rechenhilfe, keine Messgröße.

**Testfall T11:** Standardwerte, 60 min: Q_1 = 34,88 kJ, Q_2 = 38,57 kJ, Q_2 − Q_1 = 3,69 kJ, Q̇_ab(0) = 17,17 W und 20,41 W.

**Quelle:** eigene Herleitung.

## 7 Größter Unterschied der Tassen

**Behauptung:** „Der größte Unterschied der Tassen ist bei jedem kA rund 3,9 K und tritt ein, wenn der schwarze Kaffee etwa 35 °C erreicht; Dämmung verzögert ihn nur.“

**Herleitung** (Vergleich direkt nach dem Zugießen bei t_Z, gleiches kA, C_T = 0 oder C_B):

$$\frac{\mathrm{d}\Delta\vartheta}{\mathrm{d}t_\mathrm{Z}} = \frac{\dot Q_\mathrm{ab,2} - \dot Q_\mathrm{ab,1}}{C_\mathrm{G}} = \frac{kA\,(\vartheta_\mathrm{K} - \vartheta_1)}{C_\mathrm{G}} = 0 \;\Longleftrightarrow\; \vartheta_\mathrm{K}(t_\mathrm{Z}) = \vartheta_1(t_\mathrm{Z})$$

Der Unterschied ist am größten, wenn der schwarze Kaffee gerade so warm ist wie der Milchkaffee (Schnittpunkt der Kurven). Dort ist er so groß wie der Temperatursturz beim Zugießen:

$$\Delta\vartheta_\mathrm{max} = \frac{m_\mathrm{M} c_{p,\mathrm{M}}\,(\vartheta_\mathrm{K}^* - \vartheta_\mathrm{M})}{C_\mathrm{G}}, \qquad \theta_\mathrm{K}^* = \theta_{\mathrm{K},0}\left(\frac{\theta_{1,0}}{\theta_{\mathrm{K},0}}\right)^{C_\mathrm{G}/C_\mathrm{M}}, \qquad t^* = \frac{\ln(\theta_{\mathrm{K},0}/\theta_{1,0})}{kA\,(1/C_\mathrm{K} - 1/C_\mathrm{G})}$$

kA kommt nur in t* vor. Der Grund: Δϑ hängt nur von kA · t ab. Das gilt für jedes gemeinsame Verlustgesetz Q̇ = c · g(θ), also auch für n = 5/4. Mit Becher: C_K → C_K + C_B und C_G → C_G + C_B.

**Zahlen** (analytisch, numerisch auf 1 s bestätigt):

| Fall | t* in min | ϑ_K* in °C | Δϑ_max in K |
|---|---|---|---|
| ohne Becher, kA = 0,3402 W/K | 55,74 | 35,38 | 3,862 |
| ohne Becher, kA halb / doppelt | 111,49 / 27,87 | 35,38 | 3,862 |
| ohne Becher, Deckel (0,56 kA) | 99,51 | 35,38 | 3,862 |
| Becher 255 J/K, kA = 0,4440 W/K | 54,70 | 35,78 | 3,090 |
| Becher 255 J/K, kA halb | 109,39 | 35,78 | 3,090 |
| Vakuumbecher 35 J/K, 0,45 · 0,4440 W/K | 98,58 | 35,45 | 3,734 |
| nichtlinear n = 5/4 (c beliebig) | 55,25 (bei c aus der Messung) | 38,18 | 4,218 |
| nichtlinear n = 4/3 | 55,08 | 39,00 | 4,322 |
| Verdunstungsmodell (Referenz) | etwa 54 | 39,3 | 4,62 |
| Verdunstungsmodell, nur Wand gedämmt (kA_tr · 0,5) | etwa 71 | 40,2 | 4,86 |
| Milch 0 °C / 10 °C / 20 °C | 59,83 / 51,71 / 43,80 | 33,92 / 36,97 / 40,59 | 4,31 / 3,43 / 2,62 |
| Kaffee anfangs 70 °C / 90 °C | 58,19 / 54,01 | 32,07 / 38,72 | 3,44 / 4,29 |
| erwärmte Milch 60 °C | 13,95 | 62,68 | +0,34 (dann Vorzeichenwechsel, bei 60 min −1,19) |

**Ergebnis.** Die Aussage stimmt im Modell der Aufgabe (ohne Becher, gleiches konstantes kA beider Tassen, Standardwerte): 3,86 K bei 35,4 °C, unabhängig von kA; ein kleineres kA verschiebt den Zeitpunkt nur (Deckel: von 56 auf 100 min). Einschränkungen: (1) **Mit Becher** ist der Höchstwert kleiner, 3,09 K bei 35,8 °C. „Dämmung“ durch einen schweren Becher verkleinert ihn also; nur „Dämmung“, die kA beider Tassen gleich senkt und keine Wärme speichert (Deckel, Vakuumwand), verzögert ihn nur. (2) Bei **ungleichem kA** (Deckel auf einer Tasse, Füllhöhe) gilt die Unabhängigkeit nicht. (3) Mit **Verdunstung** als eigenem Term ändert eine Dämmung der Wand das Verlustgesetz; dann verschiebt sich auch der Höchstwert leicht (4,62 auf 4,86 K). (4) „Rund 3,9 K“ und „35 °C“ hängen von ϑ_K,0, ϑ_M, ϑ_u und vom Verhältnis C_M/C_G ab (Tabelle). Vorschlag für den Text im Werkzeug: „Der Unterschied ist am größten, wenn der schwarze Kaffee so warm ist wie der Milchkaffee; dann ist er so groß wie der Sprung beim Zugießen (hier 3,86 K bei 35,4 °C). Ein kleineres kA verschiebt diesen Zeitpunkt nach hinten, ändert den Wert aber nicht.“

**Testfälle:** T14 ohne Becher, beliebiges kA: Δϑ_max = 3,86 K bei ϑ_K* = 35,38 °C, t* = 55,74 min · (0,3402 W/K)/kA. T15 Becher 255 J/K: 3,09 K bei 35,78 °C, t* = 54,70 min bei kA = 0,4440 W/K. T12 n = 5/4: 4,22 K bei 38,18 °C, t* = 55,25 min. T13 Milch 60 °C: +0,34 K bei 13,95 min (ϑ_K* = 62,68 °C), bei 60 min −1,19 K.

**Quelle:** eigene Herleitung.

## 8 Abkühlen nach dem Zugießen

**Herleitung.** Nach t_Z enthalten beide Tassen dasselbe (C_G, mit Becher C_G + C_B) und haben dasselbe kA. Die Differenz der beiden Bilanzen gibt dΔϑ/dt = −kA Δϑ/C_G, also

$$\Delta\vartheta(t) = \Delta\vartheta(t_\mathrm{Z})\,\exp\!\left(-\frac{kA\,(t - t_\mathrm{Z})}{C_\mathrm{G}}\right), \qquad \tau_\mathrm{G} = \frac{C_\mathrm{G}}{kA} = 46{,}91\,\mathrm{min}$$

Halbwertszeit 32,52 min; mit Becher τ = 45,52 min. **Ja, im linearen Modell klingt der Unterschied exakt exponentiell ab.** Bei nichtlinearer Abgabe (n = 5/4) nicht genau: 3,48 / 2,43 / 1,48 K nach 10 / 30 / 60 min statt 3,40 / 2,22 / 1,17 K.

| Zugabe | Vergleich | Δϑ in K | ϑ_1 / ϑ_2 in °C |
|---|---|---|---|
| 60 min | 60 / 70 / 90 / 120 min | 3,85 / 3,11 / 2,03 / 1,07 | 34,05 / 30,19 bei 60 min; 27,41 / 25,38 bei 90 min |
| 40 min (Versuch) | 40 / 50 / 60 min | 3,70 / 2,99 / 2,42 | 41,51 / 37,81 bei 40 min |

**Fester Trinkzeitpunkt.** Wird zum festen Zeitpunkt t_V verglichen, gilt d[Δϑ(t_V)]/dt_Z ∝ (C_K + C_B) θ_K,0 (a_K − a_G) e^(−a_K t_Z) − a_G C_M θ_M mit a = kA/C. Für Milch unter Raumtemperatur (θ_M < 0) ist das immer positiv: Je später die Milch, desto kälter Tasse 2 bei t_V; „Milch sofort“ ist für einen festen Trinkzeitpunkt immer am besten. Zahlen für t_V = 60 min und Zugabe nach 0 / 10 / 20 / 30 / 40 / 50 / 60 min: 0,00 / 0,57 / 1,16 / 1,77 / 2,42 / 3,11 / 3,85 K.

**Folgerung für den Versuch:** Nach dem Zugießen zügig messen; jede 10 min Verzug kosten 19 % des Unterschieds (Faktor e^(−10/46,91) = 0,808). Im Werkzeug: Regler „Zugabe“ und Regler „Vergleich“ getrennt, Vergleich ≥ Zugabe.

**Testfall T16:** Zugabe 60 min, Vergleich 90 min: Δϑ = 3,85 K · exp(−30/46,91) = 2,03 K (ϑ_1 = 27,41 °C, ϑ_2 = 25,38 °C). Mit Becher: 3,08 K auf 1,59 K.

**Quelle:** eigene Herleitung.

## 9 Was sonst sinnvoll ist

**9a Füllhöhe.** Tasse 1 enthält 230 statt 200 ml; die benetzte Wand ist größer, kA kann größer sein. `zwei_tassen(kA1_faktor)` und eigene Rechnung gleich: Faktor 1,05: ϑ_1 = 33,18 °C, Δϑ = 2,98 K; 1,10: 32,36 °C, 2,17 K; 1,15: 31,59 °C, 1,40 K (ϑ_2 bleibt 30,19 °C). Ein Unterschied von 5 % im kA der beiden Tassen kostet 0,87 K des Effekts, ein Fehler von 10 % in kA beider Tassen nur 0,04 K. Bei Keramik ist der Einfluss vermutlich klein (Ferreira 2025a: die ganze Außenwand ist fast gleich warm, auch am Rand), Größe nicht gemessen. Empfehlung kann; im Versuch gleiche Becher und gleiche Unterlage. **Testfall T18:** kA_1 = 1,05 · 0,3402 W/K: ϑ_1 = 33,18 °C, Δϑ = 2,98 K.

**9b Biot-Zahl, ideale Durchmischung.** Wand: Bi = h e/k = 10 · 0,0052/1,5 = 0,035. Kaffee nur mit Wärmeleitung: Bi = h (V/A)/k_W ≈ 10 · 0,01/0,6 = 0,17, also grenzwertig; tatsächlich mischt freie Konvektion im Kaffee. Aus der Messung von Ferreira (2025b: Außenwand zu Beginn rund 3,5 K kälter als das Wasser) folgt h_i ≈ 10 · 66,5/3,5 ≈ 190 W/(m² K) und eine wirksame Biot-Zahl h_a/h_i ≈ 0,05; Rühren ändert die Abgabe durch die Wand nicht (Ferreira 2025a: h 9,9 gegen 10,2). Der Becher folgt dem Inhalt mit einer Zeitkonstante von rund C_B/(h_i A_i) ≈ 255/(190 · 0,02) ≈ 70 s. Die Annahmen „ideal durchmischt“ und „Becher so warm wie der Inhalt“ sind damit gut begründet. Empfehlung kann (Text im Reiter Annahmen, Verweis auf Frage 3 der Sammlung).

**9c Nicht vorgewärmter Becher.** Ein Becher bei 20 °C senkt 80 °C Kaffee nach dem Ausgleich auf (C_K ϑ_K,0 + C_B ϑ_u)/(C_K + C_B) = 65,98 °C (C_B 255 J/K) bzw. 62,96 °C (331,7 J/K): ein Sprung von 14 bis 17 K, größer als der untersuchte Effekt. Startet die Uhr beim Eingießen mit ϑ_0 = 80 °C, misst man nach 10 min 56,01 °C, und das Zwei-Punkte-kA ohne Becher wird 0,7112 W/K, 2,1-mal zu groß. Empfehlung sollte (Hinweis im Reiter Versuche und für die Vorabmessung: vorwärmen oder Uhr erst nach etwa 2 min starten; die freie Ausgleichsgerade fängt einen Anlauf teilweise ab). **Testfall T17:** C_B = 255 J/K bei 20 °C, Kaffee 80 °C: Ausgleich auf 65,98 °C (−14,02 K).

**Quellen:** Ferreira (2025b), Volltext: „the outside face of the ceramic mug is around 3.5 °C lower than the water one at the early stages of the process“. Ferreira (2025a), Volltext: „Stirring the liquid has minimal effect on heat transfer through the walls of the container, as the external transfer to the air is the limiting step.“

## Didaktisch ergiebige Effekte (für Vorhersagefragen)

1. **Deckel auf beide Tassen:** Wird der Unterschied größer oder kleiner? Nach 60 min kleiner (3,51 statt 3,85 K), sein Höchstwert aber gleich (3,86 K), nur später (100 statt 56 min). Überrascht, weil „besser dämmen“ meist als „mehr Effekt“ erwartet wird.
2. **Wann ist der Unterschied am größten?** Genau wenn der schwarze Kaffee so warm ist wie der Milchkaffee; dann ist er gleich dem Sprung beim Zugießen. Im Diagramm sichtbar als Schnittpunkt der Kurven und der Kurven Q̇_ab(t).
3. **Schwerer Becher:** Porzellan statt Pappe senkt den Unterschied (3,81 auf 2,90 K), obwohl Tasse 1 gleich warm bleibt (34,05 °C). Der Becher gibt seine Wärme beim späten Zugießen an Tasse 2 ab.
4. **Erwärmte Milch (60 °C):** Erst ist „sofort“ wärmer (bis +0,34 K nach 14 min), nach 60 min „später“ (−1,19 K). Die Antwort hängt vom Zeitpunkt ab.
5. **Fester Trinkzeitpunkt:** Je früher die kalte Milch, desto wärmer der Kaffee beim Trinken, ohne Ausnahme (0,57 K Nachteil schon bei Zugabe nach 10 min, 3,85 K nach 60 min).
6. **Robuster Unterschied:** kA um 10 % falsch verschiebt ϑ_1 um 1,7 bis 1,9 K, den Unterschied nach 60 min aber nur um 0,04 K. Ein Unterschied von 5 % zwischen den Tassen kostet dagegen 0,87 K. Gute Frage zum Versuchsplan: „Was müssen Sie genauer kontrollieren?“
7. **Nicht vorgewärmter Becher:** 14 K Sprung sofort, mehr als der ganze Effekt (Frage vor dem Versuch).
8. **Deckel nur auf einer Tasse:** ±7 bis 14 K: zeigt, warum ein fairer Vergleich gleiche Bedingungen braucht (nur als Frage, nicht als Standardregler).

## Nicht empfehlen

- **Verdunstung als Kurve oder Zahl im Werkzeug:** ein fremd kalibrierter Parameter, Übertragungsregel unsicher (verdunstete Masse 5 bis 11 g), nicht gegen eine eigene Messung getestet; geht über Tutorium 5 hinaus. Stattdessen Text mit Bereich und der Deckel als Szenario.
- **Exponent 4/3:** setzt turbulente freie Konvektion voraus (Ra > 10^9); an einer Tasse ist Ra ≈ 2,5·10^6.
- **Materialauswahl, die kA stillschweigend ändert:** Die Faktoren (Edelstahl 0,85 bis 1, Vakuum 0,44) sind Schätzungen aus Deckelversuchen an anderen Bechern; kA muss aus der Messung kommen.
- **Deckel nur auf einer Tasse als Regler:** verändert die Frage und überdeckt den Milch-Effekt (siehe oben, höchstens als Diskussionsfrage).
- **Strahlung mit Sichtfaktoren, Stefan-Korrektur, Massenverlust im linearen Modell:** zu fein für Tutorium 5; der Massenverlust (etwa 3 % von m_K) ist kleiner als die übrigen Unsicherheiten.
- **Zwei-Punkte-kA als einzige Auswertung einer Messreihe:** verschenkt Genauigkeit (1,9 % gegen 0,5 %) und verbirgt die Krümmung.

## Quellen

| Kurzname | Angabe | Prüfstatus | Wörtliches Kurzzitat |
|---|---|---|---|
| Ferreira 2025a | Ferreira, J. P. M. (2025): Forced convection and the coffee cup. Phys. Educ. 60, 035001, doi:10.1088/1361-6552/adb6ea | Volltext (akzeptiertes Autorenmanuskript, CC BY-NC-ND 4.0, https://ciencia.ucp.pt/ws/files/116791893/116791417.pdf; Verlagsfassung hinter Bezahlschranke, Seiten und Nummern können abweichen) | „y = -0.0135x + 4.2152“ (Abb. 6, mit Deckel); weitere Zitate in den Abschnitten 1, 3, 4, 9 |
| Ferreira 2025b | Ferreira, J. P. M. (2025): Radiation in the coffee cup. Phys. Educ. 60, 015011, doi:10.1088/1361-6552/ad8f84 | Volltext (akzeptiertes Autorenmanuskript, https://ciencia.ucp.pt/ws/files/114383224/114297860.pdf) | „the aluminum cup took considerably longer to reach 40 °C: 127 min vs 90 min.“ |
| Condoret 2007 | Condoret, J. S. (2007): Teaching transport phenomena around a cup of coffee. Chem. Eng. Educ. 41(2), 137 bis 143 | Sekundärquelle (Zahl 12,0 von 22,7 W aus `Kaffee_Loesung.md`; Literaturangabe bestätigt in Suleman & Gas 2024, Ref. 21; Zeitschriftenseite für das Abrufwerkzeug gesperrt, HTTP 403; im Browser vielleicht frei) | kein Zitat |
| Suleman & Gas 2024 | Suleman, M.; Gas, P. (2024): Analytical, experimental and computational analysis of heat released from a hot mug of tea ... Int. J. Heat Technol. 42(2), 359 bis 372, doi:10.18280/ijht.420201 | Volltext (CC BY 4.0) | „Mug (porcelain) 2400 1050 1.500 0.595“ (Tab. 1) |
| openLCA 2018 | Martin, S.; Bunsen, J.; Ciroth, A. (2018): Case study ceramic cup vs. paper cup. openLCA 1.7.2, Version 1.1 | Volltext | „The cup weighs 8.3 g and has an inner plastic (polyethylene) coating of 0.1 g.“ |
| ETB | Engineering ToolBox: Specific heat of solids; Emissivity coefficients of common materials (engineeringtoolbox.com) | Volltext über das Abrufwerkzeug (Zeilen vom Werkzeug wiedergegeben) | „Porcelain 0.26 1.07“ |
| NIST | NIST Chemistry WebBook, Thermophysical properties of fluid systems, Wasser, Sättigung 20 bis 100 °C | Volltext über das Abrufwerkzeug; durch eigene IF97-Rechnung auf 0,007 % bestätigt | „80 | 47.414 | 335.01 | 2643.0“ |
| Vollmer 2009 | Vollmer, M. (2009): Newton's law of cooling revisited. Eur. J. Phys. 30, 1063 bis 1084, doi:10.1088/0143-0807/30/5/014 | Abstract (INIS-Eintrag) | „The cooling of objects is often described by a law, attributed to Newton, which states that the temperature difference“ |
| IAPWS-IF97 | Gleichung für den Sättigungsdampfdruck, Region 4 | nicht geprüft (aus dem Gedächtnis umgesetzt, gegen NIST bestätigt) | kein Zitat |
| Lehrbuchkorrelationen | Nu = 0,54 Ra^(1/4) (waagerechte Platte), Nu = 0,10 Ra^(1/3) (turbulent), Lewis-Analogie, Le ≈ 0,85 | nicht geprüft | kein Zitat |
| Edelstahl 1.4301, Händlermassen | c = 500 J/(kg K); Massen 300-ml-Edelstahlbecher 110 bis 245 g | nicht geprüft (nur Suchergebnisse) | kein Zitat |

Abgeleitete Größen (nicht an einer Quelle abgelesen, sondern von mir aus Quellenwerten berechnet): Wassermasse in Ferreiras Becher 244 g, Innendurchmesser 7,16 cm (Außendurchmesser 8,2 cm aus 2025a, Wand 5,2 mm aus 2025b; vermutlich derselbe Becher, weil die Deckelgerade in beiden Arbeiten gleich ist), h_i ≈ 190 W/(m² K).
