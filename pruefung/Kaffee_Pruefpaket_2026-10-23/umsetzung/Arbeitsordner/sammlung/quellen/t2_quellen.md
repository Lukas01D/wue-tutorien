# Quellen Tutorium 2: Konvektion

Quellen der Arbeitswerte und Fakten in `teile/t2.md`, übernommen aus den Quellenverzeichnissen der Ausgangsdokumente (Ideensammlung „Leitaufgaben aus Klima und Erde“ vom 17.10.2026, Abschnitt 12; Nachrechnung `nachrechnung_leitphaenomene.py`). In Klammern steht, wo der Wert oder Fakt vorkommt. Zahlen: `rechnung/t2_rechnung.py`.

## Aufgabe 1: Offene Rinnen im Meereis

- **Rinnen bedecken im Winter nur 1 bis 2 % der zentralen Arktis, liefern aber über 70 % des Wärmestroms vom Ozean nach oben; schmale Rinnen geben pro Fläche mehr Wärme ab als breite** (Ausgangssituation, Teil f und i): Marcq, S., & Weiss, J. (2012). Influence of sea ice lead-width distribution on turbulent heat transfer between the ocean and the atmosphere. *The Cryosphere, 6*, 143 bis 156. <https://doi.org/10.5194/tc-6-143-2012>
- **Seerauch über offenem Wasser** (Ausgangssituation, Teil h): Ideensammlung, Abschnitt 4.2, Einstieg (qualitativ, ohne Zahl).
- **Luft −30 °C, Wasser −1,8 °C, Wind 8 m/s, Rinne 10 m breit und 1 km lang, Vergleichsbreiten 1 m und 100 m** (Ausgangssituation, Tabelle): Arbeitswerte der Ideensammlung, Abschnitt 4.2 (Aufgabenskizze und Kernzahlen) und Anhang A; Rechnung wie in `nachrechnung_leitphaenomene.py`, Abschnitt T2.
- **Stoffwerte der Luft bei der Filmtemperatur −15,9 °C** (Tabelle: λ, ν, Pr) und **bei −10 °C** (Zusatzaufgabe 1): CoolProp 8.0, Pseudo-Reinstoff Luft, p = 1,01325 bar, wie in der Nachrechnung. Zustandsgleichung nach Lemmon et al. (2000), Viskosität und Wärmeleitfähigkeit nach Lemmon & Jacobsen (2004) (Literaturangaben laut CoolProp-Bibliothek):
  - Lemmon, E. W., Jacobsen, R. T., Penoncello, S. G., & Friend, D. G. (2000). Thermodynamic properties of air and mixtures of nitrogen, argon, and oxygen from 60 to 2000 K at pressures to 2000 MPa. *Journal of Physical and Chemical Reference Data, 29*(3), 331 bis 385. <https://doi.org/10.1063/1.1285884>
  - Lemmon, E. W., & Jacobsen, R. T. (2004). Viscosity and thermal conductivity equations for nitrogen, oxygen, argon, and air. *International Journal of Thermophysics, 25*(1), 21 bis 69. <https://doi.org/10.1023/B:IJOT.0000022327.04529.f3>
  - Bell, I. H., Wronski, J., Quoilin, S., & Lemort, V. (2014). Pure and pseudo-pure fluid thermophysical property evaluation and the open-source thermophysical property library CoolProp. *Industrial & Engineering Chemistry Research, 53*(6), 2498 bis 2508. <https://doi.org/10.1021/ie4033999>
- **Korrelationen und charakteristische Längen** (Teil c bis g, Frage 3, Zusatzaufgabe 1): Lehrstuhl für Fluidverfahrenstechnik. (2026). *Formelsammlung Wärmeübertragung* (Stand SoSe 2026) und Zusatzblatt *Charakteristische Längen*. Universität Paderborn. Verwendet: längs angeströmte Platte (turbulent, 5·10⁵ < Re < 10⁷), waagerechte Platte bei freier Konvektion mit β = 1/T~u~ und L = A/U, quer angeströmter Zylinder (Übergangsbereich, L = πd/2).
- **Grenzschichten, lokales und mittleres α, typische Größenordnungen von α, Biot- und Nußelt-Zahl** (Teil a, b, h; Frage 4): Riese, J. (2026). *Wärmeübertragung: Foliensätze 01 bis 08* \[Vorlesungsfolien\], V03 F. 9 bis 19 und F. 21 bis 36. Lehrstuhl für Fluidverfahrenstechnik, Universität Paderborn.

## Zusatzaufgabe 1: Windchill

- **Windchill-Temperatur in Nordamerika seit 2001, Gesicht als quer angeströmter Zylinder**: Osczevski, R., & Bluestein, M. (2005). The new wind chill equivalent temperature chart. *Bulletin of the American Meteorological Society, 86*(10), 1453 bis 1458. <https://journals.ametsoc.org/view/journals/bams/86/10/bams-86-10-1453.xml>
- **Finger d = 2 cm, Kopf d = 18 cm, Wind 5 m/s (α ≈ 69 und 33 W/(m² K)); Kopf bei 0,5 m/s; Luft −10 °C**: Arbeitswerte der Ideensammlung, Abschnitt 4.2 (Zusatzaufgaben), gerechnet wie in `nachrechnung_leitphaenomene.py` (Stoffwerte der Luft bei −10 °C).

## Herkunft der Fragen

- Frage 1 (Vorab-Frage 1 m oder 100 m breite Rinne), Frage 2 (Frei oder erzwungen?, acht Situationen), Frage 3 (Charakteristische Länge) und Frage 4 (Biot oder Nußelt?): Ideensammlung, Abschnitt 4.2 (Vorab-Frage und Zusatzaufgaben).
