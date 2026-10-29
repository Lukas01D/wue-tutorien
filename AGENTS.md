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
