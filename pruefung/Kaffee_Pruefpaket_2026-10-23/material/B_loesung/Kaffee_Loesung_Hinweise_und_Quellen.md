> Auszug aus der Lösung der Kaffee-Aufgabe: Hinweise für die Tutoriumsleitung und Quellen der Arbeitswerte.

**[Hinweise für die Tutoriumsleitung]{.underline}**

- *Typische Fehler:* Mischtemperatur nach dem Volumen statt nach $m\,c_p$ gewichtet; in Tasse 1 nur mit $m_K c_{p,K}$ gerechnet; in Tasse 2 schon während der 60 Minuten mit $m_K c_{p,K} + m_M c_{p,M}$ gerechnet; in f) das alte $kA$ weiterverwendet (dann 39,1 und 36,1 °C: Aussage gleich, aber nicht mehr passend zur Messung).
- *Fehlvorstellungen:* „Energieerhaltung, also egal“: Erhalten bleibt die Energie von Kaffee, Milch und Umgebung zusammen, nicht die des Tasseninhalts (Teil e). „Schaum ist kälter als der Kaffee, wirkt also wie kalte Milch“: Entscheidend ist nicht der Vergleich mit dem Kaffee, sondern ob die Milch wärmer als der Kipppunkt aus h ist.
- *Was die Rechnung weglässt:* Bei hoher Temperatur trägt die Verdunstung rund die Hälfte der Wärmeabgabe (Condoret 2007, Tab. 2), deshalb ist $kA$ in Wirklichkeit nicht konstant. Mit einer überlinearen Wärmeabgabe $\dot{Q}_{ab} \propto (T - T_u)^{4/3}$, angepasst an dieselbe Messung, ergeben sich $\vartheta_1 = 37{,}65\,\mathrm{°C}$ und $\vartheta_2 = 33{,}34\,\mathrm{°C}$, also 4,31 K statt 3,85 K: Der Vorsprung der heißeren Tasse 2 beim Wärmeverlust wächst.
- *Zum Weiterdenken:* Hätte die Milch in beiden Tassen Raumtemperatur, wäre der Unterschied mit 2,5 K kleiner, aber vorhanden. Der schwarze Kaffee ist bis etwa 56 min heißer als das Gemisch in Tasse 1 (Abb. L2) und verliert deshalb mehr Wärme; erst die kalte Milch am Ende macht Tasse 2 deutlich kühler.
- *Versuch:* Mit echten, vorgewärmten Bechern sind nach 60 Minuten zwischen Becher 1 und 2 rund 3 K Unterschied zu erwarten (nach 30 Minuten schon gut 2,5 K), mit einem Küchenthermometer gut messbar; Becher 3 (Milch draußen) bleibt um mindestens 1,6 K kühler als Becher 1. Starttemperatur messen statt 80 °C annehmen, ein Thermometer für alle Becher verwenden, vor jeder Messung umrühren. Heißes Wasser verhält sich wie Kaffee; Verbrühungsgefahr beachten.

```{=latex}
\needspace{7\baselineskip}
```

**[Quellen der Arbeitswerte]{.underline}**

- Kaffee: Ausschank 71 bis 85 °C (Brown & Diller 2008, Burns 34, 648); beim Eingießen 2 bis 5 K weniger (Abraham & Diller 2019, J. Food Sci. 84); Stoffwerte wie Wasser (SCA, Gehalt an gelösten Stoffen 1,15 bis 1,35 %).
- Milch: Kühlschrank höchstens 7 °C, besser unter 5 °C (Bundesinstitut für Risikobewertung, 2023); im Mittel 31 g Milch je Tasse (FSANZ 2011); Dichte 1027 bis 1033 kg/m³ (Goff, Dairy Science and Technology); $c_p$ wie in Tutorium 8.
- Abkühlung: offener, nicht umgerührter Keramikbecher, $\tau \approx 41\,\mathrm{min}$ aus der Steigung 0,0241 1/min in Abb. 6 (Ferreira 2025, Phys. Educ. 60, 035001); Verdunstung bei 79 °C 12,0 von 22,7 W (Condoret 2007, Chem. Eng. Educ. 41, 137, Tab. 2).
- Milchschaum 55 bis 65 °C (Thermoplan, Coffee knowledge: milk); Keramikbecher 300 g mit 0,85 kJ/(kg·K) als Arbeitswert (Schätzung).
- Rechenskript: nachrechnung_kaffee.py mit kaffee_modell.py.

