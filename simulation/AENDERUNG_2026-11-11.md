# Änderung der Kaffee-Simulation vom 11.11.2026

Auftrag der TL: „dem simulationstool bitte hinzufügen, dass die milchtemperatur bis 95 grad hochgehen kann und es physikalisch alles noch sinn macht“ und eine schlanke Seite ohne Fragen (siehe `minimal/LIESMICH.md`).

| Bereich | Änderung |
|:--|:--|
| Regler Milchtemperatur | bis 95 °C (vorher 80 °C), Marken 2, 25, 50, 75, 95; die Sperre bei 30 °C bis Auftrag 3 bleibt |
| Diagramm | Ist die Milch wärmer als der Kaffee, steigt die Temperatur beim Zugießen: Linie und Pfeil zeigen dann nach oben; die y-Achse reicht bis über die Temperatur nach der Zugabe |
| Bildbeschreibung DE und EN | „fällt“ oder „steigt“ (EN „drops“ oder „raises“) je nach Richtung |
| Hinweis unter dem Regler ab 40 °C | zuerst ergänzt, auf Wunsch der TL wieder entfernt (zu viel Text) |
| Beschriftung „Tasse 1: Milch sofort“ | endet vor der Zugabe, damit sie den Endpunkt von Tasse 2 nicht verdeckt |
| Rechenkern | unverändert |

Physikalische Prüfung: Das Modell bleibt bis 95 °C gültig (Wasser und Milch flüssig, Stoffdaten konstant wie im Blatt). Die Energiebilanz ergibt immer Q₂ − Q₁ = C_G (ϑ1 − ϑ2); bei heißer Milch ist Q1 größer als Q2 und Tasse 2 wärmer. Beispiel 95 °C, 100 ml, 45 min: Tasse 1 nach dem Zugießen 84,90 °C, nach 45 min 62,07 °C; Tasse 2 65,72 °C; Unterschied −3,65 K; Q1 28,35 kJ, Q2 23,82 kJ, Q₂ − Q₁ = −4,54 kJ = 1241,8 J/K · (−3,65 K). Milch 70 °C: Tasse 2 0,78 K wärmer (wie Blatt, Teil g). Annahme wie in Teil g: Die warme Milch behält ihre Temperatur bis zur Zugabe.

Schlanke Seite: Der erste Entwurf (Varianten A und B mit eigener Optik) ist ersetzt. Auf Wunsch der TL hat die schlanke Seite jetzt genau den Stil der Hauptseite (gleiche Stildatei, gleiche Bausteine für Regler, Diagramm, Kasten und Säulen), keinen Lagetext, den Kasten mit den Endwerten oben und den Zeitregler mit „Abspielen“.

Nachtrag 15:18 (Wünsche der TL): Kasten „Tasse 1 (Milch zu Beginn)“, „Tasse 2 (Milch am Ende)“, „Temperaturdifferenz“; Zeit $t$ bis 180 min unabhängig von der Zugabe, Zugabe höchstens $t$, Tasse 2 kühlt nach der Milch weiter ab; alle Regler ohne Ausklappen in einem Raster; Zusammenfassung „Ausgangswerte des Blatts“ und Hinweis zur warmen Milch entfernt (auch auf der Hauptseite); neue Regler Kaffeemenge und Wärmekapazität der Tasse. Auftrag für Alltagsvergleiche: `minimal/AUFTRAG_Vergleichswerte.md`.

Nachtrag 15:28: „Abspielen“ und „Werte des Blatts“ rechts unter den Säulen; Regler kompakter (Knöpfe und Felder 36 px, engere Abstände). Bei 1366 × 768 und 1280 × 720 sind Diagramm, Säulen und alle neun Regler ohne Bildlauf zu sehen. Knopf „Werte des Blatts“ heißt auf der schlanken Seite „Standardwerte“ (EN „Default values“).

Nachtrag 15:30: Zeitangabe im Kasten kräftiger (auch auf dem Handy); Tasse 1 hellbraun, Tasse 2 dunkelbraun und durchgezogen (Säule 2 voll statt schraffiert); Temperaturdifferenz und Q₂ − Q₁ rotorange (15:33), Temperaturen im Kasten in der Farbe der Tasse. Kontraste: Linie und große Zahl Tasse 1 3,4, sonst mindestens 5,0.

Tests: Rechenkern 34 von 34, Texte 16 von 16, Browser 107 von 107, schlanke Seite 41 von 41 bestanden; Bildschirmfotos neu.
