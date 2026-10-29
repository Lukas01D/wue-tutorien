# Auftrag für Codex: unabhängige Gegenprüfung der Kaffee-Aufgabe (Rolle X)

> Für Codex (OpenAI). Startsatz der Tutoriumsleitung: „Führe die Gegenprüfung nach AGENTS.md durch.“ Parallel prüfen sechs Claude-Prüfer dieselbe Aufgabe; du bist die siebte, bewusst unabhängige Stimme mit einem anderen Modell. Deutsch. Keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern.

## Was du liest (nur das)

1. `pruefung/Kaffee_Pruefpaket_2026-10-23/02_PRUEFAUFTRAG.md`, Abschnitte 1 bis 4 (gemeinsamer Prüfauftrag; Abschnitte zu Ordnern und Platzhaltern gelten für dich nicht).
2. `pruefung/Kaffee_Pruefpaket_2026-10-23/03_ROLLEN.md`, **nur** den Abschnitt „T: Technik“. Das ist deine Rolle, mit einem Zusatz unten.
3. Dein Material im Ordner `pruefung/Kaffee_Pruefpaket_2026-10-23/material/`:
   `A_aufgabe/` (Kaffee_Aufgabe.md und .pdf, Abb1_Tassen), `B_loesung/Kaffee_Loesung.md` und .pdf mit den Abbildungen AbbL1 und AbbL2, `C_modell/` (kaffee_modell.py, nachrechnung_kaffee.py, Ausgabe), `E_lehrstuhl/Formelsammlung_2026.md`, `E_lehrstuhl/Foliensatz05_Bilanzierung_Folien1-21.txt`.

**Nicht lesen:** andere Rollentexte, `material/D_anforderungen/`, `material/F_vorlagen/`, die übrigen Dateien in `E_lehrstuhl/`, `umsetzung/`, `protokolle/`, `ergebnisse/` und alle Zweige außer deinem. Du sollst unbeeinflusst urteilen.

## Zusatz zu Rolle T

Bevor du die Lösung liest: **Löse Teil a bis e der Aufgabe selbst** (eigenes Python-Skript, nur mit Aufgabe, Formelsammlung und Folien) und notiere, wo du gestockt hast. Erst dann Lösung und Rechenmodell lesen und vergleichen. Das vorhandene Rechenmodell darfst du ausführen, aber nicht als Beweis nehmen. Websuche, falls verfügbar, höchstens 10 Mal und nur für physikalische Werte.

## Ergebnis

- Bericht nach `ergebnisse/kaffee/X_CODEX_BERICHT.md`, gegliedert wie in `02_PRUEFAUFTRAG.md` verlangt (Gesamturteil, Befunde nach Wichtigkeit, konkrete Änderungsvorschläge mit Begründung und Stelle). Vorschläge nummerierst du „Codex 1“, „Codex 2“, …
- Deine Skripte nach `ergebnisse/kaffee/codex_skripte/`.
- Nichts am Paket ändern. Committen, auf einem eigenen Zweig pushen und einen Pull Request mit dem Titel „Gegenprüfung Codex (Rolle X)“ öffnen.

---

# Zweiter Auftrag: Abnahmeprüfung nach der Umsetzung (Rolle X2)

Startsatz der Tutoriumsleitung: „Führe die Abnahmeprüfung nach AGENTS.md durch.“ (auf dem Zweig, den Claude nach der Umsetzung genannt hat). Claude hat die angenommenen Änderungsvorschläge umgesetzt. Du prüfst die neue Fassung unabhängig, bevor sie zur Freigabe geht.

## Was du liest

- `ergebnisse/kaffee/Aenderungsvorschlaege.md` (Vorschläge mit den Entscheidungen der Tutoriumsleitung)
- die neue Fassung in `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/`: `Kaffee_Aufgabe.md` und `.pdf`, `Kaffee_Loesung.md` und `.pdf`, `kaffee_modell.py`, `nachrechnung_kaffee.py` mit Ausgabe, Abbildungen in `grafik/`
- den Kaffee-Teil der Sammlung: `.../Arbeitsordner/sammlung/teile/t5a_kaffee.md`
- zum Vergleich die alte Fassung in `pruefung/Kaffee_Pruefpaket_2026-10-23/material/A_aufgabe/` und `B_loesung/` sowie `git diff` gegen `main`
- `E_lehrstuhl/Formelsammlung_2026.md` und den Foliensatz 05 wie im ersten Auftrag

## Prüffragen

1. **Zahlen:** Jede Zahl in Aufgabe und Lösung mit einem eigenen Skript nachrechnen (nicht nur das Modell ausführen). Stimmen Aufgabe, Lösung, Sammlung und Abbildungen überein?
2. **Umsetzung:** Ist jeder angenommene Vorschlag umgesetzt, und zwar so, wie entschieden (mit Anmerkung)? Wurde etwas geändert, das nicht entschieden war? Ist ein abgelehnter Vorschlag trotzdem eingeflossen?
3. **Folgefehler:** Hat eine Änderung an anderer Stelle etwas kaputt gemacht (Verweise auf Teilaufgaben, Nummerierung, Formelzeichen, Rundung, Bildunterschriften, Hinweise für die Tutoriumsleitung)?
4. **PDF und Word:** Seiten als Bild ansehen (`pdftoppm`, falls vorhanden): fehlende Bilder, kaputte Formeln, abgeschnittene Tabellen?

## Ergebnis

Bericht nach `ergebnisse/kaffee/X2_CODEX_ABNAHME.md`: Urteil (freigabereif, mit kleinen Korrekturen oder nicht freigabereif), dann Befunde nach Wichtigkeit mit Stelle und Korrekturvorschlag („Abnahme 1“, „Abnahme 2“, …). Skripte nach `ergebnisse/kaffee/codex_skripte/`. Nichts an Aufgabe oder Lösung ändern. Committen und auf demselben Zweig oder einem eigenen Zweig pushen.
