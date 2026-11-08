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

**Hinweis für die TL (Empfehlung):** Die Einfügung durch Cloudflare ist harmlos, weil die CSP sie blockiert, sie ist aber eine Veränderung der Auslieferung. Empfehlung: so lassen und im Nachweis vermerken; falls Sites eine Einstellung ohne Bot-Erkennung anbietet, kann Codex sie beim Ersetzen der Hauptadresse prüfen.

**Nicht live geprüft (offen bei der TL):** iPhone mit Safari, Android, Bildschirmleser, Beamer im Hörsaal (`simulation/ABNAHME_IPHONE.md`); Ersetzen der Hauptadresse `waermeuebertragung-kaffee` durch Fassung 3 (V1, Schritt 3) steht noch aus.

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
