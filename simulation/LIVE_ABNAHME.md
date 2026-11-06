# Live-Abnahme der Kaffee-Simulation

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
