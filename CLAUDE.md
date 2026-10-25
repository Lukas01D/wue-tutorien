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

## Git

- Arbeite auf dem Zweig der Sitzung. Nach jedem fertigen Bericht, nach der Bündelung und am Ende committen und pushen (kurze deutsche Commit-Nachrichten).
- Die Rollenordner `pruefung/arbeit*/` werden nicht eingecheckt (`.gitignore`); was davon bleiben soll, liegt in `ergebnisse/kaffee/`.
- Am Ende einen Pull Request mit einer kurzen Zusammenfassung öffnen. Gemergt wird von der TL.

## Danach (nicht deine Aufgabe in dieser Sitzung)

Ein Chat im Projekt „Wärmeübertragung Tutorium“ übernimmt die Ergebnisse aus diesem Repository in den Werkzeugkasten, den WÜ-Ordner der TL und die Projektablage.

## Regeln

Sparsam lesen (die Prüfmaterialien liest du nicht selbst, das tun die Prüfer). Jede Zahl der Prüfer nachrechnen, bevor du sie empfiehlst. Nichts an andere senden. Änderungen an Texten der TL kennzeichnen. Zwischenstände kurz halten. Bei Entscheidungen eine klare Empfehlung; entscheiden tut die TL.
