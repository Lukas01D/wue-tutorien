# Live-Abnahme der Kaffee-Simulation

## Fassung 3 (08.11.2026, Claude)

> Claude, 08.11.2026 gegen 22:15 Uhr (Berlin), aus der Cloud-Umgebung ohne Anmeldung: Abruf mit curl und Bedienung in Chromium über Playwright (1366 × 768, 1280 × 720, 390 × 844). Adresse laut Nachweis von Codex (`simulation/VEROEFFENTLICHUNG_NACHWEIS.md` auf `codex/kaffee-f3-veroeffentlichung`, af3e334): <https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site/>. Die Prüf-Site war zunächst privat (V1) und ist seit 22:09 Uhr auf Anweisung der TL („beide öffentlich für alle sichtbar bitte“) öffentlich; geprüft wurde deshalb die öffentliche Prüf-Site. Fassung 2 unter `waermeuebertragung-kaffee` ist unverändert und wurde nicht geprüft.

### Ergebnis: bestanden, mit einem Hinweis zur Auslieferung

| Prüfpunkt (VEROEFFENTLICHUNG.md, Abschnitt 5) | Ergebnis |
|:--|:--|
| Erreichbar ohne Anmeldung | bestanden: HTTP 200, `content-type: text/html`, `server: cloudflare`, `cache-control: public, max-age=0, must-revalidate` |
| 1 Datei gleich dem Bau | **bestanden mit Hinweis:** ausgeliefert 178 403 Bytes (SHA-256 `b95f5183…5a8a`) statt 177 289 Bytes (`95cff1f2…9702`, Merge 85353d9). Der einzige Unterschied ist ein von Cloudflare vor `</body>` eingefügtes Inline-Skript (1 114 Bytes, Bot-Erkennung `/cdn-cgi/challenge-platform/`); ohne diese Einfügung ist die Datei bytegleich. Die CSP der Seite verhindert seine Ausführung (CSP-Meldung in der Konsole, keine Anfrage nach außen, keine Wirkung auf die Seite). Dieselbe Einfügung erklärt das „zweite kleine Inline-Skript“ der Live-Abnahme von Fassung 2. Fuß: „Stand 2026-11-08 · Version 6700332355“ wie im Nachweis. |
| 2 Startkarte | bestanden: keine Kurve, keine Ergebniszahl im DOM, Knopf erst nach Tasse und Grund aktiv |
| 3 Tasse 1, Grund, 43,85 und 40,29 | bestanden bei allen drei Größen: 43,85 °C, 40,29 °C, 3,56 K; „Simulation und deine Rechnung stimmen überein“ |
| 4 Erklärung a | bestanden: Rückmeldung mit 25,49 und 28,90 kJ, Säulen mit 3,41 kJ |
| 5 Milch über 30 °C | bestanden: Grenze 30 °C, nach der Vermutung in Auftrag 3 bis 80 °C |
| 6 Englisch | bestanden: Dezimalpunkt (43.85 °C), Sprache bleibt nach Neuladen |
| „Von vorn“ (X6-01) | bestanden: keine Ergebniszahl im DOM, Statusansage leer |
| 7 Konsole und Netzwerk | bestanden: keine Skriptfehler, keine Anfragen an fremde Adressen; einzige Konsolenmeldung ist die CSP-Sperre des eingefügten Cloudflare-Skripts |
| 8 Laptop und Beamer | bestanden: bei 1280 × 720 Kernzahlen, Diagramm, beide Regler und Ausgangswerte im Bild; am Handy 390 px kein waagerechtes Scrollen |
| 9 Aufräumen | entfällt: frische Browserkontexte in der Cloud-Umgebung, kein Browser der TL benutzt |

**Cloudflare-Einfügung:** harmlos, weil die CSP sie blockiert. Entscheidung der TL (08.11.2026): so lassen, keine Änderung bei Sites (L1 in `ENTSCHEIDUNGEN_F3.md`).

### Gerätetest und Freigabe

| Punkt | Ergebnis |
|:--|:--|
| Gerätetest iPhone mit Safari (`simulation/ABNAHME_IPHONE.md`) | bestanden (TL, 08.11.2026) |
| Freigabe von Fassung 3 | **freigegeben durch die TL am 08.11.2026 um 22:24 Uhr** (F1 in `ENTSCHEIDUNGEN_F3.md`) |

### Hauptadresse nach dem Austausch (08.11.2026, gegen 22:35 Uhr, Claude)

Codex hat die Hauptadresse durch Fassung 3 ersetzt und die Prüfadresse wieder privat gestellt (Nachweis `simulation/VEROEFFENTLICHUNG_NACHWEIS.md` auf `codex/kaffee-f3-veroeffentlichung`, 7077e1c; dort war der HTTP-Abruf gesperrt). Abruf und Bedienung wie oben, ohne Anmeldung.

