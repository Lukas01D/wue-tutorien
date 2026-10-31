> Aufgabensammlung der Tutorien Wärmeübertragung, Markdown-Fassung ohne Steuerblöcke für LaTeX und Word. Stand 31.10.2026 (Kaffee-Aufgabe nach Prüfung und Abnahme; beschreibende Indizes in allen Tutorien aufrecht). Quelle: Aufgabensammlung_Tutorien_WUE_2026-10-31.md aus dem Arbeitsordner.

Entwurf zur Auswahl · Stand 31.10.2026 · Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn

Diese Sammlung enthält alle bisher erarbeiteten Aufgaben für die Tutorien 1 bis 8 in einer einheitlichen Struktur nach dem Vorbild der Lehrstuhl-Tutorien. Jeder Aufgabenblock beginnt mit einer **Ausgangssituation** mit Skizze. Danach folgen die **Fragen**, zuerst eine Vorab-Frage, zu der die Studierenden eine Vermutung notieren, und die **Aufgabe** mit Annahmen, gegebenen Größen und Aufgabenstellung. Das Ergebnis steht am Ende jedes rechnenden Teils. Kurze Rechnungen stehen als Zusatzaufgaben am Ende eines Tutoriums.

Die Sammlung ist bewusst umfangreich: Sie ist die Grundlage für die Auswahl und Kürzung je Tutorium. Lösungswege stehen nicht darin. Alle Zahlen stammen aus Rechenskripten, die Quellen der Arbeitswerte stehen im Anhang. Erstellt mit KI-Unterstützung (Claude, Anthropic); Auswahl, fachliche Prüfung und Freigabe durch die Tutoriumsleitung und die Professorin.

**Übersicht**

| Nr. | Thema | Aufgabenblöcke | Fragen, Zusatz | Kernrechnung |
|:------|:------------------|:------------------------------|:-----------------|:-----------------------------|
| 1 | Wärmeleitung | Seen unter dem Eisschild; Kühlhauswand | 3 Fragen, 1 Zusatzaufgabe | Fourier, mehrschichtige Wand, mittlere Wärmeleitfähigkeit, Randbedingungen |
| 2 | Konvektion | Offene Rinnen im Meereis | 4 Fragen, 1 Zusatzaufgabe | Platte erzwungen und frei, Grenzschicht, lokales und mittleres $\alpha$, charakteristische Länge |
| 3 | Wärmedurchgang | Meereis und Schnee als Deckel; Ölleitung im Permafrost | 3 Fragen, 1 Zusatzaufgabe | thermische Widerstände in Reihe, $kA = 1/R_{\mathrm{th}}$, Rohr mit $k_\mathrm{i}$ und $k_\mathrm{a}$ |
| 4 | Strahlung | Die Strahlungsbilanz der Erde | 4 Fragen, 2 Zusatzaufgaben | Stefan-Boltzmann, grauer Strahler, $\alpha + \rho + \tau = 1$, Kirchhoff |
| 5 | Wärmebilanzen (instationär global) | Kaffee mit Milch; Die AMOC und Europas milde Winter; Der Ozean als Wärmespeicher; Sverdrup und der Amazonas | 5 Fragen, 2 Zusatzaufgaben | $\mathrm{d}U/\mathrm{d}t$-Bilanz, Mischen, $T(t)$, Zeitkonstante, Massenbilanz |
| 6 | Wärmebilanzen (stationär differentiell) | Woher kommt die Erdwärme? | 4 Fragen, 1 Zusatzaufgabe | Bilanz am Element $\mathrm{d}z$ und $\mathrm{d}r$ mit Quelle, $T(z)$, $T(r)$ |
| 7 | Wärmebilanzen (instationär differentiell) | Das Gedächtnis des Bodens | 3 Fragen, 1 Zusatzaufgabe | Wärmeleitungsgleichung, Anfangs- und Randbedingungen, Temperaturleitfähigkeit |
| 8 | Wärmeübertrager und Verdampfer | Wärme aus dem Boden: Sole-Wasser-Wärmepumpe; Wer bringt die Wärme zum Pol, Luft oder Wasser? | 3 Fragen, 2 Zusatzaufgaben | Bilanz beider Ströme, $\Delta T_{\ln}$, $\varepsilon$-NTU, $C^* = 0$, Wärmekapazitätsstrom |

# Tutorium 1: Wärmeleitung

## Seen unter dem Eisschild

**Ausgangssituation**

In der Ostantarktis ist es bitterkalt: An der Station Wostok wurden am 21.\ Juli 1983 −89,2\ °C gemessen, der Kälterekord aller Wetterstationen. Im Jahresmittel hat die Oberfläche des Eisschilds dort etwa −55\ °C. Und doch liegen unter dem Eis Hunderte Seen. Als eine russische Bohrung im Februar 2012 in 3769\ m Tiefe den Wostoksee erreichte, war das Wasser kälter als 0\ °C und trotzdem flüssig. Die Wärme dafür kommt von unten: Aus dem Erdinneren dringt eine winzige Wärmestromdichte nach oben, im weltweiten Mittel nur rund 0,09\ W/m², so viel wie eine 40-W-Glühlampe, verteilt auf ein Basketballfeld. Reicht das, um das Eis an der Basis eines über drei Kilometer dicken Eisschilds zu schmelzen?

![](grafik/t1_eisschild.png){width=88%}

**Abb. 1:** Schnitt durch den Eisschild

**Frage 1** (Vorab-Frage)

Ein Eisschild besteht oben aus lockerem Firn und darunter aus dichtem Eis. In welcher Schicht ändert sich die Temperatur pro Meter Tiefe stärker? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe\ 1 rechnen.

- im Firn
- im Eis
- in beiden gleich

**Frage 2**

Ordnen Sie den Größen Temperatur, Wärme, Wärmestrom und Wärmestromdichte je eine der Einheiten J, W, W/m² und K zu. Beurteilen Sie anschließend die Aussage „Ein heißer Körper enthält viel Wärme.“

**Frage 3**

Die Profile in Abb.\ 2 sollen stationär sein, und keine der Wände enthält eine Wärmequelle. (1) In welcher Darstellung hat Schicht 1 die kleinere Wärmeleitfähigkeit? (2) Welche Darstellung kann so nicht stimmen? Begründen Sie mit der Richtung der Wärmeströme. (3) Was gilt im stationären Zustand für die Wärmestromdichte in beiden Schichten, und was folgt daraus für die Steigungen?

![](grafik/t1_profile.png){width=92%}

**Abb. 2:** Angeblich stationäre Temperaturprofile in drei Wänden aus zwei Schichten

**Aufgabe 1** (neu)

Untersuchen Sie für einen Standort in der Ostantarktis (Abb.\ 1), ob die Wärmestromdichte aus dem Erdinneren ausreicht, um die Basis des Eisschilds bis zum Schmelzpunkt zu erwärmen.

**Annahmen:**

- Der Eisschild wird als ebene Schicht betrachtet; die Wärmeleitung ist eindimensional in $z$-Richtung.
- Der Zustand ist stationär.
- Im Eis gibt es keine Wärmequellen; Reibungswärme wird vernachlässigt.
- Das Eis bewegt sich nicht.
- Wärmestrahlung im Eis wird vernachlässigt.
- Die Firnschicht wird bis Teil\ h vernachlässigt.

***Gegebene Größen:***

| ***Eisschild:*** | | ***Eis:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Dicke: | $H = 3700\,\mathrm{m}$ | Dichte: | $\rho = 917\,\mathrm{kg/m^3}$ |
| Temperatur oben: | $\vartheta_{\mathrm{O}} = -55\,\mathrm{°C}$ | Schmelzenthalpie: | $\Delta h_{\mathrm{schm}} = 333{,}5\,\mathrm{kJ/kg}$ |
| Wärmestromdichte: | $\dot{q}_{\mathrm{E}} = 58\,\mathrm{mW/m^2}$ | Schmelzpunkt sinkt: | $\gamma = 0{,}0742\,\mathrm{K/MPa}$ |
| Erdbeschleunigung: | $g = 9{,}81\,\mathrm{m/s^2}$ | | |
| | | | |
| ***Firn (oben):*** | | ***Bohrloch Dome C:*** | |
| Dicke: | $s_{\mathrm{F}} = 100\,\mathrm{m}$ | Tiefe 1: | $z_1 = 3200\,\mathrm{m}$ |
| Wärmeleitfähigkeit: | $\lambda_{\mathrm{F}} = 1{,}0\,\mathrm{W/(m\,K)}$ | Temperatur 1: | $\vartheta_1 = -4{,}2\,\mathrm{°C}$ |
| | | Tiefe 2: | $z_2 = 3270{,}2\,\mathrm{m}$ |
| | | Temperatur 2: | $\vartheta_2 = -2{,}34\,\mathrm{°C}$ |

Die Wärmeleitfähigkeit von Eis $\lambda(T) = a\,\exp(-b\,T)$ mit $a = 9{,}828\,\mathrm{W/(m\,K)}$, $b = 5{,}7\cdot 10^{-3}\,\mathrm{K^{-1}}$ und $T$ in K sowie die Schmelzpunktsenkung $\gamma$ sind hier gegeben (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Stellen Sie die gegebenen und die gesuchten Größen mit Formelzeichen zusammen. Welche Vorzeichen haben der Temperaturgradient $\mathrm{d}T/\mathrm{d}z$ und die Wärmestromdichte $\dot{q} = -\lambda\,\mathrm{d}T/\mathrm{d}z$ mit der Koordinate $z$ aus Abb.\ 1? Was bedeutet das Vorzeichen von $\dot{q}$?

b) Begründen Sie zwei der Annahmen in je einem Satz. Was bedeutet „eindimensional“ hier physikalisch?

c) Welche Randbedingung gilt an der Oberfläche, welche an der Basis? Ordnen Sie beide den Typen nach Dirichlet und nach von Neumann zu. Warum setzen Sie oben das Jahresmittel $\vartheta_{\mathrm{O}}$ an und nicht den Rekordwert von $-89{,}2\,\mathrm{°C}$?

d) Berechnen Sie die Wärmeleitfähigkeit des Eises an der Oberfläche und an der Basis (Näherung: $0\,\mathrm{°C}$) sowie die mittlere Wärmeleitfähigkeit $\lambda_{\mathrm{m}}$ als Integralmittel zwischen diesen beiden Temperaturen. Erklären Sie in zwei Sätzen, warum Firn mit Luft in den Poren schlechter leitet als dichtes Eis.\
   $\lambda(\vartheta_{\mathrm{O}}) = 2{,}83\,\mathrm{W/(m\,K)}$, $\quad\lambda(0\,\mathrm{°C}) = 2{,}07\,\mathrm{W/(m\,K)}$, $\quad\lambda_{\mathrm{m}} = 2{,}43\,\mathrm{W/(m\,K)}$

e) Nehmen Sie zunächst an, dass die gesamte Wärmestromdichte $\dot{q}_{\mathrm{E}}$ durch das Eis geleitet wird. Welche Temperatur $\vartheta_{\mathrm{B}}$ ergibt sich an der Basis ($\lambda_{\mathrm{m}}$ aus d)?\
   $\vartheta_{\mathrm{B}} = 33{,}2\,\mathrm{°C}$

f) Berechnen Sie den Druck $p$ an der Basis und den Druckschmelzpunkt $\vartheta_{\mathrm{pm}}$. Warum kann das Wasser des Wostoksees kälter als $0\,\mathrm{°C}$ sein? Vergleichen Sie $\vartheta_{\mathrm{pm}}$ mit Ihrem Ergebnis aus e): Welche Annahme ist verletzt, und was passiert an der Basis tatsächlich?\
   $p = 33{,}3\,\mathrm{MPa}$, $\quad\vartheta_{\mathrm{pm}} = -2{,}47\,\mathrm{°C}$

g) Die Basis liege nun genau am Druckschmelzpunkt. Welche Wärmestromdichte $\dot{q}_{\mathrm{leit}}$ wird dann noch durch das Eis geleitet ($\lambda_{\mathrm{m}}$ aus d)? Der Rest schmilzt an der Basis Eis. Wie viele Millimeter Eis schmelzen pro Jahr?\
   $\dot{q}_{\mathrm{leit}} = 34{,}5\,\mathrm{mW/m^2}$, $\quad v_{\mathrm{schm}} = 2{,}42\,\mathrm{mm/a}$

h) Prüfen Sie Ihr Modell an drei Stellen: (1) Ab welcher Eisdicke erreicht die Basis gerade den Schmelzpunkt aus f)? (2) Die oberen $s_{\mathrm{F}}$ bestehen aus Firn. In welcher Schicht ist das Temperaturprofil steiler, und um welchen Faktor (Eis mit $\lambda_{\mathrm{m}}$)? Vergleichen Sie mit Ihrer Vermutung zu Frage\ 1. (3) Welche Wärmestromdichte folgt aus den Messwerten im Bohrloch Dome C, wenn Sie $\lambda(-3\,\mathrm{°C})$ verwenden? Vergleichen Sie mit $\dot{q}_{\mathrm{E}}$. Bei welcher Temperatur schmilzt Eis in der Tiefe $z_2$, und wie viele Meter tiefer wäre der Schmelzpunkt bei gleichem Gradienten erreicht?\
   Zu (1): $H_{\mathrm{krit}} \approx 2200\,\mathrm{m}$, $\quad$zu (2): Faktor $2{,}43$\
   Zu (3): $\mathrm{d}T/\mathrm{d}z = 26{,}5\,\mathrm{K/km}$, $\quad\dot{q}_{\mathrm{C}} = 55{,}8\,\mathrm{mW/m^2}$,\
   $\vartheta_{\mathrm{pm}}(z_2) = -2{,}18\,\mathrm{°C}$, $\quad\Delta z \approx 6\,\mathrm{m}$

i) Erklären Sie in zwei bis drei Sätzen, warum Wasser an der Basis für einen Eisschild wichtig ist. Welche der Annahmen würden Sie als erste verbessern, und würde die Basis dadurch eher wärmer oder kälter?

## Kühlhauswand

**Ausgangssituation**

Hochsommer im Gewerbegebiet: Die Sonne heizt die Außenwand eines Kühlhauses auf. An ihrer äußeren Oberfläche messen Sie 28\ °C, an der inneren Oberfläche im Kühlraum −22\ °C. Die Wand besteht von außen nach innen aus Stahlbeton und einer Dämmung aus Polyurethan-Hartschaum. Jedes Watt, das durch die Wand dringt, muss die Kältemaschine wieder hinausbefördern. Der Betreiber möchte deshalb wissen, ob die Dämmung dick genug ist.

![](grafik/t1_kuehlhaus.png){width=80%}

**Abb. 3:** Schnitt durch die Kühlhauswand

**Aufgabe 2** (neu, technischer Zwilling)

Betrachten Sie nur die Wand zwischen den beiden gemessenen Oberflächen (Abb.\ 3).

**Annahmen:**

- Die Wärmeleitung durch die Wand ist stationär und eindimensional.
- Die Wand enthält keine Wärmequellen.
- Die Wärmeleitfähigkeit ist in jeder Schicht konstant.
- Zwischen Beton und Dämmung gibt es keinen Kontaktwiderstand.

***Gegebene Größen:***

| ***Stahlbeton:*** | | ***Dämmung:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Dicke: | $s_{\mathrm{B}} = 20\,\mathrm{cm}$ | Dicke: | $s_{\mathrm{D}} = 12\,\mathrm{cm}$ |
| Wärmeleitfähigkeit: | $\lambda_{\mathrm{B}} = 2{,}3\,\mathrm{W/(m\,K)}$ | Wärmeleitfähigkeit: | $\lambda_{\mathrm{D}} = 0{,}025\,\mathrm{W/(m\,K)}$ |
| | | | |
| ***Wand:*** | | ***Betreiber:*** | |
| Fläche: | $A = 250\,\mathrm{m^2}$ | Grenzwert: | $\dot{q}_{\mathrm{max}} = 8\,\mathrm{W/m^2}$ |
| Temperatur außen: | $\vartheta_{\mathrm{a}} = 28\,\mathrm{°C}$ | | |
| Temperatur innen: | $\vartheta_{\mathrm{i}} = -22\,\mathrm{°C}$ | | |

**Aufgabenstellung:**

a) Skizzieren Sie in Abb.\ 3 qualitativ den Temperaturverlauf durch die Wand. Welche der Annahmen ist an einem Sommertag am fragwürdigsten?

b) Berechnen Sie die Wärmestromdichte $\dot{q}$ und den Wärmestrom $\dot{Q}$ durch die gesamte Wand. Nutzen Sie, dass im stationären Zustand durch beide Schichten dieselbe Wärmestromdichte fließt.\
   $\dot{q} = 10{,}23\,\mathrm{W/m^2}$, $\quad\dot{Q} = 2{,}56\,\mathrm{kW}$

c) Welche Temperatur $\vartheta_{\mathrm{G}}$ herrscht an der Grenzfläche zwischen Beton und Dämmung? In welcher Schicht ist das Temperaturprofil steiler, und um welchen Faktor?\
   $\vartheta_{\mathrm{G}} = 27{,}11\,\mathrm{°C}$, $\quad$Faktor $92$

d) Der Betreiber möchte die Wärmestromdichte auf $\dot{q}_{\mathrm{max}}$ begrenzen. Wie dick muss die Dämmung mindestens sein? Runden Sie auf ganze Zentimeter auf und prüfen Sie den Grenzwert.\
   $s_{\mathrm{D,min}} = 15{,}41\,\mathrm{cm}$, $\quad\dot{q}(s_{\mathrm{D}} = 16\,\mathrm{cm}) = 7{,}71\,\mathrm{W/m^2}$

e) Lohnt es sich stattdessen, die Betonschicht doppelt so dick zu bauen? Begründen Sie mit Zahlen.\
   $\dot{q} = 10{,}05\,\mathrm{W/m^2}$

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Erdwärme in Deutschland

Die Kontinentale Tiefbohrung (KTB) in der Oberpfalz reicht bis in eine Tiefe von $z_{\mathrm{KTB}} = 9101\,\mathrm{m}$. Im Gestein steigt die Temperatur dort um etwa $28\,\mathrm{K/km}$; das Gestein hat eine Wärmeleitfähigkeit von etwa $\lambda_{\mathrm{KTB}} = 2{,}9\,\mathrm{W/(m\,K)}$.

a) Berechnen Sie die Wärmestromdichte $\dot{q}_{\mathrm{KTB}}$, die an der KTB aus dem Erdinneren nach oben geleitet wird.\
   $\dot{q}_{\mathrm{KTB}} = 81{,}2\,\mathrm{mW/m^2}$

b) Vergleichen Sie mit dem Eisschild aus Aufgabe\ 1 und mit dem weltweiten Mittel aus der Ausgangssituation. Warum ist der Temperaturgradient in der KTB größer als im Eis in Teil\ e, obwohl Gestein besser leitet als Eis?\
   $\dot{q}_{\mathrm{KTB}}/\dot{q}_{\mathrm{E}} = 1{,}40$, $\quad\lambda_{\mathrm{KTB}}/\lambda_{\mathrm{m}} = 1{,}19$

c) Um wie viel Kelvin ist das Gestein am Grund der Bohrung wärmer als an der Oberfläche, wenn der Gradient bis dorthin gleich bleibt? Welche Annahme aus Aufgabe\ 1 steckt in dieser Abschätzung?\
   $\Delta T = 254{,}8\,\mathrm{K}$

# Tutorium 2: Konvektion

## Offene Rinnen im Meereis

**Ausgangssituation**

Winter in der zentralen Arktis: Die Luft hat −30\ °C, und dickes Meereis bedeckt das Meer. Wind und Strömung reißen es aber immer wieder auf. In den offenen Rinnen liegt das Meerwasser frei; es hat −1,8\ °C und ist damit viel wärmer als die Luft. Über dem Wasser steigt Nebel auf, der „Seerauch“. Rinnen bedecken im Winter nur 1 bis 2\ % der Fläche, liefern aber über 70\ % der Wärme, die vom Ozean in die Luft gelangt. Wie viel Wärme trägt der Wind über einer Rinne fort, und spielt ihre Breite eine Rolle?

![](grafik/t2_rinne.png){width=80%}

**Abb. 1:** Offene Rinne im Meereis, von der Seite gesehen

**Frage 1** (Vorab-Frage)

Über zwei Rinnen im Meereis weht derselbe Wind. Die eine ist 1\ m breit, die andere 100\ m. Welche gibt pro Quadratmeter mehr Wärme ab? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe\ 1 rechnen.

- die 1\ m breite Rinne
- die 100\ m breite Rinne
- beide gleich viel

**Frage 2**

Freie oder erzwungene Konvektion? Ordnen Sie zu: (1) Seerauch über einer Rinne bei Windstille, (2) Föhn über einem Gletscher, (3) Heizkörper im Zimmer, (4) Passatwind über dem Pazifik, (5) Aufwind über einem Acker, (6) Lüfter im Rechner, (7) Tasse Tee auf dem Tisch, (8) fallendes Hagelkorn.

**Frage 3**

Ordnen Sie jeder Situation die charakteristische Länge $L$ zu (Auswahl: Länge in Strömungsrichtung, Durchmesser $d$, $\pi d/2$, $A/U$): (1) Wind über einer Rinne, (2) Wind quer zu einem Finger, (3) fallendes Hagelkorn, (4) Sole im Rohr einer Erdwärmesonde, (5) See bei Windstille.

**Frage 4**

Biot oder Nußelt? Beide Kennzahlen haben die Form $\alpha L/\lambda$. Ein Hagelkorn fällt durch kalte Luft. Welche Wärmeleitfähigkeit (Luft oder Eis) und welche Länge gehören in $Nu$, welche in $Bi$? Was sagt jede der beiden Kennzahlen aus?

**Aufgabe 1** (neu)

Betrachten Sie eine Rinne, die in Windrichtung $b$ breit und quer zum Wind $l$ lang ist (Abb.\ 1). Der Wind streicht erst über das Eis und dann über das offene Wasser.

**Annahmen:**

- Die Wasserfläche wird als ebene, längs angeströmte Platte betrachtet; beide Grenzschichten beginnen an der Eiskante.
- Der Zustand ist stationär; Windgeschwindigkeit und Lufttemperatur sind konstant.
- Die Wasseroberfläche hat überall die Temperatur $\vartheta_{\mathrm{W}}$.
- Die Stoffwerte der Luft werden bei der Filmtemperatur bestimmt und sind konstant.
- Verdunstung und Strahlung werden vernachlässigt.

***Gegebene Größen:***

| ***Rinne:*** | | ***Luft bei $\vartheta_{\mathrm{m}}$:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Breite: | $b = 10\,\mathrm{m}$ | Wärmeleitfähigkeit: | $\lambda = 0{,}02313\,\mathrm{W/(m\,K)}$ |
| Länge: | $l = 1\,\mathrm{km}$ | Kinem. Viskosität: | $\nu = 1{,}195\cdot 10^{-5}\,\mathrm{m^2/s}$ |
| Wassertemperatur: | $\vartheta_{\mathrm{W}} = -1{,}8\,\mathrm{°C}$ | Prandtl-Zahl: | $Pr = 0{,}713$ |
| | | | |
| ***Wind:*** | | ***Weitere Rinnen:*** | |
| Geschwindigkeit: | $w = 8\,\mathrm{m/s}$ | schmale Rinne: | $b_1 = 1\,\mathrm{m}$ |
| Lufttemperatur: | $\vartheta_{\mathrm{u}} = -30\,\mathrm{°C}$ | breite Rinne: | $b_2 = 100\,\mathrm{m}$ |

**Aufgabenstellung:**

a) Zeichnen Sie in Abb.\ 1 die Geschwindigkeits- und die Temperaturgrenzschicht über der Rinne qualitativ ein. Warum hat das Wasser $-1{,}8\,\mathrm{°C}$ und nicht $0\,\mathrm{°C}$?

b) Begründen Sie zwei der Annahmen in je einem Satz. Was bedeutet die Annahme, dass beide Grenzschichten an der Eiskante beginnen, und gilt sie auch für die Geschwindigkeitsgrenzschicht?

c) Welche Länge ist hier die charakteristische Länge $L$: die Breite $b$ in Windrichtung oder die Länge $l$ der Rinne? Begründen Sie mit dem Wachstum der Grenzschicht.

d) Bestimmen Sie die Filmtemperatur $\vartheta_{\mathrm{m}}$ und die Reynolds-Zahl $Re$. Ist die Strömung am Ende der Rinne laminar oder turbulent? Nach wie vielen Metern schlägt die Grenzschicht um (${Re_{\mathrm{krit}} = 5\cdot 10^{5}}$)?\
   $\vartheta_{\mathrm{m}} = -15{,}9\,\mathrm{°C}$, $\quad Re = 6{,}69\cdot 10^{6}$, $\quad x_{\mathrm{krit}} = 0{,}75\,\mathrm{m}$

e) Berechnen Sie mit der passenden Korrelation der Formelsammlung die Nußelt-Zahl $Nu$, den mittleren Wärmeübergangskoeffizienten $\alpha$ und die Wärmestromdichte $\dot{q}$. Welcher Wärmestrom $\dot{Q}$ geht von der ganzen Rinne an die Luft?\
   $Nu = 8488$, $\quad\alpha = 19{,}6\,\mathrm{W/(m^2\,K)}$, $\quad\dot{q} = 554\,\mathrm{W/m^2}$, $\quad\dot{Q} = 5{,}54\,\mathrm{MW}$

f) Wiederholen Sie die Rechnung für die schmale und die breite Rinne. Wie ändert sich das mittlere $\alpha$ mit der Breite? Gilt die Korrelation für die breite Rinne noch? Prüfen Sie damit Ihre Vermutung zu Frage\ 1.\
   $\alpha_1 = 32{,}1\,\mathrm{W/(m^2\,K)}$, $\quad\alpha_2 = 12{,}1\,\mathrm{W/(m^2\,K)}$ bei $Re_2 = 6{,}69\cdot 10^{7}$

g) Bei Windstille gibt die Rinne Wärme nur durch freie Konvektion ab. Berechnen Sie $\alpha$ und $\dot{q}$ für die waagerechte Wasserfläche mit $L = A/U$ und vergleichen Sie mit e).\
   $L = 4{,}95\,\mathrm{m}$, $\quad Gr = 9{,}67\cdot 10^{11}$, $\quad\alpha = 4{,}58\,\mathrm{W/(m^2\,K)}$, $\quad\dot{q} = 129\,\mathrm{W/m^2}$

h) Ist Ihr Ergebnis aus e) plausibel? Vergleichen Sie $\alpha$ mit den typischen Werten für erzwungene Konvektion in Gasen aus der Vorlesung. Welche Wärmeströme fehlen in der Rechnung? Denken Sie an den Seerauch.

