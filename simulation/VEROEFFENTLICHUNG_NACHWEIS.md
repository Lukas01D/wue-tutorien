# Veröffentlichungsnachweis der Kaffee-Simulation

Stand: 06.11.2026, 20:21 Uhr (Europe/Berlin, CET).

**Status: Private Veröffentlichung erfolgreich. Der Nachweis über Quelle, Upload und Sites-Zugangseinstellung ist durch Codex abgeschlossen. Live-Abgleich: extern durch Claude, gemäß ausdrücklicher Anweisung der Tutoriumsleitung im angemeldeten Browser. Codex bestätigt keine selbst gemessene Bytegleichheit der HTTP-Auslieferung.**

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
| Zugangseinstellung | Nach der Veröffentlichung erneut mit `get_site` geprüft: `current_user_role=owner`, `access_mode=custom`, genau ein erlaubtes Konto mit Rolle `owner`, keine weiteren Bearbeiter, keine Gruppen, keine externen Besucher. Die Veröffentlichung erfolgte mit `save_version_and_deploy_private`. |
| Abruf ohne Anmeldung | **Extern durch Claude.** Von Codex nicht an der Site geprüft. Der Abruf aus der Cloud-Umgebung scheiterte vorher am Netzwerkproxy mit `CONNECT tunnel failed, response 403`. Das ist kein Nachweis der Anmeldesperre der Site. |

## Sites-Kennungen

- Projekt: `appgprj_6aee2773b8788191b72faeefddd89f34`
- Gespeicherte Version: `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_6e1de74f09408191863b0e9143057de9`
- Sites bestätigt für diese Version den Quellcommit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8`.

## Live-Abgleich: extern durch Claude

Die Tutoriumsleitung hat angewiesen, keine Netzwerkfreigabe vorzunehmen und den Codex-Nachweis mit den prüfbaren Ergebnissen abzuschließen. Claude übernimmt die folgenden Live-Prüfungen im angemeldeten Browser der Tutoriumsleitung:

1. Die Startseite abrufen, Antwortkopfzeilen erfassen und den Inhalt byteweise mit der Datei aus dem Merge-Commit vergleichen. Erwartet: 433303 Bytes, SHA-256 `d37edd0c05c8a4533170e13d65d68ac564420cbb1170e7e0963316125e3df46d`.
2. Den Abruf in einer getrennten Sitzung ohne Anmeldung prüfen. Die Simulation darf dabei nicht ausgeliefert werden.
3. Das externe Prüfergebnis gesondert dokumentieren. Bei veränderten HTML-Bytes die Veröffentlichung als nicht abgenommen melden.

Bei den durch Codex geprüften Quelldateien, beim Upload und bei der Sites-Zugangseinstellung wurden keine Abweichungen festgestellt. Die externe Live-Prüfung wird durch diesen Nachweis nicht vorweggenommen.

Die Site bleibt bis zum ausdrücklichen Zuruf der Tutoriumsleitung auf das Eigentümerkonto beschränkt. Zum späteren Öffentlichschalten lautet der Satz: **„Schalte die Kaffee-Seite öffentlich.“** Dabei darf die Datei nicht geändert werden.
