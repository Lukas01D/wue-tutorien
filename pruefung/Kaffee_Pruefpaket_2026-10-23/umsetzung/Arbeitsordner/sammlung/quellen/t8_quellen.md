# Quellen zu Tutorium 8: Wärmeübertrager und Verdampfer

Stand 21.10.2026. Übernommen aus den Quellenverzeichnissen der Ausgangsdokumente: Ideensammlung „Leitaufgaben aus Klima und Erde“ (Abschnitt 4.8 und 12) und „Aufgabenideen: Meeresströmungen, Sverdrup und Luftströmungen“ (Aufgabe C, Abschnitt Quellen). In Klammern steht, wie die Angabe dort geprüft wurde. Alle Zahlen der Ergebniszeilen rechnet `rechnung/t8_rechnung.py` nach (Ausgabe `rechnung/t8_rechnung_ausgabe.txt`).

## Für alle Aufgaben

- Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* (Vorlesungsfolien). Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn, SoSe 2026. Genutzt: V06 F. 23 bis 28 (Bilanz beider Ströme, mittlere logarithmische Temperaturdifferenz), F. 35 bis 41 (ε-NTU-Konzept, Grenzfälle *C*\* = 1 und *C*\* = 0), V07 F. 3 (Temperaturverläufe bei Kondensation und Verdampfung).
- Lehrstuhl für Fluidverfahrenstechnik (2026). *Formelsammlung Wärmeübertragung* (Stand SoSe 2026): *Re* und Gültigkeitsbereiche der Rohrströmung (laminar, Übergangsbereich, turbulent). Die Beziehungen für Δ*T*~ln~ und das ε-NTU-Konzept stehen nicht in der Formelsammlung, sondern nur in V06. Die Carnot-Leistungszahl der Wärmepumpe (Teil g) steht weder in der Formelsammlung noch in den Foliensätzen 01 bis 08 (Vorwissen aus der Thermodynamik; Textfassungen am 21.10.2026 durchsucht); im Aufgabentext steht sie deshalb unter der Tabelle als gegeben.

## Aufgabe 1: Wärme aus dem Boden (Sole-Wasser-Wärmepumpe)

- Bodentemperatur rund 11 °C in 100 m Tiefe (Arbeitswert): Hessisches Landesamt für Naturschutz, Umwelt und Geologie (2017). *Leitfaden Erdwärmenutzung in Hessen*: ab etwa 10 m Tiefe 8 bis 10 °C, darunter rund 3 K je 100 m wärmer. <https://www.hlnug.de/fileadmin/dokumente/geologie/erdwaerme/Erdwaermeleitfaden_01_2017.pdf> (Volltext). Eine regionale Quelle für Paderborn ist noch offen (Ideensammlung 4.8, „Offen“).
- Jahresarbeitszahl 4,3 erdgekoppelter Wärmepumpen in Bestandsgebäuden: Fraunhofer ISE (2025). *Wärmepumpen heizen auch im Altbau klimafreundlich* (Presseinformation 30/2025). <https://www.ise.fraunhofer.de/content/dam/ise/de/documents/presseinformationen/2025/3025_ISE_PI_Waermepumpen-heizen-auch-im-Altbau-klimafreundlich.pdf> (Pressemitteilung)
- Entzugsleistung 60 W/m für normales Festgestein bei 1800 Betriebsstunden im Jahr: VDI 4640 Blatt 2 (2001). *Thermische Nutzung des Untergrunds: Erdgekoppelte Wärmepumpenanlagen*, zitiert nach 42watt. <https://42watt.de/magazin/entzugsleistung-warmepumpe> (Sekundärquelle; die Ausgabe 2019 arbeitet mit Tabellen nach *λ* und Volllaststunden, Original noch nicht eingesehen)
- Wärmestromdichte aus dem Erdinneren 65 mW/m² (Mittel der Kontinente): Pollack, H. N., Hurter, S. J., & Johnson, J. R. (1993). Heat flow from the Earth’s interior: Analysis of the global data set. *Reviews of Geophysics, 31*(3), 267 bis 280. <https://doi.org/10.1029/93RG01249> (Volltext)
- CO₂ je kWh Strom 344 g (Strommix 2025, ohne Vorketten): Umweltbundesamt (2026, 23. März). *CO₂-Emissionen pro Kilowattstunde Strom 2025*. <https://www.umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2025-nur> (Volltext)
- CO₂ je kWh Erdgas 202 g (Brennstoff, ohne Vorketten): Umweltbundesamt (2024). *Entwicklung der spezifischen Treibhausgas-Emissionen des deutschen Strommix* (Climate Change 23/2024), Tabelle 4. <https://www.umweltbundesamt.de/sites/default/files/medien/11850/publikationen/23_2024_cc_strommix_11_2024.pdf> (Volltext)
- Arbeitswerte ohne eigene Quelle (aus der Ideensammlung 4.8 übernommen): Sondenlänge 100 m, Heizleistung 8 kW, Leistungszahl 4, Sole (Wasser-Glykol) mit *c*~p~ = 3,8 kJ/(kg K), *ρ* = 1040 kg/m³ und *ν* = 4 · 10⁻⁶ m²/s, Sole von −1 auf 2 °C, Verdampfung bei −6 °C, Kondensation bei 40 °C, Rohrinnendurchmesser 26 mm, *k* = 1000 bis 2000 W/(m² K) im Verdampfer, Wirkungsgrad der Gasheizung 0,95.
- Eigene Rechnung: Ideensammlung, Anhang A und Skript `nachrechnung_leitphaenomene.py` (Abschnitt T8); hier nachgebaut in `rechnung/t8_rechnung.py`. Neu gegenüber dem Ausgangsskript: Soletemperatur am tiefsten Punkt der Sonde (nach dem halben Strömungsweg).