i) Erklären Sie in drei bis vier Sätzen mit eigenen Zahlen, warum weniger Meereis die Erwärmung der Arktis im Winter verstärkt. Beziehen Sie die Angabe zu den Rinnen aus der Ausgangssituation ein.

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Windchill

Bei Wind fühlt sich Kälte kälter an. Die Windchill-Temperatur, die Wetterdienste in Nordamerika seit 2001 angeben, beruht auf einem einfachen Modell: Das Gesicht wird als quer angeströmter Zylinder behandelt. Rechnen Sie selbst mit Luft von $\vartheta_{\mathrm{u}} = -10\,\mathrm{°C}$ und Wind mit $w = 5\,\mathrm{m/s}$. Die Stoffwerte der Luft gelten bei $\vartheta_{\mathrm{u}}$: $\lambda = 0{,}02359\,\mathrm{W/(m\,K)}$, $\nu = 1{,}245\cdot 10^{-5}\,\mathrm{m^2/s}$, $Pr = 0{,}712$.

a) Berechnen Sie den mittleren Wärmeübergangskoeffizienten für einen Finger ($d_{\mathrm{F}} = 2\,\mathrm{cm}$) und für den Kopf ($d_{\mathrm{K}} = 18\,\mathrm{cm}$), beide als quer angeströmte Zylinder.\
   $\alpha_{\mathrm{F}} = 68{,}7\,\mathrm{W/(m^2\,K)}$, $\quad\alpha_{\mathrm{K}} = 33{,}3\,\mathrm{W/(m^2\,K)}$

b) Warum frieren Finger zuerst? Begründen Sie mit der Grenzschicht und Ihrem Ergebnis aus a).\
   $\alpha_{\mathrm{F}}/\alpha_{\mathrm{K}} = 2{,}06$

c) Wie groß ist $\alpha$ am Kopf bei fast windstillem Wetter ($w = 0{,}5\,\mathrm{m/s}$)? Um welchen Faktor steigt $\alpha$, wenn der Wind auf $5\,\mathrm{m/s}$ auffrischt?\
   $\alpha_{\mathrm{K}}(0{,}5\,\mathrm{m/s}) = 7{,}1\,\mathrm{W/(m^2\,K)}$, $\quad$Faktor $4{,}7$

# Tutorium 3: Wärmedurchgang

## Meereis und Schnee als Deckel

**Ausgangssituation**

Februar in der zentralen Arktis: Seit Monaten ist die Sonne nicht aufgegangen, und die Luft hat −30\ °C. Sie stehen auf einer großen Scholle aus einjährigem Meereis. Bei der Expedition MOSAiC war solches Eis im Februar meist etwa 1,4\ m dick, und darauf lagen 10 bis 30\ cm Schnee. Unter Ihren Füßen liegt der Arktische Ozean. Er hat −1,8\ °C, den Gefrierpunkt von Meerwasser, und ist damit fast 30\ K wärmer als die Luft. Eis und Schnee liegen wie ein Deckel auf dem Ozean und bremsen den Wärmestrom in die Atmosphäre. Ganz dicht ist dieser Deckel aber nicht, und das Eis wächst den ganzen Winter über von unten weiter. Wie viel Wärme entweicht, und wie kalt wird es an der Oberfläche des Schnees?

![](grafik/t3_meereis.png){width=85%}

**Abb. 1:** Schnee und Meereis zwischen Meerwasser und Luft

**Frage 1** (Vorab-Frage)

Was dämmt den Ozean besser gegen die kalte Luft? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe\ 1 rechnen.

- die 20\ cm Schnee
- die 1,4\ m Meereis
- beide etwa gleich gut

**Frage 2**

Ordnen Sie in der elektrischen Analogie dem Wärmestrom $\dot{Q}$, der Temperaturdifferenz $\Delta T$ und dem thermischen Widerstand $R_{\mathrm{th}}$ jeweils eine elektrische Größe zu: Spannung, Strom oder ohmscher Widerstand. Wie berechnen Sie den Gesamtwiderstand zweier Widerstände in Reihe, wie bei einer Parallelschaltung?

**Aufgabe 1** (neu)

Betrachten Sie einen Ausschnitt der Scholle mit der Fläche $A$.

**Annahmen:**

- Der Wärmetransport wird als stationär und eindimensional angenommen.
- Die Wärmeleitfähigkeiten von Schnee und Eis werden als konstant angenommen.
- Der Wärmeübergang an die Luft wird mit dem konstanten Wärmeübergangskoeffizienten $\alpha_\mathrm{a}$ beschrieben (Arbeitswert für eine große Scholle). Strahlung an der Schneeoberfläche wird vernachlässigt.
- Die Unterseite des Eises hat die Temperatur des Meerwassers.

***Gegebene Größen:***

| ***Luft:*** | | ***Meerwasser:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Temperatur: | $\vartheta_\mathrm{u} = -30\,\mathrm{°C}$ | Temperatur: | $\vartheta_\mathrm{W} = -1{,}8\,\mathrm{°C}$ |
| Wärmeübergang: | $\alpha_\mathrm{a} = 15\,\mathrm{W/(m^2\,K)}$ | | |
| | | | |
| ***Schnee:*** | | ***Meereis:*** | |
| Dicke: | $s_\mathrm{S} = 0{,}2\,\mathrm{m}$ | Dicke: | $s_\mathrm{E} = 1{,}4\,\mathrm{m}$ |
| Wärmeleitfähigkeit: | $\lambda_\mathrm{S} = 0{,}2\,\mathrm{W/(m\,K)}$ | Wärmeleitfähigkeit: | $\lambda_\mathrm{E} = 2{,}1\,\mathrm{W/(m\,K)}$ |
| | | Dichte: | $\rho_\mathrm{E} = 917\,\mathrm{kg/m^3}$ |
| | | Schmelzenthalpie: | $\Delta h_{\mathrm{schm}} = 333{,}5\,\mathrm{kJ/kg}$ |
| | | | |
| ***Ausschnitt:*** | | ***Jungeis (Teil f):*** | |
| Fläche: | $A = 1\,\mathrm{m^2}$ | Dicke: | $s_\mathrm{J} = 0{,}1\,\mathrm{m}$ |

**Aufgabenstellung:**

a) Warum hat die Unterseite des Eises genau die Temperatur $\vartheta_\mathrm{W}$? Zeichnen Sie neben Abb.\ 1 das Ersatzschaltbild der thermischen Widerstände zwischen Meerwasser und Luft.

b) Welche der Annahmen halten Sie für am fragwürdigsten? Begründen Sie Ihre Wahl in zwei Sätzen.

c) Berechnen Sie die thermischen Widerstände des Wärmeübergangs an die Luft $R_{\mathrm{th},\alpha}$, der Schneeschicht $R_{\mathrm{th,S}}$ und der Eisschicht $R_{\mathrm{th,E}}$. Welcher ist am größten? Prüfen Sie damit Ihre Vermutung zu Frage\ 1. Je nach Dichte liegt $\lambda_\mathrm{S}$ zwischen $0{,}14$ und $0{,}3\,\mathrm{W/(m\,K)}$: In welchem Bereich liegt dann $R_{\mathrm{th,S}}$?\
   $R_{\mathrm{th},\alpha} = 0{,}0667\,\mathrm{K/W}$, $\quad R_{\mathrm{th,S}} = 1{,}00\,\mathrm{K/W}$, $\quad R_{\mathrm{th,E}} = 0{,}667\,\mathrm{K/W}$\
   Bereich: $R_{\mathrm{th,S}} = 0{,}667$ bis $1{,}43\,\mathrm{K/W}$

d) Berechnen Sie den Gesamtwiderstand $R_{\mathrm{th,ges}}$, das Produkt $kA$ und den Wärmestrom $\dot{Q}$. Bestimmen Sie die Temperatur $\vartheta_\mathrm{O}$ an der Schneeoberfläche und die Temperatur $\vartheta_{\mathrm{SE}}$ an der Grenze zwischen Schnee und Eis.\
   $R_{\mathrm{th,ges}} = 1{,}73\,\mathrm{K/W}$, $\quad kA = 0{,}577\,\mathrm{W/K}$, $\quad \dot{Q} = 16{,}3\,\mathrm{W}$\
   $\vartheta_\mathrm{O} = -28{,}9\,\mathrm{°C}$, $\quad \vartheta_{\mathrm{SE}} = -12{,}6\,\mathrm{°C}$

e) Prüfen Sie Ihr Ergebnis an drei Stellen. (1) Über welcher Schicht fällt die größte Temperaturdifferenz ab, und ergeben die drei Teildifferenzen zusammen die Gesamtdifferenz? (2) Welche Wärmestromdichte $\dot{q}_\mathrm{W}$ gibt offenes Wasser bei gleichem $\alpha_\mathrm{a}$ an die Luft ab, und um welchen Faktor ist sie größer als mit Eis und Schnee? (3) Für die 10\ m breite Rinne aus Tutorium\ 2 (Aufgabe\ 1, Teil\ e) ergaben sich $\alpha = 19{,}6\,\mathrm{W/(m^2\,K)}$ und $\dot{q} = 554\,\mathrm{W/m^2}$. Wie ändert sich $\dot{Q}$ mit Eis und Schnee, wenn Sie dieses $\alpha$ verwenden? Warum ändert er sich so wenig?\
   Zu (1): $\Delta T_\mathrm{S} = 16{,}3\,\mathrm{K}$, $\quad 1{,}08\,\mathrm{K} + 16{,}3\,\mathrm{K} + 10{,}8\,\mathrm{K} = 28{,}2\,\mathrm{K}$\
   Zu (2): $\dot{q}_\mathrm{W} = 423\,\mathrm{W/m^2}$, Faktor 26; $\quad$ zu (3): $\dot{Q} = 16{,}4\,\mathrm{W}$

f) Die Wärme, die durch Schnee und Eis entweicht, wird an der Unterseite des Eises beim Gefrieren von Meerwasser frei. Berechnen Sie mit einer Energiebilanz, um wie viele Zentimeter das Eis pro Tag wächst. Vergleichen Sie mit Jungeis der Dicke $s_\mathrm{J}$ ohne Schnee, wie es in einer frisch zugefrorenen Rinne entsteht: Wie groß sind dort die Wärmestromdichte $\dot{q}_\mathrm{J}$ und das Wachstum? Was folgt daraus für eine Arktis, in der das Eis im Mittel dünner wird?\
   $\mathrm{d}s_\mathrm{E}/\mathrm{d}t = 0{,}46\,\mathrm{cm/d}$; $\quad$ Jungeis: $\dot{q}_\mathrm{J} = 247\,\mathrm{W/m^2}$, $\quad \mathrm{d}s_\mathrm{J}/\mathrm{d}t = 6{,}97\,\mathrm{cm/d}$

## Ölleitung im Permafrost

**Ausgangssituation**

Die Trans-Alaska-Pipeline bringt Rohöl von der Nordküste Alaskas quer durch das Land nach Süden. Das Öl ist rund 30\ °C warm, der Boden unter der Leitung ist über weite Strecken dauerhaft gefroren. Auf etwa der Hälfte der Strecke liegt die gedämmte Leitung nicht im Boden, sondern steht auf Stützen in der Luft. Im Winter weht dort der Wind bei −30\ °C um das Rohr. Wie viel Wärme verliert das Öl auf jedem Meter?

![](grafik/t3_oelleitung.png){width=80%}

**Abb. 2:** Querschnitt der gedämmten Ölleitung

**Frage 3** (Vorab-Frage)

Welche Aussagen über ein gedämmtes Rohr sind richtig? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe\ 2 rechnen.

- [ ] Der Wärmedurchgangskoeffizient $k_\mathrm{a}$, bezogen auf die Außenfläche, ist kleiner als $k_\mathrm{i}$, bezogen auf die Innenfläche.
- [ ] Das Produkt $kA$ hängt davon ab, auf welche Fläche $k$ bezogen wird.
- [ ] Bei einem dünnwandigen Rohr ohne Dämmung sind $k_\mathrm{i}$ und $k_\mathrm{a}$ fast gleich.

**Aufgabe 2** (neu)

Betrachten Sie einen Abschnitt der Leitung mit der Länge $L$ im Winter. Der Wind strömt quer zur Leitung.

**Annahmen:**

- Der Wärmetransport wird als stationär und rein radial angenommen.
- Die Öltemperatur wird im betrachteten Abschnitt als konstant angenommen.
- Die Stoffwerte sind unabhängig von der Temperatur. Für die Luft gelten sie bei der Filmtemperatur $\vartheta_\mathrm{m} = -29\,\mathrm{°C}$ (die Oberfläche der Dämmung ist nur wenig wärmer als die Luft).
- Strahlung an der Oberfläche der Dämmung wird vernachlässigt.

***Gegebene Größen:***

| ***Öl:*** | | ***Luft:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Temperatur: | $\vartheta_\mathrm{i} = 30\,\mathrm{°C}$ | Temperatur: | $\vartheta_\mathrm{u} = -30\,\mathrm{°C}$ |
| Wärmeübergang: | $\alpha_\mathrm{i} = 500\,\mathrm{W/(m^2\,K)}$ | Geschwindigkeit: | $w = 5\,\mathrm{m/s}$ |
| | | Kinem. Viskosität: | $\nu_\mathrm{L} = 1{,}087\cdot 10^{-5}\,\mathrm{m^2/s}$ |
| | | Wärmeleitfähigkeit: | $\lambda_\mathrm{L} = 0{,}0221\,\mathrm{W/(m\,K)}$ |
| | | Prandtl-Zahl: | $Pr = 0{,}716$ |
| | | | |
| ***Stahlrohr:*** | | ***Dämmung:*** | |
| Außendurchmesser: | $d_{\mathrm{St}} = 1{,}22\,\mathrm{m}$ | Dicke: | $s_{\mathrm{Iso}} = 9{,}5\,\mathrm{cm}$ |
| Wanddicke: | $s_{\mathrm{St}} = 14{,}3\,\mathrm{mm}$ | Wärmeleitfähigkeit: | $\lambda_{\mathrm{Iso}} = 0{,}04\,\mathrm{W/(m\,K)}$ |
| Wärmeleitfähigkeit: | $\lambda_{\mathrm{St}} = 45\,\mathrm{W/(m\,K)}$ | | |
| | | | |
| ***Abschnitt:*** | | | |
| Länge: | $L = 1\,\mathrm{m}$ | | |

**Aufgabenstellung:**

a) Berechnen Sie den Wärmeübergangskoeffizienten $\alpha_\mathrm{a}$ an der Außenseite der Dämmung.\
   $Re = 1{,}02\cdot 10^{6}$, $\quad Nu_\mathrm{m} = 2024$, $\quad \alpha_\mathrm{a} = 20{,}2\,\mathrm{W/(m^2\,K)}$

b) Berechnen Sie die vier thermischen Widerstände zwischen Öl und Luft und den Wärmestrom $\dot{Q}$. Welcher Widerstand bestimmt den Wärmestrom?\
   $R_{\mathrm{th,i}} = 5{,}34\cdot 10^{-4}\,\mathrm{K/W}$, $\quad R_{\mathrm{th,St}} = 8{,}39\cdot 10^{-5}\,\mathrm{K/W}$, $\quad R_{\mathrm{th,Iso}} = 0{,}576\,\mathrm{K/W}$\
   $R_{\mathrm{th,a}} = 0{,}0112\,\mathrm{K/W}$, $\quad R_{\mathrm{th,ges}} = 0{,}588\,\mathrm{K/W}$, $\quad \dot{Q} = 102\,\mathrm{W}$

c) Berechnen Sie die Temperatur $\vartheta_\mathrm{O}$ an der Oberfläche der Dämmung. War die Annahme zur Filmtemperatur berechtigt?\
   $\vartheta_\mathrm{O} = -28{,}9\,\mathrm{°C}$, $\quad \vartheta_\mathrm{m} = -29{,}4\,\mathrm{°C}$

d) Berechnen Sie den Wärmedurchgangskoeffizienten $k_\mathrm{i}$, bezogen auf die Innenfläche $A_\mathrm{i}$ des Stahlrohrs, und $k_\mathrm{a}$, bezogen auf die Außenfläche $A_\mathrm{a}$ der Dämmung. Warum gibt es zwei Werte? Zeigen Sie, dass $k_\mathrm{i} A_\mathrm{i} = k_\mathrm{a} A_\mathrm{a}$ gilt, und prüfen Sie Ihre Antworten zu Frage\ 3.\
   $k_\mathrm{i} = 0{,}455\,\mathrm{W/(m^2\,K)}$, $\quad k_\mathrm{a} = 0{,}384\,\mathrm{W/(m^2\,K)}$, $\quad k_\mathrm{i} A_\mathrm{i} = k_\mathrm{a} A_\mathrm{a} = 1{,}70\,\mathrm{W/K}$

e) Um ein sehr dünnes Rohr kann eine Dämmung den Wärmestrom sogar vergrößern. Leiten Sie aus $R_{\mathrm{th,ges}}$ den kritischen Außenradius $r_{\mathrm{krit}}$ der Dämmung her, bei dem der Wärmestrom am größten ist. Berechnen Sie ihn und begründen Sie, warum die Dämmung der Ölleitung trotzdem wirkt.\
   $r_{\mathrm{krit}} = \lambda_{\mathrm{Iso}}/\alpha_\mathrm{a} = 1{,}98\,\mathrm{mm}$

f) Warum steht die Leitung im Permafrost auf Stützen, statt im Boden zu liegen? In vielen Stützen stecken zusätzlich Wärmerohre, die im Winter Wärme aus dem Boden an die Luft abgeben. Wozu dienen sie, und was bedeutet eine weitere Erwärmung der Arktis für Straßen, Leitungen und Häuser auf Permafrost?

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Schneefreie Stellen

Der Wind hat den Schnee von 10\ % der Scholle aus Aufgabe\ 1 weggeweht. Dort liegt nur das Eis; alle anderen Werte bleiben gleich. Betrachten Sie wieder einen Ausschnitt mit $A = 1\,\mathrm{m^2}$, davon $0{,}9\,\mathrm{m^2}$ mit und $0{,}1\,\mathrm{m^2}$ ohne Schnee.

a) Zeichnen Sie das Ersatzschaltbild und berechnen Sie den Gesamtwiderstand $R_{\mathrm{th,ges}}$.\
   $R_{\mathrm{th,ges}} = 1{,}53\,\mathrm{K/W}$

b) Berechnen Sie den Wärmestrom $\dot{Q}$. Um wie viel Prozent steigt er gegenüber der geschlossenen Schneedecke?\
   $\dot{Q} = 18{,}5\,\mathrm{W}$, $\quad$ Zunahme: $13{,}6\,\%$

c) Welcher Anteil des Wärmestroms entweicht durch die schneefreien 10\ % der Fläche? Nennen Sie ein Beispiel aus einem Gebäude, bei dem derselbe Effekt auftritt.\
   Anteil: $20{,}8\,\%$

# Tutorium 4: Strahlung

## Die Strahlungsbilanz der Erde

**Ausgangssituation**

Die Erde schwebt im fast leeren, eiskalten Weltall und tauscht mit ihm Energie nur durch Strahlung aus. Von der Sonne kommen am Rand der Atmosphäre 1361\ W/m² an, gemessen auf einer Fläche senkrecht zu den Sonnenstrahlen. Etwa 30\ % davon werfen Wolken, Schnee und Eis gleich wieder ins All zurück. Den Rest nimmt die Erde auf und gibt ihn als Wärmestrahlung wieder ab, in alle Richtungen, bei Tag und bei Nacht. Aus dem Erdinneren kommen dagegen im Mittel nur etwa 0,09\ W/m². An der Oberfläche misst man heute eine mittlere Temperatur von rund 15\ °C. Ist das warm oder kalt für einen Planeten in diesem Abstand zur Sonne? Und welche Rolle spielt die dünne Hülle aus Luft, Wasserdampf und Kohlendioxid?

![](grafik/t4_erde.png){width=85%}

**Abb. 1:** Die Erde im Sonnenlicht mit einer dünnen Atmosphärenschicht

**Frage 1** (Vorab-Frage)

Ohne Atmosphäre wäre die Erde im Mittel etwa −18\ °C kalt, gemessen werden rund 15\ °C. Woher kommen die fehlenden 33\ K? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe\ 1 rechnen.

**Frage 2**

Warum kann eine Autoscheibe in einer klaren Nacht vereisen, obwohl die Luft wärmer als 0\ °C ist? Warum bleibt sie unter einer geschlossenen Wolkendecke meist frei?

**Frage 3**

Welche Aussagen sind richtig? Kreuzen Sie an.

- [ ] Ein Körper, der bei einer Wellenlänge gut absorbiert, strahlt bei dieser Wellenlänge auch gut ab.
- [ ] Schnee wirft 80 bis 90\ % des Sonnenlichts zurück und strahlt deshalb im Infraroten nur schwach ab.
- [ ] Eine weiß gestrichene Wand kann im Infraroten fast so stark abstrahlen wie ein schwarzer Körper.
- [ ] Für einen grauen Strahler gilt $\alpha = \varepsilon$.

**Frage 4**

Beurteilen Sie die Aussage: „Durch das Ozonloch kommt mehr Wärme auf die Erde, deshalb wird es wärmer.“ In welchem Bereich des Spektrums wirkt die Ozonschicht, in welchem der Treibhauseffekt?

**Aufgabe 1** (neu)

Prüfen Sie Ihre Vermutung zu Frage\ 1 mit Strahlungsbilanzen: zuerst für eine Erde ohne Atmosphäre, dann mit einer einfachen Atmosphärenschicht.

**Annahmen:**

- Die Erde wird als stationär angenommen; ihre Oberfläche hat überall dieselbe Temperatur.
- Die Erde strahlt im Infraroten wie ein schwarzer Körper ab. Das Weltall hat etwa 0\ K.
- Die planetare Albedo $\rho_\mathrm{p}$ wird als konstant angenommen.
- Der Wärmestrom aus dem Erdinneren wird vernachlässigt.
- Ab Teil\ e ist die Atmosphäre eine dünne Schicht mit einheitlicher Temperatur $T_\mathrm{A}$. Sie lässt das Sonnenlicht vollständig durch und ist für Wärmestrahlung ein grauer Strahler mit dem Emissionsgrad $\varepsilon_\mathrm{A}$.

***Gegebene Größen:***

| ***Sonne:*** | | ***Erde:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Solarkonstante: | $S_0 = 1361\,\mathrm{W/m^2}$ | Planetare Albedo: | $\rho_\mathrm{p} = 0{,}30$ |
| | | Mitteltemperatur: | $T_\mathrm{O} = 288\,\mathrm{K}$ |
| | | Erdwärme: | $\dot{q}_\mathrm{E} = 0{,}09\,\mathrm{W/m^2}$ |
| | | | |
| ***CO~2~ verdoppelt:*** | | | |
| Strahlungsantrieb: | $\Delta\dot{q} = 3{,}93\,\mathrm{W/m^2}$ | | |

Die Stefan-Boltzmann-Konstante ${\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}}$ ist hier gegeben (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Die Sonnenstrahlung trifft die Erde auf ihrer Querschnittsfläche $\pi R^2$, abgestrahlt wird über die ganze Oberfläche $4\pi R^2$ (Abb.\ 1). Begründen Sie damit, warum in der Bilanz je Quadratmeter Erdoberfläche die Strahlungsflussdichte $S_0/4$ auftritt, und berechnen Sie sie.\
   $S_0/4 = 340\,\mathrm{W/m^2}$

b) Welche der Annahmen halten Sie für am fragwürdigsten? Begründen Sie Ihre Wahl.

c) Ordnen Sie die planetare Albedo $\rho_\mathrm{p}$ in die Beziehung $\alpha + \rho + \tau = 1$ ein. Berechnen Sie die Strahlungsflussdichte $\dot{q}_{\mathrm{abs}}$, die die Erde im Mittel absorbiert.\
   $\dot{q}_{\mathrm{abs}} = 238\,\mathrm{W/m^2}$

d) Berechnen Sie (1) die Gleichgewichtstemperatur $T_\mathrm{e}$ der Erde ohne Atmosphäre in K und °C und (2) die Temperatur $T$, die die Oberfläche ohne Sonne nur mit der Wärme aus dem Erdinneren hätte. Vergleichen Sie (1) mit dem Wert aus Frage\ 1. Ist die vierte Annahme gerechtfertigt?\
   Zu (1): $T_\mathrm{e} = 254{,}6\,\mathrm{K} = -18{,}6\,\mathrm{°C}$; zu (2): $T = 35{,}5\,\mathrm{K}$

e) Begründen Sie mit dem Kirchhoff’schen Gesetz, warum die Atmosphärenschicht Wärmestrahlung mit dem Absorptionsgrad $\alpha_\mathrm{A} = \varepsilon_\mathrm{A}$ absorbiert. Ordnen Sie $\alpha$, $\rho$ und $\tau$ der Schicht getrennt für Sonnenlicht und für Wärmestrahlung zu.

f) Stellen Sie die stationären Energiebilanzen für die Erdoberfläche und für die Atmosphärenschicht auf. Leiten Sie daraus die Oberflächentemperatur $T_\mathrm{O}$ als Funktion von $T_\mathrm{e}$ und $\varepsilon_\mathrm{A}$ her. Welcher Emissionsgrad $\varepsilon_\mathrm{A}$ ergibt $T_\mathrm{O} = 288\,\mathrm{K}$, und welche Temperatur $T_\mathrm{A}$ hat die Schicht dann?\
   $T_\mathrm{O} = T_\mathrm{e}\left(\frac{2}{2-\varepsilon_\mathrm{A}}\right)^{1/4}$, $\quad\varepsilon_\mathrm{A} = 0{,}78$, $\quad T_\mathrm{A} = 242{,}2\,\mathrm{K}$

g) Prüfen Sie das Schichtmodell. (1) Welche Oberflächentemperaturen ergeben die Grenzfälle ${\varepsilon_\mathrm{A} = 0}$ und ${\varepsilon_\mathrm{A} = 1}$? (2) Im globalen Mittel werden eine Gegenstrahlung (Wärmestrahlung der Atmosphäre zur Oberfläche) von 342\ W/m² und eine Abstrahlung der Oberfläche von 398\ W/m² gemessen. Die Atmosphäre absorbiert rund 80\ W/m² der Sonnenstrahlung, und die Oberfläche verliert rund 21\ W/m² durch Konvektion und 82\ W/m² durch Verdunstung (Forster et al., 2021). Berechnen Sie die Gegenstrahlung $\dot{q}_\mathrm{G}$ der Schicht im Modell und vergleichen Sie. Erklären Sie den Unterschied mit einer Energiebilanz der Oberfläche aus den Messwerten. Welchen Anteil der Abstrahlung machen Konvektion und Verdunstung zusammen aus? Dürfen sie neben der Strahlung vernachlässigt werden?\
   Zu (1): $T_\mathrm{O} = 254{,}6\,\mathrm{K}$ bzw. $302{,}7\,\mathrm{K}$; zu (2): $\dot{q}_\mathrm{G} = 152\,\mathrm{W/m^2}$, Anteil $26\,\%$

