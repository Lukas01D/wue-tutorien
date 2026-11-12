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

## Fassung 3 (08.11.2026)

**Aktueller Status: „Auf meine Anweisung vom 08.11.2026, 22:34 sind Hauptadresse und Prüfadresse öffentlich, beide mit Fassung 3.“ (Tutoriumsleitung, Europe/Berlin, CET). Fassung 3 ist seit 08.11.2026 um 22:28:14 Uhr CET (Europe/Berlin) unter der Hauptadresse veröffentlicht, Sites-Version 2. Die Sites-Einstellungen der Hauptseite sind unverändert. Auf die jüngste Anweisung der TL „nein beide für alle sichtbar“ ist die Prüfadresse seit 22:33:40 Uhr CET ebenfalls wieder öffentlich, Zugangsrevision 4. Der HTTP-Abgleich und die Live-Abnahme sind weiterhin offen. Die folgenden Abschnitte dokumentieren den Ablauf.**

Erstveröffentlichung: Privat bereitgestellt am 08.11.2026 um 22:04:47 Uhr CET, gemäß V1 und `simulation/VEROEFFENTLICHUNG.md`, Abschnitt 2, Schritt 1. Die folgenden Angaben zur Eigentümerbeschränkung dokumentieren diesen ursprünglichen Zustand; die Öffentlichschaltung ist am Ende dieses Abschnitts nachgewiesen.

### Quelle, Bau und Upload

| Punkt | Nachweis |
|:--|:--|
| Private Adresse | https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site |
| Quelle | Merge-Commit `85353d9a2da404b48f8238a8c42e04509c4f9aa3` auf `main`, PR #8, zusammengeführt von der TL am 08.11.2026 um 21:34:59 Uhr CET. Der Merge enthält den Zweig `claude/kaffee-simulation-v3-qw4zb2` bis einschließlich `769c155`. Abstammung mit `git merge-base --is-ancestor` geprüft. |
| Aktualisierung | `git fetch origin`, `git checkout main`, `git pull --ff-only origin main`; HEAD entspricht dem genannten Merge-Commit. |
| Datei im Repository | `simulation/site/index.html`, 177289 Bytes. SHA-256: `95cff1f24926ff60b78c458381b3a6f151d55620ec18c82f79af8a0da0049702`. |
| Bauprüfung | Beide HTML-Dateien sind bytegleich, ihre SHA-256 stimmt mit `simulation/site/BAUNACHWEIS.txt` überein. `python3 simulation/site/bauen.py --pruefen` meldet `gleich`. Das fehlende Brotli-Modul wurde dafür außerhalb des Repositorys installiert; fontTools war vorhanden. `simulation/site/` ist gegenüber dem Merge-Commit unverändert. |
| Fuß der Seite | `Stand 2026-11-08 · Version 6700332355`. Die Versionskennung sind die ersten zehn Zeichen der Quellprüfsumme `67003323553ddc9db83a8c691da1ece1828921219030654401918ed15ada9f1e`. Geprüft an den unveränderten Baukonstanten und der Fußtextvorlage; die Anzeige im ausgelieferten Browser bleibt Teil der Live-Abnahme. |
| Quelle bei Sites | Commit `040c5659d0aa820f238a72b8055654e73d793f90` auf `main` des eigenen Site-Quellrepositorys. Remote-HEAD nach dem Push und `get_site_version.source.commit_sha` stimmen mit diesem Commit überein. |
| Hochgeladene Datei | `dist/index.html`, unverändert aus dem Git-Objekt des Merge-Commits übernommen. 177289 Bytes, SHA-256 `95cff1f24926ff60b78c458381b3a6f151d55620ec18c82f79af8a0da0049702`. Bytegleichheit zwischen Git-Objekt, Site-Quellcommit, Datei und Upload-Archiv vor dem Speichern geprüft. |
| Umfang | Das Upload-Archiv enthält nur `dist/index.html` und `.openai/hosting.json` mit der Kennung der privaten Prüf-Site und `static.directory=dist`. Keine zusätzlichen Skripte, Seitenressourcen, Analyse- oder Zähldienste. |
| Sites-Version | Version 1 der privaten Prüf-Site, gespeichert und veröffentlicht mit `save_version_and_deploy_private`. Deployment `appgdep_6af0e3e0d0288191a54f0cde1f63d494`, Status `succeeded`, Zeitstempel `2026-11-08T21:04:47.311479+00:00`. |
| Ausgelieferte Datei | Noch nicht gemessen. Erwartet werden 177289 Bytes und SHA-256 `95cff1f24926ff60b78c458381b3a6f151d55620ec18c82f79af8a0da0049702`. Die nachgewiesene Bytegleichheit von Quelle und Upload ersetzt diesen Live-Abgleich nicht. |
| Antwortkopfzeilen der Site | Noch nicht ermittelt. Der direkte Abruf der privaten Adresse aus dieser Umgebung scheitert bereits am Netzwerkproxy mit `curl: (56) CONNECT tunnel failed, response 403`, HTTP-Status des Zielabrufs `000`. Die empfangene CONNECT-Antwort lautet `HTTP/1.1 403 Forbidden`, `server: envoy`, `content-type: text/plain`, Datum `Sun, 08 Nov 2026 21:05:16 GMT`. Das sind Proxy-Kopfzeilen, keine Antwort der Simulation. Keine Aussage über Veränderungen durch Sites oder den tatsächlichen Abruf ohne Anmeldung möglich. |

