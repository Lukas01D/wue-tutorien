# Änderung der Kaffee-Simulation vom 11.11.2026

Auftrag der TL: „dem simulationstool bitte hinzufügen, dass die milchtemperatur bis 95 grad hochgehen kann und es physikalisch alles noch sinn macht“ und schlanke Varianten A und B (siehe `minimal/LIESMICH.md`).

| Bereich | Änderung |
|:--|:--|
| Regler Milchtemperatur | bis 95 °C (vorher 80 °C), Marken 2, 20, 40, 60, 80, 95; die Sperre bei 30 °C bis Auftrag 3 bleibt |
| Diagramm | Ist die Milch wärmer als der Kaffee, steigt die Temperatur beim Zugießen: Linie und Pfeil zeigen dann nach oben; die y-Achse reicht bis über die Temperatur nach der Zugabe |
| Bildbeschreibung DE und EN | „fällt“ oder „steigt“ (EN „drops“ oder „raises“) je nach Richtung |
| Hinweis unter dem Regler ab 40 °C | „Warme Milch: Die Seite nimmt an, dass sie ihre Temperatur bis zur Zugabe hält (frisch erwärmt, wie in Teil g). Ist sie wärmer als der Kaffee, steigt die Temperatur beim Zugießen.“ (EN entsprechend) |
| Beschriftung „Tasse 1: Milch sofort“ | endet vor der Zugabe, damit sie den Endpunkt von Tasse 2 nicht verdeckt |
| Rechenkern | unverändert |

Physikalische Prüfung: Das Modell bleibt bis 95 °C gültig (Wasser und Milch flüssig, Stoffdaten konstant wie im Blatt). Die Energiebilanz ergibt immer Q₂ − Q₁ = C_G (ϑ1 − ϑ2); bei heißer Milch ist Q1 größer als Q2 und Tasse 2 wärmer. Beispiel 95 °C, 100 ml, 45 min: Tasse 1 nach dem Zugießen 84,90 °C, nach 45 min 62,07 °C; Tasse 2 65,72 °C; Unterschied −3,65 K; Q1 28,35 kJ, Q2 23,82 kJ, Q₂ − Q₁ = −4,54 kJ = 1241,8 J/K · (−3,65 K). Milch 70 °C: Tasse 2 0,78 K wärmer (wie Blatt, Teil g). Annahme wie in Teil g: Die warme Milch behält ihre Temperatur bis zur Zugabe.

Tests: Rechenkern 34 von 34, Texte 16 von 16, Browser 107 von 107, schlanke Varianten 49 von 49 bestanden; Bildschirmfotos neu.
