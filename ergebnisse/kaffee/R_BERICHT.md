# Bericht Prüfer R (Recherche): Kaffee mit Milch

Stand 29.10.2026. Eigene Rechnungen: `notizen/r_check.py`, `notizen/r_check2.py`, `notizen/r_check3.py` (mit der Kopie `notizen/kaffee_modell.py`). Geöffnete PDF-Quellen als Text unter `notizen/q_*/`. Websuchen: 17 von höchstens 20; dazu Abrufe der Links aus der Quellenliste und einzelner Treffer.

Kennzeichnung der Belege: **[geöffnet]** = Seite oder PDF selbst gelesen; **[Treffer]** = nur aus dem Text eines Suchtreffers; **[Gedächtnis]** = nicht geprüft.

## 1. Gesamturteil

Die Arbeitswerte sind fast alle belegt und gut gewählt: 30 ml Milch (FSANZ: im Mittel 31 g), 5 °C (BfR), 41 min Zeitkonstante (Ferreira 2025, Abb. 6, nachgerechnet 41,5 min) und 55 bis 65 °C Milchschaum (Thermoplan) stimmen mit den Quellen überein. Die Hauptaussage (Milch sofort, Tasse 1 bleibt wärmer) ist robust und stimmt mit der einzigen begutachteten Messarbeit überein, die ich gefunden habe (Rees & Viney 1988, Am. J. Phys.), ebenso mit mehreren Schulversuchen. Das größte Problem ist Teil g: Beim Cappuccino kippt das Modellergebnis schon, wenn die Schaumschicht das $kA$ von Tasse 1 um 5,6 % senkt, und eine Schaumschicht wirkt wie ein teilweiser Deckel. Dazu kommen kleinere Punkte: Die Hinweise zum Versuch sind etwas zu genau (die „mindestens 1,6 K“ gelten nur für τ = 41 min), ein Quellenlink (IARC) ist tot, und die Condoret-Werte ließen sich nicht einsehen. Mit diesen kleinen Korrekturen ist die Aufgabe einsatzbereit.

## 2. Änderungsvorschläge

**Rech1: Teil g (Cappuccino) hängt an einer Annahme, die beim Schaum nicht trägt**
- Ebene: inhaltlich (Sinn), technisch
- Stelle: Aufgabe Teil g und Gegebene Größen „Milchschaum“; Lösung, Hinweise
- Befund: Im Modell ist Tasse 2 um 1,19 K wärmer (35,99 gegen 37,18 °C, nachgerechnet). Der Vorsprung ist klein: Ist $kA$ in Tasse 1 nur um 5,6 % kleiner, sind beide Tassen gleich warm; bei 10 % kleinerem $kA$ ist Tasse 1 um 0,99 K wärmer, bei 20 % um 3,47 K. Ein Cappuccino hat den Schaum von Anfang an als Schicht oben. Ferreira (2025) zeigt, dass ein Deckel auf dem offenen Becher die Zeitkonstante von 41,5 auf 74 min verlängert, also das scheinbare $kA$ um 44 % senkt (Abb. 6, Steigungen 0,0241 und 0,0135 1/min) **[geöffnet]**. Eine Schaumschicht ist kein Styropordeckel; wie stark sie Verdunstung und Wärmeabgabe oben bremst, habe ich in keiner Quelle gefunden (eigene Schlussfolgerung). Dass sie mehr als 5,6 % ausmacht, ist aber wahrscheinlich. Wer den Teil wörtlich nimmt („Ihr Mitbewohner trinkt Cappuccino“), zieht daraus vermutlich den falschen Alltagsschluss. Teil d ist dagegen robust: Dort müsste $kA$ in Tasse 1 um 25 % *größer* sein, damit das Ergebnis kippt.
- Vorschlag (Empfehlung Variante B):
  - Variante A: heiße Milch statt Schaum. In g: „Am nächsten Tag trinkt Ihr Mitbewohner Milchkaffee: Statt kalter Milch kommt heiße Milch mit $\vartheta_S$ aus dem Milchaufschäumer in beide Tassen und wird untergerührt (gleiche Masse, Becher wieder vernachlässigt).“ In der Tabelle „Milchschaum“ durch „Heiße Milch“ ersetzen. Die Zahlen bleiben gleich.
  - Variante B: Cappuccino bleibt, aber die Annahme wird sichtbar gemacht. An g anhängen: „Nehmen Sie dafür an, dass der Schaum untergerührt wird und $kA$ unverändert bleibt. Welche Annahme ist beim echten Cappuccino fraglich, und in welche Richtung verschiebt sie das Ergebnis?“ In die Hinweise: „Schon 6 % kleineres $kA$ in Tasse 1 (Schaumschicht als Deckel) kehrt das Ergebnis um; ein Deckel senkt $kA$ beim offenen Becher um gut 40 % (Ferreira 2025, Abb. 6).“
