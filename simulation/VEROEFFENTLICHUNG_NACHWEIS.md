# Veröffentlichungsnachweis der Kaffee-Simulation

Stand: 06.11.2026, 20:25:25 Uhr (Europe/Berlin, CET).

**Status: Öffentlich seit 06.11.2026, 20:25:25 Uhr CET, gemäß geänderter Entscheidung E2 der Tutoriumsleitung vom 06.11.2026. Die veröffentlichte Datei und Sites-Version 1 sind unverändert. Der Nachweis über Quelle, Upload und Sites-Zugangseinstellung ist durch Codex abgeschlossen. Live-Abgleich: extern durch Claude, gemäß ausdrücklicher Anweisung der Tutoriumsleitung. Codex bestätigt keine selbst gemessene Bytegleichheit der HTTP-Auslieferung.**

| Punkt | Nachweis |
|:--|:--|
| Adresse | https://waermeuebertragung-kaffee.qarri196.chatgpt.site |
| Quelle | Merge-Commit auf `main`: `aa2b9d422111db0bb930b477d9e0643447291148`, 06.11.2026, 20:12:23 Uhr CET. Merge von PR #6, `claude/simulation-tool-kaffee-4kcacl`. |
| Datei im Repository | `simulation/site/index.html`, 433303 Bytes. SHA-256: `d37edd0c05c8a4533170e13d65d68ac564420cbb1170e7e0963316125e3df46d`. |
| Prüfungen vor dem Hochladen | `git fetch origin main`, `git checkout main`, `git pull --ff-only origin main`. Merge-Commit geprüft. Beide HTML-Dateien und `BAUNACHWEIS.txt` haben dieselbe Prüfsumme. `bauen.py --pruefen` meldet `gleich` mit Python 3, fontTools und Brotli. |
| Veröffentlichte Quelle bei Sites | Commit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8` auf `main` des Site-Quellrepositorys. Enthält die unveränderten Bytes aus dem oben genannten Merge-Commit als `dist/index.html` und die Hosting-Konfiguration. Push und Remote-Commit wurden abgeglichen. |
| Hochgeladene Datei | 433303 Bytes, SHA-256: `d37edd0c05c8a4533170e13d65d68ac564420cbb1170e7e0963316125e3df46d`. Bytegleichheit mit dem Git-Objekt des Merge-Commits und dem Inhalt des Upload-Archivs geprüft. |
| Umfang der Veröffentlichung | Eine Startseite `index.html`. Das Deployment-Archiv enthält nur `dist/index.html` und `.openai/hosting.json`. Keine Änderungen an HTML, Skripten, Stilen oder eingebetteten Schriften. Keine zusätzlichen Seitenressourcen. |
| Veröffentlichung | Sites-Version 1, Deployment `appgdep_6aee28079650819197a2607341778eed`, Status `succeeded`, 06.11.2026, 20:18:46 Uhr CET. |
| Ausgelieferte Datei | **Live-Abgleich: extern durch Claude.** Bytes und SHA-256 der HTTP-Auslieferung wurden von Codex nicht gemessen. Erwartet: 433303 Bytes und dieselbe SHA-256 wie im Repository und Upload. Ein externes Prüfergebnis liegt diesem Nachweis noch nicht bei. |
| Antwortkopfzeilen der Seite | **Extern durch Claude:** Content-Type, Content-Encoding, Cache-Control und Prüfung auf Veränderungen durch Sites, etwa eingefügte Skripte. Von Codex nicht ermittelt. |
| Zugangseinstellung, aktuell | **Öffentlich.** `update_site_access(access_mode="public")` bestätigt Zugangsrevision 2 vom `2026-11-06T19:25:25.726484+00:00` (20:25:25 Uhr CET). Anschließend mit `get_site` erneut geprüft: `access_mode=public`, `access_policy.access_mode=public`, Revision 2, unveränderte Adresse und weiterhin Sites-Version 1. |
| Zugangseinstellung, Erstveröffentlichung | Zunächst nur das Eigentümerkonto: `access_mode=custom`, Revision 1, keine weiteren Bearbeiter, keine Gruppen, keine externen Besucher. Die Erstveröffentlichung erfolgte mit `save_version_and_deploy_private`. Dieser Zugang wurde mit der unten dokumentierten TL-Entscheidung durch `public` ersetzt. |
| Abruf ohne Anmeldung | **Extern durch Claude.** Nach dem Öffentlichschalten soll die Simulation ohne Anmeldung erreichbar sein. Von Codex nicht per HTTP geprüft. Der frühere Abruf aus der Cloud-Umgebung scheiterte am Netzwerkproxy mit `CONNECT tunnel failed, response 403`; dies ist kein Beleg für den Zugang der Site. |

## Sites-Kennungen

- Projekt: `appgprj_6aee2773b8788191b72faeefddd89f34`
- Gespeicherte Version: `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_6e1de74f09408191863b0e9143057de9`
- Sites bestätigt für diese Version den Quellcommit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8`.