| Prüfpunkt | Ergebnis |
|:--|:--|
| Hauptadresse <https://waermeuebertragung-kaffee.qarri196.chatgpt.site/> | bestanden: HTTP 200, `text/html`, Cloudflare; liefert Fassung 3 |
| Datei gleich dem Bau | bestanden mit der bekannten Einfügung: 178 403 Bytes (SHA-256 `55c8e34c9628f2b5…`); ohne das Cloudflare-Skript (1 114 Bytes, durch die CSP blockiert, L1) bytegleich mit `simulation/site/index.html` (177 289 Bytes, `95cff1f2…9702`) |
| Fuß | „Stand 2026-11-08 · Version 6700332355“ |
| Ablauf, Zahlen, Sperren, Englisch, „Von vorn“ | bestanden wie bei der Prüf-Site (43,85 / 40,29 / 3,56; 25,49, 28,90, 3,41 kJ; Milch über 30 °C erst nach Auftrag 3) |
| Konsole, Netzwerk, Beamer 1280 × 720, Handy 390 px | bestanden: keine Skriptfehler, keine fremden Anfragen, alles im Bild, kein waagerechtes Scrollen |
| Prüfadresse privat | bestanden: <https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site/> antwortet ohne Anmeldung mit HTTP 401, keine Seite ausgeliefert |
| QR-Code (`simulation/qr/`) | zeigt auf die Hauptadresse, gilt damit für Fassung 3 |

**Ergebnis: bestanden.** Fassung 3 ist unter der Hauptadresse öffentlich. Weiter offen: Android, Bildschirmleser und Beamer im Hörsaal (nicht gemeldet).

**Nachtrag (09.11.2026):** Die Prüfadresse <https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site/> ist auf Anweisung der TL seit 08.11.2026, 22:34 Uhr wieder öffentlich (Fassung 3), also nach dieser Abnahme (gegen 22:30 Uhr, damals HTTP 401). Die Zeile „Prüfadresse privat“ oben beschreibt den Stand zum Zeitpunkt der Abnahme. Kontrollabruf am 09.11.2026: HTTP 200, 178 403 Bytes; ohne die bekannte Cloudflare-Einfügung (deren Kennung bei jedem Abruf wechselt) bytegleich mit `simulation/site/index.html`, also Fassung 3. Seit der Regel R1 der TL (09.11.2026) gibt es in wue-tutorien keine private Zwischenstufe mehr.

## Fassung 2 (06.11.2026)

> Claude, 06.11.2026, gegen 20:30 Uhr (Berlin), im Chrome der Tutoriumsleitung über Claude in Chrome, ohne Anmeldung. Ergänzt den Nachweis von Codex (`simulation/VEROEFFENTLICHUNG_NACHWEIS.md`), in dem Dateiabruf und Anmeldesperre als „extern durch Claude“ gekennzeichnet sind.

## Ergebnis: bestanden

| Prüfpunkt | Ergebnis |
|:--|:--|
| Anmeldesperre (vor dem Öffentlichschalten, privat) | bestanden: Der Aufruf ohne Anmeldung leitete zur Anmeldung bei OpenAI (Google-Konto) um; die Seite war nicht sichtbar. |
| Öffentlich erreichbar (nach 20:25 Uhr) | bestanden: <https://waermeuebertragung-kaffee.qarri196.chatgpt.site/> lädt ohne Anmeldung, Titel „Kaffee mit Milch: Simulation“. |
| Gleich dem Bau | bestanden, über den Inhalt: Das große Skript (235 015 Zeichen, SHA-256 beginnt mit `165031d7a106f420`) und das Stylesheet (190 533 Zeichen, `556470a529c34fa5`) der ausgelieferten Seite sind zeichengleich mit `simulation/site/index.html` auf `main` (aa2b9d4, Datei-SHA-256 `d37edd0c…f46d`). Fußzeile „Version fc1b035e76“ wie in der Datei. Ein bytegenauer Abruf der ganzen Datei war im Browser nicht möglich, weil die eigene Content-Security-Policy der Seite jede Netzanfrage aus der Seite heraus sperrt (`fetch` scheitert); das ist gewollt. |
| Zusätzliches Skript | Im Seitenbaum steht ein zweites kleines Inline-Skript (1097 Zeichen) am Ende von `body`, das nicht aus der Datei stammt; sein Inhalt war für das Prüfwerkzeug gesperrt. Vermutlich vom Browser oder der Erweiterung eingefügt. Kein Fehler in der Konsole, keine Wirkung auf die Seite festgestellt. Niedrige Bedeutung; bei Gelegenheit in einem frischen Browser ohne Erweiterungen gegenprüfen. |
| Ablauf und Rechenwerte | bestanden: Vorhersage „Tasse 1, etwa 4 K“ festgehalten; danach Kurven, Kernzahlen 34,05 °C, 30,19 °C, 3,85 K und Energiesäulen 34,88 kJ und 38,57 kJ (wie das Modell). Frage 1 verrät den Zeitpunkt 56 min nicht. |
| Konsole | bestanden: keine Fehler oder Ausnahmen nach Neuladen und Bedienung. |
| Laptop 1219 px | bestanden: kein waagerechtes Scrollen. |
| Aufgeräumt | Die Testeingaben im Browser der TL (vier Einträge `kaffee-sim-v2-*` im lokalen Speicher dieser Seite) wurden danach gelöscht, der Tab geschlossen. |