- Begründung: Rechnung `notizen/r_check2.py`; Ferreira, J. P. M. (2025), Forced convection and the coffee cup, Phys. Educ. 60, 035001, <https://doi.org/10.1088/1361-6552/adb6ea>, Manuskript: <https://ciencia.ucp.pt/ws/files/116791893/116791417.pdf>. Variante B nutzt die gewollte Begründung von Annahmen und hält die Überraschung des Teils.
- Priorität: sollte · Aufwand: klein
- Folgen: Variante A ohne neue Zahlen; Variante B mit einer zusätzlichen Antwortzeile in der Lösung. Das Modellergebnis selbst ist robust: Der ganze Bereich 55 bis 65 °C liegt über dem Kipppunkt (Unterschied −0,73 bis −1,65 K), mit Becher −0,96 K, mit $n = 4/3$ −1,00 K.

**Rech2: Hinweise zum Versuch: Zahlen als Bereich angeben und die Abweichung von der Vorhersage ankündigen**
- Ebene: praktisch (Durchführung)
- Stelle: Lösung, Hinweise für die Tutoriumsleitung, „Versuch“
- Befund: Die Angaben („rund 3 K“, „nach 30 Minuten gut 2,5 K“, „Becher 3 mindestens 1,6 K kühler“) gelten nur für τ = 41 min. Nachgerechnet mit Becher 300 g ergeben sich 1,57 K für Becher 3 (also nicht „mindestens 1,6“). Haushaltsbecher kühlen oft schneller (siehe Rech7). Für τ = 20 bis 75 min ergeben sich:

  | τ ohne Becher | ϑ(10 min) | Becher 1 − 2 nach 60 min | nach 30 min | Becher 1 − 3 (Milch 20 °C) |
  |---|---|---|---|---|
  | 20 min | 56,4 °C | 2,35 K | 3,07 K | 0,84 K |
  | 30 min | 63,0 °C | 2,88 K | 2,99 K | 1,38 K |
  | 41 min | 67,0 °C | 3,08 K | 2,71 K | 1,57 K |
  | 75 min | 72,5 °C | 2,80 K | 1,94 K | 1,29 K |

  Außerdem wird die gemessene Temperatur nach 60 min über der Vorhersage aus Schritt 4 liegen. Das $kA$ aus den ersten 10 min ist wegen der starken Verdunstung bei hoher Temperatur zu groß. Ferreira zeigt das direkt: Die Ausgleichsgerade des offenen Bechers beginnt bei 62,9 K Übertemperatur statt bei 70 K, die frühen Punkte fallen also schneller. Mit $n = 4/3$ und Becher ergeben sich 37,66 / 34,21 / 35,71 °C statt 34,04 / 30,96 / 32,47 °C, also rund 3,5 K mehr, bei einem Unterschied von 3,45 K (Becher 1 − 2) und 1,94 K (Becher 1 − 3).