h) Eine Verdopplung von CO~2~ wirkt ohne Rückkopplungen wie eine zusätzliche Strahlungsflussdichte $\Delta\dot{q}$, die die Erde aufnimmt (Strahlungsantrieb). Für kleine Änderungen gilt $\Delta\dot{q} \approx 4\sigma T_\mathrm{e}^3\,\Delta T$ (hier gegeben, nicht in der Formelsammlung). Um wie viel erwärmt sich die Erde? Mit Rückkopplungen nennt die Forschung etwa 3\ K (IPCC, 2021): Welche Effekte fehlen in Ihrer Rechnung?\
   $4\sigma T_\mathrm{e}^3 = 3{,}74\,\mathrm{W/(m^2\,K)}$, $\quad \Delta T = 1{,}05\,\mathrm{K}$

i) Erklären Sie in drei Sätzen für Laien, warum mehr CO~2~ die Oberfläche erwärmt, obwohl CO~2~ selbst keine Wärme erzeugt.

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Eis aus der Nacht

In Indien wurde im 18. Jahrhundert in flachen Schalen Eis hergestellt, obwohl die Luft wärmer als 0\ °C war. Eine flache Schale mit Wasser steht in einer klaren Nacht auf einer dicken Lage Stroh. Die Luft hat $\vartheta_\mathrm{L} = 5\,\mathrm{°C}$. Der klare Himmel wirkt für die Strahlung wie ein schwarzer Körper mit $\vartheta_\mathrm{H} = -20\,\mathrm{°C}$. Das Wasser ist ein grauer Strahler mit $\varepsilon = 0{,}96$. Der Wärmeübergangskoeffizient zur Luft liegt je nach Wind zwischen $\alpha_\mathrm{L} = 2$ und $5\,\mathrm{W/(m^2\,K)}$. Wärme aus dem Boden wird vernachlässigt.

a) Stellen Sie die stationäre Energiebilanz für die Wasseroberfläche auf.

b) Berechnen Sie die Gleichgewichtstemperatur $\vartheta$ des Wassers für beide Werte von $\alpha_\mathrm{L}$ (iterativ, etwa mit dem Taschenrechner).\
   $\alpha_\mathrm{L} = 2\,\mathrm{W/(m^2\,K)}$: $\vartheta = -11{,}3\,\mathrm{°C}$; $\quad \alpha_\mathrm{L} = 5\,\mathrm{W/(m^2\,K)}$: $\vartheta = -5{,}9\,\mathrm{°C}$

c) Warum gelingt das nur in klaren, möglichst windstillen Nächten? Was passiert, sobald das Wasser 0\ °C erreicht?

**Zusatzaufgabe 2** (neu): Autoscheibe und Reif

Rechnen Sie Frage\ 2 nach. Ein Auto steht nachts im Freien. Die Windschutzscheibe aus Glas ($\varepsilon = 0{,}95$) tauscht Strahlung mit ihrer Umgebung aus. Die schräge Scheibe sieht neben dem klaren Himmel auch Häuser und Bäume; zusammen wirkt diese Umgebung für die Strahlung wie ein schwarzer Körper mit $\vartheta_\mathrm{H} = -5\,\mathrm{°C}$. Die Luft mit der Temperatur $\vartheta_\mathrm{L}$ gibt über $\alpha_\mathrm{L} = 5\,\mathrm{W/(m^2\,K)}$ Wärme an die Scheibe ab. Wärme aus dem Wageninneren wird vernachlässigt.

a) Stellen Sie die stationäre Energiebilanz für die Scheibe auf. Bis zu welcher Lufttemperatur $\vartheta_\mathrm{L}$ kühlt die Scheibe auf 0\ °C oder darunter ab, sodass sie vereisen kann?\
   $\vartheta_\mathrm{L} = 4{,}27\,\mathrm{°C}$

b) Bei Wind steigt der Wärmeübergangskoeffizient auf $\alpha_\mathrm{L} = 10\,\mathrm{W/(m^2\,K)}$. Wie verschiebt sich die Grenze? Warum vereisen Scheiben vor allem in windstillen Nächten?\
   $\vartheta_\mathrm{L} = 2{,}14\,\mathrm{°C}$

c) Welche Annahme halten Sie für am fragwürdigsten? Liegt die wahre Grenze dadurch höher oder tiefer?

# Tutorium 5: Wärmebilanzen (instationär global)

## Kaffee mit Milch

**Ausgangssituation**

Sonntagmorgen in der WG-Küche: Sie haben Filterkaffee gekocht und zwei gleiche Tassen mit je 200 ml gefüllt. Da klingelt das Telefon, und das Gespräch wird eine Stunde dauern. Ihr Mitbewohner gießt seine Milch sofort in den Kaffee (Tasse 1). Sie stellen Ihre Tasse daneben und wollen die Milch erst nach dem Telefonat hineingießen (Tasse 2), damit der Kaffee „länger heiß bleibt“. Die Milch kommt in beiden Fällen direkt aus dem Kühlschrank.

![](grafik/t5_kaffee_tassen.png){width=92%}

**Abb. 1:** Die beiden Tassen

**Frage 1** (Vorab-Frage)

Ihr Mitbewohner meint: „Ob man die Milch sofort oder später hineingießt, ist egal. Die Energie bleibt ja erhalten.“ Welche Tasse ist nach einer Stunde wärmer: Tasse 1, Tasse 2, oder sind beide gleich warm? Notieren Sie Ihre Vermutung mit einem Satz Begründung, bevor Sie Aufgabe 1 rechnen.

**Frage 2**

Bilanz-Detektiv: Ordnen Sie jede Situation einer der vier Grundformen der Energiebilanz zu (stationär global, stationär differentiell, instationär global oder instationär differentiell).

- Ein Eisberg schmilzt im Meer: Wie lange dauert es, bis er verschwunden ist?
- Erdkruste mit radioaktiver Wärmequelle: Wie warm ist es in 10\ km Tiefe?
- Boden im Tagesgang: Zu welcher Uhrzeit ist es in 20\ cm Tiefe am wärmsten?
- Wärmeübertrager als Ganzes: Mit welcher Temperatur verlässt das Wasser den Apparat?
- Kraftwerk am Fluss: Um wie viel erwärmt sich der Fluss durch die Abwärme?

**Frage 3**

Welche Körper dürfen beim Abkühlen oder Erwärmen als überall gleich warm gelten? Kreuzen Sie an und begründen Sie kurz mit der Biot-Zahl oder mit der Durchmischung.

- [ ] dünner Kupferdraht, der an der Luft abkühlt
- [ ] Kartoffel, die nach dem Kochen an der Luft abkühlt
- [ ] Käse aus Foliensatz 08, Teil e (30\ cm hohe Form, Wärmeabgabe nur über die Oberseite)
- [ ] kleines Hagelkorn, das durch die Luft fällt
- [ ] Eisberg im Meer
- [ ] durchmischte Deckschicht des Ozeans

Ist die Aussage „Im stationären Zustand fließt keine Wärme.“ richtig oder falsch? Begründen Sie mit einer Situation aus Frage 2.

**Aufgabe 1** (neu)

Um die Frage zu klären, messen Sie nach 10 Minuten die Temperatur in Tasse 2 (noch ohne Milch).

**Annahmen:**

- Der Tasseninhalt ist ideal durchmischt, die Milch mischt sich sofort und ohne Wärmeverlust.
- Die Wärmekapazität der Tasse wird außer in Teil g vernachlässigt.
- Die gesamte Wärmeabgabe (auch durch Strahlung und Verdunstung) ist $\dot{Q}_{\mathrm{ab}} = kA\,(\vartheta - \vartheta_\mathrm{u})$ mit konstantem $kA$; die verdunstete Masse wird vernachlässigt.
- Kaffee (Stoffdaten von Wasser) und Milch sind inkompressibel ($c_p = c_v$); die Stoffdaten sind konstant.

**Gegebene Größen:**

| **Kaffee** | | **Milch** | |
|:-------------------------------------|:-------------------------------------------|:-------------------------------------|:-------------------------------------------|
| Volumen | $V_\mathrm{K} = 200\,\mathrm{ml}$ | Volumen | $V_\mathrm{M} = 30\,\mathrm{ml}$ |
| Dichte | $\rho_\mathrm{K} = 1000\,\mathrm{kg/m^3}$ | Dichte | $\rho_\mathrm{M} = 1030\,\mathrm{kg/m^3}$ |
| Spez. Wärmekapazität | $c_{p,\mathrm{K}} = 4{,}18\,\mathrm{kJ/(kg\,K)}$ | Spez. Wärmekapazität | $c_{p,\mathrm{M}} = 3{,}94\,\mathrm{kJ/(kg\,K)}$ |
| Anfangstemperatur | $\vartheta_{\mathrm{K},0} = 80\,\mathrm{°C}$ | Temperatur | $\vartheta_\mathrm{M} = 5\,\mathrm{°C}$ |
| **Umgebung** | | **Messung in Tasse 2** | |
| Temperatur | $\vartheta_\mathrm{u} = 20\,\mathrm{°C}$ | nach 10 min | $\vartheta_\mathrm{K}(10\,\mathrm{min}) = 67\,\mathrm{°C}$ |
| **Milch in Teil f** | | **Becher in Teil g** | |
| Temperatur | $\vartheta_{\mathrm{M,h}} = 60\,\mathrm{°C}$ | Masse | $m_\mathrm{B} = 300\,\mathrm{g}$ |
| | | Spez. Wärmekapazität | $c_\mathrm{B} = 0{,}85\,\mathrm{kJ/(kg\,K)}$ |

**Aufgabenstellung:**

a) Bestimmen Sie mit einer Energiebilanz die Mischtemperatur $\vartheta_{1,0}$ direkt nach dem Zugießen der Milch in Tasse 1.\
   $\vartheta_{1,0} = 70{,}47\,\mathrm{°C}$

b) Zeichnen Sie den Bilanzraum um den Inhalt von Tasse 1 in Abb. 1 ein. Vereinfachen Sie die allgemeine Energiebilanz (Foliensatz 05, Folie 8) zur globalen instationären Bilanz für den Inhalt einer Tasse und begründen Sie, welche Terme entfallen. Lösen Sie sie durch Trennung der Variablen für $T(t = 0\,\mathrm{s}) = T_0$.\
   $T(t) = T_\mathrm{u} + (T_0 - T_\mathrm{u})\cdot \exp\left(-\frac{kA}{m\,c_p}\,t\right)$

c) Bestimmen Sie $kA$ aus der Messung in Tasse 2. Welche Annahme brauchen Sie, um diesen Wert auch für Tasse 1 zu verwenden, und ist sie plausibel?\
   $kA = 0{,}3402\,\mathrm{W/K}$

d) Berechnen Sie $\vartheta_1$ und $\vartheta_2$ nach 60 Minuten (Tasse 2 direkt nach dem Zugießen). Welches $m\,c_p$ setzen Sie jeweils ein? Welche Tasse ist wärmer?\
   $34{,}05\,\mathrm{°C}$ und $30{,}19\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

e) Berechnen Sie die Wärme, die jede Tasse in 60 Minuten an die Umgebung abgibt. Zeigen Sie, dass $Q_2 - Q_1$ den Temperaturunterschied aus d) erklärt. Wo liegt der Denkfehler Ihres Mitbewohners?\
   $Q_1 = 34{,}88\,\mathrm{kJ}$, $\quad Q_2 = 38{,}57\,\mathrm{kJ}$

f) Am nächsten Tag gibt es Milchkaffee: Die Milch wird je Tasse kurz vorher auf $\vartheta_{\mathrm{M,h}}$ erwärmt und untergerührt (gleiche Masse und Stoffdaten). Welche Tasse ist nach 60 Minuten wärmer? Sagen Sie es mit kurzer Begründung voraus, prüfen Sie dann mit den Gleichungen aus d) und erklären Sie das Ergebnis.\
   $35{,}99\,\mathrm{°C}$ und $37{,}18\,\mathrm{°C}$ (Zuordnung selbst bestimmen)

g) *Vertiefung:* Die Tassen sind vorgewärmte Keramikbecher, die immer die Temperatur ihres Inhalts haben, auch beim Zugießen der Milch. Passen Sie Bilanzraum und Bilanz aus b) an, bestimmen Sie $kA$ neu und berechnen Sie $\vartheta_1$ und $\vartheta_2$ wie in d). Gilt die Aussage aus d) weiter?\
   $kA = 0{,}4440\,\mathrm{W/K}$, $\quad\vartheta_1 = 34{,}04\,\mathrm{°C}$, $\quad\vartheta_2 = 30{,}96\,\mathrm{°C}$

**Versuch zu Aufgabe 1** (im Tutorium, läuft neben der Rechnung)

Drei gleiche, vorgewärmte Becher mit je 200 ml heißem Wasser oder Kaffee und je 30 ml Milch: Becher 1 bekommt die Milch sofort, Becher 2 und 3 erst nach 40 Minuten (Milch aus der Kühltasche bzw. aus einem Glas mit etwas Abstand zu den Bechern). Nach 10 Minuten werden Becher 2 und 3 gemessen.

1. Bestimmen Sie $kA$ wie in Teil c (ohne Becher) aus dem Mittelwert der beiden Messungen und sagen Sie mit den Gleichungen aus d) die Temperaturen nach 40 Minuten voraus (Becher 3 mit Milch bei Raumtemperatur).
2. Ist der gemessene Unterschied zwischen Becher 1 und 2 größer als die Messunsicherheit? Nennen Sie zwei Gründe für Abweichungen vom Modell.

| Becher | Start $\vartheta(0)$ | $\vartheta(10\,\mathrm{min})$ | Milch $\vartheta_\mathrm{M}$ | Vorhersage $\vartheta(40\,\mathrm{min})$ | Messung $\vartheta(40\,\mathrm{min})$ |
|:----------------------------------------------|:---------------------|:-----------------------|:--------------------|:------------------------|:------------------------|
| 1: Milch sofort | | | | | |
| 2: Milch nach 40 min aus der Kühltasche | | | | | |
| 3: Milch nach 40 min aus dem Glas | | | | | |

Raumtemperatur: \_\_\_\_\_\_\_\_\_\_ °C

Mischtemperatur Becher 1: \_\_\_\_\_\_\_\_\_\_ °C

$kA$ aus Becher 2 und 3: \_\_\_\_\_\_\_\_\_\_ W/K

## Die AMOC und Europas milde Winter

**Ausgangssituation**

Ein Januarabend in Paderborn, draußen nieselt es bei 2\ °C. Ihre Kommilitonin aus Kanada erzählt von ihrer Heimatstadt Goose Bay in Labrador, die fast auf derselben Breite liegt: Dort beträgt das Januarmittel −17,6\ °C, in Paderborn +2,1\ °C. „Das macht der Golfstrom“, sagen Sie. Genauer ist es die Umwälzzirkulation im Atlantik, kurz AMOC: Warmes Wasser strömt an der Oberfläche nach Norden, gibt dort Wärme an die Luft ab, sinkt in die Tiefe und fließt kalt nach Süden zurück. Bei 26,5°\ N sind das rund 17\ Millionen Kubikmeter pro Sekunde, so viel wie etwa 80 Amazonas-Ströme, und mit dem Wasser fließen 1,2\ Petawatt Wärme nach Norden. Klimamodelle erwarten, dass die AMOC in diesem Jahrhundert schwächer wird.

![](grafik/t5_amoc.png){width=90%}

**Abb. 2:** Die Umwälzzirkulation im Atlantik (AMOC)

**Frage 4** (Vorab-Frage)

Angenommen, die AMOC bringt 20\ % weniger Wärme nach Norden. Um wie viel wird der Januar in Paderborn dadurch kälter: um weniger als 1\ K, um 1 bis 5\ K oder um mehr als 5\ K? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 2 rechnen.

**Aufgabe 2** (neu)

**Annahmen:**

- Der Atlantik nördlich von 26,5°\ N wird im Jahresmittel als stationär betrachtet.
- Hin- und Rückstrom haben die Stoffwerte von Meerwasser; die Stoffwerte sind unabhängig von der Temperatur.
- Die Wärme der AMOC geht vollständig zwischen 40° und 70°\ N an die Luft.
- Die Oberfläche in Paderborn wird im Januar als stationär behandelt; die Abstrahlung folgt dem Schichtmodell aus Tutorium 4 mit einer grauen Atmosphärenschicht.
- Ändert sich die Wärmezufuhr, reagiert nur die Abstrahlung; Winde, Schnee und Meereis bleiben unverändert.

***Gegebene Größen:***

| ***AMOC bei 26,5°\ N:*** | | ***Meerwasser:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Volumenstrom: | $\dot{V} = 17\,\mathrm{Sv}$ | Dichte: | $\rho_\mathrm{M} = 1025\,\mathrm{kg/m^3}$ |
| Wärmestrom: | $\dot{Q}_{\mathrm{AMOC}} = 1{,}2\,\mathrm{PW}$ | Spez. Wärmekapazität: | $c_{p,\mathrm{M}} = 3990\,\mathrm{J/(kg\,K)}$ |
| 1 Sverdrup: | $1\,\mathrm{Sv} = 10^{6}\,\mathrm{m^3/s}$ | Oberflächenwasser: | $\vartheta_\mathrm{w} \approx 20\,\mathrm{°C}$ |
| | | Tiefenwasser: | $\vartheta_\mathrm{k} \approx 3\,\mathrm{°C}$ |
| | | | |
| ***Vergleichsströme:*** | | ***Flächen:*** | |
| Amazonas: | $\dot{V}_\mathrm{A} = 0{,}206\,\mathrm{Sv}$ | Gürtel: | $A_\mathrm{G} = 7{,}6\cdot 10^{13}\,\mathrm{m^2}$ |
| Golfstrom (60°\ W): | $\dot{V}_\mathrm{G} \geq 150\,\mathrm{Sv}$ | Viertel: | $A_\mathrm{V} = 1{,}9\cdot 10^{13}\,\mathrm{m^2}$ |
| | | | |
| ***Januar, 51,7°\ N:*** | | ***Januarmittel:*** | |
| Sonne am Oberrand: | $\dot{q}_\mathrm{S} = 93\,\mathrm{W/m^2}$ | Paderborn: | $\vartheta_{\mathrm{PB}} = 2{,}1\,\mathrm{°C}$ |
| Albedo (Winter): | $\rho_\mathrm{p} = 0{,}4$ | Goose Bay: | $\vartheta_{\mathrm{GB}} = -17{,}6\,\mathrm{°C}$ |
| Atmosphäre: | $\varepsilon_\mathrm{A} = 0{,}78$ | | |
| | | | |
| ***Deckschicht:*** | | | |
| Tiefe im Winter: | $h = 100\,\mathrm{m}$ bis $350\,\mathrm{m}$ | | |

Die Stefan-Boltzmann-Konstante ${\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}}$ ist hier gegeben (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Zeichnen Sie in Abb. 2 den Bilanzraum „Atlantik nördlich von 26,5°\ N“ ein. Rechnen Sie den Volumenstrom der AMOC in $\mathrm{m^3/s}$ und den Massenstrom in $\mathrm{kg/s}$ um. Warum muss in der Tiefe genauso viel Wasser nach Süden fließen, wie oben nach Norden strömt? Prüfen Sie die Angabe „etwa 80 Amazonas-Ströme“.\
   $\dot{V} = 1{,}7\cdot 10^{7}\,\mathrm{m^3/s}$, $\quad\dot{m} = 1{,}74\cdot 10^{10}\,\mathrm{kg/s}$, $\quad\dot{V}/\dot{V}_\mathrm{A} = 82{,}5$

b) Berechnen Sie den Wärmekapazitätsstrom ${\dot{C} = \dot{m}\,c_{p,\mathrm{M}}}$ und die mittlere Temperaturdifferenz $\Delta T$ zwischen Hin- und Rückstrom, die $\dot{Q}_{\mathrm{AMOC}}$ erklärt. Passt sie zu $\vartheta_\mathrm{w}$ und $\vartheta_\mathrm{k}$? Der Golfstrom führt nahe 60°\ W mindestens $\dot{V}_\mathrm{G}$. Warum folgt daraus kein neunmal so großer Wärmestrom nach Norden?\
   $\dot{C} = 69{,}5\,\mathrm{TW/K}$, $\quad\Delta T = 17{,}3\,\mathrm{K}$, $\quad\dot{C}\,(\vartheta_\mathrm{w} - \vartheta_\mathrm{k}) = 1{,}18\,\mathrm{PW}$

c) Nehmen Sie an, der ganze Wärmestrom $\dot{Q}_{\mathrm{AMOC}}$ geht zwischen 40° und 70°\ N an die Luft. Welche Wärmestromdichte ergibt sich, wenn sich die Wärme auf den ganzen Breitengürtel verteilt ($A_\mathrm{G}$), und welche, wenn sie nur dem Viertel über Nordatlantik und Europa zugutekommt ($A_\mathrm{V}$, 50°\ W bis 40°\ O)?\
   $\dot{q}_\mathrm{G} = 15{,}8\,\mathrm{W/m^2}$, $\quad\dot{q}_\mathrm{V} = 63{,}2\,\mathrm{W/m^2}$

d) Wie kalt wäre Paderborn im Januar ohne jede Wärmezufuhr außer der Sonne? Stellen Sie die stationäre Strahlungsbilanz der Oberfläche auf, (1) ohne Atmosphäre und (2) mit dem Schichtmodell aus Tutorium 4, ${T_\mathrm{O} = T_\mathrm{e}\,\left(2/(2 - \varepsilon_\mathrm{A})\right)^{1/4}}$.\
   Zu (1): $\dot{q}_{\mathrm{abs}} = 55{,}8\,\mathrm{W/m^2}$, $\quad\vartheta_\mathrm{e} = -96{,}0\,\mathrm{°C}$; zu (2): $\vartheta_\mathrm{O} = -72{,}7\,\mathrm{°C}$

e) Welche Wärmestromdichte $\dot{q}_{\mathrm{zu}}$ muss im Januar zusätzlich ankommen, damit es in Paderborn $\vartheta_{\mathrm{PB}}$ warm ist? Die Abstrahlung nach dem Schichtmodell ist $\sigma\,(1 - \varepsilon_\mathrm{A}/2)\,T^4$. Welchen Anteil kann die AMOC nach c) höchstens liefern? Wie stark hängt das Ergebnis von der Albedo ab (0,3 oder 0,5 statt 0,4)?\
   Abstrahlung $198{,}5\,\mathrm{W/m^2}$, $\quad\dot{q}_{\mathrm{zu}} = 142{,}7\,\mathrm{W/m^2}$, AMOC-Anteil $11\,\%$ bis $44\,\%$\
   Mit $\rho_\mathrm{p} = 0{,}3$ bzw. $0{,}5$: $\dot{q}_{\mathrm{zu}} = 133{,}4$ bzw. $152{,}0\,\mathrm{W/m^2}$, Anteil $10$ bis $47\,\%$

f) Seager et al. (2002) schätzen für den Winter nördlich von 35°\ N im Mittel: 54\ W/m² bringt die Atmosphäre, 11\ W/m² der Wärmetransport im Ozean, und 53\ W/m² gibt der Ozean aus seinem Sommerspeicher ab. Passt das zu d) und e)? Welche Annahme aus c) ist am fragwürdigsten?\
   Summe nach Seager et al.: $118\,\mathrm{W/m^2}$

g) Linearisieren Sie die Abstrahlung wie in Tutorium 4: Ändert sich die Temperatur um $\Delta T$, ändert sich die Abstrahlung um $\alpha_\mathrm{S}\,\Delta T$ mit ${\alpha_\mathrm{S} = 4\sigma T^3\,(1 - \varepsilon_\mathrm{A}/2)}$, ausgewertet bei $\vartheta_{\mathrm{PB}}$. Im neuen Gleichgewicht gilt ${\alpha_\mathrm{S}\,\Delta T = \Delta\dot{q}_{\mathrm{AMOC}}}$, die Änderung der Wärmezufuhr durch die AMOC. (1) Wie viele Kelvin Erwärmung entsprechen der ganzen AMOC-Wärme aus c)? Kann sie den Unterschied zu Goose Bay erklären? Beachten Sie, wo Goose Bay liegt (60,4°\ W): im Gürtel, aber außerhalb des Viertels. (2) Die AMOC transportiert 20\ % weniger Wärme. Um wie viel ändert sich die Januartemperatur in Paderborn im neuen Gleichgewicht?\
   $\alpha_\mathrm{S} = 2{,}89\,\mathrm{W/(m^2\,K)}$; zu (1): $\Delta T_\mathrm{G} = 5{,}5\,\mathrm{K}$, $\quad\Delta T_\mathrm{V} = 21{,}9\,\mathrm{K}$\
   Zu (2): $\Delta\dot{q}_\mathrm{G} = -3{,}2\,\mathrm{W/m^2}$, $\quad\Delta\dot{q}_\mathrm{V} = -12{,}6\,\mathrm{W/m^2}$\
   $\Delta T_\mathrm{G} = -1{,}1\,\mathrm{K}$, $\quad\Delta T_\mathrm{V} = -4{,}4\,\mathrm{K}$

h) Wie schnell stellt sich das neue Gleichgewicht ein? Die Deckschicht des Ozeans (Tiefe $h$) wird als ideal durchmischter Speicher mit der Wärmekapazität ${C = \rho_\mathrm{M}\,c_{p,\mathrm{M}}\,h}$ je Quadratmeter behandelt: ${C\,\mathrm{d}\Delta T/\mathrm{d}t = \Delta\dot{q}_{\mathrm{AMOC}} - \alpha_\mathrm{S}\,\Delta T}$ mit $\Delta\dot{q}_{\mathrm{AMOC}}$ aus g) (negativ, weil die Zufuhr sinkt). Lösen Sie die Gleichung für ${\Delta T(t = 0) = 0}$ und bestimmen Sie die Zeitkonstante ${\tau = C/\alpha_\mathrm{S}}$ für 100\ m und 350\ m. Welcher Anteil der Abkühlung ist nach 10\ Jahren erreicht? Warum darf man der Deckschicht eine einzige Temperatur geben?\
   Für $h = 100\,\mathrm{m}$: $C = 4{,}09\cdot 10^{8}\,\mathrm{J/(m^2\,K)}$, $\quad\tau = 4{,}5\,\mathrm{Jahre}$, nach 10\ Jahren $89\,\%$\
   Für $h = 350\,\mathrm{m}$: $C = 1{,}43\cdot 10^{9}\,\mathrm{J/(m^2\,K)}$, $\quad\tau = 15{,}7\,\mathrm{Jahre}$, nach 10\ Jahren $47\,\%$

