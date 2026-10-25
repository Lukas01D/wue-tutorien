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