- Vorschlag: Neuer Wortlaut des Hinweises: „Nach 60 Minuten sind zwischen Becher 1 und 2 je nach Becher 2,5 bis 3,5 K Unterschied zu erwarten (nach 30 Minuten 2 bis 3 K), mit einem Küchenthermometer gut messbar. Becher 3 bleibt rund 1 bis 2 K kühler als Becher 1; das liegt nahe an der Messunsicherheit. Die gemessenen Temperaturen liegen voraussichtlich einige Kelvin über der Vorhersage, weil die Verdunstung am Anfang besonders stark ist (siehe ‚Was die Rechnung weglässt‘). Das ist kein Messfehler, sondern die Grenze des Modells mit konstantem $kA$, und lässt sich gut besprechen.“
- Begründung: `notizen/r_check2.py` und `notizen/r_check3.py`; Ferreira 2025, Abb. 6 **[geöffnet]**. Greenwald & Bauldry berichten, dass ein Klassenversuch mit kleiner Temperaturdifferenz in zwei Durchgängen gegensätzliche Ergebnisse lieferte (Fühler, Verdunstung) **[geöffnet]**: <https://cs.appstate.edu/sjg/papers/CoffeeCooling.pdf>.
- Priorität: sollte · Aufwand: klein
- Folgen: nur der Text der Hinweise; keine Änderung an Aufgabe oder Abbildungen.

**Rech3: Quellenliste korrigieren und ergänzen**
- Ebene: technisch (Belege)
- Stelle: Lösung „Quellen der Arbeitswerte“; Sammlung `t5a_kaffee_quellen.md`
- Befund und Vorschlag je Quelle:
  1. **IARC-Link tot:** Der Link leitet auf publications.iarc.who.int weiter und endet dort in 404 (29.10.2026). Ersetzen durch <https://doi.org/10.1016/j.burns.2007.09.012> (PubMed: <https://pubmed.ncbi.nlm.nih.gov/18226454/> **[geöffnet]**: Burns 34(5), 648 bis 654). Laut Kurzfassung werden Heißgetränke oft bei 71,1 bis 85 °C serviert **[Treffer]**.
  2. **Herleitung der 80 °C:** Brown & Diller nennen Temperaturen beim Servieren, also schon in der Tasse. „Ausschank 71 bis 85 °C, beim Eingießen 2 bis 5 K weniger“ verbindet deshalb zwei Stufen, die nicht zusammenpassen. Abraham & Diller (2019) liefern die passende Kette **[geöffnet]**: brühen bei 93 °C, in die Kanne 90 °C (bei kleinen, nicht isolierten Glaskannen „up to 20 °F“, also bis rund 11 K weniger), in die Tasse 2 bis 5 °C weniger; für große, isolierte Systeme 85 bis 88 °C in der Tasse (Tab. 1). Neuer Wortlaut: „Kaffee: gebrüht bei etwa 93 °C, in der Glaskanne einer Haushaltsmaschine bis etwa 11 K kälter, beim Eingießen 2 bis 5 K kälter (Abraham & Diller 2019, J. Food Sci. 84(8), 2011 bis 2014, Tab. 1); 80 °C in der Tasse liegen in diesem Bereich und im Servierbereich 71 bis 85 °C (Brown & Diller 2008).“
  3. **Ferreira:** Titel und DOI ergänzen (siehe Rech1); vermerken, dass der Link auf das angenommene Manuskript führt. Gemessen wurde Wasser, Start 90 °C, Becher fast voll (rund 245 g, aus $h$, $A$ und τ zurückgerechnet; die Masse steht nicht im Text). Die Steigung 0,0241 1/min gehört zum offenen Becher ohne Rühren und ohne Lüfter; der Autor nennt sie eine „scheinbare“ Größe, weil die Punkte von der Geraden abweichen. Bestätigt.
  4. **Condoret:** Titel ergänzen: „Teaching transport phenomena around a cup of coffee“, Chem. Eng. Educ. 41(2), 2007 **[Treffer]**. Die Werte 12,0 von 22,7 W (Tab. 2) konnte ich nicht prüfen (journals.flvc.org antwortet mit 403). Als zweiten, prüfbaren Beleg für „rund die Hälfte“ Ferreira 2025 nennen: Ein Deckel senkt das scheinbare $kA$ um 44 %; im offenen Becher verdunsteten 11 g Wasser.
  5. **FSANZ:** ergänzen: „45 Wägungen, Spanne 5 bis 79 g, Tee oder Kaffee ohne Unterschied“ **[Treffer]**. Beim Abruf zeigte die verlinkte Seite diese Zahlen nicht mehr (nur einen Überblick über AUSNUT 2023); den Link einmal prüfen.
  6. **Goff, SCA (moccamaster):** Beide Seiten antworten mit 403. Die Dichte von 1027 bis 1033 kg/m³ bei 20 °C ist durch einen Treffer bestätigt **[Treffer]**, die SCA-Angabe nicht geprüft **[Gedächtnis: plausibel]**.