i) Erklären Sie in drei Sätzen, was eine schwächere AMOC für Europas Winter bedeuten würde und warum es trotzdem nicht einfach kälter wird, solange sich die Erde insgesamt erwärmt.

## Der Ozean als Wärmespeicher

**Ausgangssituation**

Stellen Sie sich vor, der CO₂-Gehalt der Luft verdoppelt sich. Dann hält die Atmosphäre mehr Wärmestrahlung zurück, und für die Erdoberfläche wirkt das wie eine zusätzliche Wärmezufuhr von knapp 4\ W je Quadratmeter. Trotzdem steigt die Temperatur nicht sofort, denn den größten Teil der Wärme nimmt das Meer auf: 91\ % der Energie, die das Klimasystem seit 1971 zusätzlich aufgenommen hat, steckt im Ozean. Wind und Wellen wälzen die oberste Schicht des Meeres ständig um. Diese Deckschicht ist im Mittel etwa 70\ m tief und hat überall fast dieselbe Temperatur. Sie verhält sich wie ein riesiger Kochtopf auf einer sehr schwachen Herdplatte. Wie lange dauert es, bis er warm wird?

![](grafik/t5_deckschicht.png){width=88%}

**Abb. 3:** Deckschicht des Ozeans und Boden an Land

**Frage 5** (Vorab-Frage)

Ein See und ein Acker gleich daneben bekommen im Frühling gleich viel Sonne. Welcher von beiden erwärmt sich schneller, und warum? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 3 rechnen.

**Aufgabe 3** (neu)

Dasselbe Modell steckt in den letzten Teilen von Aufgabe 2 (g und h); die beiden Aufgaben können einander ersetzen.

**Annahmen:**

- Die Deckschicht wird als ideal durchmischt angenommen.
- Ein Wärmeaustausch mit der Tiefsee wird bis Teil f vernachlässigt.
- Die zusätzliche Strahlungsflussdichte $\dot{q}_\mathrm{F}$ setzt bei ${t = 0}$ ein und bleibt danach konstant.
- Die zusätzliche Wärmeabgabe nach oben ist proportional zur Erwärmung: ${\dot{q}_{\mathrm{ab}} = \alpha_{\mathrm{eff}}\,\Delta T}$.
- Die Stoffdaten sind unabhängig von der Temperatur.

***Gegebene Größen:***

| ***Deckschicht:*** | | ***Wärmeströme:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Tiefe: | $h = 70\,\mathrm{m}$ | Zufuhr: | $\dot{q}_\mathrm{F} = 3{,}93\,\mathrm{W/m^2}$ |
| Dichte: | $\rho_\mathrm{M} = 1025\,\mathrm{kg/m^3}$ | Abgabe nach oben: | $\alpha_{\mathrm{eff}} = 1{,}3\,\mathrm{W/(m^2\,K)}$ |
| Spez. Wärmekapazität: | $c_{p,\mathrm{M}} = 3990\,\mathrm{J/(kg\,K)}$ | Abgabe an Tiefsee: | $\gamma = 0{,}7\,\mathrm{W/(m^2\,K)}$ |
| Wärmeleitfähigkeit: | $\lambda_\mathrm{M} = 0{,}6\,\mathrm{W/(m\,K)}$ | | |
| | | | |
| ***Boden an Land:*** | | ***Tutorium 4:*** | |
| Tiefe: | $h_\mathrm{B} = 2\,\mathrm{m}$ | Erde: | $T_\mathrm{e} = 254{,}6\,\mathrm{K}$ |
| Wärmekapazität: | $\rho_\mathrm{B} c_\mathrm{B} = 2{,}2\,\mathrm{MJ/(m^3\,K)}$ | | |

Die Stefan-Boltzmann-Konstante ${\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}}$ ist hier gegeben (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Zeichnen Sie in Abb. 3 den Bilanzraum ein: eine Wassersäule der Deckschicht mit $1\,\mathrm{m^2}$ Grundfläche und der Tiefe $h$. Ergänzen Sie den Pfeil für die abgegebene Wärmestromdichte.

b) Was bedeutet „ideal durchmischt“ für die Temperatur in der Deckschicht? Warum prüft man bei einem Festkörper stattdessen die Biot-Zahl?

c) Berechnen Sie die Wärmekapazität der Deckschicht je Quadratmeter, ${C = \rho_\mathrm{M}\,c_{p,\mathrm{M}}\,h}$, und vergleichen Sie mit der Bodenschicht an Land.\
   $C = 2{,}86\cdot 10^{8}\,\mathrm{J/(m^2\,K)}$, $\quad C_\mathrm{B} = 4{,}4\cdot 10^{6}\,\mathrm{J/(m^2\,K)}$, $\quad C/C_\mathrm{B} = 65$

d) Stellen Sie die instationäre Energiebilanz für die Erwärmung $\Delta T(t)$ der Deckschicht auf und benennen Sie die Terme (Speicherung, Zufuhr, Abgabe).\
   $C\,\frac{\mathrm{d}\Delta T}{\mathrm{d}t} = \dot{q}_\mathrm{F} - \alpha_{\mathrm{eff}}\,\Delta T$

e) Lösen Sie die Differentialgleichung durch Trennung der Variablen für ${\Delta T(t = 0) = 0}$. Bestimmen Sie die Zeitkonstante $\tau$, die Erwärmung nach 10\ Jahren und den Endwert $\Delta T_\infty$.\
   $\Delta T(t) = \frac{\dot{q}_\mathrm{F}}{\alpha_{\mathrm{eff}}}\left(1 - \exp\left(-\frac{t}{\tau}\right)\right)$ mit $\tau = \frac{C}{\alpha_{\mathrm{eff}}}$\
   $\tau = 6{,}98\,\mathrm{Jahre}$, $\quad\Delta T(10\,\mathrm{Jahre}) = 2{,}30\,\mathrm{K}$, $\quad\Delta T_\infty = 3{,}02\,\mathrm{K}$

f) Prüfen Sie Ihr Ergebnis: (1) Welche Einheit hat $\tau$? (2) Was ergibt sich für ${t \to 0}$ und für ${t \to \infty}$? (3) Gäbe die Erde die zusätzliche Wärme nur durch Abstrahlung ab, wäre ${\alpha_\mathrm{S} = 4\sigma T_\mathrm{e}^3}$ mit der Emissionstemperatur $T_\mathrm{e}$ der Erde (Linearisierung aus Tutorium 4). Wie ändern sich $\tau$ und $\Delta T_\infty$?\
   Zu (3): $\alpha_\mathrm{S} = 3{,}74\,\mathrm{W/(m^2\,K)}$, $\quad\tau = 2{,}42\,\mathrm{Jahre}$, $\quad\Delta T_\infty = 1{,}05\,\mathrm{K}$

g) Prüfen Sie zwei Annahmen: (1) Wie lange bräuchte die Wärme, um allein durch Wärmeleitung 70\ m tief vorzudringen (${t \approx h^2/a}$)? Was mischt die Deckschicht stattdessen? (2) Die Tiefsee nimmt als zweiter, langsamer Speicher zusätzlich $\gamma\,\Delta T$ auf. Wie ändern sich $\tau$ und $\Delta T_\infty$?\
   Zu (1): $a = 1{,}47\cdot 10^{-7}\,\mathrm{m^2/s}$, $\quad t \approx 1{,}1\cdot 10^{3}\,\mathrm{Jahre}$\
   Zu (2): $\tau = 4{,}54\,\mathrm{Jahre}$, $\quad\Delta T_\infty = 1{,}97\,\mathrm{K}$

h) Erklären Sie in zwei bis drei Sätzen mit Ihrer Zeitkonstante, warum die Temperatur einer Änderung der Strahlungsbilanz nur verzögert folgt. Warum stecken 91\ % der zusätzlichen Energie im Ozean?

## Sverdrup und der Amazonas

**Ausgangssituation**

Sie stehen in Paderborn an der Pader, die mit rund 4\ km als kürzester Fluss Deutschlands gilt. Aus über 200 Quellen fließen hier im Mittel etwa 5000\ Liter pro Sekunde. Für die großen Ströme der Erde rechnen Ozeanographen in Sverdrup: Ein Sverdrup sind eine Million Kubikmeter pro Sekunde. Der Amazonas, der wasserreichste Fluss der Erde, kommt auf rund ein Fünftel Sverdrup. Über seinem Becken zieht zudem ein „fliegender Fluss“ aus Wasserdampf, der in der Trockenzeit etwa so viel Wasser trägt wie der Amazonas selbst.

![](grafik/t5_amazonas.png){width=88%}

**Abb. 4:** Der Wasserkreislauf im Amazonasbecken

**Aufgabe 4** (neu)

**Annahmen:**

- Das Becken wird im Jahresmittel als stationär betrachtet; Speicherung im Boden und Grundwasserströme werden vernachlässigt.
- Wasser verlässt das Becken nur über den Fluss und durch Verdunstung.
- Fluss und Flussfahne haben die Stoffwerte von Süßwasser.
- Das Wasser verdunstet bei rund 30\ °C.

***Gegebene Größen:***

| ***Mittlere Abflüsse:*** | | ***Amazonas:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Pader: | $\dot{V}_\mathrm{P} = 5\,\mathrm{m^3/s}$ | Abfluss: | $\dot{V}_\mathrm{A} = 206\,000\,\mathrm{m^3/s}$ |
| Weser: | $\dot{V}_\mathrm{W} = 313\,\mathrm{m^3/s}$ | Unterlauf: | $\vartheta_\mathrm{A} = 27{,}5$ bis $28{,}5\,\mathrm{°C}$ |
| Rhein: | $\dot{V}_\mathrm{R} = 2260\,\mathrm{m^3/s}$ | Flussfahne: | $\vartheta_\mathrm{F} = 28{,}5\,\mathrm{°C}$ |
| Alle Flüsse: | $\dot{V}_{\mathrm{Fl}} = 1{,}18\,\mathrm{Sv}$ | Beckenfläche: | $A_\mathrm{B} = 6\cdot 10^{12}\,\mathrm{m^2}$ |
| AMOC: | $\dot{V}_{\mathrm{AMOC}} = 17\,\mathrm{Sv}$ | Niederschlag: | $N = 2200\,\mathrm{mm/a}$ |
| | | | |
| ***Süßwasser:*** | | ***Energieumsatz:*** | |
| Dichte: | $\rho_\mathrm{W} = 1000\,\mathrm{kg/m^3}$ | Menschheit: | $\dot{Q}_{\mathrm{M}} = 19\,\mathrm{TW}$ |
| Spez. Wärmekapazität: | $c_{p,\mathrm{W}} = 4180\,\mathrm{J/(kg\,K)}$ | | |
| Verdampfung: | $\Delta h_\mathrm{v} = 2{,}43\,\mathrm{MJ/kg}$ | | |

**Aufgabenstellung:**

a) Rechnen Sie die Abflüsse von Pader, Weser, Rhein und Amazonas in Sverdrup um und ordnen Sie alle Ströme der Tabelle der Größe nach. Wie viele Rheine ergeben einen Amazonas, wie viele Amazonas-Ströme die AMOC?\
   Pader $5\cdot 10^{-6}\,\mathrm{Sv}$, Weser $3{,}13\cdot 10^{-4}\,\mathrm{Sv}$, Rhein $2{,}26\cdot 10^{-3}\,\mathrm{Sv}$, Amazonas $0{,}206\,\mathrm{Sv}$\
   $\dot{V}_\mathrm{A}/\dot{V}_\mathrm{R} = 91$, $\quad\dot{V}_{\mathrm{AMOC}}/\dot{V}_\mathrm{A} = 82{,}5$

b) Berechnen Sie den Wärmekapazitätsstrom $\dot{C}_\mathrm{A}$ des Amazonas. Wie groß ist der Wärmestrom zwischen Fluss und Meer höchstens, und in welche Richtung fließt er? Um wie viel müsste der Fluss wärmer sein als das Meer, um den Energieumsatz der Menschheit abzugeben?\
   $\dot{C}_\mathrm{A} = 0{,}861\,\mathrm{TW/K}$, $\quad|\dot{Q}| \leq 0{,}861\,\mathrm{TW}$, $\quad\Delta T = 22{,}1\,\mathrm{K}$

c) Stellen Sie die stationäre Massenbilanz des Beckens auf (Niederschlag gleich Abfluss plus Verdunstung). Wie viel Wasser verdunstet, in Sverdrup und in Millimetern pro Jahr? Vergleichen Sie mit dem Abfluss und mit dem Messwert $1083 \pm 37\,\mathrm{mm/a}$ (Baker et al., 2021).\
   $\dot{V}_\mathrm{N} = 0{,}418\,\mathrm{Sv}$, $\quad\dot{V}_\mathrm{V} = 0{,}212\,\mathrm{Sv}$, $\quad 1117\,\mathrm{mm/a}$, Abweichung $3\,\%$

d) Welche Wärmestromdichte steckt in dieser Verdunstung? Vergleichen Sie den Wärmestrom des ganzen Beckens mit b) und mit dem Energieumsatz der Menschheit, die Wärmestromdichte mit der gemessenen Nettostrahlung des Waldes von 117 bis 153\ W/m² (da Rocha et al., 2009). Erklären Sie in zwei Sätzen, warum gerodete Flächen wärmer werden.\
   $\dot{q}_\mathrm{V} = 86\,\mathrm{W/m^2}$, $\quad\dot{Q}_\mathrm{V} = 516\,\mathrm{TW}$, Anteil an der Nettostrahlung $56$ bis $73\,\%$\
   $\dot{Q}_\mathrm{V}/|\dot{Q}| = 599$, $\quad\dot{Q}_\mathrm{V}/\dot{Q}_\mathrm{M} = 27$

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Kraftwerk am Fluss

Ein Kraftwerk gibt im Hitzesommer ${\dot{Q} = 2\,\mathrm{GW}}$ Abwärme an einen Fluss ab, der ${\dot{V} = 200\,\mathrm{m^3/s}}$ Wasser führt (${\rho = 1000\,\mathrm{kg/m^3}}$, ${c_p = 4{,}18\,\mathrm{kJ/(kg\,K)}}$). Das Kühlwasser wird dem Fluss entnommen, im Kraftwerk erwärmt und wieder eingeleitet; danach mischt es sich vollständig mit dem übrigen Flusswasser.

a) Stellen Sie die Massenbilanz und die stationäre Energiebilanz für den Flussabschnitt am Kraftwerk auf. Um wie viel erwärmt sich der Fluss?\
   $\Delta T = 2{,}39\,\mathrm{K}$

b) Vor dem Kraftwerk ist der Fluss schon ${\vartheta_{\mathrm{ein}} = 26\,\mathrm{°C}}$ warm. Wie warm ist er hinter dem Kraftwerk? Was bedeutet das für Fische und andere Lebewesen im Fluss und für den Betrieb des Kraftwerks?\
   $\vartheta_{\mathrm{aus}} = 28{,}39\,\mathrm{°C}$

**Zusatzaufgabe 2** (neu): Eisberg

Ein Tafeleisberg mit quadratischer Grundfläche von $1\,\mathrm{km}$ Kantenlänge und der Dicke ${H = 250\,\mathrm{m}}$ treibt im Meer; sein Tiefgang beträgt ${h_\mathrm{T} = 224\,\mathrm{m}}$. Das Meerwasser ist 2 bis 3\ K wärmer als die Eisoberfläche, der Wärmeübergangskoeffizient beträgt ${\alpha = 20}$ bis $50\,\mathrm{W/(m^2\,K)}$. Das Eis hat überall seine Schmelztemperatur (${\rho_\mathrm{E} = 917\,\mathrm{kg/m^3}}$, ${\Delta h_\mathrm{s} = 333{,}5\,\mathrm{kJ/kg}}$). Wärme nimmt der Eisberg nur über die Unterseite und die Seitenflächen unter Wasser auf.

a) Berechnen Sie die Masse des Eisbergs und die Wärme, die zum vollständigen Schmelzen nötig ist.\
   $m_\mathrm{E} = 2{,}29\cdot 10^{11}\,\mathrm{kg}$, $\quad Q = 7{,}65\cdot 10^{16}\,\mathrm{J}$

b) Stellen Sie die instationäre Energiebilanz für den Eisberg auf: Die zugeführte Wärme schmilzt Eis. Wie lange dauert das Schmelzen, wenn die Fläche unter Wasser gleich bleibt? Rechnen Sie mit dem kleinsten (${\alpha = 20\,\mathrm{W/(m^2\,K)}}$, 2\ K) und mit dem größten Wärmestrom (${\alpha = 50\,\mathrm{W/(m^2\,K)}}$, 3\ K).\
   $A = 1{,}90\cdot 10^{6}\,\mathrm{m^2}$, $\quad\dot{Q} = 75{,}8$ bis $284\,\mathrm{MW}$, $\quad t = 31{,}9\,\mathrm{Jahre}$ bzw. $8{,}5\,\mathrm{Jahre}$

c) Eisberge zerbrechen in Wirklichkeit viel früher. Wie ändert das die Schmelzzeit? Welche Annahme der Rechnung wirkt in die andere Richtung?

# Tutorium 6: Wärmebilanzen (stationär differentiell)

## Woher kommt die Erdwärme?

**Ausgangssituation**

Wenn Sie in einem Bergwerk nach unten fahren, merken Sie es sofort: Je tiefer Sie kommen, desto wärmer wird es. In der Kontinentalen Tiefbohrung in der Oberpfalz herrschen in 9,1\ km Tiefe rund 265\ °C. Aus dem Erdinneren strömen insgesamt etwa 47\ TW an die Oberfläche. Doch woher kommt diese Wärme? Ein großer Teil stammt aus winzigen Mengen radioaktiver Stoffe wie Uran, Thorium und Kalium, die in jedem Gestein stecken. Deren Atomkerne zerfallen nach und nach und setzen dabei Wärme frei. Die Erdkruste gleicht damit einer dicken Wand mit eingebauter Heizung: Überall entsteht ein wenig Wärme, die nach oben abgeleitet werden muss. Sie untersuchen, welches Temperaturprofil sich so in der Kruste einstellt und ob diese Wärmequelle auch die Wärme der ganzen Erde erklären kann.

![](grafik/t6_erdwaerme.png){width=95%}

**Abb. 1:** Erdkruste mit dem Element $dz$ (links) und Erde als Kugel (rechts)

**Frage 1** (Vorab-Frage)

Im Inneren der Erde wird überall ein wenig Wärme durch radioaktiven Zerfall erzeugt. Wo wäre es bei reiner Wärmeleitung am wärmsten, und wie verläuft die Temperatur $T(r)$ von der Erdmitte bis zur Oberfläche? Notieren Sie Ihre Vermutung und skizzieren Sie $T(r)$, bevor Sie Aufgabe 2 rechnen.

**Frage 2**

In einer ebenen Wand mit konstantem $\lambda$ stellt sich ein stationäres Temperaturprofil $T(x)$ ein. Welche Form hat es (1) ohne Wärmequelle, (2) mit gleichmäßiger Wärmequelle und gleich warmen Oberflächen, (3) mit gleichmäßiger Wärmesenke, (4) mit gleichmäßiger Wärmequelle und einer adiabaten Seite? Ordnen Sie zu und begründen Sie mit $d^2T/dx^2$.

- A: Gerade
- B: nach unten geöffnete Parabel mit dem Scheitel in der Mitte
- C: nach unten geöffnete Parabel mit dem Scheitel an einem Rand
- D: nach oben geöffnete Parabel

**Frage 3**

Ordnen Sie die Randbedingungen den Typen Dirichlet, von Neumann und gemischt zu. Welche Größe ist am Rand jeweils bekannt?

- Unterseite einer Eisscholle, die auf dem Meer schwimmt
- ideal gedämmte Seite einer Wand
- Hauswand, die vom Wind gekühlt wird

**Frage 4**

Ergänzen Sie die Taylor-Reihe (Abbruch nach dem ersten Glied) für den Wärmestrom an der Stelle $z + dz$: $\dot{Q}_{z+dz} = \dot{Q}_z + \ldots$ Was beschreibt der ergänzte Term anschaulich?

**Aufgabe 1** (neu)

Betrachten Sie die Erdkruste unter einem Kontinent als ebene Schicht der Dicke $s$ (Abb. 1, links). An der Oberfläche tritt die Wärmestromdichte $\dot{q}_\mathrm{O}$ aus.

**Annahmen:**

- Der Zustand ist stationär.
- Die Wärme wird nur in $z$-Richtung geleitet (eindimensional).
- Die Wärmeleitfähigkeit der Kruste ist konstant.
- Die Wärmequelle ist gleichmäßig über die Kruste verteilt.

***Gegebene Größen:***

| ***Erdkruste:*** | | ***Oberfläche:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Dicke: | $s = 30\,\mathrm{km}$ | Temperatur: | $\vartheta_\mathrm{O} = 10\,\mathrm{°C}$ |
| Wärmeleitfähigkeit: | $\lambda = 2{,}5\,\mathrm{W/(m\,K)}$ | Wärmestromdichte: | $\dot{q}_\mathrm{O} = 65\,\mathrm{mW/m^2}$ |
| Wärmequelle: | $\dot{q}_{\mathrm{KV}} = 1\,\mathrm{µW/m^3}$ | | |
| | | | |
| ***Granit (Teil h):*** | | ***Tiefbohrung (Teil f):*** | |
| Wärmequelle: | $\dot{q}_{\mathrm{KV,G}} = 2{,}5\,\mathrm{µW/m^3}$ | Tiefe: | $z_\mathrm{B} = 9{,}1\,\mathrm{km}$ |
| | | Temperatur: | $\vartheta_\mathrm{B} = 265\,\mathrm{°C}$ |

**Aufgabenstellung:**

a) Begründen Sie zwei der Annahmen. Welche Ableitung ist hier null, $dT/dt$ oder $dT/dz$? Erklären Sie, was jede der beiden Ableitungen beschreibt.

b) Stellen Sie für das Element in Abb. 1 die stationäre Energiebilanz auf. Leiten Sie mit der Taylor-Reihe und dem Fourier'schen Gesetz die Differentialgleichung für $T(z)$ her.\
   $\dfrac{d^2T}{dz^2} = -\dfrac{\dot{q}_{\mathrm{KV}}}{\lambda}$

c) Formulieren Sie die beiden Randbedingungen an der Oberfläche und ordnen Sie sie ein (Dirichlet, von Neumann). Achten Sie auf das Vorzeichen, denn $z$ zeigt nach unten. Welches Vorzeichen hat $\dot{Q}_z$ in Abb. 1?\
   $T(z = 0) = T_\mathrm{O}$, $\quad\left.\dfrac{dT}{dz}\right|_{z=0} = \dfrac{\dot{q}_\mathrm{O}}{\lambda}$

d) Integrieren Sie die Differentialgleichung zweimal und bestimmen Sie die Integrationskonstanten.\
   $T(z) = T_\mathrm{O} + \dfrac{\dot{q}_\mathrm{O}}{\lambda}\,z - \dfrac{\dot{q}_{\mathrm{KV}}}{2\lambda}\,z^2$

e) Berechnen Sie die Temperaturen in 10, 20 und 30\ km Tiefe, einmal mit Wärmequelle und einmal ohne ($\dot{q}_{\mathrm{KV}} = 0$, gleiches $\dot{q}_\mathrm{O}$). Skizzieren Sie beide Profile. Warum ist es mit Quelle in der Tiefe kühler, obwohl dort zusätzlich Wärme entsteht?\
   Mit Quelle: $\vartheta(10\,\mathrm{km}) = 250\,\mathrm{°C}$, $\quad\vartheta(20\,\mathrm{km}) = 450\,\mathrm{°C}$, $\quad\vartheta(30\,\mathrm{km}) = 610\,\mathrm{°C}$\
   Ohne Quelle: $\vartheta(10\,\mathrm{km}) = 270\,\mathrm{°C}$, $\quad\vartheta(20\,\mathrm{km}) = 530\,\mathrm{°C}$, $\quad\vartheta(30\,\mathrm{km}) = 790\,\mathrm{°C}$

f) Welche Temperatur ergibt Ihr Profil in der Tiefe $z_\mathrm{B}$? Vergleichen Sie mit $\vartheta_\mathrm{B}$ (GFZ, 2024) und nennen Sie mögliche Gründe für den Unterschied.\
   $\vartheta(z_\mathrm{B}) = 230\,\mathrm{°C}$

g) Bestimmen Sie die Wärmestromdichte $\dot{q}_\mathrm{M}$, die aus dem Erdmantel in die Kruste eintritt, (1) mit dem Profil und (2) mit einer globalen Energiebilanz um die ganze Kruste. Welche Frage kann nur die differentielle Bilanz beantworten?\
   $\dot{q}_\mathrm{M} = 35\,\mathrm{mW/m^2}$

h) Granit erzeugt mehr Wärme ($\dot{q}_{\mathrm{KV,G}}$). Nehmen Sie diesen Wert für die ganze Kruste an. In welcher Tiefe hat das Profil sein Maximum, und welche Wärmestromdichte ergibt sich an der Krustenbasis? Warum kann das nicht stimmen, und welche Annahme ist falsch?\
   $z_{\mathrm{max}} = 26\,\mathrm{km}$, $\quad\dot{q}_\mathrm{M} = -10\,\mathrm{mW/m^2}$

**Aufgabe 2** (neu)

Kann die Wärme aus dem radioaktiven Zerfall auch den Wärmestrom der ganzen Erde erklären? Betrachten Sie die Erde als Kugel, in der die gesamte Wärme gleichmäßig verteilt entsteht (Abb. 1, rechts).

**Annahmen:**

- Die Erde wird als homogene Kugel mit konstanter Wärmeleitfähigkeit betrachtet.
- Der gesamte Wärmestrom $\dot{Q}$ wird gleichmäßig im Erdvolumen erzeugt.
- Der Zustand ist stationär, und die Wärme wird nur durch Wärmeleitung in radialer Richtung transportiert.

***Gegebene Größen:***

| ***Erde:*** | | ***Vergleichswerte:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Radius: | $R = 6371\,\mathrm{km}$ | Innerer Kern: | $\vartheta_\mathrm{K} = 6000\,\mathrm{°C}$ |
| Wärmestrom: | $\dot{Q} = 47\,\mathrm{TW}$ | Sonne (absorbiert): | $\dot{q}_\mathrm{S} = 238\,\mathrm{W/m^2}$ |
| Wärmeleitfähigkeit: | $\lambda = 3$ bis $4\,\mathrm{W/(m\,K)}$ | | |

**Aufgabenstellung:**

a) Zeichnen Sie in Abb. 1 eine dünne Kugelschale zwischen $r$ und $r + dr$ ein. Stellen Sie die stationäre Energiebilanz für die Schale auf und leiten Sie die Differentialgleichung für $T(r)$ her.\
   $\dfrac{d}{dr}\left(r^2\,\dfrac{dT}{dr}\right) = -\dfrac{\dot{q}_{\mathrm{KV}}}{\lambda}\,r^2$

