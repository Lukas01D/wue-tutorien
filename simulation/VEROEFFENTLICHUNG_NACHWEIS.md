# Veröffentlichungsnachweis der Kaffee-Simulation

Stand: 06.11.2026, 20:18:46 Uhr (Europe/Berlin, CET).

**Status: Sites bestätigt die private Veröffentlichung. Der vorgeschriebene Live-Abgleich ist wegen der Netzwerkfreigabe der Cloud-Umgebung noch offen. Dieser Nachweis bestätigt noch keine Bytegleichheit der HTTP-Auslieferung.**

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
| Ausgelieferte Datei | **Noch nicht abgerufen. Bytes und SHA-256 der HTTP-Auslieferung sind nicht verifiziert.** Die Upload-Prüfsumme darf noch nicht als gemessene Live-Prüfsumme gelten. |
| Antwortkopfzeilen der Seite | Content-Type, Content-Encoding und Cache-Control noch nicht ermittelt. Veränderungen durch Sites, etwa eingefügte Skripte, sind noch nicht ausgeschlossen. |
| Zugangseinstellung | Nach der Veröffentlichung erneut mit `get_site` geprüft: `current_user_role=owner`, `access_mode=custom`, genau ein erlaubtes Konto mit Rolle `owner`, keine weiteren Bearbeiter, keine Gruppen, keine externen Besucher. Die Veröffentlichung erfolgte mit `save_version_and_deploy_private`. |
| Abruf ohne Anmeldung | **Noch nicht an der Site geprüft.** Der Abruf scheitert vorher am Netzwerkproxy der Cloud-Umgebung mit `CONNECT tunnel failed, response 403`. Das ist kein Nachweis der Anmeldesperre der Site. |

## Sites-Kennungen

- Projekt: `appgprj_6aee2773b8788191b72faeefddd89f34`
- Gespeicherte Version: `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_6e1de74f09408191863b0e9143057de9`
- Sites bestätigt für diese Version den Quellcommit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8`.

## Offene Abschlussprüfung

Die Netzwerkfreigabe der Cloud-Umgebung erlaubt die Site-Domain bisher nicht. Die Domain `waermeuebertragung-kaffee.qarri196.chatgpt.site` muss über die unterstützten Netzwerkeinstellungen freigegeben werden. Danach:

1. Die Startseite mit dem von Sites bereitgestellten Servicezugang abrufen, Antwortkopfzeilen erfassen und den Inhalt byteweise mit der Datei aus dem Merge-Commit vergleichen.
2. Den Abruf in einer getrennten Sitzung ohne Anmeldung prüfen. Die Simulation darf dabei nicht ausgeliefert werden.
3. Diesen Nachweis um die gemessenen Ergebnisse ergänzen. Bei veränderten HTML-Bytes die Veröffentlichung als nicht abgenommen melden.

Die Site bleibt bis zum ausdrücklichen Zuruf der Tutoriumsleitung auf das Eigentümerkonto beschränkt. Zum späteren Öffentlichschalten lautet der Satz: **„Schalte die Kaffee-Seite öffentlich.“** Dabei darf die Datei nicht geändert werden.
