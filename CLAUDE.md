# Tutorien Wärmeübertragung: Arbeit in Cloud-Sitzungen

> Für Claude in einer Cloud-Sitzung von Claude Code. Die Tutoriumsleitung (TL) ist Lukas; er leitet die Tutorien Wärmeübertragung am Lehrstuhl für Fluidverfahrenstechnik der Universität Paderborn. Die TL entscheidet, du empfiehlst klar. Deutsch. Keine Gedankenstriche (– oder —), stattdessen Komma, Punkt, Doppelpunkt oder Klammern.

## Aktueller Auftrag: unabhängige Prüfung der Kaffee-Aufgabe

Startsatz der TL: „Führe die Kaffee-Prüfung durch.“ Dann arbeitest du nach `pruefung/Kaffee_Pruefpaket_2026-10-23/01_STARTPROMPT.md`, mit den Anpassungen unten. Das Paket ist für einen Chat in der Claude-App geschrieben; hier gibt es keine Projektablage, keinen Ordner auf dem Mac der TL und vielleicht keine Docs-Werkzeuge. Alles, was dort in die Projektablage oder in ein Claude-Dokument geht, kommt hier in dieses Repository.

## Anpassungen an 01_STARTPROMPT.md

| Stelle im Startprompt | Hier stattdessen |
|---|---|
| Schritt 1.0: Platz in der Projektablage prüfen | entfällt. Werkzeuge prüfen wie beschrieben; fehlt etwas, mit `setup/umgebung_setup.sh` nachinstallieren (läuft als root, `apt` und `pip` sind erlaubt). Für die Protokolle einmal `cd pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/protokolle_quelle && npm install docx@9.7.1`. |
| Schritt 1.1: ZIP entpacken | entfällt. Das Paket liegt schon ausgepackt in `pruefung/Kaffee_Pruefpaket_2026-10-23/`; gearbeitet wird im Ordner `pruefung/`. |
| Schritt 1.3: Feedback aus dem Claude-Dokument | Stand 25.10.2026: Das Dokument enthält keine Anmerkungen in [ ]. Gibt es Docs-Werkzeuge, kurz nachsehen, ob seitdem welche dazugekommen sind; sonst die TL im ersten Zwischenstand fragen, ob sie Feedback hat (sie kann es in den Chat schreiben). |
| Schritt 2: Prüfer als Hintergrund-Agenten | wie beschrieben, mit dem Agent-Werkzeug, alle sechs in einer Nachricht, ohne Modellvorgabe. Websuche über die Such- und Abrufwerkzeuge, nicht über die Shell (die Shell erreicht nur freigegebene Adressen). |
| Bericht in die Projektablage `claude/kaffee_pruefung/ergebnisse/<Kürzel>_BERICHT.md` | nach `ergebnisse/kaffee/<Kürzel>_BERICHT.md` kopieren, **sofort committen und pushen** (das ist die Sicherung). |
| Schritt 4.1: Tab „Änderungsvorschläge“ im Claude-Dokument | Gibt es Docs-Werkzeuge mit Zugriff auf <https://claude.ai/artifact/LCRkwWobg2nv739T5XC73d>, wie beschrieben. Sonst die Vorlage als `ergebnisse/kaffee/Aenderungsvorschlaege.md` (Tabelle aus `04_BUENDELUNG.md` mit leeren Spalten „Entscheidung“ und „Anmerkung“). Die TL entscheidet dann im Chat (z. B. „Ä1 ja, Ä2 nein, Ä3 Variante B“) oder trägt in die Datei ein. Bündelung als `ergebnisse/kaffee/Buendelung.md`. |
| Schritt 4.2: Protokolle | Quellen in `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/protokolle_quelle/` (Version 8, zuletzt vergeben K33, G39, D92). Nummern K34 (Prüfung), K35 (Umsetzung), G40, D93 ff. Bauen wie in der LIESMICH dort; PDF, Word und Markdown nach `ergebnisse/kaffee/protokolle/`. Nicht in eine Projektablage. |
| Schritt 4.4: anhalten | anhalten, committen, pushen, auf die TL warten. |
| Nach der Entscheidung, Schritt 0 | entfällt (alles liegt im Repository). |
| Schritt 3: Claude-Dokument nachziehen | nur mit Docs-Werkzeugen; sonst weglassen und im Schlussbericht erwähnen. |
| Schritt 5: Übergabe | Fertige Dateien (Kaffee-Blatt und Lösung als PDF und Word, Sammlung als PDF und Word, Protokolle) nach `ergebnisse/kaffee/fertig/`. Die Markdown-Fassungen, die in der Projektablage ersetzt werden sollen, nach `ergebnisse/kaffee/projektablage/` (gleiche Dateinamen wie im Startprompt). Kein Arbeitsstand-ZIP: Das Repository ist der Arbeitsstand. |