## Nicht live geprüft (offen bei der TL)

iPhone mit Safari (`simulation/ABNAHME_IPHONE.md`), Beamer im Hörsaal, Bildschirmleser, Probelauf mit zwei Studierenden und Stoppuhr.

## Schlanke Seite, Sites-Version 4 (12.11.2026, 00:55 Uhr)

Geprüft von Claude im Chrome der TL (Fenster 1366 × 640) auf https://waermeuebertragung-kaffee.qarri196.chatgpt.site/, Quelle Merge von PR #15 (`89d2d06658`).

| Nr. | Prüfung | Ergebnis |
|:--|:--|:--|
| 1 | Stand | Fuß „Stand 2026-11-12 · Version 3a805cda08“, gleich der Datei auf `main` |
| 2 | Kasten nach 45 min | Tasse 1 43,01 °C, Tasse 2 36,31 °C, Temperaturdifferenz 6,69 K |
| 3 | Säulen | 15,50 und 23,82 kJ, Q₂ − Q₁ 8,31 kJ |
| 4 | Regler und Vergleiche | zehn Regler; Bänder „Tasse mit Deckel“ und „Blatt: Tasse speichert keine Wärme“; Tassenwärmer höchstens 14,5 W bei kA des Blatts |
| 5 | Abspielen | nach 1,5 s „nach 10,8 min“ mit verdeckter Zukunft, Knopf „Anhalten“; am Ende „nach 45 min“, Säulen 15,50 und 23,82 kJ, Knopf wieder „Abspielen“ |
| 6 | Tassenwärmer 5 W | Tasse 1 51,83 °C, Tasse 2 44,33 °C, Differenz 7,50 K; Q₂ − Q₁ 9,31 kJ = 1241,8 J/K · 7,50 K |
| 7 | Englisch | „after 45 min“, „Cup 1 (milk at the start)“, 43.01 °C, Knopf „Play“, Band „cup with lid“ |
| 8 | Konsole, Speicher, fremde Skripte | keine Fehler, lokaler Speicher leer, keine nachgeladenen Skripte |
| 9 | Platz | im Fenster 1366 × 640 reichen die Regler bis 736 px, die Bänder brauchen Bildlauf; Codex meldet bei 1280 × 720 etwa 15 px |

Folge: Anordnung für niedrige Fenster nachgebessert (Zweig `claude/kaffee-schlank-abnahme`: Knöpfe nebeneinander, Säulen etwas kleiner, Diagramm bei Fenstern unter 700 px Höhe mindestens 200 px). Danach passt alles bei 1280 × 720 und 1366 × 768 ohne Bildlauf, bei 1366 × 640 fehlen noch etwa 40 px. Neue Veröffentlichung nach Merge nötig.

## Schlanke Seite, Sites-Version 5 (Nachtrag vom 12.11.2026, Befund A-04 der Aufarbeitung)

Claude hat Sites-Version 5 (Quelle Merge von PR #16) in der Nacht zum 12.11.2026 im Chrome der TL geprüft: Fuß „Stand 2026-11-12 · Version b5d8b9e52e“ gleich der Datei auf `main`, Werte des Blatts, Abspielen, Tassenwärmer und Englisch wie bei Version 4. Die Einzelergebnisse stehen nur im Chatverlauf und wurden damals nicht hier eingetragen (INFERRED). Belegt ist die Gleichheit der Datei: Die Prüfsumme im Nachweis von Codex (`VEROEFFENTLICHUNG_NACHWEIS.md`, Abschnitt „Nachbesserung“) ist gleich der Prüfsumme des Baus auf `main` (`aufarbeitung/ergebnisse/a5_bau.txt`, CONFIRMED). Die nächste Veröffentlichung (Behebung A-01 und A-02) bekommt wieder eine vollständige Live-Abnahme mit Tabelle.
