# Baubericht: Simulation „Kaffee mit Milch“

> Bau durch Claude nach `simulation/BAU_AUFTRAG.md` (Stand 6526feb, Rollentausch, Entscheidung der TL vom 05.11.2026). Grundlage: `simulation/KONZEPT.md` Fassung 2 (93cb32e). Dieser Bericht wächst mit jedem Teil; der Status steht am Ende.

## Umgebung (Teil 0)

| Punkt | Ergebnis |
|:--|:--|
| Repository `wue-tutorien`, Zweig `claude/simulation-tool-kaffee-4kcacl` | vorhanden, Stand 6526feb zu Beginn |
| Kaffee-Zweig `claude/kaffee-pruefung-sgvo1r` | erreichbar, Stand f8a5ce3 (wie erwartet) |
| Lernzentrum-Repository `Lukas01D/waermeuebertragung-lernzentrum` | nur Lesen, flach und ausgedünnt geklont nach `/home/user/lernzentrum_v8` (außerhalb dieses Repositorys), Tag `hauptadresse-v8-2026-11-05`, Commit c2af968fab5c883a52d8323771b7eebb5a969373 (2026-11-05 11:09 +0100, „Merge pull request #25 from Lukas01D/runde-12-v8-abnahme“); nicht als Arbeitsverzeichnis angemeldet |
| Python | 3.13.18 (numpy 2.5.3, reportlab 5.0.1) |
| Node, npm | 22.23.4, 10.9.9 |
| Playwright, Chromium | 1.63.0 mit vorinstalliertem Chromium 1243 (`/opt/pw-browsers`) |
| axe-core | 4.14.0, lokal und festgehalten in `simulation/tests/package.json` und `package-lock.json` (nur Prüfwerkzeug, nicht Teil der Seite) |
| pdftotext, pdftoppm, pandoc | vorhanden |
| Live-Adressen Lernzentrum und Werkstatt | **nicht erreichbar**: beide antworten mit 401 („Sign in required“), mit curl und im zweiten Versuch mit Chromium. Am 04.11.2026 war die Werkstatt noch offen (Bildschirmfotos von damals als ergänzender Vergleich). Ersatz: Lernzentrum lokal aus einer zweiten Kopie des Tags. |
| WebKit | **nicht verfügbar** (nicht in `/opt/pw-browsers`). Nicht nachinstalliert: Die Umgebung untersagt `playwright install`, weil es die vorhandene Chromium-Einrichtung stören kann. Alle Browserprüfungen sind Chromium-Prüfungen; der Safari-Nachweis bleibt für die TL (`simulation/ABNAHME_IPHONE.md`). |
| Bildschirmleser | keiner verfügbar (nur kopflose Browser); Nachweis bleibt offen |

## Quellcommits und Prüfsummen

| Quelle | Commit | SHA-256 |
|:--|:--|:--|
| `kaffee_modell.py` (Kaffee-Zweig, `pruefung/Kaffee_Pruefpaket_2026-10-23/umsetzung/Arbeitsordner/kaffee/`) | zuletzt geändert in 560b8d4, gelesen auf f8a5ce3 | eb7efc1d5322b629e1e11494f7c70fa8d8d54ec60e555874326fa491a31757a1 |
| `Kaffee_Simulation.html` (Kaffee-Zweig, `ergebnisse/kaffee/fertig/`, gleich `ergebnisse/kaffee/simulation/` dort; vier Fragen mit Vorhersage) | zuletzt geändert in 174e613, gelesen auf f8a5ce3 | 6f16a78ca8de373eb997ab9dea69b222f9bc57c9c97d7def3f49f9d01c6fdc83 |
| `Kaffee_Simulation.html` auf `main` (Stand 31.10.2026, ältere Fragen) | im Repository | 43f333149afd1fd805a499bf158cffb6e3beafd62e08fed134376fd436d259d5 |
| `test_simulation.py` (`ergebnisse/kaffee/simulation/`) | im Repository | fe9a55d2d37fd1e579757d47959c4c4d31d6ef77d59173f866c5bb047dec7dd3 |
| `browsertest.js` (`ergebnisse/kaffee/simulation/`) | im Repository | 354afbecf0d8c28a0ea94e7879a0b3ff501b1471e3bc5b17ff1ea223be9a92cd |
| Lernzentrum v8 | Tag `hauptadresse-v8-2026-11-05`, c2af968 | |