b) Integrieren Sie zweimal. Welche Bedingung gilt in der Erdmitte, welche an der Oberfläche? Vergleichen Sie das Profil mit Ihrer Vermutung zu Frage 1.\
   $T(r) = T_\mathrm{O} + \dfrac{\dot{q}_{\mathrm{KV}}}{6\lambda}\,(R^2 - r^2)$

c) Berechnen Sie die Wärmequelle $\dot{q}_{\mathrm{KV}}$ der Erde und den Temperaturunterschied $\Delta T$ zwischen Erdmitte und Oberfläche für $\lambda = 3$ und $4\,\mathrm{W/(m\,K)}$.\
   $\dot{q}_{\mathrm{KV}} = 4{,}34\cdot 10^{-8}\,\mathrm{W/m^3}$, $\quad\Delta T = 97\,800\,\mathrm{K}$ bzw. $73\,400\,\mathrm{K}$

d) Prüfen Sie das Profil mit einer globalen Energiebilanz: Welche Wärmestromdichte $\dot{q}_\mathrm{O}$ tritt an der Oberfläche aus? Vergleichen Sie mit der Erdkruste aus Aufgabe 1.\
   $\dot{q}_\mathrm{O} = 92{,}1\,\mathrm{mW/m^2}$

e) Vergleichen Sie Ihr Ergebnis aus c) mit der Temperatur $\vartheta_\mathrm{K}$ am inneren Kern (Anzellini et al., 2013). Welche Annahmen versagen, und wie wird die Wärme im Erdmantel tatsächlich transportiert?

f) Erklären Sie in zwei Sätzen, warum die Erdwärme die Erwärmung der Meere nicht erklären kann. Vergleichen Sie dazu $\dot{q}_\mathrm{O}$ aus d) mit $\dot{q}_\mathrm{S}$.\
   $\dot{q}_\mathrm{S}/\dot{q}_\mathrm{O} \approx 2600$

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Wie warm wäre die Erde ohne Sonne?

Ohne Sonne müsste die Erdoberfläche die Wärme aus dem Erdinneren allein abstrahlen, als schwarzer Körper ($\varepsilon = 1$, $\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}$) und ohne Atmosphäre.

a) Berechnen Sie die Oberflächentemperatur, bei der die Erde $\dot{q}_\mathrm{O}$ aus Aufgabe 2 abstrahlt.\
   $T = 35{,}7\,\mathrm{K}$

b) Ältere Auswertungen ergeben nur $87\,\mathrm{mW/m^2}$. Warum ändert sich die Temperatur so wenig?\
   $T = 35{,}2\,\mathrm{K}$

# Tutorium 7: Wärmebilanzen (instationär differentiell)

## Das Gedächtnis des Bodens

**Ausgangssituation**

In einem alten Gewölbekeller in Paderborn ist es im Sommer angenehm kühl, und im Winter frieren die eingelagerten Kartoffeln nicht ein, auch wenn draußen strenger Frost herrscht. Der Boden reagiert offenbar nur träge auf das Wetter an der Oberfläche. Der Deutsche Wetterdienst misst in Bad Lippspringe stündlich die Bodentemperatur in mehreren Tiefen bis 50\ cm, und in etwa zehn Metern Tiefe schwankt die Temperatur übers Jahr kaum noch. Weiter im Norden taut der Boden über dem Permafrost jeden Sommer nur oben auf. Temperaturen in Bohrlöchern in Alaska verraten außerdem, dass sich die Oberfläche dort innerhalb von Jahrzehnten bis zu einem Jahrhundert um 2 bis 4\ K erwärmt hat. Sie untersuchen, wie tief Tages- und Jahresgang in den Boden eindringen, wie weit der Boden über Permafrost auftaut und wie man aus Bohrlöchern die Klimageschichte abliest.

![](grafik/t7_boden.png){width=92%}

**Abb. 1:** Bodensäule mit der Temperatur an der Oberfläche und in den Tiefen $z_1$ und $z_2$

**Frage 1** (Vorab-Frage)

In 3\ m Tiefe ist der Boden nicht im Juli am wärmsten, sondern im Herbst. Warum? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 1 rechnen.

**Frage 2**

Die eindimensionale Wärmeleitungsgleichung mit Wärmequelle lautet
$$\rho\,c\,\frac{\partial T}{\partial t} = \lambda\,\frac{\partial^2 T}{\partial z^2} + \dot{q}_{\mathrm{KV}}.$$
Welche Terme fallen in den folgenden Fällen weg? Welche Form hat das Temperaturprofil in den beiden stationären Fällen?

- Eisschild in Tutorium 1 (stationär, ohne Wärmequelle)
- Erdkruste in Tutorium 6 (stationär, mit Wärmequelle)
- Boden in Aufgabe 1 (instationär, ohne Wärmequelle)

**Frage 3**

Welcher Stoff gleicht Temperaturunterschiede am schnellsten aus? Ordnen Sie die Stoffe zuerst ohne Rechnung und dann nach der Temperaturleitfähigkeit $a = \lambda/(\rho\,c)$; für Granit und feuchten Ton ist $a$ gemessen. Vergleichen Sie mit der Reihenfolge nach $\lambda$. Welcher Stoff fällt auf, und warum?

- Kupfer: $\lambda = 394\,\mathrm{W/(m\,K)}$, $\rho = 8940\,\mathrm{kg/m^3}$, $c = 386\,\mathrm{J/(kg\,K)}$
- Granit: $\lambda = 2{,}3$ bis $3{,}7\,\mathrm{W/(m\,K)}$, $a = 1{,}0$ bis $1{,}5\cdot 10^{-6}\,\mathrm{m^2/s}$
- feuchter Ton: $\lambda = 1{,}4$ bis $1{,}9\,\mathrm{W/(m\,K)}$, $a = 4{,}9$ bis $7{,}1\cdot 10^{-7}\,\mathrm{m^2/s}$
- Wasser (20\ °C): $\lambda = 0{,}598\,\mathrm{W/(m\,K)}$, $\rho = 998\,\mathrm{kg/m^3}$, $c = 4184\,\mathrm{J/(kg\,K)}$
- Luft (20\ °C): $\lambda = 0{,}0259\,\mathrm{W/(m\,K)}$, $\rho = 1{,}20\,\mathrm{kg/m^3}$, $c = 1006\,\mathrm{J/(kg\,K)}$

**Aufgabe 1** (neu)

Betrachten Sie den Boden als halbunendlichen Körper, dessen Oberflächentemperatur periodisch schwankt (Abb. 1).

**Annahmen:**

- Der Boden wird als halbunendlicher Körper mit konstanten Stoffdaten betrachtet.
- Die Wärme wird nur in $z$-Richtung geleitet. Wärmequellen gibt es nicht.
- Die Oberflächentemperatur schwankt sinusförmig um ihren Mittelwert; Tages- und Jahresgang werden getrennt betrachtet.
- Gefrieren, Tauen und Feuchtetransport im Boden werden vernachlässigt.
- Der Wärmestrom aus dem Erdinneren wird vernachlässigt.

***Gegebene Größen:***

| ***Feuchter Boden:*** | | ***Oberfläche:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Temperatur­leitfähigkeit: | $a = 5\cdot 10^{-7}\,\mathrm{m^2/s}$ | Amplitude Jahresgang: | $\Delta T_0 = 10\,\mathrm{K}$ |
| | | | |
| ***Gestein:*** | | ***Permafrost:*** | |
| Temperatur­leitfähigkeit: | $a_\mathrm{G} = 1\cdot 10^{-6}\,\mathrm{m^2/s}$ | Jahresmittel: | $\vartheta_{\mathrm{m,P}} = -8\,\mathrm{°C}$ |
| | | Amplitude: | $\Delta T_{0,\mathrm{P}} = 15\,\mathrm{K}$ |
| | | Erwärmung: | $\Delta\vartheta_\mathrm{P} = 3\,\mathrm{K}$ |

Schwankt die Oberflächentemperatur periodisch, $T(0,t) = T_\mathrm{m} + \Delta T_0\cos(\omega t)$ mit $\omega = 2\pi/t_\mathrm{P}$ und der Periodendauer $t_\mathrm{P}$ (Jahr: $t_\mathrm{J} = 365{,}25\,\mathrm{Tage}$, Tag: $t_\mathrm{T} = 24\,\mathrm{h}$), stellt sich nach einigen Perioden im Boden die Temperaturwelle
$$T(z,t) = T_\mathrm{m} + \Delta T_0\,e^{-z/d}\cos\left(\omega t - \frac{z}{d}\right)$$
mit der Dämpfungstiefe $d$ ein. Die Lösung ist gegeben (nicht in der Formelsammlung). Wie tief eine plötzliche Temperaturänderung an der Oberfläche nach der Zeit $t$ etwa eingedrungen ist, gibt die Eindringtiefe $\delta \approx \sqrt{a\,t}$ an (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Stellen Sie für eine dünne Bodenschicht der Dicke $dz$ die instationäre Energiebilanz auf und leiten Sie die Wärmeleitungsgleichung her. Deuten Sie jeden Term in Worten. Was bedeutet $\partial T/\partial t > 0$ an einer Stelle, was $\partial^2 T/\partial z^2 > 0$?\
   $\rho\,c\,\dfrac{\partial T}{\partial t} = \lambda\,\dfrac{\partial^2 T}{\partial z^2}$ bzw. $\dfrac{\partial T}{\partial t} = a\,\dfrac{\partial^2 T}{\partial z^2}$

b) Welche Randbedingungen gelten an der Oberfläche und in großer Tiefe? Ordnen Sie sie ein (Dirichlet, von Neumann, gemischt). Warum braucht die eingeschwungene Temperaturwelle keine Anfangsbedingung?

c) Leiten Sie die gegebene Lösung einmal nach $t$ und zweimal nach $z$ ab und setzen Sie sie in die Wärmeleitungsgleichung ein. Für welche Dämpfungstiefe $d$ ist die Gleichung erfüllt?\
   $d = \sqrt{2a/\omega}$

d) Berechnen Sie $\omega$ und $d$ für den Tagesgang und für den Jahresgang.\
   Tag: $\omega_\mathrm{T} = 7{,}27\cdot 10^{-5}\,\mathrm{1/s}$, $\quad d_\mathrm{T} = 0{,}117\,\mathrm{m}$\
   Jahr: $\omega_\mathrm{J} = 1{,}99\cdot 10^{-7}\,\mathrm{1/s}$, $\quad d_\mathrm{J} = 2{,}24\,\mathrm{m}$

e) Welcher Anteil der Amplitude des Jahresgangs kommt in 1, 5 und 10\ m Tiefe an, welcher Anteil des Tagesgangs in 0,5\ m Tiefe? Wie groß ist die Amplitude des Jahresgangs in 10\ m Tiefe? Bis in welche Tiefe erwarten Sie in den Messreihen des Deutschen Wetterdienstes einen deutlichen Tagesgang?\
   Jahresgang: $64\,\%$, $\quad 11\,\%$, $\quad 1{,}2\,\%$, $\quad\Delta T(10\,\mathrm{m}) = 0{,}12\,\mathrm{K}$\
   Tagesgang: $1{,}4\,\%$

f) Um wie viele Tage ist das Maximum des Jahresgangs in 2, 3 und 5\ m Tiefe gegenüber der Oberfläche verzögert? Beantworten Sie damit Frage 1.\
   $\Delta t = 52\,\mathrm{Tage}$, $\quad 78\,\mathrm{Tage}$, $\quad 130\,\mathrm{Tage}$

g) Eine Kälteperiode dauert $t_\mathrm{K} = 14\,\mathrm{Tage}$. Schätzen Sie ab, wie tief der Frost in dieser Zeit in den Boden eindringt. Wie tief sollte ein Fundament mindestens gegründet sein?\
   $\delta = \sqrt{a\,t_\mathrm{K}} = 0{,}78\,\mathrm{m}$

h) Über dem Permafrost taut der Boden im Sommer oben auf. Bestimmen Sie mit der Lösung für den Jahresgang die Tiefe $z_0$, bis zu der die höchste Temperatur des Jahres über 0\ °C steigt, für $\vartheta_{\mathrm{m,P}}$ und nach einer Erwärmung um $\Delta\vartheta_\mathrm{P}$ (gleicher Boden). Warum ist das Ergebnis eine obere Abschätzung, und welche Annahme ist dafür verantwortlich?\
   $z_0 = 1{,}41\,\mathrm{m}$ (bei $-8\,\mathrm{°C}$), $\quad z_0 = 2{,}46\,\mathrm{m}$ (bei $-5\,\mathrm{°C}$)

i) Die Oberfläche über dem Permafrost hat sich vor der Zeit $t_\mathrm{E} = 100\,\mathrm{Jahre}$ um einige Kelvin erwärmt. Schätzen Sie ab, bis in welche Tiefe sich diese Erwärmung im Gestein bis heute ausgebreitet hat. Skizzieren Sie das Temperaturprofil im Bohrloch vor der Erwärmung und heute; in den oberen 100\ m ist das Profil aus Tutorium 6 nahezu linear. Wie lässt sich aus solchen Profilen die Klimageschichte ablesen?\
   $\delta = \sqrt{a_\mathrm{G}\,t_\mathrm{E}} = 56\,\mathrm{m}$

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Lord Kelvin und das Alter der Erde

Lord Kelvin schätzte 1862 das Alter der Erde mit der Wärmeleitung ab. Er nahm an, die Erde sei anfangs überall gleich heiß gewesen ($\vartheta_\mathrm{A} = 3870\,\mathrm{°C}$, das sind 7000\ °F) und kühle seitdem wie ein halbunendlicher Körper ohne Wärmequellen ab, während ihre Oberfläche auf $\vartheta_\mathrm{O} = 0\,\mathrm{°C}$ bleibt. Für den Temperaturgradienten an der Oberfläche gilt dann
$$\left.\frac{\partial T}{\partial z}\right|_{z=0} = \frac{T_\mathrm{A} - T_\mathrm{O}}{\sqrt{\pi\,a\,t}}.$$
Die Lösung ist gegeben (nicht in der Formelsammlung). In Bergwerken nahm die Temperatur um $36{,}5\,\mathrm{K/km}$ zu, und für Gestein setzte Kelvin $a = 1{,}18\cdot 10^{-6}\,\mathrm{m^2/s}$ an.

a) Berechnen Sie das Alter der Erde nach Kelvin.\
   $t = 9{,}6\cdot 10^{7}\,\mathrm{Jahre}$

b) Prüfen Sie die Annahme „halbunendlicher Körper“: Wie tief ist die Abkühlung in dieser Zeit etwa eingedrungen? Vergleichen Sie mit dem Erdradius $R = 6371\,\mathrm{km}$.\
   $\delta = \sqrt{a\,t} = 59{,}8\,\mathrm{km}$

c) Heute kennt man ein Alter von rund 4,5 Milliarden Jahren. Welche Annahmen Kelvins waren falsch? Denken Sie an Tutorium 6.

# Tutorium 8: Wärmeübertrager und Verdampfer

## Wärme aus dem Boden: Sole-Wasser-Wärmepumpe

**Ausgangssituation**

Ihre Eltern wollen die alte Gasheizung ihres Hauses in Paderborn ersetzen. Im Garten wird dafür eine 100\ m tiefe Erdwärmesonde gebohrt, denn dort unten ist der Boden das ganze Jahr über etwa 11\ °C warm. In der Sonde fließt Sole, ein Gemisch aus Wasser und Frostschutzmittel. Sie nimmt Wärme aus dem Gestein auf und gibt sie im Verdampfer der Wärmepumpe an ein Kältemittel ab, das dabei schon bei −6\ °C siedet. Ein Verdichter bringt den Dampf auf ein höheres Temperaturniveau, und im Kondensator heizt das Kältemittel das Wasser der Fußbodenheizung. Der Installateur verspricht, dass eine Sonde in normalem Festgestein rund 60\ W je Meter liefert. In einer Feldstudie in älteren Häusern machten solche Anlagen im Jahresmittel aus 1\ kWh Strom 4,3\ kWh Wärme. Sie rechnen nach, ob das zusammenpasst.

![](grafik/t8_waermepumpe.png){width=92%}

**Abb. 1:** Sole-Wasser-Wärmepumpe mit Erdwärmesonde

**Frage 1** (Vorab-Frage)

Im Verdampfer siedet das Kältemittel bei konstanter Temperatur. Spielt es eine Rolle, ob die Sole im Gleichstrom oder im Gegenstrom zum Kältemittel fließt? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 1 rechnen.

**Frage 2**

Skizzieren Sie qualitativ die Temperaturverläufe beider Fluide über der Übertragungsfläche $A$ für die folgenden vier Fälle. Woran erkennen Sie einen Phasenwechsel?

- Gleichstrom ohne Phasenwechsel
- Gegenstrom ohne Phasenwechsel
- Kondensation des warmen Fluids
- Verdampfung des kalten Fluids

**Aufgabe 1** (neu)

Sie rechnen die Anlage für einen kalten Wintertag mit voller Heizleistung nach.

**Annahmen:**

- Die Anlage wird als stationär angenommen; Wärmeverluste der Leitungen werden vernachlässigt.
- Der Boden um die Sonde hat überall und jederzeit die Temperatur $\vartheta_{\mathrm{B}}$.
- Das Kältemittel verdampft bei der konstanten Temperatur $\vartheta_{\mathrm{V}}$ und kondensiert bei der konstanten Temperatur $\vartheta_{\mathrm{K}}$.
- Die Stoffdaten der Sole sind unabhängig von der Temperatur.
- Die Sole tauscht in der Sonde nur mit dem Boden Wärme aus. Der Wärmedurchgangskoeffizient ist in Verdampfer und Sonde jeweils über die ganze Fläche konstant.

***Gegebene Größen:***

| ***Wärmepumpe:*** | | ***Sole:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Heizleistung: | $\dot{Q}_{\mathrm{H}} = 8\,\mathrm{kW}$ | Eintritt Sonde: | $\vartheta_{\mathrm{S,ein}} = -1\,\mathrm{°C}$ |
| Leistungszahl: | $COP = 4$ | Austritt Sonde: | $\vartheta_{\mathrm{S,aus}} = 2\,\mathrm{°C}$ |
| Jahresarbeitszahl: | $JAZ = 4{,}3$ | Spez. Wärmekapazität: | $c_{p,\mathrm{S}} = 3{,}8\,\mathrm{kJ/(kg\,K)}$ |
| Verdampfung bei: | $\vartheta_{\mathrm{V}} = -6\,\mathrm{°C}$ | Dichte: | $\rho_{\mathrm{S}} = 1040\,\mathrm{kg/m^3}$ |
| Kondensation bei: | $\vartheta_{\mathrm{K}} = 40\,\mathrm{°C}$ | Kin. Viskosität: | $\nu_{\mathrm{S}} = 4\cdot 10^{-6}\,\mathrm{m^2/s}$ |
| | | | |
| ***Erdwärmesonde:*** | | ***Verdampfer:*** | |
| Länge: | $L = 100\,\mathrm{m}$ | Wärmedurchgangs­koeffizient: | $k_1 = 1000\,\mathrm{W/(m^2\,K)}$ |
| Innendurchmesser: | $d_{\mathrm{i}} = 26\,\mathrm{mm}$ | oder: | $k_2 = 2000\,\mathrm{W/(m^2\,K)}$ |
| Bodentemperatur: | $\vartheta_{\mathrm{B}} = 11\,\mathrm{°C}$ | | |
| | | | |
| ***Erdinneres:*** | | ***CO~2~-Emissionen:*** | |
| Wärmestromdichte: | $\dot{q}_{\mathrm{E}} = 65\,\mathrm{mW/m^2}$ | je kWh Strom (2025): | $e_{\mathrm{el}} = 344\,\mathrm{g/kWh}$ |
| | | je kWh Erdgas: | $e_{\mathrm{Erdgas}} = 202\,\mathrm{g/kWh}$ |
| | | Gasheizung: | $\eta_{\mathrm{G}} = 0{,}95$ |

Die CO~2~-Emissionen gelten ohne Vorketten, beim Strom für den Strommix des Jahres 2025. Die Carnot-Leistungszahl einer Wärmepumpe, $COP_{\mathrm{C}} = T_{\mathrm{K}}/(T_{\mathrm{K}} - T_{\mathrm{V}})$, ist hier gegeben (nicht in der Formelsammlung). $\Delta T_{\mathrm{ln}}$ und das $\varepsilon$-NTU-Konzept stehen in der Vorlesung (Foliensatz 06), nicht in der Formelsammlung.

**Aufgabenstellung:**

a) Welche Apparate in Abb. 1 sind Wärmeübertrager, und in welchen wechselt das Kältemittel die Phase? Begründen Sie die Annahmen zur Bodentemperatur und zum Kältemittel. Welche der Annahmen ist am fragwürdigsten?

b) Zeichnen Sie in Abb. 1 einen Bilanzraum um die Wärmepumpe ein und tragen Sie die Wärmeströme $\dot{Q}_{\mathrm{V}}$ (von der Sole an das Kältemittel) und $\dot{Q}_{\mathrm{H}}$ (an den Heizkreis) sowie die elektrische Leistung $P_{\mathrm{el}}$ des Verdichters ein. Bestimmen Sie $\dot{Q}_{\mathrm{V}}$ und $P_{\mathrm{el}}$ mit der Energiebilanz und der Leistungszahl. Wie groß ist der Massenstrom der Sole?\
   $\dot{Q}_{\mathrm{V}} = 6{,}00\,\mathrm{kW}$, $\quad P_{\mathrm{el}} = 2{,}00\,\mathrm{kW}$, $\quad\dot{m}_{\mathrm{S}} = 0{,}526\,\mathrm{kg/s}$

c) In der Sonde fließt die Sole entweder (1) durch einen einzigen Rohrkreis (Einfach-U-Sonde) oder (2) auf zwei parallele Rohrkreise aufgeteilt (Doppel-U-Sonde). Berechnen Sie jeweils die mittlere Geschwindigkeit $w$ und die Reynolds-Zahl im Rohr. In welchem Strömungsbereich liegen beide Fälle?\
   Zu (1): $w = 0{,}95\,\mathrm{m/s}$, $\quad Re = 6200$; zu (2): $w = 0{,}48\,\mathrm{m/s}$, $\quad Re = 3100$

d) Welcher der Temperaturverläufe aus Frage 2 liegt im Verdampfer vor? Berechnen Sie die mittlere logarithmische Temperaturdifferenz $\Delta T_{\mathrm{ln}}$ und das Produkt $(kA)_{\mathrm{V}}$ des Verdampfers. Wie groß muss die Übertragungsfläche $A_{\mathrm{V}}$ für $k_1$ und für $k_2$ sein?\
   $\Delta T_{\mathrm{ln}} = 6{,}38\,\mathrm{K}$, $\quad (kA)_{\mathrm{V}} = 940\,\mathrm{W/K}$, $\quad A_{\mathrm{V}} = 0{,}94\,\mathrm{m^2}$ bzw. $0{,}47\,\mathrm{m^2}$

e) Bestimmen Sie $(kA)_{\mathrm{V}}$ ein zweites Mal mit dem $\varepsilon$-NTU-Konzept. Welches Verhältnis der Wärmekapazitätsströme $C^*$ liegt vor? Berechnen Sie die Effektivität $\varepsilon_{\mathrm{V}}$ und $NTU_{\mathrm{V}}$. Erhalten Sie dasselbe $(kA)_{\mathrm{V}}$ wie in d)? Prüfen Sie damit Ihre Vermutung zu Frage 1.\
   $C^* = 0$, $\quad\varepsilon_{\mathrm{V}} = 0{,}375$, $\quad NTU_{\mathrm{V}} = 0{,}470$, $\quad (kA)_{\mathrm{V}} = 940\,\mathrm{W/K}$

f) Auch die Erdwärmesonde ist ein Wärmeübertrager: Die Sole nimmt Wärme vom Boden mit der konstanten Temperatur $\vartheta_{\mathrm{B}}$ auf. Bestimmen Sie $\varepsilon_{\mathrm{Sonde}}$, $NTU_{\mathrm{Sonde}}$ und $(kA)_{\mathrm{Sonde}}$. Welche Temperatur hat die Sole am tiefsten Punkt der Sonde, also nach der Hälfte ihres Weges, und welchen Anteil von $\dot{Q}_{\mathrm{V}}$ hat sie dort schon aufgenommen?\
   $\varepsilon_{\mathrm{Sonde}} = 0{,}250$, $\quad NTU_{\mathrm{Sonde}} = 0{,}288$, $\quad (kA)_{\mathrm{Sonde}} = 575\,\mathrm{W/K}$,\
   $\vartheta_{\mathrm{S,unten}} = 0{,}61\,\mathrm{°C}$, $\quad\dot{Q}_{\mathrm{unten}}/\dot{Q}_{\mathrm{V}} = 53{,}6\,\%$

g) Prüfen Sie Ihre Ergebnisse: (1) Wie viel Wärme entzieht die Sonde dem Boden je Meter? Vergleichen Sie mit dem Richtwert von 60\ W/m für normales Festgestein bei 1800 Betriebsstunden im Jahr (VDI 4640 Blatt 2, 2001). (2) Berechnen Sie die Carnot-Leistungszahl einer Wärmepumpe zwischen Verdampfungs- und Kondensationstemperatur. Welchen Anteil davon erreicht die reale Anlage?\
   Zu (1): $\dot{Q}_{\mathrm{V}}/L = 60\,\mathrm{W/m}$; zu (2): $COP_{\mathrm{C}} = 6{,}81$, $\quad COP/COP_{\mathrm{C}} = 59\,\%$

h) Ordnen Sie die Anlage ein. (1) Über welche Fläche müsste man den Wärmestrom aus dem Erdinneren sammeln, um $\dot{Q}_{\mathrm{V}}$ zu decken? Woher bekommt die Sonde ihre Wärme tatsächlich? (2) Berechnen Sie die CO~2~-Emissionen je kWh Wärme für die Wärmepumpe, einmal mit $COP$ und einmal mit $JAZ$, und für die Gasheizung. Nennen Sie zwei Grenzen dieses Vergleichs.\
   Zu (1): $A = 9{,}23\,\mathrm{ha}$;\
   Zu (2): $e_{\mathrm{WP}} = 86\,\mathrm{g/kWh}$ (mit $JAZ$: $80\,\mathrm{g/kWh}$), $\quad e_{\mathrm{Gas}} = 213\,\mathrm{g/kWh}$

## Wer bringt die Wärme zum Pol, Luft oder Wasser?

**Ausgangssituation**

