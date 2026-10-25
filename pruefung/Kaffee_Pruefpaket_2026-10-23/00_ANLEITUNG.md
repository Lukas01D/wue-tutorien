# Anleitung: Unabhängige Prüfung der Kaffee-Aufgabe

> Für die Tutoriumsleitung. Stand 23.10.2026. Ein Chat koordiniert alles: Er startet sechs Prüfer mit getrennten Rollen und getrennten Materialien, bündelt ihre Vorschläge und legt sie dir zur Entscheidung vor. Du musst keine einzelnen Chats starten. Das Paket wurde am 23.10.2026 in einem Trockenlauf getestet (entpacken, Rollenordner anlegen, alle Aufträge lesen, Blätter, Sammlung und Protokolle neu bauen).

**Begriffe:** *Projektablage* = die Dokumente des Claude-Projekts „Wärmeübertragung Tutorium“. *Claude-Dokument* = das bearbeitbare Dokument „Kaffee mit Milch (Tutorium 5)“ auf claude.ai, in das du Anmerkungen schreiben kannst. *Prüfer* = Hilfs-Agenten, die der Chat im Hintergrund startet; jeder hat eine Rolle und einen eigenen Ordner.

## Auf einen Blick

| Phase | Du | Der Chat | Dauer |
|---|---|---|---|
| A Vorbereiten | ZIP bereitlegen, optional Anmerkungen in [ ] ins Claude-Dokument | | 5 min |
| B Starten | neuen Chat im Projekt öffnen, ZIP anhängen, Startsatz senden | prüft Werkzeuge, entpackt, liest dein Feedback, legt sechs Rollenordner an | 5 min |
| C Prüfen | nichts (du kannst weggehen) | sechs Prüfer arbeiten gleichzeitig, Berichte landen sofort in der Projektablage | 20 bis 45 min |
| D Bündeln | nichts | vereint, rechnet nach, legt den Tab „Änderungsvorschläge“ an, trägt die Prüfung in die Protokolle ein | 15 bis 25 min |
| E Entscheiden | je Vorschlag ja, nein oder Variante wählen, Anmerkungen in [ ] | wartet | so lange du willst |
| F Umsetzen | „Entscheidungen sind eingetragen, bitte umsetzen.“ | setzt um, baut neu, prüft, Protokolle, Studierende rechnet die neue Fassung | 30 bis 60 min |

## Phase A: Vorbereiten