### Zugang und unveränderte öffentliche Fassung 2

Die verfügbaren Sites-Werkzeuge bieten keine getrennte private Versionsvorschau für die bestehende öffentliche Site. Deshalb wurde die in V1 vorgesehene eigene private Prüf-Site angelegt. `get_site` bestätigt nach der Veröffentlichung:

- Projekt `appgprj_6af0e3516aac8191b5565eaaaa0ad8cf`, Rolle des aktuellen Kontos `owner`.
- `access_mode=custom`, `access_policy.access_mode=custom`, Revision 1 vom `2026-11-08T21:02:11.890444+00:00`.
- Genau ein zugelassenes Konto mit Rolle `owner`, keine weiteren Bearbeiter, Gruppen oder externen Besucher. Der private Veröffentlichungsaufruf hat die Eigentümerbeschränkung zusätzlich serverseitig geprüft.
- Gespeicherte Version `appgprj_6af0e3516aac8191b5565eaaaa0ad8cf~appgver_9f0ac083627c81919e9d4fa832eb2a54`, Sites-Version 1.

Die öffentliche Site wurde ausschließlich gelesen. Vorher und nachher wurden `get_site` und `get_site_version` abgeglichen:

| Merkmal der öffentlichen Fassung 2 | Vorher und nachher identisch |
|:--|:--|
| Projekt und Adresse | `appgprj_6aee2773b8788191b72faeefddd89f34`, https://waermeuebertragung-kaffee.qarri196.chatgpt.site |
| Neueste Sites-Version | 1 |
| Versionskennung | `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_6e1de74f09408191863b0e9143057de9` |
| Quellcommit | `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8` |
| Deployment | `appgdep_6aee28079650819197a2607341778eed` |
| Gespeichertes Archiv | `sha256:ba816817fd9ad41dadbb76b4535091ef06d5840345d03180b926d2a86789fe52`, 440320 Bytes, zwei Dateien |
| Zugang | Öffentlich, unveränderte vollständige Zugangsrichtlinie, Revision 2 vom `2026-11-06T19:25:25.726484+00:00` |

### Prüfgrenzen und Übergabe

Keine Abweichung an der freigegebenen HTML-Datei oder am angeordneten Zugang. Die Sites-Helferskripte waren in dieser Umgebung nicht verfügbar. Deshalb erfolgten Git-Übertragung und Tar-Verpackung direkt; Quellcommit, Remote-HEAD und Archivinhalt wurden ausdrücklich geprüft. Veröffentlichung und Zugangsprüfung erfolgten über die nativen Sites-Werkzeuge.