Die Tropen nehmen mehr Sonnenstrahlung auf, als sie abstrahlen, die Polargebiete weniger. Den Ausgleich schaffen zwei Förderbänder: die Atmosphäre und der Ozean. Wasser speichert viel mehr Wärme als Luft; oft heißt es sogar, schon eine dünne Schicht an der Oberfläche des Ozeans speichere mehr Wärme als die ganze Atmosphäre. Dafür ist die Luft schnell unterwegs: Der Passat weht mit 5 bis 6\ m/s, der Jetstream mit rund 50\ m/s. Welches Förderband trägt mehr Wärme nach Norden?

![](grafik/t8_pol.png){width=92%}

**Abb. 2:** Wärmetransport vom Äquator zum Nordpol

**Frage 3** (Vorab-Frage)

Wie dick müsste eine Wasserschicht auf dem ganzen Ozean sein, um so viel Wärme zu speichern wie die ganze Atmosphäre: etwa 3\ cm, 3\ m oder 300\ m? Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 2 rechnen.

**Aufgabe 2** (neu)

Sie vergleichen Luft und Wasser als Wärmeträger mit denselben Werkzeugen wie in Aufgabe 1: Massenstrom, Wärmekapazitätsstrom und Phasenwechsel.

**Annahmen:**

- Alle Ströme werden als stationär angenommen. Über den Breitenkreis fließt genauso viel Luft nach Norden wie zurück.
- Die Luft, die nach Norden strömt, ist um $\Delta T$ wärmer als die Luft, die zurückströmt.
- Bis Teil b wird nur fühlbare Wärme transportiert; ab Teil c enthält die warme Luft zusätzlich mehr Wasserdampf.
- Lageenergie und kinetische Energie der Luft werden vernachlässigt.
- Die Stoffdaten sind unabhängig von der Temperatur.

***Gegebene Größen:***

| ***Meerwasser:*** | | ***Luft am Boden:*** | |
|:---------------------|:-----------------------------|:---------------------|:-----------------------------|
| Dichte: | $\rho_{\mathrm{W}} = 1025\,\mathrm{kg/m^3}$ | Dichte: | $\rho_{\mathrm{L}} = 1{,}2\,\mathrm{kg/m^3}$ |
| Spez. Wärmekapazität: | $c_{p,\mathrm{W}} = 3990\,\mathrm{J/(kg\,K)}$ | Spez. Wärmekapazität: | $c_{p,\mathrm{L}} = 1005\,\mathrm{J/(kg\,K)}$ |
| Ozeananteil: | $71\,\%$ der Erdoberfläche | Luftdruck: | $p_0 = 101\,325\,\mathrm{Pa}$ |
| AMOC bei 26,5°\ N: | $\dot{V}_{\mathrm{AMOC}} = 17\,\mathrm{Sv}$ | Erdbeschleunigung: | $g = 9{,}81\,\mathrm{m/s^2}$ |
| Wärmestrom: | $\dot{Q}_{\mathrm{AMOC}} = 1{,}2\,\mathrm{PW}$ (Tutorium 5) | | |
| | | | |
| ***Atmosphäre, 40°\ N:*** | | ***Wasserdampf:*** | |
| Wärmestrom: | $\dot{Q}_{\mathrm{A}} = 5\,\mathrm{PW}$ | Unterschied: | $\Delta x = 5\,\mathrm{g/kg}$ |
| Warm minus kalt: | $\Delta T = 20\,\mathrm{K}$ | Verdampfungs­enthalpie: | $\Delta h_{\mathrm{v}} = 2{,}43\,\mathrm{MJ/kg}$ |
| Umfang Breitenkreis: | $U = 30\,700\,\mathrm{km}$ | | |
| Höhe: | $H = 10\,\mathrm{km}$ | | |
| Mittlere Dichte: | $\bar{\rho} = 0{,}76\,\mathrm{kg/m^3}$ | | |

Die Einheit Sverdrup ($1\,\mathrm{Sv} = 10^{6}\,\mathrm{m^3/s}$) ist hier gegeben (nicht in der Formelsammlung).

**Aufgabenstellung:**

a) Vergleichen Sie die volumetrische Wärmekapazität $\rho\,c_p$ von Meerwasser und Luft. Die Luftsäule über $1\,\mathrm{m^2}$ hat die Masse $p_0/g$: Wie dick ist eine Wasserschicht $h_{\mathrm{W}}$ mit derselben Wärmekapazität? Wie dick muss die Schicht $h_{\mathrm{O}}$ auf dem ganzen Ozean sein, damit sie so viel Wärme speichert wie die ganze Atmosphäre? Prüfen Sie damit Ihre Vermutung zu Frage 3 und die oft zitierte Aussage, schon die obersten 3\ m des Ozeans speicherten mehr Wärme als die ganze Atmosphäre.\
   $(\rho\,c_p)_{\mathrm{W}}/(\rho\,c_p)_{\mathrm{L}} = 3390$, $\quad h_{\mathrm{W}} = 2{,}54\,\mathrm{m}$, $\quad h_{\mathrm{O}} = 3{,}57\,\mathrm{m}$, $\quad$ 3 m Ozean: $84\,\%$

b) Welcher Luftmassenstrom $\dot{m}_{\mathrm{L}}$ wäre für den Wärmestrom $\dot{Q}_{\mathrm{A}}$ nötig, wenn die Atmosphäre nur fühlbare Wärme transportierte? Rechnen Sie ihn mit der Dichte am Boden in einen Volumenstrom in Sverdrup um. Vergleichen Sie mit der AMOC, einmal als Volumenstrom und einmal als Massenstrom. Welcher Vergleich zählt für den Wärmetransport? Vergleichen Sie $\dot{Q}_{\mathrm{A}}$ mit $\dot{Q}_{\mathrm{AMOC}}$.\
   $\dot{m}_{\mathrm{L}} = 2{,}49\cdot 10^{11}\,\mathrm{kg/s}$, $\quad\dot{V}_{\mathrm{L}} = 2{,}07\cdot 10^{5}\,\mathrm{Sv}$,\
   $\dot{V}_{\mathrm{L}}/\dot{V}_{\mathrm{AMOC}} = 12\,200$, $\quad\dot{m}_{\mathrm{L}}/\dot{m}_{\mathrm{AMOC}} = 14{,}3$, $\quad\dot{Q}_{\mathrm{A}}/\dot{Q}_{\mathrm{AMOC}} = 4{,}2$

c) Nun enthält die warme Luft je Kilogramm $\Delta x$ mehr Wasserdampf als die kalte Luft. Welcher Erwärmung der Luft entspricht die latente Wärme dieses Wasserdampfs? Wie groß sind jetzt der nötige Luftmassenstrom und der latente Anteil am Transport? Vergleichen Sie mit der Forschung: In den mittleren Breiten trägt die latente Wärme ein Drittel bis die Hälfte des Transports (Stoll\ et\ al.,\ 2023). Wo wird diese Wärme wieder frei?\
   $\Delta T_{\mathrm{lat}} = 12{,}1\,\mathrm{K}$, $\quad\dot{m}_{\mathrm{L}} = 1{,}55\cdot 10^{11}\,\mathrm{kg/s}$, $\quad$ latenter Anteil $38\,\%$

d) Passat und Jetstream: (1) Die Hadley-Zelle, deren bodennaher Ast der Passat ist, wälzt auf der Nordhalbkugel im Mittel rund $\dot{m}_{\mathrm{H}} = 0{,}8\cdot 10^{11}\,\mathrm{kg/s}$ um (Li\ et\ al., 2022). Liegt Ihr Ergebnis aus c) in derselben Größenordnung? In welche Richtung trägt der Passat latente Wärme? (2) Die warme Luft nach Norden und die kalte Luft zurück teilen sich je zur Hälfte die senkrechte Fläche $U\,H$ über dem 40. Breitengrad (Abb. 2). Welche mittlere Geschwindigkeit $w_{\mathrm{N}}$ nach Norden reicht mit der mittleren Dichte $\bar{\rho}$ für den Massenstrom aus c)? Passat und Jetstream wehen viel schneller, aber vor allem in Ost-West-Richtung. Was bringt die Wärme also nach Norden?\
   Zu (1): $\dot{m}_{\mathrm{H}}/\dot{m}_{\mathrm{L}} = 0{,}52$; zu (2): $w_{\mathrm{N}} = 1{,}33\,\mathrm{m/s}$

## Zusatzaufgaben

**Zusatzaufgabe 1** (neu): Gegenstrom im Entenfuß

Eine Stockente steht im Winter stundenlang in kaltem Wasser. In ihren Beinen liegen die Arterien, die warmes Blut zu den Füßen bringen, dicht an den Venen, in denen das abgekühlte Blut zurückfließt. Beide Blutströme haben etwa denselben Wärmekapazitätsstrom $\dot{C}$. Mit $C^* = 1$ gilt für Gegenstrom und Gleichstrom

$$\varepsilon_{\mathrm{Gegen}} = \frac{NTU}{1 + NTU}, \qquad \varepsilon_{\mathrm{Gleich}} = \frac{1 - \exp(-2\,NTU)}{2}.$$

Die Beziehungen sind hier gegeben (nicht in der Formelsammlung). Rechnen Sie mit $NTU = 4$.

a) Berechnen Sie die Effektivität des Wärmeübertragers im Bein für Gegenstrom und für Gleichstrom.\
   $\varepsilon_{\mathrm{Gegen}} = 0{,}80$, $\quad\varepsilon_{\mathrm{Gleich}} = 0{,}50$

b) Welchem Wert nähert sich die Effektivität, wenn $NTU$ beliebig groß wird? Erklären Sie mit einer Skizze der Temperaturverläufe, warum der Gleichstrom nicht über 0,5 hinauskommt.\
   $\varepsilon_{\mathrm{Gegen}} \to 1$, $\quad\varepsilon_{\mathrm{Gleich}} \to 0{,}5$

c) Das Blut verlässt den Fuß etwa mit der Temperatur des Wassers. Drücken Sie die Wärmeabgabe des Fußes durch $\varepsilon$, $\dot{C}$ und die Temperaturen von Körper und Wasser aus. Um welchen Faktor senkt der Gegenstrom die Wärmeabgabe gegenüber dem Gleichstrom und gegenüber einem Bein ohne Wärmeübertragung? Messungen zeigen, dass Stockenten in 0 bis 20\ °C kaltem Wasser nur 3 bis 7\ % ihrer Stoffwechselwärme über die Füße verlieren (Kilgore & Schmidt-Nielsen, 1975). Wie viel wäre es bei gleicher Durchblutung ohne Wärmeübertragung im Bein?\
   $\dot{Q}_{\mathrm{Fuß}} = (1 - \varepsilon)\,\dot{C}\,(\vartheta_{\mathrm{Körper}} - \vartheta_{\mathrm{Wasser}})$,\
   Faktor $2{,}5$ bzw. $5$, $\quad$ ohne Wärmeübertragung $15$ bis $35\,\%$

**Zusatzaufgabe 2** (neu, Exkurs): Der Rekordflug

In der Nacht zum 9. Februar 2020 flog eine Boeing 747 in 4\ h 56\ min von New York nach London, angeschoben vom Jetstream über dem Sturm Ciara. Sie fliegt mit Mach 0,85; in 10,7\ km Höhe sind das rund 252\ m/s gegenüber der Luft. Die kürzeste Verbindung von New York nach London, der Großkreis, ist 5540\ km lang.

a) Wie stark war der mittlere Rückenwind $w_{\mathrm{R}}$, wenn das Flugzeug dem Großkreis gefolgt ist? Geben Sie ihn auch in km/h an.\
   $w_{\mathrm{R}} = 59{,}9\,\mathrm{m/s} = 216\,\mathrm{km/h}$

b) Warum ist dieser Wert eine Untergrenze? Wie stark war der Rückenwind, wenn der Flugweg 3\ % länger war als der Großkreis? Vergleichen Sie mit der Schätzung von Flightradar24, rund 67\ m/s (NPR, 2020).\
   $w_{\mathrm{R}} = 69{,}3\,\mathrm{m/s}$

c) Wie lange hätte der Flug ohne Wind gedauert?\
   $t = 6{,}11\,\mathrm{h}$

# Anhang: Quellen der Arbeitswerte

Je Tutorium die Quellen der Arbeitswerte und der Fakten in den Ausgangssituationen. Die Rechenskripte liegen im Ordner „Rechnung“ des Pakets.

## Tutorium 1: Wärmeleitung

**Quellen Tutorium 1: Wärmeleitung**

Quellen der Arbeitswerte und Fakten in `teile/t1.md`, übernommen aus den Quellenverzeichnissen der Ausgangsdokumente (Ideensammlung „Leitaufgaben aus Klima und Erde“ vom 17.10.2026, Abschnitt 12; Pilotblatt Tutorium 1 mit Musterlösung). In Klammern steht, wo der Wert oder Fakt vorkommt. Zahlen: `rechnung/t1_rechnung.py`.

**Aufgabe 1: Seen unter dem Eisschild**

- **Kälterekord −89,2 °C an der Station Wostok am 21.07.1983** (Ausgangssituation, Teil c): WMO. (o. J.). *World record: Lowest temperature, Vostok, Antarctica*. <https://public.wmo.int/node/13122>
- **Hunderte Seen unter dem Eis** (675 erfasst, Stand 2022; Ausgangssituation): Livingstone, S. J., et al. (2022). Subglacial lakes and their changing role in a warming climate. *Nature Reviews Earth & Environment, 3*, 106 bis 124. <https://doi.org/10.1038/s43017-021-00246-9>
- **Bohrung erreicht am 05.02.2012 in 3769 m Tiefe das Wasser des Wostoksees** (Ausgangssituation, Teil f; der Literaturwert von etwa −3 °C wird bewusst nicht genannt: Er passt zu luftgesättigtem Eis mit 0,098 K/MPa, das Modell der Aufgabe rechnet mit reinem Eis, 0,0742 K/MPa, und ergäbe in 3769 m −2,52 °C): Jones, N. (2012). \[Titel nicht erfasst; Nachricht zur Bohrung am Wostoksee\]. *Nature, 482*, 287. <https://doi.org/10.1038/482287a>
- **Wärmestromdichte aus dem Erdinneren im weltweiten Mittel rund 0,09 W/m²** (Ausgangssituation, Zusatzaufgabe 1 b): Davies, J. H., & Davies, D. R. (2010). Earth’s surface heat flux. *Solid Earth, 1*, 5 bis 24. <https://doi.org/10.5194/se-1-5-2010>. Vergleich mit einer 40-W-Glühlampe auf einem Basketballfeld (420 m², also 95 mW/m²): eigene Rechnung der Ideensammlung.
- **Wärmestromdichte aus dem Erdinneren 58 mW/m²** (Tabelle; Dome C aus Bohrlochdaten 57,9 ± 6,4 mW/m²): Talalay, P., et al. (2020). Geothermal heat flux from measured temperature profiles in deep ice boreholes in Antarctica. *The Cryosphere, 14*, 4021 bis 4037. <https://doi.org/10.5194/tc-14-4021-2020>
- **Wärmeleitfähigkeit von Eis λ(T) = 9,828 W/(m K) · exp(−5,7·10⁻³ K⁻¹ · T) und Schmelzpunktsenkung γ = 0,0742 K/MPa (reines Eis; luftgesättigt 0,098 K/MPa)** (Satz unter der Tabelle, Tabelle): Cuffey, K. M., & Paterson, W. S. B. (2010). *The physics of glaciers* (4. Aufl.). Elsevier. Die Formel für λ(T) ist zitiert nach Mony, L., Roberts, J. L., & Halpin, J. A. (2020). Inferring geothermal heat flux from an ice-borehole temperature profile at Law Dome, East Antarctica. *Journal of Glaciology, 66*, 509 bis 519. <https://doi.org/10.1017/jog.2020.27>
- **Messwerte im Bohrloch EPICA Dome C: −4,2 °C in 3200 m und −2,34 °C in 3270,2 m Tiefe** (Tabelle, Teil h): Augustin, L., et al. (2007). EPICA Dome C 2 drilling operations: Performances, difficulties, results. *Annals of Glaciology, 47*, 68 bis 72. <https://doi.org/10.3189/172756407786857767>. Die Tiefe 3270,2 m ist der Wert aus dem Pilotskript `pilot_tutorium1.py`; das Pilotblatt nannte gerundet 3270 m.
- **Dicke der Firnschicht s~F~ = 100 m** (Tabelle, Teil h): Arbeitswert des Pilotblatts („obere 100 m“), dort ohne eigene Quelle.
- **Wärmeleitfähigkeit von Firn λ~F~ = 1,0 W/(m K)** (Tabelle, Teil h; Arbeitswert, bei Dome C 0,9 bis 2,2 W/(m K) je nach Dichte): Calonne, N., et al. (2019). Thermal conductivity of snow, firn, and porous ice from 3-D image-based computations. *Geophysical Research Letters, 46*. Daten: PANGAEA. <https://doi.org/10.1594/PANGAEA.906906>
- **Eisdicke 3700 m und Oberflächentemperatur −55 °C** (Tabelle): Arbeitswerte der Ideensammlung (Abschnitt 4.1, Anhang A) für einen allgemeinen Standort in der Ostantarktis, nicht für die Bohrstelle Wostok (dort friert Seewasser an die Eisbasis an). Zum Vergleich: Wostoksee unter rund 3,8 km Eis, Studinger, M., et al. (2004). \[Titel nicht erfasst; Wostoksee\]. *Geophysical Research Letters, 31*. <https://doi.org/10.1029/2004GL019801>
- **Dichte von Eis 917 kg/m³, Schmelzenthalpie 333,5 kJ/kg, g = 9,81 m/s²** (Tabelle): Standardwerte; Arbeitswerte der Ideensammlung und des Pilotblatts, dort ohne eigene Quelle.
- **Mittlere Wärmeleitfähigkeit als Integralmittel, Randbedingungen nach Dirichlet und von Neumann** (Teil c, d): Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* \[Vorlesungsfolien\], V02 F. 12 und F. 28 bis 30. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn.

**Aufgabe 2: Kühlhauswand**

- **Wärmeleitfähigkeit von Stahlbeton λ~B~ = 2,3 W/(m K)** (Tabelle): Bemessungswert für Stahlbeton mit 1 % Bewehrung nach DIN EN ISO 10456, so im Pilotskript `pilot_tutorium1.py` angegeben. Die Norm wurde nicht eingesehen; die Prüfung ist im Pilotblatt als offen vermerkt.
- **Wärmeleitfähigkeit von Hartschaum aus Polyurethan λ~D~ = 0,025 W/(m K)** (Tabelle): Arbeitswert des Pilotblatts; Prüfung gegen DIN 4108-4 bzw. DIN EN ISO 10456 laut Pilotblatt offen.
- **Dicken 20 cm und 12 cm, Oberflächentemperaturen 28 °C und −22 °C, Fläche 250 m², Grenzwert 8 W/m²** (Ausgangssituation, Tabelle): frei gewählte Arbeitswerte des Pilotblatts (Teil 3, technische Zwillingsaufgabe).

**Zusatzaufgabe 1: Erdwärme in Deutschland**

- **Kontinentale Tiefbohrung (KTB) in der Oberpfalz, Endteufe 9101 m**: GFZ Helmholtz-Zentrum für Geoforschung. (2024). *Der Tiefpunkt in Deutschland feierte Jubiläum* \[Meldung zur KTB\]. <https://www.gfz.de/en/press/news/details/der-tiefpunkt-in-deutschland-feierte-jubilaeum>
- **Temperaturgradient etwa 28 K/km**: GFZ (2024), wie oben; Smellie, J. (2004). \[Titel nicht erfasst\] (SKB-Bericht R-04-09). Svensk Kärnbränslehantering. <https://skb.com/publication/21179/R-04-09.pdf>
- **Wärmeleitfähigkeit des Gesteins etwa 2,9 W/(m K)**: Arbeitswert der Ideensammlung, Abschnitt 4.1 (dort zusammen mit GFZ und Smellie, 2004, genannt; ein eigener Beleg für diesen Wert ist nicht ausgewiesen).
- **Weltweites Mittel rund 0,09 W/m²** (Teil b): Davies & Davies (2010), siehe Aufgabe 1.

**Herkunft der Fragen**

- Frage 1 (Vorab-Frage Firn oder Eis): Pilotblatt Tutorium 1 und Ideensammlung, Abschnitt 4.1 (Entscheidung D52).
- Frage 2 (Einheiten-Check): Pilotblatt, Zusatzaufgabe 2.1. Hintergrund zur Verwechslung von Wärme und Temperatur: Prince, M., Vigeant, M., & Nottis, K. (2012). Development of the Heat and Energy Concept Inventory: Preliminary results on the prevalence and persistence of engineering students’ misconceptions. *Journal of Engineering Education, 101*(3), 412 bis 438. <https://doi.org/10.1002/j.2168-9830.2012.tb00056.x>
- Frage 3 (Temperaturprofile lesen): Pilotblatt, Zusatzaufgabe 2.2; Abb. 2 neu gezeichnet nach dem Grafikskript des Pilotblatts (`pilot_t1_grafiken.py`, 17.10.2026).

## Tutorium 2: Konvektion

**Quellen Tutorium 2: Konvektion**

Quellen der Arbeitswerte und Fakten in `teile/t2.md`, übernommen aus den Quellenverzeichnissen der Ausgangsdokumente (Ideensammlung „Leitaufgaben aus Klima und Erde“ vom 17.10.2026, Abschnitt 12; Nachrechnung `nachrechnung_leitphaenomene.py`). In Klammern steht, wo der Wert oder Fakt vorkommt. Zahlen: `rechnung/t2_rechnung.py`.

**Aufgabe 1: Offene Rinnen im Meereis**

- **Rinnen bedecken im Winter nur 1 bis 2 % der zentralen Arktis, liefern aber über 70 % des Wärmestroms vom Ozean nach oben; schmale Rinnen geben pro Fläche mehr Wärme ab als breite** (Ausgangssituation, Teil f und i): Marcq, S., & Weiss, J. (2012). Influence of sea ice lead-width distribution on turbulent heat transfer between the ocean and the atmosphere. *The Cryosphere, 6*, 143 bis 156. <https://doi.org/10.5194/tc-6-143-2012>
- **Seerauch über offenem Wasser** (Ausgangssituation, Teil h): Ideensammlung, Abschnitt 4.2, Einstieg (qualitativ, ohne Zahl).
- **Luft −30 °C, Wasser −1,8 °C, Wind 8 m/s, Rinne 10 m breit und 1 km lang, Vergleichsbreiten 1 m und 100 m** (Ausgangssituation, Tabelle): Arbeitswerte der Ideensammlung, Abschnitt 4.2 (Aufgabenskizze und Kernzahlen) und Anhang A; Rechnung wie in `nachrechnung_leitphaenomene.py`, Abschnitt T2.
- **Stoffwerte der Luft bei der Filmtemperatur −15,9 °C** (Tabelle: λ, ν, Pr) und **bei −10 °C** (Zusatzaufgabe 1): CoolProp 8.0, Pseudo-Reinstoff Luft, p = 1,01325 bar, wie in der Nachrechnung. Zustandsgleichung nach Lemmon et al. (2000), Viskosität und Wärmeleitfähigkeit nach Lemmon & Jacobsen (2004) (Literaturangaben laut CoolProp-Bibliothek):
  - Lemmon, E. W., Jacobsen, R. T., Penoncello, S. G., & Friend, D. G. (2000). Thermodynamic properties of air and mixtures of nitrogen, argon, and oxygen from 60 to 2000 K at pressures to 2000 MPa. *Journal of Physical and Chemical Reference Data, 29*(3), 331 bis 385. <https://doi.org/10.1063/1.1285884>
  - Lemmon, E. W., & Jacobsen, R. T. (2004). Viscosity and thermal conductivity equations for nitrogen, oxygen, argon, and air. *International Journal of Thermophysics, 25*(1), 21 bis 69. <https://doi.org/10.1023/B:IJOT.0000022327.04529.f3>
  - Bell, I. H., Wronski, J., Quoilin, S., & Lemort, V. (2014). Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp. *Industrial & Engineering Chemistry Research, 53*(6), 2498 bis 2508. <https://doi.org/10.1021/ie4033999>
- **Korrelationen und charakteristische Längen** (Teil c bis g, Frage 3, Zusatzaufgabe 1): Lehrstuhl für Fluidverfahrenstechnik. (2026). *Formelsammlung Wärmeübertragung* (Stand SoSe 2026) und Zusatzblatt *Charakteristische Längen*. Universität Paderborn. Verwendet: längs angeströmte Platte (turbulent, 5·10⁵ < Re < 10⁷), waagerechte Platte bei freier Konvektion mit β = 1/T~u~ und L = A/U, quer angeströmter Zylinder (Übergangsbereich, L = πd/2).
- **Grenzschichten, lokales und mittleres α, typische Größenordnungen von α, Biot- und Nußelt-Zahl** (Teil a, b, h; Frage 4): Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* \[Vorlesungsfolien\], V03 F. 9 bis 19 und F. 21 bis 36. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn.

**Zusatzaufgabe 1: Windchill**

- **Windchill-Temperatur in Nordamerika seit 2001, Gesicht als quer angeströmter Zylinder**: Osczevski, R., & Bluestein, M. (2005). The new wind chill equivalent temperature chart. *Bulletin of the American Meteorological Society, 86*(10), 1453 bis 1458. <https://journals.ametsoc.org/view/journals/bams/86/10/bams-86-10-1453.xml>
- **Finger d = 2 cm, Kopf d = 18 cm, Wind 5 m/s (α ≈ 69 und 33 W/(m² K)); Kopf bei 0,5 m/s; Luft −10 °C**: Arbeitswerte der Ideensammlung, Abschnitt 4.2 (Zusatzaufgaben), gerechnet wie in `nachrechnung_leitphaenomene.py` (Stoffwerte der Luft bei −10 °C).

**Herkunft der Fragen**

- Frage 1 (Vorab-Frage 1 m oder 100 m breite Rinne), Frage 2 (Frei oder erzwungen?, acht Situationen), Frage 3 (Charakteristische Länge) und Frage 4 (Biot oder Nußelt?): Ideensammlung, Abschnitt 4.2 (Vorab-Frage und Zusatzaufgaben).

## Tutorium 3: Wärmedurchgang

**Quellen Tutorium 3: Wärmedurchgang**

Übernommen aus dem Quellenverzeichnis der Ideensammlung „Leitaufgaben aus Klima und Erde“ (17.10.2026, Abschnitt 12), ergänzt um das TAPS Factbook (am 21.10.2026 erneut eingesehen) und die Stoffwertquellen des Rechenskripts. „Arbeitswert“ heißt: in der Ideensammlung oder im Rechenskript gewählt, nicht aus einer Primärquelle.

**Aufgabe 1: Meereis und Schnee als Deckel**

- Itkin, P., et al. (2023). Sea ice and snow characteristics from year-long transects at the MOSAiC Central Observatory. *Elementa: Science of the Anthropocene, 11*(1). <https://doi.org/10.1525/elementa.2022.00048>
  Einjähriges Meereis im Februar meist etwa 1,4 m dick, darauf 10 bis 30 cm Schnee (Ausgangssituation; $s_\mathrm{E} = 1{,}4\,\mathrm{m}$, $s_\mathrm{S} = 0{,}2\,\mathrm{m}$).