## Öffentlichschaltung und Änderung von E2

Entscheidung der Tutoriumsleitung vom 06.11.2026: **„öffentlich schon jetzt statt erst am Sitzungstag (ändert E2)“**, mit dem Auftrag **„Schalte die Kaffee-Seite öffentlich.“** Damit ersetzt diese Entscheidung die bisherige zeitliche Zugangsbeschränkung aus E2 (`simulation/KONZEPT.md`, Abschnitt 9.6) und `simulation/VEROEFFENTLICHUNG.md`, Abschnitt 2. Die Freigabe gilt ab sofort, ein weiterer Zuruf am Sitzungstag ist nicht erforderlich.

Umgesetzt am 06.11.2026 um 20:25:25 Uhr CET durch Änderung ausschließlich der Sites-Zugangseinstellung von `custom` auf `public`. Die neue Einstellung wurde durch einen anschließenden `get_site`-Abruf bestätigt. Es wurde keine neue Site-Version gespeichert oder veröffentlicht.

Nach der Freigabe bestätigt `get_site_version` weiterhin Version 1 mit dem Quellcommit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8` und dem bisherigen Deployment. Der erneute lokale Prüfsummenabgleich von `simulation/site/index.html`, `simulation/site/Kaffee_Simulation.html` und der hochgeladenen `dist/index.html` ergibt unverändert `d37edd0c05c8a4533170e13d65d68ac564420cbb1170e7e0963316125e3df46d`. Der gesamte Ordner `simulation/site/` ist gegenüber dem Merge-Commit unverändert. Die SHA-256 der tatsächlichen HTTP-Auslieferung bleibt Teil des externen Live-Abgleichs.

## Live-Abgleich: extern durch Claude

Die Tutoriumsleitung hat angewiesen, keine Netzwerkfreigabe vorzunehmen und den Codex-Nachweis mit den prüfbaren Ergebnissen abzuschließen. Claude übernimmt die folgenden Live-Prüfungen im angemeldeten Browser der Tutoriumsleitung:

1. Die Startseite abrufen, Antwortkopfzeilen erfassen und den Inhalt byteweise mit der Datei aus dem Merge-Commit vergleichen. Erwartet: 433303 Bytes, SHA-256 `d37edd0c05c8a4533170e13d65d68ac564420cbb1170e7e0963316125e3df46d`.
2. Den Abruf in einer getrennten Sitzung ohne Anmeldung prüfen. Nach der Öffentlichschaltung muss die Simulation dabei erreichbar sein, die frühere Erwartung einer Anmeldesperre gilt nicht mehr.
3. Das externe Prüfergebnis gesondert dokumentieren. Bei veränderten HTML-Bytes die Veröffentlichung als nicht abgenommen melden.

Bei den durch Codex geprüften Quelldateien, beim Upload und bei der Sites-Zugangseinstellung wurden keine Abweichungen festgestellt. Die externe Live-Prüfung wird durch diesen Nachweis nicht vorweggenommen.

Die Site ist gemäß der oben dokumentierten TL-Entscheidung öffentlich. Die Datei wurde beim Öffentlichschalten nicht geändert.