- Begründung: siehe Wertetabelle 2a.
- Priorität: sollte (toter Link, unstimmige Herleitung) · Aufwand: klein
- Folgen: nur Quellenteil der Lösung und der Sammlung.

**Rech4: Plausibilitätsprüfung zur verdunsteten Masse**
- Ebene: didaktisch
- Stelle: Aufgabe Teil e (oder nur Lösung „Zum Weiterdenken“)
- Befund: Die Annahme „verdunstete Masse vernachlässigt“ steht unbegründet da, obwohl die Hinweise sagen, dass die Verdunstung rund die Hälfte der Wärme abführt. Ist das so, verdunsten in Tasse 2 in 60 min rund $0{,}5 \cdot 38{,}57\,\mathrm{kJ} / 2380\,\mathrm{kJ/kg} = 8{,}1\,\mathrm{g}$, also 4 % des Kaffees (Tasse 1: 7,3 g). Die Mischtemperatur in Tasse 2 sinkt dadurch nur um 0,13 K (30,06 statt 30,19 °C). Ferreira hat 11 g aus rund 245 g Wasser in rund 55 min (90 auf 40 °C) gemessen, das passt.
- Vorschlag: In die Hinweise (Zum Weiterdenken) oder als Satz an e: „Schätzen Sie ab, wie viel Kaffee in Tasse 2 verdunstet, wenn etwa die Hälfte von $Q_2$ durch Verdunstung abgeht ($\Delta h_v \approx 2380\,\mathrm{kJ/kg}$). Ist die Annahme vertretbar?“ Antwort: rund 8 g, 4 %, vertretbar.
- Begründung: `notizen/r_check2.py`; Ferreira 2025, Abschnitt 3.4.
- Priorität: kann · Aufwand: klein
- Folgen: in der Aufgabe eine Zeile mehr ($\Delta h_v$ in die Tabelle); in der Lösung drei Zeilen.

**Rech5: Versuch: mehrere Messpunkte, Wägung und ein Probelauf als Datenreserve**
- Ebene: praktisch, didaktisch
- Stelle: Aufgabe „Versuch zu Aufgabe 1“, Schritt 3 und 5; Hinweise
- Befund: $kA$ aus einem einzigen Messpunkt ist empfindlich; ein Ablesefehler von 1 K bei 10 min verschiebt die Vorhersage um 1,4 bis 1,8 K (Nachrechnung: Messung 64 °C gibt 29,94 °C, 67 °C gibt 34,05 °C, 70 °C gibt 39,42 °C). Ferreira und Greenwald & Bauldry bestimmen die Abkühlkonstante aus vielen Punkten über die Auftragung $\ln(T - T_u)$ gegen $t$. Diese Auftragung zeigt auch die Krümmung durch die Verdunstung. Eine offen zugängliche Messreihe zu „Milch sofort oder später“ habe ich nicht gefunden (Rees & Viney nur als Kurzfassung, Vernier nur als Logger-Pro-Datei).
- Vorschlag:
  - In Schritt 3 ergänzen: „Messen Sie Becher 2 zusätzlich nach 5, 20 und 30 min.“ In die Hinweise: „Wer Zeit hat, trägt $\ln(\vartheta - \vartheta_u)$ gegen $t$ auf: Die Punkte liegen nicht ganz auf einer Geraden, die Verdunstung wirkt am Anfang stärker (vgl. Ferreira 2025, Abb. 6).“
  - Optional: Becher 2 bei $t = 0$ und $t = 60\,\mathrm{min}$ auf eine Küchenwaage stellen; zu erwarten sind 5 bis 8 g Verlust (passt zu Rech4).
  - Die TL macht den Versuch einmal vorab und hält die Messreihe als Reserve bereit, falls im Tutorium etwas schiefgeht.
- Begründung: Ferreira 2025 **[geöffnet]**; Greenwald & Bauldry **[geöffnet]**; Vernier „Cooling Coffee“ (2011) <https://www.vernier.com/vernier-ideas/cooling-coffee/> **[geöffnet]**.
- Priorität: kann · Aufwand: klein (Waage und Probelauf: mittel)
- Folgen: Versuchstext um einen Satz länger; kein Einfluss auf die Rechnung.