- Sturm, M., Holmgren, J., König, M., & Morris, K. (1997). The thermal conductivity of seasonal snow. *Journal of Glaciology, 43*(143), 26 bis 41. <https://doi.org/10.3189/S0022143000002781>
  Wärmeleitfähigkeit von Schnee rund 0,03 bis 0,7 W/(m·K) je nach Dichte und Gefüge; Arbeitswert $\lambda_\mathrm{S} = 0{,}2\,\mathrm{W/(m\,K)}$, Spannbreite 0,14 bis 0,3 W/(m·K) in Teil c und Frage 1.
- Damseaux, A., et al. (2025). [Titel nicht erfasst; Wärmeleitfähigkeit von Schnee]. *The Cryosphere, 19*, 1539 ff. <https://doi.org/10.5194/tc-19-1539-2025>
  Wie oben (Spannbreite der Wärmeleitfähigkeit von Schnee).
- Maykut, G. A. (1978). Energy exchange over young sea ice in the central Arctic. *Journal of Geophysical Research, 83*(C7), 3646 bis 3658. <https://doi.org/10.1029/JC083iC07p03646>
  Dünnes Eis verliert viel mehr Wärme als dickes und wächst schnell nach (Teil f, Vergleich mit Jungeis).
- National Snow and Ice Data Center. (2026, 7. Oktober). *Arctic sea ice news and analysis*. <https://nsidc.org/sea-ice-today/analyses/stranger-things-2026-arctic>
  Hintergrund zur Reflexionsfrage in Teil f (Rückgang des arktischen Meereises); keine Zahl im Blatt.
- Arbeitswerte (Ideensammlung 4.2 und 4.3): Luft $-30\,\mathrm{°C}$, Meerwasser $-1{,}8\,\mathrm{°C}$ (Gefrierpunkt), $\lambda_\mathrm{E} = 2{,}1\,\mathrm{W/(m\,K)}$, $\rho_\mathrm{E} = 917\,\mathrm{kg/m^3}$, $\Delta h_{\mathrm{schm}} = 333{,}5\,\mathrm{kJ/kg}$, Jungeis $s_\mathrm{J} = 0{,}1\,\mathrm{m}$ ohne Schnee (Teil f; Kernzahlen 4.3). Für die Stoffwerte von Eis nennt die Ideensammlung keine eigene Quelle. Die Fläche $A = 1\,\mathrm{m^2}$ ist eine frei gewählte Bezugsfläche.
- Arbeitswert $\alpha_\mathrm{a} = 15\,\mathrm{W/(m^2\,K)}$ für eine große Scholle (Ideensammlung E16, Entscheidungsprotokoll D46), begründet mit Tutorium 2: Rinne von 10 m Breite bei 8 m/s mit $\alpha = 19{,}6\,\mathrm{W/(m^2\,K)}$ und $554\,\mathrm{W/m^2}$ (Nachrechnung mit der Formelsammlung SoSe 2026 und CoolProp, Teil e).

**Aufgabe 2: Ölleitung im Permafrost**

- Alyeska Pipeline Service Company. (2024). *TAPS factbook*. <https://www.alyeska-pipe.com/wp-content/uploads/2025/01/24-APSC-0352-FACTBOOK-UPDATE-FOR-WEB-FINAL1_AA.pdf>
  Außendurchmesser 48 Zoll ($d_{\mathrm{St}} = 1{,}22\,\mathrm{m}$); Wanddicke 0,462 Zoll (466 Meilen) und 0,562 Zoll (334 Meilen), gewählt 0,562 Zoll ($s_{\mathrm{St}} = 14{,}3\,\mathrm{mm}$); Dämmung der aufgeständerten Leitung 3,75 Zoll ($s_{\mathrm{Iso}} = 9{,}5\,\mathrm{cm}$); Länge 800 Meilen (1288 km), davon 420 Meilen auf Stützen („etwa die Hälfte“ in der Ausgangssituation); 124 300 Wärmerohre in den Stützen (Teil f); Öl 2024 mindestens 85 °F (29 °C) bei der Einspeisung an Pump Station 1 (Arbeitswert $\vartheta_\mathrm{i} = 30\,\mathrm{°C}$).
- Hjort, J., et al. (2018). Degrading permafrost puts Arctic infrastructure at risk by mid-century. *Nature Communications, 9*, 5147. <https://doi.org/10.1038/s41467-018-07557-4>
  Hintergrund zu Teil f (Bauwerke auf tauendem Permafrost); keine Zahl im Blatt.
- Bell, I. H., Wronski, J., Quoilin, S., & Lemort, V. (2014). Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp. *Industrial & Engineering Chemistry Research, 53*(6), 2498 bis 2508. <https://doi.org/10.1021/ie4033999>
  Stoffwerte der Luft bei $-29\,\mathrm{°C}$ und 1,01325 bar ($\nu_\mathrm{L}$, $\lambda_\mathrm{L}$, $Pr$), berechnet mit CoolProp 8.0.
- Lemmon, E. W., Jacobsen, R. T., Penoncello, S. G., & Friend, D. G. (2000). Thermodynamic properties of air and mixtures of nitrogen, argon, and oxygen from 60 to 2000 K at pressures to 2000 MPa. *Journal of Physical and Chemical Reference Data, 29*(3), 331 bis 385. <https://doi.org/10.1063/1.1285884>
  Zustandsgleichung der Luft in CoolProp (Dichte, Wärmekapazität).
- Lemmon, E. W., & Jacobsen, R. T. (2004). Viscosity and thermal conductivity equations for nitrogen, oxygen, argon, and air. *International Journal of Thermophysics, 25*(1), 21 bis 69. <https://doi.org/10.1023/B:IJOT.0000022327.04529.f3>
  Viskosität und Wärmeleitfähigkeit der Luft in CoolProp.
- Lehrstuhl für Fluidverfahrenstechnik. (2026). *Formelsammlung Wärmeübertragung* (Stand SoSe 2026) und Zusatzblatt *Charakteristische Längen*. Universität Paderborn.
  Querumströmter Zylinder (Übergangsbereich) mit $L = \pi d/2$, Stoffwerte bei der Filmtemperatur (Teil a).
- Arbeitswerte aus nachrechnung_leitphaenomene.py (ohne Primärquelle): $\lambda_{\mathrm{St}} = 45\,\mathrm{W/(m\,K)}$, $\lambda_{\mathrm{Iso}} = 0{,}04\,\mathrm{W/(m\,K)}$ (auch Ideensammlung 4.3), $\alpha_\mathrm{i} = 500\,\mathrm{W/(m^2\,K)}$, Wind 5 m/s, Luft $-30\,\mathrm{°C}$.

**Fragen und Zusatzaufgabe**

- Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* [Vorlesungsfolien]. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn, Sommersemester 2026.
  V05 F. 22 bis 27: elektrische Analogie, Reihen- und Parallelschaltung (Frage 2, Zusatzaufgabe 1); V05 F. 29 bis 38: Wärmedurchgangskoeffizient, Rohr, $k_\mathrm{i}$ und $k_\mathrm{a}$ (Frage 3, Aufgabe 2); V05 Beispiel 6: Isolationsdicke und kritischer Radius (Aufgabe 2, Teil e).
- Frage 1 (Vorab-Frage) und Zusatzaufgabe 1 (Parallelschaltung) nach Ideensammlung 4.3; Werte wie in Aufgabe 1.

## Tutorium 4: Strahlung

**Quellen Tutorium 4: Strahlung**

Übernommen aus dem Quellenverzeichnis der Ideensammlung „Leitaufgaben aus Klima und Erde“ (17.10.2026, Abschnitt 12). Der Wert 3,93 W/m² und die Gegenstrahlung von 342 W/m² wurden am 21.10.2026 im Text von Forster et al. (2021) nachgesehen. „Arbeitswert“ heißt: in der Ideensammlung oder im Rechenskript gewählt, nicht aus einer Primärquelle.

**Aufgabe 1: Die Strahlungsbilanz der Erde**

- Kopp, G., & Lean, J. L. (2011). A new, lower value of total solar irradiance: Evidence and climate significance. *Geophysical Research Letters, 38*, L01706. <https://doi.org/10.1029/2010GL045777>
  $S_0 = 1361\,\mathrm{W/m^2}$ (Ausgangssituation, Tabelle). Holman (2010) nennt noch 1395 W/m², einen älteren Wert.
- Stephens, G. L., et al. (2015). The albedo of Earth. *Reviews of Geophysics, 53*(1), 141 bis 163. <https://doi.org/10.1002/2014RG000449>
  Planetare Albedo 0,29 bis 0,30; Arbeitswert $\rho_\mathrm{p} = 0{,}30$.
- Copernicus Climate Change Service. (2025). *Global climate highlights 2024*. <https://climate.copernicus.eu/global-climate-highlights-2024>
  Mittlere Oberflächentemperatur 15,1 °C im Jahr 2024; Arbeitswert $T_\mathrm{O} = 288\,\mathrm{K}$ („rund 15 °C“).
- Davies, J. H., & Davies, D. R. (2010). Earth’s surface heat flux. *Solid Earth, 1*, 5 bis 24. <https://doi.org/10.5194/se-1-5-2010>
  Gesamter Erdwärmestrom 47 TW, im Mittel 92 mW/m² (eigene Rechnung); mit 44,2 TW nach Pollack et al. (1993) 87 mW/m². Arbeitswert $\dot{q}_\mathrm{E} = 0{,}09\,\mathrm{W/m^2}$ (Teil d).
- Pollack, H. N., Hurter, S. J., & Johnson, J. R. (1993). Heat flow from the Earth’s interior: Analysis of the global data set. *Reviews of Geophysics, 31*(3), 267 bis 280. <https://doi.org/10.1029/93RG01249>
  Wie oben.
- Forster, P., et al. (2021). The Earth’s energy budget, climate feedbacks, and climate sensitivity. In *Climate change 2021: The physical science basis* (Kapitel 7). IPCC; Cambridge University Press. <https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/>
  Abb. 7.2: Gegenstrahlung 342 W/m², Abstrahlung der Oberfläche 398 W/m², Konvektion 21 W/m², Verdunstung 82 W/m², in der Atmosphäre absorbierte Sonnenstrahlung rund 80 W/m² (alle in Teil g; die 80 W/m² zeigen, dass die Durchlässigkeit der Schicht für Sonnenlicht nur eine Modellannahme ist, Entscheidungsprotokoll D45). Strahlungsantrieb bei Verdopplung von CO₂: 3,93 ± 0,47 W/m² (Abschnitt 7.3.2.1; Tabelle und Teil h).
- IPCC. (2021). Summary for policymakers. In *Climate change 2021: The physical science basis*. Cambridge University Press. <https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/>
  Gleichgewichts-Klimasensitivität am besten geschätzt 3 K, wahrscheinlich 2,5 bis 4 K (Teil h).
- Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* [Vorlesungsfolien]. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn, Sommersemester 2026.
  V04 F. 7 bis 19: $\alpha + \rho + \tau = 1$, schwarzer und grauer Strahler, $\sigma = 5{,}6705\cdot 10^{-8}\,\mathrm{W/(m^2\,K^4)}$, Kirchhoff’sches Gesetz, Nettowärmestrom eines Körpers mit seiner Umgebung.
- Holman, J. P. (2010). *Heat transfer* (10. Aufl.). McGraw-Hill. Abschnitt 8-15 (Strahlung der Umwelt).
- Schichtmodell und Linearisierung $4\sigma T_\mathrm{e}^3$: Zusatzwissen nach Ideensammlung 4.4 (in der Aufgabe als gegeben gekennzeichnet).

**Fragen**

- Frage 1 (Vorab-Frage): Vorschlag der Ideensammlung 4.4; Werte aus Teil d.
- Frage 2 (Autoscheibe): bisherige Vorab-Frage aus „Lernziele, Vorab-Fragen und Bilanz-Systematik“ (16.10.2026); wirksame Umgebungstemperatur $-5\,\mathrm{°C}$ wie in V08 Teil g (Riese, 2026), siehe Zusatzaufgabe 2.
- Frage 3 (Kirchhoff):
  - Perovich, D. K., et al. (2002). Seasonal evolution of the albedo of multiyear Arctic sea ice. *Journal of Geophysical Research, 107*(C10), 8044. <https://doi.org/10.1029/2000JC000438> (Schnee wirft 80 bis 90 % des Sonnenlichts zurück)
  - Warren, S. G. (2019). Optical properties of ice and snow. *Philosophical Transactions of the Royal Society A, 377*, 20180161. <https://doi.org/10.1098/rsta.2018.0161> (Schnee im Infraroten mit $\varepsilon = 0{,}98$ bis $0{,}99$)
  - Holman (2010), Tabelle 8-4 (weiße Farbe strahlt im Infraroten stark ab)
- Frage 4 (Ozonloch): verbreitete Fehlvorstellung nach Boyes, E., & Stanisstreet, M. (1993). The ‘greenhouse effect’: Children’s perceptions of causes, consequences and cures. *International Journal of Science Education, 15*(5), 531 bis 552. <https://doi.org/10.1080/0950069930150507> und Walz, K. A., & Kerr, S. C. (2007). „Holes“ in student understanding: Addressing prevalent misconceptions regarding atmospheric environmental chemistry. *Journal of Chemical Education, 84*(10), 1693. <https://doi.org/10.1021/ed084p1693>

**Zusatzaufgaben**

- Zusatzaufgabe 1 (Eis aus der Nacht): Barker, R. (1775). The process of making ice in the East Indies. *Philosophical Transactions of the Royal Society of London, 65*, 252 bis 257. <https://doi.org/10.1098/rstl.1775.0023>
  Arbeitswerte aus nachrechnung_leitphaenomene.py: Luft 5 °C, Himmel $-20\,\mathrm{°C}$, $\alpha_\mathrm{L} = 2$ bis $5\,\mathrm{W/(m^2\,K)}$, Wasser $\varepsilon = 0{,}96$.
- Zusatzaufgabe 2 (Autoscheibe und Reif): Werte wie in V08 Teil g (Riese, 2026): Glas $\varepsilon = 0{,}95$, $-5\,\mathrm{°C}$ (dort Temperatur des Himmels über einem Solarpanel am Tag; hier Arbeitswert für die wirksame Temperatur der Umgebung aus klarem Himmel, Häusern und Bäumen, die die schräge Scheibe sieht; der klare Himmel allein wirkt kälter, vgl. $-20\,\mathrm{°C}$ in Zusatzaufgabe 1), freie Konvektion $\alpha = 5\,\mathrm{W/(m^2\,K)}$; Wind mit $\alpha_\mathrm{L} = 10\,\mathrm{W/(m^2\,K)}$ als eigener Arbeitswert.

## Tutorium 5: Wärmebilanzen (instationär global)

**Aufgabe 1: Kaffee mit Milch**

- Kaffee in der Tasse 80 °C: gebrüht bei etwa 93 °C, in der Glaskanne einer Haushaltsmaschine bis etwa 11 K kälter, beim Eingießen 2 bis 5 K kälter (Tab. 1): Abraham, J. P. & Diller, K. R. (2019), A review of hot beverage temperatures, satisfying consumer preference and safety, J. Food Sci. 84(8), 2011 bis 2014, doi:10.1111/1750-3841.14699: <https://foodsci.oregonstate.edu/sites/agscid7/files/foodsci/attachments/hot-bev-temp.pdf>
- Servierbereich 71 bis 85 °C: Brown, F. & Diller, K. R. (2008), Calculating the optimum temperature for serving hot beverages, Burns 34(5), 648 bis 654: <https://doi.org/10.1016/j.burns.2007.09.012>
- Kaffee mit den Stoffwerten von Wasser (gelöste Stoffe 1,15 bis 1,35 %, Specialty Coffee Association): <https://support.moccamaster.com/hc/en-us/articles/1500009409121>
- Milch aus dem Kühlschrank höchstens 7 °C, besser unter 5 °C: Bundesinstitut für Risikobewertung (13.02.2023), Fragen und Antworten zum Kühlen von Lebensmitteln: <https://www.bfr.bund.de/fragen-und-antworten/thema/korrektes-kuehlen-von-lebensmitteln-im-privathaushalt/>
- Im Mittel 31 g Milch je Tasse: Food Standards Australia New Zealand (2011), Dash and splash measures program (die Seite zeigt die Zahlen derzeit nicht mehr, Stand 29.10.2026): <https://www.foodstandards.gov.au/science-data/monitoringnutrients/ausnut/foodmeasures/2011-Dash-and-splash-measures-program>
- Dichte von Milch 1027 bis 1033 kg/m³: Goff, H. D., Dairy Science and Technology, University of Guelph: <https://books.lib.uoguelph.ca/dairyscienceandtechnologyebook/chapter/physical-properties-of-milk/>; spezifische Wärmekapazität wie in Tutorium 8 (Quelle dort)
- Abkühlung eines offenen, nicht umgerührten Keramikbechers, Zeitkonstante etwa 41 min (aus der Steigung 0,0241 1/min in Abb. 6); ein Deckel senkt das scheinbare kA um 44 %: Ferreira, J. P. M. (2025), Forced convection and the coffee cup, Phys. Educ. 60, 035001: <https://doi.org/10.1088/1361-6552/adb6ea> (Manuskript: <https://ciencia.ucp.pt/ws/files/116791893/116791417.pdf>). Haushaltsbecher kühlen je nach Form und Füllung auch schneller ab (Zeitkonstante etwa 20 bis 40 min); die Aussage der Aufgabe hängt davon kaum ab.
- Verdunstung bei 79 °C 12,0 von 22,7 W: Condoret (2007), Teaching transport phenomena around a cup of coffee, Chem. Eng. Educ. 41(2), Tab. 2 (nicht frei einsehbar): <https://journals.flvc.org/cee/article/view/122462>
- Erwärmte Milch 55 bis 65 °C: Thermoplan, Coffee knowledge: milk: <https://www.thermoplan.ch/en/coffeecompetence/blog/coffee-knowledge-milk>
- Keramikbecher 300 g mit 0,85 kJ/(kg·K): Arbeitswert (Schätzung für einen üblichen Becher), nicht durch eine Quelle belegt
- Hauptaussage (Milch sofort hält den Kaffee länger warm): Rees, W. G. & Viney, C. (1988), On cooling tea and coffee, Am. J. Phys. 56(5), 434 bis 437: <https://doi.org/10.1119/1.15572>
- Rechnung: `rechnung/kaffee_modell.py` und `rechnung/t5_kaffee_teil.py`

**Fragen 2 und 3**

- Situationen des Bilanz-Detektivs und Körper zum Ankreuzen: Ideensammlung „Leitaufgaben aus Klima und Erde“ (17.10.2026), Abschnitt 4.5, Zusatzaufgaben
- Käse aus Foliensatz 08, Teil e (Form 30 cm hoch, Wärmeabgabe nur über die Oberseite): Riese, J. (2026), Wärmeübertragung, Foliensatz 08 „Aufgabe zur Zusammenfassung“, Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn; Abschätzung *Bi* ≈ 5 bis 10 in „Tutorien: Lernziele und Bilanzsystematik“ (16.10.2026), Abschnitt 6
- Aussage „Im stationären Zustand fließt keine Wärme.“ als typische Fehlvorstellung: Streveler, R. A., Olds, B. M., Miller, R. L. & Nelson, M. A. (2003), Using a Delphi study to identify the most difficult concepts for students to master in thermal and transport sciences, ASEE Annual Conference: <https://doi.org/10.18260/1-2--12592>

**Aufgabe 2: Die AMOC und Europas milde Winter**

- AMOC bei 26,5° N im Mittel 16,9 ± 1,2 Sv (Arbeitswert 17 Sv) und Wärmestrom 1,20 ± 0,12 PW, 2004 bis 2020: Johns, W. E. et al. (2023), Phil. Trans. R. Soc. A 381, 20220188: <https://doi.org/10.1098/rsta.2022.0188>
- 1 Sv = 10⁶ m³/s: University of Miami (RSMAS), Ocean Surface Currents, Glossar: <https://oceancurrents.rsmas.miami.edu/glossary.html>; Talley, L. D. (2019), SIO 210: <https://sam.ucsd.edu/ltalley/sio210/transports/>
- Amazonas 206 000 m³/s: Callède, J. et al. (2010), Rev. Sci. Eau 23(3), 247 bis 273: <https://doi.org/10.7202/044688ar>
- Golfstrom nahe 60° W mindestens 150 Sv (nach Hogg, 1992): Heiderich, J. & Todd, R. E. (2020), J. Phys. Oceanogr. 50(8), 2251 bis 2270: <https://par.nsf.gov/servlets/purl/10193359>
- Meerwasser 1025 kg/m³ und 3990 J/(kg K), Oberflächenwasser etwa 20 °C, Tiefenwasser etwa 3 °C: Arbeitswerte aus „Aufgabenideen: Meeresströmungen, Sverdrup und Luftströmungen“ (20.10.2026), ohne eigene Quelle
- Flächen zwischen 40° und 70° N (Gürtel 7,6·10¹³ m², Viertel 50° W bis 40° O 1,9·10¹³ m²) und Sonne am Oberrand im Januarmittel bei 51,7° N (93 W/m², Tagesmittelformel mit S₀ = 1361 W/m²): eigene Rechnung im Skript `nachrechnung_ozean_atmosphaere.py`; das Skript rechnet mit 7,572·10¹³ und 1,893·10¹³ m², die Aufgabe mit den gerundeten Flächen der Tabelle (daher Viertel 63,2 statt 63,4 W/m², 21,9 statt rund 22 K und −12,6 statt −12,7 W/m²)
- Albedo im Winter 0,4: Annahme ohne Messzahl (Aufgabenideen, offene Fragen); Teil e prüft 0,3 und 0,5
- Schichtmodell mit ε~A~ = 0,78 und Linearisierung 4σT³: Tutorium 4 (Ideensammlung, Abschnitt 4.4 und Rechenprotokoll); σ = 5,6705·10⁻⁸ W/(m² K⁴) aus Foliensatz 04 (Riese, 2026)
- Januarmittel Paderborn +2,1 °C: WMO-Klimanormalwerte 1991 bis 2020, Station Bad Lippspringe (WMO 10430, DWD 03028): <https://www.nodc.noaa.gov/archive/arc0216/0253808/1.1/data/0-data/Region-6-WMO-Normals-9120/Germany/CSV/Lippspringe-Bad_10430.csv>; DWD-Stationsliste: <https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/multi_annual/mean_91-20/Temperatur_1991-2020_Stationsliste.txt>
- Januarmittel Goose Bay −17,6 °C (53,3° N, 60,4° W): Environment and Climate Change Canada, Klimanormalwerte 1981 bis 2010, Goose Bay A (8501900); die Normalwerte 1991 bis 2020 waren nicht abrufbar: <https://climate.weather.gc.ca/climate_normals/results_1981_2010_e.html?climate_id=8501900&dispBack=1&searchMethod=contains&searchType=stnName&txtCentralLatMin=0&txtCentralLatSec=0&txtCentralLongMin=0&txtCentralLongSec=0&txtStationName=goose>
- Winterbilanz nördlich von 35° N mit 54, 11 und 53 W/m² (Teil f): Seager, R. et al. (2002), Q. J. R. Meteorol. Soc. 128, 2563 bis 2586: <https://doi.org/10.1256/qj.01.128>
- Gegenposition zu Seager und Abnahme des Wärmetransports im Ozean zwischen 25° und 50° N (Hintergrund zu Teil f): Rhines, P. & Häkkinen, S. (2003), ASOF Newsletter 1: <https://usclivar.org/sites/default/files/amoc/Rhines_Hakkinen_2003.pdf>; Rhines, P., Häkkinen, S. & Josey, S. A. (2008), in: Arctic-Subarctic Ocean Fluxes, Springer, 87 bis 109: <https://doi.org/10.1007/978-1-4020-6774-7_5>
- Deckschicht im Winter bis etwa 350 m im nördlichen Nordatlantik (Teil h; die Untergrenze 100 m ist eine Annahme): de Boyer Montégut, C. et al. (2004), J. Geophys. Res. 109, C12003: <https://doi.org/10.1029/2004JC002378>, Volltext: <https://data-ww3.ifremer.fr/BIB/deBoyerMontegut_etalJGR2004.pdf>
- Abschwächung der AMOC bis 2100 (Ausgangssituation, Hintergrund zu Teil i): IPCC (2021), AR6 WG I, Kap. 9 (Fox-Kemper et al.), Abschn. 9.2.3.1, und SPM C.3.4: <https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-9/>
- Kälteextreme in De Bilt nach einem Zusammenbruch der AMOC mit und ohne gleichzeitige Erwärmung (Hintergrund zu Teil i): van Westen, R. M. & Baatsen, M. L. J. (2025), Geophys. Res. Lett. 52, e2025GL114611: <https://doi.org/10.1029/2025GL114611>
- Rechnung: `rechnung/t5_rechnung.py` (Ausgabe `rechnung/t5_rechnung_ausgabe.txt`), nach `nachrechnung_ozean_atmosphaere.py` (Version 3)

**Aufgabe 3: Der Ozean als Wärmespeicher**

- Deckschicht im Mittel 70 m, je nach Region und Jahreszeit 20 bis über 150 m: de Boyer Montégut et al. (2004), wie bei Aufgabe 2
- 91 % der zusätzlichen Energie seit 1971 stecken im Ozean: IPCC (2021), Summary for policymakers, in: Climate change 2021: The physical science basis: <https://www.ipcc.ch/report/ar6/wg1/chapter/summary-for-policymakers/>
- Zusätzliche Strahlungsflussdichte 3,93 W/m² bei Verdopplung von CO₂; α~eff~ = 1,3 W/(m² K) entspricht rund 3 K Erwärmung bei Verdopplung: Forster, P. et al. (2021), The Earth’s energy budget, climate feedbacks, and climate sensitivity, IPCC AR6 WG I, Kap. 7: <https://www.ipcc.ch/report/ar6/wg1/chapter/chapter-7/>
- Wärmeabgabe an die Tiefsee γ = 0,7 W/(m² K) (Arbeitswert der Ideensammlung) und schnelle Zeitkonstante von einigen Jahren in Klimamodellen: Geoffroy, O. et al. (2013), Transient climate response in a two-layer energy-balance model, Part I, J. Climate 26(6), 1841 bis 1857: <https://folk.uib.no/ngfhd/EarthClim/Publications/Papers/Geoffroy_etal_2012b.pdf>; Held, I. M. et al. (2010), J. Climate 23(9), 2418 bis 2427: <https://doi.org/10.1175/2009JCLI3466.1>
- T~e~ = 254,6 K aus Tutorium 4 (S₀ = 1361 W/m², planetare Albedo 0,30): Kopp, G. & Lean, J. L. (2011), Geophys. Res. Lett. 38, L01706: <https://doi.org/10.1029/2010GL045777>; Stephens, G. L. et al. (2015), Rev. Geophys. 53(1), 141 bis 163: <https://doi.org/10.1002/2014RG000449>; Rechnung in `nachrechnung_leitphaenomene.py`
- Wärmeleitfähigkeit 0,6 W/(m K): Arbeitswert für Wasser aus `nachrechnung_leitphaenomene.py` (dort mit 1000 kg/m³ und 4186 J/(kg K): 1083 Jahre; hier mit den Daten von Meerwasser: 1058 Jahre, beides rund 1,1·10³ Jahre)
- Boden 2 m mit 2,2 MJ/(m³ K): Arbeitswert aus `nachrechnung_leitphaenomene.py`, ohne eigene Quelle
- Rechnung: `rechnung/t5_rechnung.py`, nach `nachrechnung_leitphaenomene.py` (Abschnitt T5)