## Aufgabe 2: Wer bringt die Wärme zum Pol, Luft oder Wasser?

- Wärmetransport der Atmosphäre rund 5 PW bei 40° N (höchstens 5,1 PW bei 41° N; bei 35° N 78 % des Gesamttransports): Fasullo, J. T., & Trenberth, K. E. (2008). *Journal of Climate, 21*, 2313 bis 2325. <https://journals.ametsoc.org/view/journals/clim/21/10/2007jcli1936.1.xml>
- Die obersten 3 m des Ozeans speichern mehr Wärme als die ganze Atmosphäre (Ausgangssituation ohne Zahl, damit Frage 3 offen bleibt; Teil a): NASA JPL (2001). Ozean-Broschüre. <https://sealevel.jpl.nasa.gov/files/ostm/ocean_brochure.pdf>
- Passat im Mittel 5 bis 6 m/s: Encyclopaedia Britannica, „Trade wind“ (Stand 2024). <https://www.britannica.com/print/article/601703>
- Jetstream im Mittel rund 110 mph (etwa 50 m/s), in Spitzen über 275 mph: NOAA, „The Jet Stream“. <https://www.noaa.gov/jetstream/global/jet-stream>
- Latenter Anteil am Wärmetransport in den mittleren Breiten ein Drittel bis die Hälfte: Stoll, P. J., et al. (2023). *Weather and Climate Dynamics, 4*, 1 bis 17. <https://wcd.copernicus.org/articles/4/1/2023/> ; Armour, K. C., et al. (2019). *Journal of Climate, 32*. <https://earthweb.ess.washington.edu/roe/GerardWeb/Publications_files/ArmourEtAl_AHT_JClim19.pdf>
- Hadley-Zelle der Nordhalbkugel 0,69 bis 1,09 · 10¹¹ kg/s (im Aufgabentext rund 0,8 · 10¹¹ kg/s): Li et al. (2022). *Journal of Geophysical Research: Atmospheres, 127*. <https://repository.library.noaa.gov/view/noaa/59743>
- AMOC bei 26,5° N 16,9 ± 1,2 Sv (2004 bis 2020), Arbeitswert 17 Sv, und Wärmestrom 1,20 ± 0,12 PW, Arbeitswert 1,2 PW (beide wie in Tutorium 5): Johns, W. E., et al. (2023). Towards two decades of Atlantic Ocean mass and heat transports at 26.5° N. *Philosophical Transactions of the Royal Society A, 381*, 20220188. <https://doi.org/10.1098/rsta.2022.0188>
- Einheit Sverdrup (1 Sv = 10⁶ m³/s): University of Miami (RSMAS), Ocean Surface Currents, Glossar, <https://oceancurrents.rsmas.miami.edu/glossary.html> ; Talley, L. D. (2019), SIO 210, <https://sam.ucsd.edu/ltalley/sio210/transports/>
- Verdampfungsenthalpie 2,43 MJ/kg (Wasser bei 30 °C, IAPWS-95): NIST Chemistry WebBook. <https://webbook.nist.gov/chemistry/fluid/>
- Normatmosphäre (mittlere Dichte der unteren 10 km 0,76 kg/m³ als eigene Rechnung aus dem Druckverlauf): AMS Glossary of Meteorology, „Standard atmosphere“. <https://glossary.ametsoc.org/wiki/Standard_atmosphere>
- Arbeitswerte und eigene Rechnungen (Aufgabenideen Ozean und Atmosphäre, Skript `nachrechnung_ozean_atmosphaere.py`, Version 3): Meerwasser *ρ* = 1025 kg/m³, *c*~p~ = 3990 J/(kg K); Luft am Boden *ρ* = 1,2 kg/m³, *c*~p~ = 1005 J/(kg K); *p*~0~ = 101 325 Pa; Erdbeschleunigung *g* = 9,81 m/s² (Standardwert wie in Tutorium 1); Ozean 71 % der Erdoberfläche; Δ*T* = 20 K und Δ*x* = 5 g/kg als Annahmen (Prüfung mit CoolProp: Luft mit 15 °C und 80 % relativer Feuchte enthält 8,5 g/kg, mit −5 °C 2,0 g/kg); Umfang des 40. Breitengrads 30 700 km (2π *R* cos 40° mit *R* = 6371 km); Höhe der betrachteten Luftschicht *H* = 10 km.