**Rech6: Fachliteratur zur Hauptaussage in die Hinweise aufnehmen**
- Ebene: inhaltlich (Relevanz)
- Stelle: Lösung, Hinweise (Fehlvorstellungen) oder Quellen
- Befund: Die Hauptaussage hat einen begutachteten Beleg. Rees & Viney (1988) haben die Abkühlung mit Haushaltsgeräten gemessen: Schwarzer Kaffee kühlt schneller ab als Kaffee mit Milch; wer den Kaffee einige Minuten später möglichst heiß will, gibt Milch oder Sahne sofort hinein, „unter den meisten, aber nicht allen Umständen“ **[geöffnet, nur Kurzfassung]**. Dasselbe zeigen einfache Versuche: Naked Scientists (2007, Tee, 15 min; die Erklärung „hat weniger Energie verloren“ entspricht Teil e) und Vernier (2011). Die Wolfram-Demonstration (Kaffee 85 °C, Sahne und Luft 20 °C) kommt zum selben Schluss. Es gibt auch eine falsche Gegenstimme: Kurzweg (Univ. of Florida, 2017, nicht begutachtet) behauptet, der Zeitpunkt sei egal. Er übersieht, dass sich die Wärmekapazität des Inhalts ändert; im Modell bleibt selbst mit Milch bei Raumtemperatur ein Unterschied von 2,48 K. Die Aussage von wissenschaft.de (2021), schwarzer Kaffee kühle „um etwa 20 Prozent schneller“, nennt keine Messung; sie passt aber zufällig zu den Anfangswärmeströmen 20,41 gegen 17,17 W (+19 %).
- Vorschlag: In die Hinweise: „Fachlicher Beleg: Rees & Viney (1988), On cooling tea and coffee, Am. J. Phys. 56, 434 bis 437, <https://doi.org/10.1119/1.15572>. Achtung: Im Netz kursieren auch Fehlschlüsse (‚der Zeitpunkt ist egal‘), sogar von Hochschullehrern; Teil e widerlegt sie.“ Kurzweg nicht als Quelle verwenden.
- Begründung: Rees & Viney: <https://pubs.aip.org/aapt/ajp/article-abstract/56/5/434/1044307/On-cooling-tea-and-coffee>; Naked Scientists: <https://www.thenakedscientists.com/get-naked/experiments/when-add-milk>; Wolfram: <https://www.wolframcloud.com/obj/5f97f1ac-d488-435a-a4f7-a0a74af00c7e>; Kurzweg: <https://web.mae.ufl.edu/uhk/COOLING-COFFEE.pdf>; wissenschaft.de: <https://wissenschaft.de/artikel/newton-und-der-heisse-kaffee> (alle **[geöffnet]**).
- Priorität: kann · Aufwand: klein
- Folgen: nur Hinweise oder Quellen; der Volltext von Rees & Viney liegt hinter einer Bezahlschranke (offene Frage 4).

**Rech7: Zeitkonstante 41 min liegt am langsamen Ende**
- Ebene: inhaltlich
- Stelle: Lösung, Quellen; Hinweise zum Versuch
- Befund: Bestätigt für Ferreiras offenen Keramikbecher (41,5 min). Andere Angaben sind schneller: Kurzweg misst für Wasser in einer Tasse $k = 0{,}0453$ 1/min, also τ = 22 min **[geöffnet]**. Abraham & Diller nennen „typisch 10 bis 15 °C in 5 min“ **[geöffnet]**, das entspricht τ ≈ 20 bis 31 min; dabei sind kalte Becher und Pappbecher eingeschlossen. Auf die Aussage wirkt das kaum (Unterschied 3,70 K bei 64 °C, 3,85 K bei 67 °C, 3,79 K bei 70 °C), wohl aber auf die absoluten Temperaturen und den Versuch (Rech2).
- Vorschlag: In die Quellen: „Haushaltsbecher kühlen je nach Form und Füllung auch schneller ab (τ ≈ 20 bis 40 min); die Aussage hängt davon kaum ab.“
- Begründung: Nachrechnung (Empfindlichkeit), `notizen/r_check2.py`.
- Priorität: kann · Aufwand: klein
- Folgen: keine.