**Aufgabe 4: Sverdrup und der Amazonas**

- Pader rund 4 km lang, über 200 Quellen, im Mittel 5000 l/s: Stadt Paderborn (2014), „Pader erleben“: <https://www.paderborn.de/microsite/Paderborner-Natur/download/Pader-erleben.pdf>; das LUA NRW (2001) nennt rund 3,5 m³/s: <https://luadb.lds.nrw.de/LUA/hygon/docs/lippe.pdf>
- Rhein, Pegel Rees, MQ 2260 m³/s, und Weser, Pegel Intschede, MQ 313 m³/s: Bundesanstalt für Gewässerkunde, Deutsches Gewässerkundliches Jahrbuch: <https://dgj-daten.bafg.de/Rhein/Rees/2790010_WQ.pdf>, <https://dgj-daten.bafg.de/Weser-%20und%20Emsgebiet/Intschede/49100101_WQ.pdf>
- Amazonas 206 000 m³/s: Callède et al. (2010), wie bei Aufgabe 2
- Alle Flüsse der Erde 1,18 Sv (37 288 km³ pro Jahr): Dai, A. & Trenberth, K. E. (2002), J. Hydrometeorol. 3, 660 bis 687: <https://impacts.ucar.edu/en/publications/estimates-of-freshwater-discharge-from-continents-latitudinal-and/>; Dai, A. et al. (2009), J. Climate 22: <https://gmao.gsfc.nasa.gov/gmaoftp/sarith/ROUTING_MODEL/docs/Dai-discharge-JC09.pdf>
- AMOC 17 Sv: Johns et al. (2023), wie bei Aufgabe 2
- Unterlauf 27,5 bis 28,5 °C: Gagne-Maynard, W. C. et al. (2017), Front. Mar. Sci. 4, 26: <https://www.frontiersin.org/articles/10.3389/fmars.2017.00026/pdf>; Flussfahne im Mittel 28,5 °C: Reul, N. et al. (2014), J. Geophys. Res. Oceans: <https://data-ww3.ifremer.fr/BIB/Reul_etal_JGR2014.pdf>
- Becken rund 6 Mio. km², Niederschlag rund 2200 mm pro Jahr: Fassoni-Andrade, A. C. et al. (2021), Rev. Geophys. 59, e2020RG000728: <https://par.nsf.gov/servlets/purl/10330397>
- Verdunstung 1083 ± 37 mm pro Jahr, 2003 bis 2013 (Teil c): Baker, J. C. A. et al. (2021), Hydrol. Earth Syst. Sci. 25, 2279 ff.: <https://hess.copernicus.org/articles/25/2279/2021/>
- Nettostrahlung des Waldes 117 bis 153 W/m², gemessene latente Wärme 81 bis 114 W/m² (Teil d): da Rocha, H. R. et al. (2009), J. Geophys. Res. 114, G00B12: <https://opus.cloud1.lib.uts.edu.au/bitstream/10453/14723/1/2010001591.pdf>
- Tropenwälder kühlen durch Verdunstung (Hintergrund zu Teil d): Bonan, G. B. (2008), Science 320, 1444 ff.: <https://echorock.cgd.ucar.edu/events/20130729/files/Bonan-2008.pdf>
- Verdampfungsenthalpie 2430 kJ/kg bei 30 °C: NIST Chemistry WebBook, Wasser (IAPWS-95): <https://webbook.nist.gov/chemistry/fluid/>
- Energieumsatz der Menschheit rund 19 TW (über 600 EJ im Jahr 2025): Energy Institute (2026), Statistical Review of World Energy: <https://www.energyinst.org/__data/assets/file/0004/1827616/Statistical-Review-of-World-Energy-PDF-Report.pdf>
- „Fliegender Fluss“ mit 10 bis 23 Gt Wasserdampf pro Tag (Ausgangssituation): Arraut, J. M. et al. (2012), J. Climate 25, 543 bis 556: <https://mdsoar.org/items/83c2d5dc-2990-4097-bd0b-7d228303e71e>
- Süßwasser 1000 kg/m³ und 4180 J/(kg K): Arbeitswerte der Aufgabenideen (Stoffwerte von Wasser)
- Rechnung: `rechnung/t5_rechnung.py`, nach `nachrechnung_ozean_atmosphaere.py` (Abschnitt B)

**Zusatzaufgabe 1: Kraftwerk am Fluss**

- 2 GW Abwärme, 200 m³/s und 26 °C im Hitzesommer: Arbeitswerte aus der Ideensammlung, Abschnitt 4.5 (Teil 0, Aufwärmen), nicht durch eine Quelle belegt
- Rechnung: `rechnung/t5_rechnung.py`

**Zusatzaufgabe 2: Eisberg**

- Tafeleisberg 1 km² und 250 m dick, Wasser 2 bis 3 K wärmer, α = 20 bis 50 W/(m² K), Schmelzzeit rund 9 bis 32 Jahre: Arbeitswerte aus der Ideensammlung, Abschnitt 4.5 (Zusatzaufgaben), nicht durch eine Quelle belegt. Tiefgang 224 m aus dem Auftrieb, h~T~ = H ρ~E~/ρ~M~ mit 917 kg/m³ für Eis und 1025 kg/m³ für Meerwasser (wie in Aufgabe 2), 223,7 m gerundet; im Text gegeben. `nachrechnung_leitphaenomene.py` setzte 88 % der Dicke (220 m) an und kam auf 32,2 bzw. 8,6 Jahre, mit 224 m sind es 31,9 bzw. 8,5 Jahre
- Eis 917 kg/m³ und Schmelzenthalpie 333,5 kJ/kg: Arbeitswerte der Ideensammlung (Abschnitt 4.1) und des Pilotblatts zu Tutorium 1
- Zerfall eines Rieseneisbergs (Hintergrund zu Teil c): NASA Earth Observatory (13.04.2026), Megaberg ends its long odyssey at sea (Eisberg A23a): <https://science.nasa.gov/earth/earth-observatory/megaberg-ends-its-long-odyssey-at-sea/>
- Rechnung: `rechnung/t5_rechnung.py`

## Tutorium 6: Wärmebilanzen (stationär differentiell)

**Tutorium 6, Aufgabe 1: Woher kommt die Erdwärme? (Erdkruste)**

- Wärmestromdichte an der Oberfläche 65 mW/m² (Mittel der Kontinente): Pollack, H. N., Hurter, S. J. & Johnson, J. R. (1993), Heat flow from the Earth's interior: Analysis of the global data set, Reviews of Geophysics 31(3), 267 bis 280: <https://doi.org/10.1029/93RG01249>
- Kontinentale Tiefbohrung in der Oberpfalz, 9101 m, rund 265 °C (Ausgangssituation, Teil f): GFZ Helmholtz-Zentrum für Geoforschung (2024), Der Tiefpunkt in Deutschland feierte Jubiläum: <https://www.gfz.de/en/press/news/details/der-tiefpunkt-in-deutschland-feierte-jubilaeum>. Hinweis aus der Faktenprüfung der Ideensammlung (KI-Protokoll): 265 °C ist ein berechneter Gleichgewichtswert, der höchste Messwert ist 256 °C in 9070 m; deshalb steht im Aufgabentext „herrschen rund 265 °C“ und nicht „gemessen“.
- Krustendicke 30 km, Wärmeleitfähigkeit 2,5 W/(m·K), Oberflächentemperatur 10 °C, Wärmeproduktion 1 µW/m³ und 2,5 µW/m³ (Granit): Arbeitswerte der Ideensammlung, Abschnitt 4.6; keine lesbare Quelle gefunden (Ideensammlung, Abschnitt 12.4). Mögliche Quellen, nicht eingesehen: Rudnick & Gao (Treatise on Geochemistry); Hasterok & Webb (2017), Geoscience Frontiers 8; Grad et al. (2009), Geophysical Journal International 176.
- Plausibilität des Profils (nur für die Lösung): mittlerer geothermischer Gradient in Deutschland 3 K je 100 m, Hessisches Landesamt für Naturschutz, Umwelt und Geologie (2017), Leitfaden Erdwärmenutzung in Hessen, S. 7: <https://www.hlnug.de/fileadmin/dokumente/geologie/erdwaerme/Erdwaermeleitfaden_01_2017.pdf> (am 21.10.2026 eingesehen); das Profil der Aufgabe hat an der Oberfläche 2,6 K je 100 m.
- Energiebilanz am Volumenelement mit Quelle, Taylor-Reihe, Lösung durch Trennung der Variablen und direkte Integration, Randbedingungen nach Dirichlet, von Neumann und gemischt: Riese, J. (2026), Wärmeübertragung, Foliensätze 02 (F. 21 bis 30) und 05 (F. 17 bis 21 und 31 bis 40), Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn
- Rechnung: `rechnung/t6_rechnung.py` (Ausgabe `rechnung/t6_rechnung_ausgabe.txt`), nachgebaut nach `nachrechnung_leitphaenomene.py`, Abschnitt T6

**Tutorium 6, Aufgabe 2: Erde als Kugel**

- Wärmestrom aus dem Erdinneren 47 TW (Ausgangssituation, Tabelle): Davies, J. H. & Davies, D. R. (2010), Earth's surface heat flux, Solid Earth 1, 5 bis 24: <https://doi.org/10.5194/se-1-5-2010>
- Nur etwa die Hälfte davon ist radioaktive Wärme (Uran und Thorium rund 20 TW, mit Kalium rund die Hälfte von 44 TW; für die Lösung von Teil e): Gando, A. et al. (KamLAND Collaboration) (2011), Partial radiogenic heat model for Earth revealed by geoneutrino measurements, Nature Geoscience 4, 647 bis 651: <https://doi.org/10.1038/ngeo1205>
- Temperatur am inneren Kern rund 6000 °C (Teil e): ESRF (25.04.2013), Earth's centre is hotter than previously thought, Pressemitteilung zu Anzellini et al. (2013), Science 340, 464 bis 466: <https://www.esrf.fr/news/general/Earth-Center-Hotter>
- Erdradius 6371 km: mittlerer Erdradius wie in `nachrechnung_leitphaenomene.py`
- Absorbierte Sonnenstrahlung 238 W/m² = S₀(1 − ρ~p~)/4 mit S₀ = 1361 W/m² und ρ~p~ = 0,30 wie in Tutorium 4: Kopp, G. & Lean, J. L. (2011), A new, lower value of total solar irradiance: Evidence and climate significance, Geophysical Research Letters 38, L01706: <https://doi.org/10.1029/2010GL045777>; Stephens, G. L. et al. (2015), The albedo of Earth, Reviews of Geophysics 53(1), 141 bis 163: <https://doi.org/10.1002/2014RG000449>
- Wärmeleitfähigkeit der Kugel 3 bis 4 W/(m·K): Arbeitswert der Ideensammlung (Abschnitt 4.6 und Anhang A), ohne eigene Quelle

**Tutorium 6, Zusatzaufgabe 1: Wie warm wäre die Erde ohne Sonne?**

- Stefan-Boltzmann-Konstante σ = 5,6705·10⁻⁸ W/(m²·K⁴): Riese, J. (2026), Foliensatz 04, F. 10
- 92 mW/m² aus 47 TW (Davies & Davies, 2010, s. o.); 87 mW/m² gehört zu 44,2 TW (Pollack et al., 1993, s. o.); beide Werte nicht mischen (KI-Protokoll der Ideensammlung)

## Tutorium 7: Wärmebilanzen (instationär differentiell)

**Tutorium 7, Aufgabe 1: Das Gedächtnis des Bodens**

- Temperaturleitfähigkeit des feuchten Bodens a = 5·10⁻⁷ m²/s: Arbeitswert der Ideensammlung (Abschnitt 4.7) in der Spanne für schweren Ton mit 15 % Wasser, 0,042 bis 0,061 m²/Tag (4,9 bis 7,1·10⁻⁷ m²/s), Wärmeleitfähigkeit 1,4 bis 1,9 W/(m·K): ASHRAE (2000), Thermal properties of selected soil, zitiert in Sobti, J. & Singh, S. K. (2015), Earth-air heat exchanger as a green retrofit for Chandīgarh: a critical review, Geothermal Energy 3, 14, Tabelle 1: <https://geothermal-energy-journal.springeropen.com/articles/10.1186/s40517-015-0034-4/tables/1> (am 21.10.2026 eingesehen; Titel ergänzt). Die ASHRAE-Tabelle ist nur über diese Sekundärquelle geprüft.
- Temperaturleitfähigkeit von Gestein a~G~ = 1·10⁻⁶ m²/s (Bohrloch, Teil i): Arbeitswert der Ideensammlung; dieselbe Tabelle nennt für Granit 0,084 bis 0,13 m²/Tag (1,0 bis 1,5·10⁻⁶ m²/s)
- Amplitude des Jahresgangs 10 K; Permafrost mit Jahresmittel −8 °C, Amplitude 15 K und Erwärmung um 3 K; Kälteperiode 14 Tage: Arbeitswerte der Ideensammlung, ohne eigene Quelle
- Stündliche Bodentemperaturen in Bad Lippspringe (Station 03028) in mehreren Tiefen bis 50 cm (Ausgangssituation, Teil e): Deutscher Wetterdienst (2026), Climate Data Center: <https://opendata.dwd.de/climate_environment/CDC/observations_germany/climate/hourly/soil_temperature/>. Faktenprüfung der Ideensammlung (KI-Protokoll): stündlich 2, 5, 10, 20, 50 und 100 cm, täglich nur bis 50 cm, Stundenwerte seit 1981; 100 cm für diese Station nicht geprüft, deshalb im Text „bis 50 cm“. Die Messwerte selbst sind nicht geladen.
- Erwärmung der Oberfläche über Permafrost in Alaska um 2 bis 4 K innerhalb von Jahrzehnten bis einem Jahrhundert, aus Bohrlochtemperaturen (Ausgangssituation, Teil i): Lachenbruch, A. H. & Marshall, B. V. (1986), Changing climate: Geothermal evidence from permafrost in the Alaskan Arctic, Science 234, 689 bis 696: <https://doi.org/10.1126/science.234.4777.689>
- „In etwa zehn Metern Tiefe schwankt die Temperatur übers Jahr kaum noch“ und „in 3 m Tiefe am wärmsten im Herbst“: eigene Rechnung (Ideensammlung, Abschnitt 4.7; Teil e und f)
- Gegebene Lösung der Temperaturwelle und Eindringtiefe √(a·t): Holman, J. P. (2010), Heat transfer, 10. Aufl., McGraw-Hill, Abschnitt 4-3 sowie Aufgaben 4-18 und 4-19 (nicht in den Folien und nicht in der Formelsammlung; Rücksprache mit der Professorin laut Ideensammlung, Abschnitt 10, noch offen)
- Wärmeleitungsgleichung, Temperaturleitfähigkeit, Anfangs- und Randbedingungen: Riese, J. (2026), Wärmeübertragung, Foliensatz 02, F. 21 bis 30, Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn
- Frostfreie Gründungstiefe (häufig etwa 0,8 m, für die Lösung von Teil g): Norm nicht eingesehen (DIN 1054 mit DIN EN 1997-1/NA); deshalb ohne Zahl im Aufgabentext
- Rechnung: `rechnung/t7_rechnung.py` (Ausgabe `rechnung/t7_rechnung_ausgabe.txt`), nachgebaut nach `nachrechnung_leitphaenomene.py`, Abschnitt T7

**Tutorium 7, Frage 3: Temperaturleitfähigkeit vergleichen**

- Kupfer (Cu-OF): Dichte 8,94 g/cm³, Wärmeleitfähigkeit bei 20 °C 394 W/(m·K), spezifische Wärmekapazität bei 20 °C 386 J/(kg·K): Lamineries Matthey (Notz Metall AG), Werkstoffdatenblatt Cu-OF: <https://www.matthey.ch/fileadmin/user_upload/downloads/fichetechnique/DE/Cu-OF_v26D.pdf> (am 21.10.2026 eingesehen); Gegenprobe für Dichte und Wärmeleitfähigkeit: Aurubis, Werkstoff-Datenblatt Cu-OF (DE_2024_06): <https://www.aurubis.com/dam/jcr:726de301-1eb9-48cb-a2cf-09490c19fad0/PNA%20400_Cu-OF_C10200-DE%20(1).pdf>
- Wasser und Luft bei 20 °C und 1,01325 bar: berechnet mit CoolProp 8.0 in `rechnung/t7_rechnung.py`; Bell, I. H., Wronski, J., Quoilin, S. & Lemort, V. (2014), Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp, Industrial & Engineering Chemistry Research 53(6), 2498 bis 2508: <https://doi.org/10.1021/ie4033999>
- Granit und feuchter Ton (schwerer Ton, 15 % Wasser): ASHRAE (2000) über Sobti & Singh (2015), Tabelle 1 (s. o.)
- Größenordnungen der Temperaturleitfähigkeit (Flüssigkeiten etwa 0,1·10⁻⁶ m²/s, Metalle und Gase 3 bis 100·10⁻⁶ m²/s): Riese, J. (2026), Foliensatz 02, F. 26

**Tutorium 7, Zusatzaufgabe 1: Lord Kelvin und das Alter der Erde**

- Kelvins Abschätzung von rund 100 Millionen Jahren (96 Millionen Jahre, Grenzen 24 bis 400 Millionen Jahre): England, P., Molnar, P. & Richter, F. (2007), John Perry's neglected critique of Kelvin's age for the Earth: A missed opportunity in geodynamics, GSA Today 17(1), 4 bis 9: <https://doi.org/10.1130/GSAT01701A.1>. Eingangswerte 3870 °C (7000 °F), 36,5 K/km und a = 1,18·10⁻⁶ m²/s wie in der Nachrechnung der Ideensammlung (`nachrechnung_leitphaenomene.py`, Abschnitt T7); der Artikel konnte am 21.10.2026 nicht erneut gelesen werden (Abruf abgelehnt, HTTP 429), in der Ideensammlung ist er als im Volltext geprüft vermerkt.
- Lösung für den halbunendlichen Körper mit plötzlich geänderter Oberflächentemperatur (Gradient an der Oberfläche): Holman (2010), Abschnitt 4-3 (s. o.)
- Erdradius R = 6371 km (Teil b): mittlerer Erdradius wie in Tutorium 6
- Alter der Erde rund 4,5 Milliarden Jahre: Allgemeinwissen, nicht eigens belegt

## Tutorium 8: Wärmeübertrager und Verdampfer

**Quellen zu Tutorium 8: Wärmeübertrager und Verdampfer**

Stand 21.10.2026. Übernommen aus den Quellenverzeichnissen der Ausgangsdokumente: Ideensammlung „Leitaufgaben aus Klima und Erde“ (Abschnitt 4.8 und 12) und „Aufgabenideen: Meeresströmungen, Sverdrup und Luftströmungen“ (Aufgabe C, Abschnitt Quellen). In Klammern steht, wie die Angabe dort geprüft wurde. Alle Zahlen der Ergebniszeilen rechnet `rechnung/t8_rechnung.py` nach (Ausgabe `rechnung/t8_rechnung_ausgabe.txt`).

**Für alle Aufgaben**

- Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* (Vorlesungsfolien). Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn, SoSe 2026. Genutzt: V06 F. 23 bis 28 (Bilanz beider Ströme, mittlere logarithmische Temperaturdifferenz), F. 35 bis 41 (ε-NTU-Konzept, Grenzfälle *C*\* = 1 und *C*\* = 0), V07 F. 3 (Temperaturverläufe bei Kondensation und Verdampfung).
- Lehrstuhl für Fluidverfahrenstechnik (2026). *Formelsammlung Wärmeübertragung* (Stand SoSe 2026): *Re* und Gültigkeitsbereiche der Rohrströmung (laminar, Übergangsbereich, turbulent). Die Beziehungen für Δ*T*~ln~ und das ε-NTU-Konzept stehen nicht in der Formelsammlung, sondern nur in V06. Die Carnot-Leistungszahl der Wärmepumpe (Teil g) steht weder in der Formelsammlung noch in den Foliensätzen 01 bis 08 (Vorwissen aus der Thermodynamik; Textfassungen am 21.10.2026 durchsucht); im Aufgabentext steht sie deshalb unter der Tabelle als gegeben.

**Aufgabe 1: Wärme aus dem Boden (Sole-Wasser-Wärmepumpe)**

- Bodentemperatur rund 11 °C in 100 m Tiefe (Arbeitswert): Hessisches Landesamt für Naturschutz, Umwelt und Geologie (2017). *Leitfaden Erdwärmenutzung in Hessen*: ab etwa 10 m Tiefe 8 bis 10 °C, darunter rund 3 K je 100 m wärmer. <https://www.hlnug.de/fileadmin/dokumente/geologie/erdwaerme/Erdwaermeleitfaden_01_2017.pdf> (Volltext). Eine regionale Quelle für Paderborn ist noch offen (Ideensammlung 4.8, „Offen“).
- Jahresarbeitszahl 4,3 erdgekoppelter Wärmepumpen in Bestandsgebäuden: Fraunhofer ISE (2025). *Wärmepumpen heizen auch im Altbau klimafreundlich* (Presseinformation 30/2025). <https://www.ise.fraunhofer.de/content/dam/ise/de/documents/presseinformationen/2025/3025_ISE_PI_Waermepumpen-heizen-auch-im-Altbau-klimafreundlich.pdf> (Pressemitteilung)
- Entzugsleistung 60 W/m für normales Festgestein bei 1800 Betriebsstunden im Jahr: VDI 4640 Blatt 2 (2001). *Thermische Nutzung des Untergrunds: Erdgekoppelte Wärmepumpenanlagen*, zitiert nach 42watt. <https://42watt.de/magazin/entzugsleistung-warmepumpe> (Sekundärquelle; die Ausgabe 2019 arbeitet mit Tabellen nach *λ* und Volllaststunden, Original noch nicht eingesehen)
- Wärmestromdichte aus dem Erdinneren 65 mW/m² (Mittel der Kontinente): Pollack, H. N., Hurter, S. J., & Johnson, J. R. (1993). Heat flow from the Earth’s interior: Analysis of the global data set. *Reviews of Geophysics, 31*(3), 267 bis 280. <https://doi.org/10.1029/93RG01249> (Volltext)
- CO₂ je kWh Strom 344 g (Strommix 2025, ohne Vorketten): Umweltbundesamt (2026, 23. März). *CO₂-Emissionen pro Kilowattstunde Strom 2025*. <https://www.umweltbundesamt.de/themen/co2-emissionen-pro-kilowattstunde-strom-2025-nur> (Volltext)
- CO₂ je kWh Erdgas 202 g (Brennstoff, ohne Vorketten): Umweltbundesamt (2024). *Entwicklung der spezifischen Treibhausgas-Emissionen des deutschen Strommix* (Climate Change 23/2024), Tabelle 4. <https://www.umweltbundesamt.de/sites/default/files/medien/11850/publikationen/23_2024_cc_strommix_11_2024.pdf> (Volltext)
- Arbeitswerte ohne eigene Quelle (aus der Ideensammlung 4.8 übernommen): Sondenlänge 100 m, Heizleistung 8 kW, Leistungszahl 4, Sole (Wasser-Glykol) mit *c*~p~ = 3,8 kJ/(kg K), *ρ* = 1040 kg/m³ und *ν* = 4 · 10⁻⁶ m²/s, Sole von −1 auf 2 °C, Verdampfung bei −6 °C, Kondensation bei 40 °C, Rohrinnendurchmesser 26 mm, *k* = 1000 bis 2000 W/(m² K) im Verdampfer, Wirkungsgrad der Gasheizung 0,95.
- Eigene Rechnung: Ideensammlung, Anhang A und Skript `nachrechnung_leitphaenomene.py` (Abschnitt T8); hier nachgebaut in `rechnung/t8_rechnung.py`. Neu gegenüber dem Ausgangsskript: Soletemperatur am tiefsten Punkt der Sonde (nach dem halben Strömungsweg).

**Aufgabe 2: Wer bringt die Wärme zum Pol, Luft oder Wasser?**

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

**Zusatzaufgabe 1: Gegenstrom im Entenfuß**

- Stockenten verlieren in 0 bis 20 °C kaltem Wasser nur 3 bis 7 % ihrer Stoffwechselwärme über die Füße: Kilgore, D. L., & Schmidt-Nielsen, K. (1975). Heat loss from ducks’ feet immersed in cold water. *The Condor, 77*(4), 475 bis 478. <https://digitalcommons.usf.edu/condor/vol77/iss4/13> (Volltext)
- Effektivität für *C*\* = 1 im Gegen- und Gleichstrom: V06 F. 41.
- *NTU* = 4 ist ein gewählter Arbeitswert ohne Quelle (siehe Bericht).

**Zusatzaufgabe 2: Der Rekordflug**

- Rekordflug am 9. Februar 2020 in 4 h 56 min, Jetstream über dem Sturm Ciara, rund 150 mph (67 m/s) Rückenwind nach Flightradar24, Jetstream 260 mph nach BBC Weather: NPR (9.2.2020), <https://www.npr.org/2020/02/09/804266975/british-airways-sets-speed-record-crossing-the-atlantic-in-under-5-hours> ; CILT UK (2020), <https://ciltuk.org.uk/News/Latest-News/ArtMID/6887/ArticleID/25239/Storm-Ciara-helps-plane-beat-transatlantic-flight-record>
- Reiseflug mit Mach 0,85: Boeing, *747-400 Airplane Characteristics for Airport Planning*, Rev. F, Abschn. 3.2.1. <https://www.boeing.com/content/dam/boeing/boeingdotcom/commercial/airports/acaps/747-400_Rev_F.pdf>
- Eigene Rechnung (Skript `nachrechnung_ozean_atmosphaere.py`): Großkreis JFK nach LHR 5540 km; Schallgeschwindigkeit in 10,7 km nach der Normatmosphäre 296,5 m/s, also 252 m/s bei Mach 0,85.
