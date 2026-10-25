# Strukturvorlage: Aufgaben im Stil des Lehrstuhls

> Abgeleitet am 21.10.2026 aus den Übungen 1 bis 9 (SoSe 2026, mit Kurzlösung und Lösung), den Tutorien 1 bis 8 (mit Lösung) und den handschriftlichen Vorlesungsbeispielen 1 bis 9. Vorbilder laut Tutoriumsleitung: Tutorium 3, Aufgabe 3 (Fußbodenheizung, Klausur 2022-02-17) und Tutorium 6, Aufgabe 1 (Nikolaus am Nordpol, Klausur 2017-08-09). Ergänzt am 21.10.2026 nachmittags nach der Rückmeldung der Tutoriumsleitung: Ausgangssituation mit Skizze ganz am Anfang. Erstellt mit KI-Unterstützung (Claude), zur Orientierung für neue Aufgaben.

## Aufgabenblock (Tutoriumsformat)

Reihenfolge: **Ausgangssituation → Frage(n) → Aufgabe.**

1. **Kopf:** „Tutorium N: Thema“ zentriert und fett.
2. **Ausgangssituation (neu, entschieden am 21.10.2026):** ganz am Anfang ein entspannter, anschaulicher Text mit **Skizze**, damit sich die Studierenden in die Situation hineindenken können. Präsens, Sie-Form, Alltagsbezug oder ein überraschender Fakt; bei großen Aufgaben 60 bis 150 Wörter, sonst 30 bis 90. Ein bis drei Fakten, deren Zahl später in der Rechnung oder einem Vergleich vorkommt. Keine Formeln, keine Quellen im Text. Die Skizze zeigt die Situation und die Größen, aber keine Lösung; Unterschrift „**Abb. 1:** …“.
3. **Frage n:** zuerst die Vorab-Frage zur Ausgangssituation („Notieren Sie Ihre Vermutung, bevor Sie Aufgabe 1 rechnen.“), danach höchstens drei kurze Konzeptfragen (zuordnen, ankreuzen, Profile lesen).
4. **Aufgabe n** (Klausur JJJJ-MM-TT oder „neu“), dann:
   - optional ein Satz Überleitung (z. B. eine Messung, die zur Situation gehört);
   - **Annahmen:** als kurze Liste („… wird als ideal durchmischt angenommen.“, „… können vernachlässigt werden.“);
   - ***Gegebene Größen:*** als Tabelle, nach Objekt gruppiert („Kaffee“, „Milch“, „Umgebung“, „Messung“), je Zeile „Bezeichnung: Symbol = Wert“;
   - **Aufgabenstellung:** Teile a), b), c) … im Imperativ mit „Sie“, höchstens neun; das **Ergebnis** steht ohne Label am Ende jedes rechnenden Teils (im Klausurformat stattdessen „Ersatzergebnis“).
5. **Aufbau der Teile:** einfache Größe (α, k oder eine Mischtemperatur) → Bilanz und Differentialgleichung → Lösung mit Anfangsbedingung (Temperatur zu einer Zeit oder Zeit bis zu einer Temperatur) → Wärmemenge oder Prüfung gegen ein Kriterium (Norm, Grenzwert, Messwert) → Variante, Vergleich zweier Fälle oder leichte Steigerung (z. B. Becher mit Wärmekapazität) → Zusatzfrage.
6. **Weitere Bausteine:** technischer Zwilling als eigene Aufgabe mit eigener Ausgangssituation; kurze Rechnungen als „Zusatzaufgabe“ am Ende; ein Versuch im Tutorium mit Vorhersage und Messtabelle, wenn er sich anbietet.
7. **Umfang:** etwa 175 bis 425 Wörter je Aufgabe ohne Ausgangssituation.

## Lösung

- Aufgabentext wiederholen, dann „**Lösung:**“, zuerst die Auflösung der Vorab-Frage in einem Satz.
- Vorgehen wie in den Vorlesungsbeispielen und Kurzlösungen: **Geg.**, **Ges.**, **Skizze** (Bilanzraum), **Annahmen**, **Ansatz**, dann je Teil die Rechnung.
- Je Gleichung höchstens ein kurzer Satz („Umstellen nach T:“, „Werte einsetzen:“); Zahlen mit Einheiten einsetzen, Ergebnis in K und °C.
- Bilanz benennen: „Globale instationäre Energiebilanz um das geschlossene System … (V = const.)“, dann dU/dt = −Q̇_ab und m c_p dT/dt = −kA (T − T_u).
- Differentialgleichung durch Trennung der Variablen mit Integrationsgrenzen bis ln((T − T_u)/(T_0 − T_u)); keine homogene und partikuläre Lösung. Die Standardform dT/dt + aT = b mit Formelsammlung 5.1 kommt im Material vor (Tutorium 5), wird nach D24 aber nicht eigens geübt.

## Notation

- ϑ in °C, T in K (oder durchgängig T); pro Aufgabe eine Konvention. Kurze Indizes: u (Umgebung), 0, 1, 2, ein/aus, i/a; Stoff nach Komma (c_p,W).
- Dezimalkomma; Endergebnisse meist mit zwei Nachkommastellen. Keine Tausenderpunkte.
- Nicht übernehmen: Gedankenstriche, Dezimalpunkte, kaputte Querverweise.

## Was aus den bisherigen Entscheidungen dazukommt

- Vorab-Frage als „Frage 1“ direkt nach der Ausgangssituation, Auflösung in einem Satz am Anfang der Lösung (D13).
- Plausibilitätsprüfung als eigener Teil: Vergleich, Kriterium oder Grenzfall (D21).
- Annahmen aufstellen und begründen bleibt als Teil erhalten, wo es zur Aufgabe passt (D26).
- Quellen der Arbeitswerte und „Hinweise für die Tutoriumsleitung“ (typische Fehler, Fehlvorstellung, was die Rechnung weglässt, Zum Weiterdenken) stehen am Ende der Lösung bzw. im Anhang der Sammlung; das Aufgabenblatt bleibt schlank.
- Musterbeispiel: Kaffee-Aufgabe (Tutorium 5, Aufgabe 1) in der Aufgabensammlung vom 21.10.2026.