## Zusatzaufgabe 1: Gegenstrom im Entenfuß

- Stockenten verlieren in 0 bis 20 °C kaltem Wasser nur 3 bis 7 % ihrer Stoffwechselwärme über die Füße: Kilgore, D. L., & Schmidt-Nielsen, K. (1975). Heat loss from ducks’ feet immersed in cold water. *The Condor, 77*(4), 475 bis 478. <https://digitalcommons.usf.edu/condor/vol77/iss4/13> (Volltext)
- Effektivität für *C*\* = 1 im Gegen- und Gleichstrom: V06 F. 41.
- *NTU* = 4 ist ein gewählter Arbeitswert ohne Quelle (siehe Bericht).

## Zusatzaufgabe 2: Der Rekordflug

- Rekordflug am 9. Februar 2020 in 4 h 56 min, Jetstream über dem Sturm Ciara, rund 150 mph (67 m/s) Rückenwind nach Flightradar24, Jetstream 260 mph nach BBC Weather: NPR (9.2.2020), <https://www.npr.org/2020/02/09/804266975/british-airways-sets-speed-record-crossing-the-atlantic-in-under-5-hours> ; CILT UK (2020), <https://ciltuk.org.uk/News/Latest-News/ArtMID/6887/ArticleID/25239/Storm-Ciara-helps-plane-beat-transatlantic-flight-record>
- Reiseflug mit Mach 0,85: Boeing, *747-400 Airplane Characteristics for Airport Planning*, Rev. F, Abschn. 3.2.1. <https://www.boeing.com/content/dam/boeing/boeingdotcom/commercial/airports/acaps/747-400_Rev_F.pdf>
- Eigene Rechnung (Skript `nachrechnung_ozean_atmosphaere.py`): Großkreis JFK nach LHR 5540 km; Schallgeschwindigkeit in 10,7 km nach der Normatmosphäre 296,5 m/s, also 252 m/s bei Mach 0,85.