Offen bleiben der HTTP-Abgleich einschließlich Antwortkopfzeilen, die Live-Abnahme gemäß `simulation/VEROEFFENTLICHUNG.md`, Abschnitt 5, und die Geräteprüfung gemäß `simulation/ABNAHME_IPHONE.md`. Dafür wurde keine Netzwerkfreigabe verändert. Ein blockierter Proxy-Abruf ist weder eine erfolgreiche Inhaltsprüfung noch ein Beleg für die Anmeldesperre der privaten Site.

Die ursprüngliche Übergabe sah die Prüfung der privaten Fassung vor. Die nachfolgende erste Anweisung der TL hob die Zugangsbeschränkung auf. Bei dieser Zugangsumstellung wurde die bestehende Seite mit Fassung 2 nicht ersetzt. Der ursprüngliche Nachweis wurde auf dem eigenen Zweig `codex/kaffee-f3-veroeffentlichung` gesichert. Die Übernahme nach `main` erfolgt auf Anweisung der TL per Pull Request. `simulation/LIVE_ABNAHME.md` wird durch die spätere unabhängige Live-Abnahme ergänzt.

### Öffentlichschaltung beider Kaffee-Seiten

Neue Anweisung der TL vom 08.11.2026: **„beide öffentlich für alle sichtbar bitte“**. Damit entfällt die Eigentümerbeschränkung aus V1 für die Prüf-Site. Die beiden Fassungen sollen unter ihren jeweiligen Adressen öffentlich zugänglich sein.

Umgesetzt mit `update_site_access(project_id="appgprj_6af0e3516aac8191b5565eaaaa0ad8cf", access_mode="public")`. Bestätigt wurden Revision 2 und der Zeitstempel `2026-11-08T21:09:29.495827+00:00` (22:09:29 Uhr CET). Anschließend wurden beide Seiten mit `get_site` erneut geprüft:

| Seite | Bestätigter Zugang |
|:--|:--|
| Fassung 3: https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site | `access_mode=public`, `access_policy.access_mode=public`, Revision 2 vom 08.11.2026; Sites-Version 1 unverändert. |
| Fassung 2: https://waermeuebertragung-kaffee.qarri196.chatgpt.site | Bereits öffentlich, erneut bestätigt: `access_mode=public`, `access_policy.access_mode=public`, Revision 2 vom 06.11.2026; Sites-Version 1 unverändert. |

Es wurde ausschließlich der Zugang der Prüf-Site geändert. Keine neue Version, kein Austausch einer Datei, keine erneute Veröffentlichung. Die dokumentierten Grenzen des direkten HTTP-Abrufs bleiben bestehen; die öffentliche Zugangsrichtlinie beider Seiten ist durch Sites bestätigt.

### Hauptadresse durch Fassung 3 ersetzt, Prüfadresse wieder privat