**Rech8: Schätzwerte belegen oder messen (c_p der Milch, Becher)**
- Ebene: technisch
- Stelle: Gegebene Größen; Quellen
- Befund: Für $c_{p,M} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ steht nur „wie in Tutorium 8“, ohne Quelle. Die Engineering ToolBox nennt 3,77 für pasteurisierte Vollmilch und 3,98 bis 4,02 für Magermilch **[geöffnet]**; Minim et al. nennen 3,4 bis 4,1 J/(g K), abhängig von Wasser- und Fettgehalt sowie Temperatur **[Treffer]**. Mit 3,77 wird der Unterschied 3,72 statt 3,85 K, der Einfluss ist also klein. Der Becher (300 g, 0,85 kJ/(kg K)) ist als Schätzung gekennzeichnet; Treffer nennen für Keramik rund 0,9 kJ/(kg K) und für Becher in Lehrbuchaufgaben 0,25 bis 0,35 kg **[Treffer]**. Im Bereich 0,25 bis 0,40 kg und 0,80 bis 1,08 kJ/(kg K) liegt der Unterschied mit Becher zwischen 2,86 und 3,19 K.
- Vorschlag: Für $c_{p,M}$ die Quelle aus Tutorium 8 zitieren. Die Tutoriumsbecher einmal wiegen und in den Hinweisen notieren: „Becher im Tutorium wiegen ___ g“.
- Begründung: `notizen/r_check.py`; <https://www.engineeringtoolbox.com/specific-heat-capacity-food-d_295.html>.
- Priorität: kann · Aufwand: klein
- Folgen: keine neuen Zahlen, solange die Arbeitswerte bleiben.

**Rech9: Kipppunkt (Teil h) als modellabhängig kennzeichnen**
- Ebene: inhaltlich
- Stelle: Lösung h (1), Hinweise
- Befund: 47,0 °C bestätigt für $kA$ = konst. Mit überlinearer Wärmeabgabe ($n = 4/3$, angepasst an dieselbe Messung) liegt der Kipppunkt bei 49,7 °C. Milchschaum mit 55 bis 65 °C liegt in beiden Fällen darüber, die Aussage von g bleibt also im Modell bestehen. Die Milchmenge ändert den Kipppunkt kaum (46,5 °C bei 5 g, 47,7 °C bei 79 g).
- Vorschlag: In die Lösung zu h (1) ergänzen: „Der Wert hängt vom Modell ab; mit überlinearer Wärmeabgabe liegt er bei rund 50 °C, kaum abhängig von der Milchmenge.“
- Begründung: `notizen/r_check2.py`.
- Priorität: kann · Aufwand: klein
- Folgen: ein Satz in der Lösung.

**Rech10: Ideen aus Vergleichsaufgaben (nur für Hinweise)**
- Ebene: didaktisch
- Stelle: Lösung „Zum Weiterdenken“
- Befund: Die verbreitete Lehrbuchaufgabe (Nagle & Saff, Differentialgleichungen, zitiert bei Greenwald & Bauldry **[geöffnet]**) lässt einen Teelöffel Sahne erst nach 5 min dazugeben; der Unterschied ist dann klein, die Aufgabe bleibt qualitativ. Die Kaffee-Aufgabe ist mit 60 min, Messwert und Energiebilanz deutlich reicher. Die Wolfram-Demonstration stellt zwei Ziele gegenüber: möglichst bald trinkbar (Milch spät) oder möglichst lange heiß (Milch sofort). Ferreira variiert Deckel, Rühren und Lüfter. Gould & Tobochnik haben ein Kapitel „The Coffee Cooling Problem“ **[Treffer]**; dass es dort Messwerte für Kaffee mit und ohne Sahne gibt, weiß ich nur aus dem Gedächtnis **[Gedächtnis]**.
- Vorschlag: Einen Satz unter „Zum Weiterdenken“: „Umgekehrtes Ziel: Wer den Kaffee möglichst bald bei Trinktemperatur haben will, gießt die kalte Milch spät dazu, aus demselben Grund.“ Keine weiteren Teile in die Aufgabe aufnehmen; sie ist für 90 Minuten schon voll.
- Begründung: Quellen siehe Rech6.
- Priorität: kann · Aufwand: klein
- Folgen: keine.