## Siebter Bericht: Gegenprüfung durch Codex

Die TL lässt parallel Codex (OpenAI) als unabhängige Rolle X prüfen (Auftrag in `AGENTS.md`; die Datei ist für Codex, nicht für dich). Codex legt seinen Bericht auf einem eigenen Zweig als `ergebnisse/kaffee/X_CODEX_BERICHT.md` ab. **Vor dem Bündeln:** `git fetch origin '+refs/heads/*:refs/remotes/origin/*'` und mit `git log --all --oneline -- ergebnisse/kaffee/X_CODEX_BERICHT.md` suchen; gefunden: mit `git show <zweig>:ergebnisse/kaffee/X_CODEX_BERICHT.md` lesen, nach `ergebnisse/kaffee/` übernehmen und als siebten Bericht mitbündeln (Präfix „Codex“; Zahlen wie bei allen nachrechnen; im Gesamturteil sagen, wo Codex und die Claude-Prüfer übereinstimmen oder sich widersprechen). Nicht gefunden: die TL im Zwischenstand fragen, ob sie warten will oder ohne Codex gebündelt wird (Nachzügler später ergänzen).

## Abnahmeprüfung durch Codex nach der Umsetzung

Bevor du umsetzt, schreib die Entscheidungen der TL in die Spalten „Entscheidung“ und „Anmerkung“ von `ergebnisse/kaffee/Aenderungsvorschlaege.md` (auch wenn sie im Chat entschieden hat) und pushe. Nach der Umsetzung (Schritt 2 im Startprompt, gebaut und alle Seiten angesehen) und der zweiten Runde der Rolle S: alles committen und pushen, dann **anhalten** und der TL schreiben: „Bitte in Codex die Abnahmeprüfung starten: Zweig `<Name deines Zweigs>` wählen und ‚Führe die Abnahmeprüfung nach AGENTS.md durch.‘ senden.“ Wenn die TL meldet, dass Codex fertig ist: Bericht `ergebnisse/kaffee/X2_CODEX_ABNAHME.md` wie oben über `git fetch` holen, jeden Befund nachrechnen, eindeutige Fehler beheben, alles andere der TL mit Empfehlung vorlegen. Erst danach Übergabe (Schritt 5) und Pull Request. Will die TL keine Abnahme durch Codex, entfällt dieser Schritt.

## Git

- Arbeite auf dem Zweig der Sitzung. Nach jedem fertigen Bericht, nach der Bündelung und am Ende committen und pushen (kurze deutsche Commit-Nachrichten).
- Die Rollenordner `pruefung/arbeit*/` werden nicht eingecheckt (`.gitignore`); was davon bleiben soll, liegt in `ergebnisse/kaffee/`.
- Am Ende einen Pull Request mit einer kurzen Zusammenfassung öffnen. Gemergt wird von der TL.

## Danach (nicht deine Aufgabe in dieser Sitzung)

Ein Chat im Projekt „Wärmeübertragung Tutorium“ übernimmt die Ergebnisse aus diesem Repository in den Werkzeugkasten, den WÜ-Ordner der TL und die Projektablage.

## Regeln

Sparsam lesen (die Prüfmaterialien liest du nicht selbst, das tun die Prüfer). Jede Zahl der Prüfer nachrechnen, bevor du sie empfiehlst. Nichts an andere senden. Änderungen an Texten der TL kennzeichnen. Zwischenstände kurz halten. Bei Entscheidungen eine klare Empfehlung; entscheiden tut die TL.