Auftrag der TL vom 08.11.2026: **„Ersetze die Kaffee-Seite unter der Hauptadresse durch Fassung 3 (Quelle: main, Merge von PR #8). Keine Änderung an den Einstellungen von Sites. Danach die Prüfadresse wieder auf privat stellen. Melde Adresse, Version und Prüfsumme.“**

| Punkt | Nachweis |
|:--|:--|
| Hauptadresse | https://waermeuebertragung-kaffee.qarri196.chatgpt.site |
| Quelle | `main`, Merge von PR #8: `85353d9a2da404b48f8238a8c42e04509c4f9aa3`. Vor der Übertragung erneut `git fetch origin main`, `git checkout main`, `git pull --ff-only origin main`; HEAD entspricht genau diesem Merge. |
| Bauprüfung | `simulation/site/index.html` und `Kaffee_Simulation.html` stimmen mit `BAUNACHWEIS.txt` überein. `bauen.py --pruefen` meldet erneut `gleich`. Keine Änderungen an `simulation/site/`. |
| Datei und Prüfsumme | 177289 Bytes. SHA-256 `95cff1f24926ff60b78c458381b3a6f151d55620ec18c82f79af8a0da0049702`. Git-Objekt aus dem Merge, Site-Quellcommit, `dist/index.html` und Inhalt des Upload-Archivs sind bytegleich. |
| Bauversion im Seitenfuß | `6700332355`, Stand `2026-11-08`. |
| Site-Quellcommit | `4519d7eca09fb61b1d6756b01874dce943703d95`, auf `main` des vorhandenen Quellrepositorys der Hauptseite gepusht. Remote-HEAD und `get_site_version.source.commit_sha` abgeglichen. Gegenüber der bisherigen Version änderte sich ausschließlich `dist/index.html`. |
| Hosting-Konfiguration | `.openai/hosting.json` ist bytegleich mit dem bisherigen Site-Quellcommit `28c5d5eee41085987cf73b1ad8317dbe2bdcd7f8`. Bestehende Projektkennung und `static.directory=dist` unverändert. Das Archiv enthält nur diese Konfiguration und `dist/index.html`. |
| Sites-Version | **2**, gespeichert mit `save_site_version`, anschließend mit `deploy_site_version` veröffentlicht. Versionskennung `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_8bd4d1b9fce48191bd9bac1ec3b60b31`. |
| Veröffentlichung | Deployment `appgdep_6af0e9620f58819187d7f70e85526b08`, Status `succeeded`, `2026-11-08T21:28:14.444041+00:00` (22:28:14 Uhr CET). |
| Sites-Einstellungen der Hauptseite | Vorher und nachher identisch: Titel, Beschreibung, URL-Slug, Auth-Client, Remix-Einstellung, BYOP-Einstellung und vollständige Zugangsrichtlinie. Weiterhin `access_mode=public`, Zugangsrevision 2 vom 06.11.2026. Keine Einstellungen geändert, keine Tunnelbindungen angegeben, keine Laufzeitvariablen geändert; Deployment mit `env_set_revision=0`. |
| HTTP-Auslieferung | Der erneute direkte Abruf der Hauptadresse ist vom Netzwerkproxy blockiert: `curl: (56) CONNECT tunnel failed, response 403`, HTTP-Zielstatus `000`. Die genannte SHA-256 ist für Quelle und Upload nachgewiesen. Bytes, SHA-256 und Antwortkopfzeilen der tatsächlichen HTTP-Auslieferung bleiben extern zu prüfen. |

Erst nach dem erfolgreichen Deployment der Hauptseite wurde die Prüfadresse wieder privat gestellt: `update_site_access(project_id="appgprj_6af0e3516aac8191b5565eaaaa0ad8cf", access_mode="custom")`, bestätigt mit Revision 3 vom `2026-11-08T21:28:30.270811+00:00` (22:28:30 Uhr CET). Der anschließende `get_site`-Abruf bestätigt `custom` und genau ein zugelassenes Konto mit Rolle `owner`, keine weiteren Bearbeiter, Gruppen oder externen Besucher. Die Prüf-Site behält ihre bisherige Datei und Sites-Version 1 unter https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site.

Abweichungen: Keine an der freigegebenen Datei oder an den Sites-Einstellungen der Hauptseite. Offen bleibt der durch den Netzwerkproxy verhinderte HTTP-Live-Abgleich. Es wurde keine Netzwerkfreigabe verändert. Der ursprüngliche Nachweis liegt auf `codex/kaffee-f3-veroeffentlichung`; die Übernahme nach `main` erfolgt auf Anweisung der TL per Pull Request.

### Letzte Zugangsanweisung: beide Adressen öffentlich

Die TL hat anschließend klargestellt: **„nein beide für alle sichtbar“**. Damit ist die zuvor angeordnete Rückstellung der Prüfadresse auf privat aufgehoben.

Umgesetzt am 08.11.2026 um 22:33:40 Uhr CET mit `update_site_access(project_id="appgprj_6af0e3516aac8191b5565eaaaa0ad8cf", access_mode="public")`, Zugangsrevision 4, Zeitstempel `2026-11-08T21:33:40.680694+00:00`. Anschließende `get_site`-Abrufe bestätigen für beide Adressen `access_mode=public` und `access_policy.access_mode=public`:

- Hauptadresse: https://waermeuebertragung-kaffee.qarri196.chatgpt.site, Fassung 3, Sites-Version 2, unveränderte Zugangsrevision 2.
- Prüfadresse: https://waermeuebertragung-kaffee-pruefung.qarri196.chatgpt.site, Fassung 3, Sites-Version 1, Zugangsrevision 4.

Nur der Zugang der Prüfadresse wurde geändert. Dateien, Prüfsummen, gespeicherte Versionen und Deployments bleiben unverändert.

## Fassung 3, 100 ml und 45 min

Veröffentlicht am **10.11.2026 um 12:58:04 Uhr CET (Europe/Berlin)** unter der bestehenden Hauptadresse, **Sites-Version 3**, öffentlich. Grundlage ist `simulation/VEROEFFENTLICHUNG.md` auf dem Merge von PR #13. Quelle, Bau, Site-Quellcommit und Upload sind bytegleich geprüft. Der HTTP-Abgleich bleibt offen, weil der Umgebungsproxy den Abruf vor Erreichen der Site blockiert.

### Quelle, Bau und Veröffentlichung

| Punkt | Nachweis |
|:--|:--|
| Adresse | https://waermeuebertragung-kaffee.qarri196.chatgpt.site |
| Quelle | Merge-Commit auf `main`: `14c9d8e622397c31210d9f32c7610495c867df68`, PR #13, `claude/kaffee-sim-100ml-45min`, zusammengeführt am 10.11.2026 um 12:51:48 Uhr CET. Zweiter Elterncommit: `798d764650aa88bd92fb811c34be5695c63c217c`. |
| Aktualisierung | `git fetch origin`, `git checkout main`, `git pull --ff-only origin main`. HEAD entspricht dem genannten Merge-Commit. Keine Datei aus einem Arbeitszweig, aus `ergebnisse/kaffee/` oder aus `simulation/f3_entwurf/` verwendet. |
| Datei im Repository | `simulation/site/index.html`, **179395 Bytes**, SHA-256 **`e8ae197debea70f018cbbbfd5d2f56afb30e36df894166544fee1f6e6d6c35c7`**. |
| Bauprüfung | `index.html` und `Kaffee_Simulation.html` sind bytegleich; beide SHA-256 stimmen mit `simulation/site/BAUNACHWEIS.txt` überein. `python3 simulation/site/bauen.py --pruefen` meldet `gleich`. Dafür wurde das fehlende Python-Modul Brotli 1.2.1 ausschließlich unter `/tmp/kaffee-veroeffentlichung-python` installiert und über `PYTHONPATH` eingebunden; fontTools war vorhanden. `simulation/site/` ist gegenüber dem Merge unverändert. |
| Seitenfuß | `Stand 2026-11-10 · Version 425de0298b`. Die Baukonstanten und die Fußtextvorlage entsprechen dem Baunachweis, Quellprüfsumme `425de0298be5d98a944d686d89e17e09c275af9e141e4520bddd89875326e6f0`. Die Anzeige im ausgelieferten Browser bleibt Teil der Live-Abnahme. |
| Werte | Die freigegebene HTML-Datei enthält die Standardwerte `VM_ml: 100` und `tZ: 45`. |
| Quelle bei Sites | Commit `99ea2b7dcba5ddc1ba4942d59e9fc17303f1d289` auf `main` des bestehenden Site-Quellrepositorys. Push erfolgreich; anschließend Remote-HEAD mit `git ls-remote` abgeglichen. `save_site_version.source.commit_sha` bestätigt denselben Commit. |
| Übertragene Datei | `dist/index.html`, unverändert aus der freigegebenen Repository-Datei übernommen: 179395 Bytes, SHA-256 `e8ae197debea70f018cbbbfd5d2f56afb30e36df894166544fee1f6e6d6c35c7`. Git-Objekt des Merge-Commits, lokale HTML-Datei, Site-Quellcommit und HTML im Upload-Archiv sind bytegleich. |
| Umfang | Genau eine Startseite `index.html`. Das Archiv enthält ausschließlich `dist/index.html` und `.openai/hosting.json`. Keine zusätzlichen Skripte, Analyse- oder Zähldienste. Die Hosting-Konfiguration wurde unverändert aus dem bisherigen Site-Quellcommit übernommen: bestehende Projektkennung, `static.directory=dist`. |
| Gespeichertes Archiv | Sites bestätigt zwei Dateien, 184320 Bytes im gespeicherten Tar-Archiv und `sha256:a953d05541ca8aeeaca1780425dbd93c83a898573d5351e88519a6cc23135550`. Das lokale komprimierte Upload-Archiv hatte 80481 Bytes und SHA-256 `ac674d8b45b56f76abee9fbfabf957f800ced9ecfd44f75c0d22b253106ef619`. |
| Sites-Version | **3**, gespeichert mit `save_site_version`, veröffentlicht mit `deploy_site_version`. Versionskennung: `appgprj_6aee2773b8788191b72faeefddd89f34~appgver_16771bac8a0c8191a0aa9424d4f45844`. |
| Veröffentlichung | Projekt `appgprj_6aee2773b8788191b72faeefddd89f34`, Deployment `appgdep_6af306c0175c8191a12e5796699e800e`, Status **`succeeded`**, Zeitstempel `2026-11-10T11:58:04.370578+00:00`. |
| Öffentlicher Zugang | Vorher und nachher mit `get_site` bestätigt: `access_mode=public`, `access_policy.access_mode=public`, unveränderte Revision 2 vom `2026-11-06T19:25:25.726484+00:00`. Nachher bestätigt Sites die Hauptadresse und `latest_version_number=3`. Keine private Zwischenstufe und keine neue Prüf-Site. |
| Übrige Einstellungen | Titel, Beschreibung, URL-Slug, Auth-Client, Remix-Einstellung, BYOP-Einstellung und vollständige Zugangsrichtlinie sind vorher und nachher identisch. Keine Laufzeitvariablen oder Tunnelbindungen geändert, `env_set_revision=0`. Die vorhandene Prüfadresse wurde nicht verändert. |

### HTTP-Auslieferung und Prüfgrenze

Der Abruf der Hauptadresse mit `curl --compressed --location` am 10.11.2026 um 12:58:17 Uhr CET scheitert bereits beim Verbindungsaufbau am Umgebungsproxy: `curl: (56) CONNECT tunnel failed, response 403`, HTTP-Zielstatus `000`, 0 übertragene Bytes. Der Proxy antwortet:

```text
HTTP/1.1 403 Forbidden
content-length: 16
content-type: text/plain
date: Tue, 10 Nov 2026 11:58:17 GMT
server: envoy
connection: close
```

Das sind ausschließlich Proxy-Kopfzeilen, keine Antwortkopfzeilen der Site. **Bytes und SHA-256 der ausgelieferten Datei sind nicht gemessen.** Erwartet werden 179395 Bytes und SHA-256 `e8ae197debea70f018cbbbfd5d2f56afb30e36df894166544fee1f6e6d6c35c7`. Auch die Antwortkopfzeilen der Site, die Abwesenheit eingefügter Skripte und der tatsächliche Abruf ohne Anmeldung bleiben live zu prüfen. Der erfolgreiche öffentliche Sites-Deploy und die geprüften Upload-Bytes ersetzen diesen HTTP-Abgleich nicht. Keine Netzwerkfreigabe verändert.

### Abweichungen und Übergabe

Keine Abweichung an der freigegebenen Datei, der bestehenden Adresse oder dem öffentlichen Zugang. Die Sites-Helferskripte waren in dieser Umgebung nicht verfügbar. Wie bei der vorherigen Veröffentlichung erfolgten Git-Übertragung und Tar-Verpackung direkt, mit ausdrücklichem Abgleich von Quellcommit, Remote-HEAD und Archivinhalt. Zugangsdaten wurden ausschließlich im Arbeitsspeicher und über eine verdeckte Standardeingabe verwendet, nicht in Dateien oder Git-Konfiguration gespeichert. Veröffentlichung und Zugangsnachweis erfolgten über die nativen Sites-Werkzeuge.

Offen bleiben der vom Proxy blockierte HTTP-Abgleich, die Live-Abnahme durch Claude nach `simulation/VEROEFFENTLICHUNG.md`, Abschnitt 5, und der Gerätetest der Tutoriumsleitung nach `simulation/ABNAHME_IPHONE.md`. Dieser Nachweis wird auf dem eigenen Zweig `codex/kaffee-100ml-45min-veroeffentlichung` gesichert und gepusht. Gemäß Veröffentlichungsauftrag wird kein Pull Request angelegt.