## 2a. Wertetabelle

Alle Rechnungen zur Wirkung in `notizen/r_check*.py`. „Wirkung“ meint den Unterschied ϑ₁ − ϑ₂ (Grundfall 3,85 K).

| Größe | Wert in der Aufgabe | Quelle mit Link | Befund | Gefundener Wert, Wirkung |
|---|---|---|---|---|
| Kaffee beim Servieren | 71 bis 85 °C (Quellenliste) | Brown & Diller 2008, Burns 34(5), 648 bis 654, <https://pubmed.ncbi.nlm.nih.gov/18226454/> [geöffnet]; IARC-Link tot (404) | bestätigt, Link ersetzen | 71,1 bis 85 °C [Treffer, Kurzfassung] |
| Temperaturverlust beim Eingießen | 2 bis 5 K | Abraham & Diller 2019, J. Food Sci. 84(8), 2011 bis 2014, <https://foodsci.oregonstate.edu/sites/agscid7/files/foodsci/attachments/hot-bev-temp.pdf> [geöffnet] | bestätigt | 2 bis 5 °C; Kanne bis 11 K, Tasse 85 bis 88 °C bei isolierten Systemen |
| Kaffee in der Tasse | 80 °C | wie oben | plausibel, Herleitung umformulieren (Rech3) | bei 85 °C: 3,83 K |
| Stoffwerte Kaffee | wie Wasser | SCA über <https://support.moccamaster.com/hc/en-us/articles/1500009409121> (403) | nicht geprüft | Gelöstes 1,15 bis 1,35 % [Gedächtnis], Wirkung vernachlässigbar |
| Milchmenge | 30 ml (30,9 g) | FSANZ 2011, <https://www.foodstandards.gov.au/science-data/monitoringnutrients/ausnut/foodmeasures/2011-Dash-and-splash-measures-program> | bestätigt [Treffer]; Seite zeigt die Zahlen derzeit nicht | Mittel 31 g, Spanne 5 bis 79 g, n = 45; 5 g: 0,73 K, 79 g: 7,60 K |
| Kühlschrank | 5 °C | BfR 13.02.2023, <https://www.bfr.bund.de/fragen-und-antworten/thema/korrektes-kuehlen-von-lebensmitteln-im-privathaushalt/> [geöffnet] | bestätigt | höchstens 7 °C, besser unter 5 °C; im Mittel gemessen 5,5 °C (Umfrage 2020) und 6,1 °C (Übersicht 2017); 7 °C: 3,67 K |
| Dichte Milch | 1030 kg/m³ | Goff, <https://books.lib.uoguelph.ca/dairyscienceandtechnologyebook/chapter/physical-properties-of-milk/> (403) | bestätigt [Treffer] | 1027 bis 1033 kg/m³ bei 20 °C |
| c_p Milch | 3,94 kJ/(kg K) | „wie Tutorium 8“, keine Quelle | plausibel, Quelle fehlt (Rech8) | Vollmilch 3,77, Magermilch 3,98 bis 4,02 [geöffnet, Engineering ToolBox]; 3,77: 3,72 K |
| Zeitkonstante offener Keramikbecher | 41 min (Messung 67 °C nach 10 min) | Ferreira 2025, Phys. Educ. 60, 035001, <https://doi.org/10.1088/1361-6552/adb6ea>, Manuskript <https://ciencia.ucp.pt/ws/files/116791893/116791417.pdf> [geöffnet] | bestätigt; obere Grenze (Rech7) | 1/0,0241 = 41,5 min (Wasser, rund 245 g, ab 90 °C, „scheinbar“); andere Angaben 20 bis 31 min; 64 °C: 3,70 K |
| Anteil Verdunstung | rund die Hälfte (12,0 von 22,7 W bei 79 °C) | Condoret 2007, Chem. Eng. Educ. 41(2), <https://journals.flvc.org/cee/article/view/122462> (403) | Tabellenwert nicht geprüft; Größenordnung bestätigt | Ferreira: Deckel senkt scheinbares $kA$ um 44 %, 11 g verdunstet; „besonders über 50 °C“ |
| Milchschaum | 60 °C | Thermoplan, <https://www.thermoplan.ch/en/coffeecompetence/blog/coffee-knowledge-milk> [geöffnet] | bestätigt | 55 bis 65 °C; Ergebnis g −0,73 bis −1,65 K; Schaumschicht siehe Rech1 |
| Becher Masse | 300 g | Schätzung | plausibel [Treffer] | Lehrbuchaufgaben 0,25 bis 0,35 kg; Unterschied mit Becher 2,86 bis 3,19 K |
| Becher c | 0,85 kJ/(kg K) | Schätzung | plausibel [Treffer] | Keramik rund 0,9 kJ/(kg K) |
| Raumtemperatur | 20 °C | ohne Quelle | üblich | Ferreira: 19 bis 21 °C |