- **ZIP:** `Kaffee_Pruefpaket_2026-10-23.zip` aus dem Chat vom 23.10.2026 herunterladen (am besten auch in Sciebo ablegen). Es enthält alles: Steuerdateien, Material, Arbeitsordner für die Umsetzung, Protokollquellen.
- **Feedback (optional):** Im Claude-Dokument „Kaffee mit Milch (Tutorium 5)“ (<https://claude.ai/artifact/LCRkwWobg2nv739T5XC73d>) kannst du vorher Anmerkungen in [eckigen Klammern] direkt in den Text schreiben. Der Chat gibt sie den Prüfern mit (der Studierenden-Rolle erst nach ihrer eigenen Rechnung).
- **Volumen:** Am besten kurz nach dem Zurücksetzen deines Nutzungsvolumens starten (Schätzung unten).
- **Platz in der Projektablage:** Sie war am 23.10.2026 zu rund 94 % gefüllt. Für diese Prüfung reicht der Rest; lege bis dahin möglichst nichts Großes zusätzlich ab. Der Chat prüft den Platz zu Beginn.

## Phase B: Starten

1. In Claude im Projekt **„Wärmeübertragung Tutorium“** einen **neuen Chat** öffnen. Nicht den langen Chat vom 21. bis 23.10. weiterführen: Der neue ist günstiger und wirklich unabhängig von der Entstehung der Aufgabe.
2. Das stärkste Modell wählen und den Aufwand auf hoch oder maximal stellen.
3. Das ZIP anhängen und diesen **Startsatz** senden:

   > Bitte führe die unabhängige Prüfung der Kaffee-Aufgabe durch. Folge genau der Datei 01_STARTPROMPT.md im angehängten Paket.

## Phase C und D: Prüfen und Bündeln

| Kürzel | Rolle | prüft vor allem | Websuchen |
|---|---|---|---|
| P | Professorin | Passung zu Vorlesung, Übung und Klausur, Stil des Lehrstuhls, Umfang, Freigabe | höchstens 5 |
| T | Technik | Modell, Annahmen, Zahlen, Empfindlichkeit, Messbarkeit im Versuch (rechnet selbst nach) | höchstens 10 |
| D | Didaktik | Lernziele, Vorab-Frage und Fehlvorstellung, Aufbau von a bis h, Versuch, Zeit (mit Forschungsliteratur) | höchstens 10 |
| R | Recherche | Arbeitswerte und Quellen, Messungen zu „Milch sofort oder später“, Vergleichsaufgaben | höchstens 20 |
| S | Studierende | rechnet das Blatt selbst durch, Zeitbedarf und Stolperstellen, Lösung erst danach | keine |
| G | Gestaltung | Formatierung im Vergleich mit den Original-Tutoriumsblättern und der FVT-Aufgabenvorlage (kleine Anpassungen), Lesbarkeit, Abbildungen, Druck, Word | höchstens 5 |

**Getrennte Materialien:** Jede Rolle bekommt einen eigenen Ordner, in den das Skript `rollen_vorbereiten.py` nur ihre Dateien kopiert (Übersicht: `05_LESEVERTEILUNG.md`). Die Studentin liest zum Beispiel nur Blatt, Formelsammlung und Foliensatz und bekommt die Lösung erst nach dem eigenen Durchrechnen; die Recherche bekommt keine Lehrstuhlunterlagen. Das spart Volumen und hält die Rollen unabhängig. Die Prüfer sind außerdem angewiesen, keine Projektablage, keine früheren Chats und keine Erinnerungen zu nutzen. (Technisch verhindern lässt sich das nicht ganz; es ist eine klare Anweisung.)

## Phase E: Entscheiden

- Im Claude-Dokument erscheint ein neuer Tab **„Änderungsvorschläge“**: oben das Gesamturteil, darunter Tabellen nach **muss**, **sollte** und **kann** mit den Nummern Ä1, Ä2, …, jeweils mit Empfehlung, dazu Widersprüche zwischen den Rollen, „Vorgabe in Frage gestellt“ und was bleiben sollte.
- In der Spalte **„Entscheidung“** wählst du **ja**, **nein** oder **Variante**; in der Spalte **„Anmerkung“** oder direkt im Text schreibst du in [ ], was anders sein soll.
- Dann im Chat: **„Entscheidungen sind eingetragen, bitte umsetzen.“**

## Phase F: Umsetzen

Der Chat setzt nur um, was du angenommen hast: Aufgabentext (Sammlung und Einzelblatt), Lösung, Rechenmodell, Abbildungen. Er baut alles neu, prüft die Seiten als Bild, zieht das Claude-Dokument nach und schreibt KI-Protokoll und Entscheidungsprotokoll fort. Zum Schluss rechnet die Studierenden-Rolle die neue Fassung noch einmal durch. Die neuen Dateien bekommst du im Chat, die Markdown-Fassungen landen in der Projektablage. Zum Schluss bekommst du den neuen Arbeitsstand als ZIP: Häng ihn beim nächsten Mal zusammen mit dem **Werkzeugkasten** an und schreib „Übernimm den angehängten neuen Arbeitsstand in den Werkzeugkasten.“, damit künftige Aufgaben auf dem neuesten Stand aufbauen.

## Kosten und Dauer (Schätzung)

- **Dauer:** rund 45 bis 75 Minuten bis zur Entscheidungsvorlage, davon 20 bis 45 Minuten, in denen die Prüfer parallel arbeiten.
- **Volumen:** grob 1,5 bis 3 Millionen Tokens bis zur Entscheidungsvorlage; die Umsetzung kommt danach dazu. Zum Vergleich: Die Gegenprüfung der Aufgabensammlung am 21.10.2026 (drei Prüfer) lag bei rund 1,6 Millionen, der Trockenlauf dieses Pakets (ein Agent) bei rund 0,5 Millionen. Wie viel Prozent deines Max-Abos das ist, lässt sich nicht genau sagen, weil Anthropic die Grenzen nicht in Tokens angibt.
- **Sparen:** Die Leselisten sind knapp gehalten. Wer noch mehr sparen will, schreibt in den Startsatz „nur die Rollen P, T und D“ und holt R, S und G später nach.

## Notfall

| Problem | Lösung |
|---|---|
| Volumen wird knapp | Im Chat „bitte pausieren“ schreiben. Fertige Berichte liegen dann schon in der Projektablage (`claude/kaffee_pruefung/ergebnisse/`). Später „weiter“ schreiben; fehlende Rollen startet der Chat neu. |
| ZIP vergessen | Der Chat fragt danach. Ohne ZIP nimmt er die Textfassung aus der Projektablage (`claude/kaffee_pruefung/paket/…`); PDF, Word und Bilder fehlen dann, Rolle G prüft nur eingeschränkt. |
| Der Chat kann keine Hintergrund-Agenten starten | Je Rolle einen eigenen Chat im Projekt öffnen, ZIP anhängen und schreiben: „Entpacke das Paket nach `pruefung/`, führe dort `python3 Kaffee_Pruefpaket_2026-10-23/rollen_vorbereiten.py Kaffee_Pruefpaket_2026-10-23 arbeit` aus und arbeite als Prüfer `<Kürzel>` nur nach `arbeit/<Kürzel>/AUFTRAG.md`. Lege den fertigen Bericht als `claude/kaffee_pruefung/ergebnisse/<Kürzel>_BERICHT.md` in die Projektablage.“ Danach einen Chat mit ZIP: „Führe 01_STARTPROMPT.md ab Schritt 3 aus; die Berichte liegen unter `claude/kaffee_pruefung/ergebnisse/`.“ |
| Ein Prüfer bricht ab | Der Chat startet ihn einmal neu und sagt es dir. |
| Projektablage voll | Der Chat meldet es und schlägt vor, die Textfassung des Materials (`claude/kaffee_pruefung/paket/material/`) zu löschen; sie steckt vollständig im ZIP. Gelöscht wird erst nach deinem Ja. Die Prüfung läuft auch ohne Ablage weiter, übersteht dann aber keine lange Pause. |
| Umsetzung erst Tage später oder in einem neuen Chat | ZIP anhängen und schreiben: „Führe 01_STARTPROMPT.md ab ‚Nach meiner Entscheidung‘ aus. Bündelung und Berichte liegen unter `claude/kaffee_pruefung/ergebnisse/`, die Protokollquellen unter `claude/protokolle_quelle/`.“ |

## Was im Paket ist

| Datei oder Ordner | Inhalt |
|---|---|
| `00_ANLEITUNG.md` | diese Anleitung |
| `01_STARTPROMPT.md` | der eine Prompt für den koordinierenden Chat (Prüfung, Entscheidung, Umsetzung) |
| `02_PRUEFAUFTRAG.md` | gemeinsamer Teil für alle Prüfer: Kontext, Vorgaben, Regeln, Berichtsformat |
| `03_ROLLEN.md` | die sechs Rollen mit Prüffragen |
| `04_BUENDELUNG.md` | Regeln zum Bündeln, Aufbau des Tabs, Protokolleinträge |
| `05_LESEVERTEILUNG.md` | welche Rolle welche Datei liest (aus `leseliste.json` erzeugt) |
| `leseliste.json`, `rollen_vorbereiten.py` | Leselisten und das Skript, das die Rollenordner anlegt |
| `material/` | A Aufgabe (PDF, Word, Markdown, Abb. 1), B Lösung (mit Quellen), C Rechenmodell, D Anforderungen (Strukturvorlage, Auszüge aus Lernzielen und Entscheidungen, Überblick über Tutorium 5), E Lehrstuhl (Tutorium 3, 5 und 6, Übung 6 und 7 mit Lösungen, Kurzlösung, Klausurübersicht, Formelsammlung, Foliensatz 05), F Vorlagen (Original-Tutoriumsblätter, Original-Lösung, Logos, FVT-Aufgabenvorlage als Word und PDF mit ihren Maßen) |
| `umsetzung/Arbeitsordner/` | Sammlung und Kaffee-Bau zum Umsetzen der Änderungen (nicht für die Prüfer) |
| `umsetzung/protokolle_quelle/` | Quellen und Bauanleitung der Protokolle (Version 8) |
| `protokolle/` | KI-Protokoll und Entscheidungsprotokoll als Word und PDF (Version 8) |