Nachgerechnet und bestätigt: alle Ergebnisse von a bis h (70,47 °C; 0,3402 W/K; 34,05 und 30,19 °C; 34,88 und 38,57 kJ; 0,4440 W/K, 34,04 und 30,96 °C; 35,99 und 37,18 °C; 47,0 °C), die Zahlen der Hinweise zu Fehlern (39,1 und 36,1 °C), zum nichtlinearen Modell (37,65 und 33,34 °C), zur Raumtemperatur-Milch (2,48 K), zum Schnittpunkt (55,7 min) und zum Versuch nach 30 min (2,71 K). Abweichend nur „mindestens 1,6 K“ (nachgerechnet 1,57 K, siehe Rech2).

## 3. Was bleiben sollte

- $kA$ aus einer Messung bestimmen (Teil c, f): Dadurch hängt die Aussage kaum von unsicheren Werten ab. Eine Messung zwischen 64 und 70 °C ändert den Unterschied nur zwischen 3,70 und 3,85 K.
- Die Arbeitswerte liegen nahe an echten Quellen (31 g Milch, 5 °C, 41 min, 55 bis 65 °C) und sind mit Links belegt; das ist besser als bei den meisten Vergleichsaufgaben.
- Teil e (abgegebene Wärme) als Antwort auf „Energie bleibt erhalten“: Genau diese Begründung nutzen auch die Naked Scientists, und sie widerlegt die Fehlschlüsse, die im Netz kursieren.
- Der ehrliche Abschnitt „Was die Rechnung weglässt“ mit Verdunstung und nichtlinearem Modell; er wird durch Ferreira gestützt.
- Der Versuch über 60 min mit drei Bechern: Die lange Wartezeit macht den Unterschied messbar; Versuche mit 5 min Wartezeit lieferten widersprüchliche Ergebnisse (Greenwald & Bauldry).
- Becher 3 (Milch neben der Tasse) als Prüfstein für h (2).

## 4. Offene Fragen an die Tutoriumsleitung

1. Teil g: Variante A (Milchkaffee mit untergerührter heißer Milch) oder Variante B (Cappuccino bleibt, Annahme wird hinterfragt)? Ich empfehle B.
2. Welche Becher stehen im Tutorium zur Verfügung, und gibt es eine Küchenwaage (Becher wiegen, verdunstete Masse messen)?
3. Aus welcher Quelle stammt $c_{p,M} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ in Tutorium 8? Diese Quelle sollte auch hier stehen.
4. Kann jemand mit Bibliothekszugang Condoret (2007, Tab. 2) und Rees & Viney (1988) im Volltext einsehen? Ich konnte nur die Kurzfassungen bzw. gar nichts öffnen (403).
5. Soll ich die Messreihe eines Probelaufs (Rech5) als Abbildung in die Lösung aufnehmen, falls die TL ihn durchführt?

Hinweis zur Umgebung: Diese Hosts ließen sich nicht abrufen: journals.flvc.org, books.lib.uoguelph.ca, support.moccamaster.com und meetings-archive.aps.org (alle 403), www.engr.mun.ca (503), wiki.cs.umt.edu und mvhs.shodor.org (Name nicht auflösbar, in dieser Sitzung vermutlich nicht freigegeben). Der Bielefelder Didaktik-Link leitet auf die Fakultätsseite um.
